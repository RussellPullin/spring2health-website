const TO = process.env.RESEND_TO_EMAIL || 'info@spring2health.com.au';
const FROM =
  process.env.RESEND_FROM_EMAIL ||
  'Spring 2 Health <noreply@spring2health.com.au>';

function setCorsHeaders(req, res) {
  const origin = req.headers.origin;
  const allowedOrigins = [
    'https://spring2health.com.au',
    'https://www.spring2health.com.au',
    'http://localhost:3456'
  ];

  if (allowedOrigins.includes(origin)) {
    res.setHeader('Access-Control-Allow-Origin', origin);
  }

  res.setHeader('Vary', 'Origin');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
}

module.exports = async function handler(req, res) {
  setCorsHeaders(req, res);

  if (req.method === 'OPTIONS') return res.status(204).end();
  if (req.method !== 'POST') return res.status(405).end();

  if (!process.env.RESEND_API_KEY) {
    return res.status(500).json({ error: 'missing_resend_api_key' });
  }

  const d = typeof req.body === 'string' ? JSON.parse(req.body) : req.body;
  const isRef = d.type === 'referral';

  const subject = isRef
    ? `New Referral — ${d.participant_first || ''} ${d.participant_last || ''}`.trim()
    : `New Contact Message — ${d.first_name || ''} ${d.last_name || ''}`.trim();

  const html = isRef ? referralHtml(d) : contactHtml(d);

  try {
    const response = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${process.env.RESEND_API_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        from: FROM,
        to: [TO],
        reply_to: d.email || undefined,
        subject,
        html,
      }),
    });

    const result = await response.json().catch(() => ({}));

    if (!response.ok) {
      const message = JSON.stringify(result);
      console.error('Resend error:', response.status, message);
      return res.status(500).json({ error: 'send_failed' });
    }

    res.status(200).json({ ok: true, id: result.id });
  } catch (err) {
    console.error('Resend error:', err);
    res.status(500).json({ error: 'send_failed' });
  }
};

function row(label, value) {
  return `<tr>
    <td style="padding:7px 20px 7px 0;font-weight:600;color:#1B4D35;white-space:nowrap;vertical-align:top;">${label}</td>
    <td style="padding:7px 0;color:#333;">${value || '&mdash;'}</td>
  </tr>`;
}

function referralHtml(d) {
  return `
<!DOCTYPE html><html><body style="margin:0;padding:20px;background:#f0f0f0;font-family:Arial,sans-serif;">
<div style="max-width:600px;margin:0 auto;">
  <div style="background:#1B4D35;padding:28px 36px;border-radius:10px 10px 0 0;">
    <h1 style="color:#fff;margin:0;font-size:22px;font-weight:700;">New Referral Submission</h1>
    <p style="color:rgba(255,255,255,0.55);margin:6px 0 0;font-size:13px;">Spring 2 Health &mdash; spring2health.com.au</p>
  </div>
  <div style="background:#fff;padding:36px;border-radius:0 0 10px 10px;border:1px solid #ddd;border-top:none;">
    <table style="width:100%;border-collapse:collapse;">
      ${row('Participant Name', `${d.participant_first || ''} ${d.participant_last || ''}`.trim())}
      ${row('Date of Birth', d.dob)}
      ${row('NDIS Number', d.ndis_number)}
      ${row('Phone', d.phone)}
      ${row('Email', d.email)}
      ${row('Referral Source', d.referral_source)}
      ${row('Services Required', d.services_required)}
    </table>
    ${d.additional_info ? `
    <div style="margin-top:24px;padding:18px;background:#f7faf8;border-radius:8px;border:1px solid #d0e5d8;">
      <strong style="color:#1B4D35;font-size:13px;text-transform:uppercase;letter-spacing:0.06em;">Additional Information</strong>
      <p style="margin:10px 0 0;color:#444;line-height:1.7;">${d.additional_info}</p>
    </div>` : ''}
  </div>
  <p style="text-align:center;color:#999;font-size:12px;margin-top:16px;">This email was sent from the Spring 2 Health website referral form.</p>
</div>
</body></html>`;
}

function contactHtml(d) {
  return `
<!DOCTYPE html><html><body style="margin:0;padding:20px;background:#f0f0f0;font-family:Arial,sans-serif;">
<div style="max-width:600px;margin:0 auto;">
  <div style="background:#1B4D35;padding:28px 36px;border-radius:10px 10px 0 0;">
    <h1 style="color:#fff;margin:0;font-size:22px;font-weight:700;">New Contact Message</h1>
    <p style="color:rgba(255,255,255,0.55);margin:6px 0 0;font-size:13px;">Spring 2 Health &mdash; spring2health.com.au</p>
  </div>
  <div style="background:#fff;padding:36px;border-radius:0 0 10px 10px;border:1px solid #ddd;border-top:none;">
    <table style="width:100%;border-collapse:collapse;">
      ${row('Name', `${d.first_name || ''} ${d.last_name || ''}`.trim())}
      ${row('Phone', d.phone)}
      ${row('Email', d.email)}
    </table>
    <div style="margin-top:24px;padding:18px;background:#f7faf8;border-radius:8px;border:1px solid #d0e5d8;">
      <strong style="color:#1B4D35;font-size:13px;text-transform:uppercase;letter-spacing:0.06em;">Message</strong>
      <p style="margin:10px 0 0;color:#444;line-height:1.7;">${d.message}</p>
    </div>
  </div>
  <p style="text-align:center;color:#999;font-size:12px;margin-top:16px;">This email was sent from the Spring 2 Health website contact form.</p>
</div>
</body></html>`;
}
