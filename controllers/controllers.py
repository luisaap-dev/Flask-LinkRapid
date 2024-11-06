from flask import render_template, request, redirect, url_for
from models.models import AcortadorURL  # Importar la clase AcortadorURL desde el módulo models.models

class ControladorURL:
    def __init__(self):
        self.acortador_url = AcortadorURL()  # Inicializar la instancia de AcortadorURL

    def procesar_formulario(self, url_larga):
        if not url_larga.startswith(('http://', 'https://')):
            url_larga = 'http://' + url_larga

        # Acortar la URL larga y generar URLs cortas para redirección
        urls_cortas = self.acortador_url.acortar_url(url_larga)
        urls_cortas = [url_for('redirigir', url_corta=url_corta, _external=True) for url_corta in urls_cortas]

        return urls_cortas, url_larga

    def inicio(self):
        if request.method == 'POST':
            url_larga = request.form['url_larga']  # Obtener la URL larga del formulario
            urls_cortas, url_larga = self.procesar_formulario(url_larga)  # Procesar la URL y obtener URLs cortas
            return render_template('resultado.html', urls_cortas=urls_cortas, url_larga=url_larga)

        return render_template('index.html')  # Renderizar la plantilla index.html si no hay una solicitud POST

    def redirigir(self, url_corta):
        url_larga = self.acortador_url.obtener_url_larga(url_corta)  # Obtener la URL larga asociada a la URL corta
        
        if url_larga:
            self.acortador_url.borrar_url(url_corta)  # Borrar la URL corta después de redirigir
            return redirect(url_larga)  # Redirigir al usuario a la URL larga
        else:
            return self.pagina_no_encontrada(404)  # Mostrar página de error 404 si la URL corta no existe

    @staticmethod
    def pagina_no_encontrada(error):
        return render_template('404.html', error=error), 404  # Renderizar la página de error 404 con el código de estado 404
