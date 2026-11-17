import fs from 'fs';
import path from 'path';

function getPages(dir) {
  let res = [];
  for (const item of fs.readdirSync(dir)) {
    if (item.startsWith('.') || item === 'node_modules') continue;
    const full = path.join(dir, item);
    const stat = fs.statSync(full);
    if (stat.isDirectory()) {
      if (item === 'en') {
        for (const enItem of fs.readdirSync(full)) {
          if (enItem.endsWith('.html')) res.push(path.join('en', enItem));
        }
      }
    } else if (item.endsWith('.html')) {
      res.push(item);
    }
  }
  return res;
}

const baseDir = 'Calcolatore_Pendenza';
const pages = getPages(baseDir);

function buildCapsule(isEn) {
  const itOpt = `<option value="it"${!isEn ? ' selected' : ''}>IT</option>`;
  const enOpt = `<option value="en"${isEn ? ' selected' : ''}>EN</option>`;
  const titleText = isEn ? 'Toggle Light/Dark Theme' : 'Cambia Tema Chiaro/Scuro';
  return `<div class="omni-control-capsule">
                    <select id="langSelect" data-lang-switcher class="omni-capsule-btn" aria-label="Language Selector">
                        ${isEn ? enOpt + '\n                        ' + itOpt : itOpt + '\n                        ' + enOpt}
                    </select>
                    <span class="omni-capsule-divider"></span>
                    <button type="button" id="darkModeBtn" onclick="toggleDarkMode()" class="omni-capsule-btn" title="${titleText}" aria-label="${titleText}">🌙</button>
                </div>`;
}

let modifiedCount = 0;

