/* Brain Code Camp — Carbon Nav */
(function () {
  const nav    = document.getElementById('side-nav');
  const toggle = document.getElementById('nav-toggle');
  const content = document.querySelector('.cds-content');
  const footer  = document.querySelector('.cds-footer');
  const overlay = document.querySelector('.cds-header__overlay');

  /* ── collapse toggle ── */
  function isDesktop() { return window.innerWidth >= 1056; }

  function openNav() {
    nav.classList.add('open');
    if (overlay) overlay.classList.add('show');
  }
  function closeNav() {
    nav.classList.remove('open');
    if (overlay) overlay.classList.remove('show');
  }
  function collapseDesktop() {
    nav.classList.add('collapsed');
    if (content) content.classList.add('expanded');
    if (footer)  footer.classList.add('expanded');
    localStorage.setItem('bcc-nav-collapsed', '1');
  }
  function expandDesktop() {
    nav.classList.remove('collapsed');
    if (content) content.classList.remove('expanded');
    if (footer)  footer.classList.remove('expanded');
    localStorage.setItem('bcc-nav-collapsed', '0');
  }

  if (toggle) {
    toggle.addEventListener('click', function () {
      if (isDesktop()) {
        nav.classList.contains('collapsed') ? expandDesktop() : collapseDesktop();
      } else {
        nav.classList.contains('open') ? closeNav() : openNav();
      }
    });
  }
  if (overlay) {
    overlay.addEventListener('click', closeNav);
  }

  /* restore desktop collapsed state */
  if (isDesktop() && localStorage.getItem('bcc-nav-collapsed') === '1') {
    collapseDesktop();
  }

  /* ── sub-menu toggles ── */
  document.querySelectorAll('.cds-side-nav__link[data-toggle]').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      const item = btn.closest('.cds-side-nav__item');
      item.classList.toggle('open');
    });
  });

  /* ── auto-open parent of active item ── */
  const active = document.querySelector('.cds-side-nav__link.active');
  if (active) {
    let el = active.closest('.cds-side-nav__item');
    while (el) {
      el.classList.add('open');
      el = el.parentElement
             ? el.parentElement.closest('.cds-side-nav__item')
             : null;
    }
    /* scroll active item into view */
    setTimeout(function () { active.scrollIntoView({ block: 'center' }); }, 50);
  }
})();
