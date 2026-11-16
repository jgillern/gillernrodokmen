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
- Beranovi: V. Jesenice N 1863–1906 bez Beranů (ř. 33–34) → rodina tam přišla po 1906. Klíč: výpis z matriky N 1910
  (narození Josefa Berana 3. 6. 1910) z matričního úřadu – Jan jako pravnuk. Sňatek ve farnosti Pravonín není.
- (starší) Beranovi (matčina linie): Josef Beran * 3. 6. 1910 Velká Jesenice (okr. Náchod) – matrika N po 10.1906 v ARONu není;
  sňatek rodičů (Josef Beran × Emilie Kozáková) v matrice O Velká Jesenice 1871–1906 není. Další krok: narození Josefa Berana st.
  (asi 1875–1888) v matrice N Velká Jesenice 1880–1906 (apu 89ef95c3) – ale bez dalšího údaje hrozí záměna, nejdřív zjistit víc.
- Slunečkovi: Ludmila Slunečková * 7. 4. 1916 Buková (část obce Pravonín, fara Pravonín, SOA Praha – jen ručně, Jan posílá snímky).
- Sňatek Beran × Slunečková: v knize Pravonín 26 (jen obec Pravonín) 5/1934–2/1937 není. Fara vedla knihy zřejmě po obcích
  s průběžným číslováním (č. 1 chybí 1935–37) → hledat v knize oddaných pro Bukovou 1935–37 (Jan).
- Narození Ludmily Slunečkové: v rejstříku (Pravonín 24) chybí; svazek N 1894–1949 (asi XXVI) není v archivu, je na matričním
  úřadě (obvod Vlašim) → Jan může jako pravnuk požádat o výpis (asi s. ~240, vedle bratra? Jaroslava * 1915 s. 240).
- Pravonín 26 (O 1870–1949) je pro celou farnost, asi s oddíly po obcích; s. 101–103 = konec oddílu Pravonín → hledat oddíl
  Buková: sňatek Beran × Slunečková 1935–37 a Sluneček × Svatková asi 1912–15 (Jan).
- Sňatek Beran × Slunečková ve farnosti Pravonín není (Pravonín 5/1934–2/1937, Buková 1926–1945). Další: Pravonín 26 s. 104
  (Pravonín od 2/1937 – sňatek po narození Milady?); jinak jinde (Velká Jesenice, Praha, civilně).
- DOLOŽENO (16. 11.): sňatek František Sluneček × Ludmila Svatková 12. 9. 1914 Pravonín (Pravonín 26 s. 194) a narození
  Ludmily Svatkové 18. 10. 1893 Buková 5 (Pravonín 21 s. 263). Rodiče: Alois Sluneček × Josefa Píšová(?) (Tisek 17 / Buková 8);
  Jan Svatek × Marie Bezkočková (Buková 5); prarodiče František Svátek ze Bzové 1 (okr. Mladá Vožice → SOA Třeboň),
  Jan Bezkočka z Vitína 8 (okr. Sedlčany) × Marie Zelenková z Nechvalic.
- DOLOŽENO: narození Františka Slunečka 27. 11. 1888 Tisek 17 (Pravonín 21 s. 298 = snímek 290); prarodiče František Sluneček
  (obuvník, Jeníkov) × Anna Musilová; Jan Píša (rolník, Tisek 17) × Barbora Malá.
- Odkazy: https://ebadatelna.soapraha.cz/d/<matrikaId>/<snímek>; Pravonín 26 = 15260, Pravonín 21 = 10033; Pravonín 24 a 22 – id zjistit.
  Čísla snímků u ostatních zápisů jsou odvozená – ověřit.
- Pravonín 26 s. 104 přečtena (1937–38): Beran × Slunečková NENÍ. Č. 1/1936 = Tisek (Fiala × Píšová) – ne.
  Karhule i Částrovice prověřeny (ř. 31) – sňatek ve farnosti Pravonín NENÍ. Hledat mimo farnost: Velká Jesenice (fara
  ženicha), Praha, civilní sňatek – zeptat se rodiny (kde se brali, kde bydleli 1936).
  Oddíly knihy viz research_log ř. 29.
- (staré) Další od Jana: Pravonín 26 s. 104 (Beran × Slunečková po
  2/1937?); sňatek Jan Svatek × Marie Bezkočková asi 1878–80 (nejspíš ve Vitíně / farnost nevěsty, nebo Pravonín 26 Buková
  s. ~188–190); trvalé odkazy a čísla snímků pro citace. Sv. XXVI má oddíly po obcích (Pravonín ~75–155, Buková ~236–245,
  Tisek ~246–290, Karlov ~300–315, Částrovice ~330–340).
- Myslíkovi: Vladimír Myslík * 6. 5. 1930 Zdíkov (okr. Prachatice) – potřeba jména jeho rodičů.

## Slepé konce (kde jsme se zatím nepohnuli) – aktualizovat
| Linie | Kde to stojí | Co jsme zkusili | Co by to mohlo rozlousknout |
|---|---|---|---|
| Beranovi | Josef Beran * 3. 6. 1910 V. Jesenice; rodiče Josef Beran × Emilie Kozáková | sňatek Josef × Ludmila v celé farnosti Pravonín 1934–38 (ne); V. Jesenice N 1863–1906 B a K (žádný Beran ani Emilie Kozáková); O 1871–1906 B (ne) | výpis N 1910 z matričního úřadu (Jan jako pravnuk); Pravonín 25/27 – úmrtí Josefa st. nebo Emilie v Pravoníně před 1949 (rejstřík Z, písm. B); Pravonín 24 rejstřík N písm. B – mladší sourozenci Josefa narození v Pravoníně (kdy rodina přišla); Adresář RČS 1920–1929 (od kdy cihelna) |
| Gillernovi | děda Augustýn – bez roku a místa narození | Kramerius, policejní přihlášky, mapa hrobů SPH (Hrnčíře tam nejsou) | náhrobek v Hrnčířích / správa hřbitova MČ Praha-Šeberov; rodinné doklady |
| Svatkovi | sňatek Jan Svatek × Marie Bezkočková (asi 1878–80) | Pravonín 26 oddíl Buková 1870–1884 (ne) | farnost Vitína (Počepice? – eBadatelna) nebo Bzové (SOA Třeboň); narození Jana Svatka ve Bzové 1 |
| Myslíkovi | Vladimír Myslík * 6. 5. 1930 Zdíkov | – | jména jeho rodičů od rodiny; Zdíkov = SOA Třeboň (jen prohlížeč) |
