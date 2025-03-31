from pymongo import MongoClient
import datetime
conexion = MongoClient("mongodb://localhost:27017/")
db = conexion.ventas_florcatorce

def insertar_venta():
    fecha = input("Ingrese la fecha de la venta (DD-MM-YYYY): ")
    efectivo = float(input("Monto de efectivo: "). replace(",", "."))
    tarjeta = float(input("Monto de tarjeta: ").replace(",", "."))
    propina = float(input("Monto de propina: ").replace(",", "."))
    db.abril.insert_one({
        "fecha": fecha,
        "efectivo": efectivo,
        "tarjeta": tarjeta,
        "propina": propina
    })

def ver_ventas():
    ventas = db.abril.find()
    for venta in ventas:
        print(f"Fecha: {venta['fecha']}, Efectivo: {venta['efectivo']}, Tarjeta: {venta['tarjeta']}, Propina: {venta['propina']}")

def ver_una_venta():
    fecha = input("Ingrese la fecha de la venta (DD-MM-YYYY): ")
    venta = db.abril.find_one({"fecha": fecha})
    if venta:
        print(f"Fecha: {venta['fecha']}, Efectivo: {venta['efectivo']}, Tarjeta: {venta['tarjeta']}, Propina: {venta['propina']}")
    else:
        print("No se encontró la venta.")

def editar_venta():
    fecha = input("Ingrese la fecha de la venta a editar (DD-MM-YYYY): ")
    venta = db.abril.find_one({"fecha": fecha})
    if venta:
        nuevo_efectivo = float(input("Nuevo monto de efectivo: ").replace(",", "."))
        nuevo_tarjeta = float(input("Nuevo monto de tarjeta: ").replace(",", "."))
        nuevo_propina = float(input("Nuevo monto de propina: ").replace(",", "."))
        db.abril.update_one({"fecha": fecha}, {
            "$set": {
                "efectivo": nuevo_efectivo,
                "tarjeta": nuevo_tarjeta,
                "propina": nuevo_propina
            }
        })
        print("Venta actualizada.")
    else:
        print("No se encontró la venta.")

def eliminar_venta():
    fecha = input("Ingrese la fecha de la venta a eliminar (DD-MM-YYYY): ")
    venta = db.abril.find_one({"fecha": fecha})
    if venta:
        db.abril.delete_one({"fecha": fecha})
        print("Venta eliminada.")
    else:
        print("No se encontró la venta.")

def menu():
    flag = True
    while flag:
        print("1. Insertar registro de ventas")
        print("2. Ver ventas")
        print("3. Ver una venta")
        print("4. Editar una venta")
        print("5. Eliminar una venta")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            insertar_venta()
        elif opcion == "2":
            ver_ventas()
        elif opcion == "3":
            ver_una_venta()
        elif opcion == "4":
            editar_venta()
        elif opcion == "5":
            eliminar_venta()
        elif opcion == "6":
            print("Saliendo del programa...")
            flag = False
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    # Verificar la conexión a la base de datos
    if not conexion:
        print("Error al conectar a la base de datos.")
    
    menu()