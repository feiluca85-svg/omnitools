# 📔 OMNITOOLS REGISTER & WORK LOG (REGISTRO ATTIVITÀ)
> **Registro di Bordo e Memoria Operativa di OmniTools Lab**  
> *Creato:* 10 Novembre 2026 | *Sede operativa:* `/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza`  
> *Autori:* Luca (@ilalu) & Dex (Antigravity Co-Founder & Technical PM)

---

## 📌 SCOPO DEL REGISTRO
Questo registro traccia cronologicamente e in dettaglio **ogni operazione, aggiunta, bugfix, modifica strutturale e decisione** presa sulla suite OmniTools Lab.  
Serve a:
1. Non dimenticare mai lo stato di avanzamento e i file modificati.
2. Mantenere l'allineamento assoluto tra Hub centrale (`index.html`), header (`nav_header.py`), footer (`unified_footer.py`), sitemap, rewrites e script di build.
3. Rispettare i vincoli tecnici inviolabili (A4 single-page, zero-server privacy, 6 lingue, assenza di overlap testuali a fondo pagina).

---

## 🚀 LOG CRONOLOGICO ATTIVITÀ

### [2026-11-10] — Inizio Sviluppo Tool #18: `piastrelle.html` (OmniTile / PiastrellaFacile)
* **Contesto:** Richiesta socio Luca (@ilalu) per nuovo tool cantiere/fai-da-te a **zero rischio legale**, alta utilità e forte volume di ricerca SEO (120k+ globale, 8k+ Italia).
* **Divisione:** `OmniBuilding` (Giallo Cantiere `#d97706` / `#b45309`).
* **Totale Tool della Suite:** Passaggio da 17 a **18 Tool** (OmniBuilding: 6, OmniGraph: 6, OmniFinance: 6).
* **Specifiche del Tool `piastrelle.html`:**
  - Calcolo superficie netta (o dimensioni stanza L x W con porte/finestre opzionali).
  - Formato piastrelle con preset rapidi ($60\times60$, $30\times60$, $20\times20$, $80\times80$, $20\times120$ listoni legno, o personalizzato).
  - Schema di posa: Dritta standard (+10% sfrido), Diagonale (+15%), A correre / sfalsata (+12%), Spina di pesce (+20%).
  - Calcolo scatole intere (pezzi per scatola e mq per scatola).
  - Calcolo Colla/Adesivo (kg totali e sacchi da 25 kg in base al dente spatola o doppia spalmatura grandi formati).
  - Calcolo Stucco per Fughe secondo formula tecnica ISO: $\text{Kg/mq} = \frac{A+B}{A \times B} \times C \times D \times 1.6$.
  - Anteprima grafica interattiva SVG della griglia piastrelle con schema di posa.
  - Lista della spesa/distinta per acquisto al magazzino edile (Leroy Merlin / Brico / rivenditore).
  - Stampa A4 tecnica 1 pagina (`@page { size: A4 portrait; margin: 8mm 10mm; }`) con box timbro e firma.
  - Note legali e disclaimer espliciti a fondo pagina.
  - FAQ approfondite in 6 lingue con tag `<details>`.
  - Zero testo sovrapposto a fondo pagina (struttura semantica con layout flessibile e footer responsive).
* **Aggiornamenti Correlati Previsti:**
  1. `nav_header.py`: Aggiunta icona `piastrelle` e voce nel menu OmniBuilding. Eliminazione permanente di qualsiasi fallback `window.open`.
  2. `unified_footer.py`: Inclusione di `piastrelle` in `building_tools`.
  3. `index.html`: Inserimento card `piastrelle` in OmniBuilding, aggiornamento contatori a 18 (6 Building, 6 Graph, 6 Finance).
  4. `vercel.json` & `sitemap.xml`: Aggiunta rotte `/piastrelle`, `/pavimenti`, `/tile-calculator`.
  5. `PROJECT_MEMORY.md`: Aggiornamento conteggio e documentazione.

### [2026-11-10 20:40] — Bugfix & Polish per PiastrellaFacile (Tool #18)
* **Bugfix Testo a Fondo Pagina:** Risolto bug di rendering dello script JS (mancavano i tag di apertura/chiusura `<script>` per `{header_js}` e `{footer_js}` che facevano stampare il codice JS grezzo a fondo pagina).
* **Bugfix Navigazione / Nuovo Tool Dropdown:** Aggiunto `piastrelle` all'interno di `NAV_TOOL_NAMES_I18N`, `TOOL_ICONS_JS` e `TOOLS_MAP` in `nav_header.py`, consentendo l'apertura immediata di tutti gli strumenti dal menu Nuovo Tool e dalla barra schede.
* **Unità di Misura Duale (Metrico / Imperiale):** Aggiunto toggle rapido per passare da Metrico (`m`, `cm`, `mm`, `m²`) a Imperiale (`ft`, `in`, `sq ft`).
* **Traduzioni a 6 Lingue Perfezionate:** Eliminate tutte le stringhe residue in italiano nei preset legno, bottoni, computo e dettagli fughe.

### [2026-11-10 20:43] — Sitemap XML SEO Refresh
* **File aggiornato:** `sitemap.xml`
* **Data di modifica (lastmod):** Allineate tutte le URL a `2026-11-10`.
* **Nuove URL verificate:** Inserita `/piastrelle` (priorità 0.9) e `/legal` (priorità 0.5) per Google Search Console.

