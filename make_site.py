from build_pages import build

CHECK = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>'

def icon(name):
    icons = {
        "leaf": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M11 20A7 7 0 0 1 4 13c0-4 2-9 9-13 2 4 9 5 9 13a7 7 0 0 1-7 7c-2.5 0-4-1-6-3z"/><path d="M4 13c4 0 8 2 10 5"/></svg>',
        "chart": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 3v18h18"/><path d="M7 15l4-6 3 3 5-7"/></svg>',
        "calendar": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>',
        "heart": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.6l-1-1a5.5 5.5 0 0 0-7.8 7.8l1 1L12 21l7.8-7.6 1-1a5.5 5.5 0 0 0 0-7.8z"/></svg>',
        "video": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M23 7l-7 5 7 5V7z"/><rect x="1" y="5" width="15" height="14" rx="2"/></svg>',
        "scale": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg>',
        "phone": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3 19.5 19.5 0 0 1-6-6 19.8 19.8 0 0 1-3-8.7A2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1.1.4 2.1.7 3.1a2 2 0 0 1-.5 2.1L8 10.1a16 16 0 0 0 6 6l1.2-1.3a2 2 0 0 1 2.1-.5c1 .3 2 .6 3.1.7a2 2 0 0 1 1.7 2z"/></svg>',
        "mail": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/></svg>',
        "pin": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M21 10c0 6-9 13-9 13s-9-7-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
        "clock": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l4 2"/></svg>',
        "smartphone": '<svg width="56" height="56" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="6" y="2" width="12" height="20" rx="2.5"/><path d="M11 18h2"/></svg>',
    }
    return icons[name]


