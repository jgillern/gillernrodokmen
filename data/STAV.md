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
| 4 | Musilovi | UZAVŘENO u Jiřího Musila × Marie Magdaleny (viz slepé konce) | – | – |
| 5 | Bezkočkovi | UZAVŘENO (viz slepé konce) | – | – |
| 6 | Svatkovi | narození Jana Svatka (asi 1850–1855, Bzová 1) | farnost Bzové u Mladé Vožice (SOA Třeboň, jen prohlížeč) | Jan |
| 7 | Gillernovi | KRAMERIUS ÚKOL (až bude fungovat – zatím Connection reset): projít schwarzenberské šematismy a lesnické časopisy 1840–1940 (Gillern, Giller, „z Gillernů“) – kariéra Franze, Vincence, Augustina, Čeňka; zápisy úmrtí (nekrology).  Z dokladů a matrik: Augustin 1924 Osov – 1989; Jan z G. * 14. 6. 1894 Bohostice 33 (Těchnice 08 = eBadatelna d/10368/84); Augustin z G. × Marie Karolina Linková (* 9. 1. 1869 Písek); Vincenc z G. † 27. 1. 1894 Čimelice (72 let) × Tekla Vejdovcová z Veselíčka. LINKOVÉ UZAVŘENO: Pavel Linek (mlynář pod Lhotou ~1750) → Martin × Barbora Hubertová (1756) → Josef (* asi 1775, † 1847; otcovství odvozené – křest nenalezen, rejstřík fol. 169 nesedí) × Johanna Braunerová (* 1796 Osov, dcera zahradníka Jana Braunera × Alžběta Prechtová 1782) → Karel (* 1825) × Aloisie Löwová (1852 Drhovle) → Marie Karolina. LÖWOVÉ: František Löw * 5. 12. 1803 Praha sv. Vojtěch (otec Antonín, mistr sladovník, × Marie Procházková) × Anna Kudrličková (* asi 1807 Praha, † 1887 Písek) 1833 Drhovle; Kudrličkovi: Jan, klíčník, × Ludmila († 1822 Drhovle). Sňatek Augustin × Marie Linková nenalezen (Písek, Kostelec, Čimelice, Těchnice). Rod Tekly Vejdovcové hotový (řádek 7d). DALŠÍ: Franz (František) z Gillernů – Krchleby 12 rejstřík N i O bez Gillernů (sňatek nebyl v Krchlebech). Postup: přiblížit původ matky Anny v křtu Vincence (Zbyšov 01 s. 140) a Franzovo povolání/bydliště „Lebstremitz ?“ v sňatku 1859 (Veselíčko fol. 42); křty sourozenců Zbyšov 01 s. 190 (1825) a 205 (1827); pak fara nevěsty – Mitrov u Uhlířských Janovic (okr. Kutná Hora; Pelvan „pensista“ v Mitrově), sňatek asi 1812–1822. Kramerius 18. 11. stále Connection reset | Jan |
| 7b | Richtrovi / Piglovi (babička Božena) | UZAVŘENO 17. 11. 2026 – všech 8 větví do předků * asi 1770–1810. Knihy: Střezimíř 22 index N = 12576, 21 N 1881–1907 = 12575, 24 O 1876–1949 = 15262, 19 N 1856–1881 = 12577, N 1839–56 = 12588, N 1816–23 = 12590, 15 index N 1816–83 = 12580, 11 O 1839–75; Prčice 16 index = 13071, 10 N = 13065, 12 O = 13067; Sedlec-BN 13 N 1834–54 = 11705 (přehled stran po obcích na začátku); Červený Újezd 03 N = 3732, 04 O = 3733; Nová Ves u M. Vožice (Třeboň) 6 N 1801–82 = 5972, 18 index = 5984. Případně dál: sňatky asi 1800–1820 (Pigl, Doubek – přistěhovalci), Otradovec × Dědová (asi 1870–75) | – |
| 7c | Hřídelovi / Štětinovi | UZAVŘENO 17. 11. 2026 (fara Mirovice, SOA Třeboň; knihy po vesnicích, oddíl O podle nevěsty): N 7 = 5610, N 8 = 5611, N 9A = 10752, O 11 = 5614, O 12 = 5615, O 13 = 5616, index 23 = 5626 (nepravidelné bloky). Julie 1897, sňatek 1893, František 1848, Josefa 1868, Jan Štětina 1830, sňatky 1826 (Štětina × vdova Anna), 1828 (Hanzlík × Barbora), 1842 (Hřídel × vdova Barbora). Otevřené: sňatek Jan Štětina × Marie Tesková asi 1860 (fara Koupě – nenalezena), obce Ostrovec/Nerestec/Chraštičky čteny nejistě | – |
| 7d | Vejdovcovi / Kůrovi / Jírovcovi (rod Tekly Vejdovcové) | UZAVŘENO 18. 11. 2026 (SOA Třeboň). Josef Vejdovec * 1798 Božetice 5 (Sepekov N 4925 = digi 7162) – rodiče Jakub × Dorota Dědinová/Čunátová 1790 (Sepekov O 4934 = 7171; Jakub * asi 1763 – v Milevsko N digi 5537 1757–1766 NENALEZEN); Dorota pravděp. * 1762 Božetice, dcera Františka Dědiny × Kateřiny. Anna Kůrová * 5/1786 Zběšičky (Bernartice N 164 = 2169, s. 449) – rodiče Karel Kůra, vysloužilý dělostřelec (* asi 1737) × Marie Anna Jírovcová 1785 Zběšičky (Bernartice O 173 = 2178, s. 275); Marie Anna * 5. 5. 1748 Bernartice (inv. 162 = 2167, s. 181) – rodiče František Jírovec, vdovec, × Terezie, dcera Jana Bělínka (?) z Milevska, 1. 8. 1740 (inv. 162, O s. 262). Otevřené: 1. sňatek Františka Jírovce (O 1732–1739 negativní → Bernartice inv. 161, O 1709–1731); Terezie Jelínková * 8. 10. 1713 Milevsko (inv. 3373, s. 241) – rodiče Jan Jelínek alias Hlenický z Týna n. Vlt. × Anna Humpová, dcera Martina Humpy, 28. 10. 1708 Milevsko (O s. 50). Jan * 8. 3. 1680 Týn n. Vlt. (inv. 5815, fol. 185b; rejstřík 5852) – otec Václav Hlenický alias Jelínek, měšťan, × Kateřina. Sňatek Václava Hlenického: Týn O 1660–1684 (inv. 5834) prohlédnuto 2/1677 – 7/1680 – sňatek 15. 10. 1678 Václav Jelínek (konvář ?) × Anna Tyboltová je JINÁ rodina (syn Václav 1683, matka Anna); Václav Hlenický × Kateřina se brali před 1671 (O 1/1671 – 7/1680 negativní; UZAVŘENO) → případně jen 5834 1660–1670, Milevsko O před 1699 (Martin Humpa) | Jan |
| 8 | Myslíkovi / Šustrovi | HOTOVO z online matrik (fara Zdíkovec, SOA Třeboň): Ludvík Myslík × Františka Šustrová 1921; rodiče a prarodiče všech čtyř větví – Myslík × Šimková 1886, Šustr × Volfová 1892, Tomáš Šustr × Vaňková 1865, Václav Volf × Sovová 1869; narození Františka Myslíka 1858 a Anny Šimkové 1862 (osoby 12–13, 24–27, 48–55, 96–111). Knihy: O 1897–1926 ID 8798, O 1864–1896 ID 8796, N Branišov ID 8779, N Zdíkovec ID 8778; N po vesnicích (Mas. Lhota N 1868–1936 na matričním úřadě). DALŠÍ: O 1848–1864 (sňatky Vojtěch Myslík × Staňková, Fr. Šimek × Benešová, Tomáš Volf × Sovová, Václav Sova × Železná); narození Tomáše Šustra 1812 a Františky Vaňkové 1836 (N Mas. Lhota / Zdíkov starší, „matr. č. II“), Václava Volfa 1847 a Františky Sovové 1848 („č. VI“) | Jan |
| 9 | Beranovi | (slepý konec) výpis z matriky | matriční úřad Vlašim – N XXVI: Ludmila Beranová 21. 4. 1912 s. 73 | Jan, až bude chtít |
| – | Wikipedie | de.wikipedia.org/wiki/Gillern – z cloudu 429 | Jan vloží text do chatu | Jan |

