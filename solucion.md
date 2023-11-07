# Pasos para la creación de un proyecto en Python con DJango:

## 1. Creamos un nuevo entorno virtual y lo iniciamos:
```bash
python3 -m venv myvenv2
myvenv2\Scripts\activate
```
## 2. Creamos el .gitignore para que no nos suba el entorno virtual al repositorio
## 3. Actualizamos pip dentro del entorno virtual:
```bash
pip install --upgrade pip
```
## 4. Creamos un fichero de requisitos (requirements.txt) con los paquetes a instalar. Por el momento tan solo DJango en su última versión y creamos el proyecto.
```bash
pip install -r requirements.txt
django-admin.exe startproject task .
```
## 5. Cambiamos los settings:
```bash
TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'es-es'
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
## 6. Ejecutamos la migración:
```bash
python manage.py migrate
```
## 7. Iniciamos el servidor (con el siguiente comando) y en el navegador escribimos la dirección http://127.0.0.1:8000/
```bash
python manage.py runserver
```
## 8. Creamos una aplicación separada dentro de nuestro proyecto:
```bash
python manage.py startapp todolist
```
## 9. Le decimos a DJango que utilice la aplicación creada. En settings tiene que quedar:
```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todolist',
]
```
## 10. En el archivo todolist/models.py definimos todos los objetos, es el lugar en el cual definiremos nuestra entrada del To Do List.
## 11. Agregamos nuestro modelo a la bbdd:
```bash
 python manage.py makemigrations todolist
 python manage.py migrate todolist
```
## 12. Creamos un admin modificando el fichero todolist/admin.py y ejecutando el comando:
```bash
python manage.py createsuperuser
```
## 13. En task, en la carpeta urls.py añadimos la path:
```bash
path('', include('todolist.urls')),
```
## 14. Y en todolist creamos un fichero urls.py que contenga:
```bash
from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
]
```
## 15. Ahora creamos las vistas. En la carpeta todolist, en el fichero views.py agregamos las siguientes líneas:
```bash
from django.shortcuts import render
from .models import Task 

def task_list(request):
    task = Task.objects.all()
    return render(request, 'todolist/task_list.html', {'task': task})
```
## 16. Vamos a crear ahora nuestra primera plantilla. Creamos una carpeta templates dentro de todolist, y otra carpeta todolist en la carpeta templates. Creamos un fichero task_list.html en esta última carpeta todolist.
## 17. En el html añadimos:
```bash
<html>
        <head>
            <title>Task List</title>
        </head>
        <body>
            <h1>Lista de Tareas</h1>
            <ul>
                {% for task in tasks %}
                <li>
                    <h2>{{ task.title }}</h2>
                    <p>{{ task.description }} - {% if task.completed %} Sí {% else %} No {% endif %}</p>
                </li>
                {% empty %}
                <p>No hay tareas por hacer.</p>
                {% endfor %}
            </ul>
        </body>
    </html>
```
## 18. Ya podemos añadir nuestras tareas!! :)
