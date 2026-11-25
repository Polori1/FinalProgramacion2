from typing import Optional
from src.models.persona import Empleado

class ServicioAutenticacion:
    def __init__(self):
        self.empleado_autenticado: Optional[Empleado] = None

    def iniciar_sesion(self, empleado: Empleado, clave_ingresada: str) -> bool:
        if empleado.validar_clave(clave_ingresada):
            self.empleado_autenticado = empleado
            return True
        return False

    def cerrar_sesion(self):
        self.empleado_autenticado = None
