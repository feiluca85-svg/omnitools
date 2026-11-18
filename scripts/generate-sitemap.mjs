// scripts/generate-sitemap.mjs
import fs from 'fs';
import path from 'path';

const BASE_URL = 'https://www.omnitoolslab.com';
const TODAY = new Date().toISOString().split('T')[0]; // e.g. 2026-11-18

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
  let xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">

  <!-- ========================================== -->
  <!-- 1. HOMEPAGE & HUBS                         -->
  <!-- ========================================== -->
  <url>
    <loc>${BASE_URL}/</loc>
    <xhtml:link rel="alternate" hreflang="it" href="${BASE_URL}/" />
    <xhtml:link rel="alternate" hreflang="en-US" href="${BASE_URL}/?lang=en" />
    <xhtml:link rel="alternate" hreflang="en" href="${BASE_URL}/?lang=en" />
    <xhtml:link rel="alternate" hreflang="x-default" href="${BASE_URL}/" />
    <lastmod>${TODAY}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
`;

  // Institutional Pages (Legal, Partnership)
  const INSTITUTIONAL = [
    { it: '/legal', priority: '0.5', changefreq: 'monthly', comment: 'Legal Notice & Privacy' },
    { it: '/partnership', priority: '0.6', changefreq: 'monthly', comment: 'B2B Technical Sponsorship' }
  ];

  xml += `
  <!-- ========================================== -->
  <!-- 2. INSTITUTIONAL PAGES                     -->
  <!-- ========================================== -->`;

  for (const inst of INSTITUTIONAL) {
    xml += `
  <!-- ${inst.comment} -->
  <url>
    <loc>${BASE_URL}${inst.it}</loc>
    <xhtml:link rel="alternate" hreflang="it" href="${BASE_URL}${inst.it}" />
    <xhtml:link rel="alternate" hreflang="en-US" href="${BASE_URL}${inst.it}?lang=en" />
    <xhtml:link rel="alternate" hreflang="en" href="${BASE_URL}${inst.it}?lang=en" />
    <xhtml:link rel="alternate" hreflang="x-default" href="${BASE_URL}${inst.it}" />
    <lastmod>${TODAY}</lastmod>
    <changefreq>${inst.changefreq}</changefreq>
    <priority>${inst.priority}</priority>
  </url>
`;
  }

  // 22 Pairs of Calculators: Both IT and EN URLs with full cross-referencing
  xml += `
  <!-- ========================================== -->
  <!-- 3. TECHNICAL CALCULATORS (22 BILINGUAL PAIRS) -->
  <!-- ========================================== -->`;

  let currentCat = '';
  for (const pair of TOOL_PAIRS) {
    if (pair.cat !== currentCat) {
      currentCat = pair.cat;
      xml += `\n  <!-- DIVISION: ${currentCat.toUpperCase()} -->`;
    }

    // A. Italian Entry
    xml += `
  <url>
    <loc>${BASE_URL}${pair.it}</loc>
    <xhtml:link rel="alternate" hreflang="it" href="${BASE_URL}${pair.it}" />
    <xhtml:link rel="alternate" hreflang="en-US" href="${BASE_URL}${pair.en}" />
    <xhtml:link rel="alternate" hreflang="en" href="${BASE_URL}${pair.en}" />
    <xhtml:link rel="alternate" hreflang="x-default" href="${BASE_URL}${pair.en}" />
    <lastmod>${TODAY}</lastmod>
    <changefreq>${pair.changefreq}</changefreq>
    <priority>${pair.priority}</priority>
  </url>`;

    // B. English/US Entry
    xml += `
  <url>
    <loc>${BASE_URL}${pair.en}</loc>
    <xhtml:link rel="alternate" hreflang="it" href="${BASE_URL}${pair.it}" />
    <xhtml:link rel="alternate" hreflang="en-US" href="${BASE_URL}${pair.en}" />
    <xhtml:link rel="alternate" hreflang="en" href="${BASE_URL}${pair.en}" />
    <xhtml:link rel="alternate" hreflang="x-default" href="${BASE_URL}${pair.en}" />
    <lastmod>${TODAY}</lastmod>
    <changefreq>${pair.changefreq}</changefreq>
    <priority>${pair.priority}</priority>
  </url>
`;
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

console.log(`[SUCCESS] sitemap.xml generated with ${TOOL_PAIRS.length * 2 + 3} URLs.`);
console.log(`- Production: ${prodPath} (${fs.statSync(prodPath).size} bytes)`);
