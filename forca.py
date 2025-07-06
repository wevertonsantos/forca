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
lista_palavra_secreta = ["_","_","_","_","_"]
letras_python = {"p":False,"y":False,"t":False,"h":False,"o":False,"n":False}
palavra = ""
erros = 0

while True:
    # verificando se palavra é diferente da palavra secreta
    if palavra != palavra_secreta:
        # entrada do usuario
        letra = input("Digite uma letra: ")
        print(palavra)
    else:
        print(f"Você achou a palavra correta: {palavra_secreta}")
        break
    # verificando se é apenas uma letra e se é do tipo string
    if len(letra) == 1 and letra.isalpha():
        # verificando se a letra está na palavra secreta
        if letra in palavra_secreta:
            letras_python[letra] = True
            # pegando cada letra do dic
            for letra in letras_python.keys():
                # verificando se a chave letra tem valor True
                if letras_python[letra] == True:
                    # pegando o índice de cada elemento do dicionário
                    indice_dic = list(letras_python.keys()).index(letra)
                    # colocando a letra na respectiva posição
                    lista_palavra_secreta[indice_dic] = letra
            for letra in lista_palavra_secreta:
                palavra += letra
            print(palavra)
        else:
            # acaba o programa caso tenha 6 erros
            if erros == 5:
                print("As tentativas acabaram. Fim de jogo!")
                break
            else:
                print(palavra)
                # aumenta o erro caso erre
                erros += 1
    else:
        print("Você enviou algo errado. Tente novamente!")