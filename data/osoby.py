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
    30: dict(n="František Sluneček", y="", st="fam", f=[], note="Otec Ludmily Slunečkové (* 1916). Jen jméno z rodného listu vnučky Milady (1952)."),
    31: dict(n="Ludmila Svatková", y="", st="fam", f=[], note="Matka Ludmily Slunečkové (* 1916). Jen jméno z rodného listu vnučky Milady (1952)."),
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
