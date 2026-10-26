#!/usr/bin/env python3
"""Build the service and area landing pages from index.html.

Header, footer, sticky bar, dock, GTM and the stylesheet are lifted from
index.html so the pages never drift from the home page. Run after editing
index.html or the copy below:  python3 tools/build_pages.py
"""
import html, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://mianhousedecor.com"
GBP = "https://www.google.com/maps?cid=2190092133138331979"
PHONE_HREF = "tel:+17863488650"
SMS_HREF = "sms:+17863488650?&amp;body=Hi%20MIAN%20House%20%26%20Decor%2C%20I%27d%20like%20a%20free%20quote."
WA_HREF = "https://wa.me/17863488650?text=Hi%20MIAN%20House%20%26%20Decor%2C%20I%27d%20like%20a%20free%20quote."

src = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()


def block(start, end):
    i = src.index(start)
    return src[i:src.index(end, i) + len(end)]


def rootify(fragment):
    """In-page anchors and relative assets must point back to the home page."""
    fragment = re.sub(r'href="#top"', 'href="/"', fragment)
    fragment = re.sub(r'href="#([a-z]+)"', r'href="/#\1"', fragment)
    return fragment.replace('src="assets/', 'src="/assets/')


GTM_HEAD = block("<!-- Google Tag Manager -->", "<!-- End Google Tag Manager -->")
GTM_BODY = block("<!-- Google Tag Manager (noscript) -->", "<!-- End Google Tag Manager (noscript) -->")
HEADER = rootify(block('<header class="hdr"', "</header>"))
FOOTER = rootify(block('<footer class="ftr">', "</footer>"))
MBAR = rootify(block('<nav class="mbar"', "</nav>"))
DOCK = rootify(block('<div class="dock" id="dock">', "</div>"))
ICONS = re.search(r'(<link rel="icon"[\s\S]*?<meta name="theme-color"[^>]*>)', src).group(1)
FONTS = re.search(r'(<link rel="preconnect"[\s\S]*?display=swap" rel="stylesheet">)', src).group(1)
SVG_SMS = re.search(r'data-cta="sms">\s*(<svg[\s\S]*?</svg>)', src).group(1)
SVG_TEL = re.search(r'href="tel:\+17863488650" data-cta="call">\s*(<svg[\s\S]*?</svg>)', src).group(1)
SVG_WA = re.search(r'data-cta="whatsapp">\s*(<svg[\s\S]*?</svg>)', src).group(1)

EXTRA_CSS = """
/* ═══ landing pages ═══ */
.crumbs{font-size:.78rem;color:var(--ink-3);margin-bottom:18px}
.crumbs a{color:var(--marina-d);text-decoration:none}
.crumbs a:hover{text-decoration:underline}
.page-hero h1{font-style:normal}
.prose{max-width:720px}
.prose h2{font-size:clamp(1.9rem,3.6vw,2.6rem);color:var(--walnut-d);margin:0 0 16px}
.prose h3{font-size:1.45rem;color:var(--walnut-d);margin:26px 0 8px}
.prose p{color:var(--ink-2);margin:0 0 14px}
.prose ul{margin:0 0 16px;padding-left:20px;color:var(--ink-2)}
.prose li{margin:6px 0}
.prose li b{color:var(--walnut-d);font-weight:500}
.split{display:grid;grid-template-columns:1.15fr .85fr;gap:clamp(30px,5vw,64px);align-items:start}
.split__img img{width:100%;border-radius:var(--r-l);aspect-ratio:4/5;object-fit:cover;box-shadow:var(--shadow-m)}
.steps{list-style:none;padding:0;margin:8px 0 0;display:grid;grid-template-columns:repeat(4,1fr);gap:16px;counter-reset:s}
.steps li{background:var(--paper);border:1px solid var(--line);border-radius:var(--r);padding:22px 20px;counter-increment:s}
.steps li::before{content:counter(s);display:grid;place-items:center;width:34px;height:34px;border-radius:50%;background:var(--sunlight);color:var(--walnut-d);font-family:"Cormorant Garamond",serif;font-weight:600;font-size:1.15rem;margin-bottom:12px}
.steps b{display:block;color:var(--walnut-d);font-weight:500;margin-bottom:4px}
.steps span{font-size:.88rem;color:var(--ink-2)}
.faq{max-width:780px;margin-inline:auto}
.faq details{border-bottom:1px solid var(--line);padding:18px 4px}
.faq summary{cursor:pointer;list-style:none;font-family:"Cormorant Garamond",serif;font-size:1.3rem;font-weight:600;color:var(--walnut-d);display:flex;justify-content:space-between;gap:16px}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";color:var(--marina);font-family:Montserrat,sans-serif;font-weight:300}
.faq details[open] summary::after{content:"–"}
.faq details p{margin:10px 0 0;color:var(--ink-2)}
.chips{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px}
.chips a{padding:9px 18px;border:1px solid var(--marina-l);border-radius:100px;color:var(--marina-d);text-decoration:none;font-size:.86rem;background:var(--paper)}
.chips a:hover{background:var(--marina);color:#fff;border-color:var(--marina)}
.cta-row{display:flex;flex-wrap:wrap;gap:12px;justify-content:center;margin-top:30px}
@media (max-width:940px){.split{grid-template-columns:1fr}.steps{grid-template-columns:1fr 1fr}}
@media (max-width:560px){.steps{grid-template-columns:1fr}}
"""

