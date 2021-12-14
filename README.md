# Ejercicio 2

Para el ejercicio 2, se construyo un API utilizando Flask (Python) y Sqlite, se
dejaron disponibles los siguientes endpoints.
  
| Método | Endpoint | Funcion |
| -------|-------------------------------------|---------------------------------------|
| GET    | api/v1.0/usuarios/                    | lista los usuarios                      |
| GET    | api/v1.0/usuarios/{correo@domain.tld} | revisa los datos de un usuario          |
| POST   | api/v1.0/usuarios/                    | agrega un usuario (email, nombre, clave)|
| DELETE | api/v1.0/usuarios/{correo@domain.tld} | elimina un usuario                      |
| PUT    | api/v1.0/usuarios/{correo@domain.tld} | modifica un usuario                     |

## Descarga e instalación del proyecto

Para descargar el proyecto puedes clonar el repositorio:

```console
  $ git clone https://bitbucket.org/devops-grupo6/ejercicio2.git
```

### Con Docker

Construimos la imagen ejecutando:

```console
$ docker build -t ejercicio2-modulo2 .
```

Luego corremos la imagen ejecutando:
    
```console
docker run -it --name ejercicio2-modulo2 --env="APP_SETTINGS=app.config.Production" -d -p 5000:5000 ejercicio2-modulo2
```

### Con Python

Ejecutando en el entorno local, creamos un entorno de trabajo e instalamos las dependencias.

```console
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

#### Linux/Mac

    export APP_SETTINGS=app.config.Production

#### Windows

    set "APP_SETTINGS=app.config.Production"

### Ejecución con el servidor que trae Flask

Se puede iniciar el servicio del proyecto ejecutando, esto se ejecutaria en modo de pruebas.

```console
flask db init
flask db migrate
flask db upgrade
flask run
```

## Para interactuar con el API

### Agregar

Para agregar un usuario.

```console
curl -X POST -H "Content-Type: application/json" -d '{
    "nombre": "Nombre Apellido",
    "email": "correo@domain.tld",
    "clave": "111aA_"
}' http://localhost:5000/api/v1.0/usuarios
```

Adicionalmente se puede ocupar el script_test/creacion.sh para crear usuarios aleatoriamente.

### Autentificación

Para acceder a los endpoints, es necesario que se autentifique con enmail y clave

```console
curl -X POST -H "Content-Type: application/json" -d '{
    "email": "correo@domain.tld",
    "clave": "111aA_"
}' http://localhost:5000/api/v1.0/usuarios/auth/
```

La respuesta es un token, que se utilizara posteriormente

```console
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
}
```

### Listar

Para listar todos los usuarios disponibles, necesita autentificación.

```console
curl -H "Authorization: Bearer $TOKEN" http://localhost:5000/api/v1.0/usuarios
```

### Mostrar

Para mostrar los datos de un usuario, necesita autentificación.

```console
curl -H "Authorization: Bearer $TOKEN" http://localhost:5000/api/v1.0/usuarios/${correo}
```

### Eliminar

Para eliminar los datos de mi usuario, necesita autentificación.

```console
$ curl -X DELETE -H "Authorization: Bearer $TOKEN" http://localhost:5000/api/v1.0/usuarios/${correo}
```

### Modificar

Para modificar los datos de mi propio usuario, necesita autentificación.

```console
curl -X PUT -H "Content-Type: application/json" -d '{
    "nombre": "Nombre2 Apellido2",
    "clave": "111aA_2"
}' -H "Authorization: Bearer $TOKEN" http://localhost:5000/api/v1.0/usuarios/${correo}
```

# Integrantes Grupo 6
* Gonzalo Muñoz Boisier
* Flamel Jesod Canto Sanchez
* David Antonio Figueroa Mejias
* Eduardo Andres Cabrera Flores
* Alejandro Ignacio Carrasco Navarrete
