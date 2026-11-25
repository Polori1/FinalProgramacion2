from src.models.persona import Empleado
from src.models.productos import Producto
from src.models.venta import Venta 
from src.models.alerta import AlertaStock

def test_empleado():
    emp = Empleado("12345678", "Carlos", "Perez", "carlos@misterfrio.com", "E01", "Ventas", "Vendedor", "1234")
    assert emp.nombre_completo == "Carlos Perez"
    assert emp.validar_clave("1234") is True
    assert emp.validar_clave("clave_incorrecta") is False

def test_producto_descuento_stock():
    prod = Producto(1, "Gas R134a", "Gases", 4500.0, 10, 3)
    assert prod.descontar_stock(4) is True
    assert prod.stock_actual == 6
    assert prod.requiere_alerta() is False

def test_producto_stock_insuficiente():
    prod = Producto(1, "Gas R134a", "Gases", 4500.0, 2, 3)
    assert prod.requiere_alerta() is True
    assert prod.descontar_stock(5) is False

def test_venta_y_detalles():
    emp = Empleado("12345678", "Carlos", "Perez", "carlos@misterfrio", "E01", "Ventas", "Vendedor", "1234")
    prod = Producto(1, "Burlete Lavropruk", "Gomas", 1000.0, 10, 2)
    venta = Venta(1, emp)
    venta.agregar_detalle(prod, 3)
    assert venta.total == 3000.0
    assert prod.stock_actual == 7

def test_alerta_stock():
    prod = Producto(1, "Compresor 1/4 HP", "Motor", 50000.0, 0, 1)
    alerta = AlertaStock(1, prod)
    assert alerta.nivel_critico == "CRITICO"
    assert alerta.estado == "PENDIENTE"
    alerta.resolver()
    assert alerta.estado == "RESUELTA"
