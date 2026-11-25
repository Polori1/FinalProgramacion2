from abc import ABC

class Persona(ABC):
    def __init__(self, dni: str, nombre: str, apellido: str, email: str, direccion: str = "", telefono: str = ""):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.direccion = direccion
        self.telefono = telefono

    @property
    def nombre_completo(self) -> str:
        return f"{self.nombre} {self.apellido}"

class Empleado(Persona):
    def __init__(self, dni: str, nombre: str, apellido: str, email: str, legajo: str, sector: str, cargo: str, clave: str):
        super().__init__(dni, nombre, apellido, email)
        self.legajo = legajo
        self.sector = sector
        self.cargo = cargo
        self.clave = clave #aca se encapsula la contraseña

    def validar_clave(self, clave_ingresada:str) -> bool:
        return self.clave == clave_ingresada