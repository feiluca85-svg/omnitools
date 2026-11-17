import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');

const TOOLS = [
  // OmniBuilding
  { cat: 'OmniBuilding', itFile: 'rampe.html', enFile: 'en/ramp-slope-calculator.html', itUrl: '/rampe', enUrl: '/en/ramp-slope-calculator', name: 'RampaFacile / RampEasy' },
  { cat: 'OmniBuilding', itFile: 'scale.html', enFile: 'en/stair-calculator.html', itUrl: '/scale', enUrl: '/en/stair-calculator', name: 'ScalaFacile / StairEasy' },
  { cat: 'OmniBuilding', itFile: 'tubi.html', enFile: 'en/pipe-slope-calculator.html', itUrl: '/tubi', enUrl: '/en/pipe-slope-calculator', name: 'ScaricoFacile / PipesEasy' },
  { cat: 'OmniBuilding', itFile: 'tetto.html', enFile: 'en/roof-pitch-calculator.html', itUrl: '/tetto', enUrl: '/en/roof-pitch-calculator', name: 'TettoFacile / RoofEasy' },
  { cat: 'OmniBuilding', itFile: 'taglio.html', enFile: 'en/cut-list-optimizer.html', itUrl: '/taglio', enUrl: '/en/cut-list-optimizer', name: 'TaglioOttimo / OptiCut 1D' },
  { cat: 'OmniBuilding', itFile: 'piastrelle.html', enFile: 'en/tile-grout-calculator.html', itUrl: '/piastrelle', enUrl: '/en/tile-grout-calculator', name: 'PiastrellaFacile / TileEasy' },

  // OmniGraph
  { cat: 'OmniGraph', itFile: 'dorso.html', enFile: 'en/book-spine-calculator.html', itUrl: '/dorso', enUrl: '/en/book-spine-calculator', name: 'DorsoFacile / Book Spine' },
  { cat: 'OmniGraph', itFile: 'dpi.html', enFile: 'en/print-resolution-calculator.html', itUrl: '/dpi', enUrl: '/en/print-resolution-calculator', name: 'RisoluzioneFacile / Print DPI' },
  { cat: 'OmniGraph', itFile: 'tinta.html', enFile: 'en/pantone-ink-mixing-calculator.html', itUrl: '/tinta', enUrl: '/en/pantone-ink-mixing-calculator', name: 'TintaPerfetta / Pantone Ink Mixing' },
  { cat: 'OmniGraph', itFile: 'barcode.html', enFile: 'en/barcode-generator.html', itUrl: '/barcode', enUrl: '/en/barcode-generator', name: 'OmniBarcode / Barcode Generator' },
  { cat: 'OmniGraph', itFile: 'copertura.html', enFile: 'en/cmyk-ink-coverage-calculator.html', itUrl: '/copertura', enUrl: '/en/cmyk-ink-coverage-calculator', name: 'CoperturaFacile / CMYK Ink Coverage' },
  { cat: 'OmniGraph', itFile: 'resa.html', enFile: 'en/paper-cutting-yield-calculator.html', itUrl: '/resa', enUrl: '/en/paper-cutting-yield-calculator', name: 'ResaCarta / Paper Cutting Yield' },

  // OmniFinance
  { cat: 'OmniFinance', itFile: 'mutuo.html', enFile: 'en/mortgage-loan-amortization-calculator.html', itUrl: '/mutuo', enUrl: '/en/mortgage-loan-amortization-calculator', name: 'MutuoFacile / Mortgage Amortization' },
  { cat: 'OmniFinance', itFile: 'pac.html', enFile: 'en/compound-interest-calculator.html', itUrl: '/pac', enUrl: '/en/compound-interest-calculator', name: 'InteresseComposto / Compound Interest' },
  { cat: 'OmniFinance', itFile: 'margine.html', enFile: 'en/margin-markup-calculator.html', itUrl: '/margine', enUrl: '/en/margin-markup-calculator', name: 'MargineFacile / Margin & Markup' },
  { cat: 'OmniFinance', itFile: 'estinzione.html', enFile: 'en/early-mortgage-payoff-calculator.html', itUrl: '/estinzione', enUrl: '/en/early-mortgage-payoff-calculator', name: 'EstinzioneMutuo / Early Payoff' },
  { cat: 'OmniFinance', itFile: 'risparmio.html', enFile: 'en/savings-goal-calculator.html', itUrl: '/risparmio', enUrl: '/en/savings-goal-calculator', name: 'ObiettivoRisparmio / Savings Goal' },
  { cat: 'OmniFinance', itFile: 'fire.html', enFile: 'en/fire-financial-independence-calculator.html', itUrl: '/fire', enUrl: '/en/fire-financial-independence-calculator', name: 'FIRE & Rendita / FIRE Calculator' },

  // OmniFood
  { cat: 'OmniFood', itFile: 'shelflife.html', enFile: 'en/shelf-life-calculator.html', itUrl: '/shelflife', enUrl: '/en/shelf-life-calculator', name: 'ShelfLife Export / Shelf Life Calculator' }
];

