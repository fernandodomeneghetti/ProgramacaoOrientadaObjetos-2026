"""
Aula 11 — Exercício 3: Calculadora de Impostos
Imposto (ABC) → ICMS (18%) / ISS (5%) / IPI (variável) + CalculadoraFiscal

Execute: python ex3_calculadora_impostos.py
"""
from abc import ABC, abstractmethod


class Imposto(ABC):
    @property
    @abstractmethod
    def nome(self) -> str: ...

    @abstractmethod
    def calcular(self, valor: float) -> float: ...

    def __str__(self) -> str:
        return self.nome


class ICMS(Imposto):
    @property
    def nome(self) -> str:
        return "ICMS (18%)"

    def calcular(self, valor: float) -> float:
        return valor * 0.18


class ISS(Imposto):
    @property
    def nome(self) -> str:
        return "ISS (5%)"

    def calcular(self, valor: float) -> float:
        return valor * 0.05


class IPI(Imposto):
    def __init__(self, aliquota: float) -> None:
        self._aliquota = aliquota

    @property
    def nome(self) -> str:
        return f"IPI ({self._aliquota * 100:.1f}%)"

    def calcular(self, valor: float) -> float:
        return valor * self._aliquota


class CalculadoraFiscal:
    def __init__(self, impostos: list[Imposto] | None = None) -> None:
        self._impostos: list[Imposto] = list(impostos or [])

    def adicionar_imposto(self, imposto: Imposto) -> None:
        self._impostos.append(imposto)

    def calcular_total(self, valor_base: float) -> dict[str, float]:
        resultado = {"valor_base": valor_base}
        total_impostos = 0.0

        print(f"\nValor base: R${valor_base:.2f}")
        for imposto in self._impostos:
            valor_imposto = imposto.calcular(valor_base)  # polimorfismo
            total_impostos += valor_imposto
            resultado[imposto.nome] = valor_imposto
            print(f"  {imposto.nome}: R${valor_imposto:.2f}")

        resultado["total_impostos"] = total_impostos
        resultado["valor_final"] = valor_base + total_impostos
        print(f"  Total impostos: R${total_impostos:.2f}")
        print(f"  Valor final: R${resultado['valor_final']:.2f}")
        return resultado


calc = CalculadoraFiscal()
calc.adicionar_imposto(ICMS())
calc.adicionar_imposto(ISS())
calc.adicionar_imposto(IPI(0.10))
calc.calcular_total(1000)

# Recebendo a lista de impostos direto no construtor
calc_servico = CalculadoraFiscal([ISS()])
calc_servico.calcular_total(2500)