# ============================================================
# INDEX
# ============================================================
index_body = f'''
  <section class="hero">
    <div class="wrap hero-grid">
      <div>
        <span class="eyebrow">Consulta de nutrición online</span>
        <h1>Nutrición con criterio médico, sin salir de casa</h1>
        <p class="lede">Minutrisalud te acompaña por videollamada con equipo médico y nutricionistas: valoración, plan personalizado y seguimiento cercano. También disponible de forma presencial si lo prefieres.</p>
        <div class="hero-actions">
          <a href="contacto.html" class="btn btn--primary">Reservar consulta online</a>
          <a href="servicios.html" class="btn btn--ghost">Ver servicios</a>
        </div>
        <div class="hero-stats">
          <div>
            <span class="stat-num">Online</span>
            <span class="stat-label">consulta principal, por videollamada</span>
          </div>
          <div>
            <span class="stat-num">3</span>
            <span class="stat-label">profesionales: medicina y nutrición</span>
          </div>
          <div>
            <span class="stat-num">100%</span>
            <span class="stat-label">planes individualizados</span>
          </div>
        </div>
      </div>
      <div class="hero-media reveal">
        <img src="./assets/hero.png" alt="Mesa con alimentos frescos y saludables: verduras de hoja verde, nueces, cítricos y pan integral" loading="eager">
      </div>
    </div>
  </section>

  <section class="section section--offset">
    <div class="wrap">
      <div class="header-block center">
        <span class="eyebrow" style="justify-content:center;">Cómo ayudamos</span>
        <h2>Un enfoque clínico de la nutrición</h2>
        <p>Cada plan nace de una valoración real de tu salud, no de tablas genéricas.</p>
      </div>
      <div class="grid grid--3">
        <div class="card reveal">
          <div class="card-icon">{icon('scale')}</div>
          <h3>Valoración inicial completa</h3>
          <p>Historia clínica, composición corporal y hábitos, para entender tu punto de partida real.</p>
        </div>
        <div class="card reveal">
          <div class="card-icon">{icon('leaf')}</div>
          <h3>Planes personalizados</h3>
          <p>Alimentación adaptada a tu diagnóstico, tus gustos y tu rutina — nada de dietas de plantilla.</p>
        </div>
        <div class="card reveal">
          <div class="card-icon">{icon('chart')}</div>
          <h3>Seguimiento y ajuste</h3>
          <p>Revisiones periódicas con indicadores objetivos para ajustar el plan según tu evolución.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap split">
      <div class="reveal">
        <span class="eyebrow">Por qué Minutrisalud</span>
        <h2>La nutrición como parte de tu tratamiento, no aparte de él</h2>
        <p style="margin-bottom:var(--space-6);">Detrás de cada recomendación hay criterio médico: se tienen en cuenta tus antecedentes, tu medicación y tus analíticas, coordinando la alimentación con el resto de tu cuidado — todo por videollamada, sin desplazamientos.</p>
        <ul class="check-list">
          <li>{CHECK} Atención principalmente online, por videollamada segura</li>
          <li>{CHECK} Equipo con médico y nutricionistas coordinados</li>
          <li>{CHECK} Valoración nutricional con base clínica, no solo estética</li>
          <li>{CHECK} Planes realistas, revisables y sin prohibiciones absolutas</li>
        </ul>
      </div>
      <div class="split-media reveal">
        <img src="./assets/consulta.png" alt="Escritorio de consulta con cuaderno de notas, cinta métrica y un vaso de agua con limón" loading="lazy">
      </div>
    </div>
  </section>

  <section class="section section--offset">
    <div class="wrap">
      <div class="header-block center">
        <span class="eyebrow" style="justify-content:center;">Proceso</span>
        <h2>Cómo es tu primera consulta</h2>
      </div>
      <div class="steps">
        <div class="step reveal">
          <span class="step-num">01</span>
          <h3>Reserva</h3>
          <p style="font-size:var(--text-sm);">Eliges cita por videollamada (o presencial si lo prefieres) según tu disponibilidad.</p>
        </div>
        <div class="step reveal">
          <span class="step-num">02</span>
          <h3>Valoración</h3>
          <p style="font-size:var(--text-sm);">Revisamos tu historia clínica, hábitos y objetivos con calma.</p>
        </div>
        <div class="step reveal">
          <span class="step-num">03</span>
          <h3>Plan</h3>
          <p style="font-size:var(--text-sm);">Recibes un plan de alimentación personalizado y comprensible.</p>
        </div>
        <div class="step reveal">
          <span class="step-num">04</span>
          <h3>Seguimiento</h3>
          <p style="font-size:var(--text-sm);">Ajustamos el plan en revisiones periódicas según tu progreso.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--offset">
    <div class="wrap">
      <div class="header-block center">
        <span class="eyebrow" style="justify-content:center;">Planes y precios</span>
        <h2>Elige el nivel de acompañamiento que necesitas</h2>
        <p>Desde un plan generado al instante hasta la valoración conjunta con nutricionista y médico. Puedes empezar por el más sencillo y subir de nivel cuando lo necesites.</p>
      </div>
      <div class="grid grid--3">
        <div class="card pricing-card reveal">
          <span class="pricing-name">Plan Digital</span>
          <p class="pricing-tagline">Autogestionado, sin intervención profesional salvo que lo solicites</p>
          <div class="pricing-amount"><strong>9,90 €</strong><span>/ mes, sin permanencia</span></div>
          <p class="pricing-secondary">Introduces tus datos y la web genera tu plan al instante</p>
          <a href="precios.html#planes" class="btn btn--ghost pricing-cta">Ver detalles</a>
        </div>
        <div class="card pricing-card pricing-card--featured reveal">
          <span class="badge pricing-badge">Más solicitado</span>
          <span class="pricing-name">Plan Nutrición Online</span>
          <p class="pricing-tagline">Teleconsulta con nutricionista, incluye dietas especiales</p>
          <div class="pricing-amount"><strong>45 €</strong><span>primera consulta</span></div>
          <p class="pricing-secondary">Seguimientos desde 30 € · celiaquía, alergias e intolerancias sin coste adicional</p>
          <a href="precios.html#planes" class="btn btn--primary pricing-cta">Ver detalles</a>
        </div>
        <div class="card pricing-card reveal">
          <span class="pricing-name">Plan Médico + Nutrición</span>
          <p class="pricing-tagline">Valoración conjunta cuando el caso necesita más precisión</p>
          <div class="pricing-amount"><strong>89 €</strong><span>valoración inicial</span></div>
          <p class="pricing-secondary">Seguimientos desde 49 € · nutricionista y médico internista coordinados</p>
          <a href="precios.html#planes" class="btn btn--ghost pricing-cta">Ver detalles</a>
        </div>
      </div>
      <p class="pricing-note">Precios orientativos 2026, a confirmar por el equipo antes de publicarse de forma definitiva. <a href="precios.html">Ver todos los planes y qué incluye cada uno →</a></p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="quote-block reveal" style="max-width:720px;margin-inline:auto;text-align:center;border-left:none;">
        <p>“Un plan de alimentación solo funciona si se entiende por qué se recomienda y se ajusta a la vida real de cada paciente.”</p>
        <span class="quote-cite">Filosofía de trabajo — Minutrisalud</span>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="app-teaser reveal">
        <div class="app-teaser-copy">
          <span class="badge">Próximamente</span>
          <h2>La app Minutrisalud está en camino</h2>
          <p>Estamos preparando una aplicación para llevar tu plan de alimentación, registrar tu seguimiento y comunicarte con la consulta desde el móvil.</p>
          <a href="app.html" class="btn btn--ghost" style="margin-top:var(--space-4);width:fit-content;">Ver adelanto de la app</a>
        </div>
        <div class="app-teaser-media">
          <img src="./assets/app-preview.png" alt="Vista previa conceptual de la futura app Minutrisalud en un teléfono móvil" loading="lazy">
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="cta-band reveal">
        <h2>Empecemos por entender cómo comes hoy</h2>
        <p style="max-width:520px;margin-inline:auto;margin-bottom:var(--space-6);">Reserva tu primera valoración y recibe un plan pensado para tu salud, no para una talla.</p>
        <div style="display:flex;gap:var(--space-4);justify-content:center;flex-wrap:wrap;">
          <a href="contacto.html" class="btn" style="background:var(--color-bg);color:var(--color-primary);">Reservar consulta online</a>
          <a href="servicios.html" class="btn btn--ghost">Ver todos los servicios</a>
        </div>
      </div>
    </div>
  </section>
'''

