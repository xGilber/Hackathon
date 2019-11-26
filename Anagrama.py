


import string as s


def anagrama(frase):
    s.ascii_letters
    for x in frase:
        if not x in s.ascii_letters:
            if not x.isspace():
                return 'erro'
        else:
            continue
   




    with open('palavras.txt') as f:
            texto = f.read().splitlines()
        
    final = list()
    frase = frase.upper().split(' ')
        
    for palavra in frase:

        novo = ''.join(sorted(palavra)).upper()

        for x in texto:

            li = ''.join(sorted(str(x)))

            if novo == li:
                final.append(x)
            
        
    return final
    

anagra = input("Digite a palavra desejada")

while (anagra.isalpha() != True):
    anagra = input('Digite APENAS LETRAS').replace(" ", "")

print(anagrama(anagra))

