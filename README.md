# Examen Virtualización - Carolina Páez

## Autor

Carolina Páez

---

# Justificación Técnica

Para esta solución opté por utilizar contenedores Docker debido a que permiten desplegar aplicaciones de forma rápida, ligera y portable. A diferencia de los hipervisores tradicionales, los contenedores comparten el sistema operativo del host, consumiendo menos recursos y facilitando la escalabilidad.

Docker Compose permite administrar múltiples servicios desde un único archivo de configuración, simplificando el despliegue y la comunicación entre componentes.

Respecto al modelo de nube, se utilizó una nube pública AWS debido a su disponibilidad inmediata, facilidad de administración y acceso remoto desde cualquier ubicación.

---

# Arquitectura de la Solución

La solución implementada está compuesta por tres servicios:

- NGINX como Reverse Proxy.
- Aplicación Flask desarrollada sobre Python.
- Base de datos PostgreSQL con persistencia mediante volumen Docker.

Flujo:

Usuario → NGINX → Aplicación Flask → PostgreSQL

Cada visita registrada es almacenada en PostgreSQL y se mantiene incluso después de reiniciar los contenedores gracias al volumen persistente.

---

# Despliegue

## Crear directorio

```bash
mkdir examen_virtualizacion
cd examen_virtualizacion
