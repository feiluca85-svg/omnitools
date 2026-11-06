import json
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(cur_dir, 'translations_hub.json'), 'r', encoding='utf-8') as f:
    t_data = json.load(f)

t_json_str = json.dumps(t_data, ensure_ascii=False)

html_code = f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>OmniTools Lab — Calcolatori Tecnici Online: Cantiere, Grafica & Finanza</title>
    <meta name="description" content="OmniTools Lab: Suite gratuita di 12 calcolatori tecnici e finanziari online: Rampe (DM 236/89), Scale, Tubi, Dorso, DPI, Tinta, Barcode, Copertura, Resa Carta, Mutuo, PAC e Margine/Markup.">
    
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
<body class="bg-slate-50 text-slate-800 font-sans antialiased min-h-screen flex flex-col justify-between selection:bg-blue-500 selection:text-white overflow-x-hidden">

    <!-- Top Navigation Header -->
    <header class="bg-white/95 border-b border-slate-200 sticky top-0 z-40 backdrop-blur-md shadow-2xs" style="padding-top: max(env(safe-area-inset-top), 8px); padding-bottom: 8px;">
        <div class="max-w-5xl mx-auto px-4 py-1 flex items-center justify-between gap-3">
            
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
        <section class="max-w-5xl mx-auto px-4 text-center space-y-3.5">
            
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
                Calcolatori tecnici e quantitativi per cantiere, grafica e finanza. Formule certificate, zero registrazioni, subito pronti offline.
            </p>

            <!-- Spotlight Search Bar -->
            <div class="pt-1 max-w-lg mx-auto">
                <div class="relative">
                    <div class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-slate-400">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                        </svg>
                    </div>
                    <input type="text" id="searchInput" oninput="filterTools()" placeholder="Cerca: rampa, gradini, tubi, dorso libro, cmyk, mutuo, pac, margine..." class="w-full bg-white hover:bg-slate-50/70 focus:bg-white border border-slate-300 focus:border-blue-600 focus:ring-4 focus:ring-blue-100 rounded-2xl pl-10 pr-9 py-2.5 sm:py-3 text-xs sm:text-sm text-slate-900 placeholder-slate-400 outline-none shadow-xs transition">
                    <button type="button" id="clearSearchBtn" onclick="clearSearch()" class="hidden absolute inset-y-0 right-0 pr-3.5 flex items-center text-slate-400 hover:text-slate-700 text-sm font-bold">
                        ✕
                    </button>
                </div>
            </div>

            <!-- DIVISION SEGMENTED PICKER: Tabbed Hub (OmniTools 12-Tool Standard) -->
            <div class="pt-2 sm:pt-3 max-w-3xl sm:max-w-4xl mx-auto w-full">
                <div class="grid grid-cols-2 sm:grid-cols-4 gap-1.5 sm:gap-2.5 p-1 sm:p-1.5 bg-slate-200/70 rounded-2xl sm:rounded-3xl backdrop-blur-xs border border-slate-200">
                    
                    <!-- Tab 1: Tutti i Tool -->
                    <button type="button" onclick="setFilter('all')" id="filterAllBtn" class="flex flex-col sm:flex-row items-center justify-center gap-1.5 sm:gap-2.5 py-2 sm:py-2.5 px-2 sm:px-3 rounded-xl sm:rounded-2xl bg-blue-600 text-white shadow-md shadow-blue-600/25 font-bold transition-all duration-200 active:scale-95 cursor-pointer">
                        <div class="w-7 h-7 sm:w-9 sm:h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-700 flex items-center justify-center text-white shrink-0 p-1 shadow-xs border border-white/30">
                            <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <circle cx="16" cy="16" r="13.2" stroke="#ffffff" stroke-width="3.4" />
                                <path d="M 7.5 11.5 H 24.5 M 16 11.5 V 24.5" stroke="#ffffff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" />
                                <circle cx="16" cy="11.5" r="2.1" fill="#38bdf8" />
                            </svg>
                        </div>
                        <div class="text-center sm:text-left leading-tight">
                            <span class="sm:hidden font-black text-xs block text-white">Tutti (12)</span>
                            <span id="filterAllText" class="hidden sm:block text-xs sm:text-[14px] font-black tracking-tight leading-tight">Tutti i Tool</span>
                            <span class="subtext text-[10px] sm:text-[11px] text-blue-100 font-semibold hidden sm:block">12 Strumenti</span>
                        </div>
                    </button>

                    <!-- Tab 2: OmniBuilding -->
                    <button type="button" onclick="setFilter('building')" id="filterBuildingBtn" class="flex flex-col sm:flex-row items-center justify-center gap-1.5 sm:gap-2.5 py-2 sm:py-2.5 px-2 sm:px-3 rounded-xl sm:rounded-2xl bg-white hover:bg-slate-50 text-slate-700 border border-slate-200/80 font-bold transition-all duration-200 active:scale-95 cursor-pointer">
                        <div class="w-7 h-7 sm:w-9 sm:h-9 rounded-xl bg-gradient-to-br from-amber-500 to-amber-700 flex items-center justify-center text-white shrink-0 p-1 shadow-xs border border-amber-300/40">
                            <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <circle cx="16" cy="16" r="13.2" stroke="#ffffff" stroke-width="3" />
                                <path d="M 9.5 8.5 V 23.5 H 24.5" stroke="#ffffff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" />
                                <line x1="9.5" y1="23.5" x2="22.5" y2="10.5" stroke="#ffffff" stroke-width="2" stroke-dasharray="2.5 2" />
                                <circle cx="9.5" cy="23.5" r="2.2" fill="#fde047" />
                            </svg>
                        </div>
                        <div class="text-center sm:text-left leading-tight">
                            <span class="sm:hidden font-black text-xs block text-current">Building (3)</span>
                            <span class="hidden sm:block text-xs sm:text-[14px] font-black tracking-tight leading-tight">OmniBuilding</span>
                            <span class="subtext text-[10px] sm:text-[11px] text-slate-500 font-semibold hidden sm:block">3 Cantiere & Impianti</span>
                        </div>
                    </button>

                    <!-- Tab 3: OmniGraph -->
                    <button type="button" onclick="setFilter('graph')" id="filterGraphBtn" class="flex flex-col sm:flex-row items-center justify-center gap-1.5 sm:gap-2.5 py-2 sm:py-2.5 px-2 sm:px-3 rounded-xl sm:rounded-2xl bg-white hover:bg-slate-50 text-slate-700 border border-slate-200/80 font-bold transition-all duration-200 active:scale-95 cursor-pointer">
                        <div class="w-7 h-7 sm:w-9 sm:h-9 rounded-xl bg-gradient-to-br from-rose-800 to-rose-950 flex items-center justify-center text-white shrink-0 p-1 shadow-xs border border-rose-300/40">
                            <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <circle cx="16" cy="16" r="13.2" stroke="#ffffff" stroke-width="2.8" />
                                <circle cx="16" cy="16" r="6" stroke="#ffffff" stroke-width="2" />
                                <line x1="16" y1="4.5" x2="16" y2="27.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round" />
                                <line x1="4.5" y1="16" x2="27.5" y2="16" stroke="#ffffff" stroke-width="2" stroke-linecap="round" />
                                <circle cx="16" cy="16" r="2.2" fill="#fda4af" />
                            </svg>
                        </div>
                        <div class="text-center sm:text-left leading-tight">
                            <span class="sm:hidden font-black text-xs block text-current">Graph (6)</span>
                            <span class="hidden sm:block text-xs sm:text-[14px] font-black tracking-tight leading-tight">OmniGraph</span>
                            <span class="subtext text-[10px] sm:text-[11px] text-slate-500 font-semibold hidden sm:block">6 Grafica & Stampa</span>
                        </div>
                    </button>

                    <!-- Tab 4: OmniFinance -->
                    <button type="button" onclick="setFilter('finance')" id="filterFinanceBtn" class="flex flex-col sm:flex-row items-center justify-center gap-1.5 sm:gap-2.5 py-2 sm:py-2.5 px-2 sm:px-3 rounded-xl sm:rounded-2xl bg-white hover:bg-slate-50 text-slate-700 border border-slate-200/80 font-bold transition-all duration-200 active:scale-95 cursor-pointer">
                        <div class="w-7 h-7 sm:w-9 sm:h-9 rounded-xl bg-gradient-to-br from-emerald-600 to-teal-800 flex items-center justify-center text-white shrink-0 p-1 shadow-xs border border-emerald-300/40">
                            <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <circle cx="16" cy="16" r="13.2" stroke="#ffffff" stroke-width="2.6" />
                                <polygon points="16,6.5 24.5,13.5 16,25.5 7.5,13.5" stroke="#ffffff" stroke-width="2" fill="none" stroke-linejoin="round" />
                                <line x1="7.5" y1="13.5" x2="24.5" y2="13.5" stroke="#ffffff" stroke-width="1.8" />
                                <circle cx="16" cy="13.5" r="2.2" fill="#34d399" />
                            </svg>
                        </div>
                        <div class="text-center sm:text-left leading-tight">
                            <span class="sm:hidden font-black text-xs block text-current">Finance (3)</span>
                            <span class="hidden sm:block text-xs sm:text-[14px] font-black tracking-tight leading-tight">OmniFinance</span>
                            <span class="subtext text-[10px] sm:text-[11px] text-slate-500 font-semibold hidden sm:block">3 Finanza & Business</span>
                        </div>
                    </button>

                </div>
            </div>

        </section>

        <!-- Tools Showcase -->
        <section class="max-w-5xl mx-auto px-4 space-y-8">
            
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
                    <a href="/scale" class="tool-card group relative bg-white hover:bg-amber-50/20 rounded-3xl p-5 border-2 border-slate-200/90 hover:border-amber-500 shadow-xs hover:shadow-xl hover:-translate-y-1 transition-all duration-200 flex flex-col justify-between space-y-4" data-tags="scala scale gradini gradino alzata pedata blondel dislivello scale interne din 18065 numero gradini">
                        <div class="space-y-3">
                            <!-- Visual Header & Micro Blueprint -->
                            <div class="flex items-center justify-between">
                                <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-amber-500 to-amber-600 text-white flex items-center justify-center shadow-md shadow-amber-500/25 p-2">
                                    <!-- Blueprint Stairs SVG -->
                                    <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" stroke="currentColor">
                                        <path d="M 5 25 H 12 V 18 H 19 V 11 H 27" stroke="#ffffff" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" />
                                        <line x1="12" y1="25" x2="12" y2="18" stroke="#fde047" stroke-width="2" stroke-dasharray="1.5 1.5" />
                                        <line x1="19" y1="18" x2="19" y2="11" stroke="#fde047" stroke-width="2" stroke-dasharray="1.5 1.5" />
                                    </svg>
                                </div>
                                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-amber-50 text-amber-700 border border-amber-200">Blondel</span>
                            </div>

                            <!-- Title & Direct Question Hook -->
                            <div>
                                <h3 id="toolScaleTitle" class="text-base sm:text-lg font-black text-slate-900 group-hover:text-amber-600 transition">ScalaFacile</h3>
                                <div id="toolScaleHook" class="text-xs font-bold text-amber-700 mt-0.5">Quanti gradini servono?</div>
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
                            <div class="w-full py-2 px-3 rounded-xl bg-amber-50 group-hover:bg-amber-500 text-amber-800 group-hover:text-white font-bold text-xs flex items-center justify-between transition-colors shadow-2xs">
                                <span id="toolScaleCta">Progetta Scala Ora</span>
                                <span class="group-hover:translate-x-1 transition-transform">➔</span>
                            </div>
                        </div>
                    </a>

                    <!-- TOOL 3: ScaricoFacile -->
                    <a href="/tubi" class="tool-card group relative bg-white hover:bg-amber-50/20 rounded-3xl p-5 border-2 border-slate-200/90 hover:border-amber-500 shadow-xs hover:shadow-xl hover:-translate-y-1 transition-all duration-200 flex flex-col justify-between space-y-4" data-tags="scarico scarichi tubi pendenza tubazioni fognatura acque nere grigie caduta en 12056 pendenza scarico autopulizia">
                        <div class="space-y-3">
                            <!-- Visual Header & Micro Blueprint -->
                            <div class="flex items-center justify-between">
                                <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-amber-500 to-amber-600 text-white flex items-center justify-center shadow-md shadow-amber-500/25 p-2">
                                    <!-- Blueprint Pipe Flow SVG -->
                                    <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" stroke="currentColor">
                                        <line x1="5" y1="11" x2="27" y2="21" stroke="#ffffff" stroke-width="4.5" stroke-linecap="round" />
                                        <path d="M 12 14.5 C 15 16, 17 17, 20 18.5" stroke="#fde047" stroke-width="2" stroke-linecap="round" />
                                        <circle cx="21" cy="22" r="2" fill="#fde047" />
                                    </svg>
                                </div>
                                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-amber-50 text-amber-700 border border-amber-200">UNI EN 12056</span>
                            </div>

                            <!-- Title & Direct Question Hook -->
                            <div>
                                <h3 id="toolTubiTitle" class="text-base sm:text-lg font-black text-slate-900 group-hover:text-amber-600 transition">ScaricoFacile</h3>
                                <div id="toolTubiHook" class="text-xs font-bold text-amber-700 mt-0.5">L'acqua scorre o si intasa?</div>
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
                            <div class="w-full py-2 px-3 rounded-xl bg-amber-50 group-hover:bg-amber-500 text-amber-800 group-hover:text-white font-bold text-xs flex items-center justify-between transition-colors shadow-2xs">
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
                    <span class="text-xs font-mono font-bold text-rose-900 bg-rose-50 px-2.5 py-1 rounded-xl border border-rose-200 hidden sm:inline-block">5 Tool Attivi</span>
                </div>

                <!-- 4 Graphic Tools Grid -->
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                    
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
                    <a href="/dpi" class="tool-card group relative bg-white hover:bg-rose-50/20 rounded-3xl p-5 sm:p-6 border-2 border-slate-200/90 hover:border-rose-700 shadow-xs hover:shadow-xl hover:-translate-y-1 transition-all duration-200 flex flex-col justify-between space-y-4" data-tags="dpi ppi pixel pixelatura risoluzione stampa formato grande formato poster manifesto offset distanza occhio photoshop acuità visiva">
                        <div class="space-y-3">
                            <!-- Visual Header & Micro Blueprint -->
                            <div class="flex items-center justify-between">
                                <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-rose-800 to-rose-950 text-white flex items-center justify-center shadow-md shadow-rose-900/25 p-2">
                                    <!-- Blueprint DPI Grid SVG -->
                                    <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" stroke="currentColor">
                                        <circle cx="14" cy="14" r="9" stroke="#ffffff" stroke-width="2.5" />
                                        <line x1="20.5" y1="20.5" x2="27" y2="27" stroke="#ffffff" stroke-width="3" stroke-linecap="round" />
                                        <rect x="10" y="10" width="3" height="3" fill="#fda4af" />
                                        <rect x="15" y="10" width="3" height="3" fill="#fda4af" />
                                        <rect x="10" y="15" width="3" height="3" fill="#fda4af" />
                                        <rect x="15" y="15" width="3" height="3" fill="#fda4af" />
                                    </svg>
                                </div>
                                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-rose-50 text-rose-800 border border-rose-200">Pixel & Acuità</span>
                            </div>

                            <!-- Title & Direct Question Hook -->
                            <div>
                                <h3 id="toolDpiTitle" class="text-base sm:text-lg font-black text-slate-900 group-hover:text-rose-800 transition">RisoluzioneFacile</h3>
                                <div id="toolDpiHook" class="text-xs font-bold text-rose-800 mt-0.5">Verrà sgranato in stampa?</div>
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
                            <div class="w-full py-2 px-3 rounded-xl bg-rose-50 group-hover:bg-rose-900 text-rose-900 group-hover:text-white font-bold text-xs flex items-center justify-between transition-colors shadow-2xs">
                                <span id="toolDpiCta">Verifica Risoluzione</span>
                                <span class="group-hover:translate-x-1 transition-transform">➔</span>
                            </div>
                        </div>
                    </a>

                    <!-- TOOL 6: TintaPerfetta -->
                    <a href="/tinta" class="tool-card group relative bg-white hover:bg-rose-50/20 rounded-3xl p-5 border-2 border-slate-200/90 hover:border-rose-800 shadow-xs hover:shadow-xl hover:-translate-y-1 transition-all duration-200 flex flex-col justify-between space-y-4" data-tags="tinta colore pantone cmyk rgb hex calibrazione prova stampa bobina rotativa bobina offset digitale scarto bracketing fogra">
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
                                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-rose-50 text-rose-800 border border-rose-200" id="toolTintaBadge">CMYK & Rotativa</span>
                            </div>

                            <!-- Title & Direct Question Hook -->
                            <div>
                                <h3 id="toolTintaTitle" class="text-base sm:text-lg font-black text-slate-900 group-hover:text-rose-800 transition">TintaPerfetta</h3>
                                <div id="toolTintaHook" class="text-xs font-bold text-rose-800 mt-0.5">Il colore non torna in stampa?</div>
                            </div>

                            <!-- Plain Description -->
                            <p id="toolTintaDesc" class="text-xs text-slate-600 leading-relaxed">
                                Genera matrici cromatiche di scarto per azzeccare la tinta al primo colpo su rotative Rotativa e stampanti digitali.
                            </p>

                            <!-- Feature Tags -->
                            <div class="flex flex-wrap gap-1 pt-1 text-[10px] font-bold text-slate-500">
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">🎯 Matrice Scarto ±5%</span>
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">🎞️ Striscia Bobina Rotativa</span>
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

                    <!-- TOOL 7: OmniBarcode Studio -->
                    <a href="/barcode" class="tool-card group relative bg-white hover:bg-rose-50/20 rounded-3xl p-5 border-2 border-slate-200/90 hover:border-rose-700 shadow-xs hover:shadow-xl hover:-translate-y-1 transition-all duration-200 flex flex-col justify-between space-y-4" data-tags="barcode codice a barre ean 13 ean13 upc code 128 code 39 tessera sanitaria codice fiscale gs1 laser 670 nm vettoriale svg contrasto scanner cassa">
                        <div class="space-y-3">
                            <!-- Visual Header & Micro Blueprint -->
                            <div class="flex items-center justify-between">
                                <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-rose-800 to-rose-950 text-white flex items-center justify-center shadow-md shadow-rose-900/25 p-2">
                                    <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" stroke="currentColor">
                                        <rect x="4" y="6" width="24" height="20" rx="4" fill="#4c0519" />
                                        <line x1="8" y1="10" x2="8" y2="22" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
                                        <line x1="11" y1="10" x2="11" y2="22" stroke="#ffffff" stroke-width="1.2" stroke-linecap="round"/>
                                        <line x1="14" y1="10" x2="14" y2="22" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round"/>
                                        <line x1="18" y1="10" x2="18" y2="22" stroke="#ffffff" stroke-width="1.2" stroke-linecap="round"/>
                                        <line x1="21" y1="10" x2="21" y2="22" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round"/>
                                        <line x1="24" y1="10" x2="24" y2="22" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round"/>
                                        <line x1="5" y1="16" x2="27" y2="16" stroke="#fda4af" stroke-width="1.6" stroke-linecap="round" />
                                    </svg>
                                </div>
                                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-rose-50 text-rose-800 border border-rose-200" id="toolBarcodeBadge">GS1 & Vettoriale</span>
                            </div>

                            <!-- Title & Direct Question Hook -->
                            <div>
                                <h3 id="toolBarcodeTitle" class="text-base sm:text-lg font-black text-slate-900 group-hover:text-rose-800 transition">OmniBarcode</h3>
                                <div id="toolBarcodeHook" class="text-xs font-bold text-rose-800 mt-0.5">Il codice passerà alla cassa?</div>
                            </div>

                            <!-- Plain Description -->
                            <p id="toolBarcodeDesc" class="text-xs text-slate-600 leading-relaxed">
                                Genera codici a barre SVG vettoriali puri (EAN-13, Tessera Sanitaria Code 39, Code 128) con verifica contrasto laser 670 nm GS1.
                            </p>

                            <!-- Feature Tags -->
                            <div class="flex flex-wrap gap-1 pt-1 text-[10px] font-bold text-slate-500">
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">🏷️ EAN-13 & Code 128</span>
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">🏥 Tessera Sanitaria</span>
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">🔴 Laser 670 nm</span>
                            </div>
                        </div>

                        <!-- Big Action CTA Button -->
                        <div class="pt-3 border-t border-slate-100">
                            <div class="w-full py-2 px-3 rounded-xl bg-rose-50 group-hover:bg-rose-900 text-rose-900 group-hover:text-white font-bold text-xs flex items-center justify-between transition-colors shadow-2xs">
                                <span id="toolBarcodeCta">Genera Codice a Barre</span>
                                <span class="group-hover:translate-x-1 transition-transform">➔</span>
                            </div>
                        </div>
                    </a>

                    <!-- TOOL 8: CoperturaFacile -->
                    <a href="/copertura" class="tool-card group relative bg-white hover:bg-rose-50/20 rounded-3xl p-5 border-2 border-slate-200/90 hover:border-rose-700 shadow-xs hover:shadow-xl hover:-translate-y-1 transition-all duration-200 flex flex-col justify-between space-y-4" data-tags="copertura inchiostro cmyk tac total area coverage costo copia stampa preventivo quadricromia densitometria rip">
                        <div class="space-y-3">
                            <!-- Visual Header & Micro Blueprint -->
                            <div class="flex items-center justify-between">
                                <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-rose-800 to-rose-950 text-white flex items-center justify-center shadow-md shadow-rose-900/25 p-2">
                                    <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" stroke="currentColor">
                                        <rect x="4" y="6" width="24" height="20" rx="4" fill="#881337" />
                                        <circle cx="11" cy="13" r="3" fill="#22d3ee" />
                                        <circle cx="21" cy="13" r="3" fill="#ec4899" />
                                        <circle cx="16" cy="20" r="3" fill="#facc15" />
                                    </svg>
                                </div>
                                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-rose-50 text-rose-800 border border-rose-200" id="toolCoperturaBadge">CMYK & Costo Copia</span>
                            </div>

                            <!-- Title & Direct Question Hook -->
                            <div>
                                <h3 id="toolCoperturaTitle" class="text-base sm:text-lg font-black text-slate-900 group-hover:text-rose-700 transition">CoperturaFacile</h3>
                                <div id="toolCoperturaHook" class="text-xs font-bold text-rose-800 mt-0.5">Quanto inchiostro consumerà la commessa?</div>
                            </div>

                            <!-- Plain Description -->
                            <p id="toolCoperturaDesc" class="text-xs text-slate-600 leading-relaxed">
                                Analisi densitometrica CMYK e TAC (Total Area Coverage) in tempo reale. Calcola il consumo in grammi e il costo copia con privacy totale.
                            </p>

                            <!-- Feature Tags -->
                            <div class="flex flex-wrap gap-1 pt-1 text-[10px] font-bold text-slate-500">
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">📊 Separazione CMYK</span>
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">🔥 Mappa TAC</span>
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">💰 Costo Tiratura</span>
                            </div>
                        </div>

                        <!-- Big Action CTA Button -->
                        <div class="pt-3 border-t border-slate-100">
                            <div class="w-full py-2 px-3 rounded-xl bg-rose-50 group-hover:bg-rose-900 text-rose-900 group-hover:text-white font-bold text-xs flex items-center justify-between transition-colors shadow-2xs">
                                <span id="toolCoperturaCta">Calcola Copertura & Costi</span>
                                <span class="group-hover:translate-x-1 transition-transform">➔</span>
                            </div>
                        </div>
                    </a>

                    <!-- TOOL 9: ResaCarta -->
                    <a href="/resa" class="tool-card group relative bg-white hover:bg-rose-50/20 rounded-3xl p-5 border-2 border-slate-200/90 hover:border-rose-700 shadow-xs hover:shadow-xl hover:-translate-y-1 transition-all duration-200 flex flex-col justify-between space-y-4" data-tags="resa carta foglio macchina taglio ghigliottina 70x100 64x88 sra3 sfrido pose impaginazione nesting fibra">
                        <div class="space-y-3">
                            <!-- Visual Header & Micro Blueprint -->
                            <div class="flex items-center justify-between">
                                <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-rose-800 to-rose-950 text-white flex items-center justify-center shadow-md shadow-rose-900/25 p-2">
                                    <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" stroke="currentColor">
                                        <rect x="4" y="4" width="24" height="24" rx="3" fill="#4c0519" stroke="#fda4af" stroke-width="1.5" />
                                        <rect x="7" y="7" width="8" height="6" rx="1" fill="#f43f5e" />
                                        <rect x="17" y="7" width="8" height="6" rx="1" fill="#f43f5e" />
                                        <rect x="7" y="15" width="8" height="6" rx="1" fill="#f43f5e" />
                                        <rect x="17" y="15" width="8" height="6" rx="1" fill="#f43f5e" />
                                    </svg>
                                </div>
                                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-rose-50 text-rose-800 border border-rose-200" id="toolResaBadge">Nesting & Taglio</span>
                            </div>

                            <!-- Title & Direct Question Hook -->
                            <div>
                                <h3 id="toolResaTitle" class="text-base sm:text-lg font-black text-slate-900 group-hover:text-rose-800 transition">ResaCarta</h3>
                                <div id="toolResaHook" class="text-xs font-bold text-rose-800 mt-0.5">Quante pose entrano nel foglio macchina?</div>
                            </div>

                            <!-- Plain Description -->
                            <p id="toolResaDesc" class="text-xs text-slate-600 leading-relaxed">
                                Ottimizzazione taglio da 70x100, 64x88 e SRA3. Calcolo pose con rotazione, sfrido %, peso commessa e verifica senso fibra per la piega.
                            </p>

                            <!-- Feature Tags -->
                            <div class="flex flex-wrap gap-1 pt-1 text-[10px] font-bold text-slate-500">
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">📐 Schema 2D</span>
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">✂️ Azzera Sfrido</span>
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">🧭 Senso Fibra</span>
                            </div>
                        </div>

                        <!-- Big Action CTA Button -->
                        <div class="pt-3 border-t border-slate-100">
                            <div class="w-full py-2 px-3 rounded-xl bg-rose-50 group-hover:bg-rose-900 text-rose-900 group-hover:text-white font-bold text-xs flex items-center justify-between transition-colors shadow-2xs">
                                <span id="toolResaCta">Calcola Resa Fogli</span>
                                <span class="group-hover:translate-x-1 transition-transform">➔</span>
                            </div>
                        </div>
                    </a>

                </div>
            </div>

            
            <!-- ========================================== -->
            <!-- DIVISION 3: OmniFinance (Finanza & Business) -->
            <!-- ========================================== -->
            <div id="sectionFinance" class="space-y-4 pt-4">
                
                <!-- Division Department Header -->
                <div class="flex items-center justify-between pb-2.5 border-b-2 border-emerald-500/20">
                    <div class="flex items-center gap-2.5">
                        <div class="w-8 h-8 rounded-xl bg-gradient-to-br from-emerald-600 via-teal-700 to-slate-900 flex items-center justify-center text-white shadow-sm shadow-emerald-500/30 shrink-0 p-1">
                            <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <circle cx="16" cy="16" r="13.2" stroke="#ffffff" stroke-width="2.6" />
                                <polygon points="16,6.5 24.5,13.5 16,25.5 7.5,13.5" stroke="#ffffff" stroke-width="2" fill="none" stroke-linejoin="round" />
                                <line x1="7.5" y1="13.5" x2="24.5" y2="13.5" stroke="#ffffff" stroke-width="1.8" />
                                <circle cx="16" cy="13.5" r="2.2" fill="#34d399" />
                            </svg>
                        </div>
                        <div>
                            <div class="flex items-center gap-2">
                                <h2 id="divFinanceTitle" class="text-base sm:text-lg font-black text-emerald-950 tracking-tight font-jakarta leading-none">Omni<span class="text-emerald-700">Finance</span></h2>
                                <span class="text-[9px] font-extrabold uppercase bg-emerald-100 text-emerald-900 px-2 py-0.5 rounded-full border border-emerald-300">Reparto Finanza</span>
                            </div>
                            <p id="divFinanceDesc" class="text-[11px] text-slate-500 mt-0.5">Calcolatori quantitativi e formule matematiche per mutui, investimenti e pricing commerciale</p>
                        </div>
                    </div>
                    <span class="text-xs font-mono font-bold text-emerald-800 bg-emerald-50 px-2.5 py-1 rounded-xl border border-emerald-200 hidden sm:inline-block">3 Tool Attivi</span>
                </div>

                <!-- 3 Finance Tools Grid -->
                <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                    
                    <!-- TOOL 10: MutuoFacile -->
                    <a href="/mutuo" class="tool-card group relative bg-white hover:bg-emerald-50/20 rounded-3xl p-5 border-2 border-slate-200/90 hover:border-emerald-600 shadow-xs hover:shadow-xl hover:-translate-y-1 transition-all duration-200 flex flex-col justify-between space-y-4" data-tags="mutuo rata ammortamento francese banca finanziamento debito tasso tan taeg prestito sostenibilita reddito 33%">
                        <div class="space-y-3">
                            <!-- Visual Header & Micro Blueprint -->
                            <div class="flex items-center justify-between">
                                <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-emerald-600 via-teal-700 to-slate-900 text-white flex items-center justify-center shadow-md shadow-emerald-700/25 p-2">
                                    <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" stroke="currentColor">
                                        <path d="M4 12 L16 4 L28 12 Z" fill="#047857" stroke="#34d399" stroke-width="1.5" stroke-linejoin="round"/>
                                        <rect x="7" y="13" width="3" height="11" rx="0.5" fill="#34d399"/>
                                        <rect x="12" y="13" width="3" height="11" rx="0.5" fill="#34d399"/>
                                        <rect x="17" y="13" width="3" height="11" rx="0.5" fill="#34d399"/>
                                        <rect x="22" y="13" width="3" height="11" rx="0.5" fill="#34d399"/>
                                        <rect x="4" y="24" width="24" height="4" rx="1" fill="#065f46" stroke="#34d399" stroke-width="1.5"/>
                                    </svg>
                                </div>
                                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-800 border border-emerald-200" id="toolMutuoBadge">Ammortamento Francese</span>
                            </div>

                            <!-- Title & Direct Question Hook -->
                            <div>
                                <h3 id="toolMutuoTitle" class="text-base sm:text-lg font-black text-slate-900 group-hover:text-emerald-700 transition">MutuoFacile</h3>
                                <div id="toolMutuoHook" class="text-xs font-bold text-emerald-800 mt-0.5">Quanto peserà la rata sul tuo stipendio?</div>
                            </div>

                            <!-- Plain Description -->
                            <p id="toolMutuoDesc" class="text-xs text-slate-600 leading-relaxed">
                                Calcola la rata mensile costante, il totale interessi bancari, il piano di ammortamento e la sostenibilità con la regola bancaria del 33%.
                            </p>

                            <!-- Feature Tags -->
                            <div class="flex flex-wrap gap-1 pt-1 text-[10px] font-bold text-slate-500">
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">🏦 Rata Mensile</span>
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">📊 Tabella Anno/Anno</span>
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">🛡️ Sostenibilità 33%</span>
                            </div>
                        </div>

                        <!-- Big Action CTA Button -->
                        <div class="pt-3 border-t border-slate-100">
                            <div class="w-full py-2 px-3 rounded-xl bg-emerald-50 group-hover:bg-emerald-700 text-emerald-900 group-hover:text-white font-bold text-xs flex items-center justify-between transition-colors shadow-2xs">
                                <span id="toolMutuoCta">Calcola Rata Mutuo</span>
                                <span class="group-hover:translate-x-1 transition-transform">➔</span>
                            </div>
                        </div>
                    </a>

                    <!-- TOOL 11: InteresseComposto -->
                    <a href="/pac" class="tool-card group relative bg-white hover:bg-emerald-50/20 rounded-3xl p-5 border-2 border-slate-200/90 hover:border-emerald-600 shadow-xs hover:shadow-xl hover:-translate-y-1 transition-all duration-200 flex flex-col justify-between space-y-4" data-tags="interesse composto pac piano accumulo risparmio rendita 4% s&p500 investimento dividendi montante ricchezza fire">
                        <div class="space-y-3">
                            <!-- Visual Header & Micro Blueprint -->
                            <div class="flex items-center justify-between">
                                <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-emerald-600 via-teal-700 to-slate-900 text-white flex items-center justify-center shadow-md shadow-emerald-700/25 p-2">
                                    <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" stroke="currentColor">
                                        <path d="M5 25 L11 20 L17 17 L22 11 L27 6" stroke="#34d399" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
                                        <path d="M5 25 L11 20 L17 17 L22 11 L27 6 L27 25 Z" fill="rgba(52, 211, 153, 0.25)"/>
                                        <circle cx="27" cy="6" r="3" fill="#10b981" stroke="#ffffff" stroke-width="1.5"/>
                                        <line x1="5" y1="25" x2="27" y2="25" stroke="#ffffff" stroke-width="1.5" opacity="0.6"/>
                                    </svg>
                                </div>
                                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-800 border border-emerald-200" id="toolPacBadge">PAC & Rendita 4%</span>
                            </div>

                            <!-- Title & Direct Question Hook -->
                            <div>
                                <h3 id="toolPacTitle" class="text-base sm:text-lg font-black text-slate-900 group-hover:text-emerald-700 transition">InteresseComposto</h3>
                                <div id="toolPacHook" class="text-xs font-bold text-emerald-800 mt-0.5">Quanto varrà il tuo piano di accumulo tra 20 anni?</div>
                            </div>

                            <!-- Plain Description -->
                            <p id="toolPacDesc" class="text-xs text-slate-600 leading-relaxed">
                                Simula il potere dell'interesse composto con versamenti periodici. Calcola il montante futuro e la rendita passiva mensile sostenibile (Regola del 4% FIRE).
                            </p>

                            <!-- Feature Tags -->
                            <div class="flex flex-wrap gap-1 pt-1 text-[10px] font-bold text-slate-500">
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">📈 Effetto Valanga</span>
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">💰 Rendita 4% FIRE</span>
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">📉 Curva Interattiva</span>
                            </div>
                        </div>

                        <!-- Big Action CTA Button -->
                        <div class="pt-3 border-t border-slate-100">
                            <div class="w-full py-2 px-3 rounded-xl bg-emerald-50 group-hover:bg-emerald-700 text-emerald-900 group-hover:text-white font-bold text-xs flex items-center justify-between transition-colors shadow-2xs">
                                <span id="toolPacCta">Simula Crescita PAC</span>
                                <span class="group-hover:translate-x-1 transition-transform">➔</span>
                            </div>
                        </div>
                    </a>

                    <!-- TOOL 12: MargineFacile -->
                    <a href="/margine" class="tool-card group relative bg-white hover:bg-emerald-50/20 rounded-3xl p-5 border-2 border-slate-200/90 hover:border-emerald-600 shadow-xs hover:shadow-xl hover:-translate-y-1 transition-all duration-200 flex flex-col justify-between space-y-4" data-tags="margine profitto ricarico markup cogs prezzo vendita utile commercio pricing iva imposta gross margin retail ecommerce">
                        <div class="space-y-3">
                            <!-- Visual Header & Micro Blueprint -->
                            <div class="flex items-center justify-between">
                                <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-emerald-600 via-teal-700 to-slate-900 text-white flex items-center justify-center shadow-md shadow-emerald-700/25 p-2">
                                    <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" stroke="currentColor">
                                        <path d="M6 14 L14 6 H26 V18 L18 26 Z" fill="#047857" stroke="#34d399" stroke-width="1.5" stroke-linejoin="round"/>
                                        <circle cx="21" cy="11" r="2" fill="#ffffff"/>
                                        <line x1="12" y1="18" x2="18" y2="12" stroke="#ffffff" stroke-width="1.5"/>
                                        <circle cx="13" cy="13" r="1" fill="#ffffff"/>
                                        <circle cx="17" cy="17" r="1" fill="#ffffff"/>
                                    </svg>
                                </div>
                                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-800 border border-emerald-200" id="toolMargineBadge">Markup & Gross Margin</span>
                            </div>

                            <!-- Title & Direct Question Hook -->
                            <div>
                                <h3 id="toolMargineTitle" class="text-base sm:text-lg font-black text-slate-900 group-hover:text-emerald-700 transition">MargineFacile</h3>
                                <div id="toolMargineHook" class="text-xs font-bold text-emerald-800 mt-0.5">Stai calcolando il margine o solo il ricarico?</div>
                            </div>

                            <!-- Plain Description -->
                            <p id="toolMargineDesc" class="text-xs text-slate-600 leading-relaxed">
                                Risolvi la confusione tra margine di profitto e markup. Calcola il prezzo di vendita da costo unitario (COGS) e scorpora le aliquote IVA.
                            </p>

                            <!-- Feature Tags -->
                            <div class="flex flex-wrap gap-1 pt-1 text-[10px] font-bold text-slate-500">
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">🏷️ Margine vs Ricarico</span>
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">⚖️ Prezzo da COGS</span>
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">🏛️ Scorporo Imposte</span>
                            </div>
                        </div>

                        <!-- Big Action CTA Button -->
                        <div class="pt-3 border-t border-slate-100">
                            <div class="w-full py-2 px-3 rounded-xl bg-emerald-50 group-hover:bg-emerald-700 text-emerald-900 group-hover:text-white font-bold text-xs flex items-center justify-between transition-colors shadow-2xs">
                                <span id="toolMargineCta">Calcola Margine & Prezzo</span>
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
                <div class="flex items-center gap-1.5 flex-wrap justify-center shrink-0">
                    <button type="button" onclick="shareWhatsApp()" class="inline-flex items-center gap-1.5 px-2.5 py-1.5 bg-[#25D366] hover:bg-[#20ba59] active:scale-95 text-white text-xs font-bold rounded-xl transition shadow-xs" title="Condividi su WhatsApp">
                        <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
                        <span>WhatsApp</span>
                    </button>
                    <button type="button" onclick="shareLinkedIn()" class="inline-flex items-center gap-1.5 px-2.5 py-1.5 bg-[#0A66C2] hover:bg-[#004182] active:scale-95 text-white text-xs font-bold rounded-xl transition shadow-xs" title="Condividi su LinkedIn">
                        <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                        <span>LinkedIn</span>
                    </button>
                    <button type="button" onclick="shareReddit()" class="inline-flex items-center gap-1.5 px-2.5 py-1.5 bg-[#FF4500] hover:bg-[#e03d00] active:scale-95 text-white text-xs font-bold rounded-xl transition shadow-xs" title="Condividi su Reddit">
                        <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M12 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0zm5.01 4.744c.688 0 1.25.561 1.25 1.249a1.25 1.25 0 0 1-2.498.056l-2.597-.547-.8 3.747c1.824.07 3.48.632 4.674 1.488.308-.309.73-.491 1.207-.491.968 0 1.754.786 1.754 1.754 0 .716-.435 1.333-1.01 1.614a3.111 3.111 0 0 1 .042.52c0 2.694-3.13 4.87-7.004 4.87-3.874 0-7.004-2.176-7.004-4.87 0-.183.015-.366.043-.534A1.748 1.748 0 0 1 4.028 12c0-.968.786-1.754 1.754-1.754.463 0 .898.196 1.207.49 1.207-.883 2.878-1.43 4.744-1.487l.885-4.182a.342.342 0 0 1 .14-.197.35.35 0 0 1 .238-.042l2.906.617a1.214 1.214 0 0 1 1.108-.701zM9.25 12C8.561 12 8 12.562 8 13.25c0 .687.561 1.248 1.25 1.248.687 0 1.248-.561 1.248-1.249 0-.688-.561-1.249-1.249-1.249zm5.5 0c-.687 0-1.248.561-1.248 1.25 0 .687.561 1.248 1.249 1.248.688 0 1.249-.561 1.249-1.249 0-.687-.562-1.249-1.25-1.249zm-5.466 3.99a.327.327 0 0 0-.231.094.33.33 0 0 0 0 .463c.842.842 2.484.913 2.961.913.477 0 2.105-.056 2.961-.913a.361.361 0 0 0 .029-.463.33.33 0 0 0-.464 0c-.547.533-1.684.73-2.512.73-.828 0-1.979-.197-2.512-.73a.326.326 0 0 0-.232-.095z"/></svg>
                        <span>Reddit</span>
                    </button>
                    <button type="button" onclick="copyCurrentUrl()" class="inline-flex items-center gap-1.5 px-2.5 py-1.5 bg-slate-100 hover:bg-slate-200 active:scale-95 text-slate-700 text-xs font-bold rounded-xl border border-slate-200 transition" title="Copia Link">
                        <svg class="w-3.5 h-3.5 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"/></svg>
                        <span id="shareCopyText">Copia Link</span>
                    </button>
                    <button type="button" onclick="nativeShare()" class="inline-flex sm:hidden items-center gap-1.5 px-2.5 py-1.5 bg-blue-600 hover:bg-blue-500 active:scale-95 text-white text-xs font-bold rounded-xl transition shadow-xs" title="Altre opzioni">
                        <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M18 16.08c-.76 0-1.44.3-1.96.77L8.91 12.7c.05-.23.09-.46.09-.7s-.04-.47-.09-.7l7.05-4.11c.54.5 1.25.81 2.04.81 1.66 0 3-1.34 3-3s-1.34-3-3-3-3 1.34-3 3c0 .24.04.47.09.7L8.04 9.81C7.5 9.31 6.79 9 6 9c-1.66 0-3 1.34-3 3s1.34 3 3 3c.79 0 1.5-.31 2.04-.81l7.12 4.16c-.05.21-.08.43-.08.65 0 1.61 1.31 2.92 2.92 2.92 1.61 0 2.92-1.31 2.92-2.92s-1.31-2.92-2.92-2.92z"/></svg>
                        <span>Condividi</span>
                    </button>
                </div>
            </div>

            </section>

    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-slate-200 pt-8 pb-10 text-xs text-slate-500">
        <div class="max-w-5xl mx-auto px-4 space-y-5">
            
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

            <!-- Categorized Suite Directory -->
            <div class="bg-slate-50 border border-slate-200/80 rounded-2xl p-4 space-y-3 text-xs">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-1 pb-2 border-b border-slate-200">
                    <span class="font-extrabold text-slate-800">Indice Completo degli Strumenti (12 Tool)</span>
                    <a href="/partnership" class="font-bold text-indigo-600 hover:text-indigo-800 transition" id="navPartnerText">
                        🤝 Diventa Partner / Sponsor Ufficiale
                    </a>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-[11px]">
                    <div class="space-y-1">
                        <span class="font-bold text-amber-700 flex items-center gap-1">
                            <span>🏗️</span> OmniBuilding (3 Cantiere & Impianti)
                        </span>
                        <div class="flex flex-wrap gap-1.5 pt-0.5">
                            <a href="/rampe" class="px-2.5 py-1 bg-white hover:bg-slate-100 rounded-lg border border-slate-200 text-slate-700 font-semibold transition">RampaFacile</a>
                            <a href="/scale" class="px-2.5 py-1 bg-white hover:bg-slate-100 rounded-lg border border-slate-200 text-slate-700 font-semibold transition">ScalaFacile</a>
                            <a href="/tubi" class="px-2.5 py-1 bg-white hover:bg-slate-100 rounded-lg border border-slate-200 text-slate-700 font-semibold transition">ScaricoFacile</a>
                        </div>
                    </div>
                    <div class="space-y-1">
                        <span class="font-bold text-rose-700 flex items-center gap-1">
                            <span>🎨</span> OmniGraph (6 Grafica & Stampa)
                        </span>
                        <div class="flex flex-wrap gap-1.5 pt-0.5">
                            <a href="/dorso" class="px-2.5 py-1 bg-white hover:bg-slate-100 rounded-lg border border-slate-200 text-slate-700 font-semibold transition">DorsoFacile</a>
                            <a href="/dpi" class="px-2.5 py-1 bg-white hover:bg-slate-100 rounded-lg border border-slate-200 text-slate-700 font-semibold transition">RisoluzioneFacile</a>
                            <a href="/tinta" class="px-2.5 py-1 bg-white hover:bg-slate-100 rounded-lg border border-slate-200 text-slate-700 font-semibold transition">TintaPerfetta</a>
                            <a href="/barcode" class="px-2.5 py-1 bg-white hover:bg-slate-100 rounded-lg border border-slate-200 text-slate-700 font-semibold transition">OmniBarcode</a>
                            <a href="/copertura" class="px-2.5 py-1 bg-white hover:bg-slate-100 rounded-lg border border-slate-200 text-slate-700 font-semibold transition">CoperturaFacile</a>
                            <a href="/resa" class="px-2.5 py-1 bg-white hover:bg-slate-100 rounded-lg border border-slate-200 text-slate-700 font-semibold transition">ResaCarta</a>
                        </div>
                    </div>
                    <div class="space-y-1">
                        <span class="font-bold text-emerald-700 flex items-center gap-1">
                            <span>💼</span> OmniFinance (3 Finanza & Business)
                        </span>
                        <div class="flex flex-wrap gap-1.5 pt-0.5">
                            <a href="/mutuo" class="px-2.5 py-1 bg-white hover:bg-slate-100 rounded-lg border border-slate-200 text-slate-700 font-semibold transition">MutuoFacile</a>
                            <a href="/pac" class="px-2.5 py-1 bg-white hover:bg-slate-100 rounded-lg border border-slate-200 text-slate-700 font-semibold transition">InteresseComposto</a>
                            <a href="/margine" class="px-2.5 py-1 bg-white hover:bg-slate-100 rounded-lg border border-slate-200 text-slate-700 font-semibold transition">MargineFacile</a>
                        </div>
                    </div>
                </div>

                <!-- Desk Utilities Strip -->
                <div class="pt-2 border-t border-slate-200 flex flex-wrap items-center justify-between gap-2 text-[11px]">
                    <span class="font-bold text-slate-700 flex items-center gap-1.5">
                        <span>⚡</span> <strong>OmniDesk — Utilità Rapide & Widget:</strong>
                    </span>
                    <div class="flex flex-wrap items-center gap-1.5">
                        <a href="/memo" class="px-2 py-0.5 bg-amber-50 hover:bg-amber-100 text-amber-800 rounded-md border border-amber-200 font-bold transition">📝 OmniMemo (Post-it)</a>
                        <a href="/calcolatrice" class="px-2 py-0.5 bg-blue-50 hover:bg-blue-100 text-blue-800 rounded-md border border-blue-200 font-bold transition">🔢 OmniCalc (Calcolatrice)</a>
                        <a href="/orologio" class="px-2 py-0.5 bg-teal-50 hover:bg-teal-100 text-teal-800 rounded-md border border-teal-200 font-bold transition">⏱️ OmniClock (Pop Swatch)</a>
                    </div>
                </div>
            </div>
            </div>

            <!-- Disclaimer and Rights -->
            <div class="text-center space-y-1.5">
                <p id="rightsText" class="font-bold text-slate-600">© 2026 OmniTools Lab — Precision Utilities Suite. Tutti i diritti riservati.</p>
                <p id="legalDisclaimerText" class="text-[10px] text-slate-500 leading-relaxed max-w-2xl mx-auto">
                    <strong>Note Legali e Manleva:</strong> Gli strumenti della suite OmniTools Lab hanno finalità orientativa, didattica e di verifica preliminare. I calcoli tecnici (edilizia, grafica) e finanziari non sostituiscono il calcolo esecutivo, l'asseverazione di un tecnico abilitato né costituiscono consulenza finanziaria personalizzata (TUF / D.Lgs. 58/1998).
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
            if (t.division_building_title) document.getElementById('divBuildingTitle').innerHTML = 'Omni<span class="text-amber-600">Building</span>';
            if (t.division_building_desc) document.getElementById('divBuildingDesc').textContent = t.division_building_desc;
            if (t.division_graph_title) document.getElementById('divGraphTitle').innerHTML = 'Omni<span class="text-rose-700">Graph</span>';
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

            // Tool 7: Barcode
            if (t.tool_barcode_title) document.getElementById('toolBarcodeTitle').textContent = t.tool_barcode_title;
            if (t.tool_barcode_hook) document.getElementById('toolBarcodeHook').textContent = t.tool_barcode_hook;
            if (t.tool_barcode_desc) document.getElementById('toolBarcodeDesc').textContent = t.tool_barcode_desc;
            if (t.tool_barcode_cta) document.getElementById('toolBarcodeCta').textContent = t.tool_barcode_cta;
            if (t.tool_barcode_badge) document.getElementById('toolBarcodeBadge').textContent = t.tool_barcode_badge;

            // Tool 8: Copertura
            if (t.tool_copertura_title) document.getElementById('toolCoperturaTitle').textContent = t.tool_copertura_title;
            if (t.tool_copertura_hook) document.getElementById('toolCoperturaHook').textContent = t.tool_copertura_hook;
            if (t.tool_copertura_desc) document.getElementById('toolCoperturaDesc').textContent = t.tool_copertura_desc;
            if (t.tool_copertura_cta) document.getElementById('toolCoperturaCta').textContent = t.tool_copertura_cta;
            if (t.tool_copertura_badge) document.getElementById('toolCoperturaBadge').textContent = t.tool_copertura_badge;

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

                // Filter / Search Management (Tabbed Hub - Proposta 1)
        function setFilter(filter, updateHash = true) {{
            currentFilter = filter;
            if (updateHash) {{
                try {{
                    if (filter === 'all') {{
                        history.replaceState(null, null, window.location.pathname + window.location.search);
                    }} else {{
                        history.replaceState(null, null, '#' + filter);
                    }}
                }} catch (e) {{
                    // Ignored on file:// or strict origins
                }}
            }}

            const btnAll = document.getElementById('filterAllBtn');
            const btnBuilding = document.getElementById('filterBuildingBtn');
            const btnGraph = document.getElementById('filterGraphBtn');
            const btnFinance = document.getElementById('filterFinanceBtn');

            // Base inactive classes (fixed dimensions, larger inner content)
            const baseInactive = "flex flex-col sm:flex-row items-center justify-center gap-1.5 sm:gap-2.5 py-2 sm:py-2.5 px-2 sm:px-3 rounded-xl sm:rounded-2xl bg-white hover:bg-slate-50 text-slate-700 border border-slate-200/80 font-bold transition-all duration-200 active:scale-95 cursor-pointer";

            if (btnAll) {{
                btnAll.className = filter === 'all' 
                    ? "flex flex-col sm:flex-row items-center justify-center gap-1.5 sm:gap-2.5 py-2 sm:py-2.5 px-2 sm:px-3 rounded-xl sm:rounded-2xl bg-blue-600 text-white shadow-md shadow-blue-600/25 font-bold transition-all duration-200 active:scale-95 cursor-pointer"
                    : baseInactive;
                const subAll = btnAll.querySelector('.subtext');
                if (subAll) subAll.className = filter === 'all' ? "subtext text-[10px] sm:text-[11px] text-blue-100 font-semibold hidden sm:block" : "subtext text-[10px] sm:text-[11px] text-slate-500 font-semibold hidden sm:block";
            }}

            if (btnBuilding) {{
                btnBuilding.className = filter === 'building'
                    ? "flex flex-col sm:flex-row items-center justify-center gap-1.5 sm:gap-2.5 py-2 sm:py-2.5 px-2 sm:px-3 rounded-xl sm:rounded-2xl bg-amber-600 text-white shadow-md shadow-amber-600/30 border-amber-600 font-bold transition-all duration-200 active:scale-95 cursor-pointer"
                    : baseInactive;
                const subB = btnBuilding.querySelector('.subtext');
                if (subB) subB.className = filter === 'building' ? "subtext text-[10px] sm:text-[11px] text-amber-100 font-semibold hidden sm:block" : "subtext text-[10px] sm:text-[11px] text-slate-500 font-semibold hidden sm:block";
            }}

            if (btnGraph) {{
                btnGraph.className = filter === 'graph'
                    ? "flex flex-col sm:flex-row items-center justify-center gap-1.5 sm:gap-2.5 py-2 sm:py-2.5 px-2 sm:px-3 rounded-xl sm:rounded-2xl bg-rose-900 text-white shadow-md shadow-rose-900/30 border-rose-900 font-bold transition-all duration-200 active:scale-95 cursor-pointer"
                    : baseInactive;
                const subG = btnGraph.querySelector('.subtext');
                if (subG) subG.className = filter === 'graph' ? "subtext text-[10px] sm:text-[11px] text-rose-200 font-semibold hidden sm:block" : "subtext text-[10px] sm:text-[11px] text-slate-500 font-semibold hidden sm:block";
            }}

            if (btnFinance) {{
                btnFinance.className = filter === 'finance'
                    ? "flex flex-col sm:flex-row items-center justify-center gap-1.5 sm:gap-2.5 py-2 sm:py-2.5 px-2 sm:px-3 rounded-xl sm:rounded-2xl bg-emerald-700 text-white shadow-md shadow-emerald-700/30 border-emerald-700 font-bold transition-all duration-200 active:scale-95 cursor-pointer"
                    : baseInactive;
                const subF = btnFinance.querySelector('.subtext');
                if (subF) subF.className = filter === 'finance' ? "subtext text-[10px] sm:text-[11px] text-emerald-100 font-semibold hidden sm:block" : "subtext text-[10px] sm:text-[11px] text-slate-500 font-semibold hidden sm:block";
            }}

            filterTools();
        }}

        function initFilterFromHash() {{
            const hash = (window.location.hash || '').replace('#', '').toLowerCase();
            if (hash === 'building' || hash === 'graph' || hash === 'finance' || hash === 'all') {{
                setFilter(hash, false);
            }} else {{
                setFilter('all', false);
            }}
        }}

        window.addEventListener('hashchange', () => {{
            initFilterFromHash();
        }});

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
            const secFinance = document.getElementById('sectionFinance');

            let visibleBuildingCards = 0;
            let visibleGraphCards = 0;
            let visibleFinanceCards = 0;

            const cards = document.querySelectorAll('.tool-card');
            cards.forEach(card => {{
                const isBuildingCard = card.closest('#sectionBuilding') !== null;
                const isGraphCard = card.closest('#sectionGraph') !== null;
                const isFinanceCard = card.closest('#sectionFinance') !== null;

                // Check division filter
                let allowedByDivision = true;
                if (currentFilter === 'building' && !isBuildingCard) allowedByDivision = false;
                if (currentFilter === 'graph' && !isGraphCard) allowedByDivision = false;
                if (currentFilter === 'finance' && !isFinanceCard) allowedByDivision = false;

                // Check search query
                const text = card.textContent.toLowerCase();
                const tags = (card.getAttribute('data-tags') || '').toLowerCase();
                const matchQuery = query === '' || text.includes(query) || tags.includes(query);

                if (allowedByDivision && matchQuery) {{
                    card.classList.remove('hidden');
                    if (isBuildingCard) visibleBuildingCards++;
                    if (isGraphCard) visibleGraphCards++;
                    if (isFinanceCard) visibleFinanceCards++;
                }} else {{
                    card.classList.add('hidden');
                }}
            }});

            // Show or hide division containers based on visible cards
            if (secBuilding) {{
                if (visibleBuildingCards > 0 && (currentFilter === 'all' || currentFilter === 'building')) {{
                    secBuilding.classList.remove('hidden');
                }} else {{
                    secBuilding.classList.add('hidden');
                }}
            }}

            if (secGraph) {{
                if (visibleGraphCards > 0 && (currentFilter === 'all' || currentFilter === 'graph')) {{
                    secGraph.classList.remove('hidden');
                }} else {{
                    secGraph.classList.add('hidden');
                }}
            }}

            if (secFinance) {{
                if (visibleFinanceCards > 0 && (currentFilter === 'all' || currentFilter === 'finance')) {{
                    secFinance.classList.remove('hidden');
                }} else {{
                    secFinance.classList.add('hidden');
                }}
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
            window.open('https://www.linkedin.com/sharing/share-offsite/?url=' + url, '_blank');
        }}

                function shareReddit() {{
            const url = encodeURIComponent(window.location.href);
            const title = encodeURIComponent(document.title);
            window.open('https://reddit.com/submit?url=' + url + '&title=' + title, '_blank');
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
            initFilterFromHash();
            // Load OmniDesk Dock
            const deskScript = document.createElement('script');
            deskScript.src = '/desk_dock.js';
            deskScript.defer = true;
            document.body.appendChild(deskScript);
        }});
    </script>
</body>
</html>
"""

with open(os.path.join(cur_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html_code)

print('index.html compiled successfully from build_hub_i18n.py.')