css = re.search(r"<style>([\s\S]*?)</style>", src).group(1)
os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
open(os.path.join(ROOT, "assets", "site.css"), "w", encoding="utf-8").write(css.strip() + "\n" + EXTRA_CSS)

# Verbatim excerpts from the Google Business Profile (… marks omitted text). Never paraphrase.
REVIEWS = [
    ("Diane Weiss", "…she came to measure my sofa and discuss what I wanted to do. Came back a few days later with lots of swatches to choose from. I made a selection and a week later I had my sofa! … The whole thing in two weeks! Amazing!!"),
    ("Eli Martinez Cedrez", "From the initial consultation, to fabric selection, and the final delivery, they were communicative, friendly, and very accommodating. They did an incredible job reupholstering my Bernhardt headboard which was not an easy job."),
    ("Joseph Khakshouri", "Their attention to detail, refined aesthetic, and thoughtful approach to design truly stand out. … Beyond their beautiful work, they are professional, reliable, and bring great energy into the environment."),
]

SERVICES = [("Upholstery &amp; Reupholstery", "/upholstery/"), ("Custom Drapery", "/drapery/"), ("Commercial Upholstery", "/commercial/")]
AREAS = [("Coral Gables", "coral-gables"), ("Doral", "doral"), ("Brickell", "brickell"),
         ("Miami Beach", "miami-beach"), ("Kendall", "kendall"), ("North Miami", "north-miami")]

