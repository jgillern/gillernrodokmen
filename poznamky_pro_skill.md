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

- **VÚA Praha (vuapraha.cz) z cloudu:** curl přes brzdu neověří certifikát webu (chybí mezilehlý certifikát?), pomocník web-fetch byl zamítnut
  kontrolou oprávnění. Databázi legionářů (https://www.vuapraha.cz/databaze-vha/) musí hledat uživatel v prohlížeči. Do skillu doplnit
  návod: legionář ve svatebním zápisu („francouzský/ruský/italský legionář“) → databáze legionářů VÚA (karta s útvarem, daty, domovskou obcí).

- **Příběh po kapitolách:** jeden data/pribeh.md přestal stačit, když přibyly další linie. Zavedeno data/pribehy/NN-nazev.md
  (frontmatter title, strana, obdobi, rody, stav, lead) → stránky /pribehy/<nazev>/ s navigací, data/pribeh.md je úvod knihy;
  plus srovnávací kapitola „Jak žili“. Úpravy: tools/export_web.py (kopie do generated/pribehy, kontrola odkazů),
  web/src/lib/kapitoly.js, web/src/pages/pribehy/[slug].astro. Stálo by za to mít ve skillu jako výchozí strukturu.
- **SOA Třeboň, Zdíkovec:** ID archivní knihy = 8772 + pořadové číslo knihy; farní číslování v rejstřících a svatebních
  zápisech („matr. č. 12“, „kniha 1“) se s archivním neshoduje – vždy ověřit podle roků a obcí v popisu knihy.

- **Netlify + base = "web": všechna nasazení „Canceled“.** Netlify u nastaveného base directory sestavení přeskočí, když se
  v base (web/) nic nezměnilo – změny dat v data/ tak na web nikdy nedojdou. Oprava: v netlify.toml (kořen i web/) `ignore = "exit 1"`.
  Do skillu přidat do výchozí šablony netlify.toml.

- **Čtení písma – dlouhé „ſ“ a „u“ bez háčku (17. 11. 2026):** v Těchnicích 1894 jsem „Písku“ četl jako „Šitkn/Štěkni“ (ſ vypadá jako t, u bez obloučku jako n) a „Aloisie“ jako „Marie“ (velké A jako M). Do skillu: u nečitelného místa nejdřív zkusit obce, které už známe z jiných dokladů (tady „z Písku“ z křestního listu 1924), a porovnat velká písmena s jinými slovy téhož písaře.

- **Netlify a počet nasazení (17. 11. 2026):** s `ignore = "exit 1"` spouští každý push nové produkční sestavení; za jeden večer jsme jich udělali 28 a web se přestal aktualizovat (nejspíš vyčerpaný měsíční limit bezplatného tarifu – ověřit podle stránky Deploys). Do skillu: commity, které nemění web (deník, STAV), označovat `[skip netlify]` a pushovat dávkově, ne po každé drobnosti.

- **Cloudflare z cloudové session Claude (17. 11. 2026):** token uložený jako síťový secret pro api.cloudflare.com proxy vkládá do hlavičky Authorization u všech požadavků – i u `POST /workers/assets/upload`, kde wrangler posílá vlastní JWT upload session → 401 a nasazení selže (účet i subdoménu ale založit stihne). V cloudové session proto nasazovat přes Cloudflare Workers Builds (import repozitáře z GitHubu: root `web`, build `npm run data -- --nasazeni && npm run build`, deploy `npx wrangler deploy`, název projektu = name z wrangler.jsonc), ne `npm run nasadit-cloudflare`. Lokálně (bez proxy) funguje i skript.

- **Plná křestní jména ve vějíři (17. 11. 2026):** nové nepovinné pole `krest=` v osoby.py (P) – všechna křestní jména z matriky („Augustin František Jan Křtitel Gillern“); tools/fan_chart.py ho použije místo `n`. Uživatel chce ve vějíři plná jména (ne zkrácená). Do skillu: při zápisu narození vyplnit `krest`, když má osoba víc jmen.

- **Luštění zkratkovitých zápisů – druhý názor jiného modelu pomohl (18. 11. 2026).** Ve sňatku 1821 (Uhl. Janovice) jsem četl „Lobk. Adjunkt“ a zbytek nerozluštil; jiný AI model navrhl „mysliw. Lokal. Adjunkt na Pstwj Sedl[ic]kém, Knjžete Sswarcenberka“ – po kontrole tvarů písmen sedí a dává smysl (schwarzenberské Sedlec). Do skillu: u nečitelných buněk doporučit uživateli druhý názor (jiný model / fórum) a výsledek vždy ověřit podle tvarů písmen a historické věrohodnosti; zkratky panských úředníků (mysliw., lokal., wrchn., hosp.) mít v taháku.
- **Dlouhé „S“ na začátku slova vypadá jako „L“** (1859: „Lebstremitz“ = Schebestenitz). Přidat k chybám čtení (podobně jako ſ v „Písku“).

- **Kramerius: když NK (kramerius5.nkp.cz) nefunguje, funguje Česká digitální knihovna** – API v7 `https://api.ceskadigitalniknihovna.cz/search/api/client/v7.0/search?q=…&defType=edismax&qf=text_ocr&fq=model:page` a text stránky `…/items/{pid}/ocr/text`. Parametr `hl.fragsize` vrací HTTP 400. Nový nástroj tools/kramerius7.py. Po ~25 rychlých požadavcích vrátila 403 → do slusne.py přidat vlastní limit pro api.ceskadigitalniknihovna.cz (např. 1 dotaz za 5 s) a do skillu doporučit stahovat OCR po menších dávkách.

## Česká digitální knihovna – stahování textů z cloudu nefunguje (19. 11. 2026)
- Endpoint `items/{pid}/ocr/text` odmítal (HTTP 403) i při 1 dotazu za 40 s; 4 stopky za 24 h, poslední hned prvním dotazem po skončení stopky. Prohledávání (`search`) šlo, hromadné čtení textů ne.
- Pro skill: hromadný sběr textů z CDK nepoužívat; ze skriptu jen vyhledat seznam stránek (pár dotazů) a nejnadějnější stránky (do ~10–15) předat uživateli k ručnímu prohlédnutí s odkazy `https://www.ceskadigitalniknihovna.cz/uuid/<pid>`.

## Nápad: stránka o celém rodu (19. 11. 2026)
- Uživatel chtěl samostatnou sekci o celém rodu (šlechtické větve, souvislosti mimo přímou linii). Udělal jsem obecný mechanismus: `data/rod_<jméno>.json` → stránka `/rod-<jméno>/` (web/src/pages/rod-[jmeno].astro) + odkaz v menu; export_web.py ji zapíše do `src/generated/rodove_stranky.json` a kontroluje v ní odkazy na osoby.
- Obsah: úvod, erb (SVG podle blasonu), schéma napojení (uzly ve sloupcích/řádcích, hrany doc/lit/hyp/nejiste/svedek), časová osa, větve, další nositelé jména se stavem jistoty, otevřené otázky, zdroje. Mohlo by se hodit do skillu pro všechny rody se zajímavou historií.
- (19. 11.) Profily osob zobrazují „Zajímavosti“, které na osobu odkazují (web/src/lib/zajimavosti.js + components/ZajimavostiOsoby.astro): oddíl ## v zajimavosti.md s odkazem /osoba/<slug>/ nebo /rod-<jméno>/<id>/ → karta s ukázkou a proklikem na kotvu nadpisu. Hodilo by se do skillu obecně.

- 21. 11. 2026 – `tools/kramerius7_uryvky.py`: ČDK (API v7) teď vrací klíče ve `highlighting` jako „root_pid!pid“, takže nástroj ukládal prázdné úryvky. Opraveno (klíč se bere za posledním „!“) – vhodné převzít do skillu.

- 21. 11. 2026 – Díla nedostupná na trhu (DNNT) v NDK: uživatel si může za 100 Kč/rok zřídit vzdálenou registraci NK ČR přes bankovní identitu (registrace.nkp.cz) a pak číst na ndk.cz stránky s licencí „dnnto“ (noviny 20. století – parte, blahopřání, oznámení sňatků). Agent je najde přes API ČDK (úryvky + pole licenses/licenses_of_ancestors) a pošle uživateli seznam odkazů ndk.cz/uuid/<pid>. Stálo by za to přidat do skillu jako standardní krok i jako pomocný nástroj (výpis neveřejných stránek s licencí dnnto pro uživatele).

- 21. 11. 2026 – Nový stav osoby `st="lit"` („z rodopisné literatury“) pro přímé předky známé jen z rodopisů (Gotha, Sinapius), bez matričního zápisu – dřív chyběl a nutil volit mezi „prob“ a „doc“. Doplněno v data/osoby.py (komentář), tools/kontrola.py, tools/export_web.py (STATUS), web/src/lib/data.js (statusClass) a global.css (.st-lit). Ve skillu doplnit do popisu stavů.
- 21. 11. 2026 – Zásada pro rodové stránky: každá osoba ve stromu rodu, o které víme víc než pár údajů, má mít vlastní profil (osoba z přímé linie → odkaz `osoba`, příbuzný → vlastní `profily.<id>`); souhrnný profil (např. „rodopis“) jen jako přehled s odkazy, ne jako cíl kliknutí z kartičky. Jan to výslovně chtěl („když kliknu na Christoph Heinrich, očekávám informace přímo o něm“).

- 21. 11. 2026 – **ZA Opava (digi.archives.cz) blokuje z cloudového prostředí i prohlížeč Playwright**: hned první stránka přesměruje na Radware Bot Manager (validate.perfdrive.com) s CAPTCHA. Neobcházet; Dvorce a další opavské matriky jen přes ChatGPT nebo v Janově prohlížeči (lokální sezení). Odblokování jen e-mailem podpory archivu – rozhodnutí na Janovi.
- 21. 11. 2026 – **ANNO (anno.onb.ac.at) z cloudu nejde**: proxy tunel se otevře, ale server spojení při TLS resetuje (blokuje zřejmě IP datacenter). Nejde o síťové pravidlo prostředí – úprava prostředí nepomůže. ANNO jen přes ChatGPT nebo lokální sezení.
- 21. 11. 2026 – **SBC (sbc.org.pl), jednotlivé stránky z velkých PDF:** u linearizovaných PDF (např. Blažek, Content 4112 a 4028) jde stránku vytáhnout přes HTTP Range (hlavička + xref na konci + objekty stránky, řádově 1–7 MB). U nelinearizovaných PDF (Gotha freiherrlich, soubory i635235-…/i178618-…) to NEJDE: pypdf se ztratí v xref proudech a stáhne prakticky celý soubor (stalo se jednou: Gotha 1886, 52 MB). Pro tyto svazky raději ChatGPT, nebo nejdřív ověřit, že PDF je linearizované (/Linearized v prvních bajtech). Nástroj by do skillu stál za to doplnit jako tools/sbc_strana.py s touto kontrolou.
