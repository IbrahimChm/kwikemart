# Catálogo de productos

catalogo = [
    {"id": 1, "nombre": "Polera básica", "categoria": "ropa", "precio": 15000},
    {"id": 2, "nombre": "Auriculares Bluetooth", "categoria": "tecnología", "precio": 45000},
    {"id": 3, "nombre": "Taza cerámica", "categoria": "hogar", "precio": 8000},
    {"id": 4, "nombre": "Jeans clásico", "categoria": "ropa", "precio": 25000},
    {"id": 5, "nombre": "Mouse inalámbrico", "categoria": "tecnología", "precio": 20000}
]

# Carrito de compras 
carrito = []

# Funciones

def mostrar_menu():
    print("\nBienvenido/a Kwik-E-Mart")
    print("1) Ver catálogo de productos")
    print("2) Buscar producto por nombre o categoría")
    print("3) Agregar producto al carrito")
    print("4) Ver carrito y total")
    print("5) Vaciar carrito")
    print("0) Salir")

def listar_productos(catalogo):
    print("\nCatálogo de productos:")
    for producto in catalogo:
        print(f"ID: {producto['id']} | {producto['nombre']} | Categoría: {producto['categoria']} | Precio: ${producto['precio']}")

def buscar_productos(catalogo):
    busqueda = input("Ingrese nombre o categoría a buscar: ").lower()
    resultados = []
    for producto in catalogo:
        if busqueda in producto["nombre"].lower() or busqueda in producto["categoria"].lower():
            resultados.append(producto)
    if resultados:
        print("Productos encontrados:")
        for prod in resultados:
            print(f"ID: {prod['id']} | {prod['nombre']} | Categoría: {prod['categoria']} | Precio: ${prod['precio']}")
    else:
        print("No se encontraron productos con ese criterio.")

def agregar_al_carrito(catalogo, carrito):
    try:
        producto_id = int(input("Ingrese el ID del producto a agregar: "))
        # Buscar producto por id
        producto_seleccionado = None
        for producto in catalogo:
            if producto["id"] == producto_id:
                producto_seleccionado = producto
                break
        if producto_seleccionado:
            cantidad = int(input("Ingrese la cantidad: "))
            if cantidad > 0:
                # Revisar si el producto ya está en el carrito
                en_carrito = False
                for item in carrito:
                    if item["producto"]["id"] == producto_id:
                        item["cantidad"] += cantidad
                        en_carrito = True
                        break
                if not en_carrito:
                    carrito.append({"producto": producto_seleccionado, "cantidad": cantidad})
                print(f"{cantidad} x {producto_seleccionado['nombre']} agregado(s) al carrito.")
            else:
                print("Cantidad inválida. Debe ser mayor a 0.")
        else:
            print("Producto no encontrado. Verifica el ID.")
    except ValueError:
        print("Entrada inválida. Debe ingresar un número.")

def mostrar_carrito_y_total(carrito):
    if not carrito:
        print("El carrito está vacío.")
        return 0
    print("\nCarrito de compras:")
    total = 0
    for item in carrito:
        subtotal = item["producto"]["precio"] * item["cantidad"]
        total += subtotal
        print(f"ID: {item['producto']['id']} | {item['producto']['nombre']} | Cantidad: {item['cantidad']} | Precio unitario: ${item['producto']['precio']} | Subtotal: ${subtotal}")
    print(f"Total a pagar: ${total}")
    return total

def vaciar_carrito(carrito):
    carrito.clear()
    print("El carrito ha sido vaciado.")

# Programa 

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        listar_productos(catalogo)
    elif opcion == "2":
        buscar_productos(catalogo)
    elif opcion == "3":
        agregar_al_carrito(catalogo, carrito)
    elif opcion == "4":
        mostrar_carrito_y_total(carrito)
    elif opcion == "5":
        vaciar_carrito(carrito)
    elif opcion == "0":
        print("Gracias, vuelva prontos")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
