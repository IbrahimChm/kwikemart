Ecommerce en Consola 

1. Descripción General

Este programa implementa una aplicación de consola en Python que simula las funciones básicas de un ecommerce: visualizar un catálogo de productos, realizar búsquedas, agregar artículos a un carrito y calcular el total a pagar.
El proyecto está desarrollado exclusivamente con contenidos del Módulo 3.

2. Funcionalidades Principales
• Catálogo de productos

Definido como una lista de diccionarios, cada uno con:
id, nombre, categoria y precio.

• Menú principal

Disponible al iniciar el programa, con opciones para:

Ver catálogo

Buscar productos

Agregar al carrito

Ver carrito y total

Vaciar carrito

Salir

El menú se repite mediante un ciclo while.

• Carrito de compras

Estructura basada en una lista donde se almacenan productos y cantidades.


3. Funciones Principales

mostrar_menu(): despliega el menú.

listar_productos(catalogo): muestra los productos disponibles.

buscar_productos(catalogo): permite buscar por nombre o categoría.

agregar_al_carrito(catalogo, carrito): valida y agrega productos.

mostrar_carrito_y_total(carrito): muestra ítems, subtotales y total.

vaciar_carrito(carrito): limpia el carrito.


4. Contenidos de Python Utilizados

Tipos básicos (int, float, str, bool)

Estructuras de datos (list, dict)

Condicionales (if, elif, else)

Ciclos (while y for)

Funciones con parámetros y valores retornados

Estilo en snake_case e indentación adecuada


5. Ejecución

Ejecutar en consola:

python ecommerce_m3.py