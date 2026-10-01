class CuentaBancaria:
    def __init__(self, numero_cuenta: str, titular: str, saldo_inicial: float = 0.0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.__saldo = float(saldo_inicial)
# Hotfix: Validación urgente para asegurar que el monto sea siempre positivo
    def depositar(self, monto: float):
        # Corrección de seguridad/hotfix incluida: validar que monto > 0
        if monto > 0:
            self.__saldo += monto
        else:
            raise ValueError("El monto a depositar debe ser mayor a cero.")

    def retirar(self, monto: float):
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a cero.")
        if monto > self.__saldo:
            raise ValueError("Saldo insuficiente para realizar el retiro.")
        self.__saldo -= monto

    def consultar_saldo(self) -> float:
        return self.__saldo

    def __str__(self) -> str:
        return f"Cuenta: {self.numero_cuenta} | Titular: {self.titular} | Saldo: S/ {self.__saldo:.2f}"


class CuentaAhorros(CuentaBancaria):
    def __init__(self, numero_cuenta: str, titular: str, saldo_inicial: float, tasa_interes: float):
        super().__init__(numero_cuenta, titular, saldo_inicial)
        self.tasa_interes = tasa_interes  # Porcentaje anual, ej: 4.5

    def calcular_interes(self) -> float:
        """Calcula el interés anual: saldo * tasa / 100"""
        return self.consultar_saldo() * (self.tasa_interes / 100.0)

    def __str__(self) -> str:
        base_str = super().__str__()
        interes = self.calcular_interes()
        return f"{base_str} | Tasa Interés: {self.tasa_interes}% | Interés Anual: S/ {interes:.2f}"


class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero_cuenta: str, titular: str, saldo_inicial: float, limite_sobregiro: float):
        super().__init__(numero_cuenta, titular, saldo_inicial)
        self.limite_sobregiro = limite_sobregiro

    def retirar(self, monto: float):
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a cero.")
        saldo_disponible = self.consultar_saldo() + self.limite_sobregiro
        if monto > saldo_disponible:
            raise ValueError(f"Excede el límite de sobregiro permitido (Máx accesible: S/ {saldo_disponible:.2f}).")
        # Invocamos el retiro accediendo directamente al saldo privado vía depósito/retiro
        saldo_actual = self.consultar_saldo()
        nuevo_saldo = saldo_actual - monto
        # Ajustamos el saldo usando los métodos de la clase base
        if monto <= saldo_actual:
            super().retirar(monto)
        else:
            # Caso con sobregiro
            super().retirar(saldo_actual) if saldo_actual > 0 else None
            monto_restante = monto - (saldo_actual if saldo_actual > 0 else 0)
            self._CuentaBancaria__saldo -= monto_restante

    def permite_sobregiro(self) -> bool:
        return self.consultar_saldo() < 0

    def __str__(self) -> str:
        base_str = super().__str__()
        estado_sg = "Sí" if self.permite_sobregiro() else "No"
        return f"{base_str} | Límite Sobregiro: S/ {self.limite_sobregiro:.2f} | Sobregirado: {estado_sg}"


# Pruebas fuera de las clases
if __name__ == "__main__":
    print("--- PRUEBAS CUENTA AHORROS ---")
    ahorros = CuentaAhorros("AH-001", "Benjamin Salas", 1000.0, 4.5)
    print(ahorros)
    ahorros.depositar(500.0)
    print("Después de depositar S/ 500:")
    print(ahorros)

    print("\n--- PRUEBAS CUENTA CORRIENTE ---")
    corriente = CuentaCorriente("CC-002", "Benjamin Salas", 200.0, 500.0)
    print(corriente)
    print("Realizando retiro con sobregiro de S/ 400...")
    corriente.retirar(400.0)
    print(corriente)