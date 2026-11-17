// /js/omni-core.js
export const OmniCore = {
  get lang() {
    return document.documentElement.lang && document.documentElement.lang.toLowerCase().startsWith('en')
      ? 'en-US'
      : 'it-IT';
  },

  currency(value) {
    if (value === null || value === undefined || Number.isNaN(Number(value))) return '—';
    return new Intl.NumberFormat(this.lang, {
      style: 'currency',
      currency: this.lang === 'it-IT' ? 'EUR' : 'USD',
      minimumFractionDigits: 2,
      maximumFractionDigits: 2
    }).format(Number(value));
  },

  number(value, decimals = 2) {
    if (value === null || value === undefined || Number.isNaN(Number(value))) return '—';
    return new Intl.NumberFormat(this.lang, {
      minimumFractionDigits: decimals,
      maximumFractionDigits: decimals
    }).format(Number(value));
  },

  date(dateObj) {
    if (!(dateObj instanceof Date) || Number.isNaN(dateObj.getTime())) return '—';
    return new Intl.DateTimeFormat(this.lang, {
      year: 'numeric',
      month: '2-digit',
      day: '2-digit'
    }).format(dateObj);
  },

  // Converte pollici decimali in piedi, pollici e frazioni di 1/16" (es. 24.75 -> 2' 0-3/4")
  toImperialFraction(decimalInches, precision = 16) {
    if (decimalInches === null || decimalInches === undefined || Number.isNaN(Number(decimalInches))) return '0"';
    const val = Number(decimalInches);
    const sign = val < 0 ? '-' : '';
    const absInches = Math.abs(val);

    let feet = Math.floor(absInches / 12);
    let remainingInches = absInches - (feet * 12);
    let wholeInches = Math.floor(remainingInches);
    let numerator = Math.round((remainingInches - wholeInches) * precision);

    if (numerator === precision) { wholeInches += 1; numerator = 0; }
    if (wholeInches === 12) { feet += 1; wholeInches = 0; }

    const gcd = (a, b) => (b ? gcd(b, a % b) : a);
    let fractionStr = '';
    if (numerator > 0) {
      const divisor = gcd(numerator, precision);
      fractionStr = `${numerator / divisor}/${precision / divisor}`;
    }

    const feetPart = feet > 0 ? `${feet}' ` : '';
    const inchPart = wholeInches > 0 && fractionStr
      ? `${wholeInches}-${fractionStr}"`
      : wholeInches > 0 ? `${wholeInches}"` : fractionStr ? `${fractionStr}"` : `0"`;

    return `${sign}${feetPart}${inchPart}`.trim();
  },

  // Sincronizza lo stato nell'URL e aggiorna i link di cambio lingua IT <-> EN mantenendo i parametri
  syncStateToUrl(paramsObj) {
    const url = new URL(window.location.href);
    Object.entries(paramsObj).forEach(([key, val]) => {
      if (val !== null && val !== undefined && val !== '' && !Number.isNaN(val)) {
        url.searchParams.set(key, val);
      } else {
        url.searchParams.delete(key);
      }
    });
    window.history.replaceState({}, '', url.toString());

    const mirrorUrl = document.body.dataset.mirrorUrl;
    if (mirrorUrl) {
      document.querySelectorAll('[data-lang-switcher], #lang-switcher').forEach(el => {
        el.setAttribute('href', `${mirrorUrl}${url.search}`);
      });
    }
  },

  getUrlParams() {
    return Object.fromEntries(new URLSearchParams(window.location.search).entries());
  },

  // Utility per il pulsante "Copy Spec" nei box risultati
  async copyText(text, btnElement) {
    try {
      await navigator.clipboard.writeText(text);
      if (btnElement) {
        const original = btnElement.innerHTML;
        btnElement.textContent = this.lang === 'it-IT' ? 'Copiato ✓' : 'Copied ✓';
        setTimeout(() => { btnElement.innerHTML = original; }, 1500);
      }
    } catch (e) {
      console.error('Copy failed', e);
    }
  }
};

window.OmniCore = OmniCore;
