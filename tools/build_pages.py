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
CONTACT = rootify(block('<section class="section contact" id="contact">', "</section>"))
FORM_JS = "<script>(() => {\n  const $ = s => document.querySelector(s);\n  " + \
    re.search(r"(// Quote form[\s\S]*?)\n\}\)\(\);\n</script>", src).group(1) + "\n})();\n</script>"
FORM_PAGES = ("upholstery", "drapery", "commercial")

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
.tbl{width:100%;border-collapse:collapse;margin:0 0 22px;font-size:.92rem}
.tbl th,.tbl td{text-align:left;padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top;color:var(--ink-2)}
.tbl th{color:var(--walnut-d);font-weight:500}
.tbl td:first-child{white-space:nowrap}
.cta-row{display:flex;flex-wrap:wrap;gap:12px;justify-content:center;margin-top:30px}
@media (max-width:940px){.split{grid-template-columns:1fr}.steps{grid-template-columns:1fr 1fr}}
@media (max-width:560px){.steps{grid-template-columns:1fr}.tbl{font-size:.84rem}.tbl th,.tbl td{padding:8px 6px}.tbl td:first-child{white-space:normal}}
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
         ("Miami Beach", "miami-beach"), ("Kendall", "kendall"), ("North Miami", "north-miami"),
         ("North Miami Beach", "north-miami-beach"), ("Hialeah", "hialeah")]

