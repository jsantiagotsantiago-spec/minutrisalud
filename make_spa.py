# -*- coding: utf-8 -*-
"""
Genera una versión "de una sola página" (SPA) de Minutrisalud.

Por qué existe este archivo:
La vista previa privada de Perplexity Computer (el recuadro que se ve dentro
de la conversación) tiene una limitación: al hacer clic en un enlace que
carga OTRO archivo .html, la navegación no funciona bien dentro de ese
recuadro. Para evitarlo, este script junta el contenido de todas las páginas
(index, servicios, consejos, calculadora, precios, pago, equipo, app,
nutrigest, contacto) en un ÚNICO archivo `index.html`. Cambiar de "página"
ya no recarga nada: un pequeño script en JavaScript simplemente muestra u
oculta la sección correspondiente y cambia la URL después de "#/" (por
ejemplo index.html#/servicios). Esto funciona siempre, tanto en la vista
previa como en cualquier navegador normal.

Cómo actualizar el contenido en el futuro:
1. Edita el contenido real en `make_site.py` (los textos, imágenes, etc.
   siguen viviendo ahí, en las variables *_body).
2. Vuelve a ejecutar: python3 make_site.py   (regenera las páginas clásicas,
   por si se quieren seguir usando de forma independiente)
3. Vuelve a ejecutar: python3 make_spa.py    (regenera el `index.html` único
   con navegación interna, que es el que se usa en la vista previa)
"""

import re
import importlib

import build_pages
import make_site  # ejecuta make_site.py y nos da acceso a sus variables *_body

BRAND_SVG = build_pages.BRAND_SVG

# slug interno -> (título de pestaña, variable de contenido, etiqueta de menú)
PAGES = [
    ("index", "Minutrisalud — Consulta de nutrición online con criterio médico", make_site.index_body, "Inicio"),
    ("servicios", "Servicios — Minutrisalud", make_site.servicios_body, "Servicios"),
    ("consejos", "Consejos — Nutrición y hábitos saludables | Minutrisalud", make_site.consejos_body, "Consejos"),
    ("calculadora", "Calculadora nutricional — IMC y necesidad calórica | Minutrisalud", make_site.calculadora_body, "Calculadora"),
    ("precios", "Planes y precios — Minutrisalud", make_site.precios_body, "Planes y precios"),
    ("pago", "Pago y contratación — Minutrisalud", make_site.pago_body, "Pago"),
    ("equipo", "Equipo — Minutrisalud", make_site.sobre_body, "Equipo"),
    ("app", "App Minutrisalud — Próximamente", make_site.app_body, "App Minutrisalud"),
    ("nutrigest", "NutriGest — gestión de la consulta (equipo)", make_site.nutrigest_body, "NutriGest"),
    ("contacto", "Contacto — Minutrisalud", make_site.contacto_body, "Contacto"),
    ("legal", "Aviso legal — Minutrisalud", make_site.legal_body, "Aviso legal"),
    ("privacidad", "Política de privacidad — Minutrisalud", make_site.privacidad_body, "Privacidad"),
    ("cookies", "Política de cookies — Minutrisalud", make_site.cookies_body, "Cookies"),
    ("terminos", "Términos y condiciones — Minutrisalud", make_site.terminos_body, "Términos y condiciones"),
]

SLUGS = {slug for slug, *_ in PAGES}

# Enlaces del menú principal (mismos 8 de siempre, pero ahora con # en vez de .html)
NAV_ITEMS = [
    ("Inicio", "index"),
    ("Servicios", "servicios"),
    ("Consejos", "consejos"),
    ("Calculadora", "calculadora"),
    ("Planes y precios", "precios"),
    ("Equipo", "equipo"),
    ("App Minutrisalud", "app"),
    ("Contacto", "contacto"),
]


def spa_header(active_slug):
    links = "\n".join(
        f'        <a href="#/{slug}" data-nav-link="{slug}"{" aria-current=\"page\"" if slug == active_slug else ""}>{label}</a>'
        for label, slug in NAV_ITEMS
    )
    mobile_links = "\n".join(
        f'      <a href="#/{slug}" data-nav-link="{slug}">{label}</a>' for label, slug in NAV_ITEMS
    )
    return f'''  <header class="header">
    <div class="wrap header-inner">
      <a href="#/index" class="brand" data-nav-link="index">
        {BRAND_SVG}
        <span class="brand-name">Minutrisalud</span>
      </a>
      <nav class="nav">
        <div class="nav-links">
{links}
        </div>
        <div class="nav-actions">
          <button class="theme-toggle" data-theme-toggle type="button"></button>
          <a href="#/contacto" class="btn btn--primary btn--sm" data-nav-link="contacto">Consulta online</a>
        </div>
        <button class="nav-toggle" aria-label="Abrir menú" type="button">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
        </button>
      </nav>
    </div>
  </header>

  <div class="mobile-nav">
    <div class="mobile-nav-header">
      <a href="#/index" class="brand" data-nav-link="index">
        {BRAND_SVG}
        <span class="brand-name">Minutrisalud</span>
      </a>
      <button class="mobile-nav-close" aria-label="Cerrar menú" type="button">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6 6 18M6 6l12 12"/></svg>
      </button>
    </div>
    <div class="mobile-nav-links">
{mobile_links}
    </div>
    <div class="mobile-nav-actions">
      <button class="theme-toggle" data-theme-toggle type="button" style="align-self:flex-start;"></button>
      <a href="#/contacto" class="btn btn--primary" data-nav-link="contacto">Reservar consulta online</a>
    </div>
  </div>

'''


