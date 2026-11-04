"""
Aula 10 — Seção 5.2 — Duck typing: polimorfismo sem herança

Execute: python 05_duck_typing.py
"""

# Estas classes NÃO herdam de uma base comum!
class Impressora:
    def imprimir(self, documento: str) -> None:
        print(f"🖨️ Imprimindo: {documento}")


class TelaLCD:
    def imprimir(self, documento: str) -> None:
        print(f"📺 Exibindo na tela: {documento}")


class ArquivoLog:
    def imprimir(self, documento: str) -> None:
        print(f"📝 Gravando no log: {documento}")


# Duck typing: todos têm .imprimir(), então funciona!
def publicar(dispositivo, conteudo: str) -> None:
    """Não importa o tipo, só precisa ter .imprimir()"""
    dispositivo.imprimir(conteudo)


# Polimorfismo sem herança!
publicar(Impressora(), "Relatório Anual")
publicar(TelaLCD(), "Dashboard")
publicar(ArquivoLog(), "Erro 404")
