# Pasos para la creación de un proyecto en Python con DJango:

## 1. Creamos un nuevo entorno virtual y lo iniciamos:
```bash
python3 -m venv myvenv
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
## Ejecutamos la migración:
```bash
python manage.py migrate
```
## E iniciamos el servidor:
```bash
python manage.py runserver
```
