# stats.py

class Estadisticas:
    def calcular_promedio(self, resultados):
        # Calcular el promedio de los resultados
        if resultados:
            total = sum(resultados)
            promedio = total / len(resultados)
            return promedio
        else:
            return 0
