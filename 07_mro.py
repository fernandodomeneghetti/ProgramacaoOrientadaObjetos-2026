"""
Aula 10 — Seção 6.1 — MRO (Method Resolution Order)

Execute: python 07_mro.py
"""

class A:
    def metodo(self):
        print("A")

class B(A):
    def metodo(self):
        print("B")

class C(A):
    def metodo(self):
        print("C")

class D(B, C):
    pass


d = D()
d.metodo()  # B (segue o MRO)

# Ver o MRO
print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
