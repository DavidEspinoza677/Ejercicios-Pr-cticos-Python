class Customer:
    def __init__(self, id, name, contact):
        self.id = id
        self.name = name
        self.contact = contact

    def get_discount(self):
        return 0.0

class RegularCustomer(Customer):
    def get_discount(self):
        return 0.05

class VIPCustomer(Customer):
    def get_discount(self):
        return 0.15

class Order:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products

    def total(self):
        total = sum(p[1] for p in self.products)
        return total - total * self.customer.get_discount()

    def show(self):
        print("\nResumen del pedido:")
        print("Cliente:", self.customer.name)
        print("Contacto:", self.customer.contact)
        for p in self.products:
            print("-", p[0], "$", p[1])
        print("Total con descuento: $", round(self.total(), 2))

while True:
    id = input("ID del cliente: ")
    name = input("Nombre del cliente: ")
    contact = input("Contacto del cliente: ")
    tipo = input("¿Es cliente VIP? (sí/no): ").lower()
    if tipo == "sí" or tipo == "si":
        cliente = VIPCustomer(id, name, contact)
    else:
        cliente = RegularCustomer(id, name, contact)

    productos = []
    while True:
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio del producto: "))
        productos.append((nombre, precio))
        mas = input("¿Agregar otro producto? (sí/no): ").lower()
        if mas != "sí" and mas != "si":
            break

    pedido = Order(cliente, productos)
    pedido.show()

    otro = input("\n¿Hacer otro pedido? (sí/no): ").lower()
    if otro != "sí" and otro != "si":
        print("Gracias por usar el sistema.")
        break
