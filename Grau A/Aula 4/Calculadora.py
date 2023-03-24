class Calculadora():
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def somar(self):
        resultado = self.numero1 + self.numero2
        return resultado

    def subtrair(self):
        resultado = self.numero1 - self.numero2
        return resultado

    def multiplicar(self):
        resultado = self.numero1 * self.numero2
        return resultado

    def dividir(self):
        if self.numero2 == 0:
            print("Divisão por zero detectada!")
            return -1
        else:
            resultado = self.numero1 / self.numero2
            return resultado

numero1 = float(input(f"Digite o primeiro número: "))
numero2 = float(input(f"Digite o segundo número: "))
Calculo1 = Calculadora(numero1, numero2)

print(f'Calculo da soma: {Calculo1.somar():.2f}')
print(f'Calculo da subtração: {Calculo1.subtrair():.2f}')
print(f'Calculo da multiplicação: {Calculo1.multiplicar():.2f}')
print(f'Calculo da divisão: {Calculo1.dividir()}')


