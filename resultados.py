class Resultados:
    def __init__(self):
        self.resultados = []

    def agregar_resultado(self, resultado):
        self.resultados.append(resultado)

    def obtener_resultados(self):
        return self.resultados
