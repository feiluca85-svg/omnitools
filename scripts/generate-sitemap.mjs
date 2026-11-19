// scripts/generate-sitemap.mjs
import fs from 'fs';
import path from 'path';

const BASE_URL = 'https://www.omnitoolslab.com';
const TODAY = new Date().toISOString().split('T')[0]; // Current build date YYYY-MM-DD

// 22 Pairs of Technical Calculators (IT Clean Slug <-> EN Clean Slug)
const TOOL_PAIRS = [
  // OmniBuilding (6)
  { it: '/rampe', en: '/en/ramp-slope-calculator', priority: '0.9', changefreq: 'weekly', cat: 'OmniBuilding' },
  { it: '/scale', en: '/en/stair-calculator', priority: '0.9', changefreq: 'weekly', cat: 'OmniBuilding' },
  { it: '/tubi', en: '/en/pipe-slope-calculator', priority: '0.9', changefreq: 'weekly', cat: 'OmniBuilding' },
  { it: '/tetto', en: '/en/roof-pitch-calculator', priority: '0.9', changefreq: 'weekly', cat: 'OmniBuilding' },
  { it: '/taglio', en: '/en/cut-list-optimizer', priority: '0.9', changefreq: 'weekly', cat: 'OmniBuilding' },
  { it: '/piastrelle', en: '/en/tile-grout-calculator', priority: '0.9', changefreq: 'weekly', cat: 'OmniBuilding' },

  // OmniGraph (6)
  { it: '/dorso', en: '/en/book-spine-calculator', priority: '0.85', changefreq: 'weekly', cat: 'OmniGraph' },
  { it: '/dpi', en: '/en/print-resolution-calculator', priority: '0.85', changefreq: 'weekly', cat: 'OmniGraph' },
  { it: '/tinta', en: '/en/pantone-ink-mixing-calculator', priority: '0.85', changefreq: 'weekly', cat: 'OmniGraph' },
  { it: '/barcode', en: '/en/barcode-generator', priority: '0.9', changefreq: 'weekly', cat: 'OmniGraph' },
  { it: '/copertura', en: '/en/cmyk-ink-coverage-calculator', priority: '0.85', changefreq: 'weekly', cat: 'OmniGraph' },
  { it: '/resa', en: '/en/paper-cutting-yield-calculator', priority: '0.85', changefreq: 'weekly', cat: 'OmniGraph' },

  // OmniFinance (6)
  { it: '/mutuo', en: '/en/mortgage-loan-amortization-calculator', priority: '0.95', changefreq: 'weekly', cat: 'OmniFinance' },
  { it: '/pac', en: '/en/compound-interest-calculator', priority: '0.95', changefreq: 'weekly', cat: 'OmniFinance' },
  { it: '/margine', en: '/en/margin-markup-calculator', priority: '0.85', changefreq: 'weekly', cat: 'OmniFinance' },
  { it: '/estinzione', en: '/en/early-mortgage-payoff-calculator', priority: '0.9', changefreq: 'weekly', cat: 'OmniFinance' },
  { it: '/risparmio', en: '/en/savings-goal-calculator', priority: '0.85', changefreq: 'weekly', cat: 'OmniFinance' },
  { it: '/fire', en: '/en/fire-financial-independence-calculator', priority: '0.9', changefreq: 'weekly', cat: 'OmniFinance' },

  // OmniFood (4)
  { it: '/shelflife', en: '/en/shelf-life-calculator', priority: '0.95', changefreq: 'weekly', cat: 'OmniFood' },
  { it: '/nutriexport', en: '/en/nutri-export-converter', priority: '0.95', changefreq: 'weekly', cat: 'OmniFood' },
  { it: '/impasti', en: '/en/batch-scaler-calculator', priority: '0.9', changefreq: 'weekly', cat: 'OmniFood' },
  { it: '/idratazione', en: '/en/hydration-balance-calculator', priority: '0.9', changefreq: 'weekly', cat: 'OmniFood' }
];

