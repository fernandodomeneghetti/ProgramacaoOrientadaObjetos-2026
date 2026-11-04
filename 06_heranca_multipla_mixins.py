"""
Aula 10 — Seção 6 — Herança múltipla com mixins

Execute: python 06_heranca_multipla_mixins.py
"""

class Voador:
    """Mixin: capacidade de voar."""

    def voar(self) -> None:
        print(f"{self.nome} está voando! ✈️")


class Nadador:
    """Mixin: capacidade de nadar."""

    def nadar(self) -> None:
        print(f"{self.nome} está nadando! 🏊")


class Corredor:
    """Mixin: capacidade de correr."""

    def correr(self) -> None:
        print(f"{self.nome} está correndo! 🏃")


class Animal:
    def __init__(self, nome: str) -> None:
        self.nome = nome


# Herança múltipla
class Pato(Animal, Voador, Nadador):
    """Pato pode voar e nadar."""

    def fazer_som(self) -> str:
        return "Quack!"


class Aguia(Animal, Voador):
    """Águia pode voar."""

    def fazer_som(self) -> str:
        return "Screech!"


class Pinguim(Animal, Nadador, Corredor):
    """Pinguim pode nadar e correr (mas não voar!)."""

    def fazer_som(self) -> str:
        return "Honk!"


# Uso
pato = Pato("Donald")
pato.voar()   # Donald está voando! ✈️
pato.nadar()  # Donald está nadando! 🏊


pinguim = Pinguim("Tux")
pinguim.nadar()   # Tux está nadando! 🏊
pinguim.correr()  # Tux está correndo! 🏃
# pinguim.voar()  # AttributeError! Pinguim não tem Voador
