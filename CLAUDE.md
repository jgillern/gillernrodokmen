# Projekt rodokmenu

Tohle je projekt rodokmenu vedený skillem **rodokmen**. Na začátku každé konverzace:
1. Načti skill `rodokmen` (pokud ještě není načtený).
2. Přečti `data/STAV.md` – stav, pravidla a co je rozpracované – a konec `data/research_log.md`.
3. Pokračuj tam, kde se skončilo. Komunikuj česky, stručně a srozumitelně pro člověka bez zkušeností s genealogií a programováním.
4. Síť na weby archivů jen přes brzdu `tools/slusne.py` (vlastní skripty, curl), i v zadání pomocníků – viz skill, „Šetrně k archivům“.
   **Výjimka (výslovně povolil Jan 19. 11. 2026, bez časového omezení, chce maximální autonomii):** když nástroj `rodokmen`/`slusne.py` web archivu blokuje, ale Claude ho technicky umí číst, smí k němu přistupovat i mimo nástroj – jako „Claude-User“, pomalu a po jednotlivých stránkách (aspoň 5–10 s mezi stránkami, nic souběžně, žádné stahování celých knih). Soubor pravidel webu (`robots.txt`) smí číst vždy.
5. Co by šlo ve skillu zlepšit (chyby nástrojů, nové archivy, nápady), zapisuj do `poznamky_pro_skill.md` – viz skill, sekce „Poznámky pro správce skillu“.

## Badatelské předání z 25. 11. 2026

Po přečtení stavu otevři [platný plán pro Josefa a Maximiliána a přehled odložených témat](plan_badani_2026-11-25.md) a [ověřené výsledky a opravy profilů](data/badani/2026-11-25/README.md). Toto pořadí nahrazuje pořadí z 23.–24. listopadu. Doplňkové agenty pro projekt spouštěj vždy výslovně v modelu Sol. Astra koordinuje práci a vyhodnocuje důkazy. Dokončená zjištění průběžně zapisuj do deníku a do příslušných historických podkladů.

Na plán navazuje [druhé kolo, prameny a výřezy](data/badani/2026-11-25-kolo2/README.md). U matrik zvaž také FamilySearch. Uveď katalog, číslo filmu nebo DGS, dostupnost obrazů a skutečně přečtené roky či snímky. U knih a edic ověř Národní digitální knihovnu. Pokud se konkrétní svazek dá číst vzdáleně po přihlášení, předej čtenáři přímý odkaz a připrav přesnou stranu či heslo k ověření.
