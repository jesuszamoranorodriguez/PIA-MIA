# E4.5 · Clase abstracta Figura con area() y perimetro(); implementa Circulo, Rectangulo y Cuadrado.
from abc import ABC, abstractmethod
from math import pi

class Figura(ABC):

    @abstractmethod
    def area(self, x, y):
        ...

    @abstractmethod
    def perimetro(self, x, y): ...


class Circulo(Figura):

    def __init__(self, radio):
        self._radio = radio


    def perimetro(self):
        return pi * self._radio * 2

    def area(self):
        return pi * (self._radio ** 2)


class Rectangulo(Figura):

    def __init__(self, base, altura):
        self._base = base
        self._altura = altura

    def perimetro(self):
        return 2* self._base + 2 * self._altura

    def area(self):
        return self._base * self._altura

class Cuadrado(Figura):

    def __init__(self, lado):
        self._lado = lado

    def perimetro(self):
        return self._lado + self._lado + self._lado + self._lado

    def area(self):
        return self._lado * self._lado


circu = Circulo(5)

print(circu.area())
print(circu.perimetro())
