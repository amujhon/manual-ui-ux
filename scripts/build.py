#!/usr/bin/env python3
"""Construye un micrositio UI/UX 100% estático y PDFs a partir del manuscrito Markdown.
Requiere markdown-it-py, beautifulsoup4, weasyprint.
Ejecutar desde la raíz del sitio: python scripts/build.py
"""
from pathlib import Path
import re, html, json, shutil, unicodedata
from bs4 import BeautifulSoup, NavigableString
from markdown_it import MarkdownIt
from weasyprint import HTML, CSS

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'fuentes'/'manual_ui_ux_v0.2.md'
raw=SRC.read_text(encoding='utf-8')
intro, rest=raw.split('# PARTE I · FUNDAMENTOS CIENTÍFICOS, CONCEPTUALES Y METODOLÓGICOS\n',1)
c1,c2=rest.split('# Capítulo 02. Investigación de usuarios y diseño centrado en las personas\n',1)
c1='# Capítulo 01. Introducción a UI, UX y HCI\n'+c1.split('# Capítulo 01. Introducción a UI, UX y HCI\n',1)[1]
c2='# Capítulo 02. Investigación de usuarios y diseño centrado en las personas\n'+c2
c3=(ROOT/'fuentes'/'capitulo-03.md').read_text(encoding='utf-8')
(ROOT/'fuentes'/'manual_ui_ux_v0.3.md').write_text(raw.rstrip()+'\n\n'+c3,encoding='utf-8')
# Keep re-usable standalone sources.
(ROOT/'fuentes'/'introduccion.md').write_text(intro,encoding='utf-8')
(ROOT/'fuentes'/'capitulo-01.md').write_text(c1,encoding='utf-8')
(ROOT/'fuentes'/'capitulo-02.md').write_text(c2,encoding='utf-8')

GROUPS=[
 ('I','Fundamentos y métodos',[
  'Introducción a UI, UX y HCI','Investigación de usuarios y diseño centrado en las personas','Objetivos, tareas, modelos mentales y arquitectura de información','Psicología cognitiva y leyes aplicadas al diseño','Heurísticas y principios de interacción','Fundamentos de accesibilidad y diseño inclusivo']),
 ('II','Lenguaje visual',[
  'Composición, percepción y jerarquía visual','Tipografía y legibilidad','Color, contraste y sistemas de temas','Espaciado, cuadrículas y layouts','Iconografía, imágenes e identidad visual','UX Writing y diseño de contenido']),
 ('III','Componentes e interacción',[
  'Design Systems y Design Tokens','Anatomía y comportamiento de componentes interactivos','Botones, enlaces y controles de acción','Inputs y entrada de texto','Controles de selección y elección','Inputs especializados y captura avanzada','Estados, feedback, errores y animación','Diálogos, popovers, tooltips y notificaciones']),
 ('IV','Patrones y experiencias',[
  'Navegación y orientación','Validaciones y recuperación de errores','Diseño integral de formularios','Formularios multipaso y flujos complejos','Búsqueda, filtrado y ordenamiento','Listas, tablas y datos densos','Visualización de datos y dashboards','Autenticación, permisos y consentimiento']),
 ('V','Calidad transversal',[
  'Diseño responsive y adaptive','Convenciones de Android, iOS, web y escritorio','Accesibilidad avanzada y tecnologías asistivas','Rendimiento percibido, resiliencia, confianza y ética']),
 ('VI','Implementación y evaluación',[
  'Wireframes, prototipos e investigación evaluativa','Implementación de UI/UX en la web','Implementación de UI/UX con Flutter','Auditoría, métricas y evolución del diseño'])
]
chapters=[]
for p,title,items in GROUPS:
 for t in items:
  chapters.append(dict(n=len(chapters)+1, title=t, part=p, ready=len(chapters)<3))
assert len(chapters)==36

md=MarkdownIt('default', {'html':True, 'linkify':False}).enable(['table','strikethrough'])

def slug(text):
    t=unicodedata.normalize('NFKD', text.lower())
    t=''.join(x for x in t if not unicodedata.combining(x))
    t=re.sub(r'[^a-z0-9]+','-',t).strip('-')
    return t or 'seccion'

