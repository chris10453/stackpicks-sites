/* ============================================================
   Lightweight affiliate-click logger (no backend required).
   Records every affiliate-link click to this browser's
   localStorage so the portfolio dashboard can read it.
   For real cross-device numbers, add Umami/Plausible later
   (see PORTFOLIO.md) — this is the zero-cost starter layer.
   ============================================================ */
(function () {
  // Site id comes from <meta name="site-id" content="...">
  var meta = document.querySelector('meta[name="site-id"]');
  var SITE = meta ? meta.content : (location.hostname || 'unknown');
  var KEY = 'aff_clicks';

  function load() {
    try { return JSON.parse(localStorage.getItem(KEY) || '[]'); }
    catch (e) { return []; }
  }
  function save(rows) {
    try { localStorage.setItem(KEY, JSON.stringify(rows.slice(-2000))); } catch (e) {}
  }

  document.addEventListener('click', function (e) {
    var a = e.target.closest('a.aff, a.btn');
    if (!a) return;
    var rows = load();
    rows.push({
      site: SITE,
      program: a.getAttribute('data-program') || '',
      page: location.pathname.split('/').pop() || 'index.html',
      href: a.getAttribute('href') || '',
      ts: Date.now()
    });
    save(rows);
  }, true);
})();
