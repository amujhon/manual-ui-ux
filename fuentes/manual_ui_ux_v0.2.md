# MANUAL INTEGRAL DE DISEÑO UI/UX

## Fundamentos, investigación, diseño de interacción, estándares e implementación

**Una guía para diseñar experiencias digitales comprensibles, accesibles, útiles y verificables.**

**Edición de trabajo:** 0.2  
**Fecha de edición:** 19 de octubre de 2026  
**Estado:** Entregas 01 y 02 integradas: páginas iniciales y capítulos 01–02  
**Ámbito tecnológico:** Web, Android, iOS y aplicaciones multiplataforma; ejemplos principalmente con HTML/CSS/JavaScript y Flutter/Dart.  
**Orientación:** Formación, consulta técnica y evaluación de productos.

> «Que una pantalla sea atractiva no demuestra que ayude a una persona a conseguir lo que necesita».  
> — Principio editorial de este manual.

---

# Presentación

Una interfaz digital es un punto de encuentro entre una persona y un sistema. La persona llega con una intención; el sistema dispone de información, reglas, procesos y restricciones; la interfaz debe hacer posible la interacción entre ambos. Cuando esa mediación falla, la persona puede no encontrar una opción, interpretar incorrectamente un resultado, repetir una operación o abandonar su tarea.

Los problemas de UI/UX no se limitan a botones demasiado pequeños o colores mal combinados. Un mensaje de error que no explica cómo continuar, un formulario que pierde datos, una búsqueda que devuelve información incorrecta o una operación cuyo estado permanece oculto son problemas de diseño tanto como de comportamiento del producto.

Este manual parte de una premisa práctica: **una decisión de diseño tiene valor cuando resuelve una necesidad real, respeta las restricciones pertinentes y puede justificarse y evaluarse**. No basta con afirmar que una solución «se ve mejor», «es más intuitiva» o «siempre se ha hecho así». Cada afirmación importante deberá vincularse, cuando corresponda, con evidencia, estándares, guías reconocidas o resultados observables.

El objetivo no es enseñar a copiar interfaces populares. Es formar el criterio necesario para comprender qué problema resuelve un patrón, por qué puede funcionar, en qué situaciones falla y cómo implementarlo sin sacrificar accesibilidad, consistencia ni mantenimiento.

La obra está concebida como un puente entre disciplinas: investigación de usuarios, psicología cognitiva, arquitectura de información, diseño visual, ingeniería de interfaces, pruebas de usabilidad y operación de productos digitales. Ninguna de ellas explica por sí sola la experiencia completa.

## A quién está dirigido

El contenido sirve a desarrolladores web y móviles, diseñadores UI/UX, investigadores de experiencia, responsables de producto, equipos de calidad y profesionales que deben revisar o mejorar sistemas existentes. No presupone formación previa en diseño gráfico, aunque los ejemplos de código sí distinguirán los conocimientos técnicos necesarios para implementarlos.

Tendrá especial atención a productos con uso repetitivo y consecuencias reales: plataformas educativas, servicios de autogestión, sistemas administrativos, paneles de control, formularios institucionales y aplicaciones móviles. Estos contextos exigen algo más que atractivo visual: claridad, prevención de errores, manejo de estados y trazabilidad de operaciones.

## Qué pretende y qué no pretende

**Pretende** enseñar a formular problemas, elegir patrones adecuados, construir componentes coherentes, probar decisiones, distinguir reglas obligatorias de recomendaciones contextuales y documentar las excepciones.

**No pretende** ofrecer un catálogo de verdades estéticas universales, sustituir pruebas con usuarios por intuición, garantizar cumplimiento normativo por utilizar una biblioteca de componentes ni asegurar que una aplicación sea accesible únicamente por superar una herramienta automática.

---

# Cómo utilizar este manual

El manual conserva la planificación general de **36 capítulos distribuidos en seis partes**:

| Parte | Capítulos | Tema |
|---|---|---|
| I | 01–06 | Fundamentos científicos, personas, cognición, heurísticas y accesibilidad |
| II | 07–12 | Jerarquía visual, tipografía, color, composición, iconografía y contenido |
| III | 13–20 | Sistemas de diseño, componentes, entradas, estados y retroalimentación |
| IV | 21–28 | Navegación, validaciones, formularios, flujos, búsquedas, tablas y permisos |
| V | 29–32 | Adaptación multiplataforma, accesibilidad avanzada, resiliencia y ética |
| VI | 33–36 | Prototipado, implementación web, implementación Flutter y auditoría |

Se proponen dos recorridos:

**Lectura formativa.** Avanzar desde los fundamentos hasta componentes, patrones y evaluación. Es el recorrido recomendado para quien necesita construir criterio desde cero.

**Consulta técnica.** Acudir al capítulo de un problema concreto, revisar sus prerrequisitos y utilizar la implementación y los criterios de evaluación. Un equipo que necesita corregir un formulario puede acudir a los capítulos 16, 22 y 23 sin releer toda la obra.

## Convenciones de evidencia

No todas las afirmaciones tendrán el mismo estatus. Para evitar falsas certezas, se utilizarán las siguientes etiquetas:

| Etiqueta | Significado | Cómo interpretarla |
|---|---|---|
| **[NORMA]** | Requisito establecido por un estándar o una obligación aplicable. | Identificar texto, versión, criterio y ámbito exactos. |
| **[GUÍA]** | Recomendación de una plataforma u organismo especializado. | Evaluar aplicabilidad, compatibilidad y excepciones. |
| **[HEURÍSTICA]** | Principio general para razonar sobre decisiones y detectar problemas. | No interpretarlo como ley absoluta ni garantía de calidad. |
| **[EVIDENCIA]** | Resultado publicado de una investigación, estudio o evaluación. | Revisar métodos, población, limitaciones y fecha. |
| **[CRITERIO EDITORIAL]** | Propuesta de aplicación de este manual. | Debe justificarse; no se presenta como obligación universal. |
| **[HIPÓTESIS]** | Explicación o mejora plausible todavía no validada en el producto concreto. | Requiere pruebas antes de darse por demostrada. |

Por ejemplo, [NORMA] el criterio WCAG 2.2 1.4.3 establece umbrales de contraste para determinados tipos de texto y condiciones. [GUÍA] una plataforma puede recomendar otros tamaños o estilos para sus componentes. [HEURÍSTICA] «mostrar el estado del sistema» ayuda a detectar posibles problemas, pero no determina por sí sola el texto, duración o disposición de un indicador. [HIPÓTESIS] colocar una acción principal al comienzo de una página puede mejorar su localización para ciertos usuarios: debe comprobarse con el público y las tareas relevantes.

**Regla de lectura:** una cita acredita una afirmación concreta, no todas las conclusiones que un autor pueda extraer de ella. Las normas ISO se utilizarán mediante sus fichas, extractos autorizados y fuentes secundarias identificadas; no se reproducirá su contenido íntegro, pues algunas publicaciones requieren licencia.

## Cómo se construyen los ejemplos

Se mostrarán condiciones normales y casos problemáticos. Las capturas o maquetas no deben confundirse con resultados de investigación. Cuando un ejemplo represente una propuesta de mejora, se distinguirá entre la justificación teórica y la verificación con usuarios.

Los ejemplos de código priorizarán semántica, estados, accesibilidad y estructura mantenible por encima de decoraciones innecesarias. Salvo indicación expresa, son demostraciones educativas con datos ficticios, no componentes certificados ni sistemas productivos auditados.

## Qué significa «terminar» un capítulo

Un capítulo se considera comprendido cuando el lector puede explicar sus conceptos, reconocer sus principales fallos, comparar al menos dos alternativas y justificar una decisión sin recurrir únicamente al gusto personal. En los capítulos prácticos se añadirá la capacidad de implementar el patrón y demostrar su funcionamiento mediante pruebas apropiadas.

---

# PARTE I · FUNDAMENTOS CIENTÍFICOS, CONCEPTUALES Y METODOLÓGICOS

# Capítulo 01. Introducción a UI, UX y HCI

**Nivel:** Fundamental.  
**Prerrequisitos:** Ninguno.  
**Conexiones posteriores:** Cap. 02 (investigación), 03 (arquitectura de información), 04 (cognición), 05 (heurísticas), 06 (accesibilidad).  
**Resultado esperado:** Ser capaz de describir una experiencia digital como un sistema de tareas, interacciones y resultados, y distinguir problemas visuales, funcionales, informacionales, de usabilidad y de accesibilidad.

## 1.1. El error de empezar por la pantalla

Imagina que una persona ingresa a un portal educativo porque necesita descargar una constancia de matrícula. Al abrir el sitio encuentra una pantalla limpia: encabezado equilibrado, colores institucionales, iconos consistentes y animaciones discretas. Sin embargo, no existe ninguna opción llamada «Constancia de matrícula». La operación está escondida en «Gestión → Recursos → Servicios → Documentos». Tras encontrarla, el sistema muestra «Operación finalizada», sin explicar si el documento se creó, se envió por correo o quedó pendiente.

La interfaz puede ser visualmente correcta y, aun así, la experiencia resultar deficiente. El problema no se soluciona necesariamente redibujando iconos: hay que estudiar la estructura de información, las palabras elegidas, la visibilidad de la acción, la respuesta del sistema y el objetivo que la persona intentaba cumplir.

Este caso introduce la diferencia central entre **la presentación y los mecanismos de interacción** y **la experiencia que emerge al intentar satisfacer una necesidad**.

No toda buena experiencia requiere una apariencia sofisticada. Una interfaz sobria, accesible, predecible y eficaz puede ser una solución superior a otra más decorada que aumenta los pasos o dificulta el reconocimiento de acciones.

### Un mismo problema visto desde varias disciplinas