def render_markdown(content):
    soup=BeautifulSoup(md.render(content),'html.parser')
    headings=[]; ids=set()
    for h in soup.select('h1, h2, h3'):
        title=h.get_text(' ',strip=True)
        ident=slug(title)
        base=ident; k=2
        while ident in ids:
            ident=f'{base}-{k}';k+=1
        ids.add(ident); h['id']=ident
        headings.append(dict(id=ident,label=title,level=int(h.name[1])))
        if h.name=='h1': h['class']='chapter-heading'
    # Preserve bibliographic hyperlinks written as literal URLs in Markdown.
    for node in list(soup.find_all(string=True)):
        if node.parent.name in ('a','code','pre','script','style') or 'http' not in node:
            continue
        value = str(node)
        pat = re.compile(r'https?://[^\s<>]+')
        matches=list(pat.finditer(value))
        if not matches: continue
        prev=0; additions=[]
        for m in matches:
            additions.append(NavigableString(value[prev:m.start()]))
            url=m.group(0).rstrip('.,);')
            a=soup.new_tag('a',href=url)
            a.string=url
            additions.append(a)
            additions.append(NavigableString(m.group(0)[len(url):]))
            prev=m.end()
        additions.append(NavigableString(value[prev:]))
        for added in reversed(additions): node.insert_after(added)
        node.extract()
    for table in soup.find_all('table'):
        wrapper=soup.new_tag('div',attrs={'class':'table-scroller','tabindex':'0','role':'region','aria-label':'Tabla desplazable horizontalmente'})
        table.wrap(wrapper)
    for pre in soup.find_all('pre'):
        code=pre.find('code')
        if code:
            wrap=soup.new_tag('div',attrs={'class':'code-block'})
            pre.wrap(wrap)
            btn=soup.new_tag('button',attrs={'class':'copy-code','type':'button','aria-label':'Copiar fragmento de código'})
            btn.string='Copiar código'
            wrap.insert(0,btn)
    for a in soup.find_all('a'):
        if a.get('href','').startswith('https://'):
            a['target']='_blank'; a['rel']='noopener noreferrer'
    return str(soup), headings

content={
'intro':(intro,'Presentación','introduccion.html'),
'c1':(c1,'Introducción a UI, UX y HCI','capitulos/01.html'),
'c2':(c2,'Investigación de usuarios y diseño centrado en las personas','capitulos/02.html'),
'c3':(c3,'Objetivos, tareas, modelos mentales y arquitectura de información','capitulos/03.html')
}
rendered={key:render_markdown(val[0]) for key,val in content.items()}

book_mark='''<svg viewBox="0 0 42 42" width="40" height="40" aria-hidden="true"><rect x="1" y="1" width="40" height="40" rx="12" fill="currentColor"/><path d="M12 11v20m0-20 10 10-10 10m10-10 9-10m-9 10 9 10" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'''

def nav_items(prefix, current=''):
    out=[]
    for part,title,entries in GROUPS:
        out.append(f'<div class="nav-group"><p class="nav-group-label">PARTE {part} <span>· {html.escape(title)}</span></p>')
        for c in [c for c in chapters if c['part']==part]:
            sel=(current==f'{c["n"]:02d}')
            t=html.escape(c['title'])
            if c['ready']:
                out.append(f'<a class="nav-chapter {"is-current" if sel else ""}" href="{prefix}capitulos/{c["n"]:02d}.html" {"aria-current=page" if sel else ""}><span class="chapter-num">{c["n"]:02d}</span><span>{t}</span></a>')
            else:
                out.append(f'<div class="nav-chapter is-pending" title="Capítulo aún no publicado"><span class="chapter-num">{c["n"]:02d}</span><span>{t}</span><span class="small-dot" aria-hidden="true"></span></div>')
        out.append('</div>')
    return ''.join(out)

