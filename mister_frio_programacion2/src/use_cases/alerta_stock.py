from typing import List, Optional
from src.models.productos import Producto
from src.models.alerta import AlertaStock

class ServicioAlertaStock:
    def __init__(self):
        self.alertas: List[AlertaStock] = []
        self._contador_id = 1

    def verificar_y_generar_alerta(self, producto: Producto) -> Optional[AlertaStock]:
        if producto.requiere_alerta():
            alerta = AlertaStock(self._contador_id, producto)
            self._contador_id += 1
            self.alertas.append(alerta)
            return alerta
        return None
