# Aplicación de Acortamiento de URLs utilizando Flask

Esta es una aplicación simple de acortamiento de URLs implementada utilizando el framework web Flask en Python. La aplicación permite a los usuarios acortar URLs largas y redireccionar a las URLs originales a partir de las URLs cortas generadas. 

## Funcionalidades

- **Acortamiento de URLs**: Los usuarios pueden ingresar URLs largas en la página de inicio y generar URLs cortas correspondientes.

- **Redirección**: Cuando se accede a una URL corta generada, la aplicación redirige al usuario a la URL original correspondiente.

## Requisitos Previos

- Python (3.6 o superior)
- Flask (Instalable mediante `pip install flask`)

## Instalación y Ejecución

1. Clona este repositorio en tu máquina local:

```
git clone https://github.com/luisaap-dev/Flask-LinkRapid
```

2. Accede al directorio del repositorio:

```
cd Flask-LinkRapid
```

3. Crear entorno virtual (opcional pero recomendado)
- (windows)
```shell
python -m venv nombre_del_entorno
```
- (linux)
```shell
python3 -m venv nombre_del_entorno
```

4. Activar el entorno virtual (opcional pero recomendado):

- Windows (CMD):
```shell
nombre_del_entorno\Scripts\activate
```
- Windows (PowerShell):
```shell
.\nombre_del_entorno\Scripts\Activate
```
- Linux/Ubuntu:
```shell
source nombre_del_entorno/bin/activate
```

5. Instala las dependencias utilizando `pip`:

```shell
pip install -r requirements.txt
```

6. Ejecuta la aplicación:

```shell
python app.py
```

La aplicación se ejecutará en `http://127.0.0.1:5000/`. Puedes acceder a esta URL desde tu navegador web.

## Uso

1. Accede a la página de inicio en tu navegador.

2. Ingresa una URL larga en el campo proporcionado y haz clic en "Acortar".

3. Se generará una URL corta que puedes copiar y compartir.

4. Para redirigir a la URL original, simplemente accede a la URL corta generada.

## Estructura del Proyecto

- `app.py`: Archivo principal que contiene la configuración de la aplicación Flask y las rutas.

- `controllers/controllers.py`: Contiene la lógica de controladores para manejar las solicitudes y redirecciones.

- `templates/`: Carpeta que contiene las plantillas HTML utilizadas para la interfaz de usuario.

- `static/`: Carpeta para recursos estáticos como hojas de estilo CSS y archivos JavaScript.

- `database/acortador_urls.db`: Archivo de base de datos SQLite para almacenar las URLs y sus versiones acortadas.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas agregar nuevas características, resolver problemas o mejorar la aplicación, siéntete libre de crear un pull request.

## Autor

Esta aplicación fue desarrollada por [Luis Ares](https://github.com/luisaap-dev).

## Licencia

Este proyecto está bajo la Licencia [MIT](LICENSE). Puedes obtener más información en el archivo `LICENSE`.
