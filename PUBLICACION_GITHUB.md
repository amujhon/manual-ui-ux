# Publicar el manual en GitHub Pages

La raíz de este directorio es la raíz que se debe subir al repositorio. **No subir la carpeta contenedora**, sino los archivos `index.html`, `assets/`, `capitulos/`, `pdf/`, etc.

1. Crear repositorio **público** `manual-ui-ux` en la cuenta `amujhon` (sin añadir README ni .gitignore inicialmente).
2. Añadir todos estos archivos a la rama `main`, conservando la estructura de carpetas.
3. En GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: main → / (root) → Save**.
4. Comprobar la URL publicada que se mostrará en Pages (habitualmente `https://amujhon.github.io/manual-ui-ux/`).

No se necesita build: HTML/CSS/JS y PDF se sirven directamente. `.nojekyll` desactiva procesamiento Jekyll. Los enlaces a CSS, JS, capítulos y PDFs usan rutas relativas y funcionan con el prefijo del repositorio en GitHub Pages.

## Actualizaciones

Añade nuevos capítulos al manuscrito fuente y genera HTML/PDF. Publica sus cambios en `main`. GitHub Pages volverá a publicar.

No se han publicado automáticamente estos archivos ni configurado GitHub Pages mediante este paquete.
