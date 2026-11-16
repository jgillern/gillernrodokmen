# Přímí předci podle Kekulého čísel: 1 = výchozí osoba (ten, pro koho rodokmen děláme),
# otec osoby n má číslo 2n, matka 2n+1. Tedy 2 = otec, 3 = matka, 4–7 prarodiče, 8–15 pradědečci a prababičky…
#
# Každá osoba:  číslo: dict(n="Jméno Příjmení", y="1850–1910", st="doc", f=[...], r=[...], note="...")
#   n    jméno; ženy rodným příjmením („Anna Dvořáková“), u nejistého čtení otazník („Marie Špalková (?)“)
#   y    roky života pro přehledy: "* 1931" (žije / úmrtí neznámé), "1850–1910", "asi 1720–1785", "1680 – před 1740"
#   st   stav doložení:  doc  = doloženo matrikou (čteno přímo ze snímku)
#                        prob = pravděpodobné (shoda údajů, ale ne přímý doklad)
#                        fam  = údaj od rodiny / z rodinného dokumentu
#                        mh   = jen z cizího rodokmenu na internetu (MyHeritage, Geni…) – neověřeno
#                        unk  = neznámé (jen místo v rodokmenu)
#   f    fakta jako krátké věty: "* 12. 3. 1873 Hořice čp. 477", "kovář", "× 28. 1. 1897 Anna Stejskalová", "† 14. 5. 1902"
#        (* narození, × sňatek, † úmrtí – podle těchto značek web pozná sňatky a místa pro mapu)
#   r    klíče zápisů z data/zaznamy.json, které osobu dokládají
#   note poznámka: proč je údaj nejistý, rozpory, odkud se vzal
#   sex  jen u osoby 1: "M" nebo "F" (u ostatních plyne z čísla)
# Žijící lidé: jen jméno a rok narození (soukromí), note="Žijící – údaje jen základní."
# Neznámý otec nemanželského dítěte: dict(n="otec neuveden", st="unk", f=[], note="…")