# ─────────────────────────── page content ───────────────────────────
PAGES = [
  dict(
    path="upholstery", kind="service", service="Furniture reupholstery and custom upholstery",
    title="Furniture Reupholstery in Miami | Sofas, Chairs &amp; Headboards | MIAN",
    desc="Furniture reupholstery and custom upholstery in Miami: sofas, sectionals, dining chairs, headboards and antiques. Free pickup, free quote in 24h. Se habla español.",
    eyebrow="Upholstery · Miami-Dade",
    h1="Furniture Reupholstery &amp; Custom Upholstery in Miami",
    lede="Keep the sofa, chair or headboard you love — we rebuild it with new foam and new fabric in our Miami workshop. Free pickup, a free quote in 24 hours, and service in English or Spanish.",
    hero_img=("tufted-settee.jpg", "Tufted wingback settee being reupholstered in the MIAN workshop in Miami"),
    body="""
<h2>Reupholstery that brings good furniture back</h2>
<p>A well-built frame outlasts its fabric by decades. Reupholstering keeps that frame and replaces everything that wears out: the fabric, the foam and padding, and — where they need it — the springs and webbing. You end up with a piece that fits your room and your taste, built to last another long run.</p>
<p>Every piece is measured, cut and sewn in our own workshop at 1 NW 62nd St in Miami. You talk directly to the people doing the work, from the first photo to delivery.</p>
<h3>What we reupholster</h3>
<ul>
  <li><b>Sofas and sectionals</b> — including modular and oversized pieces</li>
  <li><b>Dining chairs</b> — single chairs or full sets</li>
  <li><b>Headboards and beds</b> — tufted, channelled or plain</li>
  <li><b>Armchairs, wingbacks and settees</b></li>
  <li><b>Antique and vintage pieces</b> worth preserving</li>
  <li><b>Ottomans, benches and cushions</b>, indoor and outdoor</li>
</ul>
<h3>Fabrics for Miami homes</h3>
<p>We help you choose for how the piece will be used: performance fabrics for kids and pets, outdoor-rated textiles for patios and sun, and linen, velvet, bouclé or leather-look options for living rooms. We bring swatches to you so you can see them in your own light.</p>
""",
    steps=[("Send a photo", "Text or WhatsApp a photo of the piece. You get a free quote within 24 hours."),
           ("Measure &amp; choose", "We measure and bring fabric swatches so you can choose at home."),
           ("Free pickup", "We collect the piece and rebuild it in our Miami workshop."),
           ("Delivery", "Your finished piece comes back, ready to use.")],
    gallery=[("boucle-armchair.jpg", "Bouclé armchair with a dark wood frame, fully reupholstered"),
             ("dining-chairs.jpg", "Dining chairs reupholstered in textured grey fabric in Miami"),
             ("blue-velvet-sofa.jpg", "Blue velvet sofa upholstered in the MIAN workshop")],
    faq=[("Is it worth reupholstering a sofa instead of buying a new one?",
          "If the frame is solid — common in older and better-made furniture — reupholstering usually gives you a stronger piece than a new one at the same price, in exactly the fabric you want. If the frame is broken or poorly built, we will tell you honestly."),
         ("How much does reupholstery cost in Miami?",
          "It depends on the size of the piece, the fabric and how much foam or spring work it needs. Send us a photo by text or WhatsApp and we will send a free quote within 24 hours."),
         ("How long does reupholstery take?",
          "It depends on the piece and on fabric availability; we give you a date with the quote. One recent client had her sofa back two weeks after our first visit."),
         ("Do you pick up and deliver?",
          "Yes. Pickup is free across Miami-Dade, and we deliver the finished piece back to you."),
         ("Do you come to measure and show fabrics?",
          "Yes. We measure the piece and bring swatches so you can choose fabrics at home."),
         ("¿Hablan español?",
          "Sí. Atendemos en español e inglés, desde la cotización hasta la entrega.")],
  ),
  dict(
    path="drapery", kind="service", service="Custom drapes and curtains",
    title="Custom Drapes in Miami | Euro &amp; Pinch Pleat Drapery | MIAN",
    desc="Custom drapes made to measure in Miami: euro pleat, pinch pleat, sheer, blackout &amp; outdoor drapery, measured and installed by us. Free quote in 24h.",
    eyebrow="Drapery · Miami-Dade",
    h1="Custom Drapes in Miami, Made to Measure",
    lede="Euro pleat and pinch pleat drapes, sheers and blackout curtains sewn in our Miami workshop — for tall windows, sliding doors and covered patios. Measured and installed by us. Free quote in 24 hours.",
    hero_img=("work-curtains.jpg", "Made-to-measure ivory drapery on a tall arched window in Miami"),
    body="""
<h2>Custom drapes made for your windows, not a catalogue size</h2>
<p>Ready-made curtains rarely fit Miami windows: tall living-room glass, arched windows, sliding doors and wide patio openings. We measure each opening and sew the drapery to size in our own workshop, so it hangs straight, clears the floor the way you want and closes properly. Then we install it.</p>
<p>You talk directly to the people who measure, sew and hang your drapes — in English or Spanish — from the first photo to the day they go up.</p>

<h2>Drapery styles we make</h2>
<p>The heading — how the fabric is gathered at the top — sets the look of a drape more than anything else. These are the styles we make most often in Miami homes.</p>
<h3>Euro pleat drapes</h3>
<p>Euro pleats are gathered and tacked right at the top edge, so each pleat fans out into soft, even folds below. The result is tailored but relaxed, and it suits contemporary rooms, condos and floor-to-ceiling glass where you want clean lines.</p>
<h3>Pinch pleat and pleated drapes</h3>
<p>Classic pinch pleats are stitched a few inches below the top, giving crisp, structured folds and a fuller drape. They work well in traditional and transitional rooms, dining rooms and bedrooms, and on large living-room windows.</p>
<h3>Sheer drapes</h3>
<p>Sheers soften glare and add daytime privacy while letting light through — a good fit for high-rise windows and sliding doors. They can be layered with a lined or blackout drape on a second track for full control.</p>
<h3>Blackout and lined drapes</h3>
<p>Blackout-lined drapery darkens bedrooms and media rooms. A standard lining protects the face fabric from Miami sun, improves privacy and helps the drape hang with more body.</p>
<h3>Outdoor drapes</h3>
<p>For covered patios, terraces and balconies we sew drapes in outdoor-rated fabrics that handle sun and humidity — often paired with <a href="/upholstery/">reupholstered outdoor cushions</a> in a coordinating fabric.</p>

<h2>Fabrics and lining for Miami light</h2>
<p>Light, heat and humidity matter here. We help you choose for each room:</p>
<ul>
  <li><b>Sheers</b> to soften glare without darkening the room</li>
  <li><b>Lined drapes</b> to protect fabric from fading and add privacy in sunny rooms</li>
  <li><b>Blackout lining</b> for bedrooms, nurseries and media rooms</li>
  <li><b>Outdoor-rated textiles</b> for patios, terraces and humid spaces</li>
  <li><b>Coordinating cushions and pillows</b> sewn in the same fabric as your drapes</li>
</ul>
<p>We bring samples to your home so you can see each option against your own windows, walls and furniture before anything is cut.</p>

<h2>Custom drapes across Miami</h2>
<p>We measure, make and install drapery throughout Miami-Dade:</p>
<ul>
  <li><a href="/areas/brickell/"><b>Brickell</b></a> — sheers and blackout drapery for high-rise, floor-to-ceiling glass</li>
  <li><a href="/areas/miami-beach/"><b>Miami Beach</b></a> — lined drapes for sun-facing rooms and outdoor curtains for terraces</li>
  <li><a href="/areas/coral-gables/"><b>Coral Gables</b></a> — lined drapery for large living-room windows</li>
  <li><a href="/areas/kendall/"><b>Kendall</b></a> — custom curtains for bedrooms and living rooms</li>
  <li><a href="/areas/doral/"><b>Doral</b></a> — blackout curtains for bedrooms</li>
  <li><a href="/areas/north-miami/"><b>North Miami</b></a> — close to our workshop at 1 NW 62nd St</li>
</ul>
<p>Updating more than the windows? We also do <a href="/upholstery/">furniture reupholstery and custom upholstery</a>, and <a href="/commercial/">drapery and seating for restaurants, hotels and event spaces</a>.</p>
""",
    steps=[("Send a photo", "Share photos of the windows. You get a free quote within 24 hours."),
           ("Measure", "We measure every opening and help you choose fabric, lining and heading."),
           ("Made to size", "Your drapery is cut and sewn in our Miami workshop."),
           ("Installed", "We hang your drapes, made to fit your windows.")],
    gallery=[("drapery-pleated.jpg", "Pleated drapery framing a tall window in a Miami home"),
             ("patio-drapery.jpg", "Outdoor drapery and reupholstered seating on a Miami patio"),
             ("work-curtains.jpg", "Ivory drapery on an arched window")],
    faq=[("How much do custom drapes cost in Miami?",
          "It depends on window size, fabric, lining and heading style. Send us photos of your windows and we will send a free quote within 24 hours."),
         ("What is the difference between euro pleat and pinch pleat drapes?",
          "Euro pleats are tacked at the very top edge and fan out into soft folds, for a cleaner, more contemporary look. Pinch pleats are stitched a few inches below the top, giving crisper, more structured folds and a more traditional look."),
         ("Do you measure and install the drapes?",
          "Yes. We measure each opening so the drapery is sewn to fit, and we install it in your home."),
         ("Should my curtains be lined?",
          "In Miami, usually yes for sunny rooms: lining protects the fabric from fading and improves privacy. Sheers are the exception, when you want light to pass through."),
         ("Can you make blackout curtains?",
          "Yes. Blackout-lined drapery works well for bedrooms and media rooms."),
         ("Do you make outdoor curtains?",
          "Yes, in outdoor-rated fabrics for covered patios and terraces."),
         ("Can you make cushions or pillows to match my drapes?",
          "Yes. We sew coordinating cushions and pillows in the same fabric as your drapery."),
         ("Which areas do you serve?",
          "All of Miami-Dade, including Brickell, Miami Beach, Coral Gables, Kendall, Doral and North Miami."),
         ("¿Hablan español?",
          "Sí. Atendemos en español e inglés.")],
  ),
  dict(
    path="commercial", kind="service", service="Commercial upholstery",
    title="Commercial Upholstery in Miami | Restaurants, Hotels &amp; Offices | MIAN",
    desc="Commercial upholstery in Miami-Dade: restaurant banquettes and booths, dining chairs, hotel and office seating, marine cushions. Contract-grade fabrics. Free quote in 24h.",
    eyebrow="Commercial · Miami-Dade",
    h1="Commercial Upholstery in Miami: Restaurants, Hotels &amp; Offices",
    lede="We upholster banquettes, booths, dining chairs and lounge seating with contract-grade fabrics and durable foam, made in our Miami workshop. Free quote in 24 hours.",
    hero_img=("work-commercial.jpg", "Restaurant banquette and leather dining chairs upholstered for a Miami venue"),
    body="""
<h2>Seating built for heavy daily use</h2>
<p>Restaurant and hospitality seating takes more wear in a month than a home sofa does in a year. We rebuild it with contract-grade fabrics and durable foam so it holds its shape and cleans easily — and we make it in our own workshop in Miami, so you deal directly with the people doing the work.</p>
<h3>What we upholster for businesses</h3>
<ul>
  <li><b>Restaurant banquettes and booths</b></li>
  <li><b>Dining and bar chairs</b> — matched sets</li>
  <li><b>Lounge and lobby seating</b> for hotels and offices</li>
  <li><b>Headboards and soft furnishings</b> for hospitality</li>
  <li><b>Marine and outdoor cushions</b> for yachts and terraces</li>
  <li><b>Custom drapery</b> for dining rooms and event spaces</li>
</ul>
<h3>Working around your business</h3>
<p>Tell us your schedule and we plan pickup and delivery around it, so your space spends as little time as possible without its seating. You get a written quote and a date before any work starts.</p>
""",
    steps=[("Send photos", "Photos and a rough count of pieces. Free quote within 24 hours."),
           ("Site visit", "We measure on site and help choose contract-grade fabrics."),
           ("Workshop", "Everything is rebuilt in our Miami workshop."),
           ("Delivery", "Pieces return on the agreed date, ready for service.")],
    gallery=[("work-commercial.jpg", "Restaurant banquette upholstered in brown leather in Miami"),
             ("yacht-cushions.jpg", "Navy striped outdoor cushions made for a yacht at a Miami marina"),
             ("dining-chairs.jpg", "Set of upholstered dining chairs")],
    faq=[("What kinds of businesses do you work with?",
          "Restaurants, hotels, offices and boats across Miami-Dade — anywhere with seating that takes heavy use."),
         ("Do you use contract-grade fabrics?",
          "Yes. For commercial seating we recommend contract-grade and performance fabrics with durable foam."),
         ("Can you work around our opening hours?",
          "Tell us your schedule and we plan pickup and delivery around it."),
         ("How do I get a quote?",
          "Send photos and an approximate number of pieces by text, WhatsApp or the form. You get a free quote within 24 hours."),
         ("¿Hablan español?",
          "Sí. Atendemos en español e inglés.")],
  ),
]

