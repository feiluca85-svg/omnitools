export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }
  
  try {
    let body = req.body;
    if (typeof body === 'string') {
      try { body = JSON.parse(body); } catch (_) {}
    }
    
    const { message, lang } = body || {};
    
    if (!message || message.trim().length === 0) {
      return res.status(400).json({ error: 'Message cannot be empty' });
    }
    
    // Log prominently to Vercel logs so the owner can read incoming user suggestions anytime
    console.log(`[OMNITOOLS SUGGESTION] [Lang: ${lang || 'it'}] [Timestamp: ${new Date().toISOString()}]: ${message.trim()}`);
    
    return res.status(200).json({ success: true });
  } catch (err) {
    console.error('Feedback error:', err);
    return res.status(500).json({ error: 'Internal server error' });
  }
}
