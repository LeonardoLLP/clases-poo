class Palindromo():
    def __init__(self, text: str):
        self.text = text

    def test(self):
        back_text = self.text[::-1]
        if self.text.casefold() == back_text.casefold():
            return True
        else:
            return False


    def esPalindromo(text: str):
        back_text = text[::-1]
        if text.casefold() == back_text.casefold():
            return True
        else:
            return False

    # Creo que el codigo muestra la frase cuando el garbage collector recoge el objeto.
    def __del__(self):
        print(self.text.upper())


p = Palindromo("radar") 
print(p.test()) 

p = Palindromo("sonar") 
print(p.test())