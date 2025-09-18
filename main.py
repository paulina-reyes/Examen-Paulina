from clases.areas import CalculadoraAreas

def ejecutar_pruebas():

    calculadora = CalculadoraAreas()

    calculadora.calcular_area_rectangulo()
    calculadora.calcular_area_triangulo()
    calculadora.calcular_area_circulo()
    
if __name__ == "__main__":
    ejecutar_pruebas()
    