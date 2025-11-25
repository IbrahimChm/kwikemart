# Mini Ecommerce en Consola

## Descripción
Aplicación en Python que simula un ecommerce básico en consola. Permite ver un catálogo de productos, buscar ítems, agregar al carrito, revisar el total y vaciarlo. Desarrollado únicamente con contenidos del Módulo 3.

---

## Funcionalidades Principales
- Catálogo definido como lista de diccionarios.
- Búsqueda por nombre o categoría.
- Carrito implementado como lista con productos y cantidades.
- Cálculo de subtotal y total.
- Menú interactivo mediante ciclo `while`.

---

## Funciones
- **mostrar_menu()**: despliega el menú principal.  
- **listar_productos(catalogo)**: muestra todos los productos.  
- **buscar_productos(catalogo)**: filtra coincidencias.  
- **agregar_al_carrito(catalogo, carrito)**: valida id/cantidad y agrega.  
- **mostrar_carrito_y_total(carrito)**: muestra ítems y total.  
- **vaciar_carrito(carrito)**: limpia el carrito.

---

## Contenido de Python Utilizado
- Tipos básicos (`int`, `str`, `float`)  
- Estructuras (`list`, `dict`)  
- Condicionales (`if`, `elif`, `else`)  
- Ciclos (`while`, `for`)  
- Funciones con parámetros y retornos  

---

## Ejecución
```bash
python ecommerce_m3.py

