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
Stav k 16. 11. 2026. Matriky SOA Praha (eBadatelna) čte Jan v prohlížeči a posílá snímky (+ číslo snímku / URL);
SOA Zámrsk (ARON) Claude prohledá sám. Odkazy: https://ebadatelna.soapraha.cz/d/<matrikaId>/<snímek> –
Pravonín 21 (N 1852–93) = 10033, Pravonín 22 (Index N 1852–93) = 10034, Pravonín 24 (Index N 1894–1949) = 10036,
Pravonín 26 (O 1870–1949) = 15260, Pravonín 04 = 13037, Zhoř 07 = 9162, Zhoř 14 = 9169, Čechtice 04 = 4701, Pravonín 05 = 13036, Pravonín 09 = 13049 (snímek ≈ strana − 59 v první části knihy). Oddíly knih po obcích viz research_log ř. 29.

**Doloženo z matrik:** Ludmila Svatková (* 1893 Buková 5) × František Sluneček (* 1888 Tisek 17), sňatek 1914; Alois Sluneček
(* 1863 Nakvasovice) × Josefa Píšová (* 1865 Tisek 17), sňatek 1887; jejich rodiče: František Sluneček (obuvník, Jeníkov) × Anna
Musilová; Jan Píša (Tisek 17, z Kondrace 25) × Barbora Malá (Tisek 17); Jan Svatek (krejčí, Buková 5) × Marie Bezkočková (Vitín 8);
prarodiče František Svátek (Bzová 1) × Barbora; Jan Bezkočka (Vitín 8) × Marie Zelenková; Jan Píša (Kondrac 25) × Barbora
Krušnová(?); Jan Malý (Tisek 17) × Marie Benešová(?).

### Další postup (pořadí = doporučené)
| # | Linie | Co hledat | Kde | Kdo |
|---|---|---|---|---|
| 1 | Píšovi | HOTOVO: sňatek 22. 11. 1853 (Pravonín 09 s. 98); dál starší děti Jana a Barbory 1854–1862 (rejstřík Pravonín 22, písm. P) | Pravonín 22 / 21 | Jan |
| 2 | Malí | SLEPÝ KONEC (viz níže) | – | – |
| 3 | Píšovi | narození Jana Píši (asi 1830–1838, Kondrac 25) | farnost Kondrac (SOA Praha, eBadatelna) | Jan |
| 4 | Musilovi | HOTOVO: Martin Musil * 11. 10. 1764 Jeníkov (Čechtice 04 pag. 427), syn Jiřího Musila × Marie Magdaleny. Dál: sňatek Jiří Musil × Marie Magdalena asi 1755–1762 – kniha O fary Čechtice (zjistit v eBadatelně); bratr Matěj * 1762 (pag. 369). Kubálkovi: Magdalena v indexu K 1766–70 není – zkusit 1762–66 nebo zápis Matěje Kubálka pag. 513 (1768) | Jan |
| 5 | Bezkočkovi | narození Marie Bezkočkové (asi 1855–1860, Vitín 8); sňatek Jan Svatek × Marie Bezkočková (asi 1878–80) | farnost Vitína (Počepice? – SOA Praha) | Jan |
| 6 | Svatkovi | narození Jana Svatka (asi 1850–1855, Bzová 1) | farnost Bzové u Mladé Vožice (SOA Třeboň, jen prohlížeč) | Jan |
| 7 | Gillernovi | roky dědy Augustýna a jeho rodičů | náhrobek Praha-Hrnčíře / správa hřbitova MČ Praha-Šeberov | Jan / rodina |
| 8 | Myslíkovi | jména rodičů Vladimíra Myslíka (* 1930 Zdíkov) | rodina; pak SOA Třeboň | Jan / rodina |
| 9 | Beranovi | (slepý konec) výpis z matriky | matriční úřad Vlašim – N XXVI: Ludmila Beranová 21. 4. 1912 s. 73 | Jan, až bude chtít |
| – | Wikipedie | de.wikipedia.org/wiki/Gillern – z cloudu 429 | Jan vloží text do chatu | Jan |

