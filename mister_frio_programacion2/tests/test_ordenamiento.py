from src.models.productos import Producto
from src.utils.ordenamiento import quicksort_productos_por_stock

def test_quicksort_productos_por_stock():
    productos = [
        Producto(1, "Producto A", "Cat", 100.0, 15, 2),
        Producto(2, "Producto B", "Cat", 100.0, 2, 2),
        Producto(3, "Producto C", "Cat", 100.0, 8, 2)
    ]
    ordenados = quicksort_productos_por_stock(productos)
    stocks = [p.stock_actual for p in ordenados]
    assert stocks == [2, 8, 15]
