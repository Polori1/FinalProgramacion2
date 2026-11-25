from datetime import datetime
from src.models.productos import Producto

class AlertaStock:
    def __init__(self, id_alerta: int, producto: Producto):
        self.id_alerta = id_alerta
        self.producto = producto
        self.fecha_generacion = datetime.now()
        self.nivel_critico = "CRITICO" if producto.stock_actual == 0 else "ADVERTENCIA"
        self.estado = "PENDIENTE"

    def resolver(self):
        self.estado = "RESUELTA"