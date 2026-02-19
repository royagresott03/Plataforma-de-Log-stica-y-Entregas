def asignar_repartidor(zona_usuario, **repartidores):
    zona_usuario = zona_usuario.lower()

    for nombre, zonas in repartidores.items():
        if zonas == "todas":
            print("El repartidor asignado es:", nombre)
            return
        
        if zona_usuario in [z.lower() for z in zonas]:
            print("El repartidor asignado es:", nombre)
            return

    print("No hay repartidores disponibles para esa zona.")

zona = input("Ingrese la zona de entrega: ")

asignar_repartidor(
    zona,
    Luis=["centro"],
    Roy=["torices", "marbella"],
    Marcos=["bicentenario"],
    Samuel=["centro","torices","marbella","bicentenario"]
)
