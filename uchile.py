# uchile.py
from resultados import Resultados
from scrape import Scraper
from stats import Estadisticas

def main():
    # URL de la página web de la Universidad de Chile con los resultados
    url_uchile_resultados = "https://uchile.cl/presentacion/informacion-publica/estados-financieros-balances-resultados-y-flujo-de-efectivo"

    # Crear una instancia del scraper y extraer datos
    scraper = Scraper(url_uchile_resultados)
    resultados = scraper.extraer_datos()

    # Almacenar resultados en una instancia de Resultados
    almacen_resultados = Resultados()
    for resultado in resultados:
        almacen_resultados.agregar_resultado(resultado)

    # Calcular estadísticas
    estadisticas = Estadisticas()
    promedio = estadisticas.calcular_promedio(resultados)

    # Imprimir estadísticas
    print("Resultados de la Universidad de Chile:")
    print("Promedio:", promedio)

if __name__ == "__main__":
    main()
