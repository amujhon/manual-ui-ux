# Capítulo 03. Objetivos, tareas, modelos mentales y arquitectura de información

> **Parte I · Fundamentos científicos y metodológicos.** Prerrequisitos: capítulos 01 y 02. Continúa en los capítulos 04, 21, 24 y 25. Los ejemplos de esta entrega son ficticios: representan hipótesis de diseño, no resultados de investigación con usuarios.

## 3.1. Propósito y objetivos

El capítulo 02 enseñó a investigar personas, contextos y comportamientos. Ahora convertiremos esa evidencia en estructuras y recorridos que permitan lograr objetivos. La pregunta central no es «¿dónde pongo el botón?», sino «¿qué espera lograr la persona, cómo busca hacerlo y qué organización le ayudará a encontrar el camino?». Al finalizar podrás construir modelos de tareas, distinguir modelos mentales y modelos técnicos, proponer una arquitectura de información (IA) y evaluarla mediante *card sorting* y *tree testing*.

**Caso conductor:** un representante necesita descargar una constancia de matrícula para presentarla fuera de la institución. El sistema la ubica en «Trámites institucionales → Gestión documental → Certificaciones». ¿Es comprensible? No podemos contestar sin investigar quién la busca, qué términos reconoce y qué rutas intenta.

## 3.2. Necesidades, objetivos, tareas, operaciones y funcionalidades

| Concepto | Pregunta | Ejemplo |
|---|---|---|
| Necesidad | ¿Por qué necesita resolverlo? | Demostrar ante un tercero que el estudiante está matriculado. |
| Objetivo | ¿Qué resultado desea? | Obtener una constancia válida del periodo vigente. |
| Tarea | ¿Qué debe hacer? | Encontrar, comprobar y obtener el documento. |
| Operación | ¿Qué paso concreto realiza? | Elegir al estudiante o el periodo. |
| Funcionalidad | ¿Qué capacidad ofrece el sistema? | Generar y descargar un PDF. |

Una solicitud como «agrega un botón de certificado» describe una solución deseada, **no necesariamente el problema real**. Quizá el documento ya existe y falla su localización; quizá se encuentra pero no se genera; quizá las personas desconocen su denominación. La investigación de necesidades propuesta en el manual de servicios de GOV.UK exige comprender el resultado deseado antes de definir una interfaz [F01].

**Criterio de aceptación inicial:** una persona autorizada puede localizar y obtener un documento correspondiente al estudiante y periodo correctos, sin ayuda externa, cuando el documento está disponible. Este criterio evita decidir prematuramente el diseño del menú.

## 3.3. Contexto y escenarios

Un recorrido útil depende del rol, frecuencia, equipo, permisos, conectividad y consecuencias del error. Alguien que descarga constancias diariamente puede reconocer el término «certificaciones». Un familiar que entra dos veces al año quizá busque «documentos de mi hijo». Ninguna clasificación única es necesariamente adecuada para ambos.

Un escenario debe incluir actor, detonante, objetivo, información disponible, restricciones y resultado. Ejemplo hipotético: «Una representante con dos estudiantes utiliza un teléfono con internet inestable y necesita obtener hoy un comprobante vigente. No conoce el nombre técnico del documento». De ese escenario salen **preguntas**, no conclusiones: ¿cómo elige al estudiante?, ¿cómo identifica el periodo?, ¿qué ocurre cuando la descarga falla?

## 3.4. Análisis de tareas y HTA

El *task analysis* identifica los pasos y decisiones que intervienen en una actividad. Puede ser secuencial, cuando interesa el orden, o jerárquico (*Hierarchical Task Analysis*, HTA), cuando interesa dividir un objetivo en subtareas y describir un plan [F02].

```text
0. Obtener constancia de matrícula
   1. Identificar estudiante
      1.1 Acceder con cuenta autorizada
      1.2 Elegir estudiante si hay varios
   2. Localizar documento
      2.1 Reconocer sección correspondiente
      2.2 Elegir tipo de constancia
   3. Verificar
      3.1 Estudiante y periodo
      3.2 Disponibilidad
   4. Obtener documento
      4.1 Descargar o visualizar
      4.2 Comprobar que se puede utilizar
PLAN: 1 → 2 → 3 → 4;
      si no está disponible en 3.2, explicar situación.
```