# ─────────────────────────── page content ───────────────────────────
PAGES = [
  dict(
    path="upholstery", kind="service", service="Furniture reupholstery and custom upholstery",
    title="Furniture Reupholstery Miami | Sofas &amp; Chairs | MIAN",
    desc="Furniture reupholstery in Miami: sofas, sectionals, dining chairs, headboards and antiques. Free quote in 24h. Se habla español.",
    eyebrow="Upholstery · Miami-Dade",
    h1="Furniture Reupholstery in Miami", crumb="Upholstery",
    lede="Keep the sofa, chair or headboard you love — we rebuild it with new foam and new fabric in our Miami workshop. Pickup and delivery available, a free quote in 24 hours, and service in English or Spanish.",
    hero_img=("tufted-settee.jpg", "Tufted wingback settee being reupholstered in the MIAN workshop in Miami"),
    body="""
<h2>Reupholstery that brings good furniture back</h2>
<p>A well-built frame outlasts its fabric by decades. Reupholstering keeps that frame and replaces everything that wears out: the fabric, the foam and padding, and — where they need it — the springs and webbing. You end up with a piece that fits your room and your taste, built to last another long run.</p>
<p>Every piece is measured, cut and sewn in our own workshop at 1 NW 62nd St in Miami. You talk directly to the people doing the work, from the first photo to delivery.</p>
<h2>Sofa &amp; Couch Reupholstery</h2>
<p>Sofa reupholstery keeps the frame and replaces the fabric and foam, from a two-seat couch to a modular sectional. If you are looking for couch reupholstery near me, send a photo and we will tell you whether the frame is worth it. <a href="/upholstery/sofa-reupholstery-miami/">See sofa reupholstery in Miami</a>.</p>
<h2>Chair &amp; Dining Chair Upholstery</h2>
<p>Dining chairs, one chair or a full set, plus armchairs and wingbacks. For chair upholstery near me anywhere in Miami-Dade, send a photo of the chair and tell us how many you have. <a href="/upholstery/chair-reupholstery-miami/">See chair upholstery in Miami</a>.</p>
<h2>An upholstery shop near you in Miami-Dade</h2>
<p>If you are searching for reupholstery near me, you want a local shop that can see the piece. Ours is at 1 NW 62nd St, with pickup and delivery available across Miami-Dade, from <a href="/areas/north-miami/">North Miami</a> and <a href="/areas/hialeah/">Hialeah</a> to <a href="/areas/kendall/">Kendall</a> and <a href="/areas/miami-beach/">Miami Beach</a>.</p>
<h3>What we reupholster</h3>
<ul>
  <li><a href="/upholstery/sofa-reupholstery-miami/"><b>Sofas and sectionals</b></a> — including modular and oversized pieces</li>
  <li><a href="/upholstery/chair-reupholstery-miami/"><b>Dining chairs</b></a> — single chairs or full sets</li>
  <li><a href="/upholstery/headboard-upholstery-miami/"><b>Headboards and beds</b></a> — tufted, channelled or plain</li>
  <li><a href="/upholstery/leather-reupholstery-miami/"><b>Leather sofas and chairs</b></a></li>
  <li><b>Armchairs, wingbacks and settees</b></li>
  <li><b>Antique and vintage pieces</b> worth preserving</li>
  <li><b>Ottomans and benches</b>, plus <a href="/upholstery/custom-cushions-miami/"><b>custom cushions</b></a> for indoors and outdoors</li>
</ul>
<h3>Fabrics for Miami homes</h3>
<p>We help you choose for how the piece will be used: performance fabrics for kids and pets, outdoor-rated textiles for patios and sun, and linen, velvet, bouclé or leather-look options for living rooms. We bring swatches to you so you can see them in your own light.</p>
""",
    steps=[("Send a photo", "Text or WhatsApp a photo of the piece. You get a free quote within 24 hours."),
           ("Measure &amp; choose", "We measure and bring fabric swatches so you can choose at home."),
           ("Pickup", "We collect the piece and rebuild it in our Miami workshop."),
           ("Delivery", "Your finished piece comes back, ready to use.")],
    gallery=[("boucle-armchair.jpg", "Bouclé armchair with a dark wood frame, fully reupholstered"),
             ("dining-chairs.jpg", "Dining chairs reupholstered in textured grey fabric in Miami"),
             ("blue-velvet-sofa.jpg", "Blue velvet sofa upholstered in the MIAN workshop")],
    faq=[("Is it worth reupholstering a sofa instead of buying a new one?",
          "If the frame is solid — common in older and better-made furniture — reupholstering usually gives you a stronger piece than a new one at the same price, in exactly the fabric you want. If the frame is broken or poorly built, we will tell you honestly."),
         ("How much does reupholstery cost in Miami?",
          "It depends on the size of the piece, the fabric and how much foam or spring work it needs. Send us a photo by text or WhatsApp and we will send a free quote within 24 hours."),
         ("How long does reupholstery take?",
          "It depends on the piece and on fabric availability; we give you a date with the quote. One recent client had the sofa back two weeks after our first visit."),
         ("Do you do furniture repair?",
          "We repair what sits under the fabric: foam, springs and webbing. Send a photo of the damage and we will tell you what the piece needs."),
         ("Do you pick up and deliver?",
          "Yes. Pickup and delivery are available in Miami-Dade, and we bring the finished piece back to you."),
         ("Do you come to measure and show fabrics?",
          "Yes. We measure the piece and bring swatches so you can choose fabrics at home."),
         ("¿Hablan español?",
          "Sí. Atendemos en español e inglés, desde la cotización hasta la entrega.")],
  ),
  dict(
    path="drapery", kind="service", service="Custom drapes and curtains",
    title="Custom Drapes Miami | Made to Measure &amp; Installed | MIAN",
    desc="Drapes in Miami, sewn to measure in our own workshop: euro pleat, pinch pleat, sheer, blackout &amp; outdoor. We measure and install. Free quote in 24h.",
    eyebrow="Drapery · Miami-Dade",
    h1="Custom Drapes &amp; Curtains in Miami",
    lede="Custom drapes and custom curtains in Miami: euro pleat and pinch pleat drapes, sheers and blackouts sewn in our workshop for tall windows, sliding doors and covered patios. Made to measure curtains, installed by us. Free quote in 24 hours.",
    hero_img=("work-curtains.jpg", "Made-to-measure ivory drapery on a tall arched window in Miami"),
    body="""
<h2>Custom drapes in Miami, made for your windows — not a catalogue size</h2>
<p>Ready-made curtains rarely fit Miami windows: tall living-room glass, arched windows, sliding doors and wide patio openings. We measure each opening and sew the drapery to size in our own workshop, so it hangs straight, clears the floor the way you want and closes properly. Then we install it.</p>
<p>You talk directly to the people who measure, sew and hang your drapes — in English or Spanish — from the first photo to the day they go up.</p>

<h2>Drapery styles at a glance</h2>
<table class="tbl">
  <thead><tr><th>Style</th><th>Look</th><th>Good for</th></tr></thead>
  <tbody>
    <tr><td><a href="/drapery/euro-pleat-drapes-miami/">Euro pleat</a></td><td>Pleats tacked at the top edge, soft fanned folds</td><td>Condos, contemporary rooms, floor-to-ceiling glass</td></tr>
    <tr><td><a href="/drapery/pinch-pleat-drapes-miami/">Pinch pleat</a></td><td>Pleats stitched below the top, crisp structured folds</td><td>Traditional and transitional rooms, dining rooms, bedrooms</td></tr>
    <tr><td>Sheer</td><td>Light-filtering fabric, softens glare</td><td>High-rise windows, sliding doors, layering with a lined drape</td></tr>
    <tr><td><a href="/drapery/blackout-curtains-miami/">Blackout-lined</a></td><td>Any heading with a blackout lining</td><td>Bedrooms, nurseries, media rooms</td></tr>
    <tr><td><a href="/drapery/outdoor-curtains-miami/">Outdoor</a></td><td>Outdoor-rated fabric for sun and humidity</td><td>Covered patios, terraces, balconies</td></tr>
  </tbody>
</table>

<h2>Drapery styles we make</h2>
<p>The heading — how the fabric is gathered at the top — sets the look of a drape more than anything else. These are the styles we make most often in Miami homes.</p>
<h3>Euro pleat drapes</h3>
<p>Euro pleats are gathered and tacked right at the top edge, so each pleat fans out into soft, even folds below. The result is tailored but relaxed, and it suits contemporary rooms, condos and floor-to-ceiling glass where you want clean lines. <a href="/drapery/euro-pleat-drapes-miami/">More about euro pleat drapes in Miami</a>.</p>
<h3>Pinch pleat and pleated drapes</h3>
<p>Classic pinch pleats are stitched a few inches below the top, giving crisp, structured folds and a fuller drape. They work well in traditional and transitional rooms, dining rooms and bedrooms, and on large living-room windows. <a href="/drapery/pinch-pleat-drapes-miami/">More about pinch pleat drapes in Miami</a>.</p>
<h3>Sheer drapes</h3>
<p>Sheers soften glare and add daytime privacy while letting light through — a good fit for high-rise windows and sliding doors. They can be layered with a lined or blackout drape on a second track for full control.</p>
<h3>Blackout and lined drapes</h3>
<p>Blackout-lined drapery darkens bedrooms and media rooms. A standard lining protects the face fabric from Miami sun, improves privacy and helps the drape hang with more body. <a href="/drapery/blackout-curtains-miami/">More about blackout drapes in Miami</a>.</p>
<h3>Outdoor drapes</h3>
<p>For covered patios, terraces and balconies we sew drapes in outdoor-rated fabrics that handle sun and humidity — often paired with <a href="/upholstery/custom-cushions-miami/">custom outdoor cushions</a> in a coordinating fabric. <a href="/drapery/outdoor-curtains-miami/">More about outdoor curtains in Miami</a>.</p>

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

<h2>How we measure and install your drapes</h2>
<p>Drapes made to measure only look right if the measurements are taken for the way they will hang. At the visit we measure every opening and settle the details that change the result:</p>
<ul>
  <li><b>Mounting height</b> — just above the frame, or close to the ceiling to make the window feel taller</li>
  <li><b>Length</b> — just off the floor, touching it, or with a slight break, depending on the room and how often the drapes move</li>
  <li><b>Width and stack-back</b> — how far the drapery extends past the glass, so it can open fully without blocking the view or a sliding door</li>
  <li><b>Layers</b> — a single drape, or a sheer and a lined drape on separate tracks</li>
</ul>
<p>The drapery is then cut and sewn to those numbers in our Miami workshop, and we come back to hang it.</p>

<h2>What sets the price of custom drapes</h2>
<p>We don't publish a flat price, because two windows of the same width can need very different drapery. The quote depends on:</p>
<ul>
  <li><b>Size</b> — the width and height of each opening, and how many panels it takes</li>
  <li><b>Fabric</b> — the fabric you choose and how much of it the heading needs</li>
  <li><b>Lining</b> — unlined, standard lining or blackout lining</li>
  <li><b>Heading</b> — euro pleat, pinch pleat or another style</li>
  <li><b>Installation</b> — the number of windows and how high they are</li>
</ul>
<p>Send photos of your windows by text or WhatsApp and you get a free written quote within 24 hours.</p>

<h2>Custom drapes across Miami</h2>
<p>We measure, make and install drapery throughout Miami-Dade:</p>
<ul>
  <li><a href="/areas/brickell/"><b>Brickell</b></a> — sheers and blackout drapery for high-rise, floor-to-ceiling glass</li>
  <li><a href="/areas/miami-beach/"><b>Miami Beach</b></a> — lined drapes for sun-facing rooms and outdoor curtains for terraces</li>
  <li><a href="/areas/coral-gables/"><b>Coral Gables</b></a> — lined drapery for large living-room windows</li>
  <li><a href="/areas/kendall/"><b>Kendall</b></a> — custom curtains for bedrooms and living rooms</li>
  <li><a href="/areas/doral/"><b>Doral</b></a> — blackout curtains for bedrooms</li>
  <li><a href="/areas/north-miami/"><b>North Miami</b></a> — close to our workshop at 1 NW 62nd St</li>
  <li><a href="/areas/north-miami-beach/"><b>North Miami Beach</b></a> — condo and family-home drapery north along Biscayne Bay</li>
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
         ("Can you make drapes for sliding doors and floor-to-ceiling windows?",
          "Yes. Tall glass, arched windows and sliding doors are most of what we make. We plan the width so the drapes clear the door or the view when they are open."),
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
    path="drapery/euro-pleat-drapes-miami", kind="service", service="Custom euro pleat drapes",
    parent=("Drapery", "/drapery/"), crumb="Euro Pleat Drapes",
    title="Euro Pleat Drapes in Miami | Custom Made &amp; Installed | MIAN",
    desc="Custom euro pleat drapes in Miami, sewn to measure in our workshop and installed by us. Sheer, lined or blackout. Free quote in 24h. Se habla español.",
    eyebrow="Drapery · Euro pleat",
    h1="Euro Pleat Drapes in Miami, Made to Measure",
    lede="Tailored euro pleat drapery for condos, tall windows and sliding doors — measured, sewn in our Miami workshop and installed by us. Free quote in 24 hours.",
    hero_img=("drapery-pleated.jpg", "Custom pleated drapes framing a tall window in a Miami home"),
    body="""
<h2>What makes a euro pleat drape</h2>
<p>A euro pleat — also called a top-tack or tailored pleat — gathers the fabric into small groups of folds and tacks them right at the top edge of the drape. Below the tack, each pleat opens freely into soft, even folds all the way to the floor. There is no stitched-down section under the heading, so the drape looks lighter and more relaxed than a classic pinch pleat, while still hanging in a neat, regular rhythm.</p>
<p>That balance is why euro pleat drapes are one of the most requested styles in Miami: they look clean and modern on floor-to-ceiling glass, but still feel soft and finished in a bedroom or living room.</p>

<h2>Where euro pleat drapes work best</h2>
<ul>
  <li><b>Condos and high-rise windows</b> — long, uninterrupted panels that frame the view without looking heavy</li>
  <li><b>Sliding glass doors</b> — panels that stack neatly to the side when open</li>
  <li><b>Contemporary and transitional living rooms</b> where you want clean lines</li>
  <li><b>Bedrooms</b>, paired with blackout lining for sleep</li>
  <li><b>Double-height and tall windows</b>, where a simple heading keeps the focus on the fabric</li>
</ul>

<h2>Sheer, lined or blackout</h2>
<p>The heading sets the look; the fabric and lining decide how the drape performs. Miami sun is strong, so we help you choose for each room:</p>
<ul>
  <li><b>Sheer euro pleat drapes</b> soften glare and add daytime privacy while letting light through</li>
  <li><b>Lined euro pleat drapes</b> protect the face fabric from fading and give the folds more body</li>
  <li><a href="/drapery/blackout-curtains-miami/"><b>Blackout-lined euro pleat drapes</b></a> darken bedrooms, nurseries and media rooms</li>
  <li><b>Layered sheers and lined drapes</b> on two tracks, for light control from morning to night</li>
</ul>
<p>We bring samples to your home so you can compare fabrics against your own windows, walls and furniture before anything is cut.</p>

<h2>Made in our Miami workshop, installed by us</h2>
<p>Every opening is measured individually, and the drapery is cut and sewn to size in our workshop at 1 NW 62nd St, Miami. That is what lets the pleats fall evenly and the hem clear — or just kiss — the floor the way you want. We then install the drapes ourselves, so the fit is right on the day they go up.</p>
<p>Not sure euro pleat is the right heading? Compare it with <a href="/drapery/pinch-pleat-drapes-miami/">pinch pleat drapes</a>, or see every style on our <a href="/drapery/">custom drapes in Miami</a> page. We serve all of Miami-Dade, including <a href="/areas/brickell/">Brickell</a>, <a href="/areas/miami-beach/">Miami Beach</a>, <a href="/areas/coral-gables/">Coral Gables</a> and <a href="/areas/north-miami/">North Miami</a>.</p>
""",
    steps=[("Send a photo", "Share photos of the windows. You get a free quote within 24 hours."),
           ("Measure", "We measure every opening and bring fabric and lining samples."),
           ("Made to size", "Your euro pleat drapes are cut and sewn in our Miami workshop."),
           ("Installed", "We hang the drapes and check the fit.")],
    gallery=[("drapery-pleated.jpg", "Pleated drapery framing a tall window in a Miami home"),
             ("work-curtains.jpg", "Made-to-measure ivory drapery on an arched window"),
             ("patio-drapery.jpg", "Outdoor drapery on a covered Miami patio")],
    faq=[("What is a euro pleat drape?",
          "A drape whose pleats are tacked only at the very top edge, so the folds open freely below. It looks tailored but softer and more contemporary than a pinch pleat."),
         ("What is the difference between euro pleat and pinch pleat?",
          "Euro pleats are tacked at the top edge and fan out into soft folds. Pinch pleats are stitched a few inches below the top, giving crisper, more structured folds and a more traditional look."),
         ("Can euro pleat drapes be blackout?",
          "Yes. We can line euro pleat drapery with blackout lining for bedrooms and media rooms, or with a standard lining for sunny rooms."),
         ("How much do custom euro pleat drapes cost in Miami?",
          "It depends on window size, fabric and lining. Send us photos of your windows and we will send a free quote within 24 hours."),
         ("Do you measure and install?",
          "Yes. We measure each opening, sew the drapes to size in our Miami workshop and install them in your home."),
         ("¿Hablan español?",
          "Sí. Atendemos en español e inglés.")],
  ),
  dict(
    path="drapery/pinch-pleat-drapes-miami", kind="service", service="Custom pinch pleat drapes",
    parent=("Drapery", "/drapery/"), crumb="Pinch Pleat Drapes",
    title="Pinch Pleat Drapes in Miami | Custom Made &amp; Installed | MIAN",
    desc="Custom pinch pleat drapes in Miami, sewn to measure in our workshop and installed by us. Lined, blackout or sheer. Free quote in 24h. Se habla español.",
    eyebrow="Drapery · Pinch pleat",
    h1="Pinch Pleat Drapes in Miami, Made to Measure",
    lede="Classic pinch pleat drapery with crisp, structured folds — measured, sewn in our Miami workshop and installed by us. Free quote in 24 hours.",
    hero_img=("work-curtains.jpg", "Made-to-measure ivory pleated drapery on a tall arched window in Miami"),
    body="""
<h2>What makes a pinch pleat drape</h2>
<p>A pinch pleat gathers the fabric into groups of folds and stitches them together a few inches below the top of the drape, with a stiffened heading above. Because the pleat is held for that first stretch, the folds start crisp and structured and fall into deep, regular columns. The result is the classic, fuller drapery look you see in well-dressed traditional and transitional rooms.</p>
<p>Pinch pleats are a timeless choice: they look formal in a dining room, refined in a bedroom and substantial on a large living-room window.</p>

<h2>Where pinch pleat drapes work best</h2>
<ul>
  <li><b>Traditional and transitional living rooms</b> — full, tailored panels that frame large windows</li>
  <li><b>Dining rooms</b>, where structured folds add a more formal finish</li>
  <li><b>Bedrooms</b>, paired with blackout lining for sleep</li>
  <li><b>Arched and tall windows</b> that call for a fuller, more substantial drape</li>
  <li><b>Hospitality and event spaces</b> — see our <a href="/commercial/">commercial upholstery and drapery</a> work</li>
</ul>

<h2>Lined, blackout or sheer</h2>
<p>Pinch pleats hold their shape best with some body in the fabric, so most of the pinch pleat drapes we make are lined. In Miami light, we help you choose for each room:</p>
<ul>
  <li><b>Lined pinch pleat drapes</b> protect the face fabric from fading, add privacy and help the pleats keep their form</li>
  <li><a href="/drapery/blackout-curtains-miami/"><b>Blackout-lined pinch pleat drapes</b></a> for bedrooms, nurseries and media rooms</li>
  <li><b>Sheer pinch pleat drapes</b> for a softer, lighter version that still filters glare</li>
  <li><b>Coordinating cushions and pillows</b> sewn in the same fabric as your drapes</li>
</ul>
<p>We bring fabric and lining samples to your home so you can see each option against your own windows, walls and furniture before anything is cut.</p>

<h2>Made in our Miami workshop, installed by us</h2>
<p>Each window is measured individually, and the drapes are cut and sewn to size in our workshop at 1 NW 62nd St, Miami, so the pleats are evenly spaced across the full width and the hem finishes exactly where you want it. Then we install them ourselves. You deal directly with the people who measure, sew and hang your drapery — in English or Spanish.</p>
<p>Prefer a softer, more contemporary heading? Compare with <a href="/drapery/euro-pleat-drapes-miami/">euro pleat drapes</a>, or see every style on our <a href="/drapery/">custom drapes in Miami</a> page. We serve all of Miami-Dade, including <a href="/areas/coral-gables/">Coral Gables</a>, <a href="/areas/kendall/">Kendall</a>, <a href="/areas/doral/">Doral</a> and <a href="/areas/north-miami/">North Miami</a>.</p>
""",
    steps=[("Send a photo", "Share photos of the windows. You get a free quote within 24 hours."),
           ("Measure", "We measure every opening and bring fabric and lining samples."),
           ("Made to size", "Your pinch pleat drapes are cut and sewn in our Miami workshop."),
           ("Installed", "We hang the drapes and check the fit.")],
    gallery=[("work-curtains.jpg", "Ivory pleated drapery on an arched window in Miami"),
             ("drapery-pleated.jpg", "Pleated drapery framing a tall window in a Miami home"),
             ("work-commercial.jpg", "Upholstery and soft furnishings for a Miami restaurant")],
    faq=[("What is a pinch pleat drape?",
          "A drape whose pleats are stitched together a few inches below the top, giving crisp, structured folds and a fuller, more traditional look."),
         ("Pinch pleat or euro pleat — which should I choose?",
          "Pinch pleats suit traditional and transitional rooms and give a fuller, more formal drape. Euro pleats are tacked only at the top edge, for softer folds and a more contemporary look. We bring samples so you can decide at home."),
         ("Can pinch pleat drapes be blackout?",
          "Yes. We can add blackout lining for bedrooms and media rooms, or a standard lining for sunny rooms."),
         ("How much do custom pinch pleat drapes cost in Miami?",
          "It depends on window size, fabric and lining. Send us photos of your windows and we will send a free quote within 24 hours."),
         ("Do you measure and install?",
          "Yes. We measure each opening, sew the drapes to size in our Miami workshop and install them in your home."),
         ("¿Hablan español?",
          "Sí. Atendemos en español e inglés.")],
  ),
  dict(
    path="commercial", kind="service", service="Commercial upholstery",
    title="Commercial Upholstery in Miami | Restaurants, Hotels &amp; Offices | MIAN",
    desc="Commercial upholstery in Miami-Dade: restaurant banquettes and booths, dining chairs, hotel and office seating, marine cushions. Contract-grade fabrics. Free quote in 24h.",
    eyebrow="Commercial · Miami-Dade",
    h1="Commercial Upholstery in Miami",
    lede="We upholster banquettes, booths, dining chairs and lounge seating with contract-grade fabrics and durable foam, made in our Miami workshop. Free quote in 24 hours.",
    hero_img=("work-commercial.jpg", "Restaurant banquette and leather dining chairs upholstered for a Miami venue"),
    body="""
<h2>Seating built for heavy daily use</h2>
<p>Restaurant and hospitality seating takes more wear in a month than a home sofa does in a year. We rebuild it with contract-grade fabrics and durable foam so it holds its shape and cleans easily — and we make it in our own workshop in Miami, so you deal directly with the people doing the work.</p>
<h3>What we upholster for businesses</h3>
<ul>
  <li><b>Restaurant booth upholstery</b> and banquettes</li>
  <li><b>Dining and bar chairs</b> — matched sets</li>
  <li><b>Hotel furniture upholstery</b>: lounge and lobby seating, also for offices</li>
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
    "Popular here: vintage and mid-century chair reupholstery, sofas, and made-to-measure drapery. Further north-east? See <a href=\"/areas/north-miami-beach/\">upholstery in North Miami Beach</a>."),
  "north-miami-beach": ("North Miami Beach", "", ""),  # body and FAQ in AREA_META
  "hialeah": ("Hialeah",
    "Hialeah homes keep their furniture for years, and a good sofa or dining set is usually worth rebuilding. We pick up in Hialeah, rebuild the piece in our Miami workshop and bring it back finished. Atendemos en español.",
    "Popular here: furniture upholstery for sofas and dining chairs, leather reupholstery, and replacement patio cushions."),
}
# Per-area overrides (CTR tests on queries an area already ranks for).
AREA_META = {
  "north-miami": dict(
    title="North Miami Upholstery | Free In-Home Quote, Reply in 24h",
    desc="Reupholstery &amp; custom upholstery in North Miami: sofas, chairs, headboards &amp; drapes. Free in-home quote, reply within 24h. Se habla español.",
    h1="Custom Upholstery &amp; Reupholstery in North Miami",
    lede="Custom upholstery, furniture reupholstery and made-to-measure drapes for North Miami homes, condos and businesses, made in our workshop a short drive south at 1 NW 62nd St. Pickup and delivery available, plus a free quote within 24 hours.",
    body="""
<h2>Custom upholstery for North Miami</h2>
<p>North Miami is one of the closest areas to our workshop at 1 NW 62nd St, Miami, a short drive down Biscayne Boulevard or NE 2nd Avenue — so measuring visits, pickup and delivery are easy to schedule. Mid-century and vintage pieces are common in North Miami homes, and a well-built frame is usually worth reupholstering rather than replacing.</p>
<p>You deal directly with the people who measure, cut and sew your furniture, in English or Spanish, from the first photo to delivery.</p>

<h3>Furniture upholstery and reupholstery</h3>
<p>We strip the old fabric, replace the foam and padding, repair springs and webbing where they need it, and finish the piece in the fabric you choose. Typical North Miami jobs:</p>
<ul>
  <li><a href="/upholstery/sofa-reupholstery-miami/"><b>Sofas and sectionals</b></a> — new foam and fabric on the frame you already own</li>
  <li><a href="/upholstery/chair-reupholstery-miami/"><b>Dining chairs, armchairs and wingbacks</b></a> — one chair or the full set</li>
  <li><b>Vintage and mid-century pieces</b> — kept true to their original shape</li>
  <li><a href="/upholstery/headboard-upholstery-miami/"><b>Headboards</b></a> — reupholstered or made to size</li>
  <li><a href="/upholstery/leather-reupholstery-miami/"><b>Leather sofas and chairs</b></a></li>
  <li><a href="/upholstery/custom-cushions-miami/"><b>Custom cushions</b></a> — for benches, window seats and patios</li>
</ul>

<h3>Custom upholstery: changing more than the fabric</h3>
<p>Custom upholstery is for when you want the piece to change, not just look new: a different seat firmness, new welting, buttons or tufting, a skirt added or removed, or a cushion style that suits the room better. Tell us what you want to change and we tell you what the frame allows.</p>

<h3>Fabrics for daily use and Florida sun</h3>
<p>Performance fabrics hold up to kids, pets and daily use; outdoor-rated textiles suit patios and sun-facing rooms; linen, velvet and bouclé suit a quieter living room. We bring swatches to your home so you can compare them in your own light.</p>

<h3>Drapes for North Miami homes</h3>
<p>Ready-made curtains rarely fit tall windows and sliding doors. We measure each opening, sew the drapery to size and install it: <a href="/drapery/euro-pleat-drapes-miami/">euro pleat</a> or <a href="/drapery/pinch-pleat-drapes-miami/">pinch pleat</a> headings, sheers and <a href="/drapery/blackout-curtains-miami/">blackout drapes</a>. See every style on our <a href="/drapery/">custom drapes in Miami</a> page.</p>

<h3>How it works</h3>
<p>Send a photo of the piece by text, WhatsApp or the form, and you get a free quote within 24 hours. We come to measure and bring swatches, rebuild the piece in our workshop and deliver it back to your North Miami home. Further north-east? See <a href="/areas/north-miami-beach/">upholstery in North Miami Beach</a>.</p>
""",
    faq=[("Do you do custom upholstery in North Miami?",
          "Yes. We reupholster and custom-upholster sofas, chairs, headboards and vintage pieces for North Miami homes and businesses, with pickup and delivery available."),
         ("Where is your upholstery shop?",
          "Our workshop is at 1 NW 62nd St, Unit 8, Miami, FL 33150, a short drive south of North Miami."),
         ("Do you pick up furniture in North Miami?",
          "Yes. We pick up the piece, rebuild it in our workshop and deliver it back to you."),
         ("Do you come to measure and show fabrics?",
          "Yes. We measure the piece and bring swatches so you can choose at home."),
         ("How do I get a quote?",
          "Send a photo of the piece by text, WhatsApp or the form. You get a free quote within 24 hours."),
         ("¿Hablan español?", "Sí. Atendemos en español e inglés.")]),
  "kendall": dict(
    title="Upholstery Services in Kendall &amp; Kendale Lakes, FL | MIAN",
    desc="Upholstery services in Kendall and Kendale Lakes: sofa, chair &amp; headboard reupholstery, custom cushions and drapes. Pickup &amp; delivery, free quote in 24h.",
    h1="Upholstery Services in Kendall &amp; Kendale Lakes",
    lede="Furniture reupholstery, custom upholstery and made-to-measure drapery for homes across Kendall, Kendale Lakes and West Kendall. We pick up, rebuild the piece in our Miami workshop and deliver it back. Free quote within 24 hours.",
    body="""
<h2>Upholstery for Kendall and Kendale Lakes homes</h2>
<p>Kendall and Kendale Lakes family homes get daily use from every sofa and dining chair. Reupholstering in a performance fabric brings back comfortable, easy-to-clean seating without replacing furniture you already like — and a solid frame rebuilt with new foam usually outlasts a new budget sofa.</p>
<p>Our workshop is at 1 NW 62nd St, Miami. We cover Kendall, Kendale Lakes and West Kendall with pickup and delivery, so you don't need to bring anything in: send a photo, we come to measure, and the finished piece comes back to your home.</p>

<h3>Upholstery services in Kendall</h3>
<ul>
  <li><a href="/upholstery/sofa-reupholstery-miami/"><b>Sofa and sectional reupholstery</b></a> — family-room sofas with new foam and fabric</li>
  <li><a href="/upholstery/chair-reupholstery-miami/"><b>Dining chair sets</b></a> — one chair or the whole set, in a fabric that cleans easily</li>
  <li><a href="/upholstery/headboard-upholstery-miami/"><b>Headboards</b></a> — reupholstered or made to size</li>
  <li><a href="/upholstery/leather-reupholstery-miami/"><b>Leather sofas and chairs</b></a></li>
  <li><a href="/upholstery/custom-cushions-miami/"><b>Custom cushions</b></a> — replacement patio and pool-deck cushions in outdoor fabric</li>
</ul>

<h3>Fabrics for kids, pets and the patio</h3>
<p>For family rooms we usually recommend performance fabrics that resist stains and wear; for patios and screened porches, outdoor-rated textiles that handle sun and humidity. We bring swatches to your home so you can see them in your own light.</p>

<h3>Custom curtains in Kendall</h3>
<p>We also measure, sew and install drapery for Kendall bedrooms and living rooms: <a href="/drapery/blackout-curtains-miami/">blackout drapes</a> for bedrooms, <a href="/drapery/pinch-pleat-drapes-miami/">pinch pleat</a> drapes for living and dining rooms, and sheers for sliding doors. See all styles on our <a href="/drapery/">custom drapes in Miami</a> page.</p>

<h3>How it works</h3>
<p>Send a photo of the piece by text, WhatsApp or the form and you get a free quote within 24 hours. We measure and bring swatches, rebuild the piece in our workshop and deliver it back to Kendall or Kendale Lakes. Atendemos en español.</p>
""",
    faq=[("Do you offer upholstery services in Kendale Lakes?",
          "Yes. We reupholster sofas, dining chairs, headboards and cushions for homes in Kendale Lakes, Kendall and West Kendall, with pickup and delivery."),
         ("Do you pick up furniture in Kendall?",
          "Yes. We pick up the piece, rebuild it in our Miami workshop and deliver it back to you."),
         ("Do you come to measure and show fabrics?",
          "Yes. We measure the piece and bring swatches so you can choose at home."),
         ("How do I get a quote?",
          "Send a photo of the piece by text, WhatsApp or the form. You get a free quote within 24 hours."),
         ("¿Hablan español?", "Sí. Atendemos en español e inglés.")]),
  "north-miami-beach": dict(
    title="Upholstery Services in North Miami Beach, FL | MIAN",
    desc="Upholstery services in North Miami Beach: sofa, chair &amp; headboard reupholstery and custom drapes. Pickup &amp; delivery, free quote in 24h. Se habla español.",
    h1="Upholstery Services in North Miami Beach",
    lede="Reupholstery, custom upholstery and made-to-measure drapery for North Miami Beach homes, condos and businesses, made in our Miami workshop. Pickup and delivery available, plus a free quote within 24 hours.",
    body="""
<h2>Upholstery and drapery for North Miami Beach</h2>
<p>North Miami Beach mixes bayfront condos along Biscayne Boulevard with single-family homes, townhouses and a busy stretch of restaurants and offices. That mix shows up in the work: sectionals and dining chairs that get used every day, headboards and bedroom drapes for condos, and seating for local businesses. We cover all of it from our workshop at 1 NW 62nd St, Miami, a short drive south — so pickup and delivery are easy to schedule.</p>
<p>You deal directly with the people who measure, sew and upholster your pieces, in English or Spanish, from the first photo to delivery.</p>

<h3>Furniture reupholstery</h3>
<p>If the frame is solid, reupholstering is usually the better move than replacing it. We strip the old fabric, replace the foam and padding, repair springs and webbing where they need it and finish the piece in the fabric you choose. Typical North Miami Beach jobs:</p>
<ul>
  <li><a href="/upholstery/sofa-reupholstery-miami/"><b>Sofas and sectionals</b></a> — new foam and fabric on the frame you already own</li>
  <li><a href="/upholstery/chair-reupholstery-miami/"><b>Dining chairs</b></a> — one chair or the full set</li>
  <li><a href="/upholstery/headboard-upholstery-miami/"><b>Headboards</b></a> — reupholstered or made to size for the bedroom</li>
  <li><a href="/upholstery/leather-reupholstery-miami/"><b>Leather sofas and chairs</b></a></li>
  <li><b>Vintage and mid-century pieces</b> worth keeping</li>
</ul>

<h3>Fabrics for sun, salt air and daily use</h3>
<p>Close to the bay, sun and humidity are hard on fabric. For balconies and patios we recommend outdoor-rated textiles, and for family rooms, performance fabrics that stand up to kids and pets. Linen, velvet and bouclé suit a quieter living room. We bring swatches to your home so you can compare them in your own light. For terraces, see <a href="/upholstery/custom-cushions-miami/">custom cushions</a>.</p>

<h3>Custom drapes for condos and homes</h3>
<p>Floor-to-ceiling glass and sliding doors rarely fit ready-made curtains. We measure every opening, sew the drapery to size and install it ourselves: <a href="/drapery/euro-pleat-drapes-miami/">euro pleat</a> or <a href="/drapery/pinch-pleat-drapes-miami/">pinch pleat</a> headings, sheers for glare and <a href="/drapery/blackout-curtains-miami/">blackout drapes</a> for bedrooms. See every style on our <a href="/drapery/">custom drapes in Miami</a> page.</p>

<h3>Commercial upholstery in North Miami Beach</h3>
<p>Restaurants, offices and hospitality spaces get <a href="/commercial/">commercial upholstery</a> with contract-grade fabrics and durable foam — booths, banquettes, dining chairs and lounge seating. Tell us your schedule and we plan pickup and delivery around it.</p>

<h3>How it works</h3>
<p>Send a photo of the piece or the windows by text, WhatsApp or the form, and you get a free quote within 24 hours. We come to measure and bring samples, rebuild or sew everything in our Miami workshop, and deliver or install it in North Miami Beach. Next door in <a href="/areas/north-miami/">North Miami</a>? We cover it the same way.</p>
<!-- TODO-DATO: a real North Miami Beach project (piece, fabric, neighbourhood) if one can be shared -->
""",
    faq=[("Do you offer upholstery services in North Miami Beach?",
          "Yes. We reupholster furniture, make custom drapery and upholster commercial seating for homes, condos and businesses in North Miami Beach, with pickup and delivery available."),
         ("Do you pick up furniture in North Miami Beach?",
          "Yes. We pick up the piece, rebuild it in our workshop at 1 NW 62nd St, Miami, and deliver it back to you."),
         ("Do you come to measure and show fabrics?",
          "Yes. We measure the piece or the windows and bring swatches so you can choose at home."),
         ("Do you make custom drapes for condos?",
          "Yes. We measure each opening, sew the drapes to size and install them, including sheers and blackout-lined drapery for bedrooms."),
         ("How do I get a quote?",
          "Send a photo of the piece by text, WhatsApp or the form. You get a free quote within 24 hours."),
         ("¿Hablan español?", "Sí. Atendemos en español e inglés.")]),
}
AREA_IMG = {"coral-gables": "boucle-armchair.jpg", "doral": "dining-chairs.jpg", "brickell": "drapery-pleated.jpg",
            "miami-beach": "yacht-cushions.jpg", "kendall": "blue-velvet-sofa.jpg", "north-miami": "tufted-settee.jpg",
            "hialeah": "dining-chairs.jpg", "north-miami-beach": "boucle-armchair.jpg"}
