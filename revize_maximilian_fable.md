# Nezávislá revize výzkumu: odkud pochází Maximilián svobodný pán z Gillernů

*Stav k 21. 11. 2026. Napsal nezávislý recenzent (Claude), který na výzkumu dosud nepracoval. Podklad: obsahová část repozitáře `jgillern/gillernrodokmen`, větev `claude/nice-dirac-8inizg`. V repozitáři jsem nic neměnil, jediný nový soubor je tento.*

## Jak dokument číst

- **[D] doloženo** = zápis je v repozitáři (uvádím klíč záznamu nebo číslo řádku deníku). **[O] odvozeno** = úsudek z doložených údajů. **[H] domněnka** = hypotéza bez dokladu (moje nebo dosavadní).
- **[N] nově z online tisku** = věc, kterou jsem při revizi našel ve volně dostupné digitalizované knize; odkaz je vždy uveden. Četl jsem strojově přepsaný text (OCR), ne obraz stránky. Než se cokoli z toho zapíše do rodokmenu, je potřeba stránku otevřít a přečíst.
- „deník č. 535“ = číslo v prvním sloupci `data/research_log.md` (v souboru je to řádek 535 + 7).
- Podle Janova doplnění navrhuji **jen cesty proveditelné online**, bez e-mailů, objednávek a návštěv archivů. Dříve plánované offline kroky zmiňuji jen tam, kde k nim existuje online náhrada.
- Kdo co může udělat: **A** = asistent s nástroji (AHMP, ARON, Porta fontium, Česká digitální knihovna, archive.org, katalog Rakouského státního archivu); **B** = druhý asistent, který čte prohlížeče archivů (eBadatelna SOA Praha, SOA Třeboň, ZA Opava, Matricula, MZA); **J** = Jan (jen přihlášení do bezplatných databází).

Krátký slovníček: *matrika* = církevní kniha křtů, sňatků a pohřbů; *rejstřík* = abecední seznam jmen k matrice (bývá neúplný); *kmotr, svědek* = osoby přítomné křtu nebo svatbě, často příbuzní; *svobodný pán* (baron, latinsky Liber Baro, „L. B.“) = šlechtický titul o stupeň výš než rytíř; *komorní panství* = panství patřící panovníkovi, ne soukromé šlechtě; *pluk Pallavicini* = císařský pěší pluk č. 15, pojmenovaný po svém majiteli; *fulltext* = hledání slov přímo v textu naskenovaných knih.

---

## 1. Shrnutí stavu

**Co je doloženo [D].** Maximilián Josef Emanuel (psán Gyller, Giller, Güller, Güllern, Gillern, jednou Killer) se poprvé objevuje 23. 1. 1750 jako „Jagr“ (myslivec) v hájovně Bor Bobnický u Nymburka (`n_1750_giller_anna_alexia`). Kmotry jeho prvních dětí jsou místní lidé bez titulů. Dál stoupá vždy v císařských lesích: 1756 „obrforšt“ v Hradištku, 1757–1761 lesní a „dvorní myslivec“ v Kladrubech nad Labem, 1762–1766 Čelákovice, v 70. letech „nejvyšší myslivec“ v Poděbradech (deník č. 535, 527; `data/osoby.py`, osoba 256). Manželka Johanna zemřela 18. 2. 1782 v 59 letech; měl s ní osm nebo devět dětí z let 1750–1766. Syn Josef (náš předek) je 1786 výslovně „syn pana Maximiliána, nejvyššího myslivce“ (`o_1786_giller_kochova`). Od Josefa dolů je linie doložená až k Janovi.

Titul „svobodný pán“ má Maximilián v matrice **jednou** (1781, `n_1781_klanner_marie_anna`). Známe dva jeho příbuzné: kapitána (Jana) Bedřicha „barona Gyllera“ z pluku Pallavicini (1761 svědek v zastoupení, 1765 sňatek v Pardubicích, 1766 svědek osobně) a Ignáce z Gillernů „ve Slezsku“ (1784, kmotr v zastoupení).

**Co nevíme.** Kde a kdy se Maximilián narodil, kdo byli jeho rodiče, kde a kdy se ženil, kolik mu bylo, kde zemřel (naposledy je zmíněn 1786), jak se jmenovala za svobodna Johanna a kdy se narodil Josef (věk při sňatku dává rok 1738, věk při úmrtí 1746/47).

**Hypotézy týmu** (`data/STAV.md`, ř. 142): H1 vnuk Friedricha Wilhelma I. (hlavně syn důstojníka Friedricha Wilhelma II.), H2 syn dvorního rady Karla Josefa, H3 druhá, slezská větev (Johann Christoph), H4 syn uherského barona Franze Niklase (odloženo), H5 měšťanská rodina ze Dvorců.

**Co je vyloučeno.** Maximilián se nenarodil, neženil a neměl děti v Poděbradech 1730–1749 (deník č. 508) ani v Sadské 1735–1750 (č. 543, čteno souvisle) a nejspíš ani v Nymburce (č. 538, s mezerami). V Poděbradech nezemřel 1771–1806 (č. 505, 506). Jeho křest není ve Dvorcích 1688–1730 (č. 553, 566; výřezy tým sám neověřil). Děti Franze Niklase nejsou v Chebu, Taunusu ani ve Frankfurtu (č. 560–563).

**Moje hlavní závěry.**
1. Baronský titul, pokud ho bereme vážně, ukazuje na jiné větve (H3, H4), než kam šla většina dosavadní práce (H1, H5).
2. Nejlépe dohledatelná osoba není Maximilián, ale kapitán Bedřich. Tištěné dějiny jeho pluku jsou volně online a jmenují ho [N].
3. Hypotézu H2 lze prakticky uzavřít z tištěného výtahu závěti vdovy po Karlu Josefovi, který je také online [N]. Tým si tento spis chtěl objednávat z Vídně.
4. Negativní výsledky spolehlivě říkají jen to, že před rokem 1749 nebyl v Polabí. Nic neříkají o tom, kde byl.
5. Několik údajů, které se v repozitáři berou jako hotové, je sporných (viz oddíly 2.3 a 6).