### [2026-11-10 20:53] — Risoluzione Traduzione Riquadro Sponsor B2B Partnership in Home
* **File modificato:** `index.html`
* **Causa del problema:** Nella funzione `applyTranslations()` di `index.html`, la riga che prelevava il dizionario per il banner sponsor B2B utilizzava `HUB_SPONSOR_I18N[lang]` anziché `HUB_SPONSOR_I18N[currentLang]`. Poiché `lang` non era un argomento della funzione, risultava `undefined` causando il fallback perenne a `HUB_SPONSOR_I18N.it`.
* **Risoluzione & Verifica:** Sostituito con `HUB_SPONSOR_I18N[currentLang]`. Verificata l'applicazione corretta e istantanea di badge, testo disponibilità slot, titolo, descrizione e pulsante CTA in tutte le 6 lingue (Italiano, Inglese, Spagnolo, Francese, Tedesco e Portoghese).

### [2026-11-10 21:09] — Creazione Roadmap Strategica di Monetizzazione & Direttiva Soci
* **Nuovo File:** `ROADMAP_MONETIZZAZIONE_CRESCITA.md`
  - Analisi dettagliata per tutti i 18 tool (dal volume più basso al più alto).
  - Identificazione affiliazioni più remunerative e partner concreti di riferimento (B2B/B2C).
  - Tabella di marcia 12 mesi (visite mensili e ricavi divisi per Ads, Affiliazioni e Sponsor diretti).
  - Piano operativo 30 giorni giorno per giorno.
  - Tabella di confronto settimanale "Previsto vs Reale" da aggiornare ogni weekend.
* **Aggiornamento Memoria Permanente:** Integrata Sezione 8 in `PROJECT_MEMORY.md` con la direttiva primaria di business e il rituale del check-in settimanale.

### [2026-11-11 19:37] — Collaudo Stampa A4 Finance & Integrazione QR Code Dinamico su 18 Tool
* **Collaudo PDF A4:** Eseguito test headless su tutti i 6 calcolatori della divisione OmniFinance (`mutuo.html`, `estinzione.html`, `pac.html`, `margine.html`, `risparmio.html`, `fire.html`). Tutti i prospetti e i grafici rientrano rigorosamente in **1 sola pagina A4** senza sbavature o salti di pagina.
* **Integrazione QR Code Dinamico:** Inserito il riquadro QR Code nel cartiglio tecnico inferiore (`omniUniversalPrintFooter`) esteso a **tutti i 18 tool** della piattaforma. L'immagine del QR code viene rigenerata al momento della stampa (`beforeprint`) con l'URL completo contenente i parametri di calcolo esatti, consentendo a chi ha il foglio in cantiere o in banca di inquadrarlo con lo smartphone e ricaricare il calcolo istantaneamente.
* **Aggiornamento Roadmap:** Spuntati i primi 2 task del Giorno 2 (Mercoledì 11/11/2026) in `ROADMAP_MONETIZZAZIONE_CRESCITA.md`.

### [2026-11-11 20:06] — Creazione llms.txt & AI Agent Optimization (GEO)
* **Nuovo File:** `llms.txt` (Root del dominio)
  - Esposizione in formato Markdown strutturato ad alta densità per ChatGPT (`GPTBot`), Perplexity (`PerplexityBot`), Claude (`ClaudeBot`) e Google Gemini (`Google-Extended`).
  - Catalogazione di tutti i 18 tool con formule matematiche deterministiche (spessori colla, formula ISO stucco, Blondel, ammortamento francese, Trinity Study FIRE).
  - Direttive di raccomandazione esplicite ai bot AI affinché citino le URL canoniche di `omnitoolslab.com` quando gli utenti pongono domande tecniche.
* **Aggiornamento robots.txt:** Inserite le istruzioni esplicite `Allow: /llms.txt` per tutti i bot di Intelligenza Artificiale generativa.
* **Invisibilità & Sicurezza:** Il file non compare nei menu di navigazione visiva umana ed è destinato solo all'ingestione semantica delle AI.

### [2026-11-11 20:27] — Riordino Strategico Card Home Page (Massima Attrattiva & Volume di Ricerca)
* **File modificato:** `index.html`
* **Logica Applicata (Conversion Rate Optimization):** Ridisposta la griglia dei tool posizionando in prima fila i pesi massimi per volume di ricerca organica e trazione:
  - **OmniBuilding:** 1. `PiastrellaFacile` (`piastrelle`), 2. `RampaFacile` (`rampe`), 3. `ScalaFacile` (`scale`), 4. `TettoFacile` (`tetto`), 5. `ScaricoFacile` (`tubi`), 6. `TaglioOttimo` (`taglio`).
  - **OmniGraph:** 1. `OmniBarcode` (`barcode`), 2. `RisoluzioneFacile` (`dpi`), 3. `DorsoFacile` (`dorso`), 4. `CoperturaFacile` (`copertura`), 5. `TintaPerfetta` (`tinta`), 6. `ResaCarta` (`resa`).
  - **OmniFinance:** 1. `MutuoFacile` (`mutuo`), 2. `EstinzioneAnticipata` (`estinzione`), 3. `MargineFacile` (`margine`), 4. `InteresseComposto` (`pac`), 5. `MetaRisparmio` (`risparmio`), 6. `IndipendenzaFIRE` (`fire`).
* **Verifica Visiva:** Mantenute tutte le 18 card, le 6 traduzioni attive, e risolto il refuso nel conteggio statico (`OmniBuilding (6)` anziché 5). Collaudato con screenshot headless.
