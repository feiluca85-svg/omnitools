import json

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/translations_hub.json', 'r', encoding='utf-8') as f:
    t_data = json.load(f)

t_json_str = json.dumps(t_data, ensure_ascii=False)

html_code = f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>OmniTools Lab — Calcolatori Tecnici Online: Pendenze Rampe, Scale, Tubi e Dorso</title>
    <meta name="description" content="OmniTools Lab: Suite gratuita di calcolatori tecnici online. Calcolo pendenza rampe disabili e garage (DM 236/89), alzata e pedata scale (Blondel), pendenza tubi scarico (UNI EN 12056), dorso libro e DPI stampa.">
    
    <!-- Canonical & SEO Meta Tags -->
    <link rel="canonical" href="https://www.omnitoolslab.com/">
    <meta name="robots" content="index, follow">
    <meta property="og:type" content="website">
    <meta property="og:title" content="OmniTools Lab — Suite di Calcolatori Tecnici di Precisione">
    <meta property="og:description" content="Precisione millimetrica per cantiere, grafica ed editoria. Strumenti gratuiti, senza registrazione, funzionanti offline.">
    <meta property="og:url" content="https://www.omnitoolslab.com/">
    <meta property="og:site_name" content="OmniTools Lab">
    <meta property="og:image" content="https://www.omnitoolslab.com/og-hub.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:type" content="image/png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:image" content="https://www.omnitoolslab.com/og-hub.png">

    <!-- Google Search Console Verification -->
    <meta name="google-site-verification" content="MRdbDm9lLhokeD3I0FOpUSOhNaF_2WaveKvu52FxtG4">

    <!-- Schema.org JSON-LD Structured Data -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "WebApplication",
      "name": "OmniTools Lab",
      "url": "https://www.omnitoolslab.com/",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "description": "Suite professionale di strumenti di calcolo tecnico e utility di precisione per edilizia, cantiere, grafica e prestampa.",
      "offers": {{
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "EUR"
      }}
    }}
    </script>
    <link rel="manifest" href="manifest.json">
    <link rel="icon" type="image/svg+xml" href="favicon.svg?v=6">
    <link rel="alternate icon" type="image/png" href="favicon.png?v=6">
    <link rel="shortcut icon" href="favicon.svg?v=6">
    <meta name="theme-color" content="#2563eb">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="OmniTools">
    <link rel="apple-touch-icon" href="icon-192.png?v=6">

    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script defer src="/_vercel/insights/script.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['"Plus Jakarta Sans"', 'system-ui', '-apple-system', 'sans-serif'],
                        jakarta: ['"Plus Jakarta Sans"', 'sans-serif'],
                        mono: ['"JetBrains Mono"', 'monospace'],
                    }}
                }}
            }}
        }}
    </script>