AREA_COPY = {
  "coral-gables": ("Coral Gables",
    "Coral Gables homes are full of furniture worth keeping: family pieces, antiques and well-made sofas that only need new fabric. Reupholstery lets you keep the frame and the history while updating the look to suit the room.",
    "Popular here: reupholstering antiques and heirloom chairs, dining sets, and lined drapery for large living-room windows."),
  "doral": ("Doral",
    "Doral has a mix of family homes and offices. At home, that usually means sofas and dining chairs that need fabrics able to handle kids and pets; for businesses, durable seating for offices and restaurants.",
    "Popular here: performance-fabric sofas and dining chairs, office and restaurant seating, and blackout curtains for bedrooms. Atendemos en español."),
  "brickell": ("Brickell",
    "Brickell condos have floor-to-ceiling glass and strong afternoon sun. Sheers and lined drapery made to measure soften glare and protect furniture, while sectionals and modular sofas get a second life with new foam and fabric.",
    "Popular here: sheers and blackout drapery for high-rise windows, sectional reupholstery, and custom cushions for balconies. Let us know your building's delivery rules and we plan around them."),
  "miami-beach": ("Miami Beach",
    "Salt air, sun and humidity are hard on fabric in Miami Beach. Outdoor-rated and performance textiles last much longer on terraces, balconies and boats, and lined drapery keeps sun-facing rooms from fading.",
    "Popular here: outdoor and marine cushions, terrace curtains, and hospitality seating for hotels and restaurants."),
  "kendall": ("Kendall",
    "Kendall family homes get daily use from every sofa and dining chair. Reupholstering in a performance fabric brings back comfortable, easy-to-clean seating without replacing furniture you already like.",
    "Popular here: family-room sofas and sectionals, full dining-chair sets, and custom curtains for bedrooms and living rooms."),
  "north-miami": ("North Miami",
    "North Miami is close to our workshop at 1 NW 62nd St, which makes pickup and delivery especially easy. Mid-century and vintage pieces are common here and are often worth reupholstering rather than replacing.",
    "Popular here: vintage and mid-century chair reupholstery, sofas, and made-to-measure drapery."),
}
# Per-area overrides (CTR tests on queries an area already ranks for).
AREA_META = {
  "north-miami": dict(
    title="Custom Upholstery in North Miami, FL | Free Quote 24h | MIAN",
    desc="Custom upholstery &amp; reupholstery in North Miami: sofas, chairs, headboards &amp; drapes. Free pickup and a free quote in 24h from our nearby workshop.",
    h1="Custom Upholstery &amp; Reupholstery in North Miami"),
}
AREA_IMG = {"coral-gables": "boucle-armchair.jpg", "doral": "dining-chairs.jpg", "brickell": "drapery-pleated.jpg",
            "miami-beach": "yacht-cushions.jpg", "kendall": "blue-velvet-sofa.jpg", "north-miami": "tufted-settee.jpg"}
