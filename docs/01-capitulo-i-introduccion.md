**Navegación:** [Índice](./00-student-outcome.md#s-tabla-contenidos) · Anterior: [Student Outcome](./00-student-outcome.md#s-student-outcome) · Siguiente: [Capítulo II](./02-capitulo-ii-requirements-elicitation.md)

---

<a id="s-cap-i"></a>
# Capítulo I: Introducción

<a id="s-1-1"></a>
## 1.1. Startup Profile

<a id="s-1-1-1"></a>
### 1.1.1. Descripción de la Startup

**Macallys** nace con el propósito de transformar y automatizar la gestión de la seguridad ambiental en el sector industrial, ofreciendo una solución tecnológica integral para plantas que buscan proteger la salud de sus operarios y optimizar el cumplimiento de normativas. Nuestra propuesta se centra en proporcionar prevención automatizada, visibilidad en tiempo real y entornos de trabajo seguros.

Nuestra plataforma, permite a las empresas monitorear centralizadamente la concentración de CO2, los niveles de contaminación sonora y la presencia de personal en zonas críticas. Con una aplicación móvil, los supervisores de seguridad pueden controlar remotamente los dispositivos, recibir alertas y actuar al instante. Por otro lado, los encargados de planta acceden a una plataforma web intuitiva para configurar los umbrales del sistema, revisar el historial de datos y gestionar las actualizaciones. 

Macallys radica en su capacidad de respuesta: ante un exceso de CO2, el sistema acciona automáticamente un ventilador de extracción para purificar el ambiente; si detecta operarios expuestos a concentraciones peligrosas de gas o ruido, dispara una bocina preventiva y puede accionar mamparas de aislamiento. 

Creemos firmemente que la digitalización y automatización de la seguridad industrial es el paso definitivo para garantizar la integridad de los trabajadores, reducir el ausentismo por problemas de salud y mejorar la sostenibilidad de las operaciones de manufactura e industria pesada.

**Misión:**
Nuestra misión es revolucionar la seguridad ocupacional en las plantas industriales mediante un sistema IoT inteligente que monitoree y mitigue automáticamente los riesgos ambientales.

**Visión:**
Aspiramos a convertirnos en el estándar líder en la automatización de la seguridad y salud en el trabajo en Latinoamérica, impulsando ecosistemas IoT que salven vidas y mejoren el bienestar laboral.


<a id="s-1-1-2"></a>
### 1.1.2. Perfiles de integrantes del equipo

<table>
  <thead>
    <tr>
      <th align="center">Foto</th>
      <th align="left">Apellidos y Nombres</th>
      <th align="left">Código</th>
      <th align="left">Carrera</th>
      <th align="left">Conocimientos técnicos y habilidades</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">![Integrante 1](../assets/01-capitulo-i/equipo/integrante-1.png)</td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left">Ingeniería de Software</td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="center">![Integrante 2](../assets/01-capitulo-i/equipo/integrante-2.png)</td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left">Ingeniería de Software</td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="center">![Integrante 3](../assets/01-capitulo-i/equipo/integrante-3.png)</td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left">Ingeniería de Software</td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="center">![Integrante 4](../assets/01-capitulo-i/equipo/integrante-4.png)</td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left">Ingeniería de Software</td>
      <td align="left"></td>
    </tr>
  </tbody>
</table>

<a id="s-1-2"></a>
## 1.2. Solution Profile

<a id="s-1-2-1"></a>
### 1.2.1 Antecedentes y problemática

**Antecedentes**

El sector industrial enfrenta retos constantes relacionados a la salud ocupacional y el cumplimiento de las normativas ambientales. Según la Organización Internacional del Trabajo, cada año se producen millones de casos de enfermedades profesionales en el mundo derivadas de la exposición prolongada a agentes químicos y físicos en el lugar de trabajo. La acumulación de CO2 en espacios confinados y la alta contaminación sonora por maquinaria pesada figuran entre los principales causantes de bajas médicas y problemas respiratorios. 

Las soluciones actuales implementadas en muchas plantas son insuficientes: dependen de mediciones manuales esporádicas o de sistemas antiguos que solo emiten alertas visuales en paneles fijos, pero no toman acciones correctivas de manera automática. Esto deja a los trabajadores expuestos al riesgo hasta que un operador humano se da cuenta y enciende un extractor o evacúa el área.

**Problematica**

**What (Qué)**
Las industrias enfrentan un alto riesgo de enfermedades ocupacionales y multas debido a la exposición prolongada de su personal a niveles tóxicos de CO2 y contaminación sonora excesiva.

**When (Cuándo)**
Los problemas de contaminación y ruido se evidencian principalmente durante los picos de producción, donde la maquinaria opera a máxima capacidad y se genera mayor combustión o ruido. El personal técnico está más ocupado y puede omitir las revisiones manuales de calidad ambiental.

**Where (Dónde)**
Los incidentes ocurren en las zonas críticas dentro de las plantas: cuartos de máquinas, zonas de ensamblaje cerrado, áreas de calderas y pasillos confinados donde la ventilación natural es nula y el eco del ruido se amplifica.

**Who (Quién)**
Los involucrados principales son los Operarios de planta, quienes sufren directamente las consecuencias en su salud, y los Supervisores de Seguridad, que deben monitorear estas variables pero carecen de herramientas remotas. 

**Why (Porqué)**
Se implementa para automatizar la respuesta de seguridad, protegiendo la salud del personal y evitando indemnizaciones o accidentes de planta. Este sistema funciona al reaccionar en segundos sin depender del error o la demora humana, centralizando la información en aplicaciones dedicadas.

**How (Cómo)**
Mediante la instalación de una red IoT compuesta por sensores de CO2, sonómetros y detectores de presencia conectados a la plataforma Macallys. El sistema acciona como mitigación en milisegundos si se rompe el limite permitido. A la par, el Encargado de Planta configura las métricas desde la App Web, y el Supervisor de Seguridad visualiza el estado en tiempo real desde su App Móvil.

**How much(Cuánto)**
- **Impacto económico:** Las multas impuestas por la SUNAFIL (Superintendencia Nacional de Fiscalización Laboral) por incumplimiento de normativas de salud en el trabajo pueden superar los miles de soles, sin contar las indemnizaciones médicas por pérdida auditiva irreversible.
- **Tiempos de inactividad:** Las evacuaciones de emergencia por acumulación de gases paralizan las líneas de producción, costando a la empresa miles de dólares por cada hora de inactividad.
<a id="s-1-2-2"></a>


<a id="s-1-2-2"></a>
### 1.2.2 Lean UX Process

<a id="s-1-2-2-1"></a>
#### 1.2.2.1. Lean UX Problem Statements

El estado actual de la seguridad ambiental en plantas industriales está enfocado principalmente en revisiones manuales periódicas, reportes estáticos y sistemas de alerta aislados que no interactúan de forma directa con los mecanismos de la planta.

Nuestro producto abordará esta brecha mediante un sistema IoT industrial que interconecta la monitorización de CO2 y ruido con mitigadores automáticos y aplicaciones de control remoto, permitiendo reaccionar en el acto y mantener a salvo al personal en zonas críticas.

Nuestro enfoque inicial estará dirigido a supervisores de seguridad en campo y encargados de gestión de planta.

Sabremos que hemos tenido éxito cuando observemos una reducción drástica en el tiempo de exposición a niveles peligrosos de ruido y CO2, y una disminución en los incidentes de salud reportados, medido a través de los reportes históricos que generará el sistema.

<a id="s-1-2-2-2"></a>
#### 1.2.2.2. Lean UX Assumptions

<table>
  <thead>
    <tr>
      <th align="left">Tipo de assumption</th>
      <th align="left">Enunciados (creencias)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">Business Assumptions</td>
      <td align="left">• Creemos que las industrias necesitan reducir sus tasas de ausentismo por salud y evitar sanciones regulatorias mediante la automatización de la seguridad.<br>• Estas necesidades se resuelven con un sistema IoT que no requiera reestructurar toda la planta, sino integrar sensores y actuadores manejables desde la web o móvil.<br>• Nuestros primeros clientes serán fábricas y plantas de procesamiento medianas y grandes.<br>• Valor esperado: Respuesta automática instantánea sin intervención humana.<br>• Beneficios adicionales: Monitoreo remoto 24/7, registro histórico para auditorías.<br>• Mayor riesgo: La conectividad y latencia de red dentro de zonas industriales con alta interferencia.<br>• Mitigación: Protocolos de comunicación ligeros y procesamiento Edge básico.</td>
    </tr>
    <tr>
      <td align="left">Business Outcome Assumptions</td>
      <td align="left">• Reducir en un 90% el tiempo de respuesta ante la acumulación de gases.<br>• Disminuir un 40% las alertas críticas mensuales gracias a la ventilación preventiva.<br>• Lograr que los supervisores usen la app móvil diariamente como su herramienta principal.</td>
    </tr>
    <tr>
      <td align="left">User Assumptions</td>
      <td align="left">• Usuarios: Supervisores de Seguridad y Encargados de planta.<br>• Contexto de uso: En el día a día de la operación industrial, el sistema funciona alertando anomalías. El encargado define umbrales en web y el supervisor monitorea recorriendo la planta.<br>• Problema a resolver: Falta de control remoto e incapacidad de accionar ventilación de manera inmediata.<br>• Características importantes: Alertas push inmediatas, gráficos de histórico de ruido, control de mitigadores y sensores.</td>
    </tr>
    <tr>
      <td align="left">User Outcome and Benefit Assumptions</td>
      <td align="left">• Ambientes de trabajo saludables sin depender de la revisión manual periódica.<br>• Eliminación del estrés operativo del supervisor al tener una herramienta centralizada.<br>• Auditorías simplificadas al contar con reportes de calidad del aire descargables.</td>
    </tr>
    <tr>
      <td align="left">Feature Assumptions</td>
      <td align="left">• Sensores interconectados que activan extractores.<br>• bocinas que retiran a la gente cuando no llevan protección auditiva.<br>• App Móvil de monitoreo remoto que da libertad de movimiento al supervisor de seguridad.<br>• Web que facilita al encargado de planta la parametrización de las zonas críticas.</td>
    </tr>
  </tbody>
</table>

<a id="s-1-2-2-3"></a>
#### 1.2.2.3. Lean UX Hypothesis Statements

<a id="s-1-2-2-4"></a>
#### 1.2.2.4. Lean UX Canvas

![Lean UX Canvas](../assets/01-capitulo-i/lean-ux/lean-ux-canvas.png)

<a id="s-1-3"></a>
## 1.3. Segmentos objetivo

#### **Segmento Objetivo 1: Supervisor de Seguridad (App Móvil)**

Profesionales encargados de la seguridad industrial en campo, que están en constante movimiento a lo largo de las distintas zonas críticas de la planta. Su herramienta principal es la pp Móvil, a través de la cual realizan el monitoreo en tiempo real de las métricas ambientales y el control del sistema. Se enfrentan a ruidos fuertes, espacios amplios y necesitan información de manera rápida a través de alertas push y notificaciones de emergencia. 

#### **Segmento Objetivo 2: Encargado de Planta (App Web)**

Personal de la gerencia técnica y operativa, responsables del rendimiento general y del cumplimiento normativo de la planta industrial. Trabaja mediante la **App Web**, desde una oficina o sala de control. Este segmento se encarga de la configuración del sistema, definiendo los topes máximos de CO2 o decibeles por cada zona de la fábrica. Además, analiza históricos, instala actualizaciones del software de los sensores y emite reportes ambientales semanales o mensuales para sustentar auditorías frente a los inspectores laborales.

---

**Navegación:** [Índice](./00-student-outcome.md#s-tabla-contenidos) · Anterior: [Student Outcome](./00-student-outcome.md#s-student-outcome) · Siguiente: [Capítulo II](./02-capitulo-ii-requirements-elicitation.md)
