"""
Sistema de Pagamentos
Demonstra: herança, sobrescrita, polimorfismo, super()
"""
from datetime import datetime


class Funcionario:
    """Classe base para todos os funcionários."""

    def __init__(self, nome: str, cpf: str, salario_base: float) -> None:
        self.nome = nome
        self.cpf = cpf
        self._salario_base = salario_base

    @property
    def salario_base(self) -> float:
        return self._salario_base

    def calcular_pagamento(self) -> float:
        """Método que DEVE ser sobrescrito pelas subclasses."""
        return self._salario_base

    def gerar_holerite(self) -> str:
        """Gera o holerite do funcionário."""
        pagamento = self.calcular_pagamento()
        return (f"{'─' * 40}\n"
                f"  {self.nome} ({self.__class__.__name__})\n"
                f"  CPF: {self.cpf}\n"
                f"  Salário Base: R${self._salario_base:.2f}\n"
                f"  Pagamento Final: R${pagamento:.2f}\n"
                f"{'─' * 40}")

    def __str__(self) -> str:
        return f"{self.nome} ({self.__class__.__name__}) - R${self.calcular_pagamento():.2f}"


class FuncionarioCLT(Funcionario):
    """Funcionário CLT com desconto de INSS e benefícios."""

    def __init__(self, nome: str, cpf: str, salario_base: float,
                 vale_transporte: float = 0, vale_refeicao: float = 0) -> None:
        super().__init__(nome, cpf, salario_base)
        self.vale_transporte = vale_transporte
        self.vale_refeicao = vale_refeicao

    def _calcular_inss(self) -> float:
        """Calcula desconto INSS simplificado."""
        if self._salario_base <= 1412:
            return self._salario_base * 0.075
        elif self._salario_base <= 2666:
            return self._salario_base * 0.09
        elif self._salario_base <= 4000:
            return self._salario_base * 0.12
        else:
            return self._salario_base * 0.14

    def calcular_pagamento(self) -> float:
        """Sobrescrita: salário - INSS + benefícios."""
        inss = self._calcular_inss()
        return self._salario_base - inss + self.vale_transporte + self.vale_refeicao


class Gerente(FuncionarioCLT):
    """Gerente: CLT com bônus por meta."""

    def __init__(self, nome: str, cpf: str, salario_base: float,
                 bonus_meta: float = 0, **kwargs) -> None:
        super().__init__(nome, cpf, salario_base, **kwargs)
        self.bonus_meta = bonus_meta

    def calcular_pagamento(self) -> float:
        """Sobrescrita: adiciona bônus ao pagamento CLT."""
        pagamento_clt = super().calcular_pagamento()
        return pagamento_clt + self.bonus_meta


class Freelancer(Funcionario):
    """Freelancer: pago por hora."""

    def __init__(self, nome: str, cpf: str, valor_hora: float, horas: float) -> None:
        super().__init__(nome, cpf, valor_hora)
        self.valor_hora = valor_hora
        self.horas = horas

    def calcular_pagamento(self) -> float:
        """Sobrescrita: pago por hora trabalhada."""
        return self.valor_hora * self.horas


class Estagiario(Funcionario):
    """Estagiário: bolsa fixa + auxílio."""

    def __init__(self, nome: str, cpf: str, bolsa: float,
                 auxilio_transporte: float = 200) -> None:
        super().__init__(nome, cpf, bolsa)
        self.auxilio_transporte = auxilio_transporte

    def calcular_pagamento(self) -> float:
        """Sobrescrita: bolsa + auxílio."""
        return self._salario_base + self.auxilio_transporte


# === Folha de Pagamento ===
def processar_folha(funcionarios: list[Funcionario]) -> None:
    """Processa folha de pagamento — POLIMORFISMO em ação!"""
    print("=" * 50)
    print(f"  FOLHA DE PAGAMENTO - {datetime.now().strftime('%m/%Y')}")
    print("=" * 50)

    total = 0.0
    for func in funcionarios:
        # Polimorfismo: cada tipo calcula seu pagamento
        pagamento = func.calcular_pagamento()
        total += pagamento
        print(f"  {func.nome:<20} {func.__class__.__name__:<15} R${pagamento:>10.2f}")

    print(f"{'─' * 50}")
    print(f"  {'TOTAL':<35} R${total:>10.2f}")
    print("=" * 50)


# === Programa Principal ===
if __name__ == "__main__":
    equipe: list[Funcionario] = [
        FuncionarioCLT("Ana Silva", "111.111.111-11", 5000,
                       vale_transporte=300, vale_refeicao=600),
        Gerente("Carlos Lima", "222.222.222-22", 12000,
                bonus_meta=3000, vale_transporte=0, vale_refeicao=800),
        Freelancer("Maria Souza", "333.333.333-33", 150, 80),
        Estagiario("João Santos", "444.444.444-44", 1200),
        FuncionarioCLT("Pedro Costa", "555.555.555-55", 3500,
                       vale_transporte=250, vale_refeicao=500),
    ]

    processar_folha(equipe)

    # Holerite individual
    print(f"\n{equipe[1].gerar_holerite()}")
