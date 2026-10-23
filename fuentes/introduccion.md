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

