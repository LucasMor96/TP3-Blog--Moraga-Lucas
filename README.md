Blog en Django
Descripción

Este es un proyecto de blog desarrollado con Django. 
Permite a los usuarios registrarse, iniciar sesión y realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre publicaciones de blog. 
También incluye autenticación de usuarios y un middleware personalizado para registrar las solicitudes HTTP.

Funcionalidades

    Autenticación de usuarios:
        Registro de usuarios.
        Inicio y cierre de sesión.
        La creación, edición y eliminación de publicaciones requiere autenticación.

    CRUD de publicaciones:
        Crear nuevas publicaciones.
        Ver detalles de publicaciones.
        Editar y eliminar publicaciones propias.

    Middleware personalizado:
        Registro de URLs accedidas por los usuarios para monitoreo de actividad.

Requisitos

    Python 3
    Django 4
    SQLite3 (Base de datos predeterminada de Django)

Instalación

    Clonar el repositorio:

    bash

git clone https://github.com/tuusuario/blog-django.git
cd blog-django

Crear un entorno virtual y activarlo:

bash

python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate

Instalar las dependencias:

bash

pip install -r requirements.txt

Aplicar las migraciones de la base de datos:

bash

python manage.py migrate

Crear un superusuario (opcional, para acceder al admin):

bash

python manage.py createsuperuser

Ejecutar el servidor de desarrollo:

bash

    python manage.py runserver

Uso

    Página de Inicio:
        Accede a la página de inicio en http://localhost:8000/.
        Aquí se mostrarán las publicaciones recientes del blog.

    Registro e Inicio de Sesión:
        Para acceder a funciones como la creación, edición y eliminación de publicaciones, es necesario estar autenticado.
        Dirígete a http://localhost:8000/registro/ para registrar un nuevo usuario.
        Inicia sesión en http://localhost:8000/accounts/login/.

    Crear Publicación:
        Una vez autenticado, podrás crear una nueva publicación accediendo a http://localhost:8000/crear/.
        Completa el formulario con el título y contenido de la publicación, y haz clic en el botón de enviar para publicarla.

    Listar Publicaciones:
        Para ver una lista de todas las publicaciones, accede a http://localhost:8000/listar/.
        Desde aquí, puedes hacer clic en el título de cualquier publicación para ver más detalles.

    Ver Detalles de una Publicación:
        Haz clic en una publicación desde la lista para ver los detalles completos en http://localhost:8000/publicacion/<int:id>/.
        En esta vista, podrás ver el título, contenido, fecha de creación y el autor de la publicación.

    Editar Publicación:
        Si eres el autor de una publicación, verás un botón de "Editar" en la vista de detalles.
        Al hacer clic, podrás modificar el título y el contenido accediendo a http://localhost:8000/publicacion/editar/<int:id>/.

    Eliminar Publicación:
        En la misma vista de detalles, también podrás eliminar una publicación mediante el botón "Eliminar".
        Al hacer clic, serás redirigido a una página de confirmación de eliminación en http://localhost:8000/publicacion/eliminar/<int:id>/.

    Cierre de Sesión:
        Para cerrar sesión, haz clic en el botón de "Cerrar sesión" en el navbar o accede a http://localhost:8000/accounts/logout/.
        Se te mostrará un mensaje confirmando el cierre exitoso de sesión.

Estructura de URLs

    / - Página de inicio.
    /crear/ - Crear una nueva publicación.
    /listar/ - Listar todas las publicaciones.
    /publicacion/<int:id>/ - Ver detalles de una publicación.
    /publicacion/editar/<int:id>/ - Editar una publicación.
    /publicacion/eliminar/<int:id>/ - Eliminar una publicación.
    /accounts/login/ - Iniciar sesión.
    /accounts/logout/ - Cerrar sesión.
    /registro/ - Registrar un nuevo usuario.

Middleware

Se ha implementado un middleware personalizado para registrar las solicitudes HTTP que los usuarios realizan en la aplicación.
