class Palindromo():
    def esPalindromo(text: str):
        back_text = text[::-1]
        if text.casefold() == back_text.casefold():
            return True
        else:
            return False




print(Palindromo.esPalindromo('radar'))
print(Palindromo.esPalindromo('sonar'))
print(Palindromo.esPalindromo('Arde ya la yedra'))
print(Palindromo.esPalindromo('Ardeyalayedra'))
print(Palindromo.esPalindromo('!@#$% %$#@!'))