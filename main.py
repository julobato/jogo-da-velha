#!/usr/bin/env python3
# -*- coding: utf-8 -*-

XIS = 1
ZERO = 2
VAZIO = 0

def main():
    tabuleiro = [VAZIO]*9 
    cont = 1 #checar de quem é a vez
    acabou = False
    while not acabou:
        jogada = int(input("Digite a jogada: "))
        if 0 < jogada < 10: # checa se a posição for válida (de 1 a 9)
            if tabuleiro[jogada-1] == VAZIO: # checa se a posição está vazia
                if cont%2 == 0: 
                    tabuleiro[jogada-1] = ZERO
                else:
                    tabuleiro[jogada-1] = XIS
                cont+=1 # a vez só é passada se a posição for válida
            else:
                print("\nJogada inválida! A posição já está preenchida\n")
        else:
            print("\nJogada inválida! A jogada deve ser entre 1 e 9!\n")
        if cont%2 == 1:
            ganhador,acabou = checa_fim_de_jogo(tabuleiro,ZERO)
        else:
            ganhador,acabou = checa_fim_de_jogo(tabuleiro,XIS)
        printa_tabuleiro(tabuleiro)

def checa_fim_de_jogo(tabuleiro,jogador):
    i = 0
    #checa linhas:
    while i < 9:
        if tabuleiro[i] == jogador:
            if tabuleiro[i+1] == jogador:
                if tabuleiro[i+2] == jogador:
                    print("\n Fim de jogo! \n O jogador %d venceu!\n" %(jogador))
                    return jogador,True
        i+=3
        
    i = 0
    #checa colunas:
    while i < 3:
        if tabuleiro[i] ==  jogador:
            if tabuleiro[i+3] == jogador:
                if tabuleiro[i+6] == jogador:
                    print("\n Fim de jogo! \n O jogador %d venceu!\n" %(jogador))
                    return jogador,True
        i+=1
        
    #checa diagonais:
    if tabuleiro[4] == jogador:
        if tabuleiro[0] == jogador:
            if tabuleiro[8] == jogador:
                print("\n Fim de jogo! \n O jogador %d venceu!\n" %(jogador))
                return jogador,True
        if tabuleiro[2] == jogador:
            if tabuleiro[6] == jogador:
                print("\n Fim de jogo! \n O jogador %d venceu!\n" %(jogador))
                return jogador,True
            
    #caso todas as posições estejam preenchidas, é dado empate
    i = 0
    while i < 9:
        if tabuleiro[i] != VAZIO:
            if i == 8:
                return 0, True
            i+=1
        else:
            return 0, False
        
    return 0,False
    
def printa_tabuleiro(tabuleiro):
    s = ''
    for i in range(0,3):
        if tabuleiro[i] == XIS:
            s+= " x "
        elif tabuleiro[i] == ZERO:
            s+= " o "
        elif tabuleiro[i] == VAZIO:
            s+= "   "
        if i != 2:
            s+="|"
    print(s)
    print("-----------")
    s=''
    for i in range(3,6):
        if tabuleiro[i] == XIS:
            s+= " x "
        elif tabuleiro[i] == ZERO:
            s+= " o "
        elif tabuleiro[i] == VAZIO:
            s+= "   "
        if i != 5:
            s+="|"
    print(s)
    s=''
    print("-----------")
    for i in range(6,9):
        if tabuleiro[i] == XIS:
            s+= " x "
        elif tabuleiro[i] == ZERO:
            s+= " o "
        elif tabuleiro[i] == VAZIO:
            s+= "   "
        if i != 8:
            s+="|"
    print(s)
            

main()    

if __name__ == 'main':
    main()
