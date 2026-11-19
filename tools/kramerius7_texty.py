#!/usr/bin/env python3
"""Stáhne text (OCR) vybraných stránek ze seznamu kramerius7_uryvky.py a uloží úryvky kolem jména.
Použití: kramerius7_texty.py SLOZKA 'VZOR' [do_roku]   (např. pracovni/k7/gillern 'Giller' 1950)
Bere jen veřejné stránky – podle pole „priorita“ (je-li v seznamu), pak nejstarší napřed. Výstup SLOZKA/texty.jsonl, pokračuje po zastavení brzdou."""
import sys, os, json, re, urllib.request, urllib.error
import os as _os, sys as _sys; _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import slusne  # noqa: E402 – brzda
for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8", errors="replace")
if len(sys.argv) < 3:
    sys.exit(__doc__)
slozka, vzor = sys.argv[1], re.compile(sys.argv[2], re.I)
do = int(sys.argv[3]) if len(sys.argv) > 3 else 9999
od = int(sys.argv[4]) if len(sys.argv) > 4 else 0
API = os.environ.get("K7_API", "https://api.ceskadigitalniknihovna.cz/search/api/client/v7.0/items/")  # např. MZK: https://api.kramerius.mzk.cz/search/api/client/v7.0/items/
OUT = os.path.join(slozka, "texty.jsonl")
hotovo = {json.loads(l)["pid"] for l in open(OUT, encoding="utf-8")} if os.path.exists(OUT) else set()


def rok(r):
    m = re.search(r"\d{4}", r.get("date.str") or "")
    return int(m.group()) if m else 0


rows = [json.loads(l) for l in open(os.path.join(slozka, "uryvky.jsonl"), encoding="utf-8")]
rows = [r for r in rows if r.get("accessibility") == "public" and max(od, 1) <= rok(r) <= do and r["pid"] not in hotovo]
rows.sort(key=lambda r: (r.get("priorita", 9), rok(r)))  # nejdřív podle priority (pole „priorita“), pak nejstarší
print(f"zbývá {len(rows)} stránek", flush=True)
for i, r in enumerate(rows, 1):
    req = urllib.request.Request(API + r["pid"] + "/ocr/text", headers={"User-Agent": slusne.UA})
    try:
        txt = urllib.request.urlopen(req, timeout=90).read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        if e.code != 404:
            raise
        r["uryvky"], r["chyba"] = None, "404 – stránka v této knihovně není"
        with open(OUT, "a", encoding="utf-8") as f:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
        continue
    radky = txt.splitlines()
    r["uryvky"] = ["\n".join(radky[max(0, j - 5): j + 8]) for j, x in enumerate(radky) if vzor.search(x)]
    with open(OUT, "a", encoding="utf-8") as f:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
    if i % 20 == 0:
        print(f"texty: {i}/{len(rows)}", flush=True)
print("HOTOVO", flush=True)