---

## 2. Kritika dosavadní strategie

### 2.1 Zafixované předpoklady

**P1 – „Byl svobodný pán, patří tedy k 1. nebo 2. větvi.“** (`data/rod_gillernu.json`, ř. 237 a 1425.)
Titul je doložen jen dvakrát: 1765 u Bedřicha („Illustrissimus Dnus Fridericus Baro Gyller“, `o_1765_gyller_bedrich`) a 1781 u Maximiliána. Jinde je Maximilián jen „Perillustris“ nebo „Praenobilis“, což jsou oslovení nižší šlechty. Tým z titulu vyvodil příslušnost k rodu, ale nedotáhl úvahu do konce: před rokem 1766 směli být barony jen potomci Karla Josefa (1727/1732), jeho bratrance Johanna Christopha (1732) a Franze Niklase (uherský baronát 1707) – viz výpis z Franka v `data/udaje_od_rodiny.md`, ř. 96–102. Synové důstojníka Friedricha Wilhelma II. barony nebyli: jeho syn Kristián dostal rytířský stav až 1764 a baronát 1766. Jsou tedy dvě možnosti. Buď titul platil, a pak padá nejčastější podoba H1 a zbývají H3 a H4. Nebo byl jen zdvořilostní, a pak z něj nelze vyvozovat nic. Podle dějin pluku č. 15 byl Bedřich veden jako „Baron“ i v armádě [N, viz 3.1], což mluví pro první možnost. (Kniha je z roku 1901 a autor mohl titul převzít z pozdějších seznamů; pardubický zápis z února 1765 je ale na ní nezávislý a je starší než Kristiánův baronát.) Proti první možnosti stojí to, že se potomci v 19. století psali „Edler von“, ne „Freiherr“ (deník č. 402).

**P2 – „Ignác ve Slezsku ukazuje, odkud rodina přišla.“** Zápis říká jen to, že Ignác roku 1784 ve Slezsku bydlel („in Silesia Incola“, `n_1784_clanner_maximilian`). Může to být Maximiliánův bratr, synovec, ale i syn: mezi křty 1753 a 1756 a mezi 1761 a 1766 jsou mezery. Slezsko navíc může být pruské i rakouské (Opavsko, Krnovsko, Těšínsko).

**P3 – „Josef se narodil asi 1738, tedy z prvního manželství.“** Na tomhle předpokladu stála celá zadání (`zadani_chatgpt_maximilian2.md`: hledat první manželku a sňatek kolem 1737; `zadani_chatgpt_male_davky.md`, úkol A). Opírá se o jediné číslo v jednom zápisu. Druhý zápis (úmrtí 1799, 52 let) dává rok 1746/47, a to by Josef byl prostě nejstarší dítě Johanny. První manželka není doložena ničím. Obě možnosti je třeba držet otevřené, ale hledat podle obou.

**P4 – „Franz († 1817, 70 let) je další dítě narozené před rokem 1750.“** (`data/rod_gillernu.json`, ř. 538, 845.) Franz zemřel v Malejovicích č. 1. V témže domě č. 1 se v letech 1816–1823 rodily děti Maximiliána Clannera (deník č. 556; článek M. Hanuše). Starý Franz tedy žil u synovce [O] a nejspíš je totožný s Františkem Ludvíkem Alexandrem, pokřtěným 1753 (`n_1753_giller_frantisek_ludvik`); věk 70 let je o šest let nadsazený. Pak z doby před rokem 1750 zbývá jediné dítě, Josef.

**P5 – „Před rokem 1750 byl lesníkem na jiném komorním panství.“** (`zadani_chatgpt_maximilian.md`, oddíl Hypotéza.) Stejně dobře mohl být do roku 1748 vojákem: první stopa je z ledna 1750, tedy rok po skončení války o rakouské dědictví, kdy se propouštělo z armády a propuštění dostávali místa ve státní službě. Tomu by odpovídalo i to, že Josefův křest není v žádné polabské matrice. Jiné možnosti, které se nezkoušely: Vídeň a Dolní Rakousy (titul „dvorní myslivec“; ve Vídni žil vlivný příbuzný Karel Josef), lichtenštejnská panství, Slezsko.

**P6 – „Hledá se v matrikách podle příjmení v rejstříku.“** Mimo Poděbrady, Sadskou a část Nymburka se hledalo jen v rejstřících pod G, J, K, V/W a Z (deník č. 535, 537). Rejstříky 18. století bývají neúplné a myslivec bez gruntu v nich často chybí. Nepoužily se vůbec souhrnné databáze (GenTeam pro Vídeň, FamilySearch) ani fulltext knih 18. století mimo českou digitální knihovnu.

**P7 – „Rodokmen šlechtického rodu máme z literatury hotový.“** Není. Sinapius, Gotha a Wikipedie si v několika bodech odporují a repozitář si vybral jednu verzi (viz 2.3, body 7–10).

**P8 – „Online zdroje jsou vyčerpané, další krok je objednat spisy ve Vídni.“** (`data/archivni_dotazy.md`, ř. 84–94; `data/STAV.md`, ř. 143, body 7–9.) To neplatí. Výtah závěti vdovy po Karlu Josefovi i služební údaje kapitána jsou vytištěné a volně na internetu (viz oddíl 3).

### 2.2 Negativní výsledky a co doopravdy vylučují

