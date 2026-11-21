#!/usr/bin/env python3
"""Úryvky kolem hledaného jména ze všech stránek České digitální knihovny – bez stahování celých stránek.
Použití: kramerius7_uryvky.py SLOZKA 'DOTAZ'
Bere výsledky hledání po 100 se zvýrazněním (highlighting), takže na ~6000 stránek stačí ~60 dotazů.
Výstup: SLOZKA/uryvky.jsonl (pid, titul, rok, strana, přístupnost, úryvky). Pokračuje po zastavení brzdou."""
import sys, os, json, urllib.request, urllib.parse
import os as _os, sys as _sys; _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import slusne  # noqa: E402 – brzda
for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8", errors="replace")
if len(sys.argv) < 3:
    sys.exit(__doc__)
slozka, dotaz = sys.argv[1], sys.argv[2]
os.makedirs(slozka, exist_ok=True)
API = "https://api.ceskadigitalniknihovna.cz/search/api/client/v7.0/search?"
STAV, OUT = os.path.join(slozka, "uryvky_stav.json"), os.path.join(slozka, "uryvky.jsonl")
st = json.load(open(STAV)) if os.path.exists(STAV) else {"dotaz": dotaz, "start": 0, "celkem": None}
if st["dotaz"] != dotaz:
    sys.exit("uryvky_stav.json patří k jinému dotazu")
while st["celkem"] is None or st["start"] < st["celkem"]:
    p = {"q": dotaz, "defType": "edismax", "qf": "text_ocr", "fq": "model:page", "rows": "100",
         "start": str(st["start"]), "sort": "pid asc", "hl": "true", "hl.fl": "text_ocr", "hl.snippets": "5",
         "fl": "pid,root.title,date.str,page.number,own_parent.title,accessibility,root.pid", "wt": "json"}
    req = urllib.request.Request(API + urllib.parse.urlencode(p), headers={"User-Agent": slusne.UA})
    d = json.loads(urllib.request.urlopen(req, timeout=120).read())
    st["celkem"] = d["response"]["numFound"]
    hl = {k.split("!")[-1]: v for k, v in d.get("highlighting", {}).items()}   # klíče bývají „root_pid!pid“ (změna API 2026)
    with open(OUT, "a", encoding="utf-8") as f:
        for x in d["response"]["docs"]:
            x["uryvky"] = hl.get(x["pid"], {}).get("text_ocr", [])
            f.write(json.dumps(x, ensure_ascii=False) + "\n")
    st["start"] += 100
    json.dump(st, open(STAV + ".tmp", "w")); os.replace(STAV + ".tmp", STAV)
    print(f"úryvky: {min(st['start'], st['celkem'])}/{st['celkem']}", flush=True)
print("HOTOVO", flush=True)
