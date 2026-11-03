export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    let body = req.body;
    if (typeof body === 'string') {
      try { body = JSON.parse(body); } catch (_) {}
    }

    const { company, email, type, message, phone } = body || {};

    if (!email || !email.includes('@')) {
      return res.status(400).json({ error: 'Valid email required' });
    }

    // Prominently log to Vercel logs so partners/sponsors are immediately traceable
    console.log(`[OMNITOOLS PARTNERSHIP INQUIRY] [Timestamp: ${new Date().toISOString()}]`);
    console.log(`Company: ${company || 'N/A'}`);
    console.log(`Email: ${email}`);
    console.log(`Phone: ${phone || 'N/A'}`);
    console.log(`Partnership Type: ${type || 'General'}`);
    console.log(`Message: ${message || 'N/A'}`);

    return res.status(200).json({ success: true, message: 'Richiesta ricevuta con successo. Il team di OmniTools Lab ti ricontatterà entro 24 ore lavorative.' });
  } catch (err) {
    console.error('Partner inquiry error:', err);
    return res.status(500).json({ error: 'Internal server error' });
  }
}
