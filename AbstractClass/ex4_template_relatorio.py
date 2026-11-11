"""
Aula 11 — Exercício 4: Template Method
RelatorioBase (ABC) → RelatorioTerminal / RelatorioHTML

gerar() é o template method: define a ordem (_cabecalho → _corpo → _rodape)
e as subclasses só decidem o FORMATO de cada parte.

Execute: python ex4_template_relatorio.py
"""
from abc import ABC, abstractmethod
from datetime import date


class RelatorioBase(ABC):
    def __init__(self, titulo: str, dados: list[dict]) -> None:
        self._titulo = titulo
        self._dados = dados

    def gerar(self) -> str:
        """Template method: o fluxo é fixo e não deve ser sobrescrito."""
        partes = [self._cabecalho(), self._corpo(), self._rodape()]
        return "\n".join(partes)

    @property
    def _colunas(self) -> list[str]:
        """Concreto: colunas obtidas das chaves do primeiro registro."""
        return list(self._dados[0].keys()) if self._dados else []

    @abstractmethod
    def _cabecalho(self) -> str: ...

    @abstractmethod
    def _corpo(self) -> str: ...

    @abstractmethod
    def _rodape(self) -> str: ...


class RelatorioTerminal(RelatorioBase):
    LARGURA_COLUNA = 15

    def _linha(self, valores: list) -> str:
        return " | ".join(f"{str(v):<{self.LARGURA_COLUNA}}" for v in valores)

    def _cabecalho(self) -> str:
        largura = len(self._linha(self._colunas))
        return "\n".join([
            "=" * largura,
            self._titulo.upper().center(largura),
            "=" * largura,
            self._linha(self._colunas),
            "-" * largura,
        ])

    def _corpo(self) -> str:
        return "\n".join(self._linha(list(item.values())) for item in self._dados)

    def _rodape(self) -> str:
        largura = len(self._linha(self._colunas))
        return "\n".join([
            "-" * largura,
            f"Total: {len(self._dados)} registros | Gerado em {date.today():%d/%m/%Y}",
        ])


class RelatorioHTML(RelatorioBase):
    def _cabecalho(self) -> str:
        ths = "".join(f"<th>{c}</th>" for c in self._colunas)
        return "\n".join([
            "<html>",
            f"<head><title>{self._titulo}</title></head>",
            "<body>",
            f"  <h1>{self._titulo}</h1>",
            "  <table border='1'>",
            f"    <tr>{ths}</tr>",
        ])

    def _corpo(self) -> str:
        linhas = []
        for item in self._dados:
            tds = "".join(f"<td>{v}</td>" for v in item.values())
            linhas.append(f"    <tr>{tds}</tr>")
        return "\n".join(linhas)

    def _rodape(self) -> str:
        return "\n".join([
            "  </table>",
            f"  <p>Total: {len(self._dados)} registros</p>",
            "</body>",
            "</html>",
        ])


dados = [
    {"nome": "Ana", "curso": "ADS", "nota": 9.5},
    {"nome": "Carlos", "curso": "SI", "nota": 7.0},
    {"nome": "Maria", "curso": "CC", "nota": 8.25},
]

relatorios: list[RelatorioBase] = [
    RelatorioTerminal("Notas da Turma", dados),
    RelatorioHTML("Notas da Turma", dados),
]

for relatorio in relatorios:
    print(f"\n### {relatorio.__class__.__name__} ###")
    print(relatorio.gerar())
