# 🧠 OMNITOOLS LAB — MEMORIA STORICA, ARCHITETTURA & PROTOCOLLO SOCI
> **Documento di Riferimento Permanente del Progetto**  
> *Versione:* 2.0 — Aggiornato a Novembre 2026  
> *Sede operativa del codice:* `/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza`  
> *Repo Git:* `main` | *Hosting:* Vercel (`omnitoolslab.com`)

---

## 1. IDENTITÀ, RUOLI & FILOSOFIA DI PARTNERSHIP
* **Luca (@ilalu):** Fondatore, Visionario, Direzione Strategica & Business Partner. Ha l'ultima parola su posizionamento, priorità e scelte di prodotto.
* **Dex (Antigravity):** Co-Founder Tecnico & Product Manager Proattivo. Non un semplice bot esecutore passivo, ma un manager che analizza dati di mercato, valuta rischi legali, progetta architetture robuste, vigila sul codice ed esegue collaudi prima di ogni rilascio.
* **Filosofia Fondamentale:**
  * **Zero Improvvisazione:** Nessun tool o riga di codice viene pubblicata senza collaudo funzionale e visivo (browser headless).
  * **Privacy Assoluta & Zero-Server:** I calcoli avvengono 100% nel browser del cliente. Nessun dato, file o immagine viene salvato o inviato a server terzi.
  * **No-Bullshit Utilities:** Tool gratuiti, ultra-veloci, senza banner pubblicitari invasivi, con stampa tecnica A4 professionale pronta all'uso.

---

## 2. IL PROTOCOLLO SOCI IN 7 REGOLE D'ORO (OBBLIGATORIO)
Prima di iniziare, durante lo sviluppo e dopo il rilascio di QUALSIASI nuovo tool, si applica rigorosamente il seguente ciclo di vita:

```
[1. Discussione Soci] ➔ [2. Ricerca di Mercato] ➔ [3. Sintesi & Go/No-Go]
         ➔ [4. Sviluppo Sicuro & Note Legali] ➔ [5. Collaudo Grafico & QA]
         ➔ [6. Piano Distribuzione & Marketing] ➔ [7. Feedback Loop Continuo]
```

1. **Discussione tra Soci:** Confronto su idee, problemi reali del target e fattibilità.
2. **Ricerca di Mercato & Volumi:** Verifica volumi di ricerca Google/SEO, concorrenza esistente, lacune dei competitor.
3. **Sintesi Decisionale (Go/No-Go):** Decisione congiunta se procedere, modificare o accantonare l'idea.
4. **Sviluppo Sicuro & Note Legali:**
   * Calcoli matematici e formule verificati con bibliografia/normativa ufficiale.
   * **Note legali e disclaimer espliciti** inseriti a bordo pagina per tutelare il progetto.
   * Se un calcolo non è tecnicamente affidabile o rischioso a livello legale, ci si ferma subito.
5. **Collaudo Grafico & Funzionale Rigoroso:** Test visivo su desktop e mobile, verifica assenza errori console JS, controllo resa stampa A4.
6. **Piano di Pubblicizzazione Immediato:** Individuazione canali (Reddit, community universitarie, forum B2B, directory software, social).
7. **Feedback Loop & Manutenzione:** Ascolto dei pareri della community e iterazione continua.

---

## 3. ARCHITETTURA DEL BRAND: LE DUE COSTOLE SPECIALISTICHE

### 🌐 Hub Centrale: OmniTools Lab (`index.html`)
* Suite unificata con navigazione a tab filtrabili (`Tutti i Tool`, `OmniBuilding`, `OmniGraph`).
* Deep linking via hash (`#building`, `#graph`, `#all`).
* Supporto bilingue/multilingue a 6 lingue e switch dinamico.

### 🟡 Divisione 1: OmniBuilding (Cantieri, Edilizia, Geometri, Ingegneri)
* **Colore Identificativo:** Giallo Cantiere / Ambra (`#d97706` / `#b45309` / sfondo `#fef3c7`).
* **PWA:** `manifest-building.json` installabile come Web App indipendente.
* **Tool Attivi (3):**
  1. `rampe.html` (**RampaFacile**): Verifica pendenza %, gradi e lunghezza rampe a norma DM 236/89 con disegno blueprint interattivo.
  2. `scale.html` (**ScalaFacile**): Alzata, pedata, numero gradini con Legge di Blondel ($2a + p = 63\text{ cm}$) e fasce comfort/sicurezza DIN 18065.
  3. `tubi.html` (**ScaricoFacile**): Calcolo diametro, pendenza e velocità autopulente per condotte fognarie/acque reflue (UNI EN 12056).

