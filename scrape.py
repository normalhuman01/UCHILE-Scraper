# scrape.py
import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url):
        self.url = url

    def extraer_datos(self):
        # Realizar el scraping y extraer los datos de la página web
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Aquí debes implementar el código específico para extraer los datos de la Universidad de Chile
            # Utiliza BeautifulSoup u otras herramientas de scraping.
            # Por ejemplo, si los resultados están en tablas, puedes buscar y procesar las tablas.
            # Luego, crea objetos de resultado y devuelve una lista de resultados.
            resultados = []  # reemplaza con los resultados reales
            return resultados
        else:
            print(f"No se pudo acceder a la URL: {self.url}")
            return []