const IT_SLUGS = TOOLS.map(t => t.itUrl);
const EN_SLUGS = TOOLS.map(t => t.enUrl);

console.log('='.repeat(70));
console.log('🔍 RUNNING COMPREHENSIVE BILINGUAL ROUTING AUDIT');
console.log('Target directory:', rootDir);
console.log('='.repeat(70));

let issues = [];

// 1. Audit all IT HTML files (root)
const itFiles = fs.readdirSync(rootDir).filter(f => f.endsWith('.html'));
for (const file of itFiles) {
  const filePath = path.join(rootDir, file);
  const content = fs.readFileSync(filePath, 'utf-8');

  // Check html lang
  const htmlLangMatch = content.match(/<html[^>]*lang=["']([^"']+)["']/i);
  if (!htmlLangMatch || !htmlLangMatch[1].startsWith('it')) {
    issues.push(`[LANG_TAG_ERR] ${file} has html lang="${htmlLangMatch ? htmlLangMatch[1] : 'NONE'}" (expected "it")`);
  }

  // Check navigator.language leaks
  if (/navigator\.languages|navigator\.language/i.test(content)) {
    issues.push(`[NAVIGATOR_LEAK] ${file} contains navigator.language / navigator.languages!`);
  }

  // Check <a> links: no navigation link to tools should point to /en/
  // Match <a href="..."
  const hrefMatches = content.matchAll(/<a\s+[^>]*href=["']([^"']+)["'][^>]*>/gi);
  for (const m of hrefMatches) {
    const href = m[1];
    // Ignore external, hash, or mailto
    if (href.startsWith('http') || href.startsWith('#') || href.startsWith('mailto:')) continue;
    
    // Check if it's an en tool link
    for (const enSlug of EN_SLUGS) {
      if (href === enSlug || href.startsWith(enSlug)) {
        issues.push(`[CROSS_LINK_LEAK in IT] ${file} has link to EN tool: "${href}"`);
      }
    }
  }
}

// 2. Audit all EN HTML files (/en)
const enDir = path.join(rootDir, 'en');
const enFiles = fs.readdirSync(enDir).filter(f => f.endsWith('.html'));
for (const file of enFiles) {
  const filePath = path.join(enDir, file);
  const content = fs.readFileSync(filePath, 'utf-8');

  // Check html lang
  const htmlLangMatch = content.match(/<html[^>]*lang=["']([^"']+)["']/i);
  if (!htmlLangMatch || !htmlLangMatch[1].startsWith('en')) {
    issues.push(`[LANG_TAG_ERR] en/${file} has html lang="${htmlLangMatch ? htmlLangMatch[1] : 'NONE'}" (expected "en")`);
  }

  // Check <a> links: no navigation link to tools should point to IT root slugs
  const hrefMatches = content.matchAll(/<a\s+[^>]*href=["']([^"']+)["'][^>]*>/gi);
  for (const m of hrefMatches) {
    const href = m[1];
    if (href.startsWith('http') || href.startsWith('#') || href.startsWith('mailto:')) continue;
    // Check if it matches an IT slug exactly (or .html)
    for (const itSlug of IT_SLUGS) {
      if (href === itSlug || href === itSlug + '.html' || href === itSlug + '/') {
        issues.push(`[CROSS_LINK_LEAK in EN] en/${file} has link to IT tool: "${href}"`);
      }
    }
  }
}

