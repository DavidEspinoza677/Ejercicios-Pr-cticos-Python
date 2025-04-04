class Product:
    def __init__(self, code, name, price, stock):
        self.code = code
        self.name = name
        self.price = price
        self.stock = stock

    def update(self, name=None, price=None, stock=None):
        if name is not None:
            self.name = name
        if price is not None:
            self.price = price
        if stock is not None:
            self.stock = stock

    def __str__(self):
        return f"Código: {self.code}, Nombre: {self.name}, Precio: {self.price}, Stock: {self.stock}"


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.code in self.products:
            print("Producto ya existe.")
        else:
            self.products[product.code] = product
            print("Producto agregado.")

    def search_product(self, code):
        return self.products.get(code, None)

    def update_product(self, code, name=None, price=None, stock=None):
        product = self.products.get(code)
        if product:
            product.update(name, price, stock)
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    def delete_product(self, code):
        if code in self.products:
            del self.products[code]
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def list_products(self):
        if not self.products:
            print("No hay productos en el inventario.")
        else:
            for product in self.products.values():
                print(product)


def main():
    inventory = Inventory()

    while True:
        print("\n--- Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Listar productos")
        print("6. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            while True:
                code = input("Código: ")
                name = input("Nombre: ")
                price = float(input("Precio: "))
                stock = int(input("Cantidad en stock: "))
                product = Product(code, name, price, stock)
                inventory.add_product(product)

                another = input("¿Desea añadir otro producto? (s/n): ").lower()
                if another != "s":
                    break

        elif option == "2":
            code = input("Código del producto: ")
            product = inventory.search_product(code)
            if product:
                print(product)
            else:
                print("Producto no encontrado.")

        elif option == "3":
            code = input("Código del producto: ")
            name = input("Nuevo nombre (Enter para mantener): ")
            price_input = input("Nuevo precio (Enter para mantener): ")
            stock_input = input("Nuevo stock (Enter para mantener): ")

            name = name if name else None
            price = float(price_input) if price_input else None
            stock = int(stock_input) if stock_input else None

            inventory.update_product(code, name, price, stock)

        elif option == "4":
            code = input("Código del producto: ")
            inventory.delete_product(code)

        elif option == "5":
            inventory.list_products()

        elif option == "6":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
