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
        <span class="eyebrow">Consulta de nutrición clínica</span>
        <h1>Nutrición con criterio médico, hecha a tu medida</h1>
        <p class="lede">Minutrisalud acompaña tu alimentación con valoración clínica, planes personalizados y seguimiento cercano — presencial o por teleconsulta.</p>
        <div class="hero-actions">
          <a href="contacto.html" class="btn btn--primary">Reservar primera consulta</a>
          <a href="servicios.html" class="btn btn--ghost">Ver servicios</a>
        </div>
        <div class="hero-stats">
          <div>
            <span class="stat-num">+10</span>
            <span class="stat-label">años de práctica clínica</span>
          </div>
          <div>
            <span class="stat-num">100%</span>
            <span class="stat-label">planes individualizados</span>
          </div>
          <div>
            <span class="stat-num">Online</span>
            <span class="stat-label">y presencial</span>
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
        <p style="margin-bottom:var(--space-6);">Detrás de cada recomendación hay criterio médico: se tienen en cuenta tus antecedentes, tu medicación y tus analíticas, coordinando la alimentación con el resto de tu cuidado.</p>
        <ul class="check-list">
          <li>{CHECK} Valoración nutricional con base clínica, no solo estética</li>
          <li>{CHECK} Coordinación con otras especialidades cuando es necesario</li>
          <li>{CHECK} Planes realistas, revisables y sin prohibiciones absolutas</li>
          <li>{CHECK} Teleconsulta disponible para el seguimiento</li>
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
          <p style="font-size:var(--text-sm);">Eliges cita presencial o por videollamada según tu disponibilidad.</p>
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
          <a href="contacto.html" class="btn" style="background:var(--color-bg);color:var(--color-primary);">Reservar consulta</a>
          <a href="servicios.html" class="btn btn--ghost">Ver todos los servicios</a>
        </div>
      </div>
    </div>
  </section>
'''

build(
    "/home/user/workspace/minutrisalud/index.html",
    "Minutrisalud — Consulta de nutrición clínica personalizada",
    "Minutrisalud: consulta de nutrición con criterio médico. Valoración, planes personalizados y seguimiento presencial o por teleconsulta.",
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
      <h1>Consulta de nutrición, paso a paso</h1>
      <p class="lede" style="margin-inline:auto;text-align:center;">Cada servicio puede solicitarse de forma individual o como parte de un seguimiento continuado.</p>
    </div>
  </section>

  <section class="section" id="valoracion">
    <div class="wrap split">
      <div class="reveal">
        <span class="eyebrow">01 — Primera visita</span>
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

  <section class="section section--offset" id="planes">
    <div class="wrap split reverse">
      <div class="split-media reveal">
        <img src="./assets/plan.png" alt="Planificación semanal de comidas con ingredientes naturales sobre una mesa de madera" loading="lazy">
      </div>
      <div class="reveal">
        <span class="eyebrow">02 — Plan de alimentación</span>
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

  <section class="section" id="seguimiento">
    <div class="wrap">
      <div class="header-block center">
        <span class="eyebrow" style="justify-content:center;">03 — Continuidad</span>
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

  <section class="section section--offset" id="teleconsulta">
    <div class="wrap split">
      <div class="reveal">
        <span class="eyebrow">04 — Flexibilidad</span>
        <h2>Teleconsulta cuando la necesites</h2>
        <p style="margin-bottom:var(--space-6);">Las visitas de seguimiento pueden realizarse por videollamada, manteniendo la misma calidad de atención sin necesidad de desplazamiento.</p>
        <ul class="check-list">
          <li>{CHECK} Videollamada segura desde cualquier dispositivo</li>
          <li>{CHECK} Mismo formato de valoración y ajuste de plan</li>
          <li>{CHECK} Ideal para revisiones periódicas</li>
        </ul>
        <a href="contacto.html" class="btn btn--primary" style="margin-top:var(--space-6);">Reservar teleconsulta</a>
      </div>
      <div class="split-media reveal">
        <img src="./assets/app-preview.png" alt="Concepto de seguimiento nutricional desde el móvil" loading="lazy">
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
    "Valoración nutricional, planes de alimentación personalizados, seguimiento periódico y teleconsulta en Minutrisalud.",
    "Servicios",
    servicios_body,
)
print("servicios built")


# ============================================================
# SOBRE MÍ
# ============================================================
sobre_body = f'''
  <section class="page-hero">
    <div class="wrap wrap--narrow">
      <span class="eyebrow" style="justify-content:center;">Sobre mí</span>
      <h1>Medicina interna y nutrición clínica</h1>
    </div>
  </section>

  <section class="section">
    <div class="wrap split">
      <div class="split-media reveal">
        <img src="./assets/consulta.png" alt="Espacio de consulta con ambiente cálido y natural" loading="lazy">
      </div>
      <div class="reveal">
        <span class="eyebrow">Trayectoria</span>
        <h2>Dr. Jesús Santiago</h2>
        <p style="margin-bottom:var(--space-4);">Médico especialista en Medicina Interna, con dedicación particular a la nutrición clínica como parte del abordaje integral del paciente. Minutrisalud nace de la idea de que la alimentación es una herramienta terapéutica más, y que funciona mejor cuando se apoya en criterio médico y seguimiento cercano.</p>
        <p>A lo largo de la práctica clínica diaria, esta mirada se ha aplicado tanto en pacientes con patologías crónicas como en personas que simplemente buscan mejorar sus hábitos con acompañamiento profesional.</p>
        <p style="font-size:var(--text-xs);color:var(--color-text-faint);margin-top:var(--space-6);">Este perfil es orientativo y puede ampliarse con formación específica, colegiatura y años de experiencia.</p>
      </div>
    </div>
  </section>

  <section class="section section--offset">
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

  <section class="section">
    <div class="wrap">
      <div class="quote-block reveal" style="max-width:720px;margin-inline:auto;text-align:center;border-left:none;">
        <p>“Mi objetivo no es que sigas una dieta perfecta durante dos semanas, sino que comas mejor durante años.”</p>
        <span class="quote-cite">Dr. Jesús Santiago</span>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="cta-band reveal">
        <h2>¿Empezamos con tu valoración?</h2>
        <a href="contacto.html" class="btn" style="background:var(--color-bg);color:var(--color-primary);margin-top:var(--space-4);">Reservar consulta</a>
      </div>
    </div>
  </section>
'''

build(
    "/home/user/workspace/minutrisalud/sobre-mi.html",
    "Sobre mí — Minutrisalud",
    "Conoce el enfoque clínico y la trayectoria detrás de la consulta de nutrición Minutrisalud.",
    "Sobre mí",
    sobre_body,
)
print("sobre-mi built")


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
      <h1>Reserva tu consulta</h1>
      <p class="lede" style="margin-inline:auto;text-align:center;">Escríbenos y te responderemos para concretar el formato (presencial o teleconsulta) y la fecha.</p>
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
                <option>Valoración nutricional inicial</option>
                <option>Plan personalizado</option>
                <option>Seguimiento</option>
                <option>Teleconsulta</option>
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
              <strong>Ubicación</strong>
              <p>Consulta presencial y teleconsulta — dirección a confirmar</p>
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
    "Reserva tu consulta de nutrición con Minutrisalud, presencial o por teleconsulta.",
    "Contacto",
    contacto_body,
)
print("contacto built")
