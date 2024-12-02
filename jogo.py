import random

def jogar():
    print("Bem-vindo ao jogo de ADVINHE O NÚMERO!")
    print("Tente adivinhar o número entre 1 e 100.")

    # Gerar um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    while not acertou:
        # Receber o palpite do jogador
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        # Verificar o palpite
        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            acertou = True
        elif palpite < numero_secreto:
            print("O número é maior!")
        else:
            print("O número é menor!")

if __name__ == "__main__":
    jogar()
