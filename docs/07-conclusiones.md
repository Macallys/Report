**Navegación:** [Índice](./00-student-outcome.md#s-tabla-contenidos) · Anterior: [Capítulo VI](./06-capitulo-vi-product-implementation.md) · Siguiente: [Bibliografía](./08-bibliografia.md)

---

<a id="s-conclusiones"></a>
# Conclusiones

<a id="s-conclusiones-recomendaciones"></a>
## Conclusiones y recomendaciones

<a id="s-conclusiones-conclusiones"></a>
### Conclusiones

1. Como primera conclusión, Lean UX nos ayudó a entender el problema, a quién le afecta y qué espera de una herramienta. Escribir el problema, las suposiciones y las hipótesis antes de diseñar nos ordenó como equipo. Desde ahí separamos lo que vive el supervisor de seguridad de lo que vive el encargado de planta.

2. Como segunda conclusión, el análisis, los requerimientos y la arquitectura nos dejaron una imagen completa de SafePlant. Los contextos del dominio, las historias de usuario, el backlog y los diagramas C4 ordenaron quién hace qué. Con eso la plataforma puede juntar el monitoreo de CO₂, ruido y presencia, la actuación automática, el cuidado de los umbrales y la evidencia para las auditorías.

3. Como tercera conclusión, las entrevistas confirmaron que la exposición del personal es un problema del día a día. Hablamos con dos supervisores y tres encargados de planta, en metalmecánica, fundición y ensamblaje. Anyeli Vilcapaza contó que avisar, evacuar, medir con un equipo portátil y prender el extractor de respaldo tomó cerca de 25 minutos, con un operario ya afectado. Fabrizio Buselleu contó que tres sensores estuvieron caídos casi seis horas y nadie se enteró. Esos relatos nos sirvieron para escribir las historias de monitoreo, exposición y actuación (US14 a US35) y las historias técnicas de infraestructura y contingencia, con criterios que se pueden comprobar.

4. Como cuarta conclusión, el diseño del dominio dejó cuatro contextos claros: monitoreo de planta, seguridad y actuación, gestión del dispositivo en el borde, e identidad y acceso. El equipo IoT queda en el centro del sistema y la evaluación del riesgo tiene un solo dueño. Eso nos permite seguir una lectura desde el sensor hasta la evidencia del incidente.

5. Como quinta conclusión, el EventStorming de diseño y el flujo de mensajes nos sirvieron para revisar los caminos importantes antes de programar. Recorrimos la configuración de la planta, la llegada de las lecturas, la exposición y la actuación, el trabajo sin internet y el override del supervisor. Ahí vimos que detectar el dato y evaluar la exposición son pasos separados, que el actuador vuelve a su estado normal una sola vez, y que CO₂, ruido y presencia se guardan como hechos distintos.

6. Como sexta conclusión, el ciclo automático de seguridad tiene que vivir en el servidor de la planta. El ESP32 toma las lecturas y mueve los actuadores. El nodo del borde compara con los umbrales, ordena la extracción, la sirena o la mampara, y guarda el historial local. Así la protección sigue aunque no haya internet o la nube tarde en responder.

7. Como séptima conclusión, esa decisión encaja con lo que nos contaron en planta: el Wi-Fi se pierde entre las estructuras metálicas, la maquinaria vibra y el calor está cerca de los sensores. La respuesta sale rápido dentro de la red local. Los umbrales se actualizan desde el celular del supervisor, sin reprogramar el equipo. Si se corta el enlace, en la oficina se deja de ver el dato, pero en el área la protección continúa.

8. Como octava conclusión, la información viaja en los dos sentidos. Los sensores y el ESP32 suben las lecturas al nodo del borde y al broker MQTT. Ahí se cruza la medición con la presencia de personal y, cuando hay enlace, se sincroniza con el servidor. El supervisor ve la operación, las alertas y el historial corto en el celular. El encargado ve las métricas, el historial completo y la evidencia en la web. Hacia abajo, las áreas, los umbrales y los dispositivos que configura el supervisor llegan al borde y de ahí salen las órdenes al ESP32. El override de emergencia también sale de su celular, queda registrado, y el encargado lo revisa en la web.

9. Como novena conclusión, el Capítulo V dejó esa separación en las pantallas. El azul marino y el cian identifican a SAFEPLANT, y el verde, el ámbar y el rojo marcan si la condición es normal, de cuidado o crítica. En el celular el supervisor entra, ve el panel y las alertas, ajusta umbrales y revisa el historial y los dispositivos. En la web el encargado inicia sesión, activa la cuenta, consulta el panel y las alertas, y administra las cuentas, incluido el alta de un supervisor. Los dos recorridos quedaron explicados en video.

10. Como décima conclusión, el Sprint 1 del Capítulo VI dejó el primer incremento visible. Quedó la landing en GitHub Pages, las pantallas web del Encargado de Planta y el módulo Identity & Access del backend en Azure. Ese sprint cerró la presencia pública y la sesión, pero la web aún consumía datos de muestra y la ruta del dato IoT no estaba completa.

11. Como undécima conclusión, el Sprint 2 cerró la ruta del dato y conectó los tres canales. Cloud.Api quedó en Azure con Plant Monitoring, Safety & Actuation y Device & Edge Management. Plant.Host recibe MQTT y persiste en planta. La web en Vercel dejó los mocks y consume la API. La app móvil del Supervisor se publicó como APK v0.1.0 y opera sesión, panel, alertas, exposiciones, override y setup contra esa misma API.

12. Como duodécima conclusión, la evidencia de pruebas del Sprint 2 acompaña ese incremento. El backend sumó 44 Unit Tests en SafePlant.UnitTests. El frontend Angular pasó 64 casos con `ng test`. La app móvil Flutter pasó 296 casos. Esas suites y las capturas de ejecución y despliegue sostienen la revisión del sprint en el informe.

<a id="s-recomendaciones"></a>
### Recomendaciones

1. Como primera recomendación, seguir endureciendo la integración IoT en planta real. El metal, la vibración y el calor cerca de los sensores siguen siendo el mayor riesgo de que el dato deje de llegar, aunque el stack de laboratorio y el APK ya estén desplegados.

2. Como segunda recomendación, probar el dispositivo físico en una sola área de alto riesgo, como soldadura o fundición, con quienes trabajan ahí. Conviene corregir firmware y umbrales ahí antes de escalar al resto de la planta.

3. Como tercera recomendación, completar las entrevistas de validación del apartado 6.3 con supervisor y encargado por separado. Cada uno debe recorrer la pantalla que ya está en producción, no solo el prototipo del Capítulo V.

4. Como cuarta recomendación, poner en cada área un panel físico para reiniciar el equipo y manejar a mano el extractor, la sirena y la mampara cuando se cae la red. El override a distancia ya está en el celular del supervisor y se registra. En la web del encargado ese registro se consulta como evidencia.

5. Como quinta recomendación, guardar cada umbral con su autor, su fecha y la norma que se aplicó. Lo ajusta el supervisor desde el celular, por área, con el D.S. 015-2005-SA para el CO₂ y la R.M. 375-2008-TR para el ruido. El encargado ve ese historial en la web. El cambio debería poder aplicarse a las áreas que correspondan de una sola vez.

6. Como sexta recomendación, probar primero lo que falla en el entorno desplegado: corte de internet, equipo que deja de responder, reintento y sincronización al volver el enlace, cuidando que una misma lectura no se guarde dos veces. Si un sensor calla, el tablero tiene que mostrarlo como no disponible.

7. Como séptima recomendación, recoger lo que pidieron en las entrevistas del Capítulo II. En el celular, que la alerta crítica se distinga de la informativa y que los umbrales se calibren por área en el piloto. En la web, retener mediciones, alertas, acciones, anulaciones y cambios de configuración al menos doce meses, con exportación a PDF para SUNAFIL.

8. Como octava recomendación, mantener en el código la separación de canales que ya corre en Sprint 2. Umbrales, alta de dispositivos y override van en el celular del supervisor. Métricas, historial completo y gobernanza de cuentas van en la web del encargado.

9. Como novena recomendación, para el Trabajo Final conviene sumar avisos push en alertas críticas, más de un nodo por planta y una vista de exposición acumulada. También cerrar lo que quedó abierto en DEC-008, como el fallo de un relé y la política de identidad a largo plazo.

---

**Navegación:** [Índice](./00-student-outcome.md#s-tabla-contenidos) · Anterior: [Capítulo VI](./06-capitulo-vi-product-implementation.md) · Siguiente: [Bibliografía](./08-bibliografia.md)
