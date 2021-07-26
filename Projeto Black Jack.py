import random

def criarBaralho():
    baralho = []
    carta = []
    for i in range(1,14):
        if i == 1:
            carta = ['A', i]
            baralho.append(carta)
        elif i == 11:
            carta = ['J', 10]
            baralho.append(carta)
        elif i == 12:
            carta = ['Q', 10]
            baralho.append(carta)
        elif i == 13:
            carta = ['K', 10]
            baralho.append(carta)
        else:
            carta = [i, i]
            baralho.append(carta)
    return baralho

def sorteio(listaBaralho):
    return random.choice(listaBaralho)

def entradaValida(entrada):
    valido = True
    entradasValidas = ['S', 'N']
    if entrada not in entradasValidas:
        valido = False
        print("Jogada Inválida. Digite 'S' para Sim e 'N' para Não.")      
    return valido

def jogada(jogador, baralho):
    cartaSorteada = sorteio(baralho)
    jogadaInvalida = False
    while jogadaInvalida == False:
        if jogador[1] == 'A':
            continua = input(f"{jogador[0]}, você deseja tirar outra carta? S/N")
            jogadaInvalida = entradaValida(continua)
        if jogadaInvalida == True:
            if continua == 'N':
                jogador[1] = 'I'
            else:
                jogador[2] = jogador[2] + cartaSorteada[1]
                if jogador[2] == 21:
                    jogador[1] = 'I'
                    print(f"{jogador[0]}, sua carta foi {cartaSorteada[0]} e sua pontuação está em {jogador[2]} e você ganhou o jogo.")
                elif jogador[2] > 21:
                    jogador[1] = 'I'
                    print(f"{jogador[0]}, sua carta foi {cartaSorteada[0]} e sua pontuação está em {jogador[2]} e você perdeu o jogo.")
    return jogador, cartaSorteada  

def verifica(pontuacao):
    maiorNumero = 0
    maiorPosicao = ''
    for element in pontuacao:
        if element[2] <= 21:
            if element[2] > maiorNumero:
                maiorNumero = element[2]
                maiorPosicao = element[0]
                vencedor = f"{maiorPosicao}, você alcançou a maior pontuação." 
    return vencedor

def funcaoPrincipal ():
    baralho = criarBaralho()
    numeroJogadores = int(input("Quantos são os jogadores?"))
    n = 1
    nomeJogadores = []
    jogador = []

    while n <= numeroJogadores:
        nomeJogador = input(f"Qual o nome do {n}º jogador?")
        jogador = [nomeJogador, 'A', 0]
        nomeJogadores.append(jogador)
        n +=1

    cont=0
    while cont < len(nomeJogadores):
        while nomeJogadores[cont][1] == 'A':
            jogador, cartaSorteada  = jogada(nomeJogadores[cont], baralho)
            if nomeJogadores[cont][1] == 'I':
                cont+=1
                break
            else:
                print(f"{jogador[0]}, sua carta foi {cartaSorteada[0]} e sua pontuação está em {nomeJogadores[cont][2]}")
                nomeJogadores[cont][1] = jogador[1]
                nomeJogadores[cont][2] = jogador[2]            

    print(verifica(nomeJogadores))

funcaoPrincipal()