for slug, (name, p1, p2) in AREA_COPY.items():
    PAGES.append(dict(
        path=f"areas/{slug}", kind="area", area=name,
        title=f"Upholstery &amp; Reupholstery in {name}, FL | MIAN House &amp; Decor",
        desc=f"Furniture reupholstery, custom upholstery and made-to-measure drapery in {name}, FL. Free pickup, free quote in 24h, se habla español. (786) 348-8650.",
        eyebrow=f"Serving {name}",
        h1=f"Upholstery &amp; Reupholstery in {name}",
        lede=f"Reupholstery, custom upholstery and made-to-measure drapery for homes and businesses in {name}. Free pickup and a free quote within 24 hours.",
        hero_img=(AREA_IMG[slug], f"Furniture upholstered by MIAN House &amp; Decor for a client in {name}"),
        body=f"""
<h2>Upholstery and drapery for {name}</h2>
<p>{p1}</p>
<p>{p2}</p>
<h3>Services in {name}</h3>
<ul>
  <li><a href="/upholstery/"><b>Furniture reupholstery &amp; custom upholstery</b></a> — sofas, sectionals, dining chairs, headboards and antiques</li>
  <li><a href="/drapery/"><b>Custom drapery &amp; curtains</b></a> — pleated drapes, sheers, blackout and outdoor curtains</li>
  <li><a href="/commercial/"><b>Commercial upholstery</b></a> — restaurants, hotels, offices and boats</li>
</ul>
<p>Everything is made in our workshop at 1 NW 62nd St, Miami. Pickup is free, and you get a written quote within 24 hours of sending us a photo.</p>
""",
        steps=None, gallery=None,
        faq=[(f"Do you pick up furniture in {name}?", f"Yes. Pickup is free in {name} and across Miami-Dade."),
             ("How do I get a quote?", "Send a photo of the piece by text, WhatsApp or the form. You get a free quote within 24 hours."),
             ("¿Hablan español?", "Sí. Atendemos en español e inglés.")],
    ))
    PAGES[-1].update(AREA_META.get(slug, {}))