def topbar(prefix, active=''):
    return f'''<header class="topbar">
<a class="brand" href="{prefix}index.html" aria-label="Manual UI/UX, ir al inicio"><span class="brand-icon">{book_mark}</span><span class="brand-text">manual<span class="brand-period">.</span><small>UI / UX</small></span></a>
<nav class="top-links" aria-label="Navegación principal"><a href="{prefix}index.html#indice" {"aria-current=page" if active=='indice' else ''}>Capítulos</a><a href="{prefix}introduccion.html" {"aria-current=page" if active=='intro' else ''}>Presentación</a><a href="{prefix}index.html#recursos">Recursos</a></nav>
<div class="top-actions"><span class="version-pill">EDICIÓN 0.3</span><button class="icon-button theme-toggle" type="button" aria-label="Alternar modo oscuro" title="Cambiar tema"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M4.93 4.93l1.42 1.42m11.3 11.3 1.42 1.42M2 12h2m16 0h2M4.93 19.07l1.42-1.42m11.3-11.3 1.42-1.42"/></svg></button><button class="icon-button mobile-menu" type="button" aria-expanded="false" aria-controls="reader-sidebar" aria-label="Abrir índice"><svg viewBox="0 0 24 24" width="21" height="21" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 6h16M4 12h16M4 18h16"/></svg></button></div>
</header>'''

def base_page(title, body, prefix='', body_cls='', extrahead=''):
    return f'''<!doctype html><html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="Manual integral de UI/UX: fundamentos, investigación, estándares, componentes e implementación. Lectura en línea y PDF gratuitos."><meta name="theme-color" content="#f9f9f6"><title>{html.escape(title)} — Manual UI/UX</title><link rel="stylesheet" href="{prefix}assets/styles.css">{extrahead}</head><body class="{body_cls}"><a class="skip-link" href="#contenido">Saltar al contenido</a>{body}<script src="{prefix}assets/site.js" defer></script></body></html>'''

read_prep = [
    ('introduccion.html','Presentación','intro',''),
    ('capitulos/01.html','Capítulo 01','c1','01'),
    ('capitulos/02.html','Capítulo 02','c2','02'),
    ('capitulos/03.html','Capítulo 03','c3','03'),
]
for filename,short,key,current in read_prep:
    body_html, heads=rendered[key]
    prefix='../' if filename.startswith('capitulos/') else ''
    title=content[key][1]
    toc=''.join(f'<a class="outline-item level-{e["level"]}" href="#{e["id"]}">{html.escape(e["label"])}</a>' for e in heads if e['level'] in (2,3))
    if current=='01': bottom=f'<a class="next-link" href="02.html"><span>Siguiente capítulo</span><strong>02. Investigación de usuarios →</strong></a>'
    elif current=='02': bottom=f'<a class="next-link" href="03.html"><span>Siguiente capítulo</span><strong>03. Objetivos, tareas y modelos mentales →</strong></a>'
    elif current=='03': bottom=f'<div class="next-link disabled"><span>Próximamente</span><strong>04. Psicología cognitiva y leyes aplicadas</strong></div>'
    else: bottom=f'<a class="next-link" href="capitulos/01.html"><span>Empezar la lectura</span><strong>01. Introducción a UI, UX y HCI →</strong></a>'
    pdf_key = 'manual-uiux-v0.3.pdf' if not current else f'capitulo-{current}.pdf'
    md_file = 'introduccion.md' if not current else f'capitulo-{current}.md'
    tools=f'''<div class="chapter-tools"><a class="pill-action" href="{prefix}pdf/{pdf_key}" download><span aria-hidden="true">↓</span> PDF</a><a class="pill-action" href="{prefix}fuentes/{md_file}" download>Markdown</a></div>'''
    practical=''
    if current=='01': practical=f'<div class="practical-panel"><div class="practical-icon">↗</div><div><strong>Laboratorio del capítulo 01</strong><p>Comparación de interfaces y ejemplo de código Flutter.</p><div class="practical-links"><a href="{prefix}recursos/comparacion-ui-ux.html">Abrir ejemplo interactivo ↗</a><a href="{prefix}recursos/main.dart" download>Descargar código Dart ↓</a></div></div></div>'
    elif current=='02': practical=f'<div class="practical-panel"><div class="practical-icon">↗</div><div><strong>Laboratorio del capítulo 02</strong><p>Ejercicios de investigación y distinción entre hechos e hipótesis.</p><div class="practical-links"><a href="{prefix}recursos/c02_laboratorio.html">Abrir laboratorio ↗</a><a href="{prefix}recursos/plan_investigacion.md" download>Plan de investigación ↓</a><a href="{prefix}recursos/guion_entrevista.md" download>Guion de entrevista ↓</a></div></div></div>'
    elif current=='03': practical=f'<div class="practical-panel"><div class="practical-icon">↗</div><div><strong>Laboratorio del capítulo 03</strong><p>Comparar árboles de navegación.</p><div class="practical-links"><a href="{prefix}recursos/c03_arboles.html">Abrir laboratorio ↗</a></div></div></div>'
    nwords=len(content[key][0].split()); minutes=max(1,round(nwords/210))
    badge=f'CAPÍTULO {current} DE 36' if current else 'INTRODUCCIÓN'
    layout=f'''{topbar(prefix, 'intro' if key=='intro' else '')}<div class="reading-progress" aria-hidden="true"><span id="reading-progress"></span></div>
<div class="reader-shell"><aside class="reader-sidebar" id="reader-sidebar" aria-label="Capítulos del manual"><div class="sidebar-heading">CONTENIDO DEL MANUAL</div><a class="intro-nav {"is-current" if key=='intro' else ""}" href="{prefix}introduccion.html">↗ Presentación y guía de lectura</a><div class="sidebar-scroll">{nav_items(prefix,current)}</div></aside>
<main id="contenido" class="reader-main"><div class="reader-crumb"><a href="{prefix}index.html">Manual UI/UX</a><span aria-hidden="true">/</span><span>{short}</span></div><div class="article-header"><span class="eyebrow">{badge}</span><div class="reader-title"><h1>{html.escape(title)}</h1></div><div class="article-meta"><span>{nwords:,} palabras</span><span class="meta-sep"></span><span>{minutes} min de lectura aprox.</span><span class="meta-sep"></span><span>Publicado · v0.3</span></div>{tools}</div>{practical}<article class="prose" data-article>{body_html}</article><div class="end-note"><span class="eyebrow">SIGUIENTE PASO</span>{bottom}</div><footer class="reader-footer">Manual UI/UX · Versión de trabajo 0.3 · 3 de 36 capítulos disponibles</footer></main>
<aside class="reader-outline" aria-label="En esta página"><div class="outline-inner"><div class="outline-heading">EN ESTA PÁGINA</div><nav>{toc}</nav><div class="outline-download"><p>¿Prefieres leer sin conexión?</p><a href="{prefix}pdf/{pdf_key}" download>Descargar PDF ↗</a></div></div></aside></div><div class="overlay" id="nav-overlay"></div>'''
    target=ROOT/filename; target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(base_page(short, layout, prefix, 'reader-page'),encoding='utf-8')

# Search index uses short extracts from actual sections for navigable results, no external fetch.
search=[]
for key in ('c1','c2','c3'):
    doc,heads=rendered[key]
    s=BeautifulSoup(doc,'html.parser')
    link=content[key][2]
    for h in s.find_all(['h2','h3']):
        chunks=[]
        for sib in h.next_siblings:
            if getattr(sib,'name','') in ('h1','h2','h3'): break
            text=sib.get_text(' ',strip=True) if hasattr(sib,'get_text') else str(sib).strip()
            if text: chunks.append(text)
            if len(' '.join(chunks))>240: break
        search.append({'title':h.get_text(' ',strip=True),'text':' '.join(chunks)[:210],'chapter':int(key[-1]),'url':f'{link}#{h.get("id")}'})

# Landing directory grouped by six areas.
def card_html(c):
    label=f'{c["n"]:02d}'
    txt=html.escape(c['title'])
    if c['ready']:
        return f'<a class="chapter-card available" href="capitulos/{label}.html" data-title="{html.escape(c["title"].lower())}"><span class="chapter-ordinal">{label}</span><span class="chapter-card-title">{txt}</span><span class="chapter-state ready">Leer ahora <span aria-hidden="true">↗</span></span></a>'
    return f'<div class="chapter-card upcoming" data-title="{html.escape(c["title"].lower())}"><span class="chapter-ordinal">{label}</span><span class="chapter-card-title">{txt}</span><span class="chapter-state">Pendiente</span></div>'