for (const p of pages) {
  if (p === 'logo-preview.html') continue;
  const filePath = path.join(baseDir, p);
  let html = fs.readFileSync(filePath, 'utf8');
  const isEn = p.startsWith('en/');

  if (p === 'index.html') {
    html = html.replace(
      `<div class="relative">\n                    <button type="button" id="mainDeskBtn"`,
      `<div class="relative hidden md:block">\n                    <button type="button" id="mainDeskBtn"`
    );
    html = html.replace(
      `id="headerInstallBtn" class="inline-flex items-center justify-center gap-1.5 h-8 w-8 sm:w-auto px-1.5 sm:px-2.5 text-xs font-bold text-slate-700 bg-slate-100 hover:bg-slate-200 active:scale-95 rounded-xl border border-slate-200 transition shadow-2xs cursor-pointer omni-header-btn"`,
      `id="headerInstallBtn" class="hidden sm:inline-flex items-center justify-center gap-1.5 h-8 w-8 sm:w-auto px-1.5 sm:px-2.5 text-xs font-bold text-slate-700 bg-slate-100 hover:bg-slate-200 active:scale-95 rounded-xl border border-slate-200 transition shadow-2xs cursor-pointer omni-header-btn"`
    );
    const oldIndexControlsRegex = /<div class="relative inline-block text-left">\s*<button type="button" id="darkModeBtn"[\s\S]*?<\/select>\s*<\/div>/i;
    if (oldIndexControlsRegex.test(html)) {
      html = html.replace(oldIndexControlsRegex, buildCapsule(false));
      fs.writeFileSync(filePath, html, 'utf8');
      modifiedCount++;
      console.log('index.html updated successfully');
    } else {
      console.error('COULD NOT MATCH index.html controls!');
    }
  } else if (['calcolatrice.html', 'orologio.html'].includes(p)) {
    const deskControlsRegex = /<button type="button" id="darkModeBtn"[\s\S]*?<\/select>/i;
    if (deskControlsRegex.test(html)) {
      html = html.replace(deskControlsRegex, buildCapsule(false));
      html = html.replace(`class="text-xs font-bold text-slate-400 hover:text-white transition px-2 py-1 omni-header-btn omni-header-btn--wide"`, `class="hidden sm:inline-flex text-xs font-bold text-slate-400 hover:text-white transition px-2 py-1 omni-header-btn omni-header-btn--wide"`);
      fs.writeFileSync(filePath, html, 'utf8');
      modifiedCount++;
      console.log(`${p} updated successfully`);
    } else {
      console.error(`COULD NOT MATCH ${p} controls!`);
    }
  } else if (p === 'memo.html') {
    const memoRegex = /<button type="button" id="darkModeBtn"[\s\S]*?<\/select>/i;
    if (memoRegex.test(html)) {
      html = html.replace(memoRegex, buildCapsule(false));
      html = html.replace(`class="text-xs font-bold text-slate-400 hover:text-white transition px-2 py-1 omni-header-btn omni-header-btn--wide"`, `class="hidden sm:inline-flex text-xs font-bold text-slate-400 hover:text-white transition px-2 py-1 omni-header-btn omni-header-btn--wide"`);
      fs.writeFileSync(filePath, html, 'utf8');
      modifiedCount++;
      console.log('memo.html updated successfully');
    }
  } else if (p === 'partnership.html') {
    const partRegex = /<button type="button" id="darkModeBtn"[\s\S]*?<\/select>/i;
    if (partRegex.test(html)) {
      html = html.replace(partRegex, buildCapsule(false));
      html = html.replace(`id="navBackBtn" class="text-xs sm:text-sm font-bold text-slate-600 hover:text-blue-600 bg-slate-100 hover:bg-slate-200 px-3 py-1.5 rounded-xl border border-slate-200 transition flex items-center gap-1 omni-header-btn omni-header-btn--wide"`, `id="navBackBtn" class="hidden sm:inline-flex text-xs sm:text-sm font-bold text-slate-600 hover:text-blue-600 bg-slate-100 hover:bg-slate-200 px-3 py-1.5 rounded-xl border border-slate-200 transition items-center gap-1 omni-header-btn omni-header-btn--wide"`);
      fs.writeFileSync(filePath, html, 'utf8');
      modifiedCount++;
      console.log('partnership.html updated successfully');
    }
  } else if (p === 'legal.html') {
    const legRegex = /<select id="langSelect"[\s\S]*?<\/select>/i;
    if (legRegex.test(html)) {
      html = html.replace(legRegex, buildCapsule(false));
      html = html.replace(`class="text-xs font-bold text-blue-600 hover:text-blue-800 transition flex items-center gap-1 omni-header-btn omni-header-btn--wide"`, `class="hidden sm:inline-flex text-xs font-bold text-blue-600 hover:text-blue-800 transition items-center gap-1 omni-header-btn omni-header-btn--wide"`);
      fs.writeFileSync(filePath, html, 'utf8');
      modifiedCount++;
      console.log('legal.html updated successfully');
    }
  } else {
    // 38 standard calculators (19 IT + 19 EN)
    html = html.replace(
      `<div class="relative min-w-0 flex-1 sm:flex-none">`,
      `<div class="relative min-w-0 flex-1 sm:flex-none hidden md:block">`
    );

    html = html.replace(
      `<span class="hidden sm:inline text-slate-300">/</span>`,
      `<span class="hidden md:inline text-slate-300">/</span>`
    );

    html = html.replace(
      `id="headerHelpBtn" class="no-print inline-flex items-center justify-center gap-1 h-8 w-8 sm:w-auto px-1.5 sm:px-2.5 text-xs font-bold text-amber-800 bg-amber-50 hover:bg-amber-100 active:scale-95 rounded-xl border border-amber-200 transition shadow-2xs cursor-pointer omni-header-btn"`,
      `id="headerHelpBtn" class="no-print hidden md:inline-flex items-center justify-center gap-1 h-8 w-8 sm:w-auto px-1.5 sm:px-2.5 text-xs font-bold text-amber-800 bg-amber-50 hover:bg-amber-100 active:scale-95 rounded-xl border border-amber-200 transition shadow-2xs cursor-pointer omni-header-btn"`
    );

    html = html.replace(
      `id="headerInstallBtn" class="no-print inline-flex items-center justify-center gap-1.5 h-8 w-8 sm:w-auto px-1.5 sm:px-2.5 text-xs font-bold text-slate-700 bg-slate-100 hover:bg-slate-200 active:scale-95 rounded-xl border border-slate-200 transition shadow-2xs cursor-pointer omni-header-btn"`,
      `id="headerInstallBtn" class="no-print hidden sm:inline-flex items-center justify-center gap-1.5 h-8 w-8 sm:w-auto px-1.5 sm:px-2.5 text-xs font-bold text-slate-700 bg-slate-100 hover:bg-slate-200 active:scale-95 rounded-xl border border-slate-200 transition shadow-2xs cursor-pointer omni-header-btn"`
    );

    html = html.replace(/<button type="button" id="darkModeBtn"[\s\S]*?<\/button>\s*/i, "");

    html = html.replace(/<div class="relative sm:hidden" id="omniMobileMenuWrap">[\s\S]*?<\/div>\s*<\/div>\s*<\/div>\s*<\/header>/i, "</div></div></header>");

    const langSelectRegex = /<select id="langSelect"[\s\S]*?<\/select>/i;
    if (langSelectRegex.test(html)) {
      html = html.replace(langSelectRegex, buildCapsule(isEn));
      fs.writeFileSync(filePath, html, 'utf8');
      modifiedCount++;
    } else {
      console.error(`COULD NOT MATCH langSelect in ${p}!`);
    }
  }
}

console.log(`Successfully updated ${modifiedCount} / ${pages.length - 1} pages.`);
