import json

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/translations_copertura.json', 'r', encoding='utf-8') as f:
    t = json.load(f)

extra_strings = {
    "it": {
        "share_title": "Ti è stato utile questo calcolatore?",
        "share_sub": "Condividilo con colleghi, grafici, editori o clienti",
        "share_copy": "Copia Link",
        "suggest_banner": "Hai un'idea per un nuovo calcolatore di cantiere o grafica?",
        "suggest_btn": "Suggerisci",
        "suggest_modal_title": "Suggerisci uno Strumento",
        "suggest_modal_desc": "Quale nuovo calcolatore, formula o funzione vorresti vedere su OmniTools?",
        "suggest_placeholder": "Scrivi qui la tua idea...",
        "suggest_privacy_note": "🔒 Invio 100% anonimo. Non serve registrarsi.",
        "suggest_send": "Invia",
        "suggest_close": "Annulla",
        "suggest_thanks": "Grazie mille! La tua idea è stata registrata e guiderà i prossimi strumenti di OmniTools.",
        "install_banner_title": "Installa OmniTools come App",
        "install_banner_sub": "Utility per grafici e tipografi sempre a portata di mano"
    },
    "en": {
        "share_title": "Did you find this calculator helpful?",
        "share_sub": "Share it with colleagues, print operators, or designers",
        "share_copy": "Copy Link",
        "suggest_banner": "Have an idea for a new prepress or construction tool?",
        "suggest_btn": "Suggest",
        "suggest_modal_title": "Suggest a New Tool",
        "suggest_modal_desc": "What formula or utility would you like to see on OmniTools?",
        "suggest_placeholder": "Type your idea here...",
        "suggest_privacy_note": "🔒 100% anonymous submission. No sign-up required.",
        "suggest_send": "Send",
        "suggest_close": "Cancel",
        "suggest_thanks": "Thank you! Your idea has been recorded and guides our next tools.",
        "install_banner_title": "Install OmniTools Web App",
        "install_banner_sub": "Prepress & design utilities always at your fingertips"
    },
    "es": {
        "share_title": "¿Te ha sido útil esta calculadora?",
        "share_sub": "Compártela con compañeros de trabajo, diseñadores o imprentas",
        "share_copy": "Copiar Enlace",
        "suggest_banner": "¿Tienes una idea para una nueva herramienta técnica?",
        "suggest_btn": "Sugerir",
        "suggest_modal_title": "Sugerir una Herramienta",
        "suggest_modal_desc": "¿Qué calculadora o fórmula te gustaría ver en OmniTools?",
        "suggest_placeholder": "Escribe tu idea aquí...",
        "suggest_privacy_note": "🔒 Envío 100% anónimo. Sin registros.",
        "suggest_send": "Enviar",
        "suggest_close": "Cancelar",
        "suggest_thanks": "¡Muchas gracias! Tu propuesta guiará las próximas herramientas.",
        "install_banner_title": "Instalar OmniTools como App",
        "install_banner_sub": "Utilidades técnicas siempre a mano en tu dispositivo"
    },
    "fr": {
        "share_title": "Cet outil vous a-t-il été utile ?",
        "share_sub": "Partagez-le avec vos collègues, imprimeurs ou graphistes",
        "share_copy": "Copier le Lien",
        "suggest_banner": "Une idée de nouvel outil graphique ou technique ?",
        "suggest_btn": "Suggérer",
        "suggest_modal_title": "Suggérer un Outil",
        "suggest_modal_desc": "Quelle formule ou utilitaire aimeriez-vous voir ?",
        "suggest_placeholder": "Écrivez votre idée ici...",
        "suggest_privacy_note": "🔒 Envoi 100% anonyme. Aucune inscription requise.",
        "suggest_send": "Envoyer",
        "suggest_close": "Annuler",
        "suggest_thanks": "Merci beaucoup ! Votre suggestion guidera nos prochains développements.",
        "install_banner_title": "Installer OmniTools en App",
        "install_banner_sub": "Vos utilitaires de prépresse toujours à portée de main"
    },
    "de": {
        "share_title": "War dieser Rechner hilfreich?",
        "share_sub": "Teilen Sie ihn mit Kollegen, Druckern oder Designern",
        "share_copy": "Link kopieren",
        "suggest_banner": "Haben Sie eine Idee für ein neues Werkzeug?",
        "suggest_btn": "Vorschlagen",
        "suggest_modal_title": "Werkzeug vorschlagen",
        "suggest_modal_desc": "Welche Formel oder Funktion wünschen Sie sich?",
        "suggest_placeholder": "Geben Sie Ihre Idee hier ein...",
        "suggest_privacy_note": "🔒 100% anonyme Übermittlung. Keine Registrierung.",
        "suggest_send": "Absenden",
        "suggest_close": "Abbrechen",
        "suggest_thanks": "Vielen Dank! Ihre Anregung fließt in unsere Entwicklung ein.",
        "install_banner_title": "OmniTools als App installieren",
        "install_banner_sub": "Präzisionswerkzeuge für Druck und Design griffbereit"
    },
    "pt": {
        "share_title": "Esta calculadora foi útil?",
        "share_sub": "Partilhe com colegas, gráficos ou clientes",
        "share_copy": "Copiar Link",
        "suggest_banner": "Tem ideia para uma nova ferramenta gráfica ou técnica?",
        "suggest_btn": "Sugerir",
        "suggest_modal_title": "Sugerir Ferramenta",
        "suggest_modal_desc": "Que calculadora ou utilitário gostaria de ver no OmniTools?",
        "suggest_placeholder": "Escreva aqui a sua sugestão...",
        "suggest_privacy_note": "🔒 Envio 100% anónimo. Sem registo.",
        "suggest_send": "Enviar",
        "suggest_close": "Cancelar",
        "suggest_thanks": "Muito obrigado! A sua ideia guiará as próximas ferramentas.",
        "install_banner_title": "Instalar OmniTools como App",
        "install_banner_sub": "Utilitários técnicos sempre à mão no seu dispositivo"
    }
}

for lang in t:
    if lang in extra_strings:
        t[lang].update(extra_strings[lang])

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/translations_copertura.json', 'w', encoding='utf-8') as f:
    json.dump(t, f, ensure_ascii=False, indent=2)

print("translations_copertura.json updated with footer, share and modal strings.")
