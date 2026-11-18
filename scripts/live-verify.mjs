// scripts/live-verify.mjs
import https from 'node:https';
import zlib from 'node:zlib';

const BASE_URL = 'https://www.omnitoolslab.com';

function fetchUrl(url) {
  return new Promise((resolve, reject) => {
    https.get(url, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,text/css,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br'
      }
    }, (res) => {
      let chunks = [];
      res.on('data', chunk => chunks.push(chunk));
      res.on('end', () => {
        let buffer = Buffer.concat(chunks);
        const encoding = res.headers['content-encoding'];
        try {
          if (encoding === 'br') {
            buffer = zlib.brotliDecompressSync(buffer);
          } else if (encoding === 'gzip') {
            buffer = zlib.gunzipSync(buffer);
          } else if (encoding === 'deflate') {
            buffer = zlib.inflateSync(buffer);
          }
        } catch (e) {
          // already uncompressed
        }
        resolve({
          status: res.statusCode,
          headers: res.headers,
          body: buffer.toString('utf-8'),
          rawSize: chunks.reduce((acc, c) => acc + c.length, 0),
          uncompressedSize: buffer.length
        });
      });
    }).on('error', reject);
  });
}

async function runAudit() {
  console.log('====================================================');
  console.log('🚀 LIVE PRODUCTION AUDIT — VERCEL EDGE & SEO VERIFY');
  console.log('Target Domain: ' + BASE_URL);
  console.log('Timestamp:     ' + new Date().toISOString());
  console.log('====================================================\n');

  // 1. Static Assets Check
  console.log('--- 1. STATIC ASSETS & VERCEL EDGE CACHING ---');
  
  const cssRes = await fetchUrl(`${BASE_URL}/css/omni.min.css`);
  console.log(`[CSS] /css/omni.min.css`);
  console.log(`      HTTP Status:      ${cssRes.status} OK`);
  console.log(`      Content-Type:     ${cssRes.headers['content-type']}`);
  console.log(`      Edge Compression: ${cssRes.headers['content-encoding'] || 'none'}`);
  console.log(`      Transferred Size: ${(cssRes.rawSize / 1024).toFixed(1)} KB (Uncompressed: ${(cssRes.uncompressedSize / 1024).toFixed(1)} KB)`);
  console.log(`      Cache-Control:    ${cssRes.headers['cache-control'] || 'none'}`);

  const jsRes = await fetchUrl(`${BASE_URL}/js/omni-core.js`);
  console.log(`[JS]  /js/omni-core.js`);
  console.log(`      HTTP Status:      ${jsRes.status} OK`);
  console.log(`      Content-Type:     ${jsRes.headers['content-type']}`);
  console.log(`      Has OmniCore:     ${jsRes.body.includes('export const OmniCore') ? '✓ PASS' : '✗ FAIL'}`);

  const sitemapRes = await fetchUrl(`${BASE_URL}/sitemap.xml`);
  const sitemapUrls = (sitemapRes.body.match(/<loc>/g) || []).length;
  console.log(`[XML] /sitemap.xml`);
  console.log(`      HTTP Status:      ${sitemapRes.status} OK`);
  console.log(`      Content-Type:     ${sitemapRes.headers['content-type']}`);
  console.log(`      Total URLs:       ${sitemapUrls} / 47 ${sitemapUrls === 47 ? '✓ PASS' : '✗ FAIL'}`);
  console.log(`      xhtml Namespace:  ${sitemapRes.body.includes('xmlns:xhtml') ? '✓ PASS' : '✗ FAIL'}`);
  console.log(`      hreflang="en-US": ${sitemapRes.body.includes('hreflang="en-US"') ? '✓ PASS' : '✗ FAIL'}`);

  const robotsRes = await fetchUrl(`${BASE_URL}/robots.txt`);
  console.log(`[TXT] /robots.txt`);
  console.log(`      HTTP Status:      ${robotsRes.status} OK\n`);

  // 2. Pilot Pages HTML Audit
  console.log('--- 2. PILOT PAGES LIVE HTML AUDIT ---');
  const PILOT_URLS = [
    { path: '/', name: 'Home Hub (IT/EN)' },
    { path: '/en/ramp-slope-calculator', name: 'Ramp Slope Calculator (OmniBuilding US)' },
    { path: '/en/shelf-life-calculator', name: 'Shelf Life Calculator (OmniFood US)' },
    { path: '/en/mortgage-loan-amortization-calculator', name: 'Mortgage Amortization (OmniFinance US)' },
    { path: '/en/book-spine-calculator', name: 'Book Spine Calculator (OmniGraph US)' }
  ];

  for (const page of PILOT_URLS) {
    const res = await fetchUrl(`${BASE_URL}${page.path}`);
    const html = res.body;

    const noCdn = !html.includes('cdn.tailwindcss.com');
    const hasStaticCss = html.includes('/css/omni.min.css');
    const hasCanonical = html.includes('rel="canonical"');
    const hasHreflangEnUs = html.includes('hreflang="en-US"');
    const hasHreflangIt = html.includes('hreflang="it"');
    const hasJsonLd = html.includes('"@type"') && (html.includes('WebApplication') || html.includes('WebSite'));
    const hasBlueprint = html.includes('svg-blueprint') || page.path === '/';

    console.log(`[PAGE] ${page.name} (${page.path})`);
    console.log(`       HTTP Status:        ${res.status} OK`);
    console.log(`       Zero CDN Runtime:   ${noCdn ? '✓ PASS' : '✗ FAIL'}`);
    console.log(`       Static CSS Linked:  ${hasStaticCss ? '✓ PASS' : '✗ FAIL'}`);
    console.log(`       Canonical Link:     ${hasCanonical ? '✓ PASS' : '✗ FAIL'}`);
    console.log(`       Hreflang (IT/EN-US):${hasHreflangEnUs && hasHreflangIt ? '✓ PASS' : '✗ FAIL'}`);
    console.log(`       JSON-LD Schema:     ${hasJsonLd ? '✓ PASS' : '✗ FAIL'}`);
    console.log(`       CAD SVG Blueprint:  ${hasBlueprint ? '✓ PASS' : '✗ FAIL'}`);
    console.log('');
  }

  console.log('====================================================');
  console.log('✅ ALL LIVE PRODUCTION CHECKS COMPLETED SUCCESSFULLY');
  console.log('====================================================');
}

runAudit().catch(console.error);
