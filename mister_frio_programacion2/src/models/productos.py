class Producto:
    def __init__(self, id_producto: int, nombre: str, categoria: str, precio_venta: float, stock_actual: int, stock_minimo: int):
        self.id_producto = id_producto
        self.nombre = nombre
        self.categoria = categoria
        self.precio_venta = precio_venta
        self.stock_actual = stock_actual
        self.stock_minimo = stock_minimo

    def descontar_stock(self,cantidad:int) -> bool:
        if cantidad <= 0:
            raise ValueError ("La cantidad debe ser mayor a 0.")
        if self.stock_actual >= cantidad:
            self.stock_actual -= cantidad
            return True
        return False

    def requiere_alerta(self) -> bool:
        return self.stock_actual <= self.stock_minimo