// Gera os PNGs do carrossel (1080x1350) a partir de slides.html.
// Uso: node render.mjs   (fotos opcionais em fotos/gugu-dada.jpg,
//      fotos/castelo-ra-tim-bum.jpg e fotos/quintal-da-cultura.jpg)
import { chromium } from 'playwright';
import { mkdirSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const dir = dirname(fileURLToPath(import.meta.url));
const outDir = join(dir, 'png');
mkdirSync(outDir, { recursive: true });

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 1400 } });
await page.goto(pathToFileURL(join(dir, 'slides.html')).href, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);

const slides = await page.$$('.slide');
for (const [i, slide] of slides.entries()) {
  await slide.screenshot({ path: join(outDir, `slide-${String(i + 1).padStart(2, '0')}.png`) });
}

// Posição de cada moldura de foto dentro do slide (usada pelo montador de fotos)
const molduras = await page.$$eval('.foto', (els) =>
  els.map((el) => {
    const s = el.closest('.slide').getBoundingClientRect();
    const r = el.getBoundingClientRect();
    return {
      slide: el.closest('.slide').id,
      foto: el.dataset.foto,
      x: Math.round(r.left - s.left),
      y: Math.round(r.top - s.top),
      w: Math.round(r.width),
      h: Math.round(r.height),
    };
  })
);
writeFileSync(join(outDir, 'molduras.json'), JSON.stringify(molduras, null, 2) + '\n');

await browser.close();
console.log(`${slides.length} slides em ${outDir}`);
