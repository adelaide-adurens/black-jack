#JOGO BLACKJACK OU 21 - NÃO HÁ MESA E BARALHO É ÚNICO - OBJETIVO DO JOGO É COMPLETAR 21 PONTOS OU O MÁXIMO, SEM PASSAR DE 21, ENTRE O NÚMERO DE PARTICIPANTES

import random

#Função que cria o baralho com as cartas e respectivos valores para o jogo
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

#Função que sorteia uma carta do baralho
def sorteio(listaBaralho):
    return random.choice(listaBaralho)

#Função que valida o Sim ou Não para continuar a tirar cartas durante o jogo
def entradaValida(entrada):
    valido = True
    entradasValidas = ['S', 'N']
    if entrada not in entradasValidas:
        valido = False
        print("Jogada Inválida. Digite 'S' para Sim e 'N' para Não.\n")      
    return valido

#Função que verifica se o jogador ainda está ativo e se ainda quer tirar mais cartas e inativa o jogador caso ele some 21 pontos ou passe de 21.
def jogada(jogador, baralho):
    cartaSorteada = sorteio(baralho)
    jogadaInvalida = False
    while jogadaInvalida == False:
        if jogador[1] == 'A':
            continua = input(f"{jogador[0]}, você deseja tirar uma carta? S/N\n")
            jogadaInvalida = entradaValida(continua)
        if jogadaInvalida == True:
            if continua == 'N':
                jogador[1] = 'I'
            else:
                jogador[2] = jogador[2] + cartaSorteada[1]
                if jogador[2] == 21:
                    jogador[1] = 'I'
                    print(f"{jogador[0]}, sua carta foi {cartaSorteada[0]} e sua pontuação está em {jogador[2]} e você ganhou o jogo.\n")
                elif jogador[2] > 21:
                    jogador[1] = 'I'
                    print(f"{jogador[0]}, sua carta foi {cartaSorteada[0]} e sua pontuação está em {jogador[2]} e você perdeu o jogo.\n")
    return jogador, cartaSorteada  

#Função que verifica qual jogador tirou 21 pontos ou o que alcançou mais pontos durante as jogadas
def verifica(pontuacao):
    maiorNumero = 0
    maiorPosicao = ''
    for element in pontuacao:
        if element[2] <= 21:
            if element[2] > maiorNumero:
                maiorNumero = element[2]
                maiorPosicao = element[0]
                vencedor = f"{maiorPosicao}, você alcançou a maior pontuação.\n" 
            elif element[2] == maiorNumero:
                vencedor += f"{element[0]}, você também alcançou a maior pontuação.\n" 
    return vencedor

#Função prinicpal que pede o número e nome de jogadores e chama as demais funções para que o jogo aconteceça
def __main__():
    baralho = criarBaralho()
    numeroJogadores = int(input("Quantos são os jogadores?\n"))
    n = 1
    nomeJogadores = []
    jogador = []

    while n <= numeroJogadores:
        nomeJogador = input(f"Qual o nome do {n}º jogador?\n")
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
                print(f"{jogador[0]}, sua carta foi {cartaSorteada[0]} e sua pontuação está em {nomeJogadores[cont][2]}\n")
                nomeJogadores[cont][1] = jogador[1]
                nomeJogadores[cont][2] = jogador[2]            

    print(verifica(nomeJogadores))

if __name__ =="__main__":
    __main__()