group_sections=''
for part,group_name,entries in GROUPS:
    group= [x for x in chapters if x['part']==part]
    group_sections+=f'''<section class="directory-group" data-group><div class="directory-heading"><span class="part-index">{part}</span><div><h3>{html.escape(group_name)}</h3><p>{min(x['n'] for x in group):02d}–{max(x['n'] for x in group):02d} · {len(group)} capítulos</p></div></div><div class="chapter-grid">{''.join(card_html(x) for x in group)}</div></section>'''

landing=f'''{topbar('','indice')}<main id="contenido"><section class="hero"><div class="hero-inner"><div class="hero-copy"><span class="hero-tag"><span class="status-dot"></span> EDICIÓN EN DESARROLLO · 03 / 36 CAPÍTULOS</span><h1>Diseñar interfaces.<br><em>Entender personas.</em></h1><p class="hero-desc">Un manual para pasar de las opiniones a decisiones de UI/UX fundamentadas en investigación, estándares, principios de interacción y código.</p><div class="hero-buttons"><a class="primary-cta" href="capitulos/01.html">Comenzar a leer <span aria-hidden="true">↗</span></a><a class="secondary-cta" href="pdf/manual-uiux-v0.3.pdf" download>↓ Descargar PDF completo</a></div><div class="hero-mini"><span><b>36</b> capítulos planificados</span><i></i><span><b>3</b> disponibles</span><i></i><span><b>100%</b> gratuito</span></div></div>
<div class="hero-graphic" aria-label="Diagrama del proceso de diseño"><div class="graphic-serial">01 — 04 / MÉTODO</div><div class="diagram"><div class="diagram-node node-one"><span class="node-number">01</span><b>Investigar</b><small>Personas y contexto</small></div><div class="diagram-join"></div><div class="diagram-node node-two"><span class="node-number">02</span><b>Diseñar</b><small>Flujos y patrones</small></div><div class="diagram-join"></div><div class="diagram-node node-three"><span class="node-number">03</span><b>Implementar</b><small>Componentes y código</small></div><div class="diagram-join"></div><div class="diagram-node node-four"><span class="node-number">04</span><b>Validar</b><small>Evidencia y mejora</small></div></div><div class="graphic-footer"><span>Iterar sobre evidencia, no suposiciones.</span><span>↗</span></div></div></div><div class="hero-bottom"><span>TEORÍA + ESTÁNDARES + EJEMPLOS</span><span>SCROLL PARA EXPLORAR ↓</span></div></section>
<section class="intro-strip section-wrap"><div class="intro-head"><span class="eyebrow">LA IDEA CENTRAL</span><h2>Una buena interfaz no se defiende con «se ve mejor».</h2></div><p>Se fundamenta en lo que las personas necesitan, en las restricciones del sistema y en lo que podemos medir. Cada capítulo conecta conceptos, ejemplos y criterios de validación para tomar mejores decisiones.</p><a href="introduccion.html" class="text-link">Leer la presentación del manual ↗</a></section>
<section class="features section-wrap"><div class="feature"><span class="feature-icon">✳</span><strong>Fundamentos verificables</strong><p>Normas, guías y heurísticas claramente diferenciadas.</p></div><div class="feature"><span class="feature-icon">⌘</span><strong>Ejemplos que funcionan</strong><p>Casos visuales, ejercicios y código web/Flutter.</p></div><div class="feature"><span class="feature-icon">↗</span><strong>Dos maneras de aprender</strong><p>Lectura progresiva o consulta directa por capítulo.</p></div></section>
<section class="directory section-wrap" id="indice"><div class="section-topline"><span class="eyebrow">EL ÍNDICE</span><span class="index-count">36 CAPÍTULOS · 6 PARTES</span></div><div class="directory-top"><div><h2>Explora el manual<span class="title-dot">.</span></h2><p>Lee los capítulos publicados. Los demás aparecen como hoja de ruta y se habilitarán en futuras entregas.</p></div><label class="search-field"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 5 5"/></svg><input type="search" id="chapter-search" placeholder="Buscar tema o concepto…" autocomplete="off" aria-label="Buscar dentro del manual"/><span class="keycap">/</span></label></div><div id="search-results" class="search-results" hidden aria-live="polite"></div><div id="directory-groups">{group_sections}</div></section>
<section class="resource-section" id="recursos"><div class="section-wrap resource-grid"><div><span class="eyebrow">PONLO EN PRÁCTICA</span><h2>Del principio<br>al código<span class="title-dot">.</span></h2><p>Ejemplos incluidos en los tres primeros capítulos. Funcionan localmente, sin backend ni conexión a servicios externos.</p><a class="secondary-cta on-dark" href="pdf/manual-uiux-v0.3.pdf" download>↓ Descargar manual en PDF</a></div><div class="resource-cards"><a href="recursos/comparacion-ui-ux.html"><span class="resource-num">01 / DEMO</span><b>Comparación de interfaces</b><small>Una misma tarea, dos experiencias de uso.</small><span class="resource-arrow">↗</span></a><a href="recursos/c02_laboratorio.html"><span class="resource-num">02 / LAB</span><b>Laboratorio de investigación</b><small>Distingue hechos, hipótesis y decisiones.</small><span class="resource-arrow">↗</span></a><a href="recursos/plan_investigacion.md" download><span class="resource-num">02 / RECURSO</span><b>Plantilla de investigación</b><small>Guion y plan de trabajo reutilizables.</small><span class="resource-arrow">↓</span></a></div></div></section>
<section class="update-note section-wrap"><div><span class="eyebrow">UN MANUAL VIVO</span><h2>Documentación que crece por entregas.</h2><p>Este sitio publica únicamente contenido redactado. Los capítulos pendientes se conservan en el índice, pero no se presentan como disponibles. El PDF se actualiza a medida que se añaden capítulos.</p></div><div class="update-stat"><span>03 <small>/36</small></span><p>Capítulos disponibles</p><div class="update-meter"><div></div></div></div></section>
</main><footer class="site-footer"><div><strong>manual<span class="brand-period">.</span></strong><span>UI / UX · Edición de trabajo 0.3</span></div><p>Diseñar es formular, probar y mejorar decisiones. <a href="pdf/manual-uiux-v0.3.pdf" download>PDF ↗</a></p></footer>'''
search_script=f'<script>window.MANUAL_SEARCH_INDEX={json.dumps(search,ensure_ascii=False).replace("</", "<\\/")};</script>'
(ROOT/'index.html').write_text(base_page('Inicio',landing,body_cls='landing-page',extrahead=search_script),encoding='utf-8')

