from ianimal import iAnimal

class Animal(iAnimal):
    def __init__(self, nombre: str, peso: float, edad: int):
        self.nombre = nombre
        self.peso = peso
        self.edad = edad
        self._kilos_comidos = 0
    
    def hacer_sonido(self):
        pass
    
    def comer(self, kilos):
        self._kilos_comidos += kilos
    
    def obtener_kilos_comidos(self):
        return self._kilos_comidos
    
    def obtener_nombre(self):
        return self.nombre
    
    def obtener_peso(self):
        return self.peso
    
    def obtener_edad(self):
        return self.edad