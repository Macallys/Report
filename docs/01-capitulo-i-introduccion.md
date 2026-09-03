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

Macallys radica en su capacidad de respuesta: ante un exceso de CO2, el sistema acciona automáticamente un ventilador de extracción para purificar el ambiente; si detecta operarios expuestos a concentraciones peligrosas de gas o ruido, dispara una bocina preventiva y puede accionar mamparas móviles de aislamiento acústico. 

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
      <td align="left"></td>
    </tr>
    <tr>
      <td align="left">Business Outcome Assumptions</td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="left">User Assumptions</td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="left">User Outcome and Benefit Assumptions</td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="left">Feature Assumptions</td>
      <td align="left"></td>
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

---

**Navegación:** [Índice](./00-student-outcome.md#s-tabla-contenidos) · Anterior: [Student Outcome](./00-student-outcome.md#s-student-outcome) · Siguiente: [Capítulo II](./02-capitulo-ii-requirements-elicitation.md)