## Slepé konce (kde jsme se zatím nepohnuli) – aktualizovat
| Linie | Kde to stojí | Co jsme zkusili | Co by to mohlo rozlousknout |
|---|---|---|---|
| Beranovi | Josef Beran * 3. 6. 1910 V. Jesenice (cihelna v Pravoníně 1930–39); rodiče Josef Beran × Emilie Kozáková; sestra Ludmila * 21. 4. 1912 Pravonín (rodina tam od ~1911) | sňatek Josef × Ludmila Slunečková v celé farnosti Pravonín 1934–38 (ne); sňatek Josef st. × Emilie v Pravoníně 1905–1910 (ne); V. Jesenice N 1863–1906 písm. B a K (žádný Beran ani Emilie Kozáková); V. Jesenice O 1871–1906 B (ne); Pravonín N 1852–1893 K (ne); Pravonín Z 1873–1949 B (ne) | matriční úřad Vlašim (N XXVI fary Pravonín; zápisy starší 100 let může vyžádat kdokoli): Ludmila Beranová 1912 s. 73 – uvede původ rodičů; zápis Josefa 1910 V. Jesenice (matrika Č. Skalice?); sňatek asi V. Jesenice 1906–1910 (svazek není online) |
| Gillernovi | děda Augustýn – bez roku a místa narození | Kramerius, policejní přihlášky, mapa hrobů SPH (Hrnčíře tam nejsou) | náhrobek v Hrnčířích / správa hřbitova MČ Praha-Šeberov; rodinné doklady |
| Svatkovi | sňatek Jan Svatek × Marie Bezkočková (asi 1878–80) | Pravonín 26 oddíl Buková 1870–1884 (ne) | farnost Vitína nebo Bzové (viz Další postup 5–6) |
| Myslíkovi | Vladimír Myslík * 6. 5. 1930 Zdíkov | – | jména jeho rodičů od rodiny; Zdíkov = SOA Třeboň (jen prohlížeč) |
| Malí | Jan Malý, král. svobodník Buková 12 (1819–1833), pak gruntovník/výminkář Tisek 17; manželka Marie Benešová z Pravětic (1833), v r. 1819 ale „Marie, dcera Václava Halůžka? z Chmelné?“ | narození Jana Malého v N Pravonín 1709–1805 (rejstříky 13, 14) – ne; jeho sňatek v O Pravonín 1806–1869 – ne; úmrtí 1. manželky v Z 1806–1871 – ne | farnost Chmelné (Kamberk?) nebo Načeradec (Pravětice) – sňatek Jana Malého asi 1815–1827; jeho úmrtí po 1865 v Tisku (Pravonín Z 1836–71 / 1872+) uvede věk a rodiště |
| Slunečkovi | Josef Sluneček, chalupník Jeníkov č. 17 (1823), výminkář (1863); manželka Magdalena Saubl(?) ze „Sirčic/Cirčic“ (neurčeno) | narození v Jeníkově 1787–1800 (Zhoř 01) – ne; sňatek v Jeníkově 1816–1835 – ne; úmrtí v Jeníkově 4/1862 – 4/1888 – ne (1887 † Josef Slunečko, výminkář č. 17, 65 let = asi syn Josef * ~1822); děti v Jeníkově až od 1823 | přišel odjinud kolem 1820–22; zemřel mimo Jeníkov i Nakvasovice (Nakvasovice Z 12/1861–4/1876 bez Slunečků); určit obec „Sirčice“ (Magdalenina farnost, okr. Mladá Vožice – SOA Třeboň) |
| Pešanovi | Josef Pešan, soused v Křivsoudově č. 31 (1797) × Anna Mrátková (?), dcera Matěje Mrátka (?) a Anny Fialkové z „Mišovic“ (?) | sňatek v Křivsoudově (Křivsoudov 09) 1784–11/1797 – ne; kniha nemá oddíl Mnichovice/Mišovice | Úmrtí NALEZENO (pravděpodobně): † 28. 6. 1818 Křivsoudov 31, 54 let → * asi 1764; v indexu N Křivsoudov 1752–1768 (písm. P) NENÍ → narodil se mimo farnost Křivsoudov; určit obec „Mišovice“ (Mnichovice? jiná fara) – sňatek asi tam 1790–96; narození Josefa Pešana asi 1760–75 (Křivsoudov 03/04, N 1752–1784) |
