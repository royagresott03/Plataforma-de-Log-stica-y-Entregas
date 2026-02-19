def asignar_repartidor(zona_usuario, **repartidores):
    zona_usuario = zona_usuario.lower()
    samuel = None

    for nombre, datos in repartidores.items():
        zonas = datos["zonas"]
        disponible = datos["disponible"]
        if zonas == "todas":
            samuel = nombre
            continue
        if zona_usuario in [z.lower() for z in zonas] and disponible:
            print("Repartidor asignado:", nombre)
            return
    if samuel:
        print("Todos los repartidores de la zona están ocupados.")
        print("Repartidor asignado:", samuel)
    else:
        print("No hay repartidores disponibles.")

zona = input("Ingrese la zona de entrega: ")
asignar_repartidor(
    zona,
    Luis={"zonas": ["centro"], "disponible": False},
    Roy={"zonas": ["torices", "marbella"], "disponible": False},
    Marcos={"zonas": ["bicentenario"], "disponible": True},
    Samuel={"zonas": "todas", "disponible": True}
)