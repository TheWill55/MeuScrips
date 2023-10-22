import random

# Definindo as imagens
imagens = ['imagem1', 'imagem2', 'imagem3', 'imagem4', 'imagem5']

def girar_barra():
    return [random.choice(imagens) for _ in range(3)]

def verificar_premio(barras):
    if barras[0] == barras[1] == barras[2]:
        return True
    else:
        return False

def jogo_aposta():
    saldo = 1000  # Saldo inicial do jogador

    while saldo > 0:
        print(f"Seu saldo atual é: {saldo}")
        aposta = int(input("Digite o valor da sua aposta: "))

        if aposta > saldo:
            print("Aposta inválida. Você não tem saldo suficiente.")
            continue

        barras = girar_barra()
        print(f"Barras: {barras}")

        if verificar_premio(barras):
            premio = aposta * 10  # Exemplo de prêmio, pode ser ajustado
            saldo += premio
            print(f"Você ganhou! Prêmio: {premio}")
        else:
            saldo -= aposta
            print("Você perdeu.")

    print("Seu saldo chegou a zero. Fim do jogo.")

# Iniciar o jogo
jogo_aposta()
