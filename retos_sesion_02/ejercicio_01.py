class Animal:
    def __init__(self, especie, tipo, lugar):
        self.especie = especie
        self.tipo = tipo
        self.lugar = lugar
        self.origen = 'feral'

# 2 mamiferos
mamifero_1 = Animal("León", "Mamifero", "Africa")
mamifero_2 = Animal('Llama', "Mamifero", "America")

# 1 reptil
reptil = Animal("Serpiente", "Reptil", "Desierto")

# 1 ave
ave = Animal("Avestruz", "Ave", "Africa")

print(f"Especie: {mamifero_1.especie}\nTipo: {mamifero_1.tipo}\nLugar: {mamifero_1.lugar}\nOrigen: {mamifero_1.origen}\n")
print(f"Especie: {mamifero_2.especie}\nTipo: {mamifero_2.tipo}\nLugar: {mamifero_2.lugar}\nOrigen: {mamifero_2.origen}\n")

print(f"Especie: {reptil.especie}\nTipo: {reptil.tipo}\nLugar: {reptil.lugar}\nOrigen: {reptil.origen}\n")

print(f"Especie: {ave.especie}\nTipo: {ave.tipo}\nLugar: {ave.lugar}\nOrigen: {ave.origen}\n")