# ─────────────────────────── rendering ───────────────────────────

def esc_json(obj):
    return json.dumps(obj, ensure_ascii=False, indent=1).replace("</", "<\\/")


def plain(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s))


def render(pg):
    url = f"{SITE}/{pg['path']}/"
    img, img_alt = pg["hero_img"]
    crumbs = [("Home", "/")]
    if pg["kind"] == "area":
        crumbs += [("Areas", "/#about"), (pg["area"], f"/{pg['path']}/")]
    else:
        crumbs += [(plain(pg["h1"]).split(" in Miami")[0].split(":")[0], f"/{pg['path']}/")]

    schema = [
      {"@context": "https://schema.org", "@type": "BreadcrumbList",
       "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u}
                           for i, (n, u) in enumerate(crumbs)]},
      {"@context": "https://schema.org", "@type": "Service",
       "name": plain(pg["h1"]), "description": plain(pg["desc"]), "url": url,
       "serviceType": pg.get("service", "Upholstery and drapery"),
       "areaServed": pg.get("area", "Miami-Dade County"),
       "provider": {"@type": "HomeAndConstructionBusiness", "@id": f"{SITE}/#business", "name": "MIAN House & Decor",
                    "telephone": "+1-786-348-8650", "url": f"{SITE}/",
                    "address": {"@type": "PostalAddress", "streetAddress": "1 NW 62nd St, Unit 8", "addressLocality": "Miami",
                                "addressRegion": "FL", "postalCode": "33150", "addressCountry": "US"}}},
      {"@context": "https://schema.org", "@type": "FAQPage",
       "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pg["faq"]]},
    ]

    steps = ""
    if pg.get("steps"):
        steps = '<section class="section" style="padding-top:0"><div class="wrap"><div class="head head--c rv"><h2>How it <span class="hl">works</span></h2></div><ol class="steps">' + \
            "".join(f"<li class=\"rv\"><b>{t}</b><span>{d}</span></li>" for t, d in pg["steps"]) + "</ol></div></section>"

    gallery = ""
    if pg.get("gallery"):
        gallery = '<section class="section linen"><div class="wrap"><div class="head head--c rv"><h2>Recent <span class="hl">work</span></h2></div><div class="work">' + \
            "".join(f'<figure class="rv{" rv-d"+str(i) if i else ""}"><img src="/assets/img/{f}" alt="{a}" loading="lazy" width="825" height="1100"></figure>'
                    for i, (f, a) in enumerate(pg["gallery"])) + "</div></div></section>"

    reviews = '<section class="section"><div class="wrap"><div class="head head--c rv"><h2>What Miami <span class="hl">says</span></h2><p class="lede">4.7 out of 5 from 12 reviews on Google.</p></div><div class="revs">' + \
        "".join(f'<article class="rev rv{" rv-d"+str(i) if i else ""}"><div class="rev__stars" aria-label="5 out of 5 stars">★★★★★</div><p class="rev__q">“{html.escape(t)}”</p><p class="rev__by"><b>{n}</b>Google review</p></article>'
                for i, (n, t) in enumerate(REVIEWS)) + \
        f'</div><div class="revs__cta"><a class="btn btn--ghost" href="{GBP}" target="_blank" rel="noopener">Read all reviews on Google</a></div></div></section>'

    faq = '<section class="section linen"><div class="wrap"><div class="head head--c rv"><h2>Frequently asked <span class="hl">questions</span></h2></div><div class="faq">' + \
        "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in pg["faq"]) + "</div></div></section>"

    others = SERVICES if pg["kind"] == "area" else [s for s in SERVICES if s[1] != f"/{pg['path']}/"]
    nearby = '<section class="section" style="padding-top:0"><div class="wrap"><div class="prose"><h2>More from MIAN</h2></div><div class="chips">' + \
        "".join(f'<a href="{u}">{n}</a>' for n, u in others) + \
        "".join(f'<a href="/areas/{s}/">{n}</a>' for n, s in AREAS if f"areas/{s}" != pg["path"]) + "</div></div></section>"

    cta = f'''<section class="section express"><div class="wrap"><div class="express__in rv">
<h2>Get your free quote <em>in 24 hours</em></h2>
<p>Send a photo of the piece or the windows — we reply within one business day. Se habla español.</p>
<div class="cta-row">
<a class="btn btn--lg btn--sun" href="{SMS_HREF}" data-cta="sms">{SVG_SMS} Text us</a>
<a class="btn btn--lg btn--onBlue" href="{PHONE_HREF}" data-cta="call">{SVG_TEL} (786) 348-8650</a>
<a class="btn btn--lg btn--onBlue" href="{WA_HREF}" target="_blank" rel="noopener" data-cta="whatsapp">{SVG_WA} WhatsApp</a>
<a class="btn btn--lg btn--onBlue" href="/#contact" data-cta="quote">Quote form</a>
</div></div></div></section>'''

    crumb_html = " · ".join(f'<a href="{u}">{n}</a>' if i < len(crumbs) - 1 else f"<span>{n}</span>" for i, (n, u) in enumerate(crumbs))
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
{GTM_HEAD}
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{pg["title"]}</title>
<meta name="description" content="{pg["desc"]}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{pg["title"]}">
<meta property="og:description" content="{pg["desc"]}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/{img}">
<meta property="og:type" content="website">
{ICONS}
{FONTS}
<link rel="stylesheet" href="/assets/site.css">
<script>document.documentElement.classList.add('js')</script>
<script type="application/ld+json">
{esc_json(schema)}
</script>
</head>
<body>
{GTM_BODY}
{HEADER}
<main id="main">
<section class="hero linen page-hero" id="top">
  <div class="wrap">
    <div class="hero__grid">
      <div class="hero__copy">
        <nav class="crumbs" aria-label="Breadcrumb">{crumb_html}</nav>
        <p class="eyebrow">{pg["eyebrow"]}</p>
        <h1>{pg["h1"]}</h1>
        <p class="hero__sub">{pg["lede"]}</p>
        <div class="hero__cta">
          <a class="btn btn--lg" href="{SMS_HREF}" data-cta="sms">{SVG_SMS} Text us</a>
          <a class="btn btn--lg btn--sun btn--serif" href="/#contact" data-cta="quote">Free Quote</a>
          <a class="btn btn--lg btn--ghost" href="{PHONE_HREF}" data-cta="call">{SVG_TEL} (786) 348-8650</a>
        </div>
        <div class="hero__trust">
          <a class="hero__rating" href="{GBP}" target="_blank" rel="noopener"><span class="stars">★★★★★</span> <b>4.7</b> · 12 Google reviews</a>
          <span><b>Free pickup</b> in Miami-Dade</span>
          <span><b>Free quote</b> in 24h</span>
        </div>
      </div>
      <div class="oval"><div class="oval__img"><img src="/assets/img/{img}" alt="{img_alt}" fetchpriority="high"></div></div>
    </div>
  </div>