| Perspectiva | Pregunta que formula ante el caso |
|---|---|
| UI | ¿La acción es visible, distinguible y comprensible en la pantalla? |
| Arquitectura de información | ¿La persona puede deducir dónde encontrar el documento? |
| Diseño de interacción | ¿Qué ocurre al activar la acción, esperar, fallar o volver atrás? |
| Diseño de contenido | ¿La etiqueta y los mensajes comunican con precisión qué sucede? |
| Usabilidad | ¿Puede completar la tarea de forma eficaz, eficiente y satisfactoria? |
| Accesibilidad | ¿Puede hacerlo también con teclado, lector de pantalla u otras adaptaciones? |
| UX | ¿Cómo percibe y vive todo el proceso, incluido el resultado y lo que ocurre después? |
| Ingeniería | ¿La funcionalidad produce datos correctos, seguros, disponibles y recuperables? |

Estas perspectivas se solapan; no son departamentos independientes ni una cadena rígida de trabajo.

## 1.2. Qué es una interfaz de usuario (UI)

**UI (User Interface)** es la parte de un sistema mediante la cual una persona recibe información, comprende opciones y ejecuta acciones. En productos gráficos incluye controles, distribución espacial, tipografía, iconografía, color y estados visuales; también abarca elementos de interacción más allá de lo puramente visual, como el manejo del foco, el teclado y la semántica de los componentes.

Dos interpretaciones incompletas son frecuentes:

- «UI significa escoger colores y dibujar pantallas». El diseño visual es una parte de la UI, pero la interfaz también expresa estado, opciones, restricciones y comportamiento.
- «UI equivale a UX». Una UI concreta participa en la experiencia, pero no la explica completamente. Latencia, errores de negocio, disponibilidad de información y expectativas previas también influyen en la UX.

**Ejemplo.** Un botón con la etiqueta «Descargar constancia» es una pieza de UI. También lo son su estado deshabilitado, el indicador de progreso, la explicación de por qué no está disponible y la confirmación de lo que ocurrió tras activarlo. La pantalla no está diseñada por completo si solo se dibuja el botón en su estado inicial.

## 1.3. Qué es la experiencia de usuario (UX)

**UX (User Experience)** se refiere a las percepciones y respuestas de una persona asociadas con el uso o uso anticipado de un producto, sistema o servicio. La experiencia se configura antes, durante y después de la interacción. Don Norman y Jakob Nielsen destacaron que la experiencia abarca el conjunto de interacciones con productos, servicios y organización; por ello no puede reducirse a la interfaz de una sola pantalla [F1].

En el caso de la constancia académica, la experiencia puede verse afectada por varios factores:

**Antes de usar.** ¿La persona sabe que el documento está disponible? ¿Es razonable esperar que pueda obtenerlo desde el celular? ¿Recuerda cómo ingresar?

**Durante el uso.** ¿Encuentra la opción? ¿Comprende si el documento corresponde al período académico correcto? ¿Puede descargarlo sin volver a introducir información que el sistema ya conoce?

**Después del uso.** ¿El archivo abre correctamente? ¿Tiene el contenido esperado? ¿Se informa claramente si requiere validación institucional? ¿Puede encontrarlo otra vez?

Una experiencia positiva no se demuestra con una calificación estética ni con el hecho de que la operación exista en el menú. Hay que observar el recorrido completo y sus consecuencias para las personas usuarias.

### UX como experiencia y UX como disciplina

Conviene distinguir dos usos del término. **UX como fenómeno** es lo que las personas efectivamente experimentan. **Diseño UX como práctica profesional** reúne métodos para investigar, modelar, mejorar y evaluar esa experiencia. Un equipo puede hacer actividades de UX y aun así entregar una mala experiencia; el uso de un método no garantiza el resultado [F2].

## 1.4. Qué es HCI y cómo se vincula con UI/UX

**HCI (Human–Computer Interaction)**, o interacción persona-computadora, es un campo interdisciplinario que estudia cómo las personas interactúan con sistemas informáticos y cómo diseñar y evaluar esas interacciones. Integra conocimientos de informática, psicología, ergonomía, ciencias cognitivas, diseño y otras disciplinas.

En términos prácticos, HCI ayuda a plantear preguntas como: ¿cuánto esfuerzo exige identificar una acción?, ¿cómo cambia el desempeño con la práctica?, ¿qué ocurre cuando el sistema responde tarde?, ¿cómo influyen la capacidad motriz y el contexto de uso?, ¿cómo detectar un error antes de que cause consecuencias?

No debe interpretarse como una jerarquía matemática en la que «HCI contiene UX y UX contiene UI» en todos los sentidos. Son conceptos y ámbitos de trabajo con distintos alcances, métodos y objetivos. El diagrama siguiente representa sus relaciones funcionales, no una clasificación formal de subconjuntos:

```mermaid
flowchart LR
    P[Persona y objetivos] --> I[Interacción con el sistema]
    C[Contexto de uso] --> I
    UI[Interfaz y controles] --> I
    S[Servicios, datos y reglas] --> I
    I --> R[Resultados de la tarea]
    R --> UX[Experiencia percibida]
    I --> UX
    UX --> E[Evaluación y mejoras]
    E --> UI
    E --> S
```

La calidad final depende de la colaboración entre investigación, diseño e ingeniería.

## 1.5. Usabilidad: eficaz, eficiente y satisfactoria para quién y en qué contexto

La norma **ISO 9241-11:2018** plantea la usabilidad en términos de la capacidad de usuarios especificados para lograr objetivos especificados con **eficacia, eficiencia y satisfacción**, en un **contexto de uso especificado**. La ficha oficial confirma que trata definiciones y conceptos de usabilidad, no un proceso de diseño prescrito [F3].

Las palabras «usuarios», «objetivos» y «contexto» son esenciales. No existe una única evaluación de usabilidad independiente de quién utiliza el sistema y para qué.

**Eficacia.** Grado en el que se alcanza el objetivo de manera correcta y completa. Descargar el archivo equivocado no cumple el objetivo, aunque la descarga técnica haya terminado sin errores.

**Eficiencia.** Recursos necesarios para obtener el resultado; pueden incluir tiempo, esfuerzo, pasos, carga mental o costos operativos, según el estudio.

**Satisfacción.** Percepción y respuesta de la persona durante y después del uso, evaluada mediante instrumentos apropiados. No debe inferirse automáticamente a partir del tiempo o número de clics.

### Ejemplo de métricas

En una prueba hipotética, ocho participantes intentan descargar una constancia. Seis obtienen el documento correcto sin ayuda; los otros dos no completan la tarea. La **tasa de finalización correcta observada** sería:

\[
\text{Tasa de éxito} = \frac{6}{8} \times 100 = 75\%.
\]

Este 75 % es **un dato ilustrativo ficticio**, no una medida real de una plataforma. No permite, por sí solo, conocer la causa de los fallos ni generalizar a toda una población. Sería necesario revisar tareas, participantes, incidencias, posibles sesgos y condiciones de prueba.

Del mismo modo, el tiempo medio de finalización debería calcularse y reportarse con una regla explícita: ¿se incluyen intentos fallidos?, ¿se reportan por separado?, ¿qué ocurre con quienes solicitan ayuda? Sin esa definición, dos cifras de «tiempo promedio» pueden no ser comparables.

### Cinco atributos útiles, sin confundirlos con la definición ISO

Nielsen Norman Group también caracteriza la usabilidad mediante facilidad de aprendizaje (*learnability*), eficiencia, memorabilidad, errores y satisfacción [F4]. Son dimensiones útiles para analizar una interfaz; no conviene presentarlas como sustitución literal de la formulación de ISO 9241-11.

Para un sistema administrativo de uso diario, podría ser crucial la eficiencia después del aprendizaje. Para un formulario de matrícula que una familia completa una vez al año, cobra mayor importancia el desempeño en el primer uso y la capacidad de retomar el proceso tras meses de inactividad.

**Consecuencia práctica:** no optimices un producto solo para el usuario experto si gran parte de sus usuarios son ocasionales.

## 1.6. Accesibilidad, inclusión y usabilidad: relación sin equivalencias falsas

La **accesibilidad** busca que las personas con discapacidad puedan percibir, comprender, navegar e interactuar con herramientas y contenidos digitales. La **usabilidad** aborda la eficacia, eficiencia y satisfacción en las tareas. El **diseño inclusivo** considera además la diversidad de circunstancias, capacidades, recursos y contextos. Son objetivos relacionados, pero no idénticos [F5].

Ejemplo: colocar una etiqueta visible y programáticamente asociada a un campo ayuda a usuarios que ven la pantalla y a quienes utilizan lectores de pantalla. Sin embargo, un formulario puede cumplir ciertos criterios técnicos de accesibilidad y continuar siendo demasiado largo, confuso o difícil de completar. A la inversa, que una prueba con usuarios sin discapacidad salga bien no demuestra que el formulario sea accesible.

La recomendación de este manual es abordar accesibilidad desde el inicio, incluir personas con necesidades diversas en las pruebas y verificar criterios normativos pertinentes. Las **WCAG 2.2** definen criterios verificables de accesibilidad web con niveles A, AA y AAA [F6]; no certifican por sí solas que toda la experiencia sea satisfactoria.

La conformidad WCAG para una página web se evalúa respecto de la página completa y sus variaciones, no de un control aislado que funciona correctamente [F6].

## 1.7. Arquitectura de información, interacción, visual y contenido

Estos conceptos suelen confundirse porque todos participan en una misma pantalla. Conviene separarlos analíticamente:

**Arquitectura de información (IA).** Organiza conceptos, secciones, relaciones, navegación y formas de encontrar contenido. En nuestro ejemplo, determina si la constancia debe pertenecer a «Mis documentos», «Trámites» u otra estructura basada en el lenguaje y las expectativas de quienes usan el sistema.

**Diseño de interacción (IxD).** Define la respuesta del producto a las acciones y la secuencia de eventos: activar «Consultar», mostrar espera, presentar el resultado, permitir reintento o cancelar una solicitud.

**Diseño visual.** Establece jerarquía, tipografía, espacio, color y otras propiedades de presentación para comunicar prioridades y relaciones.

**Diseño de contenido (content design / UX writing).** Define los textos y su relación con las tareas. «Documento generado» y «Tu constancia está disponible para descargar» no expresan exactamente lo mismo; el segundo comunica mejor una acción posible cuando esa disponibilidad es real.