for slug, (name, p1, p2) in AREA_COPY.items():
    PAGES.append(dict(
        path=f"areas/{slug}", kind="area", area=name,
        title=f"Upholstery &amp; Reupholstery in {name}, FL | MIAN House &amp; Decor",
        desc=f"Furniture reupholstery, custom upholstery and made-to-measure drapery in {name}, FL. Free quote in 24h, se habla español. (786) 348-8650.",
        eyebrow=f"Serving {name}",
        h1=f"Upholstery &amp; Reupholstery in {name}",
        lede=f"Reupholstery, custom upholstery and made-to-measure drapery for homes and businesses in {name}. Pickup and delivery available, plus a free quote within 24 hours.",
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
<p>Everything is made in our workshop at 1 NW 62nd St, Miami. Pickup and delivery are available, and you get a written quote within 24 hours of sending us a photo.</p>
""",
        steps=None, gallery=None,
        faq=[(f"Do you pick up furniture in {name}?", f"Yes. Pickup and delivery are available in {name} and across Miami-Dade."),
             ("How do I get a quote?", "Send a photo of the piece by text, WhatsApp or the form. You get a free quote within 24 hours."),
             ("¿Hablan español?", "Sí. Atendemos en español e inglés.")],
    ))
    PAGES[-1].update(AREA_META.get(slug, {}))

from content_new import NEW_PAGES
from content_es import ES, PAIRS, HOME_META, HOME_DESC, HOME_EXTRA, area_es
PAGES += NEW_PAGES
for name_, slug_ in AREAS:
    ES[f"areas/{slug_}"] = area_es(slug_, name_)
assert not [p["path"] for p in PAGES if p["path"] not in ES]

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
    elif pg.get("parent"):
        crumbs += [pg["parent"], (pg["crumb"], f"/{pg['path']}/")]
    else:
        crumbs += [(pg.get("crumb") or plain(pg["h1"]).split(" in Miami")[0].split(":")[0], f"/{pg['path']}/")]

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

    key = pg.get("en", pg["path"])
    hub = f"/{key}/" if not pg.get("parent") else pg["parent"][1]
    kids = [p for p in PAGES if p.get("parent") and p["parent"][1] == hub and p["path"] != key]
    label = (lambda p: ES[p["path"]]["crumb"]) if pg.get("en") else (lambda p: p["crumb"])
    specialties = "" if not kids else '<section class="section" style="padding-top:0"><div class="wrap"><div class="prose"><h2>Our specialties</h2></div><div class="chips">' + \
        "".join(f'<a href="/{p["path"]}/">{label(p)}</a>' for p in kids) + "</div></div></section>"

    others = SERVICES if pg["kind"] == "area" else [s for s in SERVICES if s[1] != f"/{key}/"]
    nearby = '<section class="section" style="padding-top:0"><div class="wrap"><div class="prose"><h2>More from MIAN</h2></div><div class="chips">' + \
        "".join(f'<a href="{u}">{n}</a>' for n, u in others) + \
        "".join(f'<a href="/areas/{s}/">{n}</a>' for n, s in AREAS if f"areas/{s}" != key) + "</div></div></section>"

    cta = f'''<section class="section express"><div class="wrap"><div class="express__in rv">
<h2>Get your free quote <em>in 24 hours</em></h2>
<p>Send a photo of the piece or the windows — we reply within one business day. Se habla español.</p>
<div class="cta-row">
<a class="btn btn--lg btn--sun" href="{SMS_HREF}" data-cta="sms">{SVG_SMS} Text us</a>
<a class="btn btn--lg btn--onBlue" href="{PHONE_HREF}" data-cta="call">{SVG_TEL} (786) 348-8650</a>
<a class="btn btn--lg btn--onBlue" href="{WA_HREF}" target="_blank" rel="noopener" data-cta="whatsapp">{SVG_WA} WhatsApp</a>
<a class="btn btn--lg btn--onBlue" href="/#contact" data-cta="quote">Quote form</a>
</div></div></div></section>'''

    form_js = ""
    if key in FORM_PAGES:
        cta, form_js = CONTACT, FORM_JS

    crumb_html = " · ".join(f'<a href="{u}">{n}</a>' if i < len(crumbs) - 1 else f"<span>{n}</span>" for i, (n, u) in enumerate(crumbs))
    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
{GTM_HEAD}
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{pg["title"]}</title>
<meta name="description" content="{pg["desc"]}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{SITE}/{key}/">
<link rel="alternate" hreflang="es" href="{SITE}/{ES[key]["path"]}/">
<link rel="alternate" hreflang="x-default" href="{SITE}/{key}/">
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
          <span><b>Pickup &amp; delivery</b> available in Miami-Dade</span>
          <span><b>Free quote</b> in 24h</span>
        </div>
      </div>
      <div class="oval"><div class="oval__img"><img src="/assets/img/{img}" alt="{img_alt}" fetchpriority="high"></div></div>
    </div>
  </div>
</section>
<section class="section"><div class="wrap"><div class="prose rv">{pg["body"]}</div></div></section>
{specialties}
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
{form_js}
<script src="/assets/site.js" defer></script>
</body>
</html>
'''
    return page.replace('href="/#contact"', 'href="#contact"') if key in FORM_PAGES else page


def es_page(pg):
    e = ES[pg["path"]]
    m = {**pg, **{k: v for k, v in e.items() if k not in ("hero_alt", "gallery_alt")}, "en": pg["path"]}
    m["hero_img"] = (pg["hero_img"][0], e["hero_alt"])
    if pg.get("gallery"):
        m["gallery"] = [(f, a) for (f, _), a in zip(pg["gallery"], e["gallery_alt"])]
    return m


LANG_LINK = r'<a class="lang"[^>]*>[^<]*</a>'
SWAPS = sorted(PAIRS + [(f'>{p["crumb"]}</a>', f'>{ES[p["path"]]["crumb"]}</a>') for p in PAGES if p.get("parent")],
               key=lambda x: -len(x[0]))


def to_es(page, en_href):
    """Spanish chrome: exact-string swaps, then every internal link to its /es/ counterpart."""
    for a, b in SWAPS:
        page = page.replace(a, b)
    for p in PAGES:
        es = ES[p["path"]]["path"]
        page = page.replace(f'href="/{p["path"]}/"', f'href="/{es}/"').replace(f'"item": "{SITE}/{p["path"]}/"', f'"item": "{SITE}/{es}/"')
    page = page.replace('href="/"', 'href="/es/"').replace('href="/#', 'href="/es/#')
    return re.sub(LANG_LINK, f'<a class="lang" href="{en_href}" hreflang="en" lang="en">English</a>', page)


def to_en(page, es_path):
    return re.sub(LANG_LINK, f'<a class="lang" href="/{es_path}/" hreflang="es" lang="es">Español</a>', page)


def es_home():
    page = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    for a, b in HOME_META:
        assert a in page, a
        page = page.replace(a, b)
    page = re.sub(r'(<meta (?:name="description"|property="og:description") content=")[^"]*', lambda m: m.group(1) + HOME_DESC, page)
    page = re.sub(r'\s*<p class="es-link">.*?</p>', "", page).replace("<!-- ═══ NEAR ═══ -->", HOME_EXTRA)
    return to_es(rootify(page).replace("url(assets/", "url(/assets/"), "/")


def es_thanks():
    page = open(os.path.join(ROOT, "thanks.html"), encoding="utf-8").read()
    return to_es(page.replace('src="assets/', 'src="/assets/').replace('href="assets/', 'href="/assets/'), "/thanks.html")


# sitemap lastmod: kept from the existing sitemap; bumped only for pages whose HTML changed.
# The home page is not built here — bump its lastmod in sitemap.xml by hand when editing index.html.
from datetime import date
SITEMAP = os.path.join(ROOT, "sitemap.xml")
lastmod = dict(re.findall(r"<loc>([^<]+)</loc><lastmod>([^<]+)</lastmod>", open(SITEMAP).read())) if os.path.exists(SITEMAP) else {}

def emit(path, page):
    out = os.path.join(ROOT, path, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    url = f"{SITE}/{path}/"
    if not os.path.exists(out) or open(out, encoding="utf-8").read() != page:
        lastmod[url] = str(date.today())
    open(out, "w", encoding="utf-8").write(page)
    print("built", "/" + path + "/")


for pg in PAGES:
    emit(pg["path"], to_en(render(pg), ES[pg["path"]]["path"]))
    emit(ES[pg["path"]]["path"], to_es(render(es_page(pg)), f"/{pg['path']}/"))
emit("es", es_home())
emit("es/gracias", es_thanks())

# Old URLs that still get traffic. GitHub Pages has no server redirects.
for path, target in (("contact", "/#contact"), ("about", "/#about")):
    os.makedirs(os.path.join(ROOT, path), exist_ok=True)
    open(os.path.join(ROOT, path, "index.html"), "w", encoding="utf-8").write(
        f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>MIAN House &amp; Decor</title>
<meta name="robots" content="noindex"><link rel="canonical" href="{SITE}/">
<meta http-equiv="refresh" content="0; url={target}"><script>location.replace("{target}")</script>
</head><body><a href="{target}">MIAN House &amp; Decor</a></body></html>
''')

urls = [f"{SITE}/", f"{SITE}/es/"] + [f"{SITE}/{p}/" for pg in PAGES for p in (pg["path"], ES[pg["path"]]["path"])]
open(SITEMAP, "w").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    "".join(f"  <url><loc>{u}</loc><lastmod>{lastmod.get(u, date.today())}</lastmod></url>\n" for u in urls) + "</urlset>\n")
print("sitemap:", len(urls), "urls")