| Co se hledalo | Jak | Deník č. | Co to nevylučuje |
|---|---|---|---|
| Poděbrady, křty 1730–1771, úmrtí 1771–1806 | souvislé čtení, místy vybledlé | 505, 506, 508, 512, 527 | křty spolehlivé pro město; **sňatky od 5/1745 do 2/1756 podle deníku nikdo souvisle nečetl** (č. 506 je uvádí mezi nepřečtenými snímky knihy 11837; později se z nich otevřel jen sňatek Kochových 1748, č. 539) |
| Sadská 1735–1750 | souvisle, 415 snímků | 543 | spolehlivé |
| Nymburk 1735–1750 | rejstřík, křty vesnic jen 1744–1749, sňatky 1743–1750 | 535, 538 | křty vesnic 1736–1743 jen rejstříkem; jeden snímek zakrytý |
| Žehuň, Křinec (sňatky), Městec, Libice, Chleby, Brandýs, Lysá, Čelákovice, Přerov, Kolín, Ovčáry; Pardubice, Dašice, Holice | jen rejstříky pod G, J, K, V/W, Z | 535, 537 | zápis bez příjmení nebo pod jiným písmenem (Hiller, Kyller); fary Stará Boleslav a Kostelec nad Labem se nehledaly vůbec |
| Dvorce 1688–1730 | druhý asistent, výřezy neověřeny | 553, 566 | říká jen, že křest není ve Dvorcích; nic o Opavě, Krnově, Šternberku ani Slezsku |
| Cheb, Taunus, Frankfurt, Vřeskovice | souvisle | 557–563 | děti Franze Niklase se mohly narodit jinde (Uhry, posádky) |
| Geneteka, Dolní Slezsko | databáze | 567 | 0 záznamů znamená, že pro 18. století index neexistuje, ne že rodina neexistovala |
| Česká digitální knihovna do roku 1830 | fulltext | 554 | knihovna tisk 18. století skoro nemá; archive.org ano [N] |
| Úmrtí Maximiliána 1786–1810 | rejstříky okolních far | 535, 544, 556 | Městec 1784–1792 se nedochoval; mimo Polabí se nehledalo |
| Rodopisná literatura | devět titulů | 510 | chybí Zedlitz-Neukirch, Schlesische Provinzialblätter, Zimmermann, dějiny pluků, ročenka společnosti Adler |

### 2.3 Možné chyby čtení a ztotožnění

1. **„Bedřich Rudolf“ († 31. 1. 1762) je nejspíš totéž dítě jako „Jan Křtitel“ (\* 16. 1. 1761).** V repozitáři jsou vedeni jako dva sourozenci a u Bedřicha se píše „křest se nenašel“ (`data/osoby.py`, ř. 268–269). V úmrtním zápisu (`z_1762_gillern_bedrich_rudolf`) stojí „1 Anni … Mensis et 17 Dierum“; číslici u měsíců tým čte jako 9, já ji na výřezu nedokážu určit. Ať je jakákoli, samostatné dítě narozené v roce 1760 se vedle sourozence narozeného 16. 1. 1761 nevejde. Počítáno ke dni pohřbu (2. 2. 1762) vychází Janu Křtiteli přesně 1 rok a 17 dní. Kmotrem Jana Křtitele byl v zastoupení Bedřich z Gillernů; dítěti se zřejmě říkalo po něm („Junior Fridericus“ = Bedřich mladší) [O].
2. **Věk Josefa při sňatku 1786.** První číslice je 4, druhá není jistá (8, možná 5 nebo 6); deník č. 536 píše „jasně 48“. Na téže straně matriky je o deset týdnů později sňatek jiného Josefa Gillara, vysloužilého vojáka, také „48 let“ (deník č. 503). Dva ženichové téhož jména a věku na jedné straně jsou buď náhoda, nebo záměna při zápisu.
3. **Zápis 1784 (Ignác).** Za slovy „in Silesia Incola“ je ještě jedno slovo, které přepis vynechal (`data/prepisy.json`, „…“). Na výřezu čtu nejspíš „Missus“ (= vyslaný zástupce), méně pravděpodobně místní jméno. Na plném rozlišení to jde rozhodnout za minutu.
4. **Franz † 1817** – viz P4.
5. **Svědek 1771 „Perillustris D. Josephus de Giller“** (`o_1771_heg_breinerova`) je veden jako nejstarší zmínka o synu Josefovi. Otec Maximilián Josef Emanuel byl ale 1753 a 1777–1778 zapisován právě jako „Josef“ (deník č. 527), takže to může být on.
6. **„Maximilián žil ještě 1786“** plyne jen z toho, že u jeho jména v synově oddacím zápisu chybí křížek. Je to rozumný úsudek, ne doklad.
7. **Panství Karlovec nepatřilo řádu německých rytířů** (tak `data/rod_gillernu.json`, ř. 33, 220, 1095, 1208, 1284). Podle české Wikipedie založil Karlovec majitel šternberského panství kníže Karel II. Minsterberský; německá Wikipedie má Friedricha Wilhelma Gillera jako úředníka vévody z Württemberg-Oels a Franze Leopolda jako správce „lichtenštejnského panství Karlsberg“ [N]. Kmotr z řádu (1694) z panství řádové nedělá. Služební síť rodiny je tedy württembersko-olešnická a lichtenštejnská.
8. **Manželka Karla Josefa se nejmenovala „von Tallern“** (ř. 973, 1297), ale **von Fellner** [N, viz 3.3].
9. **Karel Josef měl syna, který zemřel mladý, a sám zemřel na podzim 1759 ve Vídni** (pohřben u sv. Štěpána) – tak německá Wikipedie, heslo Karl Joseph von Gillern [N]. Repozitář má „synové nejsou známi“ (ř. 1296) a místo úmrtí Koryčany. Táž Wikipedie udává narození 1691 a otce Franze Leopolda; tým má z matriky křest Carla Josepha 1696, syna Friedricha Wilhelma. Ve Dvorcích je ale i křest „Hanse Carla“ 6. 2. 1690, syna Franze Leopolda, a Karel Josef se celým jménem psal Johann Carl Joseph. Kdo z těch dvou je pozdější baron, není rozhodnuto, a mění to, kdo byli jeho bratři a synovci.
10. **Malíř Joseph Edward z Gillernů nepatří k „vídeňské větvi“** (ř. 240–243, 2024–2027). Narodil se 1794 ve Wanowitz u Hlubčic v pruském Slezsku, otec Johann byl úředník, vyučil se v Nise [N, německá a polská Wikipedie]. Je to doklad katolických Gillernů v Horním Slezsku.
11. **Údaje ze Dvorců jsou v rodokmenu rodu vedeny jako doložené** (stav „doc“), ačkoli deník č. 553 výslovně říká „neověřeno z výřezů“ a č. 566 ověřuje jen křest 1696. Odporuje to pravidlu 2 v `data/STAV.md`.
12. Drobnost: přepis úmrtí Franze 1817 má stále „24./26. Dubna“ (`data/prepisy.json`, ř. 591), ačkoli deník č. 556 opravil měsíc na leden.

