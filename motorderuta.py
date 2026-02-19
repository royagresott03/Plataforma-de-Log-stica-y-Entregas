def motor_rutas(destino_usuario, *rutas):
    for nombre, distancia, precio in rutas:
        if destino_usuario.lower() == nombre.lower():
            print("\nRuta encontrada")
            print("Destino:", nombre)
            print("Distancia:", distancia, "km")
            print("Tarifa del envío:", precio, "pesos")
            return
    
    print("\nLo sentimos, la dirección no está disponible.")

ruta1 = ("marbella", 10, 15000)
ruta2 = ("torices", 15, 25000)
ruta3 = ("bicentenario", 30, 70000)

destino = input("Ingrese la dirección de destino: ")

motor_rutas(destino, ruta1, ruta2, ruta3)
