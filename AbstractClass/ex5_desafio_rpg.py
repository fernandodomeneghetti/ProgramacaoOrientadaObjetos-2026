"""
Aula 11 — Exercício 5 (Desafio): Jogo RPG

Hierarquia:
                 Personagem (ABC)
               /       |        \\
        Guerreiro     Mago     Arqueiro

Personagem define o contrato: atacar(), defender() e habilidade_especial()
são abstratos; receber_dano() e vivo são concretos e compartilhados.

Execute: python ex5_desafio_rpg.py
"""
import random
from abc import ABC, abstractmethod


class Personagem(ABC):
    def __init__(self, nome: str, vida: int, ataque: int, defesa: int) -> None:
        self.nome = nome
        self._vida_max = vida
        self._vida = vida
        self._ataque = ataque
        self._defesa = defesa
        self._defendendo = False

    @property
    def vivo(self) -> bool:
        return self._vida > 0

    @property
    def vida(self) -> int:
        return self._vida

    @property
    @abstractmethod
    def classe(self) -> str: ...

    @abstractmethod
    def atacar(self) -> int:
        """Retorna o dano causado."""
        ...

    @abstractmethod
    def defender(self) -> str:
        """Prepara a defesa para o próximo ataque recebido."""
        ...

    @abstractmethod
    def habilidade_especial(self) -> str:
        """Usa habilidade especial."""
        ...

    def _reduzir_dano(self, dano: int) -> int:
        """Concreto (pode ser sobrescrito): redução padrão pela defesa."""
        if self._defendendo:
            self._defendendo = False
            return max(1, dano - self._defesa * 2)
        return max(1, dano - self._defesa)

    def receber_dano(self, dano: int) -> None:
        dano_real = self._reduzir_dano(dano)
        self._vida = max(0, self._vida - dano_real)
        print(f"  {self.nome} recebeu {dano_real} de dano! (Vida: {self._vida}/{self._vida_max})")

    def __str__(self) -> str:
        return f"[{self.classe}] {self.nome} | HP: {self._vida}/{self._vida_max} | ATK: {self._ataque}"


class Guerreiro(Personagem):
    @property
    def classe(self) -> str:
        return "Guerreiro"

    def atacar(self) -> int:
        dano = self._ataque + random.randint(1, 6)
        print(f"  ⚔️ {self.nome} ataca com espada! (Dano: {dano})")
        return dano

    def defender(self) -> str:
        self._defendendo = True
        return f"🛡️ {self.nome} levanta o escudo (defesa dobrada no próximo golpe)"

    def habilidade_especial(self) -> str:
        self._defesa += 5
        return f"🛡️ {self.nome} ativa Escudo de Ferro! (+5 defesa)"


class Mago(Personagem):
    @property
    def classe(self) -> str:
        return "Mago"

    def atacar(self) -> int:
        dano = self._ataque + random.randint(3, 12)
        print(f"  🔥 {self.nome} lança Bola de Fogo! (Dano: {dano})")
        return dano

    def defender(self) -> str:
        self._defendendo = True
        return f"🔮 {self.nome} conjura Barreira Arcana"

    def habilidade_especial(self) -> str:
        cura = 30
        self._vida = min(self._vida_max, self._vida + cura)
        return f"✨ {self.nome} usa Cura Mágica! (+{cura} HP)"


class Arqueiro(Personagem):
    @property
    def classe(self) -> str:
        return "Arqueiro"

    def atacar(self) -> int:
        critico = random.random() < 0.3  # 30% chance de crítico
        dano = self._ataque + random.randint(2, 8)
        if critico:
            dano *= 2
            print(f"  🎯 {self.nome} acerta um CRÍTICO! (Dano: {dano})")
        else:
            print(f"  🏹 {self.nome} dispara flecha! (Dano: {dano})")
        return dano

    def defender(self) -> str:
        self._defendendo = True
        return f"💨 {self.nome} se prepara para esquivar (50% de chance)"

    def _reduzir_dano(self, dano: int) -> int:
        """Sobrescrita: ao defender, o arqueiro pode esquivar totalmente."""
        if self._defendendo and random.random() < 0.5:
            self._defendendo = False
            print(f"  💨 {self.nome} esquivou!")
            return 0
        return super()._reduzir_dano(dano)

    def habilidade_especial(self) -> str:
        self._ataque += 3
        return f"🦅 {self.nome} ativa Olho de Águia! (+3 ataque)"


def batalha(p1: Personagem, p2: Personagem, max_turnos: int = 50) -> None:
    """Batalha por turnos: só usa o contrato de Personagem (polimorfismo)."""
    print(f"\n=== BATALHA: {p1.nome} vs {p2.nome} ===")
    atacante, alvo = p1, p2
    turno = 1
    while p1.vivo and p2.vivo and turno <= max_turnos:
        print(f"\n-- Turno {turno}: {atacante.nome} --")
        acao = random.choice(["atacar", "atacar", "atacar", "atacar", "defender", "especial"])
        if acao == "atacar":
            alvo.receber_dano(atacante.atacar())
        elif acao == "defender":
            print(f"  {atacante.defender()}")
        else:
            print(f"  {atacante.habilidade_especial()}")
        atacante, alvo = alvo, atacante
        turno += 1

    print()
    if p1.vivo and p2.vivo:
        print("⏱️ Empate por limite de turnos!")
    else:
        vencedor = p1 if p1.vivo else p2
        print(f"🏆 Vencedor: {vencedor}")


if __name__ == "__main__":
    guerreiro = Guerreiro("Arthur", vida=150, ataque=20, defesa=10)
    mago = Mago("Merlin", vida=80, ataque=25, defesa=3)
    arqueiro = Arqueiro("Legolas", vida=100, ataque=18, defesa=5)

    print("--- Equipe ---")
    for p in [guerreiro, mago, arqueiro]:
        print(f"  {p}")
        p.atacar()
        print(f"  {p.defender()}")
        print(f"  {p.habilidade_especial()}")
        print()

    batalha(
        Guerreiro("Boromir", vida=120, ataque=18, defesa=8),
        Mago("Saruman", vida=90, ataque=24, defesa=3),
    )

    print("\n--- Tentando instanciar Personagem ---")
    try:
        Personagem("Genérico", 10, 1, 1)
    except TypeError as erro:
        print(f"TypeError: {erro}")
