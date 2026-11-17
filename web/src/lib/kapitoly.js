// Kapitoly příběhu: generated/pribehy/*.md (zdroj data/pribehy/), řazené podle čísla na začátku názvu souboru.
const mods = import.meta.glob('../generated/pribehy/*.md', { eager: true });
export const kapitoly = Object.entries(mods)
  .map(([path, m]) => {
    const file = path.split('/').pop().replace(/\.md$/, '');
    return { slug: file.replace(/^\d+-/, ''), file, fm: m.frontmatter ?? {}, Content: m.Content };
  })
  .sort((a, b) => a.file.localeCompare(b.file));
