# Poznámky pro správce skillu „rodokmen“

Sem Claude průběžně zapisuje, co by se mělo ve skillu zlepšit: chyby nástrojů, nové archivy a postupy, nápady.
Jen technické věci, žádné údaje o rodině. Nic se neposílá automaticky – když budete chtít, Claude poznámky vypíše
a vy je zkopírujete do e-mailu na sarsonj@gmail.com. Klidně připište i vlastní zkušenosti – užitečné změny autor rád
zapracuje do skillu, aby je měli i ostatní. Děkujeme!


## 16. 11. 2026 – Wikipedie odmítá curl přes slusne.py
- `python3 -I tools/slusne.py curl … https://de.wikipedia.org/w/api.php?...` vrátil hned na první dotaz HTTP 429.
  Nejspíš chybí popisný User-Agent (Wikimedia vyžaduje UA s kontaktem/názvem nástroje, obecné UA curl/python škrtí).
  Návrh: v slusne.py pro *.wikipedia.org posílat vlastní UA (např. „rodokmen-skill/1.0 (+odkaz na skill)“), nebo ve skillu
  doporučit pro Wikipedii jiný postup (WebFetch / prohlížeč).
- Skill „rodokmen“ nebyl v této cloudové relaci k dispozici (není v seznamu skillů, SKILL.md v repozitáři ani v ~/.claude);
  CLAUDE.md ho přitom vyžaduje načíst. Možná ho přidat do repozitáře (.claude/skills/rodokmen/).

## 16. 11. 2026 – Kramerius a hroby
- tools/kramerius.py vrací jen prvních N výsledků bez řazení a s krátkými úryvky. Užitečné bylo: stáhnout všechny výsledky
  najednou (rows=400) do JSON, pro veřejné stránky číst celé OCR (item/<pid>/streams/TEXT_OCR) a najít stránku podle čísla
  přes item/<root>/children (title = číslo strany). Pracovní skripty: pracovni/kramerius_vse.py, kramerius_text.py,
  kramerius_strana.py – možná zabudovat do kramerius.py jako přepínače.
- U neveřejných dokumentů (po ~1940) Kramerius vrací jen pár slov kolem hledaného výrazu (hl.fragsize nepomáhá).
- Hledání hrobů Správy pražských hřbitovů (mapy.hrbitovy.cz) neprojde kontrolou certifikátu přes curl (chybí mezicertifikát?);
  stará adresa 212.47.2.130:8080/mpo_sphw nefunguje. Pro skill: hroby v Praze jen přes prohlížeč.