</section>
<section class="section"><div class="wrap"><div class="prose rv">{pg["body"]}</div></div></section>
{steps}
{gallery}
{reviews}
{faq}
{nearby}
{cta}
</main>
{FOOTER}
{MBAR}
{DOCK}
<script src="/assets/site.js" defer></script>
</body>
</html>
'''


# sitemap lastmod: kept from the existing sitemap; bumped only for pages whose HTML changed.
# The home page is not built here — bump its lastmod in sitemap.xml by hand when editing index.html.
from datetime import date
SITEMAP = os.path.join(ROOT, "sitemap.xml")
lastmod = dict(re.findall(r"<loc>([^<]+)</loc><lastmod>([^<]+)</lastmod>", open(SITEMAP).read())) if os.path.exists(SITEMAP) else {}

for pg in PAGES:
    out = os.path.join(ROOT, pg["path"], "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    page = render(pg)
    url = f"{SITE}/{pg['path']}/"
    if not os.path.exists(out) or open(out, encoding="utf-8").read() != page:
        lastmod[url] = str(date.today())
    open(out, "w", encoding="utf-8").write(page)
    print("built", "/" + pg["path"] + "/")

urls = [f"{SITE}/"] + [f"{SITE}/{pg['path']}/" for pg in PAGES]
open(SITEMAP, "w").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    "".join(f"  <url><loc>{u}</loc><lastmod>{lastmod.get(u, date.today())}</lastmod></url>\n" for u in urls) + "</urlset>\n")
print("sitemap:", len(urls), "urls")