SPA_FOOTER = f'''  <footer class="footer">
    <div class="wrap">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="#/index" class="brand" data-nav-link="index">
            {BRAND_SVG}
            <span class="brand-name">Minutrisalud</span>
          </a>
          <p>Consulta de nutrición online, con equipo médico y nutricionistas: valoración, planes de alimentación y seguimiento.</p>
        </div>
        <div>
          <h4>Navegación</h4>
          <ul>
            <li><a href="#/index" data-nav-link="index">Inicio</a></li>
            <li><a href="#/servicios" data-nav-link="servicios">Servicios</a></li>
            <li><a href="#/consejos" data-nav-link="consejos">Consejos</a></li>
            <li><a href="#/calculadora" data-nav-link="calculadora">Calculadora nutricional</a></li>
            <li><a href="#/precios" data-nav-link="precios">Planes y precios</a></li>
            <li><a href="#/equipo" data-nav-link="equipo">Equipo</a></li>
            <li><a href="#/app" data-nav-link="app">App Minutrisalud</a></li>
            <li><a href="#/nutrigest" data-nav-link="nutrigest">NutriGest (equipo)</a></li>
          </ul>
        </div>
        <div>
          <h4>Servicios</h4>
          <ul>
            <li><a href="#/servicios?anchor=teleconsulta" data-nav-link="servicios">Teleconsulta</a></li>
            <li><a href="#/servicios?anchor=valoracion" data-nav-link="servicios">Valoración nutricional</a></li>
            <li><a href="#/servicios?anchor=planes-servicios" data-nav-link="servicios">Planes personalizados</a></li>
            <li><a href="#/servicios?anchor=seguimiento" data-nav-link="servicios">Seguimiento y control</a></li>
            <li><a href="#/precios" data-nav-link="precios">Ver precios</a></li>
            <li><a href="#/pago" data-nav-link="pago">Contratar y pagar</a></li>
          </ul>
        </div>
        <div>
          <h4>Contacto</h4>
          <ul>
            <li><a href="mailto:hola@minutrisalud.com" target="_blank" rel="noopener noreferrer">hola@minutrisalud.com</a></li>
            <li><a href="#/contacto" data-nav-link="contacto">Solicitar cita</a></li>
          </ul>
        </div>
        <div>
          <h4>Legal</h4>
          <ul>
            <li><a href="#/legal" data-nav-link="legal">Aviso legal</a></li>
            <li><a href="#/privacidad" data-nav-link="privacidad">Política de privacidad</a></li>
            <li><a href="#/cookies" data-nav-link="cookies">Política de cookies</a></li>
            <li><a href="#/terminos" data-nav-link="terminos">Términos y condiciones</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 Minutrisalud. Todos los derechos reservados.</p>
        <p>Contenido con fines informativos. No sustituye una valoración médica presencial.</p>
      </div>
    </div>
  </footer>
'''

HEAD_TEMPLATE = '''<!doctype html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:image" content="./assets/hero-og.jpg" />
  <link rel="icon" href="./assets/favicon.ico" sizes="any" />
  <link rel="icon" type="image/png" sizes="32x32" href="./assets/favicon-32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="./assets/favicon-16.png" />
  <link rel="apple-touch-icon" href="./assets/apple-touch-icon.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://api.fontshare.com/v2/css?f[]=erode@400,500,600&display=swap" rel="stylesheet" />
  <link href="https://fonts.googleapis.com/css2?family=Work+Sans:wght@300..700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="./base.css" />
  <link rel="stylesheet" href="./style.css" />
</head>
<body>
'''

# Regex que convierte cualquier enlace interno "algo.html" o "algo.html#ancla"
# (donde "algo" es una de nuestras páginas) en el formato de navegación interna
# "#/algo" o "#/algo?anchor=ancla". Los enlaces externos (mailto, http://127.0.0.1..., etc.)
# no coinciden con este patrón y se quedan tal cual.
INTERNAL_LINK_RE = re.compile(
    r'href="(' + "|".join(re.escape(s) for s in SLUGS) + r')\.html(?:#([A-Za-z0-9_-]+))?"'
)


