import models.order as mod_ord

class OrderDao:
    """Clase para gestionar el ordenamiento de listas"""    
    def __init__(self):
        self.algorithm = mod_ord.BubbleSort()
        self.browsing = []
    
    def sort_list(self, list, ascendant=True):
        result = self.algorithm.order(list.copy(), ascendant=ascendant)
        self.browsing.append({
            'Original': list.copy(),
            'Ordenada': result,
            'ascendente': ascendant,
            'algoritmo': self.algorithm.nombre
        })
        return result
    
    def show_list(self, list, message="Lista:"):
        self.algorithm.show_list(list, message)
    