build(
    "/home/user/workspace/minutrisalud/index.html",
    "Minutrisalud — Consulta de nutrición online con criterio médico",
    "Minutrisalud: consulta de nutrición online por videollamada, con equipo médico y nutricionistas. Valoración, planes personalizados y seguimiento — también presencial si lo prefieres.",
    "Inicio",
    index_body,
)
print("index built")


# ============================================================
# SERVICIOS
# ============================================================
servicios_body = f'''
  <section class="page-hero">
    <div class="wrap wrap--narrow">
      <span class="eyebrow" style="justify-content:center;">Servicios</span>
      <h1>Consulta de nutrición online, paso a paso</h1>
      <p class="lede" style="margin-inline:auto;text-align:center;">Atendemos principalmente por videollamada; cada servicio puede solicitarse de forma individual o como parte de un seguimiento continuado. También disponible de forma presencial si lo prefieres.</p>
    </div>
  </section>

  <section class="section" id="teleconsulta">
    <div class="wrap split">
      <div class="reveal">
        <span class="eyebrow">01 — Cómo atendemos</span>
        <h2>Teleconsulta: nuestro canal principal</h2>
        <p style="margin-bottom:var(--space-6);">Valoración, plan y seguimiento por videollamada, con la misma calidad de atención que una consulta presencial y sin necesidad de desplazamiento.</p>
        <ul class="check-list">
          <li>{CHECK} Videollamada segura desde cualquier dispositivo</li>
          <li>{CHECK} Mismo formato de valoración y ajuste de plan</li>
          <li>{CHECK} Ideal para primeras visitas y revisiones periódicas</li>
        </ul>
        <a href="contacto.html" class="btn btn--primary" style="margin-top:var(--space-6);">Reservar teleconsulta</a>
      </div>
      <div class="split-media reveal">
        <img src="./assets/app-preview.png" alt="Concepto de seguimiento nutricional desde el móvil" loading="lazy">
      </div>
    </div>
  </section>

  <section class="section section--offset" id="valoracion">
    <div class="wrap split">
      <div class="reveal">
        <span class="eyebrow">02 — Primera visita</span>
        <h2>Valoración nutricional completa</h2>
        <p style="margin-bottom:var(--space-6);">Revisamos tu historia clínica, antecedentes, medicación habitual y hábitos alimentarios. Incluye valoración antropométrica y, cuando es relevante, revisión de analíticas recientes.</p>
        <ul class="check-list">
          <li>{CHECK} Duración aproximada: 60 minutos</li>
          <li>{CHECK} Historia clínica y antecedentes familiares</li>
          <li>{CHECK} Valoración antropométrica y de composición corporal</li>
          <li>{CHECK} Definición conjunta de objetivos realistas</li>
        </ul>
      </div>
      <div class="split-media reveal">
        <img src="./assets/consulta.png" alt="Mesa de consulta con cuaderno de notas y material de valoración" loading="lazy">
      </div>
    </div>
  </section>

  <section class="section" id="planes">
    <div class="wrap split reverse">
      <div class="split-media reveal">
        <img src="./assets/plan.png" alt="Planificación semanal de comidas con ingredientes naturales sobre una mesa de madera" loading="lazy">
      </div>
      <div class="reveal">
        <span class="eyebrow">03 — Plan de alimentación</span>
        <h2>Planes personalizados, no plantillas</h2>
        <p style="margin-bottom:var(--space-6);">A partir de la valoración, se diseña un plan de alimentación adaptado a tu situación clínica, tus gustos, tu presupuesto y tu rutina diaria — con raciones y sustituciones claras.</p>
        <ul class="check-list">
          <li>{CHECK} Adaptado a patologías (diabetes, hipertensión, dislipemia, etc.)</li>
          <li>{CHECK} Opciones y sustituciones para el día a día</li>
          <li>{CHECK} Recomendaciones prácticas, sin prohibiciones absolutas</li>
          <li>{CHECK} Entrega en documento claro y fácil de seguir</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section section--offset" id="seguimiento">
    <div class="wrap">
      <div class="header-block center">
        <span class="eyebrow" style="justify-content:center;">04 — Continuidad</span>
        <h2>Seguimiento y control</h2>
        <p>El plan se revisa y ajusta con el tiempo, no se entrega y se olvida.</p>
      </div>
      <div class="grid grid--3">
        <div class="card reveal">
          <div class="card-icon">{icon('calendar')}</div>
          <h3>Revisiones periódicas</h3>
          <p>Citas de seguimiento cada 2-4 semanas para valorar evolución y ajustar el plan.</p>
        </div>
        <div class="card reveal">
          <div class="card-icon">{icon('chart')}</div>
          <h3>Indicadores objetivos</h3>
          <p>Seguimiento de peso, composición corporal y parámetros clínicos relevantes.</p>
        </div>
        <div class="card reveal">
          <div class="card-icon">{icon('heart')}</div>
          <h3>Coordinación clínica</h3>
          <p>Comunicación con otras especialidades cuando el caso lo requiere.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="cta-band reveal">
        <h2>¿Con cuál servicio quieres empezar?</h2>
        <p style="max-width:520px;margin-inline:auto;margin-bottom:var(--space-6);">Cuéntanos tu situación y te orientamos sobre el mejor punto de partida.</p>
        <a href="contacto.html" class="btn" style="background:var(--color-bg);color:var(--color-primary);">Escríbenos</a>
      </div>
    </div>
  </section>
'''

