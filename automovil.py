class Automovil:
    def __init__(self, marca: str, modelo: str, velocidad_max: float, nivel_combustible: float, año_fabricacion: int):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_max = velocidad_max
        self.nivel_combustible = nivel_combustible
        self.año_fabricacion = año_fabricacion

    # Getter y Setter para año_fabricacion
    @property
    def año_fabricacion(self) -> int:
        return self._año_fabricacion

    @año_fabricacion.setter
    def año_fabricacion(self, valor: int):
        if 1886 <= valor <= 2026:
            self._año_fabricacion = valor
        else:
            raise ValueError(f"El año de fabricación debe estar entre 1886 y 2026. Valor ingresado: {valor}")

    # Getter y Setter para nivel_combustible
    @property
    def nivel_combustible(self) -> float:
        return self._nivel_combustible

    @nivel_combustible.setter
    def nivel_combustible(self, valor: float):
        if 0.0 <= valor <= 100.0:
            self._nivel_combustible = float(valor)
        else:
            raise ValueError(f"El nivel de combustible debe estar entre 0.0 y 100.0. Valor ingresado: {valor}")

    # Getter y Setter para velocidad_max
    @property
    def velocidad_max(self) -> float:
        return self._velocidad_max

    @velocidad_max.setter
    def velocidad_max(self, valor: float):
        if valor > 0:
            self._velocidad_max = float(valor)
        else:
            raise ValueError(f"La velocidad máxima debe ser mayor a 0. Valor ingresado: {valor}")

    # Método tiempo_llegada
    def tiempo_llegada(self, distancia_km: float) -> float:
        """Calcula el tiempo de llegada en horas: distancia / velocidad_max"""
        return distancia_km / self.velocidad_max

    def __str__(self) -> str:
        return (f"Automóvil: {self.marca} {self.modelo} ({self.año_fabricacion}) | "
                f"Velocidad Máx: {self.velocidad_max} km/h | Combustible: {self.nivel_combustible}%")


# Pruebas fuera de la clase
if __name__ == "__main__":
    # Instancia de un automóvil
    auto1 = Automovil(
        marca="Toyota",
        modelo="Corolla",
        velocidad_max=180.0,
        nivel_combustible=75.5,
        año_fabricacion=2022
    )

    print("--- Datos del Automóvil ---")
    print(auto1)

    # Uso del método tiempo_llegada
    distancia = 360.0  # en km
    tiempo = auto1.tiempo_llegada(distancia)
    print(f"Tiempo estimado para recorrer {distancia} km: {tiempo:.2f} horas")

    print("\n--- Demostración de Validación de Propiedades ---")
    # Prueba de asignación incorrecta dentro de un try/except
    try:
        print("Intentando asignar año de fabricación invalido (1800)...")
        auto1.año_fabricacion = 1800
    except ValueError as e:
        print(f"Error capturado correctamente: {e}")