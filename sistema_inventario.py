class Producto:
    #constructor 
    def __init__(self, nombre: str,precio : float, cantidad : int):
        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")

        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

    
        self.nombre =  nombre
        self.precio = precio
        self.cantidad = cantidad
    
    #metodos actualizar_precio(nuevo_precio): para modificar el precio validando que sea mayor o igual que cero
    def actualizar_precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.precio = nuevo_precio

    #metodo actualizar_cantidad(nueva_cantidad): para modificar la cantidad validando que sea mayor o igual a cero
    def actualizar_cantidad(self, nueva_cantidad):
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
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
            if nombre.lower() == producto.nombre.lower():
                return producto
        return None
    #sumar el valor del inventario
    def calcular_valor_inventario(self):
        Total_productos = 0
        for producto in self.almacenar_productos:
            Total_productos += producto.calcular_valor_total()
        return Total_productos
    # mostrar todos los productos del inventario
    def listar_productos(self):
        for producto in self.almacenar_productos:
            print(producto)

def menu_principal(inventario):
    
    while True:
        try:
            opcion = int(input("""
                    MENU\n            
            1. Agregar Producto
            2. Buscar Producto
            3. Listar Productos
            4. Calcular Valor
            5. Exit                                
            """))
            #para la case Inventario la llamamos
            #vamos a añadir un producto nuevo el cual lleva 
        
        
            if opcion == 1:
                try:    
                    nombre = input("Digite el nombre del producto: ").strip()
                    if nombre == "":
                        raise ValueError("El nombre no puede estar vacío.")
                    
                    elif nombre.isdigit():
                        raise ValueError("El nombre no puede ser solo números.")
                
                except ValueError as e:
                    print(e)
                    continue
                
                try:
                    precio = float(input("Digite el precio del producto, el valor debe ser mayor a 0: "))
                    if precio < 0:
                        raise ValueError("El precio no puede ser negativo.")
                        
                except ValueError as e:
                    print(e)
                    continue
                
                try:
                    cantidad = int(input("Digite la cantidad del producto: "))
                    if cantidad < 0:
                        raise ValueError("La cantidad no puede ser negativa.")
                except ValueError as e:
                    print(e)
                    continue        
                
                producto = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(producto)
                #buscar producto
            elif opcion == 2:
                nombre = input("Digite el nombre el producto que quiere buscar: ")
                encontrado = inventario.buscar_producto(nombre)
                if encontrado is None:
                    print("No se encuentra producto con el nombre: ", nombre)
                else:
                    print(encontrado)
                
            elif opcion == 3:
                inventario.listar_productos()
            elif opcion == 4:
                valor_inventario = inventario.calcular_valor_inventario()
                print("El valor total del inventario es de: ", valor_inventario)
            elif opcion == 5:
                break
            else:
                print(f"El número: {opcion} no esta entre las opciones")
        except ValueError as e:
            print("Debe ingresar un número válido en el menú.")
            continue      
        
        
if __name__ == "__main__":
    inventario = Inventario()
    menu_principal(inventario)
    