build(
    "/home/user/workspace/minutrisalud/servicios.html",
    "Servicios — Minutrisalud",
    "Teleconsulta como canal principal, valoración nutricional, planes de alimentación personalizados y seguimiento periódico en Minutrisalud.",
    "Servicios",
    servicios_body,
)
print("servicios built")


# ============================================================
# PRECIOS
# ============================================================
precios_body = f'''
  <section class="page-hero">
    <div class="wrap wrap--narrow">
      <span class="eyebrow" style="justify-content:center;">Planes y precios</span>
      <h1>Un plan para cada nivel de acompañamiento</h1>
      <p class="lede" style="margin-inline:auto;text-align:center;">Empieza por donde necesites: un plan automático al instante, una teleconsulta con nutricionista, o una valoración conjunta con nutricionista y médico. Puedes subir de nivel en cualquier momento.</p>
    </div>
  </section>

  <section class="section" id="planes">
    <div class="wrap">
      <div class="grid grid--3">
        <div class="card pricing-card reveal">
          <span class="pricing-name">Plan Digital</span>
          <p class="pricing-tagline">100% autoguiado. Sin intervención de nutricionista ni médico, salvo que tú la solicites.</p>
          <div class="pricing-amount"><strong>9,90 €</strong><span>/ mes, sin permanencia</span></div>
          <p class="pricing-secondary">También disponible por 89 €/año (equivale a 2 meses gratis)</p>
          <ul class="pricing-list">
            <li>{CHECK} Introduces tus datos: peso, altura, medidas, patologías previas y tratamiento actual</li>
            <li>{CHECK} La web genera tu plan nutricional completo al instante</li>
            <li>{CHECK} Seguimiento automatizado con ajustes periódicos según tu evolución</li>
            <li>{CHECK} Puedes solicitar consulta con nutricionista o médico en cualquier momento</li>
          </ul>
          <a href="pago.html?plan=digital" class="btn btn--ghost pricing-cta">Contratar Plan Digital</a>
        </div>

        <div class="card pricing-card pricing-card--featured reveal">
          <span class="badge pricing-badge">Más solicitado</span>
          <span class="pricing-name">Plan Nutrición Online</span>
          <p class="pricing-tagline">Teleconsulta con nutricionista para recomendaciones según tus patologías.</p>
          <div class="pricing-amount"><strong>45 €</strong><span>primera consulta (45-60 min)</span></div>
          <p class="pricing-secondary">Seguimientos desde 30 € · Bono 4 seguimientos: 110 €</p>
          <ul class="pricing-list">
            <li>{CHECK} Videoconsulta con nutricionista colegiada</li>
            <li>{CHECK} Valoración según tus patologías y objetivos</li>
            <li>{CHECK} Dieta adaptada a necesidades especiales: celiaquía, alergias, intolerancias u otras, sin coste adicional</li>
            <li>{CHECK} Si se necesita una valoración clínica más precisa, se deriva a consulta médica</li>
          </ul>
          <a href="pago.html?plan=nutricion" class="btn btn--primary pricing-cta">Contratar Plan Nutrición</a>
        </div>

        <div class="card pricing-card reveal">
          <span class="pricing-name">Plan Médico + Nutrición</span>
          <p class="pricing-tagline">Valoración conjunta con nutricionista y médico internista para casos que necesitan más precisión.</p>
          <div class="pricing-amount"><strong>89 €</strong><span>valoración inicial conjunta</span></div>
          <p class="pricing-secondary">Seguimientos desde 49 € · incluye coordinación entre especialidades</p>
          <ul class="pricing-list">
            <li>{CHECK} Teleconsulta con médico internista además de nutricionista</li>
            <li>{CHECK} Valoración clínica más precisa: antecedentes, medicación y analíticas</li>
            <li>{CHECK} Plan de alimentación y, si procede, orientación terapéutica coordinada</li>
            <li>{CHECK} Seguimiento combinado entre ambas especialidades</li>
          </ul>
          <a href="pago.html?plan=medico" class="btn btn--ghost pricing-cta">Contratar Plan Médico</a>
        </div>
      </div>

      <div class="pricing-flow reveal">
        <span class="pricing-flow-step">1. Plan Digital</span>
        <span class="pricing-flow-arrow">→</span>
        <span class="pricing-flow-step">2. ¿No es suficiente? Nutrición Online</span>
        <span class="pricing-flow-arrow">→</span>
        <span class="pricing-flow-step">3. ¿Necesitas más precisión? Médico + Nutrición</span>
      </div>

      <p class="pricing-note">Precios orientativos para 2026, calculados a partir de tarifas de mercado de servicios equivalentes. Deben confirmarse y ajustarse antes de la publicación definitiva. El pago se realiza de forma segura al contratar cada plan.</p>
    </div>
  </section>

  <section class="section section--offset">
    <div class="wrap">
      <div class="header-block center">
        <span class="eyebrow" style="justify-content:center;">Preguntas frecuentes</span>
        <h2>Sobre los planes y el pago</h2>
      </div>
      <div class="grid grid--3">
        <div class="card reveal">
          <div class="card-icon">{icon('scale')}</div>
          <h3>¿Puedo cambiar de plan?</h3>
          <p>Sí. Puedes empezar por el Plan Digital y pasar a una teleconsulta con nutricionista o médico cuando lo necesites, sin perder tus datos ya introducidos.</p>
        </div>
        <div class="card reveal">
          <div class="card-icon">{icon('leaf')}</div>
          <h3>¿Las dietas especiales tienen coste extra?</h3>
          <p>No. La adaptación a celiaquía, alergias, intolerancias u otras necesidades especiales está incluida en el Plan Nutrición Online y en el Plan Médico + Nutrición.</p>
        </div>
        <div class="card reveal">
          <div class="card-icon">{icon('video')}</div>
          <h3>¿Cómo se realiza el pago?</h3>
          <p>El pago se gestiona de forma segura al contratar el plan, antes de la teleconsulta o de recibir el plan automatizado. Aceptamos tarjeta de crédito y débito.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="cta-band reveal">
        <h2>¿Con qué plan quieres empezar?</h2>
        <p style="max-width:520px;margin-inline:auto;margin-bottom:var(--space-6);">Elige tu plan y accede a la pasarela de pago segura para contratarlo.</p>
        <div style="display:flex;gap:var(--space-4);justify-content:center;flex-wrap:wrap;">
          <a href="pago.html" class="btn" style="background:var(--color-bg);color:var(--color-primary);">Ir a la plataforma de pago</a>
          <a href="contacto.html" class="btn btn--ghost">Tengo dudas antes de contratar</a>
        </div>
      </div>
    </div>
  </section>
'''