# PDFs assembled with full, original text; style does not depend on site CSS.
pdf_style='''@page{size:A4;margin:23mm 19mm 23mm 21mm;@bottom-left{content:"MANUAL UI/UX · EDICIÓN 0.3";font:8pt "DejaVu Sans",sans-serif;color:#718198;}@bottom-right{content:counter(page);font:9pt "DejaVu Sans",sans-serif;color:#365dc4;}}
body{font-family:"DejaVu Sans",sans-serif;font-size:9.35pt;line-height:1.62;color:#223248;}h1,h2,h3{font-family:"DejaVu Sans",sans-serif;color:#12325b;line-height:1.27;break-after:avoid;}h1{font-size:21pt;margin:17mm 0 6mm;letter-spacing:-.5pt;}h2{font-size:13.5pt;margin:7mm 0 2.5mm;}h3{font-size:11pt;margin:4mm 0 2mm;}p{margin:0 0 3.7mm;}li{margin:1.7mm 0;}ul,ol{padding-left:6mm;}strong{color:#102f57;}a{color:#2256ad;overflow-wrap:anywhere;text-decoration:none;}blockquote{margin:5mm 0;padding:2mm 4mm;border-left:3px solid #3762b7;background:#f3f6fb;}table{border-collapse:collapse;width:100%;font-size:8pt;margin:4mm 0 6mm;table-layout:auto;}th{color:#103b72;background:#eef3fb;font-weight:700;}th,td{border-bottom:.5px solid #d5deea;padding:2.2mm;text-align:left;vertical-align:top;overflow-wrap:anywhere;}tr{break-inside:avoid;}pre{white-space:pre-wrap;word-break:break-word;overflow-wrap:anywhere;padding:3mm;color:#dbeaff;background:#15233a;font:7.5pt "DejaVu Sans Mono",monospace;border-radius:3px;margin:3mm 0 5mm;}code{font-family:"DejaVu Sans Mono",monospace;font-size:8pt;overflow-wrap:anywhere;}pre code{color:inherit;}img{max-width:100%;}h1.chapter-heading{break-before:page;}ul li input{display:inline;}article{max-width:100%;}.cover{break-after:page;min-height:220mm;padding-top:35mm;}.cover .kicker{color:#3762b7;font-size:10pt;letter-spacing:3px;font-weight:700;}.cover h1{font-size:40pt;line-height:1.12;letter-spacing:-2px;margin:11mm 0 10mm;color:#10294b;}.cover .subtitle{font-size:16pt;color:#4c6686;max-width:130mm;}.cover .cover-rule{height:4px;background:#3868bf;width:35mm;margin:19mm 0 10mm;}.cover .foot{font-size:10pt;color:#536d84;margin-top:40mm;}.chapter-meta{color:#537196;font-size:10pt;font-weight:bold;letter-spacing:2px;}.toc-panel{break-after:page;}.toc-panel h1{font-size:27pt;}.toc-panel p{border-bottom:1px solid #dfe6f1;padding:4mm 0;margin:0;}.toc-panel p span{color:#3963bb;margin-right:6mm;}'''