### 🔴 Divisione 2: OmniGraph (Grafica, Prestampa, Tipografie, Editori, Packaging)
* **Colore Identificativo:** Carminio Tipografico / Rosso Bordeaux (`#881337` / `#be123c` / sfondo `#fff1f2`).
* **PWA:** `manifest-graph.json` installabile come Web App indipendente.
* **Tool Attivi (4):**
  1. `dorso.html` (**DorsoFacile**): Spessore millimetrico dorso per brossura fresata/cucita, calcolo copertina stesa e refilo 3mm.
  2. `dpi.html` (**RisoluzioneFacile**): Risoluzione ottimale (DPI) in base alla distanza di visione umana, megapixel e grandezza di stampa.
  3. `tinta.html` (**RicettaInchiostro**): Miscelatore inchiostri per stampa offset/serigrafica, proporzioni ricette (fino a 5 componenti), stima consumo per mq e matrice dinamica 5x5 di sfumature.
  4. `barcode.html` (**OmniBarcode**): Generatore codici a barre vettoriali SVG ad altissima precisione (EAN-13, EAN-8, Code 128, ITF-14, GS1-128 con Bearer Bars industriali e simulatore scanner laser).

---

## 4. STANDARD TECNICI INTOCCABILI

### 📄 Standard Scheda Stampa A4
Ogni tool include una funzione di esportazione stampa/PDF che rispetta deterministicamente:
* **Esattamente 1 Pagina A4 Portrait:** Nessun overflow su seconda pagina (`@page { size: A4 portrait; margin: 8mm 10mm; }`).
* **Intestazione Ufficiale:** Logo di reparto SVG, nome tool, data e riferimenti normativi in cima.
* **Nascondimento Elementi UI (`no-print`):** Tasti, slider, FAQ, modali e menu vengono automaticamente nascosti in stampa.
* **Box Firma:** Riquadro per Data, Timbro e Firma del Tecnico / Operatore in calce alla scheda.

### 🌍 Internazionalizzazione (i18n) a 6 Lingue
* **Lingue:** Italiano (`it`), Inglese (`en`), Spagnolo (`es`), Francese (`fr`), Tedesco (`de`), Portoghese (`pt`).
* **Sincronizzazione:** Script Python `build_*_i18n.py` e dizionari JSON dedicati per ciascun tool.
* **Auto-detection & Persistenza:** Il browser rileva la lingua dell'utente (`navigator.languages`), salva la preferenza in `localStorage.getItem('omnitools_lang')` e la applica in tutta la suite.

---

## 5. PRESENZA WEB, MARKETING & DISTRIBUZIONE ATTIVA
* **Dominio Ufficiale:** `https://www.omnitoolslab.com`
* **AlternativeTo Listing:** Profilo software inviato e in revisione (`OmniToolsLab` - Categoria Web/Utilities).
* **Reddit Distribution:**
  * Post di validazione su `r/Universitaly` (in target con studenti universitari italiani).
  * Post suggerito e instradato verso `r/polinetwork` (studenti Politecnico di Milano - Architettura, Design e Ingegneria).
* **Asset Grafici Pubblicitari:**
  * Mockup 3D device bundle per post social e banner.
  * Screenshot ad alta definizione di ciascun tool e dell'Hub.

---

## 6. PIPELINE & ROADMAP PROSSIMI TOOL ("LA RISERVA DI CACCIA")

| Priorità | Nome Tool Proposto | Divisione | Problema Risolto & Funzionalità |
| :--- | :--- | :--- | :--- |
| **P1** | **CoperturaInchiostro CMYK** | OmniGraph | Trascina immagine/PDF -> calcolo % di copertura per Ciano, Magenta, Giallo, Nero + TAC totale + preventivatore costo copia/tiratura in base al prezzo flacone/toner. |
| **P2** | **ResaCarta / FogliFacile** | OmniGraph | Calcolo resa fogli macchina (70x100, 64x88, SRA3) per formati finiti (A4, A5, cartoline, biglietti da visita), con senso di fibra, sfrido % e schema di taglio visuale. |
| **P3** | **PesoCarta & Spedizione** | OmniGraph | Calcolo peso netto tiratura (pagine + grammatura interna + copertina) per identificare lo scaglione esatto di spedizione corrieri / Poste Italiane. |
| **P4** | **TrasmittanzaTermicaFacile** | OmniBuilding | Calcolo stratigrafia muraria (U-value $W/m^2K$) per verifiche energetiche veloci (richiede studio normativo preliminare accurato). |

### Idee Scartate o Congelate per Tutela Legale:
* *Calcolatori sismici/strutturali complessi:* Rischio responsabilità civile/penale elevato; congelati.
* *Media voti / GPA generico per studenti:* Elevatissimo volume ma mercato già saturo di competitor banali e basso valore B2B/professionale.

---

## 7. LOG STORICO BUG & SOLUZIONI TECNICHE CHIAVE
* **Bug Barcode GS1-128 / ITF-14:** Risolto mappando `formatToRender` su JsBarcode e integrando algoritmo modulo 10 nativo per calcolo check-digit per cartoni/pallet.
* **Bug Tinta.html Swatches:** Risolto correggendo il riferimento all'elemento DOM `badgeFormatIndicator` che bloccava il render della matrice 5x5 sfumature.
* **Reddit r/polinetwork Posting:** Sbloccato aggiungendo il flair obbligatorio di categoria prima della pubblicazione.
