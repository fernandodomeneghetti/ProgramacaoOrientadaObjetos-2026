"""
Aula 10 — Seção 2 — Herança simples: Animal → Cachorro / Gato

Execute: python 01_heranca_simples.py
"""

class Animal:
    """Classe base para todos os animais."""

    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def comer(self) -> None:
        print(f"{self.nome} está comendo.")

    def dormir(self) -> None:
        print(f"{self.nome} está dormindo.")

    def __str__(self) -> str:
        return f"{self.nome} ({self.idade} anos)"


class Cachorro(Animal):
    """Cachorro herda de Animal."""

    def __init__(self, nome: str, idade: int, raca: str) -> None:
        super().__init__(nome, idade)  # Chama __init__ da classe pai
        self.raca = raca

    def latir(self) -> None:
        """Método específico do Cachorro."""
        print(f"{self.nome} diz: Au au!")

    def buscar(self, objeto: str) -> None:
        print(f"{self.nome} buscou o(a) {objeto}!")


class Gato(Animal):
    """Gato herda de Animal."""

    def __init__(self, nome: str, idade: int, pelagem: str) -> None:
        super().__init__(nome, idade)
        self.pelagem = pelagem

    def miar(self) -> None:
        """Método específico do Gato."""
        print(f"{self.nome} diz: Miau!")

    def ronronar(self) -> None:
        print(f"{self.nome} está ronronando...")


# Uso
rex = Cachorro("Rex", 3, "Pastor Alemão")
felix = Gato("Felix", 2, "Laranja")

# Métodos herdados de Animal
rex.comer()     # Rex está comendo.
felix.dormir()  # Felix está dormindo.

# Métodos específicos
rex.latir()       # Rex diz: Au au!
felix.miar()      # Felix diz: Miau!

# Verificação de tipo
print(isinstance(rex, Cachorro))  # True
print(isinstance(rex, Animal))    # True (é um Animal também!)
print(isinstance(felix, Cachorro))  # False