**Diseño de servicio.** Considera la experiencia más allá de una pantalla: aprobación institucional, disponibilidad del documento, notificaciones, asistencia, entrega y procedimientos que pueden involucrar personas u otros sistemas.

En muchos productos, mejorar una experiencia requiere cambiar simultáneamente varias de estas capas. No se resolverá un problema de información con un color de botón distinto si la causa es que el documento ni siquiera existe en el sistema.

## 1.8. Objetivos, tareas, soluciones y restricciones

El diseño de calidad comienza distinguiendo lo que una persona **quiere lograr** de la interfaz que el equipo **propone construir**.

| Concepto | Ejemplo del caso |
|---|---|
| Necesidad | Disponer de una constancia de matrícula válida. |
| Objetivo | Obtener la constancia del período lectivo correspondiente. |
| Tarea | Localizar la constancia, comprobar sus datos y descargarla. |
| Solución propuesta | Un acceso directo desde «Mis documentos». |
| Restricción | El documento puede no estar emitido o requerir autorización. |
| Resultado esperado | Archivo correcto, identificable, disponible y comprensible. |

El error frecuente consiste en redactar la necesidad como una solución («necesitamos un botón azul en Inicio»). Esa frase no explica el objetivo, el problema real ni por qué la ubicación y el color serían adecuados.

**Reformulación útil:** «Las familias necesitan acceder a su constancia sin contactar a soporte. Queremos comprobar si un acceso identificado en la sección de documentos reduce los intentos fallidos y las consultas de ayuda, sin comprometer privacidad ni exactitud». Es una hipótesis de trabajo mejor formulada, no una mejora todavía demostrada.

## 1.9. Caso práctico completo: encontrar y consultar una constancia

### Escenario

Una persona representante accede desde un teléfono de gama media, con una conexión variable. Su objetivo es consultar el estado de su constancia de matrícula correspondiente al período actual. No conoce el nombre interno del módulo donde el equipo desarrollador almacenó el recurso.

### Alternativa A: organizada desde la lógica interna

La navegación presenta «Servicios» → «Gestión» → «Recursos» → «Emisión». Al completar el recorrido aparece la leyenda «Proceso exitoso» y un botón «Aceptar». La pantalla carece de nombre del documento, período y una acción clara para continuar.

Es un **ejemplo inventado de diseño problemático**, no una evaluación real de una plataforma. Los riesgos de esta propuesta son: terminología ambigua, exceso de exploración, incertidumbre acerca del resultado y dificultad para reconocer si se completó la tarea.

### Alternativa B: organizada alrededor de la tarea

Una sección «Mis documentos» muestra «Constancia de matrícula», el período correspondiente y un estado explícito. Cuando el documento está disponible, presenta «Ver constancia». Si no está listo, comunica «Pendiente de emisión» y ofrece una explicación o un canal de seguimiento adecuado. Se preserva el contexto del documento después de regresar desde el detalle.

Esta alternativa expresa mejor la tarea, pero sigue siendo **una hipótesis de diseño**, no una garantía de que funcionará. Su éxito depende de que las familias entiendan el término, encuentren la sección, reconozcan el período y reciban información correcta del backend.

### Comparación

| Aspecto | Alternativa A | Alternativa B |
|---|---|---|
| Lenguaje | Nombres internos y genéricos | Nombre de documento reconocible |
| Orientación | Recorrido de varias secciones | Categoría asociada con la tarea |
| Estado | «Proceso exitoso» ambiguo | Disponible / pendiente / error con significado |
| Identificación | Documento o período omitidos | Documento y período visibles |
| Recuperación | Continuación incierta | Acción o explicación contextual |
| Evidencia faltante | No se ha probado con usuarios | Tampoco se ha probado todavía |

Abre `ejemplos/comparacion-ui-ux.html` para explorar una comparación visual local y funcional. El ejemplo está deliberadamente simplificado y **no consulta una API**.

### Cómo comprobar la hipótesis

Define una tarea neutral: «Encuentra la constancia de matrícula correspondiente al período 2026–2027 e indica su estado». No digas a los participantes «haz clic en Mis documentos», porque eso revelaría la solución.

Registra si se llega al documento correcto sin ayuda, tiempo por tarea con un criterio uniforme, errores de interpretación, pasos inesperados y comentarios. Incluye usuarios ocasionales y al menos escenarios relevantes de accesibilidad. Compara alternativas de forma controlada cuando el tamaño y el método de investigación lo permitan. No declares una «mejora del 40 %» sin datos reales y un denominador verificable.

## 1.10. Del diseño a la implementación: la semántica importa

Es útil mostrar desde este capítulo que diseño e ingeniería se afectan mutuamente. El siguiente fragmento utiliza elementos HTML nativos y nombres de acciones explícitos:

```html
<section aria-labelledby="documents-title">
  <h2 id="documents-title">Mis documentos</h2>

  <article aria-labelledby="enrollment-title">
    <h3 id="enrollment-title">Constancia de matrícula</h3>
    <p>Período lectivo 2026–2027</p>
    <p>Estado: disponible</p>
    <a href="/documentos/constancia-matricula">
      Ver constancia de matrícula
    </a>
  </article>
</section>
```

**Qué hace bien este ejemplo:** establece títulos reconocibles, comunica el período y el estado mediante texto, y utiliza un enlace para acceder a otro recurso. **Qué no garantiza:** que la ruta exista, que el documento corresponda a la persona autenticada, que la respuesta del servidor sea segura, que haya manejo de errores o que el estilo final satisfaga todos los criterios de accesibilidad. Estos aspectos se diseñan y verifican por separado.

**[GUÍA]** Usar elementos HTML semánticos de forma apropiada favorece una representación comprensible para el navegador y las tecnologías asistivas. Para los campos de entrada, por ejemplo, MDN señala que `placeholder` no sustituye a la etiqueta `label`, porque desaparece y puede no ser anunciado adecuadamente [F7]. Este asunto se desarrollará en el capítulo 16.

### Una representación equivalente en Flutter

La siguiente variante reducida utiliza un elemento de lista para comunicar el estado y navegar al detalle mediante `Navigator`. El archivo `ejemplos/main.dart` desarrolla el mismo caso con una tarjeta y un selector de estados; no se ha ejecutado en este entorno.

```dart
ListTile(
  title: const Text('Constancia de matrícula'),
  subtitle: const Text(
    'Período 2026–2027 · Disponible',
  ),
  trailing: const Icon(Icons.chevron_right),
  onTap: () {
    Navigator.of(context).push(
      MaterialPageRoute<void>(
        builder: (_) => const DocumentDetailPage(),
      ),
    );
  },
)
```

El ejemplo supone que `DocumentDetailPage` existe y que el estado procede de datos fiables. En el archivo completo se proporciona una implementación mínima ejecutable. En una aplicación real también se comprobarían autorización, estados de espera, fallo, disponibilidad, foco y navegación accesible.

## 1.11. No hay un diseño «mejor» sin un contexto definido

Considera dos perfiles:

**Perfil 1. Usuario ocasional.** Ingresa una vez al año para completar una matrícula. Necesita acciones reconocibles, instrucciones claras y señales de progreso. La memorización de rutas resulta poco útil porque transcurre demasiado tiempo entre sesiones.

**Perfil 2. Operador habitual.** Trabaja cada día registrando cientos de movimientos. Puede necesitar atajos de teclado, navegación eficiente entre campos y una alta densidad de información. El exceso de confirmaciones podría ralentizarlo, aunque operaciones irreversibles continúan requiriendo controles adecuados al riesgo.

Una navegación minimalista puede ser apropiada para la primera persona y poco eficiente para la segunda. Esto no significa que deban existir dos productos completamente distintos, sino que las decisiones deben considerar tareas, frecuencia, riesgos, tecnología y capacidades.

En software educativo, sanitario o financiero, un error no es solo una molestia estética. Puede afectar trámites, decisiones o datos importantes. Cuanto mayor sea el impacto de una operación equivocada, mayor debe ser la atención prestada a prevención, claridad, confirmación y recuperación.

### Trade-offs: decisiones con costos

Una interfaz visualmente simple puede ocultar opciones y exigir mayor exploración. Una interfaz densa puede acelerar el trabajo experto y dificultar el primer uso. Las animaciones pueden ayudar a comunicar continuidad, pero también distraer o afectar a personas sensibles al movimiento. Mostrar confirmaciones puede prevenir acciones peligrosas, pero interrumpir innecesariamente tareas seguras y repetitivas.

Por ello este manual no aplicará «menos es más» como un mandato absoluto. La regla será: **eliminar complejidad que no aporta valor, sin ocultar información o controles que sí resultan necesarios para completar la tarea**.

## 1.12. Primer procedimiento de diagnóstico UI/UX

Antes de modificar una pantalla existente, realiza un diagnóstico breve basado en una tarea real:

1. **Identifica a la persona y su objetivo:** quién necesita hacer qué y por qué.
2. **Especifica el contexto:** dispositivo, frecuencia, experiencia, conectividad, idioma, accesibilidad y posibles consecuencias de fallar.
3. **Recorre la tarea de principio a fin:** incluye entrada, ejecución, espera, fallos, resultado y regreso.
4. **Separa síntomas y causas posibles:** «tardan en encontrarlo» no prueba que el color sea inadecuado; puede ser un problema de estructura o terminología.
5. **Registra hipótesis y evidencia:** distingue lo observado de lo que sospechas.
6. **Propón la mínima intervención razonable:** modifica el componente, la estructura o el comportamiento que realmente origina el problema.
7. **Define cómo se comprobará:** éxito, tiempo, errores, comprensión, accesibilidad y efectos no deseados.

No todos los proyectos requieren el mismo volumen de investigación, pero todos deberían conservar una explicación verificable de por qué se decidió cambiar algo.

## 1.13. Ejercicio de aplicación