def pdf_content(keys, outfile, title):
    cover=f'''<section class="cover"><div class="kicker">MANUAL PROFESIONAL · UI / UX</div><h1>Diseñar interfaces.<br>Entender personas.</h1><p class="subtitle">Fundamentos, investigación, estándares y herramientas de implementación.</p><div class="cover-rule"></div><p>Edición de trabajo 0.3 · Octubre de 2026</p><p>Capítulos 01 a 03 de 36 planificados</p><div class="foot">Documento de estudio · Contenido sujeto a ampliaciones</div></section>'''
    toc='''<section class="toc-panel"><p class="chapter-meta">GUÍA DE LECTURA</p><h1>Contenido</h1><p><span>00</span> Presentación y convenciones</p><p><span>01</span> Introducción a UI, UX y HCI</p><p><span>02</span> Investigación de usuarios y diseño centrado en las personas</p><p><span>03</span> Objetivos, tareas, modelos mentales y arquitectura de información</p><p>Los capítulos 04–36 están previstos, pero todavía no forman parte de esta edición.</p></section>'''
    if keys==['intro','c1','c2','c3']:
        fragments=[rendered[k][0] for k in keys]
        intro_part=render_markdown('# Presentación\n'+intro.split('# Presentación\n',1)[1])[0]
        body=cover+toc+intro_part+''.join(fragments[1:])
    else:
        body=''.join(rendered[k][0] for k in keys)
    # Remove UI-only code controls, PDF doesn't need buttons.
    soup=BeautifulSoup(body,'html.parser')
    for b in soup.select('button.copy-code'):b.decompose()
    for t in soup.select('.table-scroller'):
        t.unwrap()
    pdf_html=f'<html lang="es"><head><meta charset="utf-8"><title>{html.escape(title)}</title></head><body>{str(soup)}</body></html>'
    HTML(string=pdf_html,base_url=str(ROOT)).write_pdf(str(ROOT/'pdf'/outfile),stylesheets=[CSS(string=pdf_style)],presentational_hints=True)

pdf_content(['intro','c1','c2','c3'],'manual-uiux-v0.3.pdf','Manual UI/UX · v0.3')
pdf_content(['c1'],'capitulo-01.pdf','Capítulo 01 · UI, UX y HCI')
pdf_content(['c2'],'capitulo-02.pdf','Capítulo 02 · Investigación de usuarios')
pdf_content(['c3'],'capitulo-03.pdf','Capítulo 03 · Arquitectura de información')
print('Construido sitio con 4 páginas de lectura, portada, buscador y 4 PDFs.')
print('PDF bytes',[(f.name,f.stat().st_size) for f in (ROOT/'pdf').glob('*.pdf')])
