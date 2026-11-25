from datetime import datetime
from typing import List
from src.models.productos import Producto
from src.models.persona import Empleado

class DetalleVenta:
    def __init__(self, producto: Producto, cantidad: int, precio_unitario: float):
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    @property
    def subtotal(self) -> float:
        return self.cantidad * self.precio_unitario

class Venta:
    def __init__(self, id_venta: int, empleado: Empleado):
        self.id_venta = id_venta
        self.empleado = empleado
        self.fecha = datetime.now()
        self.detalles: List[DetalleVenta] = []
        self.estado = "EN_PROCESO"

    def agregar_detalle(self, producto: Producto, cantidad: int) -> None:
        if producto.descontar_stock(cantidad):
            detalle = DetalleVenta(producto, cantidad, producto.precio_venta)
            self.detalles.append(detalle)
        else:
            raise ValueError(f"Stock insuficiente para {producto.nombre}. Disponible: {producto.stock_actual}")

    @property
    def total(self) -> float:
        return sum(d.subtotal for d in self.detalles)

    def finalizar_venta(self) -> None:
        if not self.detalles:
            raise ValueError("No se puede finalizar una venta sin productos.")
        self.estado = "COMPLETADA"