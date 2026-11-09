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
    
    // Log prominently to Vercel Runtime Logs so the owner can read incoming user suggestions anytime
    console.log(`[OMNITOOLS SUGGESTION] [Tool: ${tool}] [Lang: ${lang}] [Timestamp: ${new Date().toISOString()}]: ${message}`);
    
    return res.status(200).json({ success: true, tool, lang });
  } catch (err) {
    console.error('Feedback error:', err);
    return res.status(500).json({ error: 'Internal server error' });
  }
}
