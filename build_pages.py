import re

NAV_ITEMS = [
    ("Inicio", "index.html"),
    ("Servicios", "servicios.html"),
    ("Consejos", "consejos.html"),
    ("Calculadora", "calculadora.html"),
    ("Planes y precios", "precios.html"),
    ("Equipo", "equipo.html"),
    ("App Minutrisalud", "app.html"),
    ("Contacto", "contacto.html"),
]

# Brand mark uses the client's real logo icon asset (raster, transparent background)
BRAND_SVG = '<img class="brand-mark" src="./assets/logo-icon.png" alt="" width="34" height="34">'

def header(active):
    links = "\n".join(
        f'        <a href="{href}"{" aria-current=\"page\"" if label == active else ""}>{label}</a>'
        for label, href in NAV_ITEMS
    )
    mobile_links = "\n".join(
        f'      <a href="{href}">{label}</a>' for label, href in NAV_ITEMS
    )
    return f'''  <header class="header">
    <div class="wrap header-inner">
      <a href="index.html" class="brand">
        {BRAND_SVG}
        <span class="brand-name">Minutrisalud</span>
      </a>
      <nav class="nav">
        <div class="nav-links">
{links}
        </div>
        <div class="nav-actions">
          <button class="theme-toggle" data-theme-toggle type="button"></button>
          <a href="contacto.html" class="btn btn--primary btn--sm">Consulta online</a>
        </div>
        <button class="nav-toggle" aria-label="Abrir menú" type="button">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
        </button>
      </nav>
    </div>
  </header>

  <div class="mobile-nav">
    <div class="mobile-nav-header">
      <a href="index.html" class="brand">
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
      <a href="contacto.html" class="btn btn--primary">Reservar consulta online</a>
    </div>
  </div>

'''

FOOTER = f'''  <footer class="footer">
    <div class="wrap">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="index.html" class="brand">
            {BRAND_SVG}
            <span class="brand-name">Minutrisalud</span>
          </a>
          <p>Consulta de nutrición online, con equipo médico y nutricionistas: valoración, planes de alimentación y seguimiento.</p>
        </div>
        <div>
          <h4>Navegación</h4>
          <ul>
            <li><a href="index.html">Inicio</a></li>
            <li><a href="servicios.html">Servicios</a></li>
            <li><a href="consejos.html">Consejos</a></li>
            <li><a href="calculadora.html">Calculadora nutricional</a></li>
            <li><a href="precios.html">Planes y precios</a></li>
            <li><a href="equipo.html">Equipo</a></li>
            <li><a href="app.html">App Minutrisalud</a></li>
            <li><a href="nutrigest.html">NutriGest (equipo)</a></li>
          </ul>
        </div>
        <div>
          <h4>Servicios</h4>
          <ul>
            <li><a href="servicios.html#teleconsulta">Teleconsulta</a></li>
            <li><a href="servicios.html#valoracion">Valoración nutricional</a></li>
            <li><a href="servicios.html#planes">Planes personalizados</a></li>
            <li><a href="servicios.html#seguimiento">Seguimiento y control</a></li>
            <li><a href="precios.html">Ver precios</a></li>
            <li><a href="pago.html">Contratar y pagar</a></li>
          </ul>
        </div>
        <div>
          <h4>Contacto</h4>
          <ul>
            <li><a href="mailto:hola@minutrisalud.com" target="_blank" rel="noopener noreferrer">hola@minutrisalud.com</a></li>
            <li><a href="contacto.html">Solicitar cita</a></li>
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

TAIL_TEMPLATE = '''
  <script src="./app.js"></script>
</body>
</html>
'''

def build(filename, title, description, active, body):
    html = HEAD_TEMPLATE.format(title=title, description=description)
    html += header(active)
    html += body
    html += FOOTER
    html += TAIL_TEMPLATE
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename)
