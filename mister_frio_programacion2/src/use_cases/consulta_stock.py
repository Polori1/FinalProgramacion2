from typing import List
from src.models.productos import Producto

class ServicioConsultaStock:
    def __init__(self, catalogo: List[Producto]):
        self.catalogo = catalogo

    def consultar_por_nombre(self, termino: str) -> List[Producto]:
        return [p for p in self.catalogo if termino.lower() in p.nombre.lower()]

    def obtener_productos_bajo_stock(self) -> List[Producto]:
        return [p for p in self.catalogo if p.requiere_alerta()]
