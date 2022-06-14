# Backend Django
1. python -m venv venv_nombreDelEntorno
2. Activar el entorno
3. pip install django || pip install django==3.2.12
4. cd Backend
5. django-admin startproject app_nombre_del_proyecto .
6. git init
7. .gitignore
**Manejar carpetas en minuscula con snake case menos CSS y JS, para las carpeta que tengan archivos .py agregar el init, evitar el uso de tildes o ñ en el cod, si son datos de tipo string que va a ver el usuario final, manejar buena ortografía, redacción y ser lo más explícito posible (Dar por sentado que el usuario final es un niño de 3 años que apenas y si sabe leer) y en lo posible manejar todo en ingles. (Para uso práctico en esta explicación se coloca todo en español o almenos lo que no me de flojera cambiar)**
8. Crear carpeta apps a la altura del manage.py
9. Crear carpeta settings dentro de app_nombre_del_proyecto
10. Crear los archivos base.py, local.py, produccion.py, pruebas.py etc dependiendo de los entornos que vaya a tener el proyecto, ya que cada entorno puede manejar una DB diferente, en los entornos diferentes al de producción el debug va en True, etc. Puedes encontrar una configuración de ejemplo dentro de cada archivo
10. Crear el configuracion_global.json a la altura del manage.py
11. Para el manejo de imagenes usar Pillow || pip install Pillow
12. Para el manejo de rutas usar Unipath || pip install Unipath
13. Para el manejo de API Rest usar Restframework || pip install djangorestframework\
Corsheaders || pip install django-cors-headers
14. Instalar el "controlador" de la BD a usar || pip install psycopg2 => Postgresql Windows || pip install psycopg2-binary => Postgresql Linux
15. Crear carpeta public
16. Dentro de la carpeta public:
static, media, templates
17. Dentro de la carpeta static\
CSS, JS
18. Crear una app: dentro de la carpeta en la cual se quiere crear la aplicación:\
cd apps/autentificacion:\
django-admin startapp registro\
django-admin startapp login\
django-admin startapp no_recuerdo_mi_contraseña

cd apps/machine_learning/clasificacion:\
django-admin startapp support_vector_machine\
django-admin startapp decision_tree

cd apps/machine_learning/natural_language_processing:\
django-admin startapp nlp_bert\
django-admin startapp nlp_word2vec

cd apps/pagina/ecommerce:\
...

cd apps/landing_page:\
...

19. Crear las aplicaciones correspondientes dependiendo de los casos de uso y los modelos de cada aplicación correspondiente a las tablas del modelado de base de datos. Cuántas apps? a discreción del desarrollador, Qué modelos quedan dentro de cada app? a discreción del desarrollador.
20. Estructura de la carpeta apps:
* Ejm1:
    - aplicación1
    - aplicación2

* Ejm2:
    - contenedor_global1
        - aplicación1
        - aplicación2
    - contenedor_global2
        - aplicación3
        - aplicación4

* Ejm3:
    - contenedor_global1
        - sub_contenedor1
            - aplicación1
            - aplicación2
        - sub_contenedor2
            - aplicación3
    - contenedor_global2
        - sub_contenedor3
            - aplicación4
            - aplicación5
        - sub_contenedor4
            - aplicación6

**Nota**\
Cada aplicación tiene un archivo apps.py modificar este dependiendo de la ruta en la que se encuentre y colocar este mismo path en el base.py dentro de LOCAL_APPS:\
Ejm1:\
"apps.aplicación1"\
"apps.aplicación2"

Ejm2:\
"apps.contenedor_global1.aplicación1"\
"apps.contenedor_global1.aplicación2"\
"apps.contenedor_global2.aplicación3"\
"apps.contenedor_global2.aplicación4"

Ejm3:\
"apps.contenedor_global1.sub_contenedor1.aplicación1"\
"apps.contenedor_global1.sub_contenedor1.aplicación2"\
"apps.contenedor_global1.sub_contenedor2.aplicación3"\
"apps.contenedor_global2.sub_contenedor3.aplicación4"

**Nota**\
Dentro del public/templates:
Manejar la misma estructura de carpetas de las apps pq? para no tener 30mil html regadas en una sola carpeta\
Se puede crear un base.html que es de donde heredan todas, para más info ver el sistema de templates de django\
Tener una carpeta partials dentro de cada app que contenga por ejemplo los metatags, si va a tener un header y un footer, etc\
templates/autentificacion/login/login.html\
templates/autentificacion/registro/registro.html\
etc

21. Estrucura individual de cada aplicación:\
aplicación1\
migrations: Donde se registran los cambios que se aplican a la base de datos\
admin.py: Administrar de Django (Que esta full cargado para poder ser utilizado)\
apps.py: Archivo que hay que modificar dependiendo de donde se encuentre y contiene más información\
https://docs.djangoproject.com/en/4.0/ref/applications/
models.py: Django maneja modelos (tablas) basados en clases\
tests.py: Pruebas unitarias y de integración por parte del desarrollador\
views.py: Parte lógica de las vistas (Recomendación: Utilizar vistas basadas en clases, son más potentes, mejor optimizadas y más fáciles de documentar)\
**Añadir**\
Carpeta api\
routers.py\
serializers.py\
viewsets.py

En la carpeta principal de la app a la altura de los models.py\
functions.py: Acá se encuentra toda la parte de código propio de python\
managers.py: consultas avanzadas a la ORM de Django\
urls.py: urls únicas de la aplicación\
signals.py: señales? maybe, que hacer antes de guardar, despues de guardar, al guardar, eliminar, por ejemplo el usuario ingresa nombres y apellidos por aparte y en los requerimientos sale full_name, con un pre_save se puede auto generar este campo para que el usuario no tenga que ingresar lo que ya hizo

**Las únicas apps que tienen todo esto son las de autentificación pq me dio flojera cambiar el apps.py en cada una y ya con esas queda claro la estructura, besos**

22. Cada que se haga una implementación exitosa de una aplicación de terceros agregarla al requirements.txt\
Una buena forma de manejar esto es crear una carpeta que contenga los requerimientos por entorno y sistema operativo:\
z_requirements\local_windows_reqs.txt\
z_requirements\prod_linux_reqs.txt

**Nota**\
Para obtener los requirements: pip freeze

23. Revisar el manage.py
24. Revisar el app_nombre_del_proyecto/asgi.py
25. Revisar el app_nombre_del_proyecto/wsgi.py
26. Revisar el configuracion_global.json

27. Comandos útiles:
Realizar copia de la DB:\
python manage.py dumpdata > nombre_de_la_copia_de_seguridad.json\
Subir copia de la DB:\
python manage.py loaddata nombre_de_la_copia_de_seguridad.json\
Instalar requirements.txt: dentro de la carpeta z_requirements\
pip install -r local_windows_reqs.txt\
Migraciones a la db\
python manage.py makemigrations\
python manage.py migrate\
Crear superusuario\
python manage.py createsuperuser\
Correr servidor local\
python manage.py runserver\

28. Si algo no funciona llamar (Cuando digo llamar es que me escriba :3) al papi sabroso de Sebas\
+57 300 295 4040

---
Ahora el front... puede ser con React (el más demandado en el mercado), Angular (El segundo más demandado), Vue (Por los loles), Etc\
En la carpeta principal a la altura del backend (osea no estamos adentro)\
npx create-react-app frontend\
le hacemos rename a la carpeta Frontend (se ve feo en minus si Backend tiene mayus)\
cd Frontend\
npm start