function generateSitemapXml() {
  let xml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n`;

  // 1. Homepage & Hubs
  xml += `  <url>\n    <loc>${BASE_URL}/</loc>\n    <xhtml:link rel="alternate" hreflang="it" href="${BASE_URL}/"/>\n    <xhtml:link rel="alternate" hreflang="en-US" href="${BASE_URL}/?lang=en"/>\n    <xhtml:link rel="alternate" hreflang="en" href="${BASE_URL}/?lang=en"/>\n    <xhtml:link rel="alternate" hreflang="x-default" href="${BASE_URL}/"/>\n    <lastmod>${TODAY}</lastmod>\n    <changefreq>daily</changefreq>\n    <priority>1.0</priority>\n  </url>\n`;

  // 2. Institutional Pages (Legal, Partnership)
  const INSTITUTIONAL = [
    { it: '/legal', priority: '0.5', changefreq: 'monthly' },
    { it: '/partnership', priority: '0.6', changefreq: 'monthly' }
  ];

  for (const inst of INSTITUTIONAL) {
    xml += `  <url>\n    <loc>${BASE_URL}${inst.it}</loc>\n    <xhtml:link rel="alternate" hreflang="it" href="${BASE_URL}${inst.it}"/>\n    <xhtml:link rel="alternate" hreflang="en-US" href="${BASE_URL}${inst.it}?lang=en"/>\n    <xhtml:link rel="alternate" hreflang="en" href="${BASE_URL}${inst.it}?lang=en"/>\n    <xhtml:link rel="alternate" hreflang="x-default" href="${BASE_URL}${inst.it}"/>\n    <lastmod>${TODAY}</lastmod>\n    <changefreq>${inst.changefreq}</changefreq>\n    <priority>${inst.priority}</priority>\n  </url>\n`;
  }

  // 3. 22 Pairs of Calculators: Both IT and EN URLs with full cross-referencing
  for (const pair of TOOL_PAIRS) {
    // A. Italian Entry
    xml += `  <url>\n    <loc>${BASE_URL}${pair.it}</loc>\n    <xhtml:link rel="alternate" hreflang="it" href="${BASE_URL}${pair.it}"/>\n    <xhtml:link rel="alternate" hreflang="en-US" href="${BASE_URL}${pair.en}"/>\n    <xhtml:link rel="alternate" hreflang="en" href="${BASE_URL}${pair.en}"/>\n    <xhtml:link rel="alternate" hreflang="x-default" href="${BASE_URL}${pair.en}"/>\n    <lastmod>${TODAY}</lastmod>\n    <changefreq>${pair.changefreq}</changefreq>\n    <priority>${pair.priority}</priority>\n  </url>\n`;

    // B. English/US Entry
    xml += `  <url>\n    <loc>${BASE_URL}${pair.en}</loc>\n    <xhtml:link rel="alternate" hreflang="it" href="${BASE_URL}${pair.it}"/>\n    <xhtml:link rel="alternate" hreflang="en-US" href="${BASE_URL}${pair.en}"/>\n    <xhtml:link rel="alternate" hreflang="en" href="${BASE_URL}${pair.en}"/>\n    <xhtml:link rel="alternate" hreflang="x-default" href="${BASE_URL}${pair.en}"/>\n    <lastmod>${TODAY}</lastmod>\n    <changefreq>${pair.changefreq}</changefreq>\n    <priority>${pair.priority}</priority>\n  </url>\n`;
  }

  xml += `</urlset>\n`;
  return xml;
}

// Write to both production and staging
const sitemapContent = generateSitemapXml();

const prodPath = path.resolve('Calcolatore_Pendenza/sitemap.xml');
const stagingPath = path.resolve('OmniTools_Lab_Test/sitemap.xml');

fs.writeFileSync(prodPath, sitemapContent, 'utf-8');
if (fs.existsSync('OmniTools_Lab_Test')) {
  fs.writeFileSync(stagingPath, sitemapContent, 'utf-8');
}

console.log(`[SUCCESS] sitemap.xml generated with ${TOOL_PAIRS.length * 2 + 3} clean XML URLs.`);
console.log(`- Production: ${prodPath} (${fs.statSync(prodPath).size} bytes)`);
