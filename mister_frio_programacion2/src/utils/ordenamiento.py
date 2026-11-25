from typing import List
from src.models.productos import Producto

def quicksort_productos_por_stock(productos: List[Producto]) -> List[Producto]:

#Esta funcion de aca lo que hace es ordenar los productos de menor a mayor segun el stock actual
#para identificar los repuestos que requieren reposicion o que pronto van a necesitarlo
    
    if len (productos) <= 1:
        return productos

#aca uso algo que ya vimos de ordenamiento, tomo el numero del centro
    pivote = productos[len(productos) // 2]
#ahora utilizando ese numero del centro empiezo a comparar cada numero con este
    menores = [p for p in productos if p.stock_actual < pivote.stock_actual]
    iguales = [p for p in productos if p.stock_actual == pivote.stock_actual]
    mayores = [p for p in productos if p.stock_actual > pivote.stock_actual]

#y con un poco de recursividad ya se tiene el resultado
    return quicksort_productos_por_stock(menores) + iguales +quicksort_productos_por_stock(mayores)