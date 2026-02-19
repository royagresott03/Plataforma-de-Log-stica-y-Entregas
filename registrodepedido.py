def registrar_cliente():
    print("--- Registro de cliente ---")
    
    nombre = input("Ingrese su nombre: ")
    direccion = input("Ingrese su dirección: ")
    telefono = input("Ingrese su teléfono: ")
    referencia = input("Ingrese un dato de referencia: ")
    
    datos_cliente = {
        "Nombre": nombre,
        "Dirección": direccion,
        "Teléfono": telefono,
        "Referencia": referencia
    }

    return datos_cliente

cliente = registrar_cliente()

print("\nDatos guardados:")
for clave, valor in cliente.items():
    print(clave + ":", valor)