build(
    "/home/user/workspace/minutrisalud/precios.html",
    "Planes y precios — Minutrisalud",
    "Compara los planes de Minutrisalud: Plan Digital autoguiado, Plan Nutrición Online con teleconsulta y dietas especiales, y Plan Médico + Nutrición con valoración conjunta.",
    "Planes y precios",
    precios_body,
)
print("precios built")

# ============================================================
# PAGO (plataforma de pago)
# ============================================================
pago_body = f'''
  <section class="page-hero">
    <div class="wrap wrap--narrow">
      <span class="eyebrow" style="justify-content:center;">Plataforma de pago</span>
      <h1>Contrata tu plan de forma segura</h1>
      <p class="lede" style="margin-inline:auto;text-align:center;">Elige el plan, revisa el resumen y confirma el pago. Recibirás la confirmación por correo y, según el plan, accederás a tu cuestionario, a la reserva de videollamada o a ambos.</p>
    </div>
  </section>

  <section class="section--tight">
    <div class="wrap">
      <div class="demo-banner">
        {icon('phone')}
        <span>Esta es una vista de demostración de la plataforma de pago. La pasarela de cobro real (tarjeta) se activará antes de publicar la web de forma definitiva; de momento, al confirmar se registra tu solicitud y el equipo te contacta para finalizar el pago.</span>
      </div>

      <div class="checkout-grid">
        <div class="reveal">
          <form id="checkout-form" class="form">
            <h3 style="margin-bottom:var(--space-5);">1. Elige tu plan</h3>
            <div class="plan-options">
              <label class="plan-option">
                <input type="radio" name="plan" value="digital" data-price="9,90 €/mes" data-label="Plan Digital">
                <div class="plan-option-body">
                  <strong>Plan Digital</strong>
                  <span>Autoguiado, sin intervención profesional salvo que la solicites</span>
                </div>
                <span class="plan-option-price">9,90 €/mes</span>
              </label>
              <label class="plan-option">
                <input type="radio" name="plan" value="nutricion" data-price="45 €" data-label="Plan Nutrición Online" checked>
                <div class="plan-option-body">
                  <strong>Plan Nutrición Online</strong>
                  <span>Teleconsulta con nutricionista, incluye dietas especiales</span>
                </div>
                <span class="plan-option-price">45 €</span>
              </label>
              <label class="plan-option">
                <input type="radio" name="plan" value="medico" data-price="89 €" data-label="Plan Médico + Nutrición">
                <div class="plan-option-body">
                  <strong>Plan Médico + Nutrición</strong>
                  <span>Valoración conjunta con nutricionista y médico internista</span>
                </div>
                <span class="plan-option-price">89 €</span>
              </label>
            </div>

            <hr class="form-divider">

            <h3 style="margin-bottom:var(--space-5);">2. Tus datos</h3>
            <div class="form-grid">
              <div class="form-field">
                <label for="pago-name">Nombre completo</label>
                <input type="text" id="pago-name" name="name" required placeholder="Tu nombre">
              </div>
              <div class="form-field">
                <label for="pago-email">Correo electrónico</label>
                <input type="email" id="pago-email" name="email" required placeholder="tu@email.com">
              </div>
              <div class="form-field full">
                <label for="pago-phone">Teléfono</label>
                <input type="tel" id="pago-phone" name="phone" required placeholder="+34 600 000 000">
              </div>
            </div>

            <hr class="form-divider">

            <h3 style="margin-bottom:var(--space-5);">3. Pago</h3>
            <div class="form-grid">
              <div class="form-field full">
                <label for="pago-card">Número de tarjeta</label>
                <input type="text" id="pago-card" name="card" inputmode="numeric" placeholder="0000 0000 0000 0000">
              </div>
              <div class="form-field">
                <label for="pago-exp">Caducidad</label>
                <input type="text" id="pago-exp" name="exp" placeholder="MM/AA">
              </div>
              <div class="form-field">
                <label for="pago-cvc">CVC</label>
                <input type="text" id="pago-cvc" name="cvc" inputmode="numeric" placeholder="123">
              </div>
            </div>

            <button type="submit" class="btn btn--primary" style="width:100%;margin-top:var(--space-6);">Confirmar y pagar</button>
            <p style="margin-top:var(--space-3);font-size:var(--text-xs);color:var(--color-text-muted);">Al confirmar, aceptas nuestros términos de servicio. Pago procesado de forma segura.</p>
          </form>

          <div id="checkout-success" class="card checkout-success reveal" hidden>
            <div class="card-icon" style="margin:0 auto;">{icon('heart')}</div>
            <h2>¡Solicitud recibida!</h2>
            <p id="checkout-success-detail" style="max-width:420px;margin-inline:auto;"></p>
            <a href="index.html" class="btn btn--ghost" style="margin-top:var(--space-6);">Volver al inicio</a>
          </div>
        </div>

        <aside class="reveal">
          <div class="order-summary">
            <h3>Resumen del pedido</h3>
            <div class="order-summary-row">
              <span id="summary-plan-name">Plan Nutrición Online</span>
              <span id="summary-plan-price">45 €</span>
            </div>
            <div class="order-summary-row">
              <span>Impuestos</span>
              <span>Incluidos</span>
            </div>
            <div class="order-summary-row total">
              <span>Total hoy</span>
              <span id="summary-total">45 €</span>
            </div>
            <div class="order-summary-note">
              {icon('scale')}
              <span>Los planes con teleconsulta se facturan por sesión; el Plan Digital se renueva mensualmente y puedes cancelarlo cuando quieras.</span>
            </div>
          </div>
        </aside>
      </div>
    </div>
  </section>
'''