</head>
<body class="bg-slate-50 text-slate-800 font-sans antialiased min-h-screen flex flex-col justify-between selection:bg-blue-500 selection:text-white">

    <!-- Top Navigation Header with safe area padding -->
    <header class="bg-white/95 border-b border-slate-200 sticky top-0 z-40 backdrop-blur-md shadow-2xs" style="padding-top: max(env(safe-area-inset-top), 8px); padding-bottom: 8px;">
        <div class="max-w-4xl mx-auto px-4 py-1 flex items-center justify-between gap-3">
            
            <!-- Brand Identity -->
            <a href="/" class="flex items-center gap-2.5 group">
                <div class="w-[34px] h-[34px] sm:w-[38px] sm:h-[38px] rounded-xl bg-gradient-to-br from-blue-600 to-indigo-700 flex items-center justify-center text-white shadow-md shadow-blue-500/20 shrink-0 p-1 transition group-hover:scale-105">
                    <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="16" cy="16" r="13.2" stroke="#ffffff" stroke-width="3.4" />
                        <path d="M 7.5 11.5 H 24.5 M 16 11.5 V 24.5" stroke="#ffffff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" />
                        <circle cx="16" cy="11.5" r="2.1" fill="#38bdf8" />
                    </svg>
                </div>
                <div class="flex flex-col">
                    <div class="flex items-center gap-1.5 leading-none">
                        <span class="font-jakarta font-black text-base sm:text-lg text-slate-900 tracking-tight leading-none">Omni<span class="text-blue-600">Tools</span></span>
                        <span class="text-[9px] font-jakarta font-extrabold uppercase bg-blue-100 text-blue-800 px-1.5 py-0.5 rounded-full border border-blue-200/80">Lab</span>
                    </div>
                    <span id="taglineText" class="text-[10px] text-slate-600 font-medium hidden sm:inline leading-tight mt-0.5">Precision Utilities Suite</span>
                </div>
            </a>

            <!-- Right Controls: Language Selector + App Install -->
            <div class="flex items-center gap-2 shrink-0">
                <div class="relative inline-block text-left">
                    <select id="langSelect" onchange="changeLanguage(this.value)" class="bg-slate-100 hover:bg-slate-200 text-slate-800 text-xs font-bold py-1.5 px-2 rounded-xl border border-slate-200 focus:outline-none cursor-pointer transition">
                        <option value="it">🇮🇹 IT</option>
                        <option value="en">🇬🇧 EN</option>
                        <option value="es">🇪🇸 ES</option>
                        <option value="fr">🇫🇷 FR</option>
                        <option value="de">🇩🇪 DE</option>
                        <option value="pt">🇵🇹 PT</option>
                    </select>
                </div>

                <button onclick="triggerInstall()" id="headerInstallBtn" class="inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-bold text-blue-700 bg-blue-50 hover:bg-blue-100 active:scale-95 rounded-xl border border-blue-200 transition">
                    <span>📲</span>
                    <span id="headerInstallText" class="hidden sm:inline">App</span>
                </button>
            </div>
        </div>
    </header>

    <!-- Main Content Area -->
    <main class="flex-1 space-y-6 sm:space-y-8 py-6 sm:py-10">
        
        <!-- Hero Section: Clean, Light & Focused -->
        <section class="max-w-4xl mx-auto px-4 text-center space-y-3 sm:space-y-4">
            
            <!-- Compact Pill -->
            <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-blue-50 border border-blue-200 text-blue-700 text-xs font-bold">
                <span id="heroBadge">⚡ Gratuito • Zero Registrazione • 100% Offline</span>
            </div>

            <!-- Punchy Main Title -->
            <h1 id="heroTitle" class="text-2xl sm:text-3xl lg:text-4xl font-black text-slate-900 tracking-tight leading-tight max-w-2xl mx-auto">
                Calcolatori tecnici di precisione per cantiere e grafica.
            </h1>

            <!-- Subtitle -->
            <p id="heroSubtitle" class="text-xs sm:text-sm text-slate-600 max-w-xl mx-auto leading-relaxed">
                Strumenti immediati, conformi alle normative e pronti all'uso. Senza account, senza attese.
            </p>

            <!-- Spotlight / Google Search Bar -->
            <div class="pt-2 max-w-lg mx-auto">
                <div class="relative">
                    <div class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-slate-600">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                        </svg>
                    </div>
                    <input type="text" id="searchInput" oninput="filterTools()" placeholder="Cerca uno strumento (es. pendenza, rampa, scala, gradini, dorso, dpi)..." class="w-full bg-white hover:bg-slate-50/50 focus:bg-white border border-slate-300 focus:border-blue-600 focus:ring-2 focus:ring-blue-100 rounded-2xl pl-10 pr-9 py-2.5 text-xs sm:text-sm text-slate-900 placeholder-slate-600 outline-none shadow-xs transition">
                    <button type="button" id="clearSearchBtn" onclick="clearSearch()" class="hidden absolute inset-y-0 right-0 pr-3.5 flex items-center text-slate-600 hover:text-slate-700">
                        ✕
                    </button>
                </div>

                <!-- Category Filter Pills -->
                <div class="flex items-center justify-center gap-1.5 pt-3 flex-wrap text-xs font-bold">
                    <button type="button" onclick="setFilter('all')" id="filterAllBtn" class="px-3 py-1 rounded-xl bg-blue-600 text-white shadow-xs transition">
                        Tutti i Tool
                    </button>
                    <button type="button" onclick="setFilter('building')" id="filterBuildingBtn" class="px-3 py-1 rounded-xl bg-white hover:bg-slate-100 text-slate-700 border border-slate-200 transition">
                        🏗️ OmniBuilding
                    </button>
                    <button type="button" onclick="setFilter('graph')" id="filterGraphBtn" class="px-3 py-1 rounded-xl bg-white hover:bg-slate-100 text-slate-700 border border-slate-200 transition">
                        🎨 OmniGraph
                    </button>
                </div>
            </div>

        </section>

        <!-- Tools Showcase: Clean 2-Column Responsive Grid -->
        <section class="max-w-4xl mx-auto px-4 space-y-8">
            
            <!-- DIVISION 1: OmniBuilding -->
            <div id="sectionBuilding" class="space-y-3">
                <div class="flex items-center justify-between pb-1.5 border-b border-slate-200">
                    <div class="flex items-center gap-2">
                        <span class="text-base">🏗️</span>
                        <h2 id="divBuildingTitle" class="text-sm sm:text-base font-black text-slate-900 tracking-tight font-jakarta">OmniBuilding</h2>
                        <span class="h-3 w-px bg-slate-200"></span>
                        <p id="divBuildingDesc" class="text-xs text-slate-600">Edilizia, cantiere e accessibilità</p>
                    </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3.5">
                    
                    <!-- Tool Card 1: RampaFacile -->
                    <a href="/rampe" class="tool-card group p-4 sm:p-5 rounded-2xl bg-white hover:bg-blue-50/20 border border-slate-200/90 hover:border-blue-400 shadow-xs hover:shadow-md transition-all duration-150 flex flex-col justify-between space-y-3.5" data-tags="rampa rampe pendenza pendenze dislivello disabili dm 236 garage handicap accessibilita">
                        <div class="space-y-2">
                            <div class="flex items-center justify-between">
                                <div class="flex items-center gap-2.5">
                                    <div class="w-9 h-9 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center text-lg font-bold border border-blue-200 group-hover:bg-blue-600 group-hover:text-white transition">
                                        📐
                                    </div>
                                    <div>
                                        <h3 id="toolRampeTitle" class="text-sm sm:text-base font-black text-slate-900 group-hover:text-blue-600 transition">RampaFacile</h3>
                                        <span id="toolRampeBadge" class="text-[9px] font-bold text-blue-700 bg-blue-50 px-1.5 py-0.2 rounded border border-blue-200">DM 236/89 & ADA</span>
                                    </div>
                                </div>
                                <span class="text-[10px] font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full border border-emerald-200">Attivo</span>
                            </div>
                            <p id="toolRampeDesc" class="text-xs text-slate-600 leading-relaxed">
                                Calcolo pendenza %, gradi e lunghezza a terra con verifica disabili e autorimesse.
                            </p>
                        </div>

                        <div class="flex items-center justify-between pt-2.5 border-t border-slate-100 text-xs">
                            <span class="text-slate-600 font-mono text-[11px]">📏 Pendenza • Gradi • Spazio</span>
                            <span class="font-bold text-blue-600 group-hover:translate-x-1 transition inline-flex items-center gap-1 text-xs">
                                <span class="btnOpenText">Apri</span> <span>→</span>
                            </span>
                        </div>
                    </a>

                    <!-- Tool Card 2: ScalaFacile -->
                    <a href="/scale" class="tool-card group p-4 sm:p-5 rounded-2xl bg-white hover:bg-indigo-50/20 border border-slate-200/90 hover:border-indigo-400 shadow-xs hover:shadow-md transition-all duration-150 flex flex-col justify-between space-y-3.5" data-tags="scala scale gradini gradino alzata pedata blondel dislivello scale interne din 18065">
                        <div class="space-y-2">
                            <div class="flex items-center justify-between">
                                <div class="flex items-center gap-2.5">
                                    <div class="w-9 h-9 rounded-xl bg-indigo-50 text-indigo-600 flex items-center justify-center text-lg font-bold border border-indigo-200 group-hover:bg-indigo-600 group-hover:text-white transition">
                                        🪜
                                    </div>
                                    <div>
                                        <h3 id="toolScaleTitle" class="text-sm sm:text-base font-black text-slate-900 group-hover:text-indigo-600 transition">ScalaFacile</h3>
                                        <span id="toolScaleBadge" class="text-[9px] font-bold text-indigo-700 bg-indigo-50 px-1.5 py-0.2 rounded border border-indigo-200">Legge di Blondel</span>
                                    </div>
                                </div>
                                <span class="text-[10px] font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full border border-emerald-200">Attivo</span>
                            </div>
                            <p id="toolScaleDesc" class="text-xs text-slate-600 leading-relaxed">
                                Dimensionamento ergonomico di gradini, alzata e pedata con verifica 2a + p = 63 cm.
                            </p>
                        </div>

                        <div class="flex items-center justify-between pt-2.5 border-t border-slate-100 text-xs">
                            <span class="text-slate-600 font-mono text-[11px]">🪜 Gradini • Alzata • Pedata</span>
                            <span class="font-bold text-indigo-600 group-hover:translate-x-1 transition inline-flex items-center gap-1 text-xs">
                                <span class="btnOpenText">Apri</span> <span>→</span>
                            </span>
                        </div>
                    </a>

                    <!-- Tool Card 3: ScaricoFacile -->
                    <a href="/tubi" class="tool-card group p-4 sm:p-5 rounded-2xl bg-white hover:bg-cyan-50/20 border border-slate-200/90 hover:border-cyan-400 shadow-xs hover:shadow-md transition-all duration-150 flex flex-col justify-between space-y-3.5" data-tags="scarico scarichi tubi pendenza tubazioni fognatura acque nere grigie caduta en 12056 pendenza scarico">
                        <div class="space-y-2">
                            <div class="flex items-center justify-between">
                                <div class="flex items-center gap-2.5">
                                    <div class="w-9 h-9 rounded-xl bg-cyan-50 text-cyan-600 flex items-center justify-center text-lg font-bold border border-cyan-200 group-hover:bg-cyan-600 group-hover:text-white transition">
                                        🚰
                                    </div>
                                    <div>
                                        <h3 id="toolTubiTitle" class="text-sm sm:text-base font-black text-slate-900 group-hover:text-cyan-600 transition">ScaricoFacile</h3>
                                        <span id="toolTubiBadge" class="text-[9px] font-bold text-cyan-700 bg-cyan-50 px-1.5 py-0.2 rounded border border-cyan-200">UNI EN 12056</span>
                                    </div>
                                </div>
                                <span class="text-[10px] font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full border border-emerald-200">Attivo</span>
                            </div>
                            <p id="toolTubiDesc" class="text-xs text-slate-600 leading-relaxed">
                                Pendenza tubazioni, dislivello caduta per metro e verifica autopulizia scarichi fognari.
                            </p>
                        </div>

                        <div class="flex items-center justify-between pt-2.5 border-t border-slate-100 text-xs">
                            <span class="text-slate-600 font-mono text-[11px]">🚰 Pendenza • Ø 40-200 mm • Autopulizia</span>
                            <span class="font-bold text-cyan-600 group-hover:translate-x-1 transition inline-flex items-center gap-1 text-xs">
                                <span class="btnOpenText">Apri</span> <span>→</span>
                            </span>
                        </div>
                    </a>

                </div>
            </div>

            <!-- DIVISION 2: OmniGraph -->
            <div id="sectionGraph" class="space-y-3">
                <div class="flex items-center justify-between pb-1.5 border-b border-slate-200">
                    <div class="flex items-center gap-2">
                        <span class="text-base">🎨</span>
                        <h2 id="divGraphTitle" class="text-sm sm:text-base font-black text-slate-900 tracking-tight font-jakarta">OmniGraph</h2>
                        <span class="h-3 w-px bg-slate-200"></span>
                        <p id="divGraphDesc" class="text-xs text-slate-600">Grafica, prestampa e tipografia</p>
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-3.5">
                    
                    <!-- Tool Card 3: DorsoFacile -->
                    <a href="/dorso" class="tool-card group p-4 sm:p-5 rounded-2xl bg-white hover:bg-purple-50/20 border border-slate-200/90 hover:border-purple-400 shadow-xs hover:shadow-md transition-all duration-150 flex flex-col justify-between space-y-3.5" data-tags="dorso libro brossura copertina refili indesign kdp amazon pagine grammatura mano carta fustella">
                        <div class="space-y-2">
                            <div class="flex items-center justify-between">
                                <div class="flex items-center gap-2.5">
                                    <div class="w-9 h-9 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center text-lg font-bold border border-purple-200 group-hover:bg-purple-600 group-hover:text-white transition">
                                        🎨
                                    </div>
                                    <div>
                                        <h3 id="toolDorsoTitle" class="text-sm sm:text-base font-black text-slate-900 group-hover:text-purple-600 transition">DorsoFacile</h3>
                                        <span id="toolDorsoBadge" class="text-[9px] font-bold text-purple-700 bg-purple-50 px-1.5 py-0.2 rounded border border-purple-200">Copertina & Refili</span>
                                    </div>
                                </div>
                                <span class="text-[10px] font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full border border-emerald-200">Attivo</span>
                            </div>
                            <p id="toolDorsoDesc" class="text-xs text-slate-600 leading-relaxed">
                                Spessore dorso libro in base a pagine, grammatura e mano con quote per InDesign e KDP.
                            </p>
                        </div>

                        <div class="flex items-center justify-between pt-2.5 border-t border-slate-100 text-xs">
                            <span class="text-slate-600 font-mono text-[11px]">📖 Pagine • Mano • Refilo 3 mm</span>
                            <span class="font-bold text-purple-600 group-hover:translate-x-1 transition inline-flex items-center gap-1 text-xs">
                                <span class="btnOpenText">Apri</span> <span>→</span>
                            </span>
                        </div>
                    </a>

                    <!-- Tool Card 4: RisoluzioneFacile -->
                    <a href="/dpi" class="tool-card group p-4 sm:p-5 rounded-2xl bg-white hover:bg-emerald-50/20 border border-slate-200/90 hover:border-emerald-400 shadow-xs hover:shadow-md transition-all duration-150 flex flex-col justify-between space-y-3.5" data-tags="dpi ppi pixel pixelatura risoluzione stampa formato grande formato poster manifesto offset distanza occhio photoshop">
                        <div class="space-y-2">
                            <div class="flex items-center justify-between">
                                <div class="flex items-center gap-2.5">
                                    <div class="w-9 h-9 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center text-lg font-bold border border-emerald-200 group-hover:bg-emerald-600 group-hover:text-white transition">
                                        🖼️
                                    </div>
                                    <div>
                                        <h3 id="toolDpiTitle" class="text-sm sm:text-base font-black text-slate-900 group-hover:text-emerald-600 transition">RisoluzioneFacile</h3>
                                        <span id="toolDpiBadge" class="text-[9px] font-bold text-emerald-700 bg-emerald-50 px-1.5 py-0.2 rounded border border-emerald-200">Pixel & Acuità Ottica</span>
                                    </div>
                                </div>
                                <span class="text-[10px] font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full border border-emerald-200">Attivo</span>
                            </div>
                            <p id="toolDpiDesc" class="text-xs text-slate-600 leading-relaxed">
                                Conversione Pixel ↔ Centimetri ↔ DPI con calcolo della distanza dell'occhio umano.
                            </p>
                        </div>

                        <div class="flex items-center justify-between pt-2.5 border-t border-slate-100 text-xs">
                            <span class="text-slate-600 font-mono text-[11px]">🖼️ Pixel ↔ cm ↔ DPI • Occhio Umano</span>
                            <span class="font-bold text-emerald-600 group-hover:translate-x-1 transition inline-flex items-center gap-1 text-xs">
                                <span class="btnOpenText">Apri</span> <span>→</span>
                            </span>
                        </div>
                    </a>

                </div>
            </div>

            <!-- Social Share & Viral Action Strip (Light Theme) -->
            <div class="bg-white p-3.5 sm:p-4 rounded-2xl border border-slate-200 shadow-xs flex flex-col sm:flex-row items-center justify-between gap-3 text-center sm:text-left mt-4">
                <div class="flex items-center gap-2.5">
                    <span class="text-lg">📢</span>
                    <div>
                        <span id="shareTitleText" class="text-xs sm:text-sm font-bold text-slate-800 block">Ti sono utili questi strumenti?</span>
                        <span id="shareSubText" class="text-[11px] text-slate-500 block">Condividi la suite con colleghi, collaboratori o clienti</span>
                    </div>
                </div>
                <div class="flex items-center gap-1.5 flex-wrap justify-center shrink-0">
                    <button type="button" onclick="shareWhatsApp()" class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-emerald-600 hover:bg-emerald-500 active:scale-95 text-white text-xs font-bold rounded-xl transition shadow-xs" title="Condividi su WhatsApp">
                        <span>💬</span> <span>WhatsApp</span>
                    </button>
                    <button type="button" onclick="shareLinkedIn()" class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-[#0a66c2] hover:bg-[#004182] active:scale-95 text-white text-xs font-bold rounded-xl transition shadow-xs" title="Condividi su LinkedIn">
                        <span>💼</span> <span>LinkedIn</span>
                    </button>
                    <button type="button" onclick="copyCurrentUrl()" class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-slate-100 hover:bg-slate-200 active:scale-95 text-slate-700 text-xs font-bold rounded-xl border border-slate-200 transition" title="Copia Link">
                        <span>🔗</span> <span id="shareCopyText">Copia Link</span>
                    </button>
                    <button type="button" onclick="nativeShare()" class="inline-flex sm:hidden items-center gap-1.5 px-3 py-1.5 bg-blue-600 hover:bg-blue-500 active:scale-95 text-white text-xs font-bold rounded-xl transition shadow-xs" title="Altre opzioni di condivisione">
                        <span>📤</span> <span>Condividi</span>
                    </button>
                </div>
            </div>

        </section>

    </main>

    <!-- Footer: Clean & Light -->
    <footer class="bg-white border-t border-slate-200 pt-8 pb-10 text-xs text-slate-500">
        <div class="max-w-4xl mx-auto px-4 space-y-5">
            
            <!-- Suggestion Bar -->
            <div class="bg-gradient-to-r from-blue-50 to-indigo-50/70 border border-blue-200/80 rounded-2xl p-3.5 sm:p-4 flex flex-col sm:flex-row items-center justify-between gap-3 text-center sm:text-left shadow-2xs">
                <div class="flex items-center gap-2.5">
                    <span class="text-xl">💡</span>
                    <span id="suggestBannerText" class="text-xs sm:text-sm font-bold text-slate-800">
                        Hai un'idea per un nuovo calcolatore tecnico?
                    </span>
                </div>
                <button type="button" onclick="openSuggestModal()" class="px-3.5 py-1.5 bg-blue-600 hover:bg-blue-500 active:scale-95 text-white font-bold text-xs rounded-xl shadow-xs transition">
                    <span id="suggestBtnText">Suggerisci Tool</span>
                </button>
            </div>

            <!-- Suite Navigation & Partner Hook -->
            <div class="flex items-center justify-center gap-3 text-xs font-bold text-slate-600 flex-wrap pb-1">
                <a href="/rampe" class="hover:text-blue-600 transition">RampaFacile</a>
                <span>•</span>
                <a href="/scale" class="hover:text-blue-600 transition">ScalaFacile</a>
                <span>•</span>
                <a href="/tubi" class="hover:text-blue-600 transition">ScaricoFacile</a>
                <span>•</span>
                <a href="/dorso" class="hover:text-blue-600 transition">DorsoFacile</a>
                <span>•</span>
                <a href="/dpi" class="hover:text-blue-600 transition">RisoluzioneFacile</a>
                <span>•</span>
                <a href="/partnership" class="text-indigo-600 hover:underline" id="navPartnerText">🤝 Diventa Partner / Sponsor</a>
            </div>

            <!-- Disclaimer and Rights -->
            <div class="text-center space-y-1.5">
                <p id="rightsText" class="font-bold text-slate-600">© 2026 OmniTools Lab — Precision Utilities Suite. Tutti i diritti riservati.</p>
                <p id="legalDisclaimerText" class="text-[10px] text-slate-600 leading-relaxed max-w-2xl mx-auto">
                    <strong>Note Legali e Manleva:</strong> Gli strumenti della suite OmniTools Lab hanno finalità orientativa e didattica. Non sostituiscono il calcolo esecutivo, l'asseverazione o il progetto firmato da un tecnico abilitato.
                </p>
            </div>
        </div>
    </footer>

    <!-- Floating PWA Install Banner -->
    <div id="installBanner" class="fixed bottom-3 left-3 right-3 sm:left-auto sm:right-6 sm:bottom-6 sm:max-w-sm bg-slate-900 text-white p-3.5 rounded-2xl shadow-2xl border border-slate-700 z-50 flex items-center justify-between gap-3 transition-all duration-300">
        <div class="flex items-center gap-2.5 min-w-0">
            <div class="w-9 h-9 rounded-xl bg-blue-600 flex items-center justify-center text-white shrink-0 font-bold shadow-md">
                📱
            </div>
            <div class="min-w-0">
                <span class="text-xs font-bold block text-white truncate">Installa OmniTools Lab</span>
                <span class="text-[10px] text-slate-400 block truncate">Sempre pronta anche senza connessione</span>
            </div>
        </div>
        <div class="flex items-center gap-1.5 shrink-0">
            <button onclick="triggerInstall()" class="px-3 py-1.5 bg-blue-600 hover:bg-blue-500 text-white font-bold text-xs rounded-xl transition shadow-xs">
                Installa
            </button>
            <button onclick="dismissInstallBanner()" class="p-1.5 text-slate-400 hover:text-white rounded-lg transition">
                ✕
            </button>
        </div>
    </div>

    <!-- Suggestion Modal -->
    <div id="suggestModal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-xs z-50 hidden flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl max-w-md w-full p-5 sm:p-6 shadow-2xl border border-slate-200 space-y-4">
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-2">
                    <span class="text-xl">💡</span>
                    <h3 class="text-sm sm:text-base font-bold text-slate-900">Suggerisci uno Strumento</h3>
                </div>
                <button onclick="closeSuggestModal()" class="text-slate-400 hover:text-slate-600 p-1 rounded-lg">✕</button>
            </div>
            <p class="text-xs text-slate-600">
                Quale calcolatore tecnico o funzione vorresti vedere su OmniTools Lab?
            </p>
            <textarea id="suggestIdeaInput" rows="3" class="w-full bg-slate-50 border border-slate-200 rounded-xl p-3 text-xs text-slate-900 placeholder-slate-400 focus:bg-white focus:border-blue-600 outline-none transition" placeholder="Es. Calcolo pendenza tubazioni di scarico, resa foglio macchina, etc."></textarea>
            <div class="flex items-center justify-between pt-1">
                <span class="text-[10px] text-slate-500">🔒 Invio 100% anonimo</span>
                <button type="button" onclick="sendSuggestion()" id="suggestSendBtn" class="px-4 py-2 bg-blue-600 hover:bg-blue-500 text-white text-xs font-bold rounded-xl transition shadow-xs">
                    Invia Suggerimento
                </button>
            </div>
            <div id="suggestFeedback" class="hidden text-xs font-bold text-emerald-700 bg-emerald-50 p-2.5 rounded-xl border border-emerald-200 text-center">
                🎉 Grazie mille! La tua idea guiderà i prossimi moduli di OmniTools Lab.
            </div>
        </div>
    </div>

    <!-- JAVASCRIPT LOGIC -->
    <script>
        const TRANSLATIONS = {t_json_str};

        let currentLang = localStorage.getItem('omnitools_lang') || 'it';
        let currentFilter = 'all';

        function changeLanguage(lang) {{
            if (!TRANSLATIONS[lang]) return;
            currentLang = lang;
            localStorage.setItem('omnitools_lang', lang);
            document.documentElement.lang = lang;
            document.getElementById('langSelect').value = lang;
            applyTranslations();
        }}

        function applyTranslations() {{
            const t = TRANSLATIONS[currentLang];
            if (!t) return;

            document.title = t.title;
            document.getElementById('taglineText').textContent = t.tagline;
            document.getElementById('heroBadge').textContent = t.hero_badge;
            document.getElementById('heroTitle').textContent = t.hero_title;
            document.getElementById('heroSubtitle').textContent = t.hero_subtitle;
            document.getElementById('searchInput').placeholder = t.search_placeholder;
            document.getElementById('filterAllBtn').textContent = t.filter_all;
            document.getElementById('filterBuildingBtn').textContent = t.filter_building;
            document.getElementById('filterGraphBtn').textContent = t.filter_graph;
            document.getElementById('divBuildingTitle').textContent = t.division_building_title;
            document.getElementById('divBuildingDesc').textContent = t.division_building_desc;
            document.getElementById('divGraphTitle').textContent = t.division_graph_title;
            document.getElementById('divGraphDesc').textContent = t.division_graph_desc;
            document.getElementById('toolRampeTitle').textContent = t.tool_rampe_title;
            document.getElementById('toolRampeBadge').textContent = t.tool_rampe_badge;
            document.getElementById('toolRampeDesc').textContent = t.tool_rampe_desc;
            document.getElementById('toolScaleTitle').textContent = t.tool_scale_title;
            document.getElementById('toolScaleBadge').textContent = t.tool_scale_badge;
            document.getElementById('toolScaleDesc').textContent = t.tool_scale_desc;
            if (document.getElementById('toolTubiTitle')) {{
                document.getElementById('toolTubiTitle').textContent = t.tool_tubi_title;
                document.getElementById('toolTubiBadge').textContent = t.tool_tubi_badge;
                document.getElementById('toolTubiDesc').textContent = t.tool_tubi_desc;
            }}
            if (document.getElementById('navPartnerText')) {{
                document.getElementById('navPartnerText').textContent = '🤝 ' + (t.nav_partner || 'Diventa Partner / Sponsor');
            }}
            document.getElementById('toolDorsoTitle').textContent = t.tool_dorso_title;
            document.getElementById('toolDorsoBadge').textContent = t.tool_dorso_badge;
            document.getElementById('toolDorsoDesc').textContent = t.tool_dorso_desc;
            document.getElementById('toolDpiTitle').textContent = t.tool_dpi_title;
            document.getElementById('toolDpiBadge').textContent = t.tool_dpi_badge;
            document.getElementById('toolDpiDesc').textContent = t.tool_dpi_desc;
            document.getElementById('shareTitleText').textContent = t.share_title;
            document.getElementById('shareSubText').textContent = t.share_sub;
            document.getElementById('shareCopyText').textContent = t.share_copy;
            document.getElementById('suggestBannerText').textContent = t.suggest_banner;
            document.getElementById('suggestBtnText').textContent = t.suggest_btn;
            document.getElementById('rightsText').textContent = t.rights_reserved;
            document.getElementById('legalDisclaimerText').innerHTML = t.legal_disclaimer;

            document.querySelectorAll('.btnOpenText').forEach(el => {{
                el.textContent = t.btn_open || 'Apri';
            }});
        }}

        function setFilter(filter) {{
            currentFilter = filter;
            const btnAll = document.getElementById('filterAllBtn');
            const btnBuilding = document.getElementById('filterBuildingBtn');
            const btnGraph = document.getElementById('filterGraphBtn');

            const activeClass = "px-3 py-1 rounded-xl bg-blue-600 text-white shadow-xs transition font-bold";
            const inactiveClass = "px-3 py-1 rounded-xl bg-white hover:bg-slate-100 text-slate-700 border border-slate-200 transition font-bold";

            btnAll.className = filter === 'all' ? activeClass : inactiveClass;
            btnBuilding.className = filter === 'building' ? activeClass : inactiveClass;
            btnGraph.className = filter === 'graph' ? activeClass : inactiveClass;

            const secBuilding = document.getElementById('sectionBuilding');
            const secGraph = document.getElementById('sectionGraph');

            if (filter === 'all') {{
                secBuilding.classList.remove('hidden');
                secGraph.classList.remove('hidden');
            }} else if (filter === 'building') {{
                secBuilding.classList.remove('hidden');
                secGraph.classList.add('hidden');
            }} else if (filter === 'graph') {{
                secBuilding.classList.add('hidden');
                secGraph.classList.remove('hidden');
            }}
        }}

        function filterTools() {{
            const query = document.getElementById('searchInput').value.toLowerCase().trim();
            const clearBtn = document.getElementById('clearSearchBtn');
            if (query.length > 0) {{
                clearBtn.classList.remove('hidden');
            }} else {{
                clearBtn.classList.add('hidden');
            }}

            const cards = document.querySelectorAll('.tool-card');
            cards.forEach(card => {{
                const text = card.textContent.toLowerCase();
                const tags = (card.getAttribute('data-tags') || '').toLowerCase();
                if (text.includes(query) || tags.includes(query)) {{
                    card.classList.remove('hidden');
                }} else {{
                    card.classList.add('hidden');
                }}
            }});
        }}

        function clearSearch() {{
            document.getElementById('searchInput').value = '';
            document.getElementById('clearSearchBtn').classList.add('hidden');
            filterTools();
        }}

        // Social Sharing Functions
        function shareWhatsApp() {{
            const url = encodeURIComponent(window.location.href);
            const text = encodeURIComponent(document.title);
            window.open(`https://api.whatsapp.com/send?text=${{text}}%20${{url}}`, '_blank');
        }}
        function shareLinkedIn() {{
            const url = encodeURIComponent(window.location.href);
            window.open(`https://www.linkedin.com/sharing/share-offsite/?url=${{url}}`, '_blank');
        }}
        function copyCurrentUrl() {{
            navigator.clipboard.writeText(window.location.href).then(() => {{
                const el = document.getElementById('shareCopyText');
                if (el) {{
                    const orig = el.textContent;
                    el.textContent = (TRANSLATIONS[currentLang] && TRANSLATIONS[currentLang].share_copied) || 'Copiato! ✓';
                    setTimeout(() => {{ el.textContent = orig; }}, 2000);
                }}
            }});
        }}
        function nativeShare() {{
            if (navigator.share) {{
                navigator.share({{
                    title: document.title,
                    url: window.location.href
                }}).catch(() => {{}});
            }} else {{
                copyCurrentUrl();
            }}
        }}

        // Feedback / Suggest Modal
        function openSuggestModal() {{
            document.getElementById('suggestModal').classList.remove('hidden');
        }}
        function closeSuggestModal() {{
            document.getElementById('suggestModal').classList.add('hidden');
            document.getElementById('suggestFeedback').classList.add('hidden');
        }}
        async function sendSuggestion() {{
            const input = document.getElementById('suggestIdeaInput');
            const val = input.value.trim();
            if (!val) return;
            const btn = document.getElementById('suggestSendBtn');
            btn.disabled = true;
            btn.textContent = '...';
            try {{
                await fetch('/api/suggest', {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify({{ idea: val, tool: 'Hub', lang: currentLang }})
                }});
            }} catch(e) {{}}
            document.getElementById('suggestFeedback').classList.remove('hidden');
            input.value = '';
            setTimeout(() => closeSuggestModal(), 2000);
            btn.disabled = false;
            btn.textContent = 'Invia Suggerimento';
        }}

        // PWA Install Prompt
        let deferredPrompt;
        window.addEventListener('beforeinstallprompt', (e) => {{
            e.preventDefault();
            deferredPrompt = e;
            const banner = document.getElementById('installBanner');
            if (banner && !sessionStorage.getItem('omnitools_install_dismissed')) {{
                banner.classList.remove('hidden');
            }}
        }});
        function triggerInstall() {{
            if (deferredPrompt) {{
                deferredPrompt.prompt();
                deferredPrompt.userChoice.then(() => {{
                    deferredPrompt = null;
                    dismissInstallBanner();
                }});
            }}
        }}
        function dismissInstallBanner() {{
            document.getElementById('installBanner').classList.add('hidden');
            sessionStorage.setItem('omnitools_install_dismissed', '1');
        }}

        // Init
        document.addEventListener('DOMContentLoaded', () => {{
            applyTranslations();
        }});
    </script>
</body>
</html>
"""

with open("/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/index.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("index.html compiled with Light Clean Hub Portal successfully.")