def rewrite_internal_links(html):
    def repl(m):
        slug, anchor = m.group(1), m.group(2)
        if anchor:
            return f'href="#/{slug}?anchor={anchor}" data-nav-link="{slug}"'
        return f'href="#/{slug}" data-nav-link="{slug}"'
    return INTERNAL_LINK_RE.sub(repl, html)


ROUTER_SCRIPT = f'''
  <script>
  (function () {{
    var TITLES = {{
{chr(10).join(f'      {slug!r}: {title!r},' for slug, title, _, _ in PAGES)}
    }};
    var sections = document.querySelectorAll('.spa-page');
    var navLinks = document.querySelectorAll('[data-nav-link]');

    function parseHash() {{
      var raw = (window.location.hash || '').replace(/^#\\/?/, '');
      var parts = raw.split('?');
      var page = parts[0] || 'index';
      var anchor = null;
      if (parts[1]) {{
        var params = new URLSearchParams(parts[1]);
        anchor = params.get('anchor');
      }}
      return {{ page: page, anchor: anchor }};
    }}

    function showPage(page, anchor) {{
      var found = false;
      sections.forEach(function (sec) {{
        if (sec.dataset.page === page) {{
          sec.hidden = false;
          found = true;
        }} else {{
          sec.hidden = true;
        }}
      }});
      if (!found) {{ page = 'index'; }}
      if (TITLES[page]) {{ document.title = TITLES[page]; }}
      navLinks.forEach(function (a) {{
        if (a.dataset.navLink === page) {{ a.setAttribute('aria-current', 'page'); }}
        else {{ a.removeAttribute('aria-current'); }}
      }});
      document.body.classList.remove('mobile-nav-open');
      if (anchor) {{
        requestAnimationFrame(function () {{
          var el = document.getElementById(anchor);
          if (el) {{ el.scrollIntoView({{ behavior: 'smooth', block: 'start' }}); }}
        }});
      }} else {{
        window.scrollTo({{ top: 0, left: 0, behavior: 'instant' }});
      }}
    }}

    function route() {{
      var parsed = parseHash();
      showPage(parsed.page, parsed.anchor);
    }}

    window.addEventListener('hashchange', route);
    document.addEventListener('DOMContentLoaded', route);
    if (!window.location.hash) {{ window.location.hash = '#/index'; }}
    route();
  }})();
  </script>
'''

TAIL_TEMPLATE = '''
  <script src="./app.js"></script>''' + ROUTER_SCRIPT + '''
</body>
</html>
'''


CONSTRUCTION_BANNER = '''  <div class="construction-banner">
    <div class="wrap construction-banner-inner">
      <span class="construction-banner-icon" aria-hidden="true">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 9v4m0 4h.01M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0Z"/></svg>
      </span>
      <p>Este sitio está en construcción: algunos contenidos y funciones (como el pago online y NutriGest) todavía se están terminando de preparar.</p>
    </div>
  </div>
'''


def build_spa(filename):
    html = HEAD_TEMPLATE.format(
        title="Minutrisalud — Consulta de nutrición online con criterio médico",
        description="Minutrisalud: consulta de nutrición online por videollamada, con equipo médico y nutricionistas. Valoración, planes personalizados y seguimiento.",
    )
    html += CONSTRUCTION_BANNER
    html += spa_header("index")
    html += '  <main id="spa-root">\n'
    for slug, title, body, nav_label in PAGES:
        hidden_attr = "" if slug == "index" else " hidden"
        html += f'  <section class="spa-page" data-page="{slug}"{hidden_attr}>\n'
        html += body
        html += '  </section>\n\n'
    html += '  </main>\n'
    html += SPA_FOOTER
    html += TAIL_TEMPLATE

    html = rewrite_internal_links(html)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename, "(SPA, una sola página con navegación interna)")


if __name__ == "__main__":
    build_spa("/home/user/workspace/minutrisalud/index.html")

    # Las páginas clásicas (servicios.html, consejos.html, etc.) se sustituyen
    # por una redirección automática a la sección correspondiente del index,
    # por si alguien tenía guardado un enlace directo a una de ellas.
    redirect_slugs = [slug for slug, *_ in PAGES if slug != "index"]
    for slug in redirect_slugs:
        target = f"index.html#/{slug}"
        redirect_html = f'''<!doctype html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="refresh" content="0; url={target}" />
  <title>Minutrisalud</title>
  <script>window.location.replace({target!r});</script>
</head>
<body>
  <p>Redirigiendo a <a href="{target}">{target}</a>…</p>
</body>
</html>
'''
        path = f"/home/user/workspace/minutrisalud/{slug}.html"
        with open(path, "w", encoding="utf-8") as f:
            f.write(redirect_html)
        print("wrote", path, "(redirección de compatibilidad)")