## Slepé konce (kde jsme se zatím nepohnuli) – aktualizovat
| Linie | Kde to stojí | Co jsme zkusili | Co by to mohlo rozlousknout |
|---|---|---|---|
| Beranovi | Josef Beran * 3. 6. 1910 V. Jesenice (cihelna v Pravoníně 1930–39); rodiče Josef Beran × Emilie Kozáková; sestra Ludmila * 21. 4. 1912 Pravonín (rodina tam od ~1911) | sňatek Josef × Ludmila Slunečková v celé farnosti Pravonín 1934–38 (ne); sňatek Josef st. × Emilie v Pravoníně 1905–1910 (ne); V. Jesenice N 1863–1906 písm. B a K (žádný Beran ani Emilie Kozáková); V. Jesenice O 1871–1906 B (ne); Pravonín N 1852–1893 K (ne); Pravonín Z 1873–1949 B (ne) | matriční úřad Vlašim (N XXVI fary Pravonín; zápisy starší 100 let může vyžádat kdokoli): Ludmila Beranová 1912 s. 73 – uvede původ rodičů; zápis Josefa 1910 V. Jesenice (matrika Č. Skalice?); sňatek asi V. Jesenice 1906–1910 (svazek není online) |
| Gillernovi | děda Augustýn – bez roku a místa narození | Kramerius, policejní přihlášky, mapa hrobů SPH (Hrnčíře tam nejsou) | náhrobek v Hrnčířích / správa hřbitova MČ Praha-Šeberov; rodinné doklady |
| Svatkovi | sňatek Jan Svatek × Marie Bezkočková (asi 1878–80) | Pravonín 26 oddíl Buková 1870–1884 (ne); Počepice 22 oddíl Vitín 1858–5/1877 (ne) | sňatek asi 1878–80 – kniha O Počepice po 1878 není online (matriční úřad); Bzová (SOA Třeboň) |
| Malí | Jan Malý, král. svobodník Buková 12 (1819–1833), pak gruntovník/výminkář Tisek 17; manželka Marie Benešová z Pravětic (1833), v r. 1819 ale „Marie, dcera Václava Halůžka? z Chmelné?“ | narození Jana Malého v N Pravonín 1709–1805 (rejstříky 13, 14) – ne; jeho sňatek v O Pravonín 1806–1869 – ne; úmrtí 1. manželky v Z 1806–1871 – ne | farnost Chmelné (Kamberk?) nebo Načeradec (Pravětice) – sňatek Jana Malého asi 1815–1827; jeho úmrtí po 1865 v Tisku (Pravonín Z 1836–71 / 1872+) uvede věk a rodiště |
| Slunečkovi | Josef Sluneček, chalupník Jeníkov č. 17 (1823), výminkář (1863); manželka Magdalena Saubl(?) ze „Sirčic/Cirčic“ (neurčeno) | narození v Jeníkově 1787–1800 (Zhoř 01) – ne; sňatek v Jeníkově 1816–1835 – ne; úmrtí v Jeníkově 4/1862 – 4/1888 – ne (1887 † Josef Slunečko, výminkář č. 17, 65 let = asi syn Josef * ~1822); děti v Jeníkově až od 1823 | přišel odjinud kolem 1820–22; zemřel mimo Jeníkov i Nakvasovice (Nakvasovice Z 12/1861–4/1876 bez Slunečků); určit obec „Sirčice“ (Magdalenina farnost, okr. Mladá Vožice – SOA Třeboň) |
| Pešanovi | Josef Pešan, soused v Křivsoudově č. 31 (1797) × Anna Mrátková (?), dcera Matěje Mrátka (?) a Anny Fialkové z „Mišovic“ (?) | sňatek v Křivsoudově (Křivsoudov 09) 1784–11/1797 – ne; kniha nemá oddíl Mnichovice/Mišovice | Úmrtí NALEZENO (pravděpodobně): † 28. 6. 1818 Křivsoudov 31, 54 let → * asi 1764; v indexu N Křivsoudov 1752–1768 (písm. P) NENÍ → narodil se mimo farnost Křivsoudov; určit obec „Mišovice“ (Mnichovice? jiná fara) – sňatek asi tam 1790–96; narození Josefa Pešana asi 1760–75 (Křivsoudov 03/04, N 1752–1784) |
| Myslíkovi (Vojtěch × Marianna Staňková) | rodiče obou známe z křtů dětí (Tomáš 1849, František 1858); svatba chybí | Zdíkovec O 1828–1847 konec (Jan), O 1848–1864 do 1850 (Jan), Vacov O oddíl Nespice 1847–2/1849 (vybledlé, kurent) – ne | sňatek asi před 1847 jinde (místo služby?) nebo čtení ve Vacově přehlédnuto; přidal by jen věk – nízká priorita |
| Šimkovi (František × Marie Anna Benešová) | rodiče obou známe z křtu dcery Anny (1862); svatba chybí | Zdíkovec N 1848–1862 (Anna nejstarší dítě), O 1848–1864 snímky 195–227 (1859–1862, Jan; 1859–61 skoro nečitelné) – ne | možná přehlédnuto v nečitelných stranách 1859–61; přidal by jen data narození snoubenců – nízká priorita |
| Volfovi / Sovové (Tomáš Volf × Kateřina Sovová; Václav Sova × Anna Železná) | rodiče všech čtyř známe z křtů dětí (Václav Volf 1847, Františka Sovová 1848) | Zdíkovec O 1828–1847 celá kniha (Jan, kurent; 1828–35 podle čísel domů) – ne | sňatky asi před 1828 nebo jinde (Tomáš Volf ze Stach → fara Stachy?); nízká priorita |
| Šedinovi (Marie Šedinová * asi 1820, matka Jana Pigla) | rodiče Jan Šedina, domkář Mezno 40, × Marianna ? (sňatek 1844) | index N Střezimíř 14 a 15 (S), N 12590 Mezno 1818–1821 – ne | narozena mimo Mezno (Rašovice? jiná obec farnosti) nebo věk nepřesný; nízká priorita |
| Doubkovi / Piglovi – původ | František Doubek a Jakub Pigl se ve farnosti Střezimíř 1708–1801 nenarodili | index N Střezimíř 14 (D, P) | přistěhovalci kolem 1800 – původ ze sňatků (asi 1805–1818, O Střezimíř před 1839) |
| Štětinovi (Jan × Marie Tesková, asi 1860) | rodiče obou známe z křtu Josefy 1868 | Mirovice O oddíl Horosedly 1859–1864; Koupě v eBadatelně ani ve faře Březnice nenalezena | farnost Koupě u Březnice určit (Bubovice? Hudčice?) |
| Musilovi | Jiří Musil, sedlák Jeníkov č. 5 († před 1789) × Marie Magdalena (rodné příjmení neznámé); syn Martin * 11. 10. 1764 | sňatek v Čechtice 07 (O) 10/1757 – 6/1762 – ne | sňatek před 10/1757 (Čechtice 07 pag. <68) nebo ve farnosti nevěsty; úmrtí Jiřího před 1789 (Čechtice 09, Z 1737–84) uvede věk; narození Jiřího asi 1730–40 (Čechtice 03/04) |
| Bezkočkovi | Jan Bezkočka, domkář Vitín 8 (syn †Jakuba, sedláka z Roviny 7, × Kateřina Trnková?) × Marie Zelenková (dcera Josefa Zelenky × Anna Saborová?); děti 1850–59 | sňatek ve Vitíně (Počepice 22) 1846–50 – ne; v Rovině (Počepice 22) 1846–1/1853 – ne; v Nechvalicích (index Nechvalice 18, písm. B) 1815–1871 – ne (jen František Bezkočka × Barbora Kutelová 1851) | sňatek jinde (rodiště nevěsty – určit obec Marie Zelenkové); narození Jana Bezkočky Rovina 7 asi 1818–28 (Počepice 27 index B, zvětšit); narození Marie Zelenkové (Nechvalice 04, N 1823–42) |
| Píšovi | Jakub Píša z Kondrace († před 1723) – otec Víta (× 1723 Anna Mudrá?) | narození Víta v indexu N Kondrac 1684–1716 (P) – ne (Vít 1691 = Přibyl) | Vít narozen mimo farnost Kondrac; úmrtí Jakuba před 1723 (Kondrac 12, Z 1684–1751) uvede věk |
| Svatkovi | Jan Svatek, krejčí/chalupník Buková 5 (otec Ludmily * 1893), syn Františka Svátka, rolníka ze Bzové č. 1, × Barbory (fara Šebířov, SOA Třeboň) | Šebířov N Bzová 1849–1855 kompletně (7776 fol. 36–40, 7777 pag. 100–103) a index S 1856–1864 (7782 sn. 86–88) – ne; kandidát 1859 Bzová 6 = nemanželský, jiný | Bzová N 1840–1848 (7776 fol. ~30–35); Jan mohl být starší (sňatek ~1880, dítě 1881) nebo narozen jinde; index S do 1855 nenalezen; v Bzové víc rodin Svatků (č. 2, 6, 8, 11, 14, 15, 18), r. 1852 rychtář Jan Svátek |
