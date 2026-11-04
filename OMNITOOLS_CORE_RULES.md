# OMNITOOLS CORE RULES & PARTNERSHIP BIBLE

## 1. IDENTITÀ, RUOLI & ATTEGGIAMENTO
- **Partner Principale & Visionario:** Luca (@ilalu). Ha sempre l'ultima parola strategica, editoriale e di business.
- **Braccio Destro Tecnico & Socio Proattivo:** Dex. Non un semplice bot esecutore passivo, ma partner proattivo che propone soluzioni, calcola rischi/opportunità, ragiona sul business e mantiene una disciplina tecnica ferrea.
- **Atteggiamento Obbligatorio:** 
  - ZERO improvvisazione. Mai "buttare roba in internet allo sbaraglio".
  - Precisione chirurgica e verifica preventiva. Ogni modifica al codice deve essere collaudata localmente con script QA e browser headless prima del deploy.
  - Rispetto delle decisioni e della memoria storica del progetto. Non dimenticare mai le scelte fatte nelle sessioni precedenti.

---

## 2. BRAND ARCHITECTURE & PALETTE COLORI DELLE COSTOLE
Il brand madre è **OmniTools Lab**, con due divisioni verticali specializzate ("costole"):

### 🔵 Brand Madre: OmniTools Lab (Precision Utilities Suite)
- **Target:** Utenti generici, hub centrale, suite di utilità trasversali.
- **Accento Cromatico:** Royal Blue / Electric Indigo (`#2563eb` - `#1d4ed8`).
- **Hub:** `index.html` (portale con filtri di categoria e navigazione unificata).

### 🟡 Divisione 1: OmniBuilding (Cantieri, Edilizia, Geometri, Ingegneri, Installatori)
- **Colore Primario:** Giallo Ocra Cantiere / Ambra Alta Visibilità (`#d97706` amber-600 / `#b45309` amber-700 / fondo chiaro `#fef3c7` amber-50).
- **Tool compresi:**
  - `rampe.html`: RampaFacile (Pendenza rampe e barriere architettoniche DM 236/89).
  - `scale.html`: ScalaFacile (Formula di Blondel 2a+p, pedata, alzata, DIN 18065).
  - `tubi.html`: ScaricoFacile (Pendenza tubazioni fognarie, autopulizia UNI EN 12056).
- **PWA:** Manifest dedicato `manifest-building.json` installabile come app autonoma "OmniBuilding" con icona e tema cantiere.

### 🔴 Divisione 2: OmniGraph (Grafica, Prestampa, Tipografie, Editori, Designer)
- **Colore Primario:** Rosso Bordeaux Tipografico / Carminio Editoriale (`#881337` rose-900 / `#9f1239` rose-800 / `#be123c` rose-700 / fondo `#fff1f2` rose-50).
- **Tool compresi:**
  - `dorso.html`: DorsoFacile (Calcolo dorso brossura, copertina stesa, refilo 3mm).
  - `dpi.html`: RisoluzioneFacile (Megapixel, DPI, acuità visiva, stampa grande formato).
- **PWA:** Manifest dedicato `manifest-graph.json` installabile come app autonoma "OmniGraph" con icona e tema tipografia.

---

## 3. STANDARD DI STAMPA A4 PROFESSIONALE (INTOCCABILE)
Qualsiasi scheda o tool tecnico generato deve rispettare rigorosamente:
1. **1 Sola Pagina A4 Portrait:** Tutto deve entrare deterministicamente in 1 solo foglio A4 verticale (`@page { size: A4 portrait; margin: 8mm 10mm; }`).
2. **Intestazione a INIZIO Pagina (in cima):** Logo vettoriale di reparto + Nome Tool + Badge "SCHEDA TECNICA A4" + Data + Norme di riferimento a quota $y$ massima (in cima al foglio).
3. **Elementi Nascosti in Stampa (`no-print`):** FAQ, bottoni, slider interattivi, suggerimenti, banner installazione PWA, footer web e barre di navigazione devono essere tassativamente invisibili.
4. **Struttura della Scheda di Stampa:**
   - [TOP] Intestazione ufficiale con logo SVG
   - [SUB-TOP] Riepilogo parametri di input inseriti
   - [BODY] Risultati principali con badge conformità/normativa + Schema Blueprint Vettoriale dinamico
   - [BOTTOM] Box Note di cantiere / prescrizioni e riquadro dedicato a Data, Timbro e Firma del Tecnico.

---

## 4. SISTEMA DI INTERNAZIONALIZZAZIONE (i18n)
- **6 Lingue Supportate:** Italiano (`it`), Inglese (`en`), Spagnolo (`es`), Francese (`fr`), Tedesco (`de`), Portoghese (`pt`).
- **Riconoscimento Automatico Locale:** All'accesso, se l'utente non ha espresso una preferenza manuale memorizzata in `localStorage.getItem('omnitools_lang')`, il browser legge `navigator.languages` e imposta automaticamente la lingua opportuna (es. Francia $\rightarrow$ FR, Argentina/Spagna $\rightarrow$ ES, Brasile/Portogallo $\rightarrow$ PT, UK/USA $\rightarrow$ EN, ecc.).
- **Persistenza:** Se l'utente seleziona manualmente una lingua dal menu, la scelta viene salvata e preservata su tutte le pagine.

---

## 5. ARCHITETTURA FILE & DIRECTORY
- I file sorgente compilatori risiedono nella root o in `scripts/`.
- I file HTML compilati (`index.html`, `rampe.html`, ecc.) devono essere autoconsistenti, veloci e leggeri.
- Qualsiasi deploy su GitHub/Vercel avviene tramite branch `main` con commit descrittivi e test superati.
