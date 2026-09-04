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

// Calculadora nutricional — IMC + estimación de gasto calórico
// (reinterpretación propia con fórmulas clínicas actuales: SEEDO, Mifflin-St Jeor, FAO/OMS/UNU)
(function () {
  const form = document.querySelector('#calc-form');
  const results = document.querySelector('#calc-results');
  if (!form || !results) return;

  const BMI_BANDS = [
    { max: 18.5, label: 'Peso insuficiente', badge: 'warn', pos: 8 },
    { max: 25, label: 'Normopeso', badge: 'good', pos: 30 },
    { max: 27, label: 'Sobrepeso grado I', badge: 'warn', pos: 48 },
    { max: 30, label: 'Sobrepeso grado II', badge: 'warn', pos: 58 },
    { max: 35, label: 'Obesidad tipo I', badge: 'alert', pos: 70 },
    { max: 40, label: 'Obesidad tipo II', badge: 'alert', pos: 82 },
    { max: Infinity, label: 'Obesidad tipo III', badge: 'alert', pos: 94 },
  ];

  function classifyBMI(bmi) {
    return BMI_BANDS.find((b) => bmi < b.max) || BMI_BANDS[BMI_BANDS.length - 1];
  }

  function fmt(n) {
    return Math.round(n).toLocaleString('es-ES');
  }

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const weight = parseFloat(document.querySelector('#calc-weight').value);
    const heightCm = parseFloat(document.querySelector('#calc-height').value);
    const age = parseFloat(document.querySelector('#calc-age').value);
    const sex = form.querySelector('input[name="calc-sex"]:checked').value;
    const activity = parseFloat(document.querySelector('#calc-activity').value);
    const goal = document.querySelector('#calc-goal').value;

    if (!weight || !heightCm || !age) return;

    const heightM = heightCm / 100;
    const bmi = weight / (heightM * heightM);
    const band = classifyBMI(bmi);

    // Ecuación de Mifflin-St Jeor (1990) para el metabolismo basal
    const bmr =
      sex === 'hombre'
        ? 10 * weight + 6.25 * heightCm - 5 * age + 5
        : 10 * weight + 6.25 * heightCm - 5 * age - 161;

    const tdee = bmr * activity;
    const deficit = Math.round((tdee - 500) / 10) * 10;
    const surplus = Math.round((tdee + 350) / 10) * 10;
    const maintain = Math.round(tdee / 10) * 10;

    const goalValue = goal === 'perder' ? deficit : goal === 'ganar' ? surplus : maintain;
    const goalLabel =
      goal === 'perder' ? 'Para tu objetivo (déficit moderado)' : goal === 'ganar' ? 'Para tu objetivo (superávit moderado)' : 'Para tu objetivo (mantenimiento)';

    results.innerHTML = `
      <div class="calc-result-block">
        <div class="calc-result-label">Tu índice de masa corporal</div>
        <div class="calc-result-value">
          <span class="num">${bmi.toFixed(1)}</span>
          <span class="calc-badge calc-badge--${band.badge}">${band.label}</span>
        </div>
        <div class="calc-scale">
          <div class="calc-scale-marker" style="left:${band.pos}%"></div>
        </div>
        <p class="calc-result-note">Clasificación según el consenso SEEDO para población adulta. No tiene en cuenta composición corporal ni perímetro de cintura.</p>
      </div>
      <div class="calc-result-block">
        <div class="calc-result-label">Necesidad calórica diaria estimada</div>
        <div class="calc-cal-grid">
          <div class="calc-cal-item">
            <strong>${fmt(maintain)} kcal</strong>
            <span>Mantenimiento</span>
          </div>
          <div class="calc-cal-item is-goal">
            <strong>${fmt(goalValue)} kcal</strong>
            <span>${goalLabel}</span>
          </div>
        </div>
        <p class="calc-result-note" style="margin-top:var(--space-4);">Estimación con la ecuación de Mifflin-St Jeor y tu nivel de actividad declarado. Los ajustes de peso reales dependen de muchos más factores; en consulta lo afinamos contigo.</p>
      </div>
    `;
    results.querySelectorAll('.calc-result-block').forEach((el) => el.classList.add('reveal', 'is-visible'));
    if (window.innerWidth < 860) {
      results.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
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
