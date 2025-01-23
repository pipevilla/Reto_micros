# Reto_micros
Repo para resolver el reto de Ing de Plataformas

Microservicios con FastAPI y EKS en AWS

Este proyecto implementa una arquitectura basada en microservicios utilizando la libreria FastAPI, con dos servicios independientes que se comunican entre si. Estos servicios se despliegan tanto localmente usando Docker, como en un clúster EKS en AWS, utilizando Infraestructura como Código (IaC) con AWS CloudFormation.

Explicación de Funcionalidades Básicas:

Servicio 1:

Genera un token JWT con información de prueba y una expiración de 5 minutos.
Envía el token al Servicio B para validarlo.
Devuelve el resultado de la validación junto con el token generado.

Servicio 2: 

Recibe un token JWT desde el Servicio 1.
Valida el token utilizando la clave secreta.
Retorna un mensaje de confirmación si el token es válido o un mensaje de error en caso contrario.

Pre-requisitos:

En ambiente Local:

-Python 3.10 o superior.
-Docker y Docker Compose.
-Herramientas de prueba como Postman o cURL.
-Conexión a Internet (opcional)

En AWS:

-Cuenta activa de AWS.
-AWS CLI configurado con un perfil con permisos suficientes.
-Kubernetes CLI (kubectl) configurado.

Explicación de la Infraestructura como Código (IaC):

El despliegue utiliza AWS CloudFormation para crear un clúster EKS, configurar VPC con subredes públicas y privadas, implementar un grupo de nodos administrados y finalmente asignar permisos y roles necesarios para el clúster y sus nodos.

Estructura del Proyecto

//Local
|-- service_1/                # Código y Dockerfile del Servicio 1
|   |-- main.py               # Código principal del Servicio 1
|   |-- Dockerfile            # Dockerfile para construir la imagen del Servicio 1
|   |-- requirements.txt      # Archivo con requisitos de librerias necesarias para el Servicio 1
|
|-- service_2/                # Código y Dockerfile del Servicio 2
|   |-- main.py               # Código principal del Servicio 2
|   |-- Dockerfile            # Dockerfile para construir la imagen del Servicio 2
|   |-- requirements.txt      # Archivo con requisitos de librerias necesarias para el Servicio 2
|
|-- docker-compose.yml        # Configuración para entorno local Docker
|

//AWS
|-- iac/                            # Código YAML en CloudFormation para despliegue de la IaC
|   |-- EKS.yaml                    # Código principal para el despliegue de toda la IaC del proyecto
|-- service_1/                      # Código y Dockerfile del Servicio 1
|   |-- main.py                     # Código principal del Servicio 1
|   |-- service-1-deployement.yaml  # Archivo con el deployement EKS para el Servicio 1
|   |-- service-1-service.yaml      # Archivo con servicio (EKS) para el Servicio 1
|   |-- Dockerfile                  # Dockerfile para construir la imagen del Servicio 1
|   |-- requirements.txt            # Archivo con requisitos de librerias necesarias para el Servicio 1
|
|-- service_2/                      # Código y Dockerfile del Servicio 2
|   |-- main.py                     # Código principal del Servicio 2
|   |-- service-2-deployement.yaml  # Archivo con el deployement EKS para el Servicio 2
|   |-- service-2-service.yaml      # Archivo con servicio (EKS) para el Servicio 2
|   |-- Dockerfile                  # Dockerfile para construir la imagen del Servicio 2
|   |-- requirements.txt            # Archivo con requisitos de librerias necesarias para el Servicio 2
|


Pasos para Ponerlo en a correr la solución:

Ambiente local:

1) Clonar el repo:

    git clone <https://github.com/pipevilla/Reto_micros>
    cd <Reto_micros>

2) Instalar Docker y Docker Compose

3) Sube los servicios con Docker Compose:

    docker-compose up --build

4) Probar los servicios 1 y 2:

Servicio 1: http://localhost:8000/generate-token/

Servicio 2: http://localhost:8001/validate-token

5) Instala Postman o cURL para lanzar las solicitudes POST y poder probar funcionalidad

---------

En ambiente AWS usando EKS:

1) Configura las credenciales de AWS CLI en tu máquina local:

    aws configure (y sigue los pasos)

2) Crear la Infraestructura con CloudFormation, usando el archivo yaml en el repo y usando la CLI, con este comando:

    aws cloudformation create-stack --stack-name eks-microservices-stack --template-body https://raw.githubusercontent.com/pipevilla/Reto_micros/refs/heads/main/AWS/iac/EKS.yaml --capabilities CAPABILITY_NAMED_IAM

3) Configurar linea de comandos K8s con kubectl

Actualiza el contexto de kubectl:

    aws eks update-kubeconfig --region <region> --name <eks-cluster-name>

4) Verifica el estado del clúster:

    kubectl get nodes

5) Desplegar los Servicios en el Clúster

Usa los archivos YAML en el repo para los despliegues y servicios de Kubernetes.

6) Aplica los manifiestos:

    kubectl apply -f service-a-deployment.yml
    kubectl apply -f service-b-deployment.yml

7) Verifica los pods y servicios:

    kubectl get pods
    kubectl get svc

8) Probar los Servicios

Obtén la dirección IP del servicio A:

    kubectl get svc service-a

9) Prueba los endpoints usando Postman o cURL.


-----------

Notas Adicionales:

-Para reducir costos en AWS usa instancias tipo t3.small.
-Configura MinSize: 1 y MaxSize: 1 en los workernodes para bajar costos innecesarios.

by JFVO