El HTA **no prescribe cuatro pantallas**. Algunas subtareas pueden ser automáticas o presentarse en una sola vista. Una ficha de tarea debe conservar el objetivo, actores, frecuencia, entradas, bifurcaciones, errores, dependencias, resultado y fuente de evidencia. Cuando intervienen equipos o sistemas internos resulta útil complementar el HTA con un *service blueprint*.

## 3.5. Modelos mentales y expectativas

Un modelo mental es la explicación que la persona construye acerca de cómo funciona un sistema y dónde debería encontrar sus elementos. Puede diferir del modelo conceptual del diseñador y de la arquitectura técnica [F03].

| Expectativa del usuario (hipotética) | Estructura técnica | Posible conflicto |
|---|---|---|
| «Los documentos están dentro del perfil de mi hijo» | Documentos en menú institucional | No encuentra el punto de entrada. |
| «Matrícula y constancia están relacionadas» | Constancia en reportes generales | Etiquetas incomprensibles. |
| «Descargar significa obtener un archivo» | Una tarea asíncrona inicia sin aviso | Falta visibilidad del estado. |

Cómo conocer estas expectativas: observar el primer lugar en que buscan, preguntar dónde esperarían encontrar algo, analizar el lenguaje espontáneo, registrar rutas fallidas y comparar agrupaciones de contenidos. Un solo usuario no representa todo el público. Si dos grupos usan vocabularios diferentes, considera entradas contextuales, etiquetas explicativas y accesos cruzados antes de forzar una taxonomía universal.

## 3.6. Qué comprende la arquitectura de información

La IA organiza, etiqueta y relaciona contenido para que pueda encontrarse y entenderse. Es más amplia que la barra de navegación: incluye inventarios, taxonomías, metadatos, jerarquías, rotulado y búsqueda [F04].

| Artefacto | Función | Ejemplo |
|---|---|---|
| Inventario | Listar contenido real y responsables | Constancias, notas, matrículas, recibos. |
| Taxonomía | Definir criterios de agrupación | Documentos académicos / financieros. |
| Rotulado | Nombrar destinos de forma predecible | «Constancia de matrícula». |
| Jerarquía | Mostrar relaciones | Estudiante → Documentos → Constancia. |
| Metadatos | Filtrar y recuperar | Estudiante, periodo, tipo, estado. |
| Navegación | Ofrecer recorridos visibles | Enlaces, menú, migas de pan. |
| Búsqueda | Recuperar mediante términos | «Constancia», «matrícula». |

La IA no debe copiar por defecto las tablas de la base de datos ni el organigrama institucional: ambos representan intereses técnicos y administrativos que pueden diferir de las tareas reales. Un mismo documento puede aparecer desde «Matrícula» y desde «Documentos» sin convertirse en dos documentos físicos distintos.

## 3.7. Inventario, auditoría y taxonomía

Antes de reorganizar, registra cada destino: identificador, título visible, ruta, audiencia autorizada, responsable, vigencia, uso, términos equivalentes, enlaces y dependencias. Marca denominaciones ambiguas, duplicaciones y contenido abandonado.

Ejemplo de auditoría ficticia:

| Elemento | Título actual | Problema hipotético | Etiqueta candidata |
|---|---|---|---|
| DOC-01 | Gestión documental | Vago | Documentos y constancias |
| MAT-03 | Cert. matrícula | Abreviado | Constancia de matrícula |
| ACA-04 | Resumen | Ambiguo | Calificaciones |
| INF-11 | Historial | No indica qué contiene | Historial académico |

Estas etiquetas son **candidatas a probar**, no resultados definitivos. Tampoco es razonable eliminar una función únicamente por baja frecuencia: un trámite anual puede ser crítico. Las categorías pueden organizarse por objeto («Estudiantes»), tarea («Solicitudes»), etapa («Matrícula»), audiencia o tema. Mezclar criterios en el mismo nivel sin una lógica clara suele dificultar la orientación.

