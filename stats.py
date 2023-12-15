import math


class Estadisticas:
    def calcular_promedio(self, resultados):

        try:
            if not resultados:
                raise ValueError("La lista de resultados está vacía.")
            
            total = sum(resultados)
            promedio = total / len(resultados)
            return promedio
        except ZeroDivisionError:
            print("La lista de resultados no puede estar vacía.")
            return 0
        except Exception as e:
            print(f"Ocurrió un error: {str(e)}")
            return 0

    def calcular_desviacion_estandar(self, resultados):

        try:
            if not resultados:
                raise ValueError("La lista de resultados está vacía.")
            
            promedio = self.calcular_promedio(resultados)
            suma_de_cuadrados = sum((x - promedio) ** 2 for x in resultados)
            desviacion_estandar = math.sqrt(suma_de_cuadrados / len(resultados))
            return desviacion_estandar
        except ZeroDivisionError:
            print("La lista de resultados no puede estar vacía.")
            return 0
        except Exception as e:
            print(f"Ocurrió un error: {str(e)}")
            return 0
