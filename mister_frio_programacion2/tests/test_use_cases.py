from src.models.persona import Empleado
from src.models.productos import Producto
from src.use_cases.autenticacion import ServicioAutenticacion
from src.use_cases.consulta_stock import ServicioConsultaStock
from src.use_cases.alerta_stock import ServicioAlertaStock
from src.use_cases.procesar_venta import ServicioProcesarVenta

def test_cu1_iniciar_sesion():
    emp = Empleado("1", "Carlos", "Perez", "c@frio.com", "E02", "Taller", "Tecnico", "pass123")
    auth = ServicioAutenticacion()
    assert auth.iniciar_sesion(emp, "pass123") is True
    assert auth.empleado_autenticado == emp

def test_cu6_consultar_disponibilidad_stock():
    catalogo = [
        Producto(1, "Gas R134a", "Gases", 4500.0, 5, 5),
        Producto(2, "Termostato Ranco", "Repuestos", 1200.0, 1, 3)
    ]
    srv = ServicioConsultaStock(catalogo)
    resultado = srv.consultar_por_nombre("gas")
    assert len(resultado) == 1
    assert resultado[0].nombre == "Gas R134a"
    assert len(srv.obtener_productos_bajo_stock()) == 2

def test_cu3_procesar_venta_de_producto():
    emp = Empleado("1", "Carlos", "Perez", "c@frio.com", "E02", "Taller", "Tecnico", "pass123")
    p1 = Producto(1, "Filtro Secador", "Insumos", 500.0, 10, 2)
    srv_cons = ServicioConsultaStock([p1])
    srv_alt = ServicioAlertaStock()
    srv_venta = ServicioProcesarVenta(srv_cons, srv_alt)

    venta = srv_venta.procesar_venta(emp, [(p1, 2)])
    assert venta.total == 1000.0
    assert p1.stock_actual == 8

def test_cu7_generar_alerta_stock_minimo():
    p1 = Producto(1, "Gas R134a", "Gases", 4500.0, 3, 3)
    srv_alt = ServicioAlertaStock()
    alerta = srv_alt.verificar_y_generar_alerta(p1)
    assert alerta is not None
    assert alerta.producto == p1