La discusión de anchura y profundidad no se resuelve imponiendo «máximo siete opciones». La cantidad adecuada depende de diferenciación, relevancia, términos y estructura. Menos opciones no garantizan menos carga cognitiva si sus nombres son imprecisos.

## 3.8. Rotulado y vocabulario

Los rótulos ayudan a anticipar destinos. «Procesos varios» comunica menos que «Solicitudes pendientes». Sin embargo, los términos «certificado», «constancia» y «comprobante» podrían designar documentos jurídicamente distintos; no deben tratarse como sinónimos sin comprobarlo. Puede mantenerse la denominación oficial y añadir una descripción comprensible o términos alternativos de búsqueda.

En sistemas con instituciones distintas, guarda un **identificador estable** distinto de la etiqueta localizada. No utilices el texto mostrado para determinar permisos o integridad de datos.

## 3.9. Card sorting: investigar agrupaciones

En *card sorting* se presentan tarjetas con contenidos y se observa cómo las personas los agrupan. Hay modalidad **abierta** (participantes crean grupos y nombres), **cerrada** (se proporcionan grupos) e **híbrida** [F05].

Protocolo básico: definir pregunta; redactar tarjetas neutrales; reclutar por audiencia; observar agrupaciones y términos; registrar discrepancias; proponer estructuras; **validar después encontrabilidad**. Tarjetas ilustrativas: Constancia de matrícula, notas, horarios, recibos, justificar falta, asistencia, pagos, permiso de salida, historial académico, mensajes del docente.

No confundas agrupar con navegar: que varias personas coloquen «constancia» con «matrícula» no demuestra que después la encontrarán correctamente en un menú real. La prueba complementaria es *tree testing*.

## 3.10. Tree testing: comprobar dónde buscarían

Un *tree test* presenta la arquitectura en forma de árbol textual, sin decoración gráfica. Las personas reciben tareas realistas y seleccionan rutas; se analizan destino, primer clic, retrocesos y errores [F06].

**Árbol A: clasificación institucional**

```text
Inicio
├── Mi perfil
├── Mis clases
└── Trámites institucionales
    └── Gestión documental
        └── Certificaciones
            └── Constancia de matrícula
```

**Árbol B: clasificación contextual**

```text
Inicio
├── Estudiantes
│   └── Estudiante seleccionado
│       └── Documentos y constancias
│           └── Constancia de matrícula
├── Pagos
└── Comunicaciones
```

Tarea neutral: «Necesitas un documento que demuestre que uno de tus hijos está inscrito este periodo. ¿Dónde intentarías encontrarlo?». No digas de antemano «entra a Documentos»; contaminaría la prueba.

**Métricas:** éxito final, éxito directo (sin retrocesos), primer clic, número de retrocesos, tiempo e interpretación cualitativa. Define **antes** del estudio los destinos aceptables. La ruta con menos clics no es necesariamente más clara. Abre el [laboratorio interactivo del capítulo](../recursos/c03_arboles.html) para recorrer ambos árboles; no es un experimento con participantes reales.

## 3.11. Mapa de sitio, task flow, user flow, journey y blueprint

Estos artefactos representan aspectos distintos:

| Artefacto | Qué representa | Ejemplo |
|---|---|---|
| Mapa de sitio | Destinos y relaciones jerárquicas | Estudiantes → Documentos → Constancias. |
| Task flow | Pasos de una tarea concreta | Elegir estudiante → comprobar → descargar. |
| User flow | Decisiones y bifurcaciones en producto | Disponible / pendiente / acceso denegado. |
| Journey map | Experiencia completa, incluso fuera del sistema | Recibir solicitud → obtener PDF → presentarlo. |
| Service blueprint | Operaciones visibles e internas | Validar matrícula, generar, autorizar y servir documento. |

NN/G diferencia las vistas de recorrido general de la interacción específica con el sistema [F07]. No necesitas producir cinco diagramas para cada mejora; elige el artefacto que revele los riesgos relevantes.

