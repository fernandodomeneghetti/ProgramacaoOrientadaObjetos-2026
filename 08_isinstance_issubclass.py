"""
Aula 10 — Seção 7 — isinstance() e issubclass()

Execute: python 08_isinstance_issubclass.py
"""

class Animal:
    pass

class Cachorro(Animal):
    pass

class GoldenRetriever(Cachorro):
    pass


rex = GoldenRetriever()

# isinstance - verifica se objeto é instância de uma classe
print(isinstance(rex, GoldenRetriever))  # True
print(isinstance(rex, Cachorro))         # True (herança!)
print(isinstance(rex, Animal))           # True
print(isinstance(rex, int))              # False

# issubclass - verifica se classe é subclasse de outra
print(issubclass(GoldenRetriever, Cachorro))  # True
print(issubclass(GoldenRetriever, Animal))    # True
print(issubclass(Cachorro, GoldenRetriever))  # False
