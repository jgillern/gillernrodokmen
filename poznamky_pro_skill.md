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
- Doplnění: i s popisným User-Agentem (-A) Wikipedie vrátila 429 hned na první dotaz po vypršení stopky → spíš přiškrcená
  sdílená IP cloudového prostředí než UA. V cloudu Wikipedii raději nechat přečíst uživatele / vložit text do chatu.
- eBadatelna SOA Praha přes Playwright v cloudové relaci: úvodní stránka šla, ale vyhledávání ve formuláři zamítl klasifikátor
  oprávnění (auto mode, „Destructive or Unwanted Actions“) – zřejmě kvůli zákazu skriptů archivem. Ve skillu počítat s tím, že
  v cloudu SOA Praha čte uživatel sám a posílá screenshoty / odkazy na snímky.
- Když uživatel listuje v eBadatelně sám: „strana“ v citacích (pag.) je ručně psané číslo v rohu knihy, ne číslo snímku
  v prohlížeči – uživatele to mate. Ve skillu doporučit: vždy říct „číslo v horním rohu stránky“ + přibližný snímek
  (z poměru: jeden snímek = dvoustrana, u pravonínských knih s jedním číslem na dvoustranu) a požádat o URL z adresního řádku.
- eBadatelna: našeptávač lokalit nenajde menší osady (Nakvasovice), i když jsou v popisu knih. Fungovalo hledat obec fary
  („Zhoř – obec Čechtice – okres Benešov“) podle údaje ze zápisu („křestní list ze Zhoře“). Ve skillu zmínit.
- SOA Třeboň (digi.ceskearchivy.cz): uživatel může stáhnout snímek jako PDF („Print to PDF“ z exportu) – hlavička obsahuje
  trvalý odkaz https://digi.ceskearchivy.cz/<id>/<snímek>, název knihy a číslo snímku. Číst přes pdftoppm -r 200.
- Web: přidal jsem „Cestu časem“ na úvodní stránku (web/src/pages/index.astro + styly v global.css), data v data/web.json
  pod klíčem `casova_osa` (období → události s rokem, nadpisem, textem, odkazem na osobu, štítkem strany/rodu, příznakem
  „historie“ pro dobové souvislosti) a `podtitul` pod nadpisem. Uživatel to chtěl podle webu kolegy (stejný skill) –
  stálo by za to mít to ve skillu jako standard, ideálně generované z osob/zápisů automaticky.
