"""
Aula 10 — Seção 5.1 — Polimorfismo por herança: fazer_som()

Execute: python 04_polimorfismo_animais.py
"""

class Animal:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def fazer_som(self) -> str:
        return "..."


class Cachorro(Animal):
    def fazer_som(self) -> str:
        return "Au au!"


class Gato(Animal):
    def fazer_som(self) -> str:
        return "Miau!"


class Pato(Animal):
    def fazer_som(self) -> str:
        return "Quack!"


# Polimorfismo em ação: mesma interface, comportamento diferente
animais: list[Animal] = [
    Cachorro("Rex"),
    Gato("Felix"),
    Pato("Donald"),
    Cachorro("Bob"),
]

for animal in animais:
    # Todos respondem a fazer_som(), cada um à sua maneira
    print(f"{animal.nome}: {animal.fazer_som()}")

# Rex: Au au!
# Felix: Miau!
# Donald: Quack!
# Bob: Au au!
