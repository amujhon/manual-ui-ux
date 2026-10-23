# Manual integral de UI/UX — sitio web estático

**Edición 0.3 · 21 de octubre de 2026**

Sitio de lectura con índice de 36 capítulos planificados, presentación, los capítulos 01, 02 y 03 completos, búsqueda local, recursos prácticos y botones para descargar PDF. Los capítulos 04 al 36 aparecen como **pendientes** y no tienen enlaces de lectura. Los PDF corresponden exclusivamente a los capítulos publicados.

## Uso

1. Abre `index.html` en un navegador moderno o publica la carpeta completa en un hosting estático.
2. Pulsa **Comenzar a leer** o abre un capítulo desde el índice.
3. Usa **Descargar PDF completo** para obtener el PDF consolidado. Dentro de cada capítulo también hay enlaces de descarga individuales.
4. En `recursos/` están los ejemplos y las plantillas del contenido original.

### Estructura

```text
index.html                   Página principal
introduccion.html            Presentación y convenciones
capitulos/01.html            Capítulo 01 completo
capitulos/02.html            Capítulo 02 completo
capitulos/03.html            Capítulo 03 completo
pdf/manual-uiux-v0.3.pdf     PDF consolidado
pdf/capitulo-01.pdf          PDF capítulo 01
pdf/capitulo-02.pdf          PDF capítulo 02
pdf/capitulo-03.pdf          PDF capítulo 03
assets/styles.css            Estilos responsivos
assets/site.js               Buscador, lectura y tema
recursos/                    Laboratorios y plantillas
fuentes/                     Manuscrito original y capítulos en Markdown
scripts/build.py             Generador de HTML y PDF
```

**Sin servidor:** para leer las páginas o descargar los PDF no se requiere PHP, Node.js, base de datos ni conexión a APIs. Los enlaces bibliográficos externos sí requieren internet.

## Publicación

- **GitHub Pages:** crea un repositorio, copia el contenido de esta carpeta a la raíz, en *Settings → Pages* publica desde la rama principal y la carpeta `/ (root)`. El botón PDF funciona con rutas relativas.
- **Cloudflare Pages:** sube el directorio directamente con *Direct Upload* o conéctalo a un repositorio. No se necesita comando de compilación ni directorio de salida distinto de esta carpeta.
- **Cualquier servidor web:** sirve `index.html` junto con las subcarpetas. No hace falta reescritura de rutas.

> No hay alojamiento web configurado en esta entrega; los archivos se han preparado para publicar donde prefieras.

## Actualizar los capítulos

El manuscrito original está en `fuentes/manual_ui_ux_v0.3.md` y esta versión usa `scripts/build.py` para construir HTML y PDF. El script requiere **Python 3**, `markdown-it-py`, `beautifulsoup4` y `weasyprint` (solo para la reconstrucción, no para visitar el sitio). Para incluir los capítulos 04–36 es necesario ampliar la detección de capítulos y el índice del generador; **no** basta con concatenar texto sin modificar el índice y las rutas.

```bash
python scripts/build.py
```

## Alcance de validación

- HTML/CSS/JavaScript evaluados en Chromium mediante un montaje local de las páginas en la herramienta de pruebas: búsqueda, navegación móvil, ausencia de errores JavaScript y controles de desbordamiento horizontal.
- Los tres PDF fueron generados y examinados para confirmar páginas útiles, contenido y portada.
- No se han realizado auditorías WCAG completas, pruebas con lectores de pantalla ni pruebas de usuario reales. El material de código original conserva las advertencias de ejecución de sus respectivas entregas.
- No se modificó el contenido técnico del manuscrito original; solo se transformó para lectura y exportación.
# manual-ui-ux
