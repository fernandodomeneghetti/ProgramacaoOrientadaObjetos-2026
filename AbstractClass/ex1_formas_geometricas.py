"""
Aula 11 — Exercício 1: Formas Geométricas Abstratas
Forma (ABC) → Circulo / Retangulo / Triangulo

Execute: python ex1_formas_geometricas.py
"""
import math
from abc import ABC, abstractmethod


class Forma(ABC):
    @property
    @abstractmethod
    def nome(self) -> str: ...

    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimetro(self) -> float: ...

    def __str__(self) -> str:
        return f"{self.nome}: Área={self.area():.2f}, Perímetro={self.perimetro():.2f}"


class Circulo(Forma):
    def __init__(self, raio: float) -> None:
        self._raio = raio

    @property
    def nome(self) -> str:
        return f"Círculo(r={self._raio})"

    def area(self) -> float:
        return math.pi * self._raio ** 2

    def perimetro(self) -> float:
        return 2 * math.pi * self._raio


class Retangulo(Forma):
    def __init__(self, largura: float, altura: float) -> None:
        self._largura = largura
        self._altura = altura

    @property
    def nome(self) -> str:
        return f"Retângulo({self._largura}x{self._altura})"

    def area(self) -> float:
        return self._largura * self._altura

    def perimetro(self) -> float:
        return 2 * (self._largura + self._altura)


class Triangulo(Forma):
    def __init__(self, a: float, b: float, c: float) -> None:
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError(f"Lados ({a}, {b}, {c}) não formam um triângulo")
        self._a, self._b, self._c = a, b, c

    @property
    def nome(self) -> str:
        return f"Triângulo({self._a},{self._b},{self._c})"

    def area(self) -> float:
        # Fórmula de Heron
        s = (self._a + self._b + self._c) / 2
        return math.sqrt(s * (s - self._a) * (s - self._b) * (s - self._c))

    def perimetro(self) -> float:
        return self._a + self._b + self._c


formas: list[Forma] = [Circulo(5), Retangulo(4, 6), Triangulo(3, 4, 5)]
for f in formas:
    print(f)

maior = max(formas, key=lambda f: f.area())
print(f"\nMaior área: {maior.nome}")

try:
    Forma()
except TypeError as erro:
    print(f"\nTypeError: {erro}")