### 2.4 Co se dělalo neefektivně

- **Plošné procházení rejstříků** desítek far kvůli muži, který do kraje prokazatelně přišel jako dospělý. Po prvním negativním výsledku v Sadské a Nymburce mělo přijít „kde tedy byl“, ne „další fara“.
- **Informace, které byly zadarmo, zůstaly ležet:** kmotři a svědci (kromě Bedřicha a Ignáce), čísla domů, celý text Hanušova článku o Clannerech, heslo o Karlu Josefovi na Wikipedii (deník č. 557 z něj vypsal jen část), důstojníci jménem Güller v Poděbradech (č. 506).
- **Hypotéza Franz Niklas** se testovala sedmi řádky deníku na místech vybraných podle manželčina rodu, ne podle toho, kde otec sloužil.
- **Hromadný sběr z České digitální knihovny** skončil pětkrát odmítnutím (č. 485, 496, 497, 509), přitom ta knihovna tisk 18. století skoro nemá (č. 554).
- **Zprávy druhého asistenta bez výřezů** se zapisovaly do rodokmenu (Dvorce).
- **Dvorce:** plán A1–A10 (`data/STAV.md`, ř. 141) rozplétá měšťanské rodiny ševců a tkalců, ačkoli pro vazbu Maximiliána na Dvorce není jediný doklad.

---

## 3. Přehlédnuté souvislosti

**3.1 Kapitán Bedřich je v tištěných dějinách pluku [N].** L. Rona, *Geschichte des k. u. k. Infanterie-Regimentes Nr. 15, 1701–1901* (Praha 1901), <https://archive.org/details/bub_gb_wWTRAAAAMAAJ>. V abecedním seznamu důstojníků (příloha, písmeno G): „Gillern Friedrich, Baron, H. 1753. 1771 als Platz-Major zu Grosswardein“ – podle vysvětlivek k pluku přišel roku 1753 jako hejtman a odešel 1771 jako major a velitel místa do Velkého Varadína (dnes Oradea v Rumunsku). V textu: 1760 slouží u plukovního depozitoria (s. 235); v září 1766 odchází 3. prapor do Brna a velí v něm hejtmani „Fürst Cantacuzeno, Hunger, Gillern und Stentsch“; v únoru 1767 jde prapor do Vídně a zůstává tam do začátku 1770, pak Budín a Stoličný Bělehrad; 1771 „Hptm. Gillern wurde Major und Platzcommandant in Großwardein“ (s. 247). Pluk byl 1744–1756 v Itálii (1751–1752 Cremona, 1753–1756 Como) a 1764–1766 ležel mezi moravskou hranicí a Kolínem, mimo jiné v Pardubicích.
*Co z toho plyne:* sedí to na všechny tři naše zápisy (1761 v zastoupení, 1765 Pardubice, únor 1766 Čelákovice). Víme, kde hledat jeho děti a úmrtí. A jako barona ho píše plukovní seznam i pardubický zápis z února 1765, tedy dřív, než baronát dostal Kristián (1766).

**3.2 U téhož pluku sloužil ještě „Gillern Franz Anton“ [N]:** praporčík „z civilu“ 1744, poručík, 1746 rezignoval (tamtéž). Pluk byl tehdy v Itálii. *Co z toho plyne:* další Gillern stejné generace; bez titulu, tedy možná z jiné linie než Bedřich. Kristián Matyáš Antonín se narodil 1723 v Lodi – Franz Anton může být jeho bratr [H].

**3.3 Závěť vdovy po Karlu Josefovi je vytištěná [N].** Ročenka společnosti Adler, *Monatsblatt*, sv. IV, s. 442, <https://archive.org/details/monatsblattdesh01adlgoog> (výtahy ze závětí vyhlášených u dvorského maršálského soudu): „Gillern, Maria Josefa, Freiin, geb. von Fellner, p. 1765. Geschwister: Karl Josef, Johann Adam und Maria Theresia, verehel. Freiin von Locella“. *Co z toho plyne:* je to spis, který stojí v `data/archivni_dotazy.md` (ř. 88) jako první k objednání. Výtah jmenuje jen její sourozence, žádné dítě ani žádného Gillerna. Spolu se zprávou o předčasně zemřelém synovi je H2 prakticky vyloučena.

