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

palavra = []
erros = 1

while True:
    # entrada do usuario
    letra = input("Digite uma letra: ")
    # verificando se é apenas uma letra e se é do tipo string
    if len(letra) == 1 and letra.isalpha():
        # verificando se a letra está na palavra secreta
        if letra in palavra_secreta:
            ...
        else:
            # acaba o programa caso tenha 6 erros
            if erros == 6:
                print("As tentativas acabaram. Fim de jogo!")
                break
            else:
                # aumenta o erro caso erre
                erros += 1
    else:
        print("Você enviou algo errado. Tente novamente!")