**Situación:** una app muestra un botón llamado «Procesar» al final de un formulario. Tras pulsarlo, aparece un indicador de carga durante varios segundos y luego la pantalla se cierra. El usuario no sabe si la solicitud se registró y a veces vuelve a enviarla.

**Tu trabajo:** identifica el objetivo de la persona; enumera al menos tres explicaciones posibles del problema; distingue qué pertenece a UI, interacción, UX e ingeniería; plantea una mejora sin suponer que la petición se completó; especifica al menos dos pruebas para evaluar el resultado.

### Una solución orientativa

El objetivo no es «presionar Procesar», sino registrar una solicitud correctamente y conocer su estado. Una posible mejora incluye un nombre de acción explícito, prevención de envíos duplicados mientras la operación está pendiente, resultado confirmado por la respuesta fiable del servidor y un identificador o mecanismo de seguimiento. Si la conexión falla, el sistema debe diferenciar «no enviado», «estado desconocido» y «registrado» según la evidencia disponible.

Esta propuesta no justifica mostrar «Solicitud enviada» antes de confirmar que el servidor la recibió. Tampoco resuelve por sí sola idempotencia, persistencia y seguridad, que pertenecen a la implementación integral del proceso.

## 1.14. Lista de verificación del capítulo

Al concluir, comprueba que puedes responder con ejemplos propios:

- ¿En qué difieren UI, UX, HCI, usabilidad y accesibilidad?
- ¿Por qué una interfaz bonita puede resultar poco útil?
- ¿Qué papel cumplen usuario, objetivo y contexto en la definición de usabilidad?
- ¿Cómo distingues necesidad, tarea, solución y restricción?
- ¿Por qué un estudio con ocho personas no equivale a una afirmación universal?
- ¿Qué debe mostrar el sistema cuando una operación está pendiente o falla?
- ¿Cómo explicas una decisión de diseño sin basarte solo en preferencias estéticas?

**Criterio de dominio:** formular un diagnóstico del caso práctico con una hipótesis explícita, una propuesta justificable y un modo razonable de evaluarla.

## 1.15. Relaciones con los capítulos siguientes

- **Capítulo 02 — Investigación de usuarios:** cómo obtener evidencia sobre personas, tareas y expectativas sin inventarlas.
- **Capítulo 03 — Modelos mentales y arquitectura de información:** por qué algunas rutas y etiquetas resultan reconocibles y otras no.
- **Capítulo 04 — Psicología cognitiva:** qué mecanismos explican la atención, la decisión y el esfuerzo mental.
- **Capítulo 05 — Heurísticas:** cómo inspeccionar sistemáticamente posibles problemas de interacción.
- **Capítulo 06 — Accesibilidad:** cómo diseñar y comprobar que distintas personas pueden usar el producto.

---

# Referencias verificadas de esta entrega

**[F1]** Don Norman y Jakob Nielsen. *The Definition of User Experience (UX).* Nielsen Norman Group. https://www.nngroup.com/articles/definition-user-experience/

**[F2]** Kate Kaplan. *What Is User Experience (and What Is It Not)?* Nielsen Norman Group, 2024. https://www.nngroup.com/articles/what-is-user-experience/

**[F3]** ISO. *ISO 9241-11:2018 — Ergonomics of human-system interaction — Part 11: Usability: Definitions and concepts.* Ficha oficial; revisión y confirmación en 2023. https://www.iso.org/standard/63500.html

**[F4]** Jakob Nielsen. *Usability 101: Introduction to Usability.* Nielsen Norman Group, 2012; revisión de 2026. https://www.nngroup.com/articles/usability-101-introduction-to-usability/

**[F5]** W3C WAI. *Accessibility, Usability, and Inclusion.* https://www.w3.org/WAI/fundamentals/accessibility-usability-inclusion/

**[F6]** W3C. *Web Content Accessibility Guidelines (WCAG) 2.2.* https://www.w3.org/TR/WCAG22/

**[F7]** MDN Web Docs. *HTML placeholder attribute.* https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/placeholder

**[F8]** ISO. *ISO 9241-210:2019 — Human-centred design for interactive systems.* Ficha oficial; revisión y confirmación en 2025. https://www.iso.org/standard/77520.html

**[F9]** NIST. *Human Centered Design (HCD).* https://www.nist.gov/itl/iad/human-centered-technologies/human-factors-human-centered-design

**[F10]** Jakob Nielsen. *10 Usability Heuristics for User Interface Design.* Nielsen Norman Group, 1994; revisión de 2024. https://www.nngroup.com/articles/ten-usability-heuristics/

**Observación editorial:** Las referencias están ligadas al contenido de esta entrega. En próximos capítulos se citarán fuentes especializadas adicionales y se consignarán versiones de plataformas o componentes cuando puedan afectar una implementación.

---

**Fin del Capítulo 01 (primera entrega).**


# Capítulo 02. Investigación de usuarios y diseño centrado en las personas

**Parte I · Fundamentos científicos, conceptuales y metodológicos**  
**Nivel:** Fundamental–intermedio.  
**Prerrequisito:** Capítulo 01.  
**Lecturas relacionadas:** Capítulo 03 (tareas y arquitectura de información), 05 (heurísticas), 06 (accesibilidad), 21 (navegación), 23 (formularios), 33 (prototipado y pruebas) y 36 (métricas y auditoría).  
**Resultados de aprendizaje:** formular preguntas de investigación verificables; seleccionar métodos según la incertidumbre; reclutar participantes pertinentes; conducir entrevistas sin inducir respuestas; distinguir observación, interpretación e hipótesis; producir hallazgos trazables; proteger a los participantes; y transformar evidencia en decisiones de producto.

> **Idea rectora:** investigar usuarios no es preguntarles qué interfaz les gustaría. Es obtener evidencia suficientemente fiable acerca de qué intentan lograr, cómo trabajan, qué les impide avanzar y bajo qué condiciones usan el sistema.

## 2.1. El problema de diseñar a partir de suposiciones

Una plataforma educativa recibe una petición: «Necesitamos un botón para que las familias descarguen los certificados más rápido». El equipo podría ejecutar la solicitud literalmente: agregar un botón visible en la página de inicio, asignarle un icono y considerarlo resuelto. Pero detrás de esa petición podrían existir problemas muy diferentes:

- El certificado existe, pero su ubicación no coincide con el vocabulario de las familias.
- La búsqueda funciona, pero se usa una cuenta equivocada cuando una persona representa a varios estudiantes.
- El certificado depende de una aprobación y la plataforma no comunica su estado.
- La descarga ocurre, pero algunos usuarios no saben dónde encontrar el archivo en su teléfono.
- El problema se manifiesta solo con conexiones inestables, tecnologías asistivas o dispositivos compartidos.

Estas explicaciones son **hipótesis, no hechos**. Elegir cualquiera antes de investigar puede producir una interfaz vistosa que no elimina la causa del problema.

La diferencia entre diseñar por intuición y diseñar con evidencia no significa prescindir de la experiencia profesional. Significa emplearla para formular mejores preguntas, proponer alternativas y decidir qué incertidumbres son suficientemente importantes como para investigarlas.

| Afirmación inicial | ¿Qué sabemos realmente? | Pregunta investigable |
|---|---|---|
| «Los representantes no entienden el módulo». | Hay una percepción de dificultad, pero no conocemos la tarea ni la causa. | ¿En qué paso y ante qué información se detienen? |
| «Hay que poner un botón más grande». | Existe una solución propuesta, no un diagnóstico. | ¿Los participantes localizan la acción y pueden activarla? |
| «Todos quieren recibirlo por WhatsApp». | No consta la distribución de preferencias ni las restricciones de privacidad. | ¿Cómo reciben, almacenan y comparten hoy sus documentos? |
| «El problema es que no saben usar tecnología». | Es una atribución sobre las personas sin evidencia. | ¿Qué terminología, estados o decisiones de la interfaz provocan errores? |

**[CRITERIO EDITORIAL]** Antes de implementar una solicitud de UI, registrar: problema declarado, evidencia disponible, supuestos, consecuencias de equivocarse y prueba mínima que permitiría tomar una decisión más informada.

## 2.2. Diseño centrado en las personas: qué establece ISO 9241-210

**ISO 9241-210:2019** trata principios y actividades de diseño centrado en las personas a lo largo del ciclo de vida de los sistemas interactivos. Su ficha oficial describe requisitos y recomendaciones sobre el proceso, no reglas de color, tipografía ni composición de pantallas [C02-F01]. La norma es aplicable tanto a proyectos nuevos como a la evolución de productos existentes.

En este manual sintetizamos el proceso operativo mediante cuatro actividades estrechamente relacionadas:

1. **Comprender y especificar el contexto de uso.** ¿Quién utilizará el producto?, ¿qué tareas realizará?, ¿con qué dispositivos, conocimientos, apoyos y restricciones?
2. **Especificar requisitos centrados en las personas.** ¿Qué resultados y condiciones debe permitir el sistema?, ¿qué barreras no son aceptables?
3. **Producir soluciones de diseño.** Explorar flujos, contenido, componentes y prototipos acordes con los requisitos.
4. **Evaluar las soluciones frente a los requisitos.** Observar si las personas pueden cumplir sus objetivos y actualizar lo que aún no sabemos.

Las cuatro actividades se retroalimentan. Un prototipo puede revelar un requisito omitido; una sesión de observación puede mostrar que el público inicialmente definido era incompleto; una implementación puede obligar a revisar restricciones. Por ello el enfoque es **iterativo**, no una cascada rígida en la que la investigación termina antes de escribir código.

```mermaid
flowchart TB
    A[Comprender el contexto de uso] --> B[Definir necesidades y requisitos]
    B --> C[Proponer soluciones]
    C --> D[Evaluar con evidencia]
    D -->|Persisten incertidumbres| A
    D -->|Se identifican ajustes| C
    D -->|Criterios suficientes| E[Publicar y seguir aprendiendo]
    E -->|Cambian usuarios o contexto| A
```

