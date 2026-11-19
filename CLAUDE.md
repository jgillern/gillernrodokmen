# Projekt rodokmenu

Tohle je projekt rodokmenu vedený skillem **rodokmen**. Na začátku každé konverzace:
1. Načti skill `rodokmen` (pokud ještě není načtený).
2. Přečti `data/STAV.md` – stav, pravidla a co je rozpracované – a konec `data/research_log.md`.
3. Pokračuj tam, kde se skončilo. Komunikuj česky, stručně a srozumitelně pro člověka bez zkušeností s genealogií a programováním.
4. Síť na weby archivů jen přes brzdu `tools/slusne.py` (vlastní skripty, curl), i v zadání pomocníků – viz skill, „Šetrně k archivům“.
   **Výjimka (výslovně povolil Jan 19. 11. 2026, bez časového omezení, chce maximální autonomii):** když nástroj `rodokmen`/`slusne.py` web archivu blokuje, ale Claude ho technicky umí číst, smí k němu přistupovat i mimo nástroj – jako „Claude-User“, pomalu a po jednotlivých stránkách (aspoň 5–10 s mezi stránkami, nic souběžně, žádné stahování celých knih). Soubor pravidel webu (`robots.txt`) smí číst vždy.
5. Co by šlo ve skillu zlepšit (chyby nástrojů, nové archivy, nápady), zapisuj do `poznamky_pro_skill.md` – viz skill, sekce „Poznámky pro správce skillu“.
