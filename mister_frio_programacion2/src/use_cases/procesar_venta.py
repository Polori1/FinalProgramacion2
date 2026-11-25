from typing import List, Tuple
from src.models.persona import Empleado
from src.models.productos import Producto
from src.models.venta import Venta
from src.use_cases.consulta_stock import ServicioConsultaStock
from src.use_cases.alerta_stock import ServicioAlertaStock

class ServicioProcesarVenta:
    def __init__(self, servicio_consulta: ServicioConsultaStock, servicio_alerta: ServicioAlertaStock):
        self.servicio_consulta = servicio_consulta
        self.servicio_alerta = servicio_alerta
        self._contador_ventas = 1

    def procesar_venta(self, empleado: Empleado, items: List[Tuple[Producto, int]]) -> Venta:
        venta = Venta(self._contador_ventas, empleado)
        self._contador_ventas += 1

        for producto, cantidad in items:
            disponibles = self.servicio_consulta.consultar_por_nombre(producto.nombre)
            if not disponibles or producto.stock_actual < cantidad:
                raise ValueError(f"No hay stock suficiente para {producto.nombre}")

            venta.agregar_detalle(producto, cantidad)
            self.servicio_alerta.verificar_y_generar_alerta(producto)

        venta.finalizar_venta()
        return venta