build(
    "/home/user/workspace/minutrisalud/pago.html",
    "Pago y contratación — Minutrisalud",
    "Contrata tu plan Minutrisalud de forma segura: Plan Digital, Plan Nutrición Online o Plan Médico + Nutrición.",
    "Planes y precios",
    pago_body,
)
print("pago built")


# ============================================================
# EQUIPO
# ============================================================
sobre_body = f'''
  <section class="page-hero">
    <div class="wrap wrap--narrow">
      <span class="eyebrow" style="justify-content:center;">Equipo</span>
      <h1>Medicina interna y nutrición clínica, coordinadas</h1>
      <p class="lede" style="margin-inline:auto;text-align:center;">Un equipo de tres profesionales que atiende principalmente por teleconsulta, para que la valoración médica y el seguimiento nutricional vayan siempre de la mano.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="grid grid--3">
        <div class="card team-card reveal">
          <div class="team-avatar">JS</div>
          <span class="team-role">Medicina interna</span>
          <h3>Dr. Jesús Santiago</h3>
          <p>Coordinación médica de Minutrisalud. Aporta la valoración clínica de base — antecedentes, medicación y analíticas — sobre la que se construye cada plan de alimentación.</p>
        </div>
        <div class="card team-card reveal">
          <div class="team-avatar">RS</div>
          <span class="team-role">Nutricionista</span>
          <h3>Raquel Santiago Carrasco</h3>
          <p>Diseño de planes de alimentación personalizados y acompañamiento en el seguimiento nutricional, adaptados a la situación clínica y la rutina de cada paciente.</p>
        </div>
        <div class="card team-card reveal">
          <div class="team-avatar">SM</div>
          <span class="team-role">Nutricionista</span>
          <h3>Saida Mohamed Mohamed</h3>
          <p>Valoración nutricional y consulta de seguimiento, con atención cercana a las revisiones periódicas y al ajuste continuado de los planes.</p>
        </div>
      </div>
      <p style="font-size:var(--text-xs);color:var(--color-text-faint);margin-top:var(--space-8);text-align:center;">Estos perfiles son orientativos y pueden ampliarse con formación específica, colegiatura y años de experiencia de cada profesional.</p>
    </div>
  </section>

  <section class="section section--offset">
    <div class="wrap split">
      <div class="split-media reveal">
        <img src="./assets/consulta.png" alt="Espacio de consulta con ambiente cálido y natural" loading="lazy">
      </div>
      <div class="reveal">
        <span class="eyebrow">Cómo trabajamos</span>
        <h2>La alimentación, una herramienta terapéutica más</h2>
        <p style="margin-bottom:var(--space-4);">Minutrisalud nace de la idea de que la nutrición funciona mejor cuando se apoya en criterio médico y seguimiento cercano. El equipo atiende principalmente por videollamada, coordinando la mirada médica y nutricional en cada valoración, plan y revisión.</p>
        <p>Esta forma de trabajar se aplica tanto en pacientes con patologías crónicas como en quienes buscan mejorar sus hábitos con acompañamiento profesional.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="header-block center">
        <span class="eyebrow" style="justify-content:center;">Enfoque</span>
        <h2>Principios de trabajo</h2>
      </div>
      <div class="grid grid--3">
        <div class="card reveal">
          <div class="card-icon">{icon('heart')}</div>
          <h3>Mirada clínica integral</h3>
          <p>La alimentación se valora junto con el resto de tu historia de salud, no de forma aislada.</p>
        </div>
        <div class="card reveal">
          <div class="card-icon">{icon('leaf')}</div>
          <h3>Planes sostenibles</h3>
          <p>Cambios que puedan mantenerse en el tiempo, adaptados a tu vida real.</p>
        </div>
        <div class="card reveal">
          <div class="card-icon">{icon('chart')}</div>
          <h3>Decisiones con datos</h3>
          <p>Seguimiento con indicadores objetivos para ajustar el plan cuando haga falta.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--offset">
    <div class="wrap">
      <div class="quote-block reveal" style="max-width:720px;margin-inline:auto;text-align:center;border-left:none;">
        <p>“Nuestro objetivo no es que sigas una dieta perfecta durante dos semanas, sino que comas mejor durante años — con el equipo médico y nutricional acompañándote por videollamada.”</p>
        <span class="quote-cite">Equipo Minutrisalud</span>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="cta-band reveal">
        <h2>¿Empezamos con tu valoración?</h2>
        <a href="contacto.html" class="btn" style="background:var(--color-bg);color:var(--color-primary);margin-top:var(--space-4);">Reservar consulta online</a>
      </div>
    </div>
  </section>
'''

