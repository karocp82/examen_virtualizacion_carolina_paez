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

## Flujo de funcionamiento

Usuario → NGINX → Aplicación Flask → PostgreSQL

Cada visita registrada es almacenada en PostgreSQL y se mantiene incluso después de reiniciar los contenedores gracias al volumen persistente.

---

# Despliegue

## Crear directorio

```bash
mkdir examen_virtualizacion
cd examen_virtualizacion
```

## Construir imagen de la aplicación

```bash
docker build -t myapp-image .
```

## Levantar el stack completo

```bash
docker-compose up -d
```

## Verificar contenedores

```bash
docker-compose ps
```

## Reiniciar servicios

```bash
docker-compose restart
```

## Verificar funcionamiento

```bash
curl http://localhost
```

---

# Evidencias

## 1. Instancia EC2 creada

![Instancia EC2](evidencias/ec2.png)

La instancia EC2 fue creada en AWS Learner Lab utilizando Amazon Linux 2023.

---

## 2. Docker Engine instalado

![Docker instalado](evidencias/docker_version.png)

Verificación de la instalación de Docker Engine en la instancia EC2.

---

## 3. Imágenes Docker construidas

![Docker Images](evidencias/docker_images.png)

Se verifican las imágenes utilizadas para la solución.

---

## 4. Stack levantado con Docker Compose

![Docker Compose](evidencias/docker_compose_ps.png)

Los servicios PostgreSQL, Flask y NGINX se encuentran ejecutándose correctamente.

---

## 5. Persistencia de datos

### Antes del reinicio

![Visitas antes](evidencias/visitas_antes.png)

### Después del reinicio

![Visitas despues](evidencias/visitas_despues.png)

El contador continúa aumentando después del reinicio, demostrando la persistencia de datos mediante volumen Docker.

---

## 6. Docker Inspect

![Docker Inspect](evidencias/docker_inspect.png)

Se verifica la configuración interna del contenedor mediante el comando docker inspect.

---

## 7. Aplicación funcionando

![Aplicacion funcionando](evidencias/aplicacion_funcionando.png)

La aplicación se encuentra accesible desde el navegador a través de la IP pública de la instancia EC2.

---

# Conclusión

Durante esta evaluación implementé una solución basada en contenedores Docker utilizando Docker Compose para orquestar múltiples servicios. La arquitectura permitió integrar una aplicación Flask, una base de datos PostgreSQL y un servidor NGINX como punto de acceso.

Los resultados obtenidos demostraron la facilidad de despliegue, administración y portabilidad que ofrecen los contenedores, además de validar la persistencia de datos mediante volúmenes Docker. Finalmente, el uso de AWS como nube pública permitió publicar la solución de manera rápida y accesible desde Internet.
