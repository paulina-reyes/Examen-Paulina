
class CalculadoraAreas:

    def _leer_datos(self, figura):

        if figura == 'círculo':
            radio = float(input(f"Introduce la base del {figura}: "))
            return radio

        base = float(input(f"Introduce la base del {figura}: "))
        altura = float(input(f"Introduce la altura del {figura}: "))

        return base, altura
    
    
    def _mostrar_resultado(self, figura, area):
      
        print(f"El área del {figura} es: {area}")

    def calcular_area_rectangulo(self):

        base, altura = self._leer_datos("rectángulo")
        
        area = base * altura
        self._mostrar_resultado("rectángulo", area)

    def calcular_area_triangulo(self):

        base, altura = self._leer_datos("triángulo")

        area = (base * altura) / 2
        self._mostrar_resultado("triángulo", area)

    def calcular_area_circulo(self):
        import numpy as np

        radio = self._leer_datos("círculo")
        
        area = radio**2 * np.pi
        self._mostrar_resultado("círculo", area)