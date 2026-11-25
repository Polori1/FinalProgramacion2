from src.models.persona import Empleado
from src.models.productos import Producto
from src.use_cases.autenticacion import ServicioAutenticacion
from src.use_cases.consulta_stock import ServicioConsultaStock
from src.use_cases.alerta_stock import ServicioAlertaStock
from src.use_cases.procesar_venta import ServicioProcesarVenta
from src.utils.ordenamiento import quicksort_productos_por_stock

def ejecutar_menu():
    empleado = Empleado("38123456", "Santiago", "Oviedo", "santiago@misterfrio.com", "E001", "Ventas", "Vendedor", "1234")
    
    catalogo = [
        Producto(101, "Gas Refrigerante R134a", "Gases", 45000.0, 3, 5),
        Producto(102, "Burlete Lavropruk 1.2m", "Gomas", 8500.0, 15, 10),
        Producto(103, "Compresor Tecumseh 1/4 HP", "Motor", 120000.0, 1, 2),
        Producto(104, "Termostato Robertshaw", "Repuestos", 12500.0, 8, 4),
        Producto(105, "Filtro Secador 1/4", "Insumos", 3200.0, 0, 5)
    ]

    auth_service = ServicioAutenticacion()
    consulta_service = ServicioConsultaStock(catalogo)
    alerta_service = ServicioAlertaStock()
    venta_service = ServicioProcesarVenta(consulta_service, alerta_service)

    print("==================================================")
    print("      SISTEMA DE GESTIÓN MÍSTER FRÍO S.A.S.")
    print("==================================================")
    
    intentos = 0
    while not auth_service.empleado_autenticado and intentos < 3:
        clave = input(f"Ingrese contraseña para {empleado.nombre_completo} (Demo: 1234): ")
        if auth_service.iniciar_sesion(empleado, clave):
            print(f"\n[✓] Sesión iniciada como: {empleado.nombre_completo} ({empleado.cargo})")
        else:
            intentos += 1
            print("[X] Contraseña incorrecta. Reintente.")

    if not auth_service.empleado_autenticado:
        print("Demasiados intentos fallidos. Saliendo...")
        return

    while True:
        print("\n---------------- MENU PRINCIPAL ----------------")
        print("1. Consultar Stock de Productos (CU6)")
        print("2. Registrar Venta de Producto (CU3 + CU6 + CU7)")
        print("3. Ver Alertas de Stock Mínimo (CU7)")
        print("4. Ordenar Productos por Urgencia de Stock (QuickSort)")
        print("0. Salir (CU2 Cerrar Sesión)")
        print("------------------------------------------------")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n--- INVENTARIO DE PRODUCTOS ---")
            for p in catalogo:
                alerta_str = "ALERTA STOCK" if p.requiere_alerta() else "OK"
                print(f"[{p.id_producto}] {p.nombre:<30} | Stock: {p.stock_actual:>2} | Mínimo: {p.stock_minimo:>2} | [{alerta_str}]")

        elif opcion == "2":
            print("\n--- PROCESAR VENTA EN MOSTRADOR ---")
            for p in catalogo:
                print(f"ID: {p.id_producto} - {p.nombre} (${p.precio_venta}) - Disponible: {p.stock_actual}")
            try:
                prod_id = int(input("Ingrese ID del producto a vender: "))
                cant = int(input("Ingrese cantidad a vender: "))
                
                prod_sel = next((p for p in catalogo if p.id_producto == prod_id), None)
                if prod_sel:
                    venta = venta_service.procesar_venta(empleado, [(prod_sel, cant)])
                    print(f"\n[✓] Venta #{venta.id_venta} registrada con éxito. Total: ${venta.total:,.2f}")
                else:
                    print("[X] Producto no encontrado.")
            except Exception as e:
                print(f"[X] Error al procesar venta: {e}")

        elif opcion == "3":
            print("\n--- ALERTAS DE STOCK MÍNIMO GENERADAS ---")
            if not alerta_service.alertas:
                print("No hay alertas generadas aún en esta sesión.")
            for alt in alerta_service.alertas:
                print(f"Alerta #{alt.id_alerta} - Producto: {alt.producto.nombre} | Stock Actual: {alt.producto.stock_actual} | Nivel: {alt.nivel_critico}")

        elif opcion == "4":
            print("\n--- PRODUCTOS ORDENADOS POR STOCK (QuickSort) ---")
            ordenados = quicksort_productos_por_stock(catalogo)
            for p in ordenados:
                print(f"Stock: {p.stock_actual:>2} | {p.nombre:<30} | Categoria: {p.categoria}")

        elif opcion == "0":
            auth_service.cerrar_sesion()
            print("\n[✓] Sesión cerrada. ¡Hasta luego!")
            break
        else:
            print("[X] Opción no válida.")
