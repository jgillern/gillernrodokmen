// Data exported from the research repo by tools/export_web.py (re-run `npm run data` after changes).
import site from '../data/site.json';

export const { people, families, lines, stats, issues, hypotheses, docs, config } = site;
/** Počet rodů slovem pro nadpisy („Osm rodů“). */
export const linesTitle = (n) => (['Žádný rod', 'Jeden rod', 'Dva rody', 'Tři rody', 'Čtyři rody', 'Pět rodů', 'Šest rodů', 'Sedm rodů', 'Osm rodů'][n] ?? `${n} rodů`);
export const root = people[site.root];
export const records = Object.fromEntries(site.records.map((r) => [r.key, r]));
export const recordList = site.records;
export const byK = Object.fromEntries([
  ...Object.values(people).map((p) => [p.k, p]),
  ...Object.entries(site.aliases ?? {}).map(([k, slug]) => [Number(k), people[slug]]),
]);
export const lineByK = Object.fromEntries(Object.values(lines).map((l) => [l.k, l]));

export const href = {
  person: (slug) => `/osoba/${slug}/`,
  family: (id) => `/rodina/${id}/`,
  line: (slug) => `/rod/${slug}/`,
  record: (key) => `/zdroj/${key}/`,
};

/** Sortable number from dates like "12. 5. 1811", "3/1867", "12/1790", "1797". */
export function dateKey(date) {
  const y = (date.match(/\d{4}/) || ['9999'])[0];
  const parts = date.replace(y, '').match(/\d+/g) || [];
  const [d, m] = parts.length >= 2 ? [parts[0], parts[1]] : [0, parts[0] || 0];
  return Number(y) * 10000 + Number(m) * 100 + Number(d);
}

export const genName = (g) =>
  ['výchozí osoba', 'rodiče', 'prarodiče', 'praprarodiče'][g] ?? `${g}. generace (${'pra'.repeat(g - 1)}rodiče)`;

export const statusClass = (st) => ({ doc: 'st-doc', prob: 'st-prob', fam: 'st-fam', mh: 'st-mh' })[st] ?? 'st-unk';

/** Větve (podrody) uvnitř rodu: z config.podrody; každá je otcovská linie od `koren` (Kekulé) nahoru (k → 2k → 4k …). */
export const subLines = (config.podrody ?? []).map((s) => {
  const chain = [];
  for (let k = s.koren; byK[k]; k *= 2) chain.push(byK[k]);
  const oldest = chain[chain.length - 1];
  return { ...s, chain, oldest, color: lineByK[s.rod]?.color ?? '#ccc' };
}).filter((s) => s.chain.length > 0);

/** Filtry (mapa, rody): strana, rod, období. */
export const OBDOBI = [
  { id: 'do1750', name: 'do roku 1750', od: -Infinity, do: 1749 },
  { id: '1750', name: '1750–1799', od: 1750, do: 1799 },
  { id: '1800', name: '1800–1849', od: 1800, do: 1849 },
  { id: '1850', name: '1850–1899', od: 1850, do: 1899 },
  { id: '1900', name: '1900 a později', od: 1900, do: Infinity },
];
/** Rok osoby: první letopočet z let nebo údajů; jinak odhad podle generace (30 let na generaci od kořene). */
export function personYear(p) {
  const m = ((p.years || '') + ' ' + (p.facts || []).join(' ')).match(/1[5-9]\d\d|20\d\d/);
  if (m) return Number(m[0]);
  const rootY = Number(((root.years || '').match(/\d{4}/) || ['1990'])[0]);
  return p.gen != null ? rootY - 30 * p.gen : null;
}
export const obdobiOf = (y) => (y == null ? null : OBDOBI.find((o) => y >= o.od && y <= o.do)?.id ?? null);
/** Strana podle Kekulého čísla: 2, 4–5, 8–11 … otcova; 3, 6–7, 12–15 … matčina; 1 = výchozí osoba. */
export function sideOfK(k) {
  if (!k || k < 2) return 'oba';
  let x = k;
  while (x > 3) x = Math.floor(x / 2);
  return x === 2 ? 'otec' : 'matka';
}
export const sideOf = (p) => sideOfK(p.k);
