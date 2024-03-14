import requests
from bs4 import BeautifulSoup #para que funcione tienes que descargarte la libre beautifulSoup

def scrape_all_web():
    # URL de la página web a raspar, con el esquema HTTP

    url = "https://www.youtube.com/"

    # Realizar la petición HTTP a la página web
    response = requests.get(url)

    # Crear una instancia de BeautifulSoup con el contenido de la respuesta
    soup = BeautifulSoup(response.content, 'html.parser')

    # Mostrar la "sopa" completa (todo el contenido HTML)
    print("Contenido HTML completo:\n", soup.prettify())

    # Extraer y mostrar el título de la página web
    page_title = soup.title.string if soup.title else "Título no encontrado"
    print("\nTítulo de la página web:", page_title)

scrape_all_web()
