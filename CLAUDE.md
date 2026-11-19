# Projekt rodokmenu

Tohle je projekt rodokmenu vedený skillem **rodokmen**. Na začátku každé konverzace:
1. Načti skill `rodokmen` (pokud ještě není načtený).
2. Přečti `data/STAV.md` – stav, pravidla a co je rozpracované – a konec `data/research_log.md`.
3. Pokračuj tam, kde se skončilo. Komunikuj česky, stručně a srozumitelně pro člověka bez zkušeností s genealogií a programováním.
4. Síť na weby archivů jen přes brzdu `tools/slusne.py` (vlastní skripty, curl), i v zadání pomocníků – viz skill, „Šetrně k archivům“.
   **Výjimka (výslovně povolil Jan 19. 11. 2026, bez časového omezení):** když nástroj `rodokmen`/`slusne.py` web archivu blokuje, ale Claude ho technicky umí číst, smí k němu přistupovat i mimo nástroj – jako „Claude-User“ (vlastním jménem, ne přestrojený za jiný prohlížeč), pomalu (aspoň 5–10 s mezi stránkami, nic souběžně, žádné stahování celých knih). Soubor pravidel webu (`robots.txt`) smí číst vždy. Hranice: co archiv sám zakazuje automatickým klientům obecně nebo Claudovi (robots.txt pro `*` / `Claude-User` / `ClaudeBot`, opakované 403/429, podmínky užití), se nedělá – např. eBadatelna SOA Praha zakazuje všem robotům `/d/` a `/a/` (snímky a popisy), takže snímky matrik dál čte Jan.
5. Co by šlo ve skillu zlepšit (chyby nástrojů, nové archivy, nápady), zapisuj do `poznamky_pro_skill.md` – viz skill, sekce „Poznámky pro správce skillu“.
