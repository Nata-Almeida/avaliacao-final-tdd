

def trocar_vogais(palavra):




    palavra = palavra.replace("@", "a")
    palavra = palavra.replace("&", "e")
    palavra = palavra.replace("!", "i")
    palavra = palavra.replace("#", "o")
    palavra = palavra.replace("*", "u")

    return palavra

palavra = str(input("digite uma palavra: "))


print(trocar_vogais(palavra))

