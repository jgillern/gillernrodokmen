#!/usr/bin/env python3
"""Fulltextové hledání v České digitální knihovně (Kramerius 7, sdružuje NK, MZK, KNAV …).
Použití: kramerius7.py 'DOTAZ' [počet] [rok_od] [rok_do]
  např. kramerius7.py '"von Gillern"' 50 1800 1870
Vypíše rok, titul, PID stránky a úryvek textu kolem nálezu. Síť jde přes brzdu slusne.py."""
import sys, json, urllib.request, urllib.parse
import os as _os, sys as _sys; _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import slusne  # noqa: E402,F401 – brzda (společný limit dotazů)
for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8", errors="replace")
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    sys.exit(__doc__)
q = sys.argv[1]
rows = sys.argv[2] if len(sys.argv) > 2 else "30"
fq = "model:page"
if len(sys.argv) > 4:
    fq += f" AND date_range_start.year:[* TO {sys.argv[4]}] AND date_range_end.year:[{sys.argv[3]} TO *]"
p = {"q": q, "defType": "edismax", "qf": "text_ocr", "fq": fq, "rows": rows,
     "fl": "pid,root.title,root.pid,date.str,page.number,own_parent.title,accessibility",
     "hl": "true", "hl.fl": "text_ocr", "wt": "json"}
u = "https://api.ceskadigitalniknihovna.cz/search/api/client/v7.0/search?" + urllib.parse.urlencode(p)
d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": slusne.UA}), timeout=90))
print("nalezeno", d["response"]["numFound"])
hl = d.get("highlighting", {})
for x in d["response"]["docs"]:
    h = " | ".join(hl.get(x["pid"], {}).get("text_ocr", []))[:600].replace("\n", " ")
    print("-", x.get("date.str"), "|", str(x.get("root.title"))[:70], "|", str(x.get("own_parent.title", ""))[:30],
          "| str.", x.get("page.number"), "|", x["pid"], "|", x.get("accessibility", ""))
    if h:
        print("   ", h)
