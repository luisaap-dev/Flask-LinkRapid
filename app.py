from flask import Flask
from controllers.controllers import ControladorURL

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Crea una instancia del ControladorURL para gestionar las URLs
controlador_url = ControladorURL()

# Define una ruta para la página de inicio que acepta métodos GET y POST
@app.route('/', methods=['GET', 'POST'])
def inicio():
    # Llama al método 'inicio' del controlador_url para manejar la solicitud
    return controlador_url.inicio()

# Define una ruta para redireccionar a una URL larga a partir de la URL corta proporcionada
@app.route('/<url_corta>', methods=['GET'])
def redirigir(url_corta):
    # Llama al método 'redirigir' del controlador_url para manejar la redirección
    return controlador_url.redirigir(url_corta)


@app.errorhandler(404)
def pagina_no_encontrada(error):
    return controlador_url.pagina_no_encontrada(error)

# Ejecuta la aplicación si el archivo se ejecuta directamente
if __name__ == '__main__':
    # Crea la tabla en la base de datos usando el método 'crear_tabla'
    controlador_url.acortador_url.crear_tabla()
    
    # Inicia la aplicación en modo de depuración
    app.run(debug=True)
