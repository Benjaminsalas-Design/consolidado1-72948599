import math

class Planeta:
    def __init__(self, nombre: str, masa: float, radio: float, distancia_al_sol: float, tiene_vida: bool = False):
        self.nombre = nombre
        self.masa = masa
        self.radio = radio
        self.distancia_al_sol = distancia_al_sol
        self.tiene_vida = tiene_vida

    def calcular_densidad(self) -> float:
        """Calcula la densidad media en kg/m³: masa / (4/3 * pi * radio³)"""
        volumen = (4 / 3) * math.pi * (self.radio ** 3)
        return self.masa / volumen

    def es_planeta_exterior(self) -> bool:
        """Retorna True si la distancia al Sol es mayor a 5.2 UA"""
        return self.distancia_al_sol > 5.2

    def __str__(self) -> str:
        tipo = "Exterior" if self.es_planeta_exterior() else "Interior"
        densidad = self.calcular_densidad()
        return f"Planeta: {self.nombre} | Tipo: {tipo} | Densidad: {densidad:.2f} kg/m³ | Vida: {self.tiene_vida}"


# Pruebas fuera de la clase
if __name__ == "__main__":
    # Instancia 1: Tierra (Planeta Interior)
    tierra = Planeta(
        nombre="Tierra",
        masa=5.972e24,          # en kg
        radio=6371000.0,         # en metros
        distancia_al_sol=1.0,    # en UA
        tiene_vida=True
    )

    # Instancia 2: Júpiter (Planeta Exterior)
    jupiter = Planeta(
        nombre="Júpiter",
        masa=1.898e27,          # en kg
        radio=69911000.0,        # en metros
        distancia_al_sol=5.2,    # en UA
        tiene_vida=False
    )

    print(tierra)
    print(jupiter)