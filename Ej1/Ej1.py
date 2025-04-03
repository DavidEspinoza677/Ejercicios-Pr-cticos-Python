from functools import reduce

sales = []

print("Ingrese los datos de ventas.\n")

while True:
    product = input("Producto: ")
    price = float(input("Precio: "))
    quantity = int(input("Cantidad: "))
    sales.append({"product": product, "price": price, "quantity": quantity})
    
    another = input("¿Añadir otro producto? (si/no): ")
    if another.lower() != 'si':
        break

totals = list(map(lambda s: s["price"] * s["quantity"], sales))
total_sales = reduce(lambda a, b: a + b, totals, 0)
average = total_sales / len(totals) if totals else 0
high_sales = list(filter(lambda s: s["price"] * s["quantity"] > 200, sales))

print("\n--- Resultados ---")
print("Totales individuales:", totals)
print("Total general de ventas:", total_sales)
print("Promedio por venta:", average)
print("Ventas mayores a $200:")
for s in high_sales:
    print(s)
