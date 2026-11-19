// Zajímavosti podle osob: která zajímavost (oddíl ## v data/zajimavosti.md) odkazuje na danou osobu
// (/osoba/<slug>/) nebo na profil příbuzného (/rod-<jméno>/<id>/). Kotva = slug nadpisu, jak ho dělá Astro.
import { rawContent, getHeadings } from '../generated/zajimavosti.md';

const kotvy = getHeadings().filter((h) => h.depth === 2).map((h) => h.slug);
const oddily = rawContent()
  .split(/^## /m)
  .slice(1)
  .map((blok, i) => {
    const [nadpis, ...zbytek] = blok.split('\n');
    const text = zbytek.join('\n').trim();
    const cisty = text.replace(/\[([^\]]+)\]\([^)]+\)/g, '$1').replace(/[*_`]/g, '').replace(/\s+/g, ' ');
    const odkazy = new Set();
    for (const m of text.matchAll(/\]\((\/[^)\s#]+)/g)) odkazy.add(m[1].replace(/\/?$/, '/'));
    return { nadpis: nadpis.trim(), kotva: kotvy[i], ukazka: cisty.length > 240 ? cisty.slice(0, 240).replace(/\s\S*$/, '') + ' …' : cisty, odkazy };
  });

/** Zajímavosti, které zmiňují stránku s adresou `cesta` (např. "/osoba/jan-pisa-1831/"). */
export const zajimavostiPro = (cesta) => oddily.filter((o) => o.odkazy.has(cesta));