P = {
    1: dict(n="Jan Gillern", y="* 1990", st="fam", sex="M", f=[], note="Žijící – údaje jen základní. Výchozí osoba rodokmenu."),
    2: dict(n="Jiří Gillern", y="asi 1955 – asi 2015", st="fam", f=["* asi 1955 (snad Praha)", "telekomunikační technik", "† asi 2015", "pohřben Praha-Hrnčíře"], note="Otec Jana. Údaje od Jana Gillerna (16. 11. 2026), roky i místo narození jen odhadem."),
    3: dict(n="Zuzana Myslíková", y="", st="fam", f=[], note="Matka Jana, provdaná Gillernová. Údaj od Jana Gillerna (16. 11. 2026)."),
    4: dict(n="Augustýn Gillern", y="", st="fam", f=["pohřben Praha-Hrnčíře"], note="Otec Jiřího. Údaj od Jana Gillerna (16. 11. 2026). Na hřbitově v Hrnčířích leží i jeho rodiče a syn Jiří."),
    5: dict(n="Božena (rodné příjmení?)", y="", st="fam", f=[], note="Matka Jiřího, provdaná Gillernová. Rodné příjmení zatím neznámé."),
    6: dict(n="Vladimír Myslík", y="1930–2024", st="fam", f=["* 6. 5. 1930 Zdíkov (okr. Prachatice)", "† 23. 8. 2024 Český Brod"], note="Otec Zuzany. Údaje z jeho úmrtního listu (matrika Český Brod 2024), kopii poslal Jan Gillern 16. 11. 2026."),
    7: dict(n="Milada Beranová", y="* 1937", st="fam", f=["* 1937 Pravonín čp. 72"], note="Matka Zuzany, provdaná Myslíková. Rodný list Milady Beranové (MNV Pravonín 1952, podle matriky Pravonín sv. XXVI s. 155), foto od Jana Gillerna 16. 11. 2026. Zda žije, zatím nevíme – proto jen rok."),
    14: dict(n="Josef Beran", y="* 1910", st="fam", f=["* 3. 6. 1910 Velká Jesenice", "majitel cihelny v Pravoníně čp. 72 (1937)"], note="Otec Milady. Rodný list Milady Beranové (MNV Pravonín 1952, podle matriky Pravonín sv. XXVI s. 155), foto od Jana Gillerna 16. 11. 2026."),
    15: dict(n="Ludmila Slunečková", y="* 1916", st="fam", f=["* 7. 4. 1916 Buková"], note="Matka Milady. Která Buková, zatím neurčeno. Rodný list Milady Beranové (MNV Pravonín 1952, podle matriky Pravonín sv. XXVI s. 155), foto od Jana Gillerna 16. 11. 2026."),
    28: dict(n="Josef Beran", y="", st="fam", f=[], note="Otec Josefa Berana (* 1910). Jen jméno z rodného listu vnučky Milady (1952)."),
    29: dict(n="Emilie Kozáková", y="", st="fam", f=[], note="Matka Josefa Berana (* 1910). Jen jméno z rodného listu vnučky Milady (1952)."),
    30: dict(n="František Sluneček", y="* 1888", st="doc", f=["* 27. 11. 1888 Tisek č. 17", "obuvník v Bukové č. 8 (1914)", "× 12. 9. 1914 Pravonín Ludmila Svatková", "obchodník (1924, svědek na svatbě švagrové Augustiny Svatkové)"], r=["o_1914_slunecek_svatkova"], note="Otec Ludmily Slunečkové (* 1916). Sňatek čten ze snímku (Pravonín 26, s. 194); datum a místo narození jsou z poznámky v zápisu o sňatku (matr. N XXIII s. 298) – samotný zápis o narození zatím nečten."),
    31: dict(n="Ludmila Svatková", y="* 1893", st="doc", f=["* 18. 10. 1893 Buková č. 5", "× 12. 9. 1914 Pravonín František Sluneček"], r=["n_1893_svatkova_ludmila", "o_1914_slunecek_svatkova"], note="Matka Ludmily Slunečkové (* 1916). V matrice psána „Lidmila Svátková“. Sestry (podle sňatků v Bukové): Marie * 1881 (× 1905 Jan Šimánek), Anežka * 1898 (× 1922), Augustina * 1900 (× 1924 Josef Kuklík)."),
    60: dict(n="Alois Sluneček", y="", st="doc", f=["lokynář (?) v Bukové č. 8 (1914)"], r=["o_1914_slunecek_svatkova"], note="Otec Františka Slunečka. Ze zápisu o sňatku syna (1914), kde byl i svědkem. Povolání nejasně čitelné. Snad týž Alois Sluneček, jehož dcera Marie (* 1902 Tisek 17) se vdala 1925 – tehdy už „zemřelý“."),
    61: dict(n="Josefa Píšová (?)", y="", st="doc", f=[], r=["o_1914_slunecek_svatkova"], note="Matka Františka Slunečka, dcera Jana Píši (?) z Tisku č. 17. Příjmení nejistě čteno (v zápisu 1925 snad „Čížová“?)."),
    62: dict(n="Jan Svatek", y="", st="doc", f=["krejčí v Bukové (1893)", "chalupník v Bukové č. 5 (1914)"], r=["n_1893_svatkova_ludmila", "o_1914_slunecek_svatkova"], note="Otec Ludmily Svatkové. V matrikách psán Svátek i Svatek. Syn Františka Svátka ze Bzové č. 1 (okr. Mladá Vožice)."),
    63: dict(n="Marie Bezkočková", y="", st="doc", f=[], r=["n_1893_svatkova_ludmila", "o_1914_slunecek_svatkova"], note="Matka Ludmily Svatkové, dcera Jana Bezkočky, domkáře z Vitína č. 8 (okr. Sedlčany). Příjmení psáno Bezkočka (1893), Berkočka (1914), Bezkoška (1905)."),
    124: dict(n="František Svátek", y="", st="doc", f=["rolník ve Bzové č. 1 (okr. Mladá Vožice)"], r=["n_1893_svatkova_ludmila"], note="Otec Jana Svatka. Jen ze zápisu o narození vnučky Ludmily (1893)."),
    125: dict(n="Barbora Svátková (?)", y="", st="doc", f=[], r=["n_1893_svatkova_ludmila"], note="Matka Jana Svatka, „rodem Svátkova (?) ze Bzové“ – rodné příjmení nejistě čteno. Jen ze zápisu o narození vnučky Ludmily (1893)."),
    126: dict(n="Jan Bezkočka", y="", st="doc", f=["domkář ve Vitíně č. 8 (okr. Sedlčany)"], r=["n_1893_svatkova_ludmila"], note="Otec Marie Bezkočkové. Jen ze zápisu o narození vnučky Ludmily (1893)."),
    127: dict(n="Marie Zelenková", y="", st="doc", f=[], r=["n_1893_svatkova_ludmila"], note="Matka Marie Bezkočkové, dcera Josefa Zelenky z Nechvalic. Jen ze zápisu o narození vnučky Ludmily (1893)."),
}

# Rody = osm větví podle pradědečků a prababiček (čísla 8–15). Doplňte, jakmile je znáte:
# 8: ("Novákové", "Jedna věta, kdo to byli a odkud – ukáže se na webu u rodu."),
LINES = {
}

# Příbuzní mimo přímou linii (sourozenci, strýcové…): k = číslo předka, ke kterému patří.
# dict(k=16, n="Josef Novák (1865–1920)", t="Bratr Jana. Kovář v …", r=["klic_zapisu"])
SIDE = [
    dict(k=4, n="Jan Gillern", t="Snad bratr Augustýna (údaj od rodiny, nejistý). Olešovice u Kamenice (okr. Praha-východ); manželka Anna Gillernová. V knize Kamenice v proměnách věků (2010) se zmiňuje Jan G. a Jan G. ml.", r=[]),
]

# Rozpory a otevřené otázky (na web do „Co hledáme“) jako dvojice (otázka, odpověď). Odpověď začněte
# „Vyřešeno: …“ (na webu se skryje), „Hypotéza: …“ nebo „Otevřené: …“. Jde na web – nic citlivého.
# ("Kdy se narodil Jan Novák?", "Otevřené: rodina říká 1850, v Holicích 1848–1852 nenalezen.")
ISSUES = [
]

# Hypotézy o původu rodu nad rámec doložené linie (zobrazí se na stránce rodu):
# dict(rod=8, nadpis="Hypotéza: Novákové z Lhoty", text="…", polozky=[("Jan Novák", "kmotr 1681…")], zaznamy=["klic"])
HYPOTEZY = [
]

# Předek v rodokmenu vícekrát (příbuzní rodiče): {alias: hlavní číslo}, např. {350: 140}
SAME = {}
