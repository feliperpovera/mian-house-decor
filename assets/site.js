// Shared behaviour for the service and area pages (the home page carries its own inline copy).
(() => {
  'use strict';
  const $ = s => document.querySelector(s);
  const yr = document.getElementById('yr'); if (yr) yr.textContent = new Date().getFullYear();

  const hdr = $('#hdr'), dock = $('#dock');
  let ticking = false;
  const onScroll = () => {
    const y = window.scrollY;
    if (hdr) hdr.classList.toggle('is-stuck', y > 40);
    if (dock) dock.classList.toggle('is-on', y > 520);
    ticking = false;
  };
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, {passive: true});
  onScroll();

  const burger = $('#burger'), nav = $('#nav');
  const setMenu = open => { document.body.classList.toggle('menu-open', open); burger && burger.setAttribute('aria-expanded', String(open)); };
  burger && burger.addEventListener('click', () => setMenu(!document.body.classList.contains('menu-open')));
  nav && nav.addEventListener('click', e => { if (e.target.tagName === 'A') setMenu(false); });
  addEventListener('keydown', e => { if (e.key === 'Escape') setMenu(false); });

  const io = new IntersectionObserver((entries, obs) => {
    for (const e of entries) if (e.isIntersecting) { e.target.classList.add('in'); obs.unobserve(e.target); }
  }, {rootMargin: '0px 0px -8% 0px', threshold: 0.08});
  document.querySelectorAll('.rv').forEach(el => io.observe(el));

  // Contact clicks -> dataLayer, then thank-you page once the call/text/WhatsApp app takes over.
  window.dataLayer = window.dataLayer || [];
  const THANKS = {call: 1, sms: 1, whatsapp: 1};
  let pendingVia = null, pendingTimer;
  document.addEventListener('click', e => {
    const a = e.target.closest('[data-cta]');
    if (!a) return;
    dataLayer.push({event: 'cta_click', cta_type: a.dataset.cta, cta_location: location.pathname});
    if (!THANKS[a.dataset.cta]) return;
    pendingVia = a.dataset.cta;
    clearTimeout(pendingTimer);
    pendingTimer = setTimeout(() => { pendingVia = null; }, 15000);
  });
  document.addEventListener('visibilitychange', () => {
    if (!document.hidden || !pendingVia) return;
    const via = pendingVia; pendingVia = null; clearTimeout(pendingTimer);
    location.href = '/thanks.html?via=' + via + '&t=' + Date.now();
  });
})();
