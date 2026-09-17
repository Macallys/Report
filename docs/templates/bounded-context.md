<a id="s-4-2-x"></a>
# 4.2.X. Bounded Context: \<Bounded Context Name\>

> Plantilla. Copiar a `../bounded-contexts/bc-0N-<nombre>.md` y registrar en el Capítulo IV § 4.2.

**Navegación:** [Capítulo IV](../04-capitulo-iv-solution-software-design.md) · [Índice](../00-student-outcome.md#s-tabla-contenidos)

---

<a id="s-4-2-x-1"></a>
## 4.2.X.1. Domain Layer

Entities, Value Objects, Aggregates, Factories, Domain Services e interfaces de Repository que representan el core y las reglas de negocio del bounded context.

<table>
  <thead>
    <tr>
      <th align="left">Clase</th>
      <th align="left">Tipo</th>
      <th align="left">Propósito</th>
      <th align="left">Atributos</th>
      <th align="left">Métodos</th>
      <th align="left">Relaciones</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>

<a id="s-4-2-x-2"></a>
## 4.2.X.2. Interface Layer

Controllers y Consumers que exponen el bounded context hacia clientes (apps, otros BCs) o lo conectan a mensajería entrante.

<table>
  <thead>
    <tr>
      <th align="left">Clase</th>
      <th align="left">Tipo</th>
      <th align="left">Propósito</th>
      <th align="left">Métodos / Endpoints</th>
      <th align="left">Colabora con</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>

<a id="s-4-2-x-3"></a>
## 4.2.X.3. Application Layer

Command Handlers y Event Handlers que orquestan las capabilities del bounded context.

<table>
  <thead>
    <tr>
      <th align="left">Clase</th>
      <th align="left">Tipo</th>
      <th align="left">Comando / Evento</th>
      <th align="left">Propósito</th>
      <th align="left">Colabora con</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>

<a id="s-4-2-x-4"></a>
## 4.2.X.4. Infrastructure Layer

Implementaciones de las interfaces de Repository y MessageBroker definidas en el Domain Layer, y adaptadores hacia servicios externos (databases, messaging, email).

<table>
  <thead>
    <tr>
      <th align="left">Clase</th>
      <th align="left">Tipo</th>
      <th align="left">Interfaz que implementa</th>
      <th align="left">Servicio externo</th>
      <th align="left">Propósito</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>

<a id="s-4-2-x-5"></a>
## 4.2.X.5. Bounded Context Software Architecture Component Level Diagrams

![Component Level Diagram](../../assets/04-capitulo-iv/bounded-contexts/bc-x-component.png)

<a id="s-4-2-x-6"></a>
## 4.2.X.6. Bounded Context Software Architecture Code Level Diagrams

<a id="s-4-2-x-6-1"></a>
### 4.2.X.6.1. Bounded Context Domain Layer Class Diagrams

![Domain Layer Class Diagram](../../assets/04-capitulo-iv/bounded-contexts/bc-x-domain-class.png)

<a id="s-4-2-x-6-2"></a>
### 4.2.X.6.2. Bounded Context Database Design Diagram

![Database Design Diagram](../../assets/04-capitulo-iv/bounded-contexts/bc-x-database.png)
