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
    <meta name="description" content="OmniTools Lab: Suite gratuita di calcolatori tecnici online. RampaFacile (DM 236/89), ScalaFacile (Blondel), ScaricoFacile (UNI EN 12056), DorsoFacile e RisoluzioneFacile.">
    
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
                    }},
                    colors: {{
                        building: {{
                            50: '#fffbeb',
                            100: '#fef3c7',
                            200: '#fde68a',
                            500: '#f59e0b',
                            600: '#d97706',
                            700: '#b45309',
                            800: '#92400e',
                            900: '#78350f',
                        }},
                        graph: {{
                            50: '#fff1f2',
                            100: '#ffe4e6',
                            200: '#fecdd3',
                            500: '#f43f5e',
                            600: '#e11d48',
                            700: '#be123c',
                            800: '#9f1239',
                            900: '#881337',
                        }}
                    }}
                }}
            }}
        }}
    </script>
</head>
<body class="bg-slate-50 text-slate-800 font-sans antialiased min-h-screen flex flex-col justify-between selection:bg-blue-500 selection:text-white">

    <!-- Top Navigation Header -->
    <header class="bg-white/95 border-b border-slate-200 sticky top-0 z-40 backdrop-blur-md shadow-2xs" style="padding-top: max(env(safe-area-inset-top), 8px); padding-bottom: 8px;">
        <div class="max-w-4xl mx-auto px-4 py-1 flex items-center justify-between gap-3">
            
            <!-- Brand Identity -->
            <a href="/" class="flex items-center gap-2.5 group">
                <div class="w-[36px] h-[36px] sm:w-[40px] sm:h-[40px] rounded-xl bg-gradient-to-br from-blue-600 to-indigo-700 flex items-center justify-center text-white shadow-md shadow-blue-500/20 shrink-0 p-1 transition group-hover:scale-105">
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
                    <span id="taglineText" class="text-[10px] text-slate-500 font-medium hidden sm:inline leading-tight mt-0.5">Precision Utilities Suite</span>
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

                <button onclick="triggerInstall()" id="headerInstallBtn" class="inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-bold text-blue-700 bg-blue-50 hover:bg-blue-100 active:scale-95 rounded-xl border border-blue-200 transition shadow-xs">
                    <span>📲</span>
                    <span id="headerInstallText" class="hidden sm:inline">Installa App</span>
                </button>
            </div>
        </div>
    </header>

    <!-- Main Content Area -->
    <main class="flex-1 space-y-6 sm:space-y-8 py-6 sm:py-9">
        
        <!-- Hero Section: High Impact, Direct & Child-Proof -->
        <section class="max-w-4xl mx-auto px-4 text-center space-y-3.5">
            
            <!-- Trust Badge -->
            <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-blue-50/80 border border-blue-200/90 text-blue-700 text-xs font-bold shadow-2xs">
                <span>⚡</span>
                <span id="heroBadge">Gratuito • Nessuna Registrazione • Funziona 100% Offline</span>
            </div>

            <!-- Big Magnetic Question -->
            <h1 id="heroTitle" class="text-2xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight leading-tight max-w-2xl mx-auto">
                Cosa vuoi calcolare oggi?
            </h1>

            <!-- Subtitle -->
            <p id="heroSubtitle" class="text-xs sm:text-sm text-slate-600 max-w-xl mx-auto leading-relaxed">
                Calcolatori tecnici di precisione per cantiere, impianti e grafica. Formule certificate, zero registrazioni, subito pronti offline.
            </p>

            <!-- Spotlight Search Bar -->
            <div class="pt-1 max-w-lg mx-auto">
                <div class="relative">
                    <div class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-slate-400">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                        </svg>
                    </div>
                    <input type="text" id="searchInput" oninput="filterTools()" placeholder="Cerca: rampa, gradini, tubi, dorso libro, dpi..." class="w-full bg-white hover:bg-slate-50/70 focus:bg-white border border-slate-300 focus:border-blue-600 focus:ring-4 focus:ring-blue-100 rounded-2xl pl-10 pr-9 py-2.5 sm:py-3 text-xs sm:text-sm text-slate-900 placeholder-slate-400 outline-none shadow-xs transition">
                    <button type="button" id="clearSearchBtn" onclick="clearSearch()" class="hidden absolute inset-y-0 right-0 pr-3.5 flex items-center text-slate-400 hover:text-slate-700 text-sm font-bold">
                        ✕
                    </button>
                </div>

                <!-- DIVISION SEGMENTED PICKER: Child-Proof, Authentic Division Logos & Brand Colors -->
                <div class="grid grid-cols-3 gap-1.5 sm:gap-2.5 pt-3.5">
                    
                    <!-- Tab: Tutti (OmniTools Blue) -->
                    <button type="button" onclick="setFilter('all')" id="filterAllBtn" class="flex flex-col sm:flex-row items-center justify-center gap-1.5 sm:gap-2.5 py-2 sm:py-2.5 px-2 rounded-2xl bg-blue-600 text-white shadow-md shadow-blue-600/20 font-bold text-xs sm:text-sm transition-all duration-150">
                        <div class="w-6 h-6 sm:w-7 sm:h-7 rounded-lg bg-gradient-to-br from-blue-500 to-indigo-700 flex items-center justify-center text-white shrink-0 p-0.5 shadow-xs border border-white/30">
                            <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <circle cx="16" cy="16" r="13.2" stroke="#ffffff" stroke-width="3.4" />
                                <path d="M 7.5 11.5 H 24.5 M 16 11.5 V 24.5" stroke="#ffffff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" />
                                <circle cx="16" cy="11.5" r="2.1" fill="#38bdf8" />
                            </svg>
                        </div>
                        <div class="text-left leading-tight">
                            <span id="filterAllText" class="block">Tutti i Tool</span>
                            <span class="subtext text-[10px] text-blue-100 font-normal hidden sm:block">6 Strumenti</span>
                        </div>
                    </button>

                    <!-- Tab: OmniBuilding (Ocra) -->
                    <button type="button" onclick="setFilter('building')" id="filterBuildingBtn" class="flex flex-col sm:flex-row items-center justify-center gap-1.5 sm:gap-2.5 py-2 sm:py-2.5 px-2 rounded-2xl bg-white hover:bg-amber-50/50 text-slate-700 hover:text-amber-800 border border-slate-200/90 font-bold text-xs sm:text-sm transition-all duration-150">
                        <div class="w-6 h-6 sm:w-7 sm:h-7 rounded-lg bg-gradient-to-br from-amber-500 to-amber-700 flex items-center justify-center text-white shrink-0 p-0.5 shadow-xs border border-amber-300/40">
                            <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <circle cx="16" cy="16" r="13.2" stroke="#ffffff" stroke-width="3" />
                                <path d="M 9.5 8.5 V 23.5 H 24.5" stroke="#ffffff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" />
                                <line x1="9.5" y1="23.5" x2="22.5" y2="10.5" stroke="#ffffff" stroke-width="2" stroke-dasharray="2.5 2" />
                                <circle cx="9.5" cy="23.5" r="2.2" fill="#fde047" />
                            </svg>
                        </div>
                        <div class="text-left leading-tight">
                            <span class="block">OmniBuilding</span>
                            <span class="subtext text-[10px] text-amber-700/80 font-normal hidden sm:block">3 Cantiere & Impianti</span>
                        </div>
                    </button>

                    <!-- Tab: OmniGraph (Bordeaux) -->
                    <button type="button" onclick="setFilter('graph')" id="filterGraphBtn" class="flex flex-col sm:flex-row items-center justify-center gap-1.5 sm:gap-2.5 py-2 sm:py-2.5 px-2 rounded-2xl bg-white hover:bg-rose-50/50 text-slate-700 hover:text-rose-900 border border-slate-200/90 font-bold text-xs sm:text-sm transition-all duration-150">
                        <div class="w-6 h-6 sm:w-7 sm:h-7 rounded-lg bg-gradient-to-br from-rose-800 to-rose-950 flex items-center justify-center text-white shrink-0 p-0.5 shadow-xs border border-rose-300/40">
                            <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <circle cx="16" cy="16" r="13.2" stroke="#ffffff" stroke-width="2.8" />
                                <circle cx="16" cy="16" r="6" stroke="#ffffff" stroke-width="2" />
                                <line x1="16" y1="4.5" x2="16" y2="27.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round" />
                                <line x1="4.5" y1="16" x2="27.5" y2="16" stroke="#ffffff" stroke-width="2" stroke-linecap="round" />
                                <circle cx="16" cy="16" r="2.2" fill="#fda4af" />
                            </svg>
                        </div>
                        <div class="text-left leading-tight">
                            <span class="block">OmniGraph</span>
                            <span class="subtext text-[10px] text-rose-800/80 font-normal hidden sm:block">3 Grafica & Stampa</span>
                        </div>
                    </button>

                </div>
            </div>

        </section>

        <!-- Tools Showcase -->
        <section class="max-w-4xl mx-auto px-4 space-y-8">
            
            <!-- ========================================== -->
            <!-- DIVISION 1: OmniBuilding (Edilizia & Tubi) -->
            <!-- ========================================== -->
            <div id="sectionBuilding" class="space-y-4">
                
                <!-- Division Department Header -->
                <div class="flex items-center justify-between pb-2.5 border-b-2 border-amber-500/20">
                    <div class="flex items-center gap-2.5">
                        <div class="w-8 h-8 rounded-xl bg-gradient-to-br from-amber-500 to-amber-700 flex items-center justify-center text-white shadow-sm shadow-amber-500/30 shrink-0 p-1">
                            <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <circle cx="16" cy="16" r="13.2" stroke="#ffffff" stroke-width="3" />
                                <path d="M 9.5 8.5 V 23.5 H 24.5" stroke="#ffffff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" />
                                <line x1="9.5" y1="23.5" x2="22.5" y2="10.5" stroke="#ffffff" stroke-width="2" stroke-dasharray="2.5 2" />
                                <circle cx="9.5" cy="23.5" r="2.2" fill="#fde047" />
                            </svg>
                        </div>
                        <div>
                            <div class="flex items-center gap-2">
                                <h2 id="divBuildingTitle" class="text-base sm:text-lg font-black text-amber-900 tracking-tight font-jakarta leading-none">Omni<span class="text-amber-600">Building</span></h2>
                                <span class="text-[9px] font-extrabold uppercase bg-amber-100 text-amber-900 px-2 py-0.5 rounded-full border border-amber-300">Reparto Cantiere</span>
                            </div>
                            <p id="divBuildingDesc" class="text-[11px] text-slate-500 mt-0.5">Calcolatori geometrici e normativi per cantieri, architettura e impianti</p>
                        </div>
                    </div>
                    <span class="text-xs font-mono font-bold text-amber-800 bg-amber-50 px-2.5 py-1 rounded-xl border border-amber-200 hidden sm:inline-block">3 Tool Attivi</span>
                </div>

                <!-- 3 Building Tools Grid -->
                <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                    
                    <!-- TOOL 1: RampaFacile -->
                    <a href="/rampe" class="tool-card group relative bg-white hover:bg-amber-50/20 rounded-3xl p-5 border-2 border-slate-200/90 hover:border-amber-500 shadow-xs hover:shadow-xl hover:-translate-y-1 transition-all duration-200 flex flex-col justify-between space-y-4" data-tags="rampa rampe pendenza gradi disabili dm 236 autorimesse garage dislivello pendenza disabili lunghezza a terra">
                        <div class="space-y-3">
                            <!-- Visual Header & Micro Blueprint -->
                            <div class="flex items-center justify-between">
                                <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-amber-500 to-amber-600 text-white flex items-center justify-center shadow-md shadow-amber-500/25 p-2">
                                    <!-- Blueprint Ramp SVG -->
                                    <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" stroke="currentColor">
                                        <path d="M 4 24 H 28 L 4 10 Z" fill="rgba(255,255,255,0.2)" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" />
                                        <line x1="28" y1="10" x2="28" y2="24" stroke="#fde047" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="2 2" />
                                        <path d="M 9 20 A 4 4 0 0 1 15 20" stroke="#ffffff" stroke-width="2" />
                                    </svg>
                                </div>
                                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-700 border border-emerald-200">DM 236/89</span>
                            </div>

                            <!-- Title & Direct Question Hook -->
                            <div>
                                <h3 id="toolRampeTitle" class="text-base sm:text-lg font-black text-slate-900 group-hover:text-amber-600 transition">RampaFacile</h3>
                                <div id="toolRampeHook" class="text-xs font-bold text-amber-700 mt-0.5">La rampa è a norma?</div>
                            </div>

                            <!-- Plain Description -->
                            <p id="toolRampeDesc" class="text-xs text-slate-600 leading-relaxed">
                                Calcola pendenza %, gradi e lunghezza a terra per disabili (DM 236/89) e garage in 1 secondo.
                            </p>

                            <!-- Feature Tags -->
                            <div class="flex flex-wrap gap-1 pt-1 text-[10px] font-bold text-slate-500">
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">📐 Pendenza %</span>
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">♿ Disabili 8%</span>
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">🚗 Garage 20%</span>
                            </div>
                        </div>

                        <!-- Big Action CTA Button -->
                        <div class="pt-3 border-t border-slate-100">
                            <div class="w-full py-2 px-3 rounded-xl bg-amber-50 group-hover:bg-amber-500 text-amber-800 group-hover:text-white font-bold text-xs flex items-center justify-between transition-colors shadow-2xs">
                                <span id="toolRampeCta">Calcola Rampa Ora</span>
                                <span class="group-hover:translate-x-1 transition-transform">➔</span>
                            </div>
                        </div>
                    </a>

                    <!-- TOOL 2: ScalaFacile -->
                    <a href="/scale" class="tool-card group relative bg-white hover:bg-indigo-50/20 rounded-3xl p-5 border-2 border-slate-200/90 hover:border-indigo-500 shadow-xs hover:shadow-xl hover:-translate-y-1 transition-all duration-200 flex flex-col justify-between space-y-4" data-tags="scala scale gradini gradino alzata pedata blondel dislivello scale interne din 18065 numero gradini">
                        <div class="space-y-3">
                            <!-- Visual Header & Micro Blueprint -->
                            <div class="flex items-center justify-between">
                                <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-indigo-500 to-indigo-700 text-white flex items-center justify-center shadow-md shadow-indigo-500/25 p-2">
                                    <!-- Blueprint Stairs SVG -->
                                    <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" stroke="currentColor">
                                        <path d="M 5 25 H 12 V 18 H 19 V 11 H 27" stroke="#ffffff" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" />
                                        <line x1="12" y1="25" x2="12" y2="18" stroke="#a5b4fc" stroke-width="2" stroke-dasharray="1.5 1.5" />
                                        <line x1="19" y1="18" x2="19" y2="11" stroke="#a5b4fc" stroke-width="2" stroke-dasharray="1.5 1.5" />
                                    </svg>
                                </div>
                                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-indigo-50 text-indigo-700 border border-indigo-200">Blondel</span>
                            </div>

                            <!-- Title & Direct Question Hook -->
                            <div>
                                <h3 id="toolScaleTitle" class="text-base sm:text-lg font-black text-slate-900 group-hover:text-indigo-600 transition">ScalaFacile</h3>
                                <div id="toolScaleHook" class="text-xs font-bold text-indigo-700 mt-0.5">Quanti gradini servono?</div>
                            </div>

                            <!-- Plain Description -->
                            <p id="toolScaleDesc" class="text-xs text-slate-600 leading-relaxed">
                                Trova numero di gradini, alzata e pedata perfetti con la formula ergonomica di Blondel.
                            </p>

                            <!-- Feature Tags -->
                            <div class="flex flex-wrap gap-1 pt-1 text-[10px] font-bold text-slate-500">
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">🪜 Alzata / Pedata</span>
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">📐 2a + p = 63 cm</span>
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">🏢 DIN 18065</span>
                            </div>
                        </div>

                        <!-- Big Action CTA Button -->
                        <div class="pt-3 border-t border-slate-100">
                            <div class="w-full py-2 px-3 rounded-xl bg-indigo-50 group-hover:bg-indigo-600 text-indigo-800 group-hover:text-white font-bold text-xs flex items-center justify-between transition-colors shadow-2xs">
                                <span id="toolScaleCta">Progetta Scala Ora</span>
                                <span class="group-hover:translate-x-1 transition-transform">➔</span>
                            </div>
                        </div>
                    </a>

                    <!-- TOOL 3: ScaricoFacile -->
                    <a href="/tubi" class="tool-card group relative bg-white hover:bg-cyan-50/20 rounded-3xl p-5 border-2 border-slate-200/90 hover:border-cyan-500 shadow-xs hover:shadow-xl hover:-translate-y-1 transition-all duration-200 flex flex-col justify-between space-y-4" data-tags="scarico scarichi tubi pendenza tubazioni fognatura acque nere grigie caduta en 12056 pendenza scarico autopulizia">
                        <div class="space-y-3">
                            <!-- Visual Header & Micro Blueprint -->
                            <div class="flex items-center justify-between">
                                <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-cyan-600 to-blue-700 text-white flex items-center justify-center shadow-md shadow-cyan-600/25 p-2">
                                    <!-- Blueprint Pipe Flow SVG -->
                                    <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" stroke="currentColor">
                                        <line x1="5" y1="11" x2="27" y2="21" stroke="#ffffff" stroke-width="4.5" stroke-linecap="round" />
                                        <path d="M 12 14.5 C 15 16, 17 17, 20 18.5" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" />
                                        <circle cx="21" cy="22" r="2" fill="#38bdf8" />
                                    </svg>
                                </div>
                                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-cyan-50 text-cyan-700 border border-cyan-200">UNI EN 12056</span>
                            </div>

                            <!-- Title & Direct Question Hook -->
                            <div>
                                <h3 id="toolTubiTitle" class="text-base sm:text-lg font-black text-slate-900 group-hover:text-cyan-600 transition">ScaricoFacile</h3>
                                <div id="toolTubiHook" class="text-xs font-bold text-cyan-700 mt-0.5">L'acqua scorre o si intasa?</div>
                            </div>

                            <!-- Plain Description -->
                            <p id="toolTubiDesc" class="text-xs text-slate-600 leading-relaxed">
                                Pendenza corretta, dislivello al metro e verifica autopulizia per tubazioni di scarico (UNI EN 12056).
                            </p>

                            <!-- Feature Tags -->
                            <div class="flex flex-wrap gap-1 pt-1 text-[10px] font-bold text-slate-500">
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">🚰 Caduta cm/m</span>
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">💧 Autopulizia 1-2%</span>
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">📏 Ø 40-200 mm</span>
                            </div>
                        </div>

                        <!-- Big Action CTA Button -->
                        <div class="pt-3 border-t border-slate-100">
                            <div class="w-full py-2 px-3 rounded-xl bg-cyan-50 group-hover:bg-cyan-600 text-cyan-800 group-hover:text-white font-bold text-xs flex items-center justify-between transition-colors shadow-2xs">
                                <span id="toolTubiCta">Calcola Pendenza Tubo</span>
                                <span class="group-hover:translate-x-1 transition-transform">➔</span>
                            </div>
                        </div>
                    </a>

                </div>
            </div>

            <!-- ========================================== -->
            <!-- DIVISION 2: OmniGraph (Grafica & Stampa)   -->
            <!-- ========================================== -->
            <div id="sectionGraph" class="space-y-4">
                
                <!-- Division Department Header -->
                <div class="flex items-center justify-between pb-2.5 border-b-2 border-rose-900/20">
                    <div class="flex items-center gap-2.5">
                        <div class="w-8 h-8 rounded-xl bg-gradient-to-br from-rose-800 to-rose-950 flex items-center justify-center text-white shadow-sm shadow-rose-900/30 shrink-0 p-1">
                            <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <circle cx="16" cy="16" r="13.2" stroke="#ffffff" stroke-width="2.8" />
                                <circle cx="16" cy="16" r="6" stroke="#ffffff" stroke-width="2" />
                                <line x1="16" y1="4.5" x2="16" y2="27.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round" />
                                <line x1="4.5" y1="16" x2="27.5" y2="16" stroke="#ffffff" stroke-width="2" stroke-linecap="round" />
                                <circle cx="16" cy="16" r="2.2" fill="#fda4af" />
                            </svg>
                        </div>
                        <div>
                            <div class="flex items-center gap-2">
                                <h2 id="divGraphTitle" class="text-base sm:text-lg font-black text-rose-950 tracking-tight font-jakarta leading-none">Omni<span class="text-rose-700">Graph</span></h2>
                                <span class="text-[9px] font-extrabold uppercase bg-rose-100 text-rose-900 px-2 py-0.5 rounded-full border border-rose-300">Reparto Grafica</span>
                            </div>
                            <p id="divGraphDesc" class="text-[11px] text-slate-500 mt-0.5">Strumenti di precisione tipografica per grafici, editori e prestampa</p>
                        </div>
                    </div>
                    <span class="text-xs font-mono font-bold text-rose-900 bg-rose-50 px-2.5 py-1 rounded-xl border border-rose-200 hidden sm:inline-block">3 Tool Attivi</span>
                </div>

                <!-- 3 Graphic Tools Grid -->
                <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                    
                    <!-- TOOL 4: DorsoFacile -->
                    <a href="/dorso" class="tool-card group relative bg-white hover:bg-rose-50/20 rounded-3xl p-5 sm:p-6 border-2 border-slate-200/90 hover:border-rose-700 shadow-xs hover:shadow-xl hover:-translate-y-1 transition-all duration-200 flex flex-col justify-between space-y-4" data-tags="dorso libro brossura copertina refili indesign kdp amazon pagine grammatura mano carta fustella spessore dorso">
                        <div class="space-y-3">
                            <!-- Visual Header & Micro Blueprint -->
                            <div class="flex items-center justify-between">
                                <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-rose-800 to-rose-950 text-white flex items-center justify-center shadow-md shadow-rose-900/25 p-2">
                                    <!-- Blueprint Book Spine SVG -->
                                    <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" stroke="currentColor">
                                        <rect x="7" y="5" width="18" height="22" rx="2" stroke="#ffffff" stroke-width="2.5" />
                                        <rect x="13" y="5" width="6" height="22" fill="rgba(255,255,255,0.25)" stroke="#fda4af" stroke-width="2" />
                                        <line x1="10" y1="12" x2="12" y2="12" stroke="#ffffff" stroke-width="1.8" />
                                        <line x1="10" y1="16" x2="12" y2="16" stroke="#ffffff" stroke-width="1.8" />
                                        <line x1="20" y1="12" x2="22" y2="12" stroke="#ffffff" stroke-width="1.8" />
                                    </svg>
                                </div>
                                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-rose-50 text-rose-800 border border-rose-200">Editoria & KDP</span>
                            </div>

                            <!-- Title & Direct Question Hook -->
                            <div>
                                <h3 id="toolDorsoTitle" class="text-base sm:text-lg font-black text-slate-900 group-hover:text-rose-800 transition">DorsoFacile</h3>
                                <div id="toolDorsoHook" class="text-xs font-bold text-rose-800 mt-0.5">Quanto è spesso il libro?</div>
                            </div>

                            <!-- Plain Description -->
                            <p id="toolDorsoDesc" class="text-xs text-slate-600 leading-relaxed">
                                Calcola lo spessore esatto del dorso per la copertina in base a pagine, grammatura e carta.
                            </p>

                            <!-- Feature Tags -->
                            <div class="flex flex-wrap gap-1 pt-1 text-[10px] font-bold text-slate-500">
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">📖 Spessore Dorso mm</span>
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">📐 Quote InDesign</span>
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">📦 KDP & Brossura</span>
                            </div>
                        </div>

                        <!-- Big Action CTA Button -->
                        <div class="pt-3 border-t border-slate-100">
                            <div class="w-full py-2 px-3 rounded-xl bg-rose-50 group-hover:bg-rose-900 text-rose-900 group-hover:text-white font-bold text-xs flex items-center justify-between transition-colors shadow-2xs">
                                <span id="toolDorsoCta">Calcola Spessore Dorso</span>
                                <span class="group-hover:translate-x-1 transition-transform">➔</span>
                            </div>
                        </div>
                    </a>

                    <!-- TOOL 5: RisoluzioneFacile -->
                    <a href="/dpi" class="tool-card group relative bg-white hover:bg-emerald-50/20 rounded-3xl p-5 sm:p-6 border-2 border-slate-200/90 hover:border-emerald-600 shadow-xs hover:shadow-xl hover:-translate-y-1 transition-all duration-200 flex flex-col justify-between space-y-4" data-tags="dpi ppi pixel pixelatura risoluzione stampa formato grande formato poster manifesto offset distanza occhio photoshop acuità visiva">
                        <div class="space-y-3">
                            <!-- Visual Header & Micro Blueprint -->
                            <div class="flex items-center justify-between">
                                <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-emerald-600 to-teal-800 text-white flex items-center justify-center shadow-md shadow-emerald-600/25 p-2">
                                    <!-- Blueprint DPI Grid SVG -->
                                    <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" stroke="currentColor">
                                        <circle cx="14" cy="14" r="9" stroke="#ffffff" stroke-width="2.5" />
                                        <line x1="20.5" y1="20.5" x2="27" y2="27" stroke="#ffffff" stroke-width="3" stroke-linecap="round" />
                                        <rect x="10" y="10" width="3" height="3" fill="#6ee7b7" />
                                        <rect x="15" y="10" width="3" height="3" fill="#6ee7b7" />
                                        <rect x="10" y="15" width="3" height="3" fill="#6ee7b7" />
                                        <rect x="15" y="15" width="3" height="3" fill="#6ee7b7" />
                                    </svg>
                                </div>
                                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-700 border border-emerald-200">Pixel & Acuità</span>
                            </div>

                            <!-- Title & Direct Question Hook -->
                            <div>
                                <h3 id="toolDpiTitle" class="text-base sm:text-lg font-black text-slate-900 group-hover:text-emerald-700 transition">RisoluzioneFacile</h3>
                                <div id="toolDpiHook" class="text-xs font-bold text-emerald-700 mt-0.5">Verrà sgranato in stampa?</div>
                            </div>

                            <!-- Plain Description -->
                            <p id="toolDpiDesc" class="text-xs text-slate-600 leading-relaxed">
                                Converti Pixel in Centimetri e verifica i DPI ideali in base alla distanza di visione dell'occhio.
                            </p>

                            <!-- Feature Tags -->
                            <div class="flex flex-wrap gap-1 pt-1 text-[10px] font-bold text-slate-500">
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">🖼️ Pixel ↔ cm</span>
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">🖨️ 300 DPI Tipografia</span>
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">👁️ Distanza Visiva</span>
                            </div>
                        </div>

                        <!-- Big Action CTA Button -->
                        <div class="pt-3 border-t border-slate-100">
                            <div class="w-full py-2 px-3 rounded-xl bg-emerald-50 group-hover:bg-emerald-600 text-emerald-800 group-hover:text-white font-bold text-xs flex items-center justify-between transition-colors shadow-2xs">
                                <span id="toolDpiCta">Verifica Risoluzione</span>
                                <span class="group-hover:translate-x-1 transition-transform">➔</span>
                            </div>
                        </div>
                    </a>

                    <!-- TOOL 6: TintaPerfetta -->
                    <a href="/tinta" class="tool-card group relative bg-white hover:bg-rose-50/20 rounded-3xl p-5 border-2 border-slate-200/90 hover:border-rose-800 shadow-xs hover:shadow-xl hover:-translate-y-1 transition-all duration-200 flex flex-col justify-between space-y-4" data-tags="tinta colore pantone cmyk rgb hex calibrazione prova stampa xeikon rotativa bobina offset digitale scarto bracketing fogra">
                        <div class="space-y-3">
                            <!-- Visual Header & Micro Blueprint -->
                            <div class="flex items-center justify-between">
                                <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-rose-800 to-rose-950 text-white flex items-center justify-center shadow-md shadow-rose-900/25 p-2">
                                    <!-- Blueprint Swatch Matrix SVG -->
                                    <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" stroke="currentColor">
                                        <rect x="4" y="4" width="7" height="7" rx="1.5" fill="#f43f5e" stroke="none" />
                                        <rect x="12.5" y="4" width="7" height="7" rx="1.5" fill="#fb7185" stroke="none" />
                                        <rect x="21" y="4" width="7" height="7" rx="1.5" fill="#fda4af" stroke="none" />
                                        
                                        <rect x="4" y="12.5" width="7" height="7" rx="1.5" fill="#e11d48" stroke="none" />
                                        <rect x="12.5" y="12.5" width="7" height="7" rx="1.5" fill="#be123c" stroke="#fde047" stroke-width="1.8" />
                                        <rect x="21" y="12.5" width="7" height="7" rx="1.5" fill="#9f1239" stroke="none" />
                                        
                                        <rect x="4" y="21" width="7" height="7" rx="1.5" fill="#9f1239" stroke="none" />
                                        <rect x="12.5" y="21" width="7" height="7" rx="1.5" fill="#881337" stroke="none" />
                                        <rect x="21" y="21" width="7" height="7" rx="1.5" fill="#4c0519" stroke="none" />
                                    </svg>
                                </div>
                                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-rose-50 text-rose-800 border border-rose-200" id="toolTintaBadge">CMYK & Xeikon</span>
                            </div>

                            <!-- Title & Direct Question Hook -->
                            <div>
                                <h3 id="toolTintaTitle" class="text-base sm:text-lg font-black text-slate-900 group-hover:text-rose-800 transition">TintaPerfetta</h3>
                                <div id="toolTintaHook" class="text-xs font-bold text-rose-800 mt-0.5">Il colore non torna in stampa?</div>
                            </div>

                            <!-- Plain Description -->
                            <p id="toolTintaDesc" class="text-xs text-slate-600 leading-relaxed">
                                Genera matrici cromatiche di scarto per azzeccare la tinta al primo colpo su rotative Xeikon e stampanti digitali.
                            </p>

                            <!-- Feature Tags -->
                            <div class="flex flex-wrap gap-1 pt-1 text-[10px] font-bold text-slate-500">
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">🎯 Matrice Scarto ±5%</span>
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">🎞️ Striscia Bobina Xeikon</span>
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">🖨️ Zero Spreco Carta</span>
                            </div>
                        </div>

                        <!-- Big Action CTA Button -->
                        <div class="pt-3 border-t border-slate-100">
                            <div class="w-full py-2 px-3 rounded-xl bg-rose-50 group-hover:bg-rose-900 text-rose-900 group-hover:text-white font-bold text-xs flex items-center justify-between transition-colors shadow-2xs">
                                <span id="toolTintaCta">Genera Matrice Prova</span>
                                <span class="group-hover:translate-x-1 transition-transform">➔</span>
                            </div>
                        </div>
                    </a>

                </div>
            </div>

            <!-- Social Share & Viral Action Strip -->
            <div class="bg-white p-4 rounded-3xl border border-slate-200 shadow-xs flex flex-col sm:flex-row items-center justify-between gap-3.5 text-center sm:text-left mt-6">
                <div class="flex items-center gap-3">
                    <span class="text-2xl">📢</span>
                    <div>
                        <span id="shareTitleText" class="text-xs sm:text-sm font-bold text-slate-900 block">Ti sono utili questi strumenti?</span>
                        <span id="shareSubText" class="text-[11px] text-slate-500 block">Condividi la suite con colleghi, collaboratori o clienti</span>
                    </div>
                </div>
                <div class="flex items-center gap-2 flex-wrap justify-center shrink-0">
                    <button type="button" onclick="shareWhatsApp()" class="inline-flex items-center gap-1.5 px-3.5 py-2 bg-emerald-600 hover:bg-emerald-500 active:scale-95 text-white text-xs font-bold rounded-xl transition shadow-xs" title="Condividi su WhatsApp">
                        <span>💬</span> <span>WhatsApp</span>
                    </button>
                    <button type="button" onclick="shareLinkedIn()" class="inline-flex items-center gap-1.5 px-3.5 py-2 bg-[#0a66c2] hover:bg-[#004182] active:scale-95 text-white text-xs font-bold rounded-xl transition shadow-xs" title="Condividi su LinkedIn">
                        <span>💼</span> <span>LinkedIn</span>
                    </button>
                    <button type="button" onclick="copyCurrentUrl()" class="inline-flex items-center gap-1.5 px-3.5 py-2 bg-slate-100 hover:bg-slate-200 active:scale-95 text-slate-700 text-xs font-bold rounded-xl border border-slate-200 transition" title="Copia Link">
                        <span>🔗</span> <span id="shareCopyText">Copia Link</span>
                    </button>
                    <button type="button" onclick="nativeShare()" class="inline-flex sm:hidden items-center gap-1.5 px-3.5 py-2 bg-blue-600 hover:bg-blue-500 active:scale-95 text-white text-xs font-bold rounded-xl transition shadow-xs" title="Altre opzioni">
                        <span>📤</span> <span>Condividi</span>
                    </button>
                </div>
            </div>

        </section>

    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-slate-200 pt-8 pb-10 text-xs text-slate-500">
        <div class="max-w-4xl mx-auto px-4 space-y-5">
            
            <!-- Suggestion Bar -->
            <div class="bg-gradient-to-r from-blue-50 to-indigo-50/70 border border-blue-200/80 rounded-2xl p-4 flex flex-col sm:flex-row items-center justify-between gap-3 text-center sm:text-left shadow-2xs">
                <div class="flex items-center gap-2.5">
                    <span class="text-xl">💡</span>
                    <span id="suggestBannerText" class="text-xs sm:text-sm font-bold text-slate-800">
                        Hai un'idea per un nuovo calcolatore tecnico?
                    </span>
                </div>
                <button type="button" onclick="openSuggestModal()" class="px-4 py-2 bg-blue-600 hover:bg-blue-500 active:scale-95 text-white font-bold text-xs rounded-xl shadow-xs transition">
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
                <a href="/tinta" class="hover:text-rose-900 transition">TintaPerfetta</a>
                <span>•</span>
                <a href="/partnership" class="text-indigo-600 hover:underline" id="navPartnerText">🤝 Diventa Partner / Sponsor</a>
            </div>

            <!-- Disclaimer and Rights -->
            <div class="text-center space-y-1.5">
                <p id="rightsText" class="font-bold text-slate-600">© 2026 OmniTools Lab — Precision Utilities Suite. Tutti i diritti riservati.</p>
                <p id="legalDisclaimerText" class="text-[10px] text-slate-500 leading-relaxed max-w-2xl mx-auto">
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
                    <h3 class="text-base font-black text-slate-900">Suggerisci un Calcolatore</h3>
                </div>
                <button type="button" onclick="closeSuggestModal()" class="text-slate-400 hover:text-slate-700 font-bold p-1">✕</button>
            </div>
            <p class="text-xs text-slate-600">Quale formula, norma o utility tecnica vorresti vedere integrata nella suite OmniTools?</p>
            <textarea id="suggestIdeaInput" rows="3" placeholder="Es. Calcolo travi in legno, caditoie stradali, resa colore..." class="w-full p-3 text-xs border border-slate-200 rounded-xl focus:border-blue-500 focus:outline-none"></textarea>
            <div class="flex justify-end gap-2">
                <button type="button" onclick="closeSuggestModal()" class="px-3 py-1.5 text-xs text-slate-600 hover:bg-slate-100 rounded-xl font-bold">Annulla</button>
                <button type="button" onclick="sendSuggestion()" id="suggestSendBtn" class="px-4 py-1.5 text-xs bg-blue-600 text-white font-bold rounded-xl hover:bg-blue-500">Invia Suggerimento</button>
            </div>
            <div id="suggestFeedback" class="hidden text-xs text-emerald-600 font-bold text-center">Grazie! Il tuo suggerimento è stato preso in carico.</div>
        </div>
    </div>

    <!-- Translations & Client Logic -->
    <script>
        const TRANSLATIONS = {t_json_str};

        function detectInitialLanguage() {{
            const saved = localStorage.getItem('omnitools_lang');
            if (saved && TRANSLATIONS[saved]) return saved;
            const langs = navigator.languages || [navigator.language || 'it'];
            for (const l of langs) {{
                const code = l.toLowerCase().split('-')[0];
                if (TRANSLATIONS[code]) return code;
            }}
            return 'en';
        }}

        let currentLang = detectInitialLanguage();
        let currentFilter = 'all';

        function changeLanguage(lang) {{
            if (!TRANSLATIONS[lang]) lang = 'en';
            currentLang = lang;
            localStorage.setItem('omnitools_lang', lang);
            document.getElementById('langSelect').value = lang;
            document.documentElement.lang = lang;
            applyTranslations();
        }}

        function applyTranslations() {{
            const t = TRANSLATIONS[currentLang] || TRANSLATIONS['it'];
            
            // Header & Hero
            if (t.tagline) document.getElementById('taglineText').textContent = t.tagline;
            if (t.hero_badge) document.getElementById('heroBadge').textContent = t.hero_badge;
            if (t.hero_title) document.getElementById('heroTitle').textContent = t.hero_title;
            if (t.hero_subtitle) document.getElementById('heroSubtitle').textContent = t.hero_subtitle;
            if (t.search_placeholder) document.getElementById('searchInput').placeholder = t.search_placeholder;

            // Division Titles & Descriptions
            if (t.division_building_title) document.getElementById('divBuildingTitle').innerHTML = 'Omni<span class=\"text-amber-600\">Building</span>';
            if (t.division_building_desc) document.getElementById('divBuildingDesc').textContent = t.division_building_desc;
            if (t.division_graph_title) document.getElementById('divGraphTitle').innerHTML = 'Omni<span class=\"text-rose-700\">Graph</span>';
            if (t.division_graph_desc) document.getElementById('divGraphDesc').textContent = t.division_graph_desc;

            // Tool 1: Rampe
            if (t.tool_rampe_title) document.getElementById('toolRampeTitle').textContent = t.tool_rampe_title;
            if (t.tool_rampe_hook) document.getElementById('toolRampeHook').textContent = t.tool_rampe_hook;
            if (t.tool_rampe_desc) document.getElementById('toolRampeDesc').textContent = t.tool_rampe_desc;
            if (t.tool_rampe_cta) document.getElementById('toolRampeCta').textContent = t.tool_rampe_cta;

            // Tool 2: Scale
            if (t.tool_scale_title) document.getElementById('toolScaleTitle').textContent = t.tool_scale_title;
            if (t.tool_scale_hook) document.getElementById('toolScaleHook').textContent = t.tool_scale_hook;
            if (t.tool_scale_desc) document.getElementById('toolScaleDesc').textContent = t.tool_scale_desc;
            if (t.tool_scale_cta) document.getElementById('toolScaleCta').textContent = t.tool_scale_cta;

            // Tool 3: Tubi
            if (t.tool_tubi_title) document.getElementById('toolTubiTitle').textContent = t.tool_tubi_title;
            if (t.tool_tubi_hook) document.getElementById('toolTubiHook').textContent = t.tool_tubi_hook;
            if (t.tool_tubi_desc) document.getElementById('toolTubiDesc').textContent = t.tool_tubi_desc;
            if (t.tool_tubi_cta) document.getElementById('toolTubiCta').textContent = t.tool_tubi_cta;

            // Tool 4: Dorso
            if (t.tool_dorso_title) document.getElementById('toolDorsoTitle').textContent = t.tool_dorso_title;
            if (t.tool_dorso_hook) document.getElementById('toolDorsoHook').textContent = t.tool_dorso_hook;
            if (t.tool_dorso_desc) document.getElementById('toolDorsoDesc').textContent = t.tool_dorso_desc;
            if (t.tool_dorso_cta) document.getElementById('toolDorsoCta').textContent = t.tool_dorso_cta;

            // Tool 5: DPI
            if (t.tool_dpi_title) document.getElementById('toolDpiTitle').textContent = t.tool_dpi_title;
            if (t.tool_dpi_hook) document.getElementById('toolDpiHook').textContent = t.tool_dpi_hook;
            if (t.tool_dpi_desc) document.getElementById('toolDpiDesc').textContent = t.tool_dpi_desc;
            if (t.tool_dpi_cta) document.getElementById('toolDpiCta').textContent = t.tool_dpi_cta;

            // Tool 6: Tinta
            if (t.tool_tinta_title) document.getElementById('toolTintaTitle').textContent = t.tool_tinta_title;
            if (t.tool_tinta_hook) document.getElementById('toolTintaHook').textContent = t.tool_tinta_hook;
            if (t.tool_tinta_desc) document.getElementById('toolTintaDesc').textContent = t.tool_tinta_desc;
            if (t.tool_tinta_cta) document.getElementById('toolTintaCta').textContent = t.tool_tinta_cta;
            if (t.tool_tinta_badge) document.getElementById('toolTintaBadge').textContent = t.tool_tinta_badge;

            // Share & Footer
            if (t.share_title) document.getElementById('shareTitleText').textContent = t.share_title;
            if (t.share_sub) document.getElementById('shareSubText').textContent = t.share_sub;
            if (t.share_copy) document.getElementById('shareCopyText').textContent = t.share_copy;
            if (t.suggest_banner) document.getElementById('suggestBannerText').textContent = t.suggest_banner;
            if (t.suggest_btn) document.getElementById('suggestBtnText').textContent = t.suggest_btn;
            if (t.nav_partner) document.getElementById('navPartnerText').innerHTML = '🤝 ' + t.nav_partner;
            if (t.rights_reserved) document.getElementById('rightsText').textContent = t.rights_reserved;
            if (t.legal_disclaimer) document.getElementById('legalDisclaimerText').innerHTML = t.legal_disclaimer;
        }}

        // Filter / Search Management
        function setFilter(filter) {{
            currentFilter = filter;
            const btnAll = document.getElementById('filterAllBtn');
            const btnBuilding = document.getElementById('filterBuildingBtn');
            const btnGraph = document.getElementById('filterGraphBtn');

            // Reset base classes
            const baseInactive = "flex flex-col sm:flex-row items-center justify-center gap-1.5 sm:gap-2.5 py-2 sm:py-2.5 px-2 rounded-2xl bg-white hover:bg-slate-50 text-slate-700 border border-slate-200/90 font-bold text-xs sm:text-sm transition-all duration-150";

            btnAll.className = filter === 'all' 
                ? "flex flex-col sm:flex-row items-center justify-center gap-1.5 sm:gap-2.5 py-2 sm:py-2.5 px-2 rounded-2xl bg-blue-600 text-white shadow-md shadow-blue-600/20 font-bold text-xs sm:text-sm transition-all duration-150"
                : baseInactive;

            btnBuilding.className = filter === 'building'
                ? "flex flex-col sm:flex-row items-center justify-center gap-1.5 sm:gap-2.5 py-2 sm:py-2.5 px-2 rounded-2xl bg-amber-600 text-white shadow-md shadow-amber-600/25 border-amber-600 font-bold text-xs sm:text-sm transition-all duration-150"
                : baseInactive;

            btnGraph.className = filter === 'graph'
                ? "flex flex-col sm:flex-row items-center justify-center gap-1.5 sm:gap-2.5 py-2 sm:py-2.5 px-2 rounded-2xl bg-rose-900 text-white shadow-md shadow-rose-900/25 border-rose-900 font-bold text-xs sm:text-sm transition-all duration-150"
                : baseInactive;

            // Adjust subtext colors
            const subAll = btnAll.querySelector('.subtext');
            if (subAll) subAll.className = filter === 'all' ? "subtext text-[10px] text-blue-100 font-normal hidden sm:block" : "subtext text-[10px] text-slate-500 font-normal hidden sm:block";

            const subB = btnBuilding.querySelector('.subtext');
            if (subB) subB.className = filter === 'building' ? "subtext text-[10px] text-amber-100 font-normal hidden sm:block" : "subtext text-[10px] text-amber-700/80 font-normal hidden sm:block";

            const subG = btnGraph.querySelector('.subtext');
            if (subG) subG.className = filter === 'graph' ? "subtext text-[10px] text-rose-200 font-normal hidden sm:block" : "subtext text-[10px] text-rose-800/80 font-normal hidden sm:block";

            filterTools();
        }}

        function filterTools() {{
            const query = document.getElementById('searchInput').value.toLowerCase().trim();
            const clearBtn = document.getElementById('clearSearchBtn');
            if (query.length > 0) {{
                clearBtn.classList.remove('hidden');
            }} else {{
                clearBtn.classList.add('hidden');
            }}

            const secBuilding = document.getElementById('sectionBuilding');
            const secGraph = document.getElementById('sectionGraph');

            let visibleBuildingCards = 0;
            let visibleGraphCards = 0;

            const cards = document.querySelectorAll('.tool-card');
            cards.forEach(card => {{
                const isBuildingCard = card.closest('#sectionBuilding') !== null;
                const isGraphCard = card.closest('#sectionGraph') !== null;

                // Check division filter
                let allowedByDivision = true;
                if (currentFilter === 'building' && !isBuildingCard) allowedByDivision = false;
                if (currentFilter === 'graph' && !isGraphCard) allowedByDivision = false;

                // Check search query
                const text = card.textContent.toLowerCase();
                const tags = (card.getAttribute('data-tags') || '').toLowerCase();
                const matchQuery = query === '' || text.includes(query) || tags.includes(query);

                if (allowedByDivision && matchQuery) {{
                    card.classList.remove('hidden');
                    if (isBuildingCard) visibleBuildingCards++;
                    if (isGraphCard) visibleGraphCards++;
                }} else {{
                    card.classList.add('hidden');
                }}
            }});

            // Show or hide division containers based on visible cards
            if (visibleBuildingCards > 0 && (currentFilter === 'all' || currentFilter === 'building')) {{
                secBuilding.classList.remove('hidden');
            }} else {{
                secBuilding.classList.add('hidden');
            }}

            if (visibleGraphCards > 0 && (currentFilter === 'all' || currentFilter === 'graph')) {{
                secGraph.classList.remove('hidden');
            }} else {{
                secGraph.classList.add('hidden');
            }}
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
            filterTools();
        }});
    </script>
</body>
</html>
"""

with open("/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/index.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("index.html compiled with Vibrant Magnetic Child-Proof Hub successfully.")
