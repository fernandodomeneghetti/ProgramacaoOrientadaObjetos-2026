"""
Aula 11 — Exercício 2: Repositório de Dados
Repositorio (ABC) → RepositorioMemoria (lista) / RepositorioArquivo (txt)

O mesmo código cliente (demonstrar) funciona com qualquer implementação:
é o contrato da classe abstrata que garante isso.

Execute: python ex2_repositorio_dados.py
"""
import json
import os
import tempfile
from abc import ABC, abstractmethod


class Repositorio(ABC):
    """Contrato para armazenar itens (dicts) identificados por 'id'."""

    @abstractmethod
    def salvar(self, item: dict) -> None:
        """Insere ou atualiza o item (pelo 'id')."""
        ...

    @abstractmethod
    def buscar(self, id: int) -> dict | None:
        """Retorna o item com o id informado, ou None."""
        ...

    @abstractmethod
    def listar(self) -> list[dict]:
        """Retorna todos os itens."""
        ...

    @abstractmethod
    def remover(self, id: int) -> bool:
        """Remove o item; retorna True se existia."""
        ...

    # Método CONCRETO construído em cima dos abstratos
    def total(self) -> int:
        return len(self.listar())

    def __str__(self) -> str:
        return f"{self.__class__.__name__} ({self.total()} itens)"


class RepositorioMemoria(Repositorio):
    """Guarda os itens em uma lista na memória."""

    def __init__(self) -> None:
        self._itens: list[dict] = []

    def salvar(self, item: dict) -> None:
        self.remover(item["id"])  # se já existe, substitui
        self._itens.append(dict(item))

    def buscar(self, id: int) -> dict | None:
        for item in self._itens:
            if item["id"] == id:
                return dict(item)
        return None

    def listar(self) -> list[dict]:
        return [dict(item) for item in self._itens]

    def remover(self, id: int) -> bool:
        for i, item in enumerate(self._itens):
            if item["id"] == id:
                del self._itens[i]
                return True
        return False


class RepositorioArquivo(Repositorio):
    """Guarda os itens em um arquivo .txt (um JSON por linha)."""

    def __init__(self, caminho: str) -> None:
        self._caminho = caminho
        if not os.path.exists(caminho):
            open(caminho, "w", encoding="utf-8").close()

    def _ler(self) -> list[dict]:
        with open(self._caminho, encoding="utf-8") as arquivo:
            return [json.loads(linha) for linha in arquivo if linha.strip()]

    def _gravar(self, itens: list[dict]) -> None:
        with open(self._caminho, "w", encoding="utf-8") as arquivo:
            for item in itens:
                arquivo.write(json.dumps(item, ensure_ascii=False) + "\n")

    def salvar(self, item: dict) -> None:
        itens = [i for i in self._ler() if i["id"] != item["id"]]
        itens.append(item)
        self._gravar(itens)

    def buscar(self, id: int) -> dict | None:
        for item in self._ler():
            if item["id"] == id:
                return item
        return None

    def listar(self) -> list[dict]:
        return self._ler()

    def remover(self, id: int) -> bool:
        itens = self._ler()
        restantes = [i for i in itens if i["id"] != id]
        self._gravar(restantes)
        return len(restantes) < len(itens)


def demonstrar(repo: Repositorio) -> None:
    """Código cliente: só conhece o contrato Repositorio (polimorfismo)."""
    print(f"\n=== {repo.__class__.__name__} ===")
    repo.salvar({"id": 1, "nome": "Ana", "curso": "ADS"})
    repo.salvar({"id": 2, "nome": "Carlos", "curso": "SI"})
    repo.salvar({"id": 3, "nome": "Maria", "curso": "CC"})
    print(f"  Após salvar 3: {repo}")

    print(f"  buscar(2): {repo.buscar(2)}")
    print(f"  buscar(99): {repo.buscar(99)}")

    repo.salvar({"id": 2, "nome": "Carlos", "curso": "ADS"})  # atualização
    print(f"  Após atualizar id 2: {repo.buscar(2)}")

    print(f"  remover(1): {repo.remover(1)}")
    print(f"  remover(1) de novo: {repo.remover(1)}")

    print("  listar():")
    for item in repo.listar():
        print(f"    {item}")


if __name__ == "__main__":
    demonstrar(RepositorioMemoria())

    caminho = os.path.join(tempfile.gettempdir(), "aula11_repositorio.txt")
    if os.path.exists(caminho):
        os.remove(caminho)
    demonstrar(RepositorioArquivo(caminho))

    print(f"\nConteúdo de {caminho}:")
    with open(caminho, encoding="utf-8") as arquivo:
        print(arquivo.read(), end="")
