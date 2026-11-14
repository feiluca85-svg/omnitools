// In-memory rate limiting map for edge/serverless execution
const ipRateLimit = new Map();

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }
  
  // Rate Limiting: Max 5 submissions per IP every 5 minutes
  const forwarded = req.headers['x-forwarded-for'];
  const ip = (typeof forwarded === 'string' ? forwarded.split(',')[0] : req.socket?.remoteAddress || 'unknown').trim();
  const now = Date.now();
  const limitWindow = 5 * 60 * 1000; // 5 minuti
  const maxRequests = 5;

  const currentLog = ipRateLimit.get(ip) || { count: 0, firstRequest: now };
  if (now - currentLog.firstRequest > limitWindow) {
    ipRateLimit.set(ip, { count: 1, firstRequest: now });
  } else {
    currentLog.count++;
    if (currentLog.count > maxRequests) {
      console.warn(`[RATE_LIMIT_BLOCKED] IP: ${ip} attempted spam on /api/suggest`);
      return res.status(429).json({ error: 'Troppe richieste inviate. Riprova tra qualche minuto.' });
    }
    ipRateLimit.set(ip, currentLog);
  }
  
  try {
    let body = req.body;
    if (typeof body === 'string') {
      try { body = JSON.parse(body); } catch (_) {}
    }
    
    // Honeypot check (anti-bot trap)
    if (body && (body._gotcha || body.website_url_trap)) {
      return res.status(200).json({ success: true }); // Silently drop bot spam
    }
    
    const rawMsg = (body && (body.message || body.idea || body.text)) || '';
    const message = String(rawMsg).trim();
    const lang = (body && body.lang) || 'it';
    const tool = (body && (body.tool || body.page)) || 'unknown';
    
    if (!message || message.length === 0) {
      return res.status(400).json({ error: 'Message cannot be empty' });
    }

    if (message.length > 2500) {
      return res.status(400).json({ error: 'Message too long (max 2500 chars)' });
    }
    
    const timestamp = new Date().toISOString();
    // 1. Log prominently to Vercel Runtime Logs
    console.log(`[OMNITOOLS SUGGESTION] [Tool: ${tool}] [Lang: ${lang}] [Timestamp: ${timestamp}]: ${message}`);
    
    // 2. Zero-registration instant Email Notification to clickbanger.agency@outlook.com via obfuscated FormSubmit Token
    try {
      await fetch('https://formsubmit.co/ajax/0bbb163b700573322a5bd20f8e1ef71e', {
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
