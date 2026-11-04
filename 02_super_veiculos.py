"""
Aula 10 — Seção 3 — super(): Veiculo → Carro / Moto

Execute: python 02_super_veiculos.py
"""

class Veiculo:
    """Classe base para veículos."""

    def __init__(self, marca: str, modelo: str, ano: int) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False

    def ligar(self) -> None:
        self.ligado = True
        print(f"{self.marca} {self.modelo} ligado!")

    def desligar(self) -> None:
        self.ligado = False
        print(f"{self.marca} {self.modelo} desligado.")

    def __str__(self) -> str:
        status = "Ligado" if self.ligado else "Desligado"
        return f"{self.marca} {self.modelo} ({self.ano}) [{status}]"


class Carro(Veiculo):
    """Carro estende Veículo com portas e ar-condicionado."""

    def __init__(self, marca: str, modelo: str, ano: int, portas: int = 4) -> None:
        super().__init__(marca, modelo, ano)  # Inicializa Veiculo
        self.portas = portas
        self.ar_ligado = False

    def ligar_ar(self) -> None:
        if self.ligado:
            self.ar_ligado = True
            print("Ar-condicionado ligado!")
        else:
            print("Ligue o carro primeiro!")

    def __str__(self) -> str:
        base = super().__str__()  # Usa __str__ do pai
        return f"{base} | {self.portas} portas"


class Moto(Veiculo):
    """Moto estende Veículo com cilindradas."""

    def __init__(self, marca: str, modelo: str, ano: int, cilindradas: int) -> None:
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

    def empinar(self) -> None:
        if self.ligado:
            print(f"{self.modelo} empinando! 🏍️")
        else:
            print("Ligue a moto primeiro!")

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} | {self.cilindradas}cc"


# Uso
carro = Carro("Toyota", "Corolla", 2024)
moto = Moto("Honda", "CB 500", 2023, 500)

carro.ligar()        # Toyota Corolla ligado!
carro.ligar_ar()     # Ar-condicionado ligado!
print(carro)         # Toyota Corolla (2024) [Ligado] | 4 portas

moto.ligar()         # Honda CB 500 ligado!
moto.empinar()       # CB 500 empinando! 🏍️
print(moto)          # Honda CB 500 (2023) [Ligado] | 500cc
