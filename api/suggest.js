export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }
  
  try {
    let body = req.body;
    if (typeof body === 'string') {
      try { body = JSON.parse(body); } catch (_) {}
    }
    
    const rawMsg = (body && (body.message || body.idea || body.text)) || '';
    const message = String(rawMsg).trim();
    const lang = (body && body.lang) || 'it';
    const tool = (body && (body.tool || body.page)) || 'unknown';
    
    if (!message || message.length === 0) {
      return res.status(400).json({ error: 'Message cannot be empty' });
    }
    
    const timestamp = new Date().toISOString();
    // 1. Log prominently to Vercel Runtime Logs
    console.log(`[OMNITOOLS SUGGESTION] [Tool: ${tool}] [Lang: ${lang}] [Timestamp: ${timestamp}]: ${message}`);
    
    // 2. Zero-registration instant Email Notification to clickbanger.agency@outlook.com
    try {
      await fetch('https://formsubmit.co/ajax/clickbanger.agency@outlook.com', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
          'Referer': 'https://www.omnitoolslab.com/',
          'Origin': 'https://www.omnitoolslab.com'
        },
        body: JSON.stringify({
          _subject: `💡 Nuovo Suggerimento OmniTools [${tool.toUpperCase()}]`,
          _template: 'table',
          _captcha: 'false',
          Tool: tool,
          Lingua: lang,
          Data: timestamp,
          Suggerimento_Utente: message
        })
      });
    } catch (mailErr) {
      console.warn('FormSubmit email forwarding warning:', mailErr);
    }
    
    return res.status(200).json({ success: true, tool, lang });
  } catch (err) {
    console.error('Feedback error:', err);
    return res.status(500).json({ error: 'Internal server error' });
  }
}