**3.4 Tři větve spojuje jeden sňatkový okruh [N].** Sestra vdovy po Karlu Josefovi byla provdaná za dvorního radu barona Locellu; Locellův syn měl za ženu Antonii hraběnku „Ostreschau“, zřejmě Osteschau (tamtéž, s. 442–443). Kristián z Gillernů měl za ženu M. Karolinu svobodnou paní z Locella; jejich dcera Josefa se narodila 9. 7. 1768 (Hyrtl 1851, s. 261, <https://archive.org/details/bub_gb_jR9AAAAAYAAJ>). A slezský baron Joseph Anton z Gillernů měl za ženu Marii Františku hraběnku Osteschau (viz 3.5). *Co z toho plyne:* vídeňská, koryčanská a hlohovská větev držely pohromadě. Kdo z nich mohl pomáhat chudým příbuzným, pomáhal by jim odkudkoli z tohoto okruhu.

**3.5 Slezská baronská větev je v dobovém tisku dobře vidět [N].** Majitelé vsi Priedemost u Hlohova: Johann Christoph svobodný pán z Gillernů (1730), Joseph Anton (1757), ovdovělá Maria Franziska roz. hraběnka Osteschau (1765) – německá Wikipedie, heslo Przedmoście (Głogów), podle místní kroniky. F. A. Zimmermann, *Beyträge zur Beschreibung von Schlesien*: sv. 8 (1789) – „Johann Christoph Freyherr v. Giller auf Rettkau, Amtshauptmann des bischöfl. Preichauschen Haltes“ pobíral důchody asi 1710–1742 (<https://archive.org/details/10014531bsb>); sv. 7 (1787) – statek Culmikau na Stínavsku koupil v 80. letech „Freyherr v. Gillern“, patří mu i Gorkau (<https://archive.org/details/10014530bsb>); sv. 12 (1795) – Polnisch-Gandau držel „Baron v. Gillern“ (<https://archive.org/details/10014535bsb>). *Schlesische Provinzialblätter*, sv. 15 (1792): baronce „von Giller zu Culmickau“ se 8. 4. 1792 narodil syn Christian Ludwig Antonius, který po šesti týdnech zemřel; mezi kanovnicemi nové nadace je „Maria Josepha Freyin von Giller, aus dem großväterlichen Stammhause Rettkau, katholischer Religion“ (<https://archive.org/details/bub_gb_bZABAAAAYAAJ>).
*Co z toho plyne:* větev byla katolická, ve službách vratislavského biskupa, a Johann Christoph odchází ze scény kolem roku 1742, kdy Slezsko připadlo Prusku. Mladší synové takové rodiny šli běžně do rakouských služeb. V 80. letech 18. století žil na Stínavsku baron z Gillernů, kterému se ještě 1792 rodily děti – dobrý kandidát na kmotra Ignáce; křestní jméno v těchto tiscích zatím nemám. Tým tuto větev testoval jediným dotazem do Geneteky (deník č. 567).

**3.6 Úřad Karla Josefa a Maximiliánova kariéra.** Podle německé Wikipedie byl Karel Josef od roku 1729 radou dvorské komory a „bankality“ a nakonec prvním úředníkem ministeriální bankovní deputace [N]. Maximilián sloužil od roku 1749/50 jen na panstvích panovníka: Poděbrady, Pardubice (Kladruby), Brandýs (Čelákovice). Pokud vím, právě tato panství byla tehdy zastavena vídeňské městské bance a spravována bankovní deputací; to je moje obecná znalost a je třeba ji ověřit [H]. *Co z toho plyne:* cesta chudého příbuzného k místu myslivce vedla nejspíš přes Vídeň, ne přes sousední faru.

**3.7 Lichtenštejnská síť a lesnictví v rodině už 1716.** Karel Josef byl lichtenštejnský dvorní rada; dcera Franze Leopolda si 1716 vzala lesního jezdce ve Šternberku (`data/rod_gillernu.json`, ř. 1357). Lichtenštejnům patřila i velká lesní panství hned za Labem (Kostelec nad Černými lesy, Škvorec). Na žádném z nich se nehledalo.

**3.8 Clannerové (z Hanušova článku, který je v repozitáři jen citován).** Otec Jana Baptisty Clannera byl do roku 1740 královským regentem Poděbrad a Kolína. Jan Baptista sloužil 1765–1768 na brandýském panství v Kostelci nad Labem, tedy současně s Maximiliánem v Čelákovicích; od 1770 byl polesným v Poděbradech a **1787 se stal forstmistrem**. Josef odchází z Poděbrad do Býchor na kolínském panství mezi 1787 a 1789 (deník č. 530). *Co z toho plyne:* Maximiliánova služba skončila nejspíš 1786/87 [O]; tam je třeba hledat úmrtí nebo penzi. Vnuk Maximilián Clanner se v rodině jmenoval Ignác – kmotr Ignác byl tedy pro rodinu důležitý člověk.

**3.9 Jména a kmotři ukazují na západ Evropy.** Děti dostaly jména Genovefa, Filipína, Alexie, Alexandr, Ludvík, Eleonora; v Kladrubech jsou svědky paní Lambottin a ředitel manufaktury Pailloux (`n_1757_gillern_maria_eleonora`, `n_1761_gillern_jan_baptista`). V Poděbradech zemřel 5. 2. 1775 vysloužilý kapitán Sigisbert Güller (deník č. 506, neověřeno); Sigisbert je jméno typické pro Lotrinsko (moje obecná znalost). *Co z toho plyne [H]:* buď pocházela ze západu Johanna, nebo to podporuje H4 (matka Eleonora z Cronbergu, Porýní), nebo posádkové dětství (Friedrich Wilhelm II. zemřel 1751 v Lucemburku). Jména Friedrich, Wilhelm, Karl naopak připomínají 1. větev. Jména sama nerozhodnou, ale Sigisbertův zápis může.

**3.10 Sociální postavení.** Roku 1750 obyčejný „Jagr“ s místními lidmi bez titulů za kmotry (`n_1750_giller_anna_alexia`, `n_1753_giller_frantisek_ludvik`); syn Josef si bere dceru podruha po nemanželském dítěti (`n_1785_giller_frantisek`, osoba 258 v `data/osoby.py`); kapitán Bedřich si bere měšťanskou dceru. To nesedí na dědice bohatého Karla Josefa, ale sedí na nemajetnou vedlejší linii nebo na syny zchudlého barona.

**3.11 Důstojníci „Giller“ ve vídeňských novinách.** *Wienerisches Diarium* 1720: „Herr Giller, Fändrich vom Geyerischen Regiment“ (deník č. 559). Podle Sinapia a Gothy je pluk „Geyer“ plukem Friedricha Wilhelma II. a jeho bratr Johann Peter byl praporčík (`data/rod_gillernu.json`, profil „rodopis“). Tým zprávu zapsal pod hypotézu Franze Niklase a nespojil ji. V témže řádku deníku je i „Gillern, Obr. Lieut.“ v ročence z roku 1744 (s. 243, 538) – nepřečteno.

---

## 4. Návrhy nových směrů

Pořadí = jak moc by výsledek rozhodl mezi hypotézami × pravděpodobnost úspěchu ÷ pracnost. Odhady jsou moje a hrubé.

| # | Co udělat | Jakou otázku to rozhodne | Přínos a pravděpodobnost | Kdo | Z čeho v repozitáři vychází | Proč to ještě nebylo zkoušeno | Úspěch / neúspěch |
|---|---|---|---|---|---|---|---|
| 1 | Znovu přečíst na plném rozlišení šest už známých snímků: Poděbrady 11867/49 (Sigisbert Güller † 1775), 11845/10 (slovo za „Incola“), 11863/7 (oba Josefové 1786), Čelákovice 4722/449 (věk 1762), 11872/22 a /81 (poručík Antonín Giller), úmrtí invalidy Josefa Gillara 7. 7. 1792 | Je Sigisbert příbuzný a jak starý? Kde žil Ignác? Je věk 48 omyl? Kolik bylo dětí? | střední až vysoký; zápisy existují; půl hodiny práce | B | deník č. 502, 503, 506, 535; `data/prepisy.json` | č. 506: „podle zprávy, nezapsáno“; č. 536: „jasně 48“; č. 544: slovo za Silesia vynecháno | úspěch: Sigisbert „de Güllern“ s věkem; neúspěch: jiné jméno, bez „de“ |
| 2 | Jít po kapitánu Bedřichovi podle dějin pluku: obrazy stran v Ronově knize; křty dětí ve Vídni 1767–1770; jeho úmrtí ve Velkém Varadíně po 1771; schematismy 1772–1795 | Z které baronské větve je; věk a rodiště; kmotři = příbuzní | vysoký; asi 40 % na nový zápis, 20 % na rodiště | A (kniha, schematismy), J a B (Vídeň, Uhry) | `o_1765_gyller_bedrich`, `n_1766_gillern_jan_bedrich`; otázka 8 v `data/rod_gillernu.json` | č. 541 hledal jen Pardubice, Chrudim, Hradec; vojenské prameny v deníku nejsou | úspěch: úmrtní zápis s věkem nebo křest s kmotry Gillerny |
| 3 | Sestavit slezskou baronskou větev 1700–1800 z tisků: Schlesische Provinzialblätter 1785–1810, Zimmermann, Zedlitz-Neukirch II s. 234, kronika Priedemostu, dějiny kláštera Trzebnica; pak teprve matriky Rettkau, Priedemost, Preichau | H3: je mezi syny Johanna Christopha Maximilián a Friedrich? Kdo je Ignác? | vysoký; 60 % na určení Ignáce, 15–20 % na Maximiliána | A (archive.org), B | „Ignác in Silesia“ `n_1784_clanner_maximilian`; profil „rodopis“ | č. 510 tyto tituly nemá; č. 567 jen Geneteka | úspěch: jmenný seznam dětí Johanna Christopha |
| 4 | Vídeň: rejstříky GenTeam (křty, sňatky), obrazy na Matricule, Wienerisches Diarium; všechna jména Gillern, Giller, Güller 1700–1800 | H2 definitivně; děti kapitána; byl Maximilián před 1749 ve Vídni? | střední až vysoký; 70 % na rodinu Karla Josefa, 15 % na Maximiliána | J (účet GenTeam), B | profil „karel_josef“; titul „Venator Aulicus“ v `n_1761_gillern_jan_baptista` | Vídeň v deníku není (Matricula jen pro Taunus, č. 558–562) | úspěch: křty dětí Karla Josefa s kmotry; pohřeb 1759 |
| 5 | Uhry a Slovensko: jmenné hledání ve FamilySearch (indexované katolické matriky) 1700–1730 a 1770–1800; uherské šlechtické příručky | H4: děti Franze Niklase; úmrtí majora Bedřicha | střední; 20–25 % | J | deník č. 557–563; `data/STAV.md` ř. 86 | hledalo se v Chebu a Taunusu, v Uhrách jen diplom (č. 559) | úspěch: křest Gillera 1705–1713 s otcem Franzem Niklasem |
| 6 | Koryčany (MZA, Acta Publica) 1742–1800: všechny zápisy Gillernů, hlavně křest Josefy 9. 7. 1768 a kmotři; úmrtí 1783–1795 | Jsou Maximilián nebo Bedřich mezi kmotry u Kristiána? Nedožil Maximilián v Koryčanech? | střední; 30 % | B | profil „kristian“; STAV ř. 69 | Koryčany jen z literatury (č. 2, 152, 510, 557) | úspěch: Gillern z Čech jako kmotr nebo zemřelý |
| 7 | Opava, Krnov a Šternberk (ZA Opava) 1710–1735: křty Gillerů v lichtenštejnské službě | H1: narodil se Maximilián v úřednickém prostředí kolem Karla Josefa? | střední; 15 % | B | rodokmen rodu, ř. 1357; Pilnáček (STAV ř. 144) | hledaly se jen Dvorce (č. 553, 566) | úspěch: křest Maximiliána Josefa Emanuela |
| 8 | Úmrtí Maximiliána 1783–1795: rejstříky zemřelých pražských far (AHMP), Brandýs, Stará Boleslav, Kostelec nad Labem | Jeho věk, tedy rok narození | střední; 15 % | A (Praha), B | osoba 256; Hanuš (1787) | č. 544 a 556 jen Poděbradsko a Uhlířské Janovice | úspěch: zápis s věkem |
| 9 | Josefův křest a sňatek rodičů 1736–1749 tam, kde se nehledalo: nejdřív nepřečtené poděbradské sňatky 5/1745–2/1756 (kniha 11837); pak Stará Boleslav a Kostelec nad Labem přímo; fary pardubického panství v ARON; lichtenštejnská panství | Kde byl Maximilián před 1749; kdo byla Johanna | vysoký přínos, ale jen asi 10 % | B, A | osoba 128; č. 535 | rejstříky jen ve vyjmenovaných farách | úspěch: křest Josefa s otcem Maximiliánem |
| 10 | Lucemburk 1740–1751 a posádky pluku „Geyer/Platz“; přečíst „Obr. Lieut. Gillern“ 1744 (s. 243, 538) | H1: byli Maximilián nebo Franz Anton syny Friedricha Wilhelma II.? | střední; 10–15 % | B, J | profil „kristian“ († 1751 Lucemburk); č. 559 | Lucembursko v deníku není | úspěch: pohřeb 1751 se jmény dětí |
| 11 | Sňatek Eleonory s Clannerem 1780 (není v Poděbradech): Kostelec nad Labem, Brandýs, Praha | Svědci = příbuzní z Maximiliánovy strany | nízký až střední; 15 % | B, A | č. 527 | hledalo se jen v Poděbradech | úspěch: zápis se svědky |

### Podrobněji k prvním pěti

**Návrh 1 – šest snímků znovu.** Nic nového se nehledá, jen se na maximum přiblíží zápisy, které už má druhý asistent dohledané. Nejdůležitější je Sigisbert: pokud je zapsán s šlechtickým „de“ a věkem kolem 60–70 let, byl to někdo z Maximiliánovy generace, kdo k němu přišel dožít, a jeho věk a případná poznámka o původu by silně zúžily hypotézy. Pokud ne, vyřadí se a nic se neztratí. U zápisu 1786 stačí položit vedle sebe číslice u obou Josefů a u nevěst. U zápisu 1762 přečíst číslici u měsíců.

**Návrh 2 – kapitán Bedřich.** (a) A otevře obrazy stran 235 a 243–247 a seznam důstojníků v Ronově knize, přečte i poznámky pod čarou (odkazují na spisy válečného archivu) a pasáž k roku 1753 v Como. (b) Prapor byl od února 1767 do začátku 1770 ve Vídni: J nebo B vyhledá v rejstřících GenTeam křty dětí s otcem „Gillern, Güllern, Giller“, hejtmanem, a matkou Annou; obraz zápisu je na Matricule. Kmotři budou nejspíš příbuzní. (c) Od 1771 Velký Varadín: úmrtí „majora a velitele místa“. Je třeba nejdřív ověřit, zda jsou varadínské katolické matriky online (FamilySearch; rumunské archivy) – to nevím. (d) Dvorské a vojenské schematismy 1772–1795: rok, kdy z místa zmizí, je rok úmrtí nebo penze. Neúspěch poznáme tak, že ve Vídni 1767–1770 žádný křest není a varadínské matriky online nejsou; pak zbývají jen schematismy.

**Návrh 3 – slezští baroni.** Postup, který jsem si ověřil: z archive.org se dá přes brzdu stáhnout strojový text celého svazku jedním dotazem a v něm hledat „Giller“, „Gillern“, „Culmi(c)kau“, „Rettkau“. Tak jsem během revize prošel 13 svazků Zimmermanna a jeden svazek Provinzialblätter. Zbývá projít ostatní svazky Provinzialblätter 1785–1810 (narození, sňatky a úmrtí šlechty s daty a věkem) a heslo u Zedlitze-Neukirche (díl II, s. 234; dodatkový díl, s. 180, říká jen, že starými statky rodu jsou Rettkau a díl Priedemostu). Cílem je tabulka: Johann Christoph († asi 1742) – jeho děti – Joseph Anton († před 1765) – jeho děti – baron na Culmikau. Do ní se zkusí zařadit Ignác, Bedřich (hejtman 1753, tedy narozen nejpozději kolem 1730) a Maximilián. Teprve potom má smysl hledat katolické matriky Rettkau, Priedemostu a Preichau; zda jsou online, jsem neověřil.

**Návrh 4 – Vídeň.** Karel Josef žil ve Vídni od roku 1724 do smrti. GenTeam je bezplatná databáze s rejstříky vídeňských křtů a sňatků; vyžaduje registraci, proto J. Rozsah rejstříků pro 18. století jsem neověřil. Hledat všechny tvary jména. Co čekat: křty dětí Karla Josefa (a jejich kmotry), pohřeb na podzim 1759 u sv. Štěpána, děti kapitána 1767–1770, případně sňatek nebo dítě Maximiliána před rokem 1749. Výtahy závětí v ročence Adler vycházely na pokračování ve více svazcích; závěť samotného Karla Josefa jsem ve svazku IV nenašel, může být v jiném – A to zjistí fulltextem archive.org.

**Návrh 5 – Uhry.** Franz Niklas dostal uherský baronát 1707, v době Rákócziho povstání; děti se mu mohly rodit v uherské posádce, kde se nehledalo. FamilySearch má indexované katolické matriky Maďarska a Slovenska; stačí jmenné hledání. Stejným hledáním se dá zachytit i major Bedřich po roce 1770 (Budín, Stoličný Bělehrad). Pokrytí Oradey jsem neověřil.

**Jak se podle mě posouvá váha hypotéz** (odhad recenzenta): H3 výrazně nahoru (titul u obou bratrů, katolická větev ve Slezsku doložená v 80. letech, odchod Johanna Christopha kolem 1742). H4 nahoru (titul, jméno Eleonora, západní jména, uherské místo majora), ale bez jediného dokladu dětí. H1 dolů v podobě „syn Friedricha Wilhelma II.“, protože ti barony nebyli; zůstává možná, pokud byl titul jen zdvořilostní. H2 prakticky vyloučena. H5 bez opory.

---

## 5. Co přestat dělat

1. Další rejstříky polabských far pod G, J, K, V/W, Z bez nové indicie.
2. Hledání „první manželky“ a „Josefa kolem 1737“ jako samostatný cíl, dokud se neověří věk (návrh 1).
3. Další matriky v Taunusu, Frankfurtu a Chebu kvůli Franzi Niklasovi; pokud H4, tak Uhry a jmenné indexy.
4. Rozplétání měšťanských Gillerů ve Dvorcích (body A1–A8 plánu); pro Maximiliána nemá váhu.
5. Hromadný sběr z České digitální knihovny a schematismy Čech 1789–1830 kvůli Maximiliánovi.
6. Geneteku pro Dolní Slezsko 18. století.
7. Zapisovat do rodokmenu rodu jako doložené to, co nikdo neviděl na snímku.
8. Plánovat objednávky ve Vídni jako další krok; nejdřív vytěžit tisk, který je online.

---

## 6. Nejistoty v datech k ověření

Seřazeno podle toho, jak moc ovlivňují závěry.

1. **Baronský titul.** Kolikrát a kde přesně je v zápisech 1750–1786; platí údaj z dějin pluku („Gillern Friedrich, Baron, H. 1753“)? Rozhoduje mezi H1 a H3/H4. Ověřit na obrazu stránky Ronovy knihy a projít všechny poděbradské zápisy znovu jen kvůli titulu.
2. **Věk Josefa 1786 (48?) proti 1799 (52).** Rozhoduje, zda existovala první manželka a jak starý byl Maximilián.
3. **Sigisbert Güller † 1775** – příbuzný, nebo cizí člověk? Dosud jen z hlášení (deník č. 506).
4. **Ignác 1784** – nepřečtené slovo; kdo to je.
5. **Všechna [N] zjištění z OCR** (dějiny pluku, závěť vdovy, Zimmermann, Provinzialblätter) – ověřit na obrazech stran, než se zapíšou.
6. **Kostra šlechtického rodokmenu:** kdo je Karel Josef (křest 1690, nebo 1696), jeho otec, syn, datum a místo úmrtí (1759 Vídeň, nebo 1762), manželka (Fellner); komu patřil Karlovec; kdo je Friedrich Wilhelm I. (správce v Karlovci a zároveň účetní v Lehnici?).
7. **Bedřich Rudolf = Jan Křtitel?**
8. **Franz † 1817 = František Ludvík Alexandr (\* 1753)?**
9. **Údaje ze Dvorců** – neověřené výřezy vedené jako doložené.
10. **„Maximilián žil ještě 1786“** a kdy skončil ve službě (Clanner forstmistrem 1787).
11. **Svědek 1771 Josef** – otec, nebo syn.
12. Drobnosti: měsíc v přepisu úmrtí 1817; měsíc křtu 1781; příjmení nevěsty 1765 (Neška / Newka) a jméno svědka majora; zařazení malíře Josepha Edwarda.

---

## Příloha: co jsem při revizi ověřoval online a co se nepovedlo

- **Přečteno přes brzdu `tools/slusne.py`, pomalu, po jednom dotazu:** německá, česká a polská Wikipedie (hesla Gillern, Karl Joseph, Dominika, William a Joseph Edward von Gillern, Ernst Heinrich, Przedmoście, Koryčany, Karlovec); článek M. Hanuše na pratelepardubicka.cz; z archive.org strojové texty 13 svazků Zimmermanna, Ronových dějin pluku č. 15, ročenky Adler sv. IV, Hyrtla 1851, Provinzialblätter sv. 15, dodatkového dílu Zedlitze-Neukirche a několik dotazů do fulltextu archive.org.
- **Nepovedlo se:** Google Books odmítlo hned první dotaz (HTTP 429), brzda web zastavila a neobcházel jsem to. Bavorská digitální knihovna vyžaduje prohlížeč; jeho spuštění mimo brzdu mi systém nepovolil, takže jsem ji nepoužil. Běžný vyhledávač k tématu skoro nic nenašel.
- **Neověřeno, i když na tom stojí některé návrhy:** rozsah rejstříků GenTeam pro 18. století; dostupnost matrik Oradey, Rettkau a Priedemostu online; zda jsou online moravské zemské desky se závětí Karla Josefa (proto je mezi návrhy nemám); zda česká komorní panství spravovala bankovní deputace.
- Snímky jsem otevíral jen z repozitáře (`vyrezy/`, `zdroje/`): sňatek 1786, křest 1784, křest 1781, sňatek 1765, úmrtí 1762, křest 1750.