Ejemplo de *user flow*:

```text
Seleccionar estudiante
        ↓
Abrir documentos
        ↓
¿Constancia disponible?
    /          \
   Sí          No
   ↓           ↓
Revisar      Explicar motivo
periodo      y alternativa
   ↓
Descargar
   ↓
Verificar archivo
```

Es distinto de un mapa de sitio: muestra estado y decisiones, no solo categorías.

## 3.12. Priorización, múltiples vías y accesibilidad

La prominencia de una función debe evaluarse con frecuencia, criticidad, urgencia, impacto del error y audiencia. Evita convertir una puntuación inventada en una «ley» de usabilidad. Cuando una función tiene varios contextos legítimos, pueden ofrecerse múltiples accesos al mismo recurso, conservando identidad y permisos.

WCAG 2.2 (criterio 2.4.5, nivel AA) contempla **más de una forma de localizar páginas** dentro de conjuntos de páginas, con excepciones para pasos o resultados de un proceso. No exige duplicar menús idénticos [F08]. Encabezados claros, navegación consistente y regiones semánticas ayudan a orientarse a usuarios de teclado y lectores de pantalla [F09].

**Ejemplo HTML con navegación semántica:**

```html
<a href="#principal" class="skip-link">Saltar al contenido</a>
<nav aria-label="Navegación del estudiante">
  <ul>
    <li><a href="/estudiante/inicio">Inicio</a></li>
    <li><a href="/estudiante/calificaciones">Calificaciones</a></li>
    <li><a href="/estudiante/documentos" aria-current="page">
      Documentos y constancias
    </a></li>
  </ul>
</nav>
<main id="principal" tabindex="-1">
  <h1>Documentos y constancias</h1>
</main>
```

```css
.skip-link { position: absolute; transform: translateY(-200%); }
.skip-link:focus { transform: translateY(0); }
nav a:focus-visible { outline: 3px solid #1d4ed8; outline-offset: 3px; }
nav a[aria-current="page"] { font-weight: 700; text-decoration: underline; }
```

Usa `nav` y enlaces nativos en una navegación común; no agregues roles `menubar` o `menu` sin implementar los comportamientos complejos que exigen. El ejemplo **no garantiza** por sí solo todas las WCAG ni los permisos del servicio.

## 3.13. Identificadores de destino en Flutter

Separar la identidad del destino de su etiqueta ayuda a localizar el texto y cambiar rutas sin afectar lógica de permisos:

```dart
enum StudentDestination { grades, attendance, documents }

class DestinationSpec {
  const DestinationSpec(this.id, this.label);
  final StudentDestination id;
  final String label; // En producción: traducción con l10n.
}

const destinations = [
  DestinationSpec(StudentDestination.grades, 'Calificaciones'),
  DestinationSpec(StudentDestination.attendance, 'Asistencia'),
  DestinationSpec(StudentDestination.documents, 'Documentos y constancias'),
];
```

Este fragmento ilustra una estructura de datos. No es una aplicación completa ni código ejecutado; debe integrarse con navegación, autorización, estados y semántica, que se profundizarán en los capítulos 21 y 35.

## 3.14. Método de trabajo recomendado

1. Precisar objetivo y público; no empezar por rediseñar un menú.
2. Recuperar evidencia de entrevistas, observación y analítica (capítulo 02).
3. Inventariar contenido, permisos, vigencia y términos.
4. Modelar tareas, errores y rutas alternativas.
5. Investigar expectativas y agrupaciones, cuando sea necesario.
6. Proponer una o varias arquitecturas candidatas.
7. Evaluar con tree testing y tareas realistas.
8. Prototipar y comprobar flujos, accesibilidad y estados.
9. Implementar sin romper permisos, enlaces ni registros anteriores.
10. Documentar decisiones, excepciones y fecha de revisión.

No es un proceso estrictamente lineal: los resultados de una prueba pueden devolvernos a investigación o a taxonomía.

## 3.15. Antipatrones

