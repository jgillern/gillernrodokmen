#!/usr/bin/env python3
"""Postupný sběr všech stránek České digitální knihovny (Kramerius 7), kde je zadané jméno.
Použití: kramerius7_sber.py SLOZKA 'DOTAZ'      (např. pracovni/k7 'Gillern OR Giller OR Gillernů')
Fáze 1 projde výsledky hledání (po 100), fáze 2 stáhne text (OCR) každé veřejné stránky a uloží
úryvky kolem jména do SLOZKA/nalezy.jsonl. Stav je v SLOZKA/stav.json – po zastavení brzdou
(slusne.py) stačí spustit znovu a pokračuje, kde skončil. Neveřejné stránky jen zapíše (text nestahuje)."""
import sys, os, json, re, time, urllib.request, urllib.parse
import os as _os, sys as _sys; _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import slusne  # noqa: E402 – brzda
for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8", errors="replace")
if len(sys.argv) < 3:
    sys.exit(__doc__)
slozka, dotaz = sys.argv[1], sys.argv[2]
os.makedirs(slozka, exist_ok=True)
API = "https://api.ceskadigitalniknihovna.cz/search/api/client/v7.0/"
STAV = os.path.join(slozka, "stav.json")
NALEZY = os.path.join(slozka, "nalezy.jsonl")
st = json.load(open(STAV)) if os.path.exists(STAV) else {"dotaz": dotaz, "start": 0, "celkem": None, "stranky": {}, "hotovo": []}
if st["dotaz"] != dotaz:
    sys.exit("stav.json patří k jinému dotazu – použij jinou složku")
slova = [w for w in re.findall(r"\w+", dotaz) if w not in ("OR", "AND", "NOT")]
vzor = re.compile("|".join(re.escape(w) for w in sorted(slova, key=len, reverse=True)), re.I)


def uloz():
    tmp = STAV + ".tmp"
    json.dump(st, open(tmp, "w"), ensure_ascii=False)
    os.replace(tmp, STAV)


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": slusne.UA})
    return urllib.request.urlopen(req, timeout=90).read()


# Fáze 1 – seznam stránek
while st["celkem"] is None or st["start"] < st["celkem"]:
    p = {"q": dotaz, "defType": "edismax", "qf": "text_ocr", "fq": "model:page", "rows": "100",
         "start": str(st["start"]), "sort": "pid asc",
         "fl": "pid,root.title,date.str,page.number,own_parent.title,accessibility,root.pid", "wt": "json"}
    d = json.loads(get(API + "search?" + urllib.parse.urlencode(p)))
    st["celkem"] = d["response"]["numFound"]
    for x in d["response"]["docs"]:
        st["stranky"].setdefault(x["pid"], {k: x.get(k) for k in ("root.title", "date.str", "page.number", "own_parent.title", "accessibility", "root.pid")})
    st["start"] += 100
    uloz()
    print(f"hledání: {min(st['start'], st['celkem'])}/{st['celkem']}", flush=True)

# Fáze 2 – texty stránek
hotovo = set(st["hotovo"])
zbyva = [pid for pid, m in st["stranky"].items() if pid not in hotovo]
print(f"texty: hotovo {len(hotovo)}, zbývá {len(zbyva)}", flush=True)
for i, pid in enumerate(zbyva, 1):
    m = st["stranky"][pid]
    zaznam = dict(pid=pid, **m)
    if m.get("accessibility") == "public":
        txt = get(API + f"items/{pid}/ocr/text").decode("utf-8", "replace")
        radky = txt.splitlines()
        uryvky = []
        for j, r in enumerate(radky):
            if vzor.search(r):
                uryvky.append("\n".join(radky[max(0, j - 6): j + 10]))
        zaznam["uryvky"] = uryvky
    else:
        zaznam["uryvky"] = None          # neveřejné – jen odkaz (prohlížet ve studovně / přihlášeně)
    with open(NALEZY, "a", encoding="utf-8") as f:
        f.write(json.dumps(zaznam, ensure_ascii=False) + "\n")
    st["hotovo"].append(pid)
    uloz()
    if i % 10 == 0:
        print(f"texty: {len(st['hotovo'])}/{len(st['stranky'])}", flush=True)
print("HOTOVO", len(st["hotovo"]), "stránek", flush=True)
