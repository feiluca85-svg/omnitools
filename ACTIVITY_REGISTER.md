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
