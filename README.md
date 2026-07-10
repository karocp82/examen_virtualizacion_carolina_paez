Examen Virtualización - Carolina Páez
Autor

Carolina Páez

Descripción del Proyecto

Este proyecto corresponde al desarrollo de una solución basada en contenedores Docker desplegada sobre una instancia EC2 de AWS.

La arquitectura implementada considera tres servicios principales:

NGINX como servidor web y proxy inverso.
Aplicación Flask desarrollada en Python.
Base de datos PostgreSQL con persistencia mediante volúmenes Docker.

La aplicación registra visitas y almacena la información en PostgreSQL, permitiendo conservar los datos incluso después de reiniciar los contenedores.

Justificación Técnica

Para esta solución opté por utilizar contenedores Docker debido a que permiten desplegar aplicaciones de forma rápida, ligera y portable. A diferencia de las máquinas virtuales tradicionales, los contenedores comparten el sistema operativo anfitrión, reduciendo el consumo de recursos y facilitando la administración.

Docker Compose permite gestionar múltiples servicios desde un único archivo de configuración, simplificando la implementación y comunicación entre componentes.

Respecto al modelo de nube, se utilizó AWS EC2 debido a su disponibilidad inmediata, acceso remoto y facilidad para desplegar entornos de laboratorio y producción.

Arquitectura de la Solución

La solución implementada se compone de tres servicios:

NGINX

Encargado de recibir las solicitudes HTTP y redirigirlas hacia la aplicación Flask.

Aplicación Flask

Aplicación desarrollada en Python encargada de procesar las solicitudes y registrar visitas.

PostgreSQL

Base de datos relacional utilizada para almacenar la información generada por la aplicación.

Flujo de funcionamiento
Usuario
   │
   ▼
NGINX
   │
   ▼
Aplicación Flask
   │
   ▼
PostgreSQL
Tecnologías Utilizadas
AWS EC2
Amazon Linux 2023
Docker
Docker Compose
Python Flask
PostgreSQL 16
NGINX Latest
Git
GitHub
Estructura del Proyecto
examen_virtualizacion/
│
├── app/
│   ├── app.py
│   └── requirements.txt
│
├── nginx/
│   └── default.conf
│
├── evidencias/
│
├── Dockerfile
│
├── docker-compose.yml
│
└── README.md
Evidencias
Evidencia 1 – Creación de la instancia EC2

Se creó una instancia EC2 sobre AWS Learner Lab que actuó como infraestructura base para desplegar la solución.

![Creación EC2](evidencias/01_creacion_instancia_ec2.png)
Evidencia 2 – Instalación de Docker

Se instaló Docker Engine en Amazon Linux 2023 para gestionar la ejecución de contenedores.

![Instalación Docker](evidencias/02_instalacion_docker.png)
Evidencia 3 – Verificación del servicio Docker

Se verificó que Docker se encontrara activo y operativo.

![Servicio Docker](evidencias/03_servicio_docker_activo.png)
Evidencia 4 – Instalación de Docker Compose

Se instaló Docker Compose para administrar múltiples servicios desde un único archivo YAML.

![Docker Compose](evidencias/04_instalacion_docker_compose.png)
Evidencia 5 – Creación del proyecto

Se creó el directorio principal del proyecto y la estructura de trabajo.

![Proyecto](evidencias/05_creacion_directorio_proyecto.png)
Evidencia 6 – Configuración Git

Se inicializó Git y se configuró la identidad del repositorio.

![Git Configurado](evidencias/06_configuracion_git.png)
Evidencia 7 – Asociación con GitHub

Se configuró el repositorio remoto para publicar la solución.

![GitHub](evidencias/07_repositorio_remoto_github.png)
Evidencia 8 – Despliegue mediante Docker Compose

Se ejecutó Docker Compose para crear la red, descargar imágenes y levantar los servicios.

![Docker Compose Up](evidencias/08_docker_compose_up.png)
Evidencia 9 – Contenedores activos

Se comprobó el funcionamiento simultáneo de los servicios:

PostgreSQL
Flask
NGINX
![Contenedores Activos](evidencias/09_contenedores_activos.png)
Evidencia 10 – Imágenes Docker utilizadas

Se verificaron las imágenes descargadas y utilizadas por la solución.

![Docker Images](evidencias/10_imagenes_docker.png)
Evidencia 11 – Creación del volumen persistente

Se comprobó la existencia del volumen encargado de almacenar los datos de PostgreSQL.

![Volumen PostgreSQL](evidencias/11_volumen_postgres.png)
Evidencia 12 – Inspección del volumen

Se verificó la configuración interna y el punto de montaje del volumen persistente.

![Volume Inspect](evidencias/12_volume_inspect.png)
Evidencia 13 – Docker Inspect

Se revisó la configuración interna del contenedor de la aplicación Flask.

![Docker Inspect](evidencias/13_docker_inspect_app.png)
Evidencia 14 – Aplicación funcionando localmente

Se validó el correcto funcionamiento de la aplicación mediante el comando curl desde la instancia EC2.

![Aplicación Local](evidencias/14_aplicacion_local.png)
Evidencia 15 – Aplicación accesible desde navegador

La aplicación quedó publicada mediante NGINX y accesible desde Internet utilizando la IP pública de la instancia.

![Aplicación Web](evidencias/15_aplicacion_web.png)
Evidencia 16 – Página publicada mediante NGINX

Se verificó el acceso web desde un navegador externo.

![NGINX](evidencias/16_nginx_publicado.png)
Evidencia 17 – Reinicio de contenedores

Se reiniciaron los servicios utilizando Docker Compose para comprobar su recuperación automática.

![Reinicio](evidencias/17_reinicio_contenedores.png)
Evidencia 18 – Persistencia de datos

Se comprobó que el contador continuó incrementándose después del reinicio, validando el uso correcto del volumen persistente asociado a PostgreSQL.

![Persistencia](evidencias/18_persistencia_datos.png)
Repositorio GitHub

Repositorio utilizado para almacenar el código fuente y la documentación del proyecto:

https://github.com/karocp82/examen_virtualizacion_carolina_paez
Resultados Obtenidos

Durante la implementación se logró:

Desplegar una arquitectura multicontenedor.
Configurar comunicación entre servicios.
Implementar persistencia mediante volúmenes Docker.
Publicar la aplicación en AWS.
Gestionar el proyecto mediante Git y GitHub.
Validar el acceso web externo.
Comprobar la recuperación automática de servicios.
Verificar la persistencia de datos después de reinicios.
Conclusión

Durante esta evaluación implementé una solución basada en contenedores Docker sobre una instancia EC2 de AWS. La arquitectura considera NGINX como servidor web, una aplicación Flask desarrollada en Python y una base de datos PostgreSQL con almacenamiento persistente.

Las pruebas realizadas permitieron validar el correcto funcionamiento de cada componente, la comunicación entre servicios, la persistencia de la información mediante volúmenes Docker y la publicación de la aplicación en Internet.

Esta implementación demuestra las ventajas de la virtualización basada en contenedores, permitiendo desplegar aplicaciones de manera eficiente, portable y escalable utilizando tecnologías ampliamente utilizadas en entornos reales de infraestructura y plataformas tecnológicas.
