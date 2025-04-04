class Invoice:
    def __init__(self):
        self.__items = []

    def add_item(self, name, quantity, price, discount):
        self.__items.append((name, quantity, price, discount))

    def total(self):
        return sum(q * p * (1 - d / 100) for _, q, p, d in self.__items)

    def report(self):
        print("Factura:")
        for name, q, p, d in self.__items:
            print(f"{q} x {name} @ ${p} - {d}%")
        print(f"Total: ${self.total():.2f}")

invoice = Invoice()

while True:
    name = input("Nombre del producto: ")
    quantity = int(input("Cantidad: "))
    price = float(input("Precio unitario: "))
    discount = float(input("Descuento (%): "))
    invoice.add_item(name, quantity, price, discount)
    more = input("¿Desea añadir otro producto? (si/no): ").lower()
    if more != "si":
        break

invoice.report()