// 3. Audit all 19 Tool Pairs: Bidirectional symmetry (data-mirror-url and target existence)
const tableResults = [];

for (const tool of TOOLS) {
  const itPath = path.join(rootDir, tool.itFile);
  const enPath = path.join(rootDir, tool.enFile);

  const itExists = fs.existsSync(itPath);
  const enExists = fs.existsSync(enPath);

  if (!itExists || !enExists) {
    issues.push(`[FILE_NOT_FOUND] ${tool.name}: it=${itExists}, en=${enExists}`);
    continue;
  }

  const itContent = fs.readFileSync(itPath, 'utf-8');
  const enContent = fs.readFileSync(enPath, 'utf-8');

  // Check data-mirror-url on IT
  const itMirrorMatch = itContent.match(/<body[^>]*data-mirror-url=["']([^"']+)["']/i);
  const itMirror = itMirrorMatch ? itMirrorMatch[1] : '';
  const itToEnValid = (itMirror === tool.enUrl || itMirror === tool.enUrl + '.html');

  // Check data-mirror-url on EN
  const enMirrorMatch = enContent.match(/<body[^>]*data-mirror-url=["']([^"']+)["']/i);
  const enMirror = enMirrorMatch ? enMirrorMatch[1] : '';
  const enToItValid = (enMirror === tool.itUrl || enMirror === tool.itUrl + '.html');

  // Check links in desktop suiteMenuDropdown & mobile dock in IT file
  const itHasCorrectLinks = !itContent.includes(`href="${tool.enUrl}"`) && !itContent.includes(`href="${tool.enUrl}.html"`);
  
  // Check links in EN file
  const enHasCorrectLinks = !enContent.includes(`href="${tool.itUrl}"`) && !enContent.includes(`href="${tool.itUrl}.html"`);

  const passed = itToEnValid && enToItValid && itHasCorrectLinks && enHasCorrectLinks;

  tableResults.push({
    division: tool.cat,
    name: tool.name,
    itUrl: tool.itUrl,
    enUrl: tool.enUrl,
    itMirror: itMirror,
    enMirror: enMirror,
    itToEnValid,
    enToItValid,
    passed
  });
}

// 4. Output results
console.log('\n--- AUDIT ISSUES DETECTED ---');
if (issues.length === 0) {
  console.log('✅ ZERO ISSUES DETECTED! All files passed inspection.');
} else {
  console.log(`❌ Found ${issues.length} issues:`);
  issues.forEach(i => console.log('  -', i));
}

console.log('\n--- 19 TOOLS BILINGUAL ROUTING MATRIX ---');
console.table(tableResults.map(r => ({
  Division: r.division,
  'Tool (IT / EN)': r.name,
  'IT Route': r.itUrl,
  'EN Route': r.enUrl,
  'Switch IT→EN': r.itToEnValid ? `PASS (${r.itMirror})` : `FAIL (${r.itMirror})`,
  'Switch EN→IT': r.enToItValid ? `PASS (${r.enMirror})` : `FAIL (${r.enMirror})`,
  Status: r.passed ? '✅ 100% PASS' : '❌ FAIL'
})));

if (issues.length > 0) {
  process.exit(1);
} else {
  process.exit(0);
}