| Error | Por qué perjudica | Alternativa |
|---|---|---|
| Organizar por tablas de base de datos | Impone estructura técnica | Agrupar según tareas y expectativas. |
| Resolver cada queja con un botón | Añade ruido sin diagnosticar | Verificar causa del fallo. |
| Creer que solo hay una ruta posible | Ignora contextos distintos | Múltiples puntos de entrada razonables. |
| Fijar siete opciones como máximo | Regla universal infundada | Probar comprensión y encontrabilidad. |
| Dar por buena IA tras card sorting | Agrupar no es encontrar | Complementar con tree testing. |
| Medir solo tiempo | Oculta errores y estrategias | Éxito, retrocesos y observación. |
| Ocultar enlaces para aplicar permisos | La UI no protege el backend | Autorizar en servidor. |

## 3.16. Ejercicios, rúbrica y checklist

**Ejercicio A.** Escribe una necesidad, un objetivo y tres tareas para justificar una inasistencia. No uses nombres de botones como necesidades.

**Ejercicio B.** Modela un HTA para consultar un historial académico con varios periodos. Incluye errores, autorizaciones y estados.

**Ejercicio C.** Diseña diez tarjetas para investigar cómo se agrupan documentos de estudiantes. Especifica si harás clasificación abierta o cerrada y por qué.

**Ejercicio D.** Compara los dos árboles del laboratorio. Define previamente qué destinos se consideran correctos y registra primer clic, retrocesos y resultado. No generalices a partir de tu propia participación.

**Ejercicio E.** Implementa la navegación HTML de la sección anterior con foco visible, ruta actual y enlaces reales; comprueba que los permisos no dependan del menú.

**Checklist de revisión:**

- [ ] La necesidad describe un resultado, no un widget.
- [ ] Las tareas distinguen operación, decisión y error.
- [ ] Se identifican actores y sus modelos mentales.
- [ ] Existe un inventario y una taxonomía argumentada.
- [ ] Los rótulos son comprensibles y precisos.
- [ ] Las rutas alternativas no duplican datos.
- [ ] Hay un protocolo de prueba con destinos definidos de antemano.
- [ ] Se evalúan éxito, primeros clics, retrocesos y accesibilidad.
- [ ] Las decisiones se etiquetan como probadas o hipotéticas.

**Conclusión:** la arquitectura de información no consiste en acomodar enlaces de forma atractiva. Consiste en hacer que el modelo de contenido y las rutas disponibles permitan a distintas personas encontrar información y completar objetivos, con evidencia y sin sacrificar seguridad, accesibilidad ni coherencia.

## 3.17. Fuentes y lectura complementaria

- [F01] GOV.UK Service Manual. *Start by learning user needs*. https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs
- [F02] Nielsen Norman Group. *Task Analysis: Support Users in Achieving Their Goals*. https://www.nngroup.com/articles/task-analysis/
- [F03] Nielsen Norman Group. *Mental Models*. https://www.nngroup.com/articles/mental-models/
- [F04] Nielsen Norman Group. *Information Architecture: Study Guide*. https://www.nngroup.com/articles/ia-study-guide/
- [F05] Nielsen Norman Group. *Card Sorting: Uncover Users’ Mental Models*. https://www.nngroup.com/articles/card-sorting-definition/
- [F06] Nielsen Norman Group. *Tree Testing*. https://www.nngroup.com/articles/tree-testing/
- [F07] Nielsen Norman Group. *User Journeys vs. User Flows*. https://www.nngroup.com/articles/user-journeys-vs-user-flows/
- [F08] W3C. *WCAG 2.2 — 2.4.5 Multiple Ways*. https://www.w3.org/WAI/WCAG22/quickref/#multiple-ways
- [F09] W3C WAI. *Menus Tutorial — Structure*. https://www.w3.org/WAI/tutorials/menus/structure/
- [F10] GOV.UK Service Manual. *Map a user's whole problem*. https://www.gov.uk/service-manual/design/map-a-users-whole-problem

*Fin del Capítulo 03. Los casos, árboles y posibles hallazgos son ilustrativos; deben validarse antes de implementarse.*
