from animal import Animal

class Animal_Exotico(Animal):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float):
        super().__init__(nombre, peso, edad)
        self.pais_origen = pais_origen
        self.impuestos = impuestos
    
    def calcular_flete(self):
        """Calcula el costo de importar el animal multiplicando su peso por los impuestos."""
        return self.peso * self.impuestos


class Huron(Animal_Exotico):
    def hacer_sonido(self):
        """Devuelve el sonido característico del hurón."""
        return "¡Eek Eek!"


class Boa_Constrictor(Animal_Exotico):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self.ratones_comidos = 0
    
    def hacer_sonido(self):
        """Devuelve el sonido característico de la boa constrictor."""
        return "¡Tsss!"
    
    def comer_raton(self):
        """Aumenta en uno la cantidad de ratones comidos por la boa."""
        if self.ratones_comidos >= 10:
            raise ValueError("Demasiados Ratones!")
        self.ratones_comidos += 1

class Guarderia:
    def __init__(self):
        self.boas = [Boa_Constrictor("Boa1", 15.0, 4, "Argentina", 20.0),
                     Boa_Constrictor("Boa2", 18.0, 6, "Colombia", 22.0)]
        self.hurones = [Huron("Huron1", 3.0, 2, "Chile", 10.0),
                        Huron("Huron2", 2.0, 1, "Perú", 12.0)]

    def alimentar_boa(self, boa):
        if boa is None:
            return "Esta Boa no existe!"
        try:
            boa.comer_raton()
            return "Éxito"
        except ValueError as e:
            return "La boa está llena"