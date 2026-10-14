// Gera os PNGs do carrossel (1080x1350) a partir de slides.html.
// Uso: node render.mjs   (fotos opcionais em fotos/gugu-dada.jpg,
//      fotos/castelo-ra-tim-bum.jpg e fotos/quintal-da-cultura.jpg)
//
// Além dos slides prontos, gera em png/camadas/ as duas camadas dos slides
// de marca (fundo sem fita/carimbo e só fita/carimbo) e png/molduras.json,
// usados pelo montador.html para encaixar a foto da embalagem.
import { chromium } from 'playwright';
import { mkdirSync, rmSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const dir = dirname(fileURLToPath(import.meta.url));
const outDir = join(dir, 'png');
const camadasDir = join(outDir, 'camadas');
rmSync(outDir, { recursive: true, force: true });
mkdirSync(camadasDir, { recursive: true });

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 1400 } });
await page.goto(pathToFileURL(join(dir, 'slides.html')).href, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);

const nome = (i) => `slide-${String(i + 1).padStart(2, '0')}`;
const slides = await page.$$('.slide');
for (const [i, slide] of slides.entries()) {
  await slide.screenshot({ path: join(outDir, `${nome(i)}.png`) });
}

// Moldura da foto: retângulo sem rotação + centro e ângulo da polaroid
const molduras = await page.$$eval('[data-polaroid]', (els) =>
  els.map((pol) => {
    const slide = pol.closest('.slide');
    const foto = pol.querySelector('.foto');
    const t = pol.style.transform;
    pol.style.transform = 'none';
    const s = slide.getBoundingClientRect();
    const p = pol.getBoundingClientRect();
    const f = foto.getBoundingClientRect();
    pol.style.transform = t;
    const m = new DOMMatrix(getComputedStyle(pol).transform);
    return {
      slide: slide.id,
      foto: foto.dataset.foto,
      x: Math.round(f.left - s.left),
      y: Math.round(f.top - s.top),
      w: Math.round(f.width),
      h: Math.round(f.height),
      cx: Math.round(p.left - s.left + p.width / 2),
      cy: Math.round(p.top - s.top + p.height / 2),
      graus: Math.round((Math.atan2(m.b, m.a) * 180) / Math.PI * 100) / 100,
    };
  })
);
writeFileSync(join(outDir, 'molduras.json'), JSON.stringify(molduras, null, 2) + '\n');

// Camadas dos slides de marca
const idxMarca = await page.$$eval('.slide', (els) =>
  els.map((el, i) => (el.querySelector('[data-polaroid]') ? i : -1)).filter((i) => i >= 0)
);
const estilo = await page.addStyleTag({ content: '.sobre { visibility: hidden !important; }' });
for (const i of idxMarca) await slides[i].screenshot({ path: join(camadasDir, `${nome(i)}-base.png`) });
await estilo.evaluate((el) => el.remove());
await page.addStyleTag({
  content: `
    body { background: transparent !important; }
    .slide { background: transparent !important; }
    .slide::after { display: none !important; }
    .slide, .slide * { visibility: hidden !important; }
    .slide .sobre, .slide .sobre * { visibility: visible !important; }
    .polaroid { box-shadow: none !important; }`,
});
// os slides ficam invisíveis aqui, então recorta a página inteira na posição de cada um
for (const i of idxMarca) {
  const clip = await slides[i].evaluate((el) => {
    const r = el.getBoundingClientRect();
    return { x: r.left + scrollX, y: r.top + scrollY, width: r.width, height: r.height };
  });
  await page.screenshot({ path: join(camadasDir, `${nome(i)}-sobre.png`), clip, fullPage: true, omitBackground: true });
}

await browser.close();
console.log(`${slides.length} slides em ${outDir}`);
