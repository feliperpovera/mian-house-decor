// Quote form -> Resend. Deployed as a Supabase Edge Function.
// Secrets (supabase secrets set ...): RESEND_API_KEY, MAIL_TO, MAIL_FROM
// MAIL_FROM must be on a domain verified in Resend (e.g. quotes@mianhousedecor.com).
// Until the domain is verified, use "MIAN <onboarding@resend.dev>" — Resend then only
// delivers to the email that owns the Resend account, so create it with MAIL_TO.

const ALLOWED = [
  "https://feliperpovera.github.io",
  "https://mianhousedecor.com",
  "https://www.mianhousedecor.com",
];

const cors = (origin: string) => ({
  "Access-Control-Allow-Origin": ALLOWED.includes(origin) ? origin : ALLOWED[0],
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "content-type",
  "Vary": "Origin",
});

const esc = (s: string) =>
  s.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]!));

Deno.serve(async (req) => {
  const origin = req.headers.get("origin") ?? "";
  const h = cors(origin);
  if (req.method === "OPTIONS") return new Response(null, { headers: h });
  if (req.method !== "POST") return new Response("Method not allowed", { status: 405, headers: h });
  if (!ALLOWED.includes(origin)) return new Response("Forbidden", { status: 403, headers: h });

  let d: Record<string, string>;
  try {
    const f = await req.formData();
    d = Object.fromEntries([...f.entries()].map(([k, v]) => [k, String(v).trim().slice(0, 2000)]));
  } catch {
    return Response.json({ success: false, message: "Bad request" }, { status: 400, headers: h });
  }

  if (d._honey) return Response.json({ success: true }, { headers: h }); // bot: pretend OK
  if (!d.name || !d.phone) {
    return Response.json({ success: false, message: "Name and phone are required" }, { status: 422, headers: h });
  }
  const email = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(d.email ?? "") ? d.email : undefined;

  const rows = [["Name", d.name], ["Phone", d.phone], ["Email", d.email || "—"],
                ["Service", d.service || "—"], ["Message", d.message || "—"]]
    .map(([k, v]) => `<tr><td style="padding:8px 14px;color:#7A5F44;font-weight:600">${k}</td>
                      <td style="padding:8px 14px">${esc(v).replace(/\n/g, "<br>")}</td></tr>`).join("");

  const r = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${Deno.env.get("RESEND_API_KEY")}`, "Content-Type": "application/json" },
    body: JSON.stringify({
      from: Deno.env.get("MAIL_FROM"),
      to: [Deno.env.get("MAIL_TO")],
      reply_to: email,
      subject: `New quote request — ${d.name} (${d.service || "general"})`,
      html: `<div style="font-family:Arial,sans-serif;color:#4A4238">
        <h2 style="color:#607e97;margin:0 0 12px">New quote request</h2>
        <table style="border-collapse:collapse;background:#FFFCF4;border:1px solid #E7DCC4">${rows}</table>
        <p style="font-size:12px;color:#9A8E7E">Sent from the website quote form.</p></div>`,
      text: `New quote request\n\nName: ${d.name}\nPhone: ${d.phone}\nEmail: ${d.email || "-"}\nService: ${d.service || "-"}\nMessage: ${d.message || "-"}`,
    }),
  });

  if (!r.ok) {
    console.error("resend", r.status, await r.text());
    return Response.json({ success: false, message: "Email failed" }, { status: 502, headers: h });
  }
  return Response.json({ success: true }, { headers: h });
});
