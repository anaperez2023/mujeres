import streamlit as st

class MultiApp:
    """
    Clase para crear múltiples aplicaciones dentro de una sola aplicación de Streamlit.
    """
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """
        Agrega una aplicación al objeto MultiApp.

        Parámetros:
        -----------
        title : str
            Título de la aplicación.
        func : función
            Función que contiene el código de la aplicación.
        """
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        """
        Ejecuta la aplicación seleccionada por el usuario.
        """
        app = st.sidebar.selectbox(
            'Selecciona una sección:',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()
        
