class Producto:
    #constructor 
    def __init__(self, nombre: str,precio : float, cantidad : int):
        self.nombre =  nombre
        self.precio = precio
        self.cantidad = cantidad
    
    #metodos actualizar_precio(nuevo_precio): para modificar el precio validando que sea mayor o igual que cero
    def actualizar_precio(self, nuevo_precio):
        if self.nuevo_precio >= 0:
            self.precio = nuevo_precio

    
    #metodo actualizar_cantidad(nueva_cantidad): para modificar la cantidad validando que sea mayor o igual a cero
    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad
        
    #metodo calcular_valor_total(): que devuelva el valor total (precio × cantidad)
    def calcular_valor_total(self):
        return self.precio * self.cantidad
    
    #metodo para mostrar la informacion de manera legible 
    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"
        
class Inventario:
    #constructor para crear una lista
    def __int__(self):
        self.almacenar_productos = []
    # añadir un produto a mi lista de producto
    def agregar_producto(self, producto):
        self.almacenar_productos.append(producto)
    
    def buscar_producto(self, nombre):
        pass

if __name__ == "__main__":
    pass