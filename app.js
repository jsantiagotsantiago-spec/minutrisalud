// ============================================
// MINUTRISALUD — shared behaviors
// ============================================

// Theme toggle (system-preference aware, no localStorage — sandboxed iframes block it)
(function () {
  const root = document.documentElement;
  let theme = matchMedia('(prefers-color-scheme:dark)').matches ? 'dark' : 'light';
  root.setAttribute('data-theme', theme);

  document.querySelectorAll('[data-theme-toggle]').forEach((btn) => {
    updateIcon(btn, theme);
    btn.addEventListener('click', () => {
      theme = theme === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', theme);
      document.querySelectorAll('[data-theme-toggle]').forEach((b) => updateIcon(b, theme));
    });
  });

  function updateIcon(btn, t) {
    btn.setAttribute('aria-label', 'Cambiar a modo ' + (t === 'dark' ? 'claro' : 'oscuro'));
    btn.innerHTML =
      t === 'dark'
        ? '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>'
        : '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
  }
})();

// Sticky header hide-on-scroll
(function () {
  const header = document.querySelector('.header');
  if (!header) return;
  let lastY = window.scrollY;
  window.addEventListener('scroll', () => {
    const y = window.scrollY;
    if (y > lastY && y > 120) header.classList.add('header--hidden');
    else header.classList.remove('header--hidden');
    header.classList.toggle('header--scrolled', y > 8);
    lastY = y;
  });
})();

// Mobile nav drawer
(function () {
  const toggle = document.querySelector('.nav-toggle');
  const drawer = document.querySelector('.mobile-nav');
  const close = document.querySelector('.mobile-nav-close');
  if (!toggle || !drawer) return;
  const open = () => drawer.classList.add('open');
  const shut = () => drawer.classList.remove('open');
  toggle.addEventListener('click', open);
  close && close.addEventListener('click', shut);
  drawer.querySelectorAll('a').forEach((a) => a.addEventListener('click', shut));
})();

// Scroll reveal
(function () {
  const items = document.querySelectorAll('.reveal');
  if (!items.length || !('IntersectionObserver' in window)) {
    items.forEach((el) => el.classList.add('is-visible'));
    return;
  }
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          e.target.classList.add('is-visible');
          io.unobserve(e.target);
        }
      });
    },
    { threshold: 0.05, rootMargin: '0px 0px -10% 0px' }
  );
  items.forEach((el) => io.observe(el));
  // Safety net: some environments (embedded/sandboxed preview iframes, very fast
  // scrolling, or anchor-jump navigation) can prevent the IntersectionObserver from
  // firing for every element. Never let content stay permanently hidden.
  setTimeout(() => {
    items.forEach((el) => el.classList.add('is-visible'));
    io.disconnect();
  }, 1500);
})();

// Contact form (mailto fallback — no backend wired yet)
(function () {
  const form = document.querySelector('#contact-form');
  if (!form) return;
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const data = new FormData(form);
    const nombre = data.get('name') || '';
    const email = data.get('email') || '';
    const telefono = data.get('phone') || '';
    const servicio = data.get('service') || '';
    const mensaje = data.get('message') || '';
    const body = encodeURIComponent(
      `Nombre: ${nombre}\nEmail: ${email}\nTeléfono: ${telefono}\nServicio de interés: ${servicio}\n\n${mensaje}`
    );
    window.location.href = `mailto:hola@minutrisalud.com?subject=Nueva%20consulta%20desde%20la%20web&body=${body}`;
    const note = document.querySelector('#form-note');
    if (note) note.hidden = false;
  });
})();

// Checkout form (pago.html — plan selector, live summary, mailto fallback, no real payment gateway wired yet)
(function () {
  const form = document.querySelector('#checkout-form');
  if (!form) return;

  const planName = document.querySelector('#summary-plan-name');
  const planPrice = document.querySelector('#summary-plan-price');
  const total = document.querySelector('#summary-total');
  const radios = form.querySelectorAll('input[name="plan"]');

  function preselectFromQuery() {
    const params = new URLSearchParams(window.location.search);
    const plan = params.get('plan');
    if (!plan) return;
    const match = form.querySelector(`input[name="plan"][value="${plan}"]`);
    if (match) match.checked = true;
  }

  function updateSummary() {
    const checked = form.querySelector('input[name="plan"]:checked');
    if (!checked) return;
    planName.textContent = checked.dataset.label;
    planPrice.textContent = checked.dataset.price;
    total.textContent = checked.dataset.price;
  }

  preselectFromQuery();
  updateSummary();
  radios.forEach((r) => r.addEventListener('change', updateSummary));

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const checked = form.querySelector('input[name="plan"]:checked');
    const data = new FormData(form);
    const email = (data.get('email') || '').trim();
    const nombre = (data.get('name') || '').trim();
    const paymentLink = checked ? checked.dataset.paymentLink : '';

    if (!paymentLink) return;

    // Redirige a la pasarela segura de Stripe (entorno de pruebas). Stripe recoge los
    // datos de la tarjeta directamente en su página alojada; no pasan por nuestro servidor.
    const url = new URL(paymentLink);
    if (email) url.searchParams.set('prefilled_email', email);
    if (nombre) url.searchParams.set('client_reference_id', nombre);

    window.location.href = url.toString();
  });
})();

// Notify form (app teaser page — mailto fallback, no backend wired yet)
(function () {
  const form = document.querySelector('#notify-form');
  if (!form) return;
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = form.querySelector('input[type="email"]').value;
    const body = encodeURIComponent(`Avísame cuando la app Minutrisalud esté disponible.\nEmail: ${email}`);
    window.location.href = `mailto:hola@minutrisalud.com?subject=Aviso%20app%20Minutrisalud&body=${body}`;
    const note = document.querySelector('#notify-note');
    if (note) note.hidden = false;
    form.reset();
  });
})();

// Consejos page — category filter pills
(function () {
  const filters = document.querySelectorAll('.tip-filters .filter-pill');
  const cards = document.querySelectorAll('.tip-grid .tip-card');
  if (!filters.length || !cards.length) return;

  filters.forEach((pill) => {
    pill.addEventListener('click', () => {
      filters.forEach((p) => p.classList.remove('is-active'));
      pill.classList.add('is-active');
      const filter = pill.dataset.filter;

      cards.forEach((card) => {
        const show = filter === 'all' || card.dataset.category === filter;
        card.classList.toggle('is-filtered-out', !show);
      });
    });
  });
})();
