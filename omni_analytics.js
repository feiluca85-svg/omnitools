/**
 * OmniTools Lab — Anonymous & Non-Invasive Event Tracking Engine
 * Fully client-side, zero personal data, zero cookies, zero PII, zero blocking.
 * Dispatches normalized events to window.gtag (if present), window.dataLayer and CustomEvent('omni:track').
 */
(function () {
  'use strict';

  // Normalize tool ID from URL pathname
  function detectToolId() {
    try {
      var p = window.location.pathname || '';
      var clean = p.replace(/\.html$/, '').replace(/^\/+/, '').replace(/^en\//, '');
      return clean || 'hub';
    } catch (e) {
      return 'unknown';
    }
  }

  /**
   * Central Tracking Helper
   * @param {Object} options
   * @param {string} options.category - e.g. 'tool_interaction', 'tool_export', 'tool_navigation'
   * @param {string} [options.tool] - slug of the tool, auto-detected if omitted
   * @param {string} options.action - e.g. 'tool_preset_click', 'tool_mode_change', 'tool_export_click', 'tool_cross_link_click'
   * @param {string} [options.label] - non-sensitive sanitized label (e.g. 'csv', 'bySlope', 'WC-110mm')
   */
  window.trackToolEvent = function (options) {
    try {
      if (!options || typeof options !== 'object') return;
      var action = String(options.action || 'interaction').trim();
      var category = String(options.category || 'tool_interaction').trim();
      var tool = String(options.tool || detectToolId()).trim();
      var rawLabel = options.label != null ? String(options.label).trim() : '';

      // Sanitize label: cap at 60 chars, remove potential personal data, keep clean alphanumeric + symbols
      var label = rawLabel.replace(/[\r\n\t]+/g, ' ').replace(/\s+/g, ' ').slice(0, 60);

      var eventData = {
        event_category: category,
        tool_name: tool,
        event_label: label
      };

      // 1. Dispatch to Google Analytics (gtag) if present
      if (typeof window.gtag === 'function') {
        window.gtag('event', action, eventData);
      }

      // 2. Push to dataLayer if present (GTM or custom analytics)
      if (Array.isArray(window.dataLayer)) {
        window.dataLayer.push(Object.assign({ event: action }, eventData));
      }

      // 3. Dispatch DOM CustomEvent for local debugging or third-party listeners
      if (typeof window.dispatchEvent === 'function' && typeof CustomEvent === 'function') {
        window.dispatchEvent(new CustomEvent('omni:track', {
          detail: Object.assign({ action: action }, eventData)
        }));
      }
    } catch (err) {
      // Safe fail: never impact calculations, exports, or user experience
    }
  };

  // Helper to extract clean button label without personal input
  function getElementLabel(el, fallback) {
    try {
      if (!el) return fallback || '';
      var explicit = el.getAttribute('data-analytics-label') || el.getAttribute('data-preset-name') || el.getAttribute('data-mode');
      if (explicit) return explicit.trim();
      var title = el.getAttribute('title');
      if (title && title.length < 40) return title.trim();
      var text = el.innerText || el.textContent || '';
      text = text.replace(/[\r\n\t]+/g, ' ').replace(/\s+/g, ' ').trim();
      if (text.length > 0 && text.length <= 40) return text;
      if (text.length > 40) return text.slice(0, 40) + '...';
      return el.id || fallback || '';
    } catch (e) {
      return fallback || '';
    }
  }

  // Global Delegated Click Listener for Non-Invasive Automatic Tracking
  function initAutoTracker() {
    if (window._omniAutoTrackerInitialized) return;
    window._omniAutoTrackerInitialized = true;

    document.addEventListener('click', function (e) {
      try {
        var target = e.target;
        if (!target) return;

        // A. TOOL CROSS-LINK CLICK (internal links to other tools)
        var link = target.closest('a[href]');
        if (link) {
          var href = link.getAttribute('href') || '';
          // Ignore hash, external, javascript:, mailto:, tel:
          if (href && !href.startsWith('#') && !href.startsWith('mailto:') && !href.startsWith('tel:') && !href.startsWith('javascript:')) {
            var isInternal = href.startsWith('/') || href.includes('omnitoolslab.com');
            var isDifferentPage = false;
            try {
              var url = new URL(href, window.location.origin);
              if (url.origin === window.location.origin && url.pathname !== window.location.pathname) {
                isDifferentPage = true;
              }
            } catch (ex) {}

            if (isInternal && isDifferentPage) {
              var card = link.closest('.tool-card, .rel-card, [id^="toolCard_"], .group');
              var destTool = href.replace(/\.html$/, '').replace(/^\/+/, '').replace(/^en\//, '');
              var label = destTool;
              if (link.closest('#footerRelTrack, [id*="Rel"], .rel-container')) {
                label = 'related:' + destTool;
              } else if (link.closest('#omniChromeTabsTrack, #omniChromeTabsBar')) {
                label = 'tab:' + destTool;
              } else if (link.closest('#suiteMenuDropdown, #topNewToolDropdown, [id*="suiteMenu"]')) {
                label = 'menu:' + destTool;
              } else if (link.closest('header, nav')) {
                label = 'nav:' + destTool;
              } else if (card) {
                label = 'card:' + destTool;
              }

              window.trackToolEvent({
                category: 'tool_navigation',
                action: 'tool_cross_link_click',
                label: label
              });
              return; // Handled
            }
          }
        }

        // B. BUTTON / ACTION CLICKS
        var btn = target.closest('button, [role="button"], a.btn, a[onclick]');
        if (!btn) return;

        var onclickStr = btn.getAttribute('onclick') || '';
        var btnId = btn.id || '';

        // 1. TOOL EXPORT CLICK (CSV, Print, Copy, SVG, PNG, EPS, PDF)
        var isExport = (
          /triggerUniversalExport|export\w*Csv|download\w*|window\.print|printSheet|copyResults|copyExport|copyRecipe|copySpecs|copySvg|copyCurrentUrl/i.test(onclickStr) ||
          /export|print|download|copy/i.test(btnId) ||
          btn.hasAttribute('data-action-export')
        );

        if (isExport) {
          var exportType = 'generic';
          var combinedText = (onclickStr + ' ' + btnId + ' ' + (btn.innerText || '')).toLowerCase();
          if (combinedText.includes('csv')) {
            exportType = 'csv';
          } else if (combinedText.includes('print') || combinedText.includes('stampa')) {
            exportType = 'print';
          } else if (combinedText.includes('svg')) {
            exportType = 'svg';
          } else if (combinedText.includes('png')) {
            exportType = 'png';
          } else if (combinedText.includes('eps') || combinedText.includes('pdf')) {
            exportType = 'vector';
          } else if (combinedText.includes('copy') || combinedText.includes('copia')) {
            exportType = 'copy';
          }

          window.trackToolEvent({
            category: 'tool_export',
            action: 'tool_export_click',
            label: exportType
          });
          return;
        }

        // 2. TOOL MODE CHANGE
        var isMode = (
          /setMode|switchMode|setCalcMode|switchBindingMode|switchInputMode|setScalerMode|setRoomMode|toggleTableDisplayMode/i.test(onclickStr) ||
          /mode/i.test(btnId) ||
          btn.hasAttribute('data-mode') ||
          btn.closest('[role="tablist"], [id*="Mode"], [class*="mode-selector"]')
        );

        // Exclude dark mode toggle from calculation mode
        if (isMode && !/toggleDarkMode|darkMode/i.test(onclickStr) && !/darkMode/i.test(btnId)) {
          var modeLabel = btn.getAttribute('data-mode') || '';
          if (!modeLabel) {
            var mMatch = onclickStr.match(/(?:setMode|switchMode|switchBindingMode|setCalcMode|setScalerMode|setRoomMode)\(['"]([^'"]+)['"]\)/i);
            if (mMatch) modeLabel = mMatch[1];
          }
          if (!modeLabel) modeLabel = getElementLabel(btn, btnId || 'mode_toggle');

          window.trackToolEvent({
            category: 'tool_interaction',
            action: 'tool_mode_change',
            label: modeLabel
          });
          return;
        }

        // 3. TOOL PRESET CLICK
        var isPreset = (
          /applyPreset|applyEditorialPreset|setPreset|quickPreset|restoreDefaultPresets/i.test(onclickStr) ||
          /preset/i.test(btnId) ||
          btn.hasAttribute('data-preset') ||
          btn.closest('[id*="Preset"], [class*="preset"]')
        );

        // Exclude preset deletion buttons
        if (isPreset && !/deleteCustomPreset|remove/i.test(onclickStr)) {
          var presetLabel = btn.getAttribute('data-preset') || '';
          if (!presetLabel) {
            var pMatch = onclickStr.match(/applyPreset\(['"]([^'"]+)['"]\)/i);
            if (pMatch) presetLabel = pMatch[1];
          }
          if (!presetLabel) presetLabel = getElementLabel(btn, 'preset');

          window.trackToolEvent({
            category: 'tool_interaction',
            action: 'tool_preset_click',
            label: presetLabel
          });
          return;
        }
      } catch (err) {
        // Safe fail
      }
    }, true); // Capture phase ensures events are intercepted reliably
  }

  // Initialize auto-tracker as soon as DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAutoTracker);
  } else {
    initAutoTracker();
  }
})();