**[NORMA / ALCANCE]** La descripción anterior es una síntesis pedagógica del enfoque. No constituye una reproducción completa de ISO 9241-210 ni una certificación de conformidad. Para invocar cumplimiento formal, deben consultarse sus requisitos íntegros y la edición aplicable.

## 2.3. Usuario, cliente, actor y parte interesada no son sinónimos

En productos institucionales suele pagar una organización mientras otras personas realizan el trabajo. Los términos deben separarse:

- **Usuario directo:** interactúa con la interfaz para cumplir una tarea. Ej.: un docente registra notas.
- **Usuario indirecto o afectado:** recibe consecuencias del sistema aunque no ejecute esa operación. Ej.: un estudiante cuya calificación depende de lo registrado.
- **Cliente o comprador:** contrata o financia el producto. Ej.: una institución.
- **Administrador y soporte:** configuran, autorizan, corrigen o atienden incidentes; también son usuarios, con tareas propias.
- **Parte interesada (*stakeholder*):** cualquier actor con intereses legítimos o responsabilidades relevantes, incluidas áreas legales y de seguridad.

Escuchar solo al comprador deja fuera a quienes padecerán errores en el uso cotidiano. Escuchar únicamente a usuarios frecuentes puede dejar fuera a nuevos usuarios o personas que dejaron de utilizar el servicio.

### Unidad de análisis: persona + tarea + contexto

Un mismo ser humano puede comportarse de manera diferente según la tarea. Un representante que consulta tareas todos los días puede tener dificultades para completar una matrícula anual. Una docente experta puede dominar la carga de calificaciones, pero no un trámite administrativo poco frecuente.

La unidad de estudio no debe ser «un usuario promedio» abstracto, sino el conjunto **quién realiza qué, bajo qué condiciones y con qué consecuencias**. El contexto incluye dispositivo, conectividad, entorno físico, idioma, experiencia previa, apoyos disponibles, presión de tiempo y riesgos de error.

## 2.4. Qué preguntas responde cada tipo de investigación

No basta con elegir entre «entrevista» o «encuesta». Las metodologías se diferencian por al menos tres ejes descritos por Nielsen Norman Group: **actitud frente a conducta**, **cualitativo frente a cuantitativo** y **contexto de la interacción** [C02-F02]. A esto conviene sumar el momento de decisión y el grado de madurez del producto.

| Dimensión | Pregunta | Ejemplos | Precaución |
|---|---|---|---|
| Actitudinal | ¿Qué piensa, recuerda o declara la persona? | Entrevistas, encuestas. | Las respuestas no sustituyen la conducta observada. |
| Conductual | ¿Qué hace realmente? | Observación, tareas de usabilidad, registros de eventos. | La conducta requiere interpretación contextual. |
| Cualitativa | ¿Cómo y por qué ocurre algo? | Entrevistas abiertas, observación contextual. | Una muestra pequeña no estima porcentajes poblacionales. |
| Cuantitativa | ¿Con qué frecuencia o magnitud ocurre? | Encuestas correctamente muestreadas, analítica y estudios de tareas con métricas. | La selección y definición de métricas condicionan la validez. |
| Generativa / descubrimiento | ¿Cuál es el problema o necesidad? | Investigación contextual, entrevistas sobre experiencias pasadas. | No confundir solicitudes de funciones con necesidades. |
| Evaluativa | ¿Esta alternativa permite completar la tarea? | Pruebas de usabilidad, experimentos. | No evaluar solo satisfacción declarada. |

**Ejemplo:** una entrevista puede revelar que una persona tiene miedo de «dañar» la matrícula si retrocede; una prueba de usabilidad puede mostrar que busca repetidamente un botón «Guardar borrador»; la analítica puede mostrar cuántas sesiones quedan incompletas. Son piezas complementarias, no respuestas intercambiables.

### Matriz rápida de selección

| Incertidumbre principal | Método prioritario | Método complementario |
|---|---|---|
| No comprendemos una necesidad | Entrevistas sobre experiencias reales | Observación de contexto |
| No conocemos el proceso fuera de pantalla | Observación contextual | Diario de actividades |
| No sabemos si encuentran una sección | *Tree testing* o prueba de tareas | Entrevistas posteriores |
| Las personas no completan un formulario | Prueba de usabilidad moderada | Analítica de pasos y errores |
| Queremos medir prevalencia en una población | Encuesta con muestreo diseñado | Análisis de sesgo/no respuesta |
| Queremos comparar dos variantes | Experimento controlado, si es viable | Investigación cualitativa sobre el resultado |
| Queremos evaluar accesibilidad real | Pruebas con usuarios con discapacidad | Evaluación WCAG por especialistas |

**No se debe diseñar la investigación comenzando por la técnica favorita del equipo.** Primero se define la decisión a tomar y después se elige la evidencia necesaria.

## 2.5. Formular un problema, una hipótesis y una pregunta de investigación

Un problema bien enunciado se refiere a una situación observada o documentada, no a la ausencia de una función inventada:

- **Débil:** «Hace falta agregar un botón de descarga».
- **Mejor:** «Algunas familias no logran obtener una constancia sin solicitar ayuda».
- **Más preciso, si está sustentado:** «En tickets de soporte de septiembre, varias solicitudes se refieren a la localización de la constancia; no sabemos si el origen es navegación, permisos o disponibilidad».

**Problema ≠ hipótesis ≠ pregunta ≠ solución.**

| Elemento | Ejemplo |
|---|---|
| Observación inicial | Se reciben consultas repetidas por la descarga de documentos. |
| Hipótesis H1 | La etiqueta actual no coincide con el vocabulario del público. |
| Hipótesis H2 | La operación depende de un estado de aprobación que no se comunica. |
| Pregunta P1 | ¿Qué palabras usan las familias para describir el documento? |
| Pregunta P2 | ¿Qué ocurre cuando intentan descargarlo y aún no está habilitado? |
| Decisión posible | Renombrar navegación, explicar estados o corregir la lógica de disponibilidad, según los hallazgos. |

Un objetivo operativo sería: «Identificar las principales barreras que impiden a representantes obtener el documento correcto desde el teléfono y priorizar una solución verificable». Debe definirse también qué resultados llevarían a **no cambiar la interfaz**: por ejemplo, si la causa demostrada fuera un proceso institucional externo.

### Registro de supuestos

Antes de investigar, conviene listar supuestos con su impacto y evidencia. No hay una puntuación universal obligatoria; una matriz sencilla puede considerar *incertidumbre*, *riesgo* y *coste de equivocarse*. Prioriza las afirmaciones que, de ser falsas, provocarían trabajo innecesario o consecuencias graves.

## 2.6. Planificar una investigación pequeña pero rigurosa

Según el Service Manual de GOV.UK, una ronda de investigación debería definir objetivos, supuestos, participantes, actividades, consentimientos, logística y tiempo para análisis [C02-F03]. El formato puede ocupar una sola página en proyectos pequeños.

**Plan resumido — ejemplo ficticio**

| Campo | Decisión |
|---|---|
| Problema | Dificultad para obtener una constancia académica. |
| Decisión pendiente | Cambiar navegación, lenguaje, estados o procedimiento. |
| Población | Representantes que solicitan constancias; soporte como actor complementario. |
| Segmentación | Uso frecuente/ocasional; Android/iOS/web; distintos niveles de familiaridad. |
| Métodos | 6 entrevistas exploratorias y 6 pruebas de tareas como punto de partida ajustable. |
| Reclutamiento | Diferentes instituciones y patrones de uso, sin limitarse a quienes ya reclamaron. |
| Evidencia adicional | Tipos de tickets anonimizados y eventos agregados disponibles. |
| Riesgos | Datos académicos, terceros visibles en pantalla, dispositivos compartidos. |
| Protección | Datos sintéticos; consentimiento específico; acceso limitado a notas. |
| Resultados esperados | Hallazgos trazables, alternativas priorizadas y plan de validación. |

**Los números son una decisión de planificación ilustrativa, no un tamaño muestral universal.** Se revisan al observar diversidad, repetición de hallazgos, riesgos y necesidad de inferencia estadística.

La plantilla editable se entrega en `plantillas/plan_investigacion.md`.

## 2.7. Reclutamiento y muestreo: encontrar a las personas correctas

Un estudio puede estar perfectamente moderado y, aun así, fallar si selecciona a personas que no representan los contextos pertinentes.

### Muestreo intencional para descubrir mecanismos

En estudios cualitativos, es habitual reclutar según características relevantes para la pregunta: frecuencia de uso, tipo de tarea, acceso, experiencia, condiciones de discapacidad, casos exitosos y fallidos. No implica representatividad estadística; pretende abarcar variabilidad útil.

En nuestro caso, una muestra formada únicamente por personal de soporte no describiría cómo interactúan familias nuevas. Una muestra formada solo por personas que completaron la descarga excluiría barreras que impidieron llegar al resultado.

### Encuestas y representatividad

Un enlace de encuesta enviado únicamente dentro de la app llega principalmente a quienes pueden entrar, leen el aviso y deciden responder. Es probable que omita a personas sin acceso, con bajas competencias digitales o que abandonaron el producto. La OCDE advierte que los medios de contacto y la no respuesta generan sesgos de selección que no desaparecen automáticamente con muchas respuestas [C02-F04].

**[EVIDENCIA]** Una muestra grande obtenida por autoselección no adquiere representatividad solo por aumentar el número de respuestas.

### ¿Cinco participantes son suficientes?

La recomendación popular de alrededor de cinco participantes se refiere a determinadas **rondas de pruebas cualitativas de usabilidad orientadas a descubrir problemas**, no a toda entrevista, encuesta, estudio de accesibilidad o prueba cuantitativa. Nielsen Norman Group enfatiza que la investigación para estimar métricas de población requiere muestras y diseño distintos [C02-F05].

- En un estudio **exploratorio**, se ajusta el reclutamiento a la diversidad de situaciones y a la aparición de nueva evidencia.
- Para **comparar tasas o estimar porcentajes**, se necesita un plan estadístico con margen de error, confianza, variación y selección apropiada.
- En **accesibilidad**, importa la diversidad de tecnologías asistivas y estrategias; una sola persona no representa a todas las demás [C02-F06].

No se impondrá un «N mágico» válido para todos los casos.

## 2.8. Entrevistas: descubrir experiencias sin poner respuestas en boca del participante

Una entrevista de investigación no es una demostración comercial, una reunión de requisitos ni una votación sobre pantallas. Nielsen Norman Group la caracteriza como un método para comprender experiencias, necesidades, valores y motivaciones de usuarios [C02-F07].

### Preguntas útiles y preguntas sesgadas

| Evitar | Preferir | Por qué |
|---|---|---|
| «¿Te gustaría un botón rápido para descargar?» | «Cuéntame la última vez que necesitaste ese documento». | Evita orientar hacia una solución. |
| «¿Fue confuso nuestro sistema?» | «¿Qué esperabas que ocurriera en ese punto?» | Evita etiquetar la experiencia por adelantado. |
| «¿No crees que tres pasos son demasiados?» | «¿Cómo decidiste qué hacer después?» | Busca conducta y razonamiento en vez de aprobación. |
| «¿Siempre revisas las notificaciones?» | «Piensa en la última notificación: ¿qué hiciste con ella?» | Reduce generalizaciones y sesgo de recuerdo. |

### Guion recomendado

1. **Apertura:** explicar propósito, duración, participación voluntaria, tratamiento de datos y eventual grabación; verificar consentimiento.
2. **Contexto:** «¿Con qué dispositivo acostumbras consultar información académica?».
3. **Último episodio real:** «¿Cuándo fue la última vez que necesitaste una constancia? ¿Cómo lo resolviste?».
4. **Profundización:** «¿Qué te hizo elegir esa opción?», «¿Qué sucedió después?», «¿Hubo alguna alternativa?».
5. **Contraste:** pedir que relate un episodio con resultado diferente, si existe.
6. **Cierre:** «¿Hay algo importante que no te pregunté?»; aclarar qué ocurrirá con los datos y recordar los mecanismos acordados para retirarse.

El moderador debe escuchar, evitar completar frases, tolerar silencios e indagar hechos concretos. Si se presenta una interfaz y se observa su uso, debe distinguirse ese segmento como **prueba de tareas**, aunque ocurra en la misma sesión.

## 2.9. Observación contextual: lo que una entrevista no puede revelar

Una persona puede afirmar que «descargar un certificado es fácil», pero durante la observación cambiar de aplicación, buscar en el correo, preguntar a un familiar y reenviarse el archivo. La observación contextual permite estudiar el flujo real, incluidos atajos, herramientas externas y restricciones del entorno [C02-F08].

**Procedimiento sugerido:** acordar una tarea cotidiana; obtener permisos; observar sin intervenir de forma innecesaria; anotar acciones y condiciones; preguntar al final por comportamientos que requieran explicación; distinguir hechos de inferencias.

**Ejemplo de registro:**

| Momento | Observación literal | Interpretación provisional |
|---|---|---|
| 10:04 | Participante abre «Comunicaciones». | Esperaba encontrar el certificado allí. |
| 10:05 | Vuelve y entra a «Repositorio». | La categorización podría ser ambigua. |
| 10:07 | Pregunta si el archivo llegará al correo. | El destino o estado de entrega podría ser poco claro. |

El registro de observación no debe afirmar «no entiende» si solo se observó una navegación alternativa. **La conducta es el dato; la explicación es una hipótesis que debe contrastarse.**

### Otras técnicas de descubrimiento

- **Estudios de diario:** las personas registran episodios durante días o semanas; útiles para tareas poco frecuentes o distribuidas en el tiempo; sensibles a abandonos y memoria.
- **Análisis de soporte:** agrupa problemas reportados; útil para detectar temas, pero no mide prevalencia entre quienes nunca contactan soporte.
- **Analítica de uso:** aporta secuencias y eventos; sin contexto no revela por qué alguien se detuvo.
- **Talleres de co-diseño:** producen ideas y lenguaje con participantes; no garantizan que la solución ideada funcione.

## 2.10. Encuestas: medir opiniones y características con cuidado

Las encuestas sirven para describir respuestas de una población o muestra, comparar segmentos y detectar patrones actitudinales. No son una alternativa barata universal a entrevistas u observación.

**Buenas prácticas:** definir la población objetivo; reclutar por un procedimiento explícito; formular preguntas neutras y de una sola idea; ofrecer opciones exhaustivas cuando sea pertinente; no exigir datos sensibles innecesarios; evitar escalas inconsistentes; probar el cuestionario antes de publicarlo; reportar no respuestas y canal de distribución.

**Mal planteada:** «¿Qué tan rápida y fácil es nuestra excelente plataforma?» mezcla atributos y sugiere la respuesta. **Mejor:** «Durante la última ocasión en que buscaste un documento, ¿lograste encontrarlo?» con opciones definidas y una pregunta independiente para dificultades experimentadas.

Si se usa una escala de 1 a 5, deben identificarse ambos extremos y mantener la dirección consistente. Una media numérica de una muestra de conveniencia puede resumir lo observado, pero no justifica inferir un promedio de toda la población.

### Ejemplo de encuesta mínima sin recolección real

1. ¿Has intentado obtener una constancia en los últimos seis meses? (Sí / No / No recuerdo).
2. Si lo intentaste, ¿cuál fue el resultado? (Obtuve el documento correcto / Otro documento / No pude obtenerlo / No recuerdo).
3. ¿Desde qué dispositivo realizaste el último intento? (Teléfono / Computadora / Tableta / Otro).
4. ¿Qué dificultad experimentaste? (Respuesta abierta, opcional).

Este cuestionario es solo una plantilla de partida; antes de aplicarlo deben revisarse su validez, flujo condicional, accesibilidad y consentimiento. El archivo HTML de esta entrega **no registra ni transmite respuestas de personas**; es un laboratorio local para diseñar estudios.

## 2.11. De datos dispersos a hallazgos defendibles

La investigación produce notas, episodios, frases, capturas, registros y estadísticas. El desafío no es acumularlos, sino convertirlos en interpretaciones que permitan tomar decisiones sin confundir certeza y posibilidad.

El proceso descrito por GOV.UK recomienda extraer observaciones, agruparlas por temas, sintetizar hallazgos y decidir acciones; también sugiere analizar los resultados con varias personas del equipo para reducir sesgos individuales [C02-F09].

**Cadena de trazabilidad:**

```mermaid
flowchart LR
    D[Dato observado] --> E[Evidencia verificable]
    E --> H[Hallazgo acotado]
    H --> I[Implicación de diseño]
    I --> P[Propuesta / hipótesis]
    P --> T[Prueba de validación]
```

### Ejemplo: evidencia frente a conclusión apresurada

**Dato ficticio:** en una prueba de tareas, cuatro participantes buscaron inicialmente la constancia en «Mis documentos»; la sección real se llamaba «Servicios institucionales». Dos lograron encontrarla sin ayuda y dos necesitaron indicaciones.

**Inferencia débil:** «El 50 % de todos los representantes no sabe utilizar la plataforma».

**Hallazgo defendible:** «En esta prueba cualitativa, dos de cuatro participantes no localizaron la constancia sin ayuda. Los cuatro buscaron inicialmente en una sección con una etiqueta diferente; la estructura y el vocabulario son candidatos a revisión». La redacción conserva límites de muestra y contexto.

**Hipótesis de mejora:** utilizar un nombre reconocible para el documento y ubicarlo donde el público espera encontrarlo.

**Cómo validarla:** realizar una prueba comparativa de localización con participantes pertinentes y comprobar tasa de finalización, errores y rutas recorridas; diseñar un estudio cuantitativo si se requiere estimar impacto poblacional.

### Matriz de hallazgos

| ID | Observación | Fuentes | Hallazgo | Confianza | Acción siguiente |
|---|---|---|---|---|---|
| H-01 | Se busca el documento en otras secciones. | P-01, P-02, P-04 | Posible desajuste de vocabulario. | Media; evidencia limitada. | Probar alternativas de denominación. |
| H-02 | Se interpreta «Procesado» como «Disponible». | P-03 y soporte S-02 | Un estado podría comunicar disponibilidad erróneamente. | Baja–media; pendiente de contraste. | Revisar reglas y mensajes con equipo técnico. |

Los IDs anteriores son datos inventados para demostrar trazabilidad. El nivel de confianza no es una probabilidad matemática; documenta calidad, diversidad y consistencia de las evidencias de forma cualitativa. Mantener una **evidencia contradictoria** es igualmente importante: si alguien encontró el documento sin dificultad, registrar qué experiencia o condición lo explica.

## 2.12. Personas, segmentos y arquetipos: útiles solo si proceden de datos

Una *persona* es una representación compuesta de un patrón de necesidades, comportamientos y contextos relevante para diseñar. No debe confundirse con una fotografía, una edad arbitraria y una biografía inventada.

**Ejemplo didáctico, no una persona validada:**

> **Arquetipo provisional: representante con tareas esporádicas.** Ingresa al sistema unas pocas veces por período para trámites específicos. Necesita reconocer rápidamente el documento correcto, distinguir si está disponible y obtener una confirmación inequívoca. Puede usar un dispositivo compartido y no recordar el camino utilizado meses atrás. **Origen:** hipótesis del equipo hasta contrastar con investigación.

Una ficha de persona basada en evidencia debería documentar: patrón de tareas, objetivo principal, frecuencia, condiciones, dificultades, estrategias, fuentes, fecha, segmentos donde aplica y grado de confianza.

**Errores frecuentes:** inventar características demográficas irrelevantes; creer que una persona representa a «todas las madres» o «todos los docentes»; describir deseos sin ejemplos reales; fijar una persona que nunca se revisa; usar categorías estereotipadas de edad o discapacidad.

El uso efectivo de personas también es un asunto de ingeniería de requisitos: un estudio de profesionales publicado en 2024 identificó diferencias de uso y desafíos al trasladar personas a procesos reales de desarrollo [C02-F10]. Por eso el artefacto solo merece mantenerse si ayuda a decidir.

