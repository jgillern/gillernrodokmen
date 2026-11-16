# Stav rodokmenu a pravidla práce

Tento soubor je vstupní bod. Po každém restartu (nová konverzace, zkrácený kontext) ho Claude čte jako první,
pak konec `research_log.md` a sekci „Rozpracováno“.

## Pro koho
- Výchozí osoba: Jan Gillern (rok a místo narození doplnit). Cíl: rodokmen co nejdál do minulosti.
- Kdo s Claudem pracuje a jak chce komunikovat: Jan sám, česky; pracuje v cloudové relaci claude.ai (archivy a Wikipedie zatím blokované sítí prostředí).

## Kde co je
| Soubor | Obsah |
|---|---|
| `data/osoby.py` | Přímí předci podle Kekulého čísla + rody, boční příbuzní, otevřené otázky, hypotézy. |
| `data/zaznamy.json` | Každý použitý zápis z matriky (klíč = název obrázku). |
| `data/svazky.json` | Matriční svazky (archiv, signatura, odkaz). |
| `data/prepisy.json` | Přepis originálu a český překlad každého zápisu. |
| `data/zvyrazneni.json` | Rámečky – které místo výřezu čteme. |
| `data/research_log.md` | Deník VŠECH hledání, i neúspěšných. |
| `data/udaje_od_rodiny.md` | Co řekla rodina, rodinné dokumenty. |
| `data/zajimavosti.md`, `data/pribeh.md` | Texty na web. |
| `data/archivni_dotazy.md` | Co by šlo zjistit jen v archivu. |
| `data/mista.json`, `data/dokumenty.json`, `data/web.json` | Mapa, rodinné fotky a dokumenty, nastavení webu. |
| `vyrezy/`, `zdroje/` | Výřezy zápisů pro web (1800 px) a v plném rozlišení. |
| `dokumenty/` | Rodinné dokumenty a fotky od uživatele (originály). |
| `pracovni/` | Pracovní soubory (stažené stránky, kontrolní obrázky) – nejdou na web. |
| `web/` | Rodinný web. `cd web && npm run nahled` (data + sestavení + náhled); po změně dat stačí `npm run data && npm run build`. |

## Pravidla
1. Než něco ohlásím jako nové, prohledám `osoby.py`, `zaznamy.json` a `research_log.md` (jméno, místo, rok).
2. Údaj je „doloženo“ (doc) jen tehdy, když jsem ho přečetl přímo na snímku. Čtení od pomocníků ověřím sám.
3. Každé hledání (i neúspěšné) zapíšu do `research_log.md`.
4. Nejistá čtení označím (?) – nic nedomýšlím.
5. Ke každému novému zápisu: výřez (`tools/vyrez.py`), rámeček (`tools/ramecek.py`) a přepis s překladem.
6. Po změně dat spustím `python3 -I tools/kontrola.py`.

## Rozpracováno (aktualizovat průběžně)
- Fáze 1 – rozhovor s rodinou: známe rodiče a prarodiče (jen jména). Chybí roky, místa, rodná příjmení babiček, pradědečkové.
- Síť funguje (16. 11. 2026), ale de.wikipedia.org odmítá dotazy z cloudu (429, 2×) – zastaveno do 11:02 UTC; případně ať Jan text stránky vloží do chatu.
- Gillernové (jméno je vzácné): v Krameriu nalezena česká lesnická větev u Orlíku/Vorlíka (Augustin, Čeněk, Vincenc, Bedřich
  z Gillernů, 1872–1903) – viz research_log č. 4–5. Hypotéza: děda Augustýn je jejich potomek (jméno Augustin se opakuje,
  student „Gillern Augu…“ v Písku 1936). NEOVĚŘENO – chybí rok a místo narození dědy Augustýna; zeptat se rodiny.
- Další kroky: matriky farností u Orlíku (Lavičky → fara Kostelec n. Vlt.? / Zbenice; Vorlík → Orlík n. Vlt.), SOA Praha a
  SOA Třeboň jen v prohlížeči; vyhledání hrobu Gillern na pražských hřbitovech (mapy.hrbitovy.cz) v prohlížeči.
- Beranovi (matčina linie): Josef Beran * 3. 6. 1910 Velká Jesenice (okr. Náchod) – matrika N po 10.1906 v ARONu není;
  sňatek rodičů (Josef Beran × Emilie Kozáková) v matrice O Velká Jesenice 1871–1906 není. Další krok: narození Josefa Berana st.
  (asi 1875–1888) v matrice N Velká Jesenice 1880–1906 (apu 89ef95c3) – ale bez dalšího údaje hrozí záměna, nejdřív zjistit víc.
- Slunečkovi: Ludmila Slunečková * 7. 4. 1916 Buková (část obce Pravonín, fara Pravonín, SOA Praha – jen ručně, Jan posílá snímky).
- Sňatek Beran × Slunečková: v knize Pravonín 26 (jen obec Pravonín) 5/1934–2/1937 není. Fara vedla knihy zřejmě po obcích
  s průběžným číslováním (č. 1 chybí 1935–37) → hledat v knize oddaných pro Bukovou 1935–37 (Jan).
- Myslíkovi: Vladimír Myslík * 6. 5. 1930 Zdíkov (okr. Prachatice) – potřeba jména jeho rodičů.
