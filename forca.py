def mostrar_estado_do_jogo(lista_palavra_secreta, letras_tentadas, erros, max_erros):
    # mostra palavra com espaços, letras tentadas e erros
    print("Palavra:", ' '.join(lista_palavra_secreta))
    print(f"Tentativas restantes: {6 - erros}")

def obter_letra(letras_tentadas):
     while True:
        letra = input("Digite uma letra: ").lower().strip()
        if len(letra) != 1 or not letra.isalpha():
            print("Entrada inválida. Digite apenas uma letra do alfabeto.")
        elif letra in letras_tentadas:
            print("Você já tentou essa letra. Tente outra.")
        else:
            return letra
        
def atualizar_palavra(palavra_secreta, lista_palavra_secreta, letra):
    for i, l in enumerate(palavra_secreta):
        if l == letra:
            lista_palavra_secreta[i] = letra

def verificar_vitoria(lista_palavra_secreta, palavra_secreta):
    return ''.join(lista_palavra_secreta) == palavra_secreta

def jogar_forca():
    palavra_secreta = "python"
    lista_palavra_secreta = ["_"] * len(palavra_secreta)
    letras_tentadas = set()
    erros = 0
    max_erros = 6

    while True:
        if verificar_vitoria(lista_palavra_secreta, palavra_secreta):
            print(f"Parabéns! Você descobriu a palavra: {palavra_secreta}")
            break

        if erros >= max_erros:
            print(f"Fim de jogo. A palavra era: {palavra_secreta}")
            break

        letra = obter_letra(letras_tentadas)
        letras_tentadas.add(letra)

        if letra in palavra_secreta:
            atualizar_palavra(palavra_secreta, lista_palavra_secreta, letra)
            print("Letra correta!")
        else:
            erros += 1
            print("Letra errada!")
        
        mostrar_estado_do_jogo(lista_palavra_secreta, letras_tentadas, erros, max_erros)

jogar_forca()