## 2.13. Jobs to Be Done: entender el progreso que la persona busca

El enfoque **Jobs to Be Done (JTBD)** pone el énfasis en el resultado que una persona intenta conseguir dentro de una situación. Puede complementar a las personas: estas ayudan a describir patrones de usuarios y contextos; JTBD ayuda a explicar la motivación de una tarea [C02-F11].

Una formulación práctica es:

> **Cuando** [contexto y situación], **quiero** [progreso o acción necesaria], **para** [resultado importante].

**Ejemplo:** «Cuando una institución me pide una constancia de matrícula para un trámite, quiero obtener un documento vigente y verificable desde mi teléfono, para presentarlo sin depender de atención presencial».

Esta formulación es mejor que «quiero un botón azul», porque no presupone el mecanismo. Podría resolverse con una descarga, una vista de verificación o un envío seguro, dependiendo de requisitos y restricciones que aún deben comprobarse.

**Precaución:** JTBD no demuestra por sí solo qué solución funciona; necesita investigación y evaluación. Tampoco sustituye a la definición de actores, permisos o contextos de accesibilidad.

## 2.14. Segmentación: diferenciar necesidades sin fragmentar el producto

Segmentar significa agrupar personas o situaciones por características **relevantes para una decisión de diseño**, no necesariamente por edad o cargo.

Para una plataforma educativa, algunos ejes plausibles de segmentación son:

- **Frecuencia de uso:** primera vez, uso ocasional, uso cotidiano.
- **Responsabilidad:** consulta de información, captura de datos, aprobación, administración.
- **Complejidad:** un estudiante o varios; una institución o múltiples entidades.
- **Condiciones de uso:** móvil compartido, conexión intermitente, tecnologías asistivas.
- **Experiencia técnica:** familiaridad con una tarea concreta, no «nivel digital» genérico.

Una persona puede pertenecer simultáneamente a varios segmentos. El objetivo no es fabricar veinte versiones de la UI, sino identificar qué necesidades pueden compartirse y cuáles requieren adaptación.

**Regla:** no convertir segmentos derivados de una muestra cualitativa en proporciones poblacionales, ni inferir discapacidad, situación económica o capacidades a partir de estereotipos.

## 2.15. Ética, consentimiento y protección de participantes

La investigación con personas puede generar riesgos si se graban pantallas con datos de estudiantes, se publican citas reconocibles o se presiona a alguien a participar. El Service Manual de GOV.UK exige, para sus investigaciones, consentimiento informado y explica qué información debe comunicarse antes de participar [C02-F12]. Se toma como guía metodológica, no como sustitución de la legislación ecuatoriana ni de la evaluación jurídica del proyecto.

### Información mínima a comunicar

1. Quién realiza la investigación y para qué.
2. Qué actividad se realizará, su duración y qué datos se recogerán.
3. Si habrá grabaciones, observadores o servicios externos de transcripción.
4. Cómo se almacenará, utilizará, compartirá y eliminará la información.
5. Que participar es voluntario y cómo detenerse o solicitar la retirada según las condiciones informadas y obligaciones aplicables.
6. Un canal de contacto para dudas o derechos.

**[CRITERIO EDITORIAL]** La participación en investigación no debe condicionarse a recibir un servicio institucional ordinario; hay que prevenir relaciones de presión entre docentes, instituciones, estudiantes, familias y personal administrativo.

### Minimización de datos

Para estudiar si se encuentra un certificado, normalmente no hace falta recopilar números de cédula, calificaciones, diagnósticos, direcciones o documentos reales. Utiliza cuentas de prueba, datos sintéticos y escenarios ficticios. Separa información de contacto del contenido de la investigación. Evita enviar grabaciones o transcripciones identificables a servicios externos sin base y autorizaciones apropiadas. Define tiempos de conservación y responsabilidades.

La orientación de GOV.UK sobre privacidad recomienda recopilar solo información necesaria y prestar especial atención a datos sensibles y datos relativos a menores [C02-F13].

### Investigación con niñas, niños y adolescentes

La investigación en entornos educativos puede involucrar menores de edad. En tales casos, los procedimientos deben adaptarse a edad, comprensión, consentimiento de representantes o responsables según el marco aplicable, asentimiento del menor y medidas de protección. El Department for Education del Reino Unido ofrece guías específicas sobre bienestar, salvaguardas y participación activa de niños y jóvenes [C02-F14].

No asumiremos que el consentimiento de una institución sustituye automáticamente a todas las autorizaciones necesarias ni que los requisitos de otro país sean directamente exigibles en Ecuador. La regla operativa es realizar una revisión ética y jurídica local antes de estudiar a menores o tratar datos sensibles.

## 2.16. Accesibilidad de la propia investigación

Una investigación excluyente produce conclusiones incompletas. Si las sesiones exigen necesariamente videollamada, teclado físico, visión normal o lectura rápida, es posible que queden fuera personas relevantes para el producto.

**Preparaciones recomendadas:** información y consentimiento en formatos accesibles; canales alternativos de comunicación; pausas; espacio físico accesible; tiempo suficiente; respeto por tecnologías asistivas; preguntas comprensibles; posibilidad de evitar grabaciones innecesarias; y reclutamiento de participantes con distintas estrategias de interacción.

W3C WAI recomienda incluir personas con discapacidad durante todo el proyecto y recuerda que ninguna persona representa por sí sola a todo un grupo; además, las pruebas con usuarios **complementan pero no reemplazan** la evaluación de conformidad con WCAG [C02-F06].

Ejemplo: si una persona que usa lector de pantalla no encuentra el botón, registrar la secuencia observada, plataforma, lector, dispositivo y contexto; no concluir inmediatamente que «todos los lectores fallan». El diagnóstico puede requerir inspeccionar orden de foco, semántica del control o comportamiento de la tecnología asistiva.

## 2.17. Sesgos y amenazas a la validez

**Sesgo de confirmación:** buscar evidencia que respalde la solución que el equipo ya eligió. *Control:* formular hipótesis alternativas y registrar resultados que las contradicen.

**Sesgo de selección:** estudiar solo a personas fáciles de reclutar o muy comprometidas con el producto. *Control:* considerar quién falta y por qué.

**Sesgo de cortesía o deseabilidad social:** participantes dicen que todo está bien ante quien desarrolló el sistema. *Control:* preguntas neutrales, moderadores que no defiendan el producto y observación real.

**Sesgo de recuerdo:** las personas reconstruyen incorrectamente episodios pasados. *Control:* solicitar episodios recientes y contrastar con registros apropiados.

**Efecto de observación:** saber que se está siendo observado puede cambiar la conducta. *Control:* explicar la sesión, permitir familiarización y considerar métodos en contexto real.

**Confusión por variables externas:** cambios de red, permisos, experiencia o datos pueden explicar una diferencia aparente entre interfaces. *Control:* documentar condiciones y, en experimentos, controlar factores relevantes.

### Cuatro preguntas de control

- ¿Qué evidencia contradice nuestra interpretación?
- ¿Qué grupos o situaciones no estudiamos?
- ¿Una explicación alternativa encaja igual de bien con lo observado?
- ¿Qué decisión cambiaríamos si este hallazgo resultara falso?

Responder estas preguntas mejora el rigor incluso cuando el equipo tiene poco presupuesto.

## 2.18. Caso práctico integrado: investigar la descarga de una constancia

**Todos los datos de este caso son ficticios y solo tienen propósito educativo.** No describen hallazgos reales de ningún producto.

### Paso A. Definir incertidumbre

El equipo observa solicitudes de soporte acerca de constancias. No conoce las causas. Plantea tres hipótesis: H1, terminología confusa; H2, estado del documento mal comunicado; H3, descarga terminada pero archivo difícil de localizar.

### Paso B. Planificar y reclutar

Organiza entrevistas breves con representantes de uso esporádico y frecuente, incorpora distintas condiciones de dispositivo y accesibilidad, y prepara cuentas de prueba sin datos reales. Los criterios de inclusión se vinculan al objetivo de la tarea, no solo a disponibilidad.

### Paso C. Observar tareas

Se propone un escenario neutral: «Necesitas presentar una constancia de matrícula vigente. Usando esta cuenta de prueba, intenta obtenerla». El moderador no dice qué menú contiene el archivo. Si la sesión permite preguntas, se registran por separado las indicaciones dadas.

### Paso D. Registrar evidencias

| Participante | Evidencia sintética | Hipótesis relacionada |
|---|---|---|
| P-01 | Buscó primero en «Documentos». | H1 |
| P-02 | Interpretó «Generado» como disponible para descarga. | H2 |
| P-03 | Descargó el archivo, pero buscó un mensaje sobre dónde se guardó. | H3 |
| P-04 | Encontró la acción sin ayuda. | Evidencia contraria a una dificultad universal |

No se obtiene una «tasa de problemas del 75 %». Se identifican mecanismos plausibles para probar, porque cada fila describe situaciones diferentes y el número de observaciones es deliberadamente pequeño.

### Paso E. Decidir intervenciones

- **Para H1:** preparar denominaciones alternativas y probar su capacidad de localización antes de modificar toda la navegación.
- **Para H2:** verificar primero las reglas reales del backend; después diferenciar «En proceso», «Disponible» y «No disponible» sin inventar estados.
- **Para H3:** ofrecer un mensaje posterior consistente con el comportamiento de cada plataforma, evitando afirmar que el archivo está en una ruta desconocida.

### Paso F. Validar y documentar

Realizar tareas con la variante revisada, registrar errores y ayuda requerida, comparar condiciones equivalentes y contrastar con las hipótesis originales. Si el cambio afecta documentos sensibles, incorporar revisión de autorizaciones y accesibilidad. Un hallazgo sin responsable, decisión ni prueba futura corre el riesgo de convertirse en una nota archivada.

## 2.19. Código aplicado: instrumentación de eventos sin registrar datos sensibles

