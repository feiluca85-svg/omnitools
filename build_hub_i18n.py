import json

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/translations_hub.json', 'r', encoding='utf-8') as f:
    t_data = json.load(f)

t_json_str = json.dumps(t_data, ensure_ascii=False)

html_code = f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>OmniTools Lab — Suite Professionale di Calcolatori & Utility di Precisione</title>
    <meta name="description" content="OmniTools Lab: La suite gratuita e senza registrazione di calcolatori tecnici per cantiere, architettura, grafica e prestampa. 100% offline e conforme alle normative.">
    
    <!-- Canonical & SEO Meta Tags -->
    <link rel="canonical" href="https://www.omnitoolslab.com/">
    <meta name="robots" content="index, follow">
    <meta property="og:type" content="website">
    <meta property="og:title" content="OmniTools Lab — Suite Professionale di Calcolatori & Utility">
    <meta property="og:description" content="Precisione millimetrica per cantiere, grafica e ingegneria. Strumenti gratuiti, senza registrazione, funzionanti offline.">
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
    <style>
        .hero-pattern {{
            background-color: #0b1329;
            background-image: 
                radial-gradient(circle at 50% 0%, rgba(37, 99, 235, 0.28) 0%, transparent 60%),
                linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
            background-size: 100% 100%, 40px 40px, 40px 40px;
        }}
    </style>
