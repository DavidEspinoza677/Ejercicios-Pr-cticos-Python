import controllers.order_dao as dao
import models.order as mod_ord
import os

os.system('cls' if os.name == 'nt' else 'clear')

order_dao = dao.OrderDao()

enter = input("Añadir números separados por comas: ")
numbers = list(map(int, enter.split(',')))

order_dao.show_list(numbers, "Original:")

ascendant = order_dao.sort_list(numbers)
order_dao.show_list(ascendant, "Ascendente:")

descending = order_dao.sort_list(numbers, ascendant=False)
order_dao.show_list(descending, "Descendente:")
