// MIAN quote form -> Resend. Cloudflare Worker (module syntax).
// Secret:    RESEND_API_KEY            (Settings > Variables and Secrets > Secret)
// Variables: MAIL_TO   = mianhousedecor@gmail.com
//            MAIL_FROM = MIAN House & Decor <quotes@mianhousedecor.com>

const ALLOWED = [
  "https://feliperpovera.github.io",
  "https://mianhousedecor.com",
  "https://www.mianhousedecor.com",
];

const cors = (origin) => ({
  "Access-Control-Allow-Origin": ALLOWED.includes(origin) ? origin : ALLOWED[0],
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "content-type",
  "Vary": "Origin",
});

const esc = (s) => s.replace(/[&<>"']/g, (c) =>
  ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

const json = (body, status, headers) =>
  new Response(JSON.stringify(body), { status, headers: { ...headers, "Content-Type": "application/json" } });

export default {
  async fetch(req, env) {
    const origin = req.headers.get("origin") || "";
    const h = cors(origin);
    if (req.method === "OPTIONS") return new Response(null, { headers: h });
    if (req.method !== "POST") return json({ success: false, message: "Method not allowed" }, 405, h);
    if (!ALLOWED.includes(origin)) return json({ success: false, message: "Forbidden" }, 403, h);

    let d;
    try {
      const f = await req.formData();
      d = Object.fromEntries([...f.entries()].map(([k, v]) => [k, String(v).trim().slice(0, 2000)]));
    } catch {
      return json({ success: false, message: "Bad request" }, 400, h);
    }

    if (d._honey) return json({ success: true }, 200, h); // bot: pretend OK
    if (!d.name || !d.phone) return json({ success: false, message: "Name and phone are required" }, 422, h);
    const email = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(d.email || "") ? d.email : undefined;

    const rows = [["Name", d.name], ["Phone", d.phone], ["Email", d.email || "—"],
                  ["Service", d.service || "—"], ["Message", d.message || "—"]]
      .map(([k, v]) => `<tr><td style="padding:8px 14px;color:#7A5F44;font-weight:600;vertical-align:top">${k}</td>
                        <td style="padding:8px 14px">${esc(v).replace(/\n/g, "<br>")}</td></tr>`).join("");

    const r = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: { Authorization: `Bearer ${env.RESEND_API_KEY}`, "Content-Type": "application/json" },
      body: JSON.stringify({
        from: env.MAIL_FROM,
        to: [env.MAIL_TO],
        reply_to: email,
        subject: `New quote request — ${d.name} (${d.service || "general"})`,
        html: `<div style="font-family:Arial,sans-serif;color:#4A4238">
          <h2 style="color:#607e97;margin:0 0 12px">New quote request</h2>
          <table style="border-collapse:collapse;background:#FFFCF4;border:1px solid #E7DCC4">${rows}</table>
          <p style="font-size:12px;color:#9A8E7E">Sent from the mianhousedecor.com quote form.</p></div>`,
        text: `New quote request\n\nName: ${d.name}\nPhone: ${d.phone}\nEmail: ${d.email || "-"}\nService: ${d.service || "-"}\nMessage: ${d.message || "-"}`,
      }),
    });

    if (!r.ok) {
      console.log("resend error", r.status, await r.text());
      return json({ success: false, message: "Email failed" }, 502, h);
    }
    return json({ success: true }, 200, h);
  },
};
