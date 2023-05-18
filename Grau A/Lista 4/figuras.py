import math

class FiguraGeometrica:
    def calcularArea(self):
        pass
    
    def calcularPerimetro(self):
        pass

class Retangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcularArea(self):
        return self.base * self.altura
    
    def calcularPerimetro(self):
        return 2 * (self.base + self.altura)


class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcularArea(self):
        return 0.5 * self.base * self.altura
    
    def calcularPerimetro(self):
        hipotenusa = math.sqrt(self.base**2 + self.altura**2)
        return self.base + self.altura + hipotenusa


class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio
    
    def calcularArea(self):
        return math.pi * self.raio**2
    
    def calcularPerimetro(self):
        return 2 * math.pi * self.raio


retangulo = Retangulo(5, 3)
area_retangulo = retangulo.calcularArea()
perimetro_retangulo = retangulo.calcularPerimetro()

triangulo = Triangulo(4, 6)
area_triangulo = triangulo.calcularArea()
perimetro_triangulo = triangulo.calcularPerimetro()

circulo = Circulo(2)
area_circulo = circulo.calcularArea()
perimetro_circulo = circulo.calcularPerimetro()

print("Retângulo:")
print("Área:", area_retangulo)
print("Perímetro:", perimetro_retangulo)

print('\n--------------------------\n')

print("Triângulo:")
print("Área:", area_triangulo)
print("Perímetro:", perimetro_triangulo)

print('\n--------------------------\n')

print("Círculo:")
print("Área:", area_circulo)
print("Circunferência:", perimetro_circulo)
