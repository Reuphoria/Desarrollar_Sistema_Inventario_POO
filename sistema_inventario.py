class Producto:
    #constructor 
    def __init__(self, nombre: str,precio : float, cantidad : int):
        self.nombre =  nombre
        self.precio = precio
        self.cantidad = cantidad
    
    #metodos actualizar_precio(nuevo_precio): para modificar el precio validando que sea mayor o igual que cero
    def actualizar_precio(self, nuevo_precio):
        if nuevo_precio >= 0:
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
    def __init__(self):
        self.almacenar_productos = []
    # añadir un produto a mi lista de producto
    def agregar_producto(self, producto):
        self.almacenar_productos.append(producto)
    # buscar un producto en el almacen
    def buscar_producto(self, nombre):
        for producto in self.almacenar_productos:
            if nombre.lower() in producto.nombre.lower():
                return producto
        return None
    #sumar el valor del inventario
    def calcular_valor_inventario(self):
        Total_productos = 0
        for producto in self.almacenar_productos:
            Total_producto += producto.calcular_valor_total()
        return Total_productos
    # mostrar todos los productos del inventario
    def listar_productos(self):
        for producto in self.almacenar_productos:
            print(producto)

def menu_principal():
    inventario = Inventario()
    while True:
        try:
            opcion = int(input("""Menu\n
                           
            1. Agregar Producto\n
            2. Buscar Producto\n
            3. Listar Productos\n
            4. Calcular Valor\n
            5. Exit                      
            """))
            #para la case Inventario la llamamos
            #vamos a añadir un producto nuevo el cual lleva 
            if opcion == 1:
                nombre = str(input("Digite el nombre del producto"))
                precio = float(input("Digite el precio del producto"))
                cantidad = int(input("Digite la cantidad del producto"))
                producto = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(producto)
            #buscar producto
            elif opcion == 2:
               nombre = str(input("Digite el nombre el producto que quiere buscar")) 
               print(inventario.buscar_producto(nombre))
            elif opcion == 3:
                pass
            elif opcion == 4:
                pass
            elif opcion == 5:
                break
            else:
                print("Valor invalido")
                
        except ValueError:
            print("valor invalido")
        
if __name__ == "__main__":
    menu_principal()
    