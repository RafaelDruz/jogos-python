import random

def jogar():

    secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000
    print("Qual o nível de dificuldade (1)(2)(3)?")
    nivel = int(input("Defina o nível: "))
    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5
    for rodada in range(1, tentativas + 1):
        print(f'Tentativa {rodada} de {tentativas}')
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)
        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
        acertou = chute == secreto
        maior = chute > secreto
        menor = chute < secreto
        if(acertou):
            print(f'Você acertou e fez {pontos} pontos!')
            break
        else:
            perdidos = abs(secreto - chute)
            pontos = pontos - perdidos
            if(maior):
                print("O seu chute foi maior que o número secreto")
                if (rodada == tentativas):
                    print(f'O número secreto era {secreto}. Você fez {pontos}')
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                if (rodada == tentativas):
                    print(f'O número secreto era {secreto}. Você fez {pontos}')
    print("Fim do jogo")
if(__name__ == '__main__'):
    jogar()