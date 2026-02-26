class MotorTarifas:
    def __init__(self):
        self.rutas = {
            "marbella": {"distancia": 10, "tarifa": 15000},
            "torices": {"distancia": 15, "tarifa": 25000},
            "bicentenario": {"distancia": 30, "tarifa": 70000},
            "centro": {"distancia":3, "tarifa": 10000}
        }

    def calcular_tarifa(self, direccion):
        direccion = direccion.lower()

        if direccion in self.rutas:
            datos = self.rutas[direccion]
            print("\nRuta encontrada")
            print("Dirección:", direccion.capitalize())
            print("Distancia:", datos["distancia"], "km")
            print("Tarifa:", datos["tarifa"], "pesos")
        else:
            print("\nLa dirección ingresada no está disponible.")
motor = MotorTarifas()

direccion_usuario = input("Ingrese la dirección de entrega: ")

motor.calcular_tarifa(direccion_usuario)