"""
Aula 10 — Seção 4 — Sobrescrita de métodos: Forma → Retangulo / Circulo / Triangulo

Execute: python 03_sobrescrita_formas.py
"""

class Forma:
    """Classe base para formas geométricas."""

    def __init__(self, cor: str = "preto") -> None:
        self.cor = cor

    def area(self) -> float:
        """Método que DEVE ser sobrescrito pelas filhas."""
        return 0.0

    def perimetro(self) -> float:
        """Método que DEVE ser sobrescrito pelas filhas."""
        return 0.0

    def descricao(self) -> str:
        return f"Forma({self.cor}) | Área: {self.area():.2f}"


class Retangulo(Forma):
    def __init__(self, largura: float, altura: float, cor: str = "azul") -> None:
        super().__init__(cor)
        self.largura = largura
        self.altura = altura

    def area(self) -> float:
        """Sobrescreve o método area() da classe Forma."""
        return self.largura * self.altura

    def perimetro(self) -> float:
        return 2 * (self.largura + self.altura)


class Circulo(Forma):
    def __init__(self, raio: float, cor: str = "vermelho") -> None:
        super().__init__(cor)
        self.raio = raio

    def area(self) -> float:
        """Sobrescreve o método area() da classe Forma."""
        import math
        return math.pi * self.raio ** 2

    def perimetro(self) -> float:
        import math
        return 2 * math.pi * self.raio


class Triangulo(Forma):
    def __init__(self, base: float, altura: float, lado1: float,
                 lado2: float, lado3: float, cor: str = "verde") -> None:
        super().__init__(cor)
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def area(self) -> float:
        return (self.base * self.altura) / 2

    def perimetro(self) -> float:
        return self.lado1 + self.lado2 + self.lado3


# Cada classe fornece SUA implementação de area()
formas = [
    Retangulo(5, 3),
    Circulo(4),
    Triangulo(6, 4, 5, 5, 6),
]

for forma in formas:
    print(forma.descricao())
# Forma(azul) | Área: 15.00
# Forma(vermelho) | Área: 50.27
# Forma(verde) | Área: 12.00
