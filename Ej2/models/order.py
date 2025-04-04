class sortAlgorithm:
    """Clase abstracta para los algoritmos de ordenamiento"""    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def order(self, list, ascendant=True):
        raise NotImplementedError("Abstracto")
    
    def show_list(self, list, message="Lista:"):
        print(f"{message} {', '.join(map(str, list))}")


class BubbleSort(sortAlgorithm):
    """Clase para el algoritmo de ordenamiento Bubble Sort"""  
    def __init__(self):
        super().__init__("Bubble Sort")
    
    def order(self, list, ascendant=True):
        n = len(list)
        for i in range(n):
            exchange = False
            for j in range(0, n-i-1):
                if (ascendant and list[j] > list[j+1]) or (not ascendant and list[j] < list[j+1]):
                    list[j], list[j+1] = list[j+1], list[j]
                    exchange = True
            if not exchange:
                break
        return list