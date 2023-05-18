class Criptografia:
    def cifrar(self, texto):
        pass

    def decifrar(self, texto_cifrado):
        pass


class CifraCesar(Criptografia):
    def __init__(self, deslocamento):
        self.deslocamento = deslocamento

    def cifrar(self, texto):
        texto_cifrado = ""
        for char in texto:
            if char.isalpha():
                char_cifrado = chr((ord(char) - ord('a') + self.deslocamento) % 26 + ord('a'))
                texto_cifrado += char_cifrado
            else:
                texto_cifrado += char
        return texto_cifrado

    def decifrar(self, texto_cifrado):
        texto_decifrado = ""
        for char in texto_cifrado:
            if char.isalpha():
                char_decifrado = chr((ord(char) - ord('a') - self.deslocamento) % 26 + ord('a'))
                texto_decifrado += char_decifrado
            else:
                texto_decifrado += char
        return texto_decifrado


class CifraXor(Criptografia):
    def __init__(self, chave):
        self.chave = chave

    def cifrar(self, texto):
        texto_cifrado = ""
        for char in texto:
            char_cifrado = chr(ord(char) ^ self.chave)
            texto_cifrado += char_cifrado
        return texto_cifrado

    def decifrar(self, texto_cifrado):
        texto_decifrado = ""
        for char in texto_cifrado:
            char_decifrado = chr(ord(char) ^ self.chave)
            texto_decifrado += char_decifrado
        return texto_decifrado


cesar = CifraCesar(3)
texto_original = "Hello world!"
texto_cifrado = cesar.cifrar(texto_original)
texto_decifrado = cesar.decifrar(texto_cifrado)

print("Cesar")
print("Texto original:", texto_original)
print("Texto cifrado:", texto_cifrado)
print("Texto decifrado:", texto_decifrado)

print("\n--------------------------\n")

xor = CifraXor(7)
texto_original = "Hello world!"
texto_cifrado = xor.cifrar(texto_original)
texto_decifrado = xor.decifrar(texto_cifrado)

print("Xor")
print("Texto original:", texto_original)
print("Texto cifrado:", texto_cifrado)
print("Texto decifrado:", texto_decifrado)
