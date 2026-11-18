import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');

const sitemapPath = path.join(rootDir, 'sitemap.xml');
const keyPath = path.join(rootDir, 'omnitoolsindexnow2026key.txt');

if (!fs.existsSync(sitemapPath)) {
  console.error(`[IndexNow] Sitemap not found at: ${sitemapPath}`);
  process.exit(1);
}

if (!fs.existsSync(keyPath)) {
  console.error(`[IndexNow] Key file not found at: ${keyPath}`);
  process.exit(1);
}

const key = fs.readFileSync(keyPath, 'utf8').trim();
const sitemapContent = fs.readFileSync(sitemapPath, 'utf8');

const urlRegex = /<loc>(https?:\/\/[^<]+)<\/loc>/g;
const urlList = [];
let match;
while ((match = urlRegex.exec(sitemapContent)) !== null) {
  urlList.push(match[1].trim());
}

if (urlList.length === 0) {
  console.error('[IndexNow] No URLs extracted from sitemap.xml');
  process.exit(1);
}

const payload = {
  host: 'www.omnitoolslab.com',
  key: key,
  keyLocation: `https://www.omnitoolslab.com/${path.basename(keyPath)}`,
  urlList: urlList,
};

console.log(`[IndexNow] Preparing submission for ${urlList.length} URLs...`);
console.log(`[IndexNow] Host: ${payload.host}`);
console.log(`[IndexNow] Key: ${payload.key}`);
console.log(`[IndexNow] KeyLocation: ${payload.keyLocation}`);

try {
  const response = await fetch('https://api.indexnow.org/indexnow', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
    },
    body: JSON.stringify(payload),
  });

  const status = response.status;
  const statusText = response.statusText;
  const responseText = await response.text();

  console.log(`[IndexNow] HTTP Status: ${status} ${statusText}`);
  if (responseText) {
    console.log(`[IndexNow] Response Body: ${responseText}`);
  }

  // 200 = OK, 202 = Accepted
  if (status === 200 || status === 202) {
    console.log(`✅ [IndexNow] Successfully submitted ${urlList.length} URLs to IndexNow API!`);
  } else {
    console.warn(`⚠️ [IndexNow] API returned unexpected status code: ${status}`);
  }
} catch (err) {
  console.error(`❌ [IndexNow] Network error connecting to api.indexnow.org:`, err.message);
  process.exit(1);
}