La investigación conductual puede apoyarse en telemetría limitada y autorizada. La siguiente estructura de ejemplo en **Dart** muestra cómo registrar eventos de tarea **sin** incluir nombres, cédulas, identificadores de estudiantes ni contenido del documento. La integración concreta con un proveedor de analítica debe respetar permisos, políticas de privacidad y configuración de consentimiento aplicable.

```dart
/// Ejemplo conceptual para una aplicación Flutter/Dart.
/// No envía información a ningún servicio.
enum ResultadoTarea { completada, fallida, abandonada }

class EventoTarea {
  final String nombreTarea; // Vocabulario cerrado, p. ej. 'descargar_constancia'
  final ResultadoTarea resultado;
  final int duracionMilisegundos;

  const EventoTarea({
    required this.nombreTarea,
    required this.resultado,
    required this.duracionMilisegundos,
  });

  Map<String, Object> toSafeMap() => {
        'tarea': nombreTarea,
        'resultado': resultado.name,
        'duracion_ms': duracionMilisegundos,
      };
}

void registrarLocalmente(EventoTarea evento, {required bool permitido}) {
  if (!permitido) return;
  // Un repositorio real aplicaría límites, controles de acceso y retención.
  final registro = evento.toSafeMap();
  assert(!registro.containsKey('cedula'));
  // En este ejemplo, no se transmite ni persiste el registro.
}
```

Este fragmento **no constituye una implementación de producción**: no cubre almacenamiento seguro, retención, agregación, concurrencia, obligaciones legales ni amenazas de reidentificación. Incluso un conjunto de eventos aparentemente anónimos puede volverse identificable al combinarse con otros datos. Además, los eventos solo dicen *qué ocurrió en el sistema instrumentado*, no necesariamente *qué experimentó la persona*.

El paquete incluye `ejemplos/c02_analisis.py`, un ejercicio reproducible con CSV sintético que separa eventos observados de inferencias y calcula únicamente medidas descriptivas del conjunto de práctica. El capítulo 36 estudiará diseño formal de métricas, intervalos de confianza y pruebas cuantitativas.

## 2.20. Laboratorio visual: distinguir hechos, interpretaciones y decisiones

La demostración `ejemplos/c02_laboratorio.html` presenta una pequeña investigación simulada con cuatro momentos:

1. **Pregunta:** elegir qué se necesita aprender antes de elegir una técnica.
2. **Evidencia:** revisar registros observacionales ficticios.
3. **Interpretación:** diferenciar una conclusión exagerada de un hallazgo limitado a la muestra.
4. **Acción:** decidir qué hipótesis de diseño probar sin presentarla como confirmada.

El laboratorio funciona localmente, sin servidor, almacenamiento ni transferencia de datos. Su valor está en practicar la distinción entre observar, explicar y decidir, no en simular resultados estadísticos válidos.

### Ejercicio individual

Lee el siguiente caso: «Tres usuarios abandonaron un formulario cuando apareció la sección de datos del representante». Escribe:

1. **Dos explicaciones rivales** que no atribuyan el problema a incapacidad de los participantes.
2. **Un método** para averiguar qué sucedió y por qué.
3. **Una observación neutral** que registrarías durante la sesión.
4. **Una métrica** que estudiarías después, distinguiendo su denominador y limitaciones.
5. **Una decisión que todavía no tomarías** por falta de evidencia.

Una respuesta razonable podría considerar la complejidad de los campos, el desconocimiento de información requerida o el temor a compartir datos. La investigación podría combinar observación de tareas y entrevistas posteriores. No bastaría con cambiar el color del botón «Continuar».

## 2.21. Lista de verificación del capítulo

Marca cada punto solo si puedes justificarlo con un ejemplo:

- [ ] Diferencio una necesidad real, una solicitud de funcionalidad, una hipótesis y una solución.
- [ ] Conozco el papel y alcance de ISO 9241-210.
- [ ] Sé distinguir usuarios directos, afectados, compradores y otras partes interesadas.
- [ ] Puedo elegir métodos actitudinales/conductuales y cualitativos/cuantitativos según una decisión pendiente.
- [ ] Elaboro preguntas de entrevista que no conduzcan artificialmente a una respuesta.
- [ ] Documento criterios de reclutamiento y grupos no incluidos.
- [ ] No convierto muestras cualitativas pequeñas en porcentajes poblacionales.
- [ ] Mantengo trazabilidad entre observación, hallazgo, recomendación y validación.
- [ ] Identifico sesgos e hipótesis rivales.
- [ ] Preparo consentimiento, minimización de datos y medidas de accesibilidad.
- [ ] Considero salvaguardas adicionales para menores y datos académicos.
- [ ] Puedo transformar una petición de UI en un plan de investigación sencillo y accionable.

**Criterio de dominio:** producir un plan de una página, una guía de entrevista neutral, una tabla de evidencias y dos decisiones posibles condicionadas a resultados distintos.

## 2.22. Relaciones con los capítulos siguientes

- **Capítulo 03 · Objetivos, tareas, modelos mentales y arquitectura de información.** Toma los datos sobre vocabulario, secuencia de tareas y necesidades para estructurar navegación y contenido. **Se recomienda leerlo después de este capítulo.**
- **Capítulo 04 · Psicología cognitiva.** Explica mecanismos que pueden sustentar hipótesis; no reemplaza la investigación contextual.
- **Capítulo 05 · Heurísticas.** Ayuda a detectar problemas hipotéticos durante inspecciones expertas y a priorizar pruebas posteriores.
- **Capítulo 06 · Accesibilidad.** Profundiza en criterios verificables y en la diversidad de necesidades investigadas aquí.
- **Capítulo 23 · Formularios.** Utiliza investigación sobre errores, campos, secuencias y tareas antes de decidir el diseño.
- **Capítulo 33 · Prototipos y pruebas.** Enseña con mayor profundidad cómo evaluar propuestas de solución, incluyendo investigación evaluativa.
- **Capítulo 36 · Auditoría y métricas.** Traduce preguntas y hallazgos en indicadores bien definidos, controles de calidad y seguimiento.

---

# Referencias verificadas del Capítulo 02

**[C02-F01]** ISO. *ISO 9241-210:2019 — Ergonomics of human-system interaction — Part 210: Human-centred design for interactive systems.* Ficha oficial: https://www.iso.org/standard/77520.html. Consulta: 19 de octubre de 2026. La ficha describe el alcance; el texto completo de la norma puede requerir licencia.

**[C02-F02]** Nielsen Norman Group. Christian Rohrer. *When to Use Which User-Experience Research Methods.* https://www.nngroup.com/articles/which-ux-research-methods/. Consulta: 19 de octubre de 2026.

**[C02-F03]** GOV.UK Service Manual. *Plan a round of user research.* https://www.gov.uk/service-manual/user-research/plan-round-of-user-research. Consulta: 19 de octubre de 2026.

**[C02-F04]** OECD. *Survey design and technical documentation supporting the OECD Risks that Matter Survey* (2025), apartado sobre muestreo y sesgo de no respuesta. https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/07/survey-design-and-technical-documentation-supporting-the-oecd-risks-that-matter-survey_dfd831d9/5eebe551-en.pdf. Consulta: 19 de octubre de 2026.

**[C02-F05]** Nielsen Norman Group. Raluca Budiu. *Why 5 Participants Are Okay in a Qualitative Study, but Not in a Quantitative One.* https://www.nngroup.com/articles/5-test-users-qual-quant/. Consulta: 19 de octubre de 2026.

**[C02-F06]** W3C Web Accessibility Initiative. *Involving Users in Evaluating Web Accessibility.* https://www.w3.org/WAI/test-evaluate/involving-users/ y *Involving Users in Web Projects for Better, Easier Accessibility.* https://www.w3.org/WAI/planning/involving-users/. Consulta: 19 de octubre de 2026.

**[C02-F07]** Nielsen Norman Group. Maria Rosala y Kara Pernice. *User Interviews 101.* Publicado en 2023; última revisión indicada en 2026. https://www.nngroup.com/articles/user-interviews/. Consulta: 19 de octubre de 2026.

**[C02-F08]** GOV.UK Service Manual. *Contextual research and observation.* https://www.gov.uk/service-manual/user-research/contextual-research-and-observation. Consulta: 19 de octubre de 2026.

**[C02-F09]** GOV.UK Service Manual. *Analyse a research session.* https://www.gov.uk/service-manual/user-research/analyse-a-research-session. Consulta: 19 de octubre de 2026.

**[C02-F10]** Wang, Y. et al. (2024). *Who Uses Personas in Requirements Engineering: The Practitioners' Perspective.* Estudio empírico de prácticas profesionales. https://arxiv.org/abs/2403.15917. Consulta: 19 de octubre de 2026.

**[C02-F11]** Nielsen Norman Group. *Personas vs. Jobs-to-Be-Done.* https://www.nngroup.com/articles/personas-jobs-be-done/. Consulta: 19 de octubre de 2026.

**[C02-F12]** GOV.UK Service Manual. *Getting informed consent for user research.* https://www.gov.uk/service-manual/user-research/getting-users-consent-for-research. Consulta: 19 de octubre de 2026.

**[C02-F13]** GOV.UK Service Manual. *Managing user research data and participant privacy.* https://www.gov.uk/service-manual/user-research/managing-user-research-data-participant-privacy. Consulta: 19 de octubre de 2026.

**[C02-F14]** UK Department for Education. *Research with children and young people.* https://user-research.education.gov.uk/guidance/ethics-and-safeguarding/research-with-children-and-young-people. Consulta: 19 de octubre de 2026. Referencia metodológica extranjera, no asesoría legal ecuatoriana; la propia página advierte que parte de su orientación está en revisión.

**Nota de método:** Los ejemplos, participantes, resultados y métricas de este capítulo son sintéticos. No se han realizado entrevistas, experimentos ni estudios de usabilidad reales para elaborar los ejemplos. Las referencias fundamentan conceptos y métodos; no constituyen evidencia empírica sobre una plataforma educativa concreta.

---

**Fin del Capítulo 02.** El próximo capítulo previsto es *03. Objetivos, tareas, modelos mentales y arquitectura de información*.