</head>
<body class="bg-slate-900 text-slate-100 font-sans antialiased min-h-screen flex flex-col justify-between selection:bg-blue-500 selection:text-white">

    <!-- Top Navigation Header -->
    <header class="bg-slate-900/90 border-b border-slate-800 sticky top-0 z-40 backdrop-blur-md" style="padding-top: max(env(safe-area-inset-top), 8px); padding-bottom: 8px;">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 py-1 flex items-center justify-between gap-3">
            
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
                        <span class="font-jakarta font-black text-base sm:text-lg text-white tracking-tight leading-none">Omni<span class="text-blue-500">Tools</span></span>
                        <span class="text-[9px] font-jakarta font-extrabold uppercase bg-blue-500/20 text-blue-400 px-1.5 py-0.5 rounded-full border border-blue-500/30">Lab</span>
                    </div>
                    <span id="taglineText" class="text-[10px] text-slate-400 font-medium hidden sm:inline leading-tight mt-0.5">Suite di Calcolo Tecnico ad Alta Precisione</span>
                </div>
            </a>

            <!-- Right Controls: Language Selector + App Install -->
            <div class="flex items-center gap-2 shrink-0">
                <div class="relative inline-block text-left">
                    <select id="langSelect" onchange="changeLanguage(this.value)" class="bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold py-1.5 px-2 rounded-xl border border-slate-700 focus:outline-none cursor-pointer transition">
                        <option value="it">🇮🇹 IT</option>
                        <option value="en">🇬🇧 EN</option>
                        <option value="es">🇪🇸 ES</option>
                        <option value="fr">🇫🇷 FR</option>
                        <option value="de">🇩🇪 DE</option>
                        <option value="pt">🇵🇹 PT</option>
                    </select>
                </div>

                <button onclick="triggerInstall()" id="headerInstallBtn" class="inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-bold text-white bg-blue-600 hover:bg-blue-500 active:scale-95 rounded-xl shadow-xs transition">
                    <span>📲</span>
                    <span id="headerInstallText" class="hidden sm:inline">Installa App</span>
                </button>
            </div>
        </div>
    </header>

    <!-- Main Content Area -->
    <main class="flex-1 space-y-8 sm:space-y-12">
        
        <!-- Hero Section with Central Search -->
        <section class="hero-pattern border-b border-slate-800/80 pt-10 sm:pt-16 pb-12 sm:pb-16 px-4 sm:px-6">
            <div class="max-w-4xl mx-auto text-center space-y-4 sm:space-y-5">
                
                <!-- Pill Badge -->
                <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/10 border border-blue-500/30 text-blue-400 text-xs font-bold">
                    <span id="heroBadge">⚡ Gratuito • Zero Registrazione • Funziona Offline</span>
                </div>

                <!-- Main Punchy Title -->
                <h1 id="heroTitle" class="text-2xl sm:text-4xl lg:text-5xl font-black text-white tracking-tight leading-tight">
                    Tutti gli strumenti di calcolo tecnico, a portata di click.
                </h1>

                <!-- Subtitle -->
                <p id="heroSubtitle" class="text-sm sm:text-base text-slate-300 max-w-2xl mx-auto leading-relaxed">
                    Precisione millimetrica per cantiere, grafica, editoria e ingegneria. Calcola, verifica le normative e genera schede tecniche di livello professionale.
                </p>

                <!-- Instant Search Bar -->
                <div class="pt-2 sm:pt-4 max-w-xl mx-auto">
                    <div class="relative">
                        <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none text-slate-400">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                            </svg>
                        </div>
                        <input type="text" id="searchInput" oninput="filterTools()" placeholder="Cerca uno strumento (es. pendenza, rampa, scala, gradini, dorso libro, dpi, pixel)..." class="w-full bg-slate-800/90 hover:bg-slate-800 focus:bg-slate-800 border border-slate-700 focus:border-blue-500 rounded-2xl pl-12 pr-4 py-3 sm:py-3.5 text-sm sm:text-base text-white placeholder-slate-400 outline-none shadow-xl transition">
                        <button type="button" id="clearSearchBtn" onclick="clearSearch()" class="hidden absolute inset-y-0 right-0 pr-4 flex items-center text-slate-400 hover:text-white">
                            ✕
                        </button>
                    </div>

                    <!-- Category Filter Pills -->
                    <div class="flex items-center justify-center gap-1.5 sm:gap-2 pt-3 flex-wrap text-xs font-bold">
                        <button type="button" onclick="setFilter('all')" id="filterAllBtn" class="px-3 py-1.5 rounded-xl bg-blue-600 text-white shadow-xs transition">
                            Tutti i Tool
                        </button>
                        <button type="button" onclick="setFilter('building')" id="filterBuildingBtn" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 transition">
                            🏗️ OmniBuilding
                        </button>
                        <button type="button" onclick="setFilter('graph')" id="filterGraphBtn" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 transition">
                            🎨 OmniGraph
                        </button>
                    </div>
                </div>

            </div>
        </section>

        <!-- Tools Showcase Grid -->
        <section class="max-w-6xl mx-auto px-4 sm:px-6 space-y-10">
            
            <!-- SECTION 1: OmniBuilding -->
            <div id="sectionBuilding" class="space-y-4">
                <div class="flex items-center justify-between pb-2 border-b border-slate-800">
                    <div class="flex items-center gap-2">
                        <div class="w-7 h-7 rounded-lg bg-blue-500/20 text-blue-400 flex items-center justify-center text-sm font-bold border border-blue-500/30">
                            🏗️
                        </div>
                        <div>
                            <h2 id="divBuildingTitle" class="text-base sm:text-lg font-black text-white tracking-tight">OmniBuilding — Edilizia & Progettazione</h2>
                            <p id="divBuildingDesc" class="text-xs text-slate-400">Soluzioni matematiche e normative per cantieri, architetti, ingegneri e artigiani.</p>
                        </div>
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    
                    <!-- Tool Card 1: RampaFacile -->
                    <a href="/rampe" class="tool-card group p-5 rounded-2xl bg-slate-800/80 hover:bg-slate-800 border border-slate-700/80 hover:border-blue-500/50 shadow-lg transition-all duration-200 flex flex-col justify-between space-y-4 hover:-translate-y-0.5" data-tags="rampa rampe pendenza pendenze dislivello disabili dm 236 garage handicap accessibilita">
                        <div class="space-y-2.5">
                            <div class="flex items-center justify-between">
                                <div class="flex items-center gap-2.5">
                                    <div class="w-10 h-10 rounded-xl bg-blue-600/20 text-blue-400 flex items-center justify-center text-xl font-bold border border-blue-500/30 group-hover:bg-blue-600 group-hover:text-white transition">
                                        📐
                                    </div>
                                    <div>
                                        <h3 id="toolRampeTitle" class="text-base font-black text-white group-hover:text-blue-400 transition">RampaFacile</h3>
                                        <span id="toolRampeBadge" class="text-[10px] font-bold text-blue-400 bg-blue-500/10 px-2 py-0.5 rounded-md border border-blue-500/20">DM 236/89 & ADA</span>
                                    </div>
                                </div>
                                <span class="text-xs font-bold text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded-full border border-emerald-500/30">Attivo</span>
                            </div>
                            <p id="toolRampeDesc" class="text-xs sm:text-sm text-slate-300 leading-relaxed">
                                Calcolo pendenza percentuale, gradi e ingombro a terra di rampe con verifica conformità per disabili e veicoli.
                            </p>
                        </div>

                        <div class="flex items-center justify-between pt-3 border-t border-slate-700/60 text-xs">
                            <span class="text-slate-400 font-mono text-[11px]">📏 Pendenza • Gradi • Spazio a terra</span>
                            <span class="font-bold text-blue-400 group-hover:translate-x-1 transition inline-flex items-center gap-1">
                                <span>Apri</span> <span>→</span>
                            </span>
                        </div>
                    </a>

                    <!-- Tool Card 2: ScalaFacile -->
                    <a href="/scale" class="tool-card group p-5 rounded-2xl bg-slate-800/80 hover:bg-slate-800 border border-slate-700/80 hover:border-indigo-500/50 shadow-lg transition-all duration-200 flex flex-col justify-between space-y-4 hover:-translate-y-0.5" data-tags="scala scale gradini gradino alzata pedata blondel dislivello scale interne din 18065">
                        <div class="space-y-2.5">
                            <div class="flex items-center justify-between">
                                <div class="flex items-center gap-2.5">
                                    <div class="w-10 h-10 rounded-xl bg-indigo-600/20 text-indigo-400 flex items-center justify-center text-xl font-bold border border-indigo-500/30 group-hover:bg-indigo-600 group-hover:text-white transition">
                                        🪜
                                    </div>
                                    <div>
                                        <h3 id="toolScaleTitle" class="text-base font-black text-white group-hover:text-indigo-400 transition">ScalaFacile</h3>
                                        <span id="toolScaleBadge" class="text-[10px] font-bold text-indigo-400 bg-indigo-500/10 px-2 py-0.5 rounded-md border border-indigo-500/20">Legge di Blondel</span>
                                    </div>
                                </div>
                                <span class="text-xs font-bold text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded-full border border-emerald-500/30">Attivo</span>
                            </div>
                            <p id="toolScaleDesc" class="text-xs sm:text-sm text-slate-300 leading-relaxed">
                                Dimensionamento ergonomico del numero di gradini, altezza alzata e pedata secondo la formula di Blondel 2a + p.
                            </p>
                        </div>

                        <div class="flex items-center justify-between pt-3 border-t border-slate-700/60 text-xs">
                            <span class="text-slate-400 font-mono text-[11px]">🪜 Gradini • Alzata • Pedata (2a + p)</span>
                            <span class="font-bold text-indigo-400 group-hover:translate-x-1 transition inline-flex items-center gap-1">
                                <span>Apri</span> <span>→</span>
                            </span>
                        </div>
                    </a>

                </div>
            </div>

            <!-- SECTION 2: OmniGraph -->
            <div id="sectionGraph" class="space-y-4">
                <div class="flex items-center justify-between pb-2 border-b border-slate-800">
                    <div class="flex items-center gap-2">
                        <div class="w-7 h-7 rounded-lg bg-purple-500/20 text-purple-400 flex items-center justify-center text-sm font-bold border border-purple-500/30">
                            🎨
                        </div>
                        <div>
                            <h2 id="divGraphTitle" class="text-base sm:text-lg font-black text-white tracking-tight">OmniGraph — Grafica & Tipografia</h2>
                            <p id="divGraphDesc" class="text-xs text-slate-400">Utility di prestampa e conversione geometrico-ottica per grafici, editori e tipografi.</p>
                        </div>
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    
                    <!-- Tool Card 3: DorsoFacile -->
                    <a href="/dorso" class="tool-card group p-5 rounded-2xl bg-slate-800/80 hover:bg-slate-800 border border-slate-700/80 hover:border-purple-500/50 shadow-lg transition-all duration-200 flex flex-col justify-between space-y-4 hover:-translate-y-0.5" data-tags="dorso libro brossura copertina refili indesign kdp amazon pagine grammatura mano carta fustella">
                        <div class="space-y-2.5">
                            <div class="flex items-center justify-between">
                                <div class="flex items-center gap-2.5">
                                    <div class="w-10 h-10 rounded-xl bg-purple-600/20 text-purple-400 flex items-center justify-center text-xl font-bold border border-purple-500/30 group-hover:bg-purple-600 group-hover:text-white transition">
                                        🎨
                                    </div>
                                    <div>
                                        <h3 id="toolDorsoTitle" class="text-base font-black text-white group-hover:text-purple-400 transition">DorsoFacile</h3>
                                        <span id="toolDorsoBadge" class="text-[10px] font-bold text-purple-400 bg-purple-500/10 px-2 py-0.5 rounded-md border border-purple-500/20">Copertina Stesa & Refili</span>
                                    </div>
                                </div>
                                <span class="text-xs font-bold text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded-full border border-emerald-500/30">Attivo</span>
                            </div>
                            <p id="toolDorsoDesc" class="text-xs sm:text-sm text-slate-300 leading-relaxed">
                                Spessore esatto del dorso libro in base a pagine, grammatura e mano della carta con quote InDesign e KDP.
                            </p>
                        </div>

                        <div class="flex items-center justify-between pt-3 border-t border-slate-700/60 text-xs">
                            <span class="text-slate-400 font-mono text-[11px]">📖 Pagine • Mano carta • Refilo 3 mm</span>
                            <span class="font-bold text-purple-400 group-hover:translate-x-1 transition inline-flex items-center gap-1">
                                <span>Apri</span> <span>→</span>
                            </span>
                        </div>
                    </a>

                    <!-- Tool Card 4: RisoluzioneFacile -->
                    <a href="/dpi" class="tool-card group p-5 rounded-2xl bg-slate-800/80 hover:bg-slate-800 border border-slate-700/80 hover:border-emerald-500/50 shadow-lg transition-all duration-200 flex flex-col justify-between space-y-4 hover:-translate-y-0.5" data-tags="dpi ppi pixel pixelatura risoluzione stampa formato grande formato poster manifesto offset distanza occhio photoshop">
                        <div class="space-y-2.5">
                            <div class="flex items-center justify-between">
                                <div class="flex items-center gap-2.5">
                                    <div class="w-10 h-10 rounded-xl bg-emerald-600/20 text-emerald-400 flex items-center justify-center text-xl font-bold border border-emerald-500/30 group-hover:bg-emerald-600 group-hover:text-white transition">
                                        🖼️
                                    </div>
                                    <div>
                                        <h3 id="toolDpiTitle" class="text-base font-black text-white group-hover:text-emerald-400 transition">RisoluzioneFacile</h3>
                                        <span id="toolDpiBadge" class="text-[10px] font-bold text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded-md border border-emerald-500/20">Pixel, cm & Acuità Ottica</span>
                                    </div>
                                </div>
                                <span class="text-xs font-bold text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded-full border border-emerald-500/30">Attivo</span>
                            </div>
                            <p id="toolDpiDesc" class="text-xs sm:text-sm text-slate-300 leading-relaxed">
                                Conversione istantanea Pixel ↔ Centimetri ↔ DPI per offset, digitale e grande formato con distanza dell'occhio.
                            </p>
                        </div>

                        <div class="flex items-center justify-between pt-3 border-t border-slate-700/60 text-xs">
                            <span class="text-slate-400 font-mono text-[11px]">🖼️ Pixel ↔ cm ↔ DPI • Occhio Umano</span>
                            <span class="font-bold text-emerald-400 group-hover:translate-x-1 transition inline-flex items-center gap-1">
                                <span>Apri</span> <span>→</span>
                            </span>
                        </div>
                    </a>

                </div>
            </div>

            <!-- SECTION 3: Roadmap (Coming Soon) -->
            <div id="sectionRoadmap" class="pt-4 border-t border-slate-800 space-y-4">
                <div class="flex items-center justify-between">
                    <span id="roadmapTitle" class="text-xs font-bold uppercase tracking-wider text-slate-400">Prossimi Moduli in Arrivo:</span>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
                    <div class="p-4 rounded-xl bg-slate-800/40 border border-slate-800 opacity-80 flex flex-col justify-between space-y-2">
                        <div class="space-y-1">
                            <div class="flex items-center justify-between">
                                <span id="toolScarichiTitle" class="font-bold text-slate-300">💧 ScaricoFacile</span>
                                <span class="text-[9px] px-1.5 py-0.2 bg-amber-500/20 text-amber-300 font-bold rounded">In sviluppo</span>
                            </div>
                            <p id="toolScarichiDesc" class="text-[11px] text-slate-400 leading-snug">Pendenza tubazioni fognarie e reflue con diametri commerciali.</p>
                        </div>
                        <span class="text-[10px] text-blue-400 font-medium">OmniBuilding</span>
                    </div>

                    <div class="p-4 rounded-xl bg-slate-800/40 border border-slate-800 opacity-80 flex flex-col justify-between space-y-2">
                        <div class="space-y-1">
                            <div class="flex items-center justify-between">
                                <span id="toolCalceTitle" class="font-bold text-slate-300">🧱 CalceFacile</span>
                                <span class="text-[9px] px-1.5 py-0.2 bg-amber-500/20 text-amber-300 font-bold rounded">In sviluppo</span>
                            </div>
                            <p id="toolCalceDesc" class="text-[11px] text-slate-400 leading-snug">Dosaggio sacchi cemento, sabbia e acqua per mc di massetto.</p>
                        </div>
                        <span class="text-[10px] text-blue-400 font-medium">OmniBuilding</span>
                    </div>

                    <div class="p-4 rounded-xl bg-slate-800/40 border border-slate-800 opacity-80 flex flex-col justify-between space-y-2">
                        <div class="space-y-1">
                            <div class="flex items-center justify-between">
                                <span id="toolResaTitle" class="font-bold text-slate-300">📄 ResaCarta</span>
                                <span class="text-[9px] px-1.5 py-0.2 bg-amber-500/20 text-amber-300 font-bold rounded">In sviluppo</span>
                            </div>
                            <p id="toolResaDesc" class="text-[11px] text-slate-400 leading-snug">Calcolo tagli ottimali su foglio macchina e scarto carta.</p>
                        </div>
                        <span class="text-[10px] text-purple-400 font-medium">OmniGraph</span>
                    </div>
                </div>
            </div>

            <!-- Features / Value Pillars Grid -->
            <div class="grid grid-cols-2 lg:grid-cols-4 gap-3 pt-6 border-t border-slate-800 text-left">
                <div class="p-4 rounded-2xl bg-slate-800/40 border border-slate-800/80 space-y-1.5">
                    <span class="text-xl">⚡</span>
                    <h3 id="feat1Title" class="text-xs sm:text-sm font-bold text-white">Nessuna Registrazione</h3>
                    <p id="feat1Desc" class="text-[11px] text-slate-400 leading-snug">Accedi e calcoli all'istante, senza account o abbonamenti.</p>
                </div>
                <div class="p-4 rounded-2xl bg-slate-800/40 border border-slate-800/80 space-y-1.5">
                    <span class="text-xl">📐</span>
                    <h3 id="feat2Title" class="text-xs sm:text-sm font-bold text-white">Precisione Normativa</h3>
                    <p id="feat2Desc" class="text-[11px] text-slate-400 leading-snug">Formule rigorose allineate a standard tecnici italiani ed esteri.</p>
                </div>
                <div class="p-4 rounded-2xl bg-slate-800/40 border border-slate-800/80 space-y-1.5">
                    <span class="text-xl">📱</span>
                    <h3 id="feat3Title" class="text-xs sm:text-sm font-bold text-white">Funziona Offline</h3>
                    <p id="feat3Desc" class="text-[11px] text-slate-400 leading-snug">PWA installabile su smartphone per lavorare anche in cantiere senza rete.</p>
                </div>
                <div class="p-4 rounded-2xl bg-slate-800/40 border border-slate-800/80 space-y-1.5">
                    <span class="text-xl">📄</span>
                    <h3 id="feat4Title" class="text-xs sm:text-sm font-bold text-white">Schede Tecniche A4</h3>
                    <p id="feat4Desc" class="text-[11px] text-slate-400 leading-snug">Stampa o esporta relazioni tecniche pulite pronte da allegare al fascicolo.</p>
                </div>
            </div>

        </section>

    </main>

    <!-- Footer -->
    <footer class="bg-slate-950 border-t border-slate-800/80 pt-10 pb-12 mt-12 text-xs text-slate-500">
        <div class="max-w-5xl mx-auto px-4 space-y-6">
            
            <!-- Share & Viral Action Strip (Dark Mode) -->
            <div class="bg-slate-900 p-4 rounded-2xl border border-slate-800 shadow-md flex flex-col sm:flex-row items-center justify-between gap-3 text-center sm:text-left">
                <div class="flex items-center gap-2.5">
                    <span class="text-xl">📢</span>
                    <div>
                        <span class="text-xs sm:text-sm font-bold text-white block">Condividi la Suite OmniTools Lab</span>
                        <span class="text-[11px] text-slate-400 block">Fai conoscere questi strumenti gratuiti ai tuoi colleghi e contatti</span>
                    </div>
                </div>
                <div class="flex items-center gap-1.5 flex-wrap justify-center shrink-0">
                    <button type="button" onclick="shareWhatsApp()" class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-emerald-600 hover:bg-emerald-500 active:scale-95 text-white text-xs font-bold rounded-xl transition shadow-xs" title="Condividi su WhatsApp">
                        <span>💬</span> <span>WhatsApp</span>
                    </button>
                    <button type="button" onclick="shareLinkedIn()" class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-[#0a66c2] hover:bg-[#004182] active:scale-95 text-white text-xs font-bold rounded-xl transition shadow-xs" title="Condividi su LinkedIn">
                        <span>💼</span> <span>LinkedIn</span>
                    </button>
                    <button type="button" onclick="copyCurrentUrl()" class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-slate-800 hover:bg-slate-700 active:scale-95 text-slate-200 text-xs font-bold rounded-xl border border-slate-700 transition" title="Copia Link">
                        <span>🔗</span> <span id="shareCopyText">Copia Link</span>
                    </button>
                    <button type="button" onclick="nativeShare()" class="inline-flex sm:hidden items-center gap-1.5 px-3 py-1.5 bg-blue-600 hover:bg-blue-500 active:scale-95 text-white text-xs font-bold rounded-xl transition shadow-xs" title="Altre opzioni di condivisione">
                        <span>📤</span> <span>Condividi</span>
                    </button>
                </div>
            </div>

            <!-- Suggestion Bar -->
            <div class="bg-gradient-to-r from-blue-900/30 to-indigo-900/30 border border-blue-500/20 rounded-2xl p-4 flex flex-col sm:flex-row items-center justify-between gap-3 text-center sm:text-left">
                <div class="flex items-center gap-2.5">
                    <span class="text-xl">💡</span>
                    <span id="suggestBannerText" class="text-xs sm:text-sm font-bold text-slate-200">
                        Hai un'idea per un nuovo calcolatore tecnico?
                    </span>
                </div>
                <button type="button" onclick="openSuggestModal()" class="px-4 py-2 bg-blue-600 hover:bg-blue-500 active:scale-95 text-white font-bold text-xs rounded-xl shadow-xs transition">
                    <span id="suggestBtnText">Suggerisci Tool</span>
                </button>
            </div>

            <!-- Disclaimer and Rights -->
            <div class="text-center space-y-2">
                <p id="rightsText" class="font-bold text-slate-400">© 2026 OmniTools Lab — Precision Utilities Suite. Tutti i diritti riservati.</p>
                <p id="legalDisclaimerText" class="text-[10px] text-slate-500 leading-relaxed max-w-3xl mx-auto">
                    <strong>Note Legali e Manleva:</strong> Gli strumenti della suite OmniTools Lab sono concepiti a scopo didattico, orientativo e di verifica preliminare. Non sostituiscono il calcolo esecutivo, l'asseverazione o il progetto firmato da un tecnico abilitato (ingegnere, architetto, geometra o perito).
                </p>
            </div>
        </div>
    </footer>

    <!-- Floating PWA Install Banner -->
    <div id="installBanner" class="fixed bottom-3 left-3 right-3 sm:left-auto sm:right-6 sm:bottom-6 sm:max-w-sm bg-slate-800 text-white p-3.5 rounded-2xl shadow-2xl border border-slate-700 z-50 flex items-center justify-between gap-3 transition-all duration-300">
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
    <div id="suggestModal" class="fixed inset-0 bg-slate-950/70 backdrop-blur-xs z-50 hidden flex items-center justify-center p-4">
        <div class="bg-slate-900 rounded-3xl max-w-md w-full p-5 sm:p-6 shadow-2xl border border-slate-700 space-y-4">
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-2">
                    <span class="text-xl">💡</span>
                    <h3 class="text-sm sm:text-base font-bold text-white">Suggerisci uno Strumento</h3>
                </div>
                <button onclick="closeSuggestModal()" class="text-slate-400 hover:text-white p-1 rounded-lg">✕</button>
            </div>
            <p class="text-xs text-slate-300">
                Quale calcolatore tecnico o funzione vorresti vedere su OmniTools Lab?
            </p>
            <textarea id="suggestIdeaInput" rows="3" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-3 text-xs text-white placeholder-slate-500 focus:bg-slate-800 focus:border-blue-500 outline-none transition" placeholder="Es. Calcolo peso putrelle in acciaio, scarichi acque meteoriche, etc."></textarea>
            <div class="flex items-center justify-between pt-1">
                <span class="text-[10px] text-slate-500">🔒 Invio 100% anonimo</span>
                <button type="button" onclick="sendSuggestion()" id="suggestSendBtn" class="px-4 py-2 bg-blue-600 hover:bg-blue-500 text-white text-xs font-bold rounded-xl transition shadow-xs">
                    Invia Suggerimento
                </button>
            </div>
            <div id="suggestFeedback" class="hidden text-xs font-bold text-emerald-400 bg-emerald-500/10 p-2.5 rounded-xl border border-emerald-500/20 text-center">
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
            document.getElementById('toolDorsoTitle').textContent = t.tool_dorso_title;
            document.getElementById('toolDorsoBadge').textContent = t.tool_dorso_badge;
            document.getElementById('toolDorsoDesc').textContent = t.tool_dorso_desc;
            document.getElementById('toolDpiTitle').textContent = t.tool_dpi_title;
            document.getElementById('toolDpiBadge').textContent = t.tool_dpi_badge;
            document.getElementById('toolDpiDesc').textContent = t.tool_dpi_desc;
            document.getElementById('roadmapTitle').textContent = t.coming_soon_title;
            document.getElementById('toolScarichiTitle').textContent = t.tool_scarichi_title;
            document.getElementById('toolScarichiDesc').textContent = t.tool_scarichi_desc;
            document.getElementById('toolCalceTitle').textContent = t.tool_calce_title;
            document.getElementById('toolCalceDesc').textContent = t.tool_calce_desc;
            document.getElementById('toolResaTitle').textContent = t.tool_resa_title;
            document.getElementById('toolResaDesc').textContent = t.tool_resa_desc;
            document.getElementById('feat1Title').textContent = t.feature_1_title;
            document.getElementById('feat1Desc').textContent = t.feature_1_desc;
            document.getElementById('feat2Title').textContent = t.feature_2_title;
            document.getElementById('feat2Desc').textContent = t.feature_2_desc;
            document.getElementById('feat3Title').textContent = t.feature_3_title;
            document.getElementById('feat3Desc').textContent = t.feature_3_desc;
            document.getElementById('feat4Title').textContent = t.feature_4_title;
            document.getElementById('feat4Desc').textContent = t.feature_4_desc;
            document.getElementById('suggestBannerText').textContent = t.suggest_banner;
            document.getElementById('suggestBtnText').textContent = t.suggest_btn;
            document.getElementById('rightsText').textContent = t.rights_reserved;
            document.getElementById('legalDisclaimerText').innerHTML = t.legal_disclaimer;
        }}

        function setFilter(filter) {{
            currentFilter = filter;
            const btnAll = document.getElementById('filterAllBtn');
            const btnBuilding = document.getElementById('filterBuildingBtn');
            const btnGraph = document.getElementById('filterGraphBtn');

            const activeClass = "px-3 py-1.5 rounded-xl bg-blue-600 text-white shadow-xs transition font-bold";
            const inactiveClass = "px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 transition font-bold";

            btnAll.className = filter === 'all' ? activeClass : inactiveClass;
            btnBuilding.className = filter === 'building' ? activeClass : inactiveClass;
            btnGraph.className = filter === 'graph' ? activeClass : inactiveClass;

            const secBuilding = document.getElementById('sectionBuilding');
            const secGraph = document.getElementById('sectionGraph');
            const secRoadmap = document.getElementById('sectionRoadmap');

            if (filter === 'all') {{
                secBuilding.classList.remove('hidden');
                secGraph.classList.remove('hidden');
                secRoadmap.classList.remove('hidden');
            }} else if (filter === 'building') {{
                secBuilding.classList.remove('hidden');
                secGraph.classList.add('hidden');
                secRoadmap.classList.remove('hidden');
            }} else if (filter === 'graph') {{
                secBuilding.classList.add('hidden');
                secGraph.classList.remove('hidden');
                secRoadmap.classList.remove('hidden');
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
                    el.textContent = 'Copiato! ✓';
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

print("index.html compiled with Central Hub Portal successfully.")
