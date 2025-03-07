from animal_exotico import Huron, Boa_Constrictor

# Crear un Hurón
huron = Huron("Furby", 2.5, 3, "Estados Unidos", 15.0)
print(f"{huron.obtener_nombre()} hace {huron.hacer_sonido()}")
print(f"El costo de flete es: {huron.calcular_flete()}")

# Crear una Boa Constrictor
boa = Boa_Constrictor("Nagini", 20.0, 5, "Brasil", 25.0)
print(f"{boa.obtener_nombre()} hace {boa.hacer_sonido()}")
boa.comer_raton()
print(f"Ratones comidos: {boa.ratones_comidos}")
print(f"El costo de flete es: {boa.calcular_flete()}")