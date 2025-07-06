"""
O programa escolhe uma palavra secreta (pode ser fixada no código ou sorteada de uma lista).

O jogador tenta adivinhar essa palavra letra por letra.

Para cada letra correta, o programa revela a letra na posição correta na palavra.

Para cada letra errada, o programa registra um erro.

O jogador tem um número limitado de erros (exemplo: 6 chances).

Se o jogador adivinhar todas as letras antes de acabar as chances, ele vence.

Se acabar as chances antes de descobrir a palavra, perde.
"""

# variável com a palavra secreta
palavra_secreta = "python"
lista_palavra_secreta = ["_","_","_","_","_","_"]
palavra = ''.join(lista_palavra_secreta)
erros = 0

# conjunto para armazenar letras já tentadas
letras_tentadas = set()

while True:
    # verificando se palavra é diferente da palavra secreta
    if palavra != palavra_secreta:
        # entrada do usuario
        letra = input("Digite uma letra: ").lower().strip()
    else:
        print(f"Você achou a palavra correta: {palavra_secreta}")
        break

    # verificando se é apenas uma letra e se é do tipo string
    if len(letra) == 1 and letra.isalpha():

        # verifica se já tentou a letra
        if letra in letras_tentadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        letras_tentadas.add(letra)  # registra a letra

        # verificando se a letra está na palavra secreta
        if letra in palavra_secreta:
            # atualizando todas as posições da letra correta
            for i, l in enumerate(palavra_secreta):
                if l == letra:
                    lista_palavra_secreta[i] = letra
            # atualizando a string "palavra"
            palavra = ''.join(lista_palavra_secreta)
            print("Palavra: ", ' '.join(lista_palavra_secreta))
        else:
            erros += 1
            # acaba o programa caso tenha 6 erros
            if erros == 6:
                print("As tentativas acabaram. Fim de jogo!")
                break
            else:
                print("\nLetra errada.")
                print("Palavra:", ' '.join(lista_palavra_secreta))
                print(f"Tentativas restantes: {6 - erros}")
    else:
        print("Você enviou algo errado. Tente digitar apenas uma letra do alfabeto.")