build(
    "/home/user/workspace/minutrisalud/equipo.html",
    "Equipo — Minutrisalud",
    "Conoce al equipo de Minutrisalud: medicina interna y nutrición clínica coordinadas, con atención principalmente online.",
    "Equipo",
    sobre_body,
)
print("equipo built")


# ============================================================
# APP MINUTRISALUD (integration-ready placeholder)
# ============================================================
app_body = f'''
  <section class="page-hero">
    <div class="wrap wrap--narrow">
      <span class="badge" style="margin-inline:auto;">En construcción</span>
      <h1>La app Minutrisalud</h1>
      <p class="lede" style="margin-inline:auto;text-align:center;">Tu plan de alimentación, tu seguimiento y tu consulta, en el móvil. Esta sección ya está preparada para conectar la aplicación en cuanto esté lista.</p>
    </div>
  </section>

  <section class="section--tight">
    <div class="wrap">
      <div class="grid grid--3">
        <div class="card reveal">
          <div class="card-icon">{icon('leaf')}</div>
          <h3>Tu plan siempre a mano</h3>
          <p>Consulta tus comidas, raciones y sustituciones desde el móvil, en cualquier momento.</p>
        </div>
        <div class="card reveal">
          <div class="card-icon">{icon('chart')}</div>
          <h3>Registro de seguimiento</h3>
          <p>Anota peso, sensaciones y cumplimiento para que cada revisión sea más precisa.</p>
        </div>
        <div class="card reveal">
          <div class="card-icon">{icon('video')}</div>
          <h3>Contacto con la consulta</h3>
          <p>Mensajes y recordatorios de cita conectados directamente con Minutrisalud.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap wrap--narrow">
      <!--
        PUNTO DE INTEGRACIÓN — App Minutrisalud
        ==========================================================
        Este contenedor está preparado para alojar la futura app de nutrición.
        Opciones al conectarla:

        1) Insertar la app como iframe (si es una web app):
           <iframe id="app-embed" src="https://app.minutrisalud.com"
             style="width:100%;height:640px;border:0;border-radius:var(--radius-lg);"
             title="App Minutrisalud"></iframe>

        2) Sustituir por botones de descarga (si es app nativa iOS/Android):
           <a href="https://apps.apple.com/..." target="_blank" rel="noopener noreferrer" class="btn btn--primary">Descargar en App Store</a>
           <a href="https://play.google.com/..." target="_blank" rel="noopener noreferrer" class="btn btn--primary">Descargar en Google Play</a>

        3) Insertar un widget/script embebido del proveedor de la app, si aplica.

        El div#app-embed-container es el único elemento que hay que sustituir; el resto de la
        página (cabecera, texto, tarjetas de beneficios y pie) no requiere cambios.
      -->
      <div id="app-embed-container" class="reveal">
        <div>
          <div class="placeholder-icon">{icon('smartphone')}</div>
          <h3 style="margin-bottom:var(--space-2);">Aquí se integrará la app Minutrisalud</h3>
          <p style="font-size:var(--text-sm);max-width:46ch;margin-inline:auto;">Este espacio está listo para alojar la aplicación (como iframe, enlaces de descarga o widget) en cuanto esté publicada.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap wrap--narrow" style="text-align:center;">
      <h2>Sé de los primeros en probarla</h2>
      <p class="lede" style="margin-inline:auto;margin-bottom:var(--space-8);">Déjanos tu correo y te avisaremos en cuanto la app Minutrisalud esté disponible.</p>
      <form id="notify-form" style="display:flex;gap:var(--space-3);max-width:440px;margin-inline:auto;flex-wrap:wrap;justify-content:center;">
        <input type="email" required placeholder="tu@email.com" aria-label="Correo electrónico" style="flex:1;min-width:220px;background:var(--color-surface);border:1px solid var(--color-border);border-radius:var(--radius-full);padding:0.75em 1.4em;font-size:var(--text-base);color:var(--color-text);">
        <button type="submit" class="btn btn--primary">Avisarme</button>
      </form>
      <p id="notify-note" hidden style="margin-top:var(--space-4);font-size:var(--text-sm);color:var(--color-primary);">Gracias — te avisaremos en cuanto esté disponible.</p>
    </div>
  </section>
'''

build(
    "/home/user/workspace/minutrisalud/app.html",
    "App Minutrisalud — Próximamente",
    "La app Minutrisalud está en camino: sigue tu plan de alimentación y tu seguimiento desde el móvil. Página lista para integrar la aplicación.",
    "App Minutrisalud",
    app_body,
)
print("app built")


# ============================================================
# CONTACTO
# ============================================================
contacto_body = f'''
  <section class="page-hero">
    <div class="wrap wrap--narrow">
      <span class="eyebrow" style="justify-content:center;">Contacto</span>
      <h1>Reserva tu consulta online</h1>
      <p class="lede" style="margin-inline:auto;text-align:center;">Escríbenos y te responderemos para concretar tu videollamada. Si prefieres una visita presencial, también puedes indicarlo.</p>
    </div>
  </section>

  <section class="section--tight">
    <div class="wrap split">
      <div class="reveal">
        <form id="contact-form" class="form">
          <div class="form-grid">
            <div class="form-field">
              <label for="name">Nombre</label>
              <input type="text" id="name" name="name" required placeholder="Tu nombre">
            </div>
            <div class="form-field">
              <label for="email">Correo electrónico</label>
              <input type="email" id="email" name="email" required placeholder="tu@email.com">
            </div>
            <div class="form-field full">
              <label for="phone">Teléfono (opcional)</label>
              <input type="tel" id="phone" name="phone" placeholder="+34 600 000 000">
            </div>
            <div class="form-field full">
              <label for="service">Servicio de interés</label>
              <select id="service" name="service">
                <option>Teleconsulta</option>
                <option>Valoración nutricional inicial</option>
                <option>Plan personalizado</option>
                <option>Seguimiento</option>
                <option>Consulta presencial</option>
                <option>Otro</option>
              </select>
            </div>
            <div class="form-field full">
              <label for="message">Mensaje</label>
              <textarea id="message" name="message" rows="5" placeholder="Cuéntanos brevemente tu situación y disponibilidad"></textarea>
            </div>
          </div>
          <button type="submit" class="btn btn--primary" style="width:100%;">Enviar solicitud</button>
          <p id="form-note" hidden style="margin-top:var(--space-3);font-size:var(--text-sm);color:var(--color-primary);">Gracias — se abrirá tu cliente de correo para enviar la solicitud.</p>
        </form>
      </div>

      <div class="reveal">
        <div class="contact-info-card contact-info-list">
          <h3 style="margin-bottom:var(--space-5);">Información práctica</h3>
          <div class="contact-info-item">
            <span class="contact-info-icon">{icon('video')}</span>
            <div>
              <strong>Modalidad</strong>
              <p>Principalmente online, por videollamada. Consulta presencial disponible bajo petición.</p>
            </div>
          </div>
          <div class="contact-info-item">
            <span class="contact-info-icon">{icon('mail')}</span>
            <div>
              <strong>Correo</strong>
              <p><a href="mailto:hola@minutrisalud.com">hola@minutrisalud.com</a></p>
            </div>
          </div>
          <div class="contact-info-item">
            <span class="contact-info-icon">{icon('phone')}</span>
            <div>
              <strong>Teléfono</strong>
              <p>A confirmar</p>
            </div>
          </div>
          <div class="contact-info-item">
            <span class="contact-info-icon">{icon('pin')}</span>
            <div>
              <strong>Ubicación (consulta presencial)</strong>
              <p>Dirección a confirmar</p>
            </div>
          </div>
          <div class="contact-info-item">
            <span class="contact-info-icon">{icon('clock')}</span>
            <div>
              <strong>Horario orientativo</strong>
              <p>Lunes a viernes, mañana y tarde (a confirmar)</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
'''

build(
    "/home/user/workspace/minutrisalud/contacto.html",
    "Contacto — Minutrisalud",
    "Reserva tu consulta de nutrición online con Minutrisalud, por videollamada; también disponible de forma presencial.",
    "Contacto",
    contacto_body,
)
print("contacto built")
