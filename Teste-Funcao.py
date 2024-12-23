win = int(input("Escreva a quantidade de vitórias: "))
loss = int(input("Escreva a quantidade de derrotas: "))

def rankedMmr(wins,losses):
    mmr = wins - losses
    rank = "Indefinido"
    if mmr < 10:
        rank = "Ferro"
    elif mmr < 21:
        rank = "Bronze"
    elif mmr < 51:
        rank = "Prata"
    elif mmr < 81:
        rank = "Ouro"
    elif mmr < 91:
        rank = "Diamante"
    elif mmr < 101:
        rank = "Lendário"
    else:
        rank = "Imortal"
    return rank

def mmr(wins, losses):
    mmr = wins - losses
    return mmr

print(f"o herói tem de saldo",mmr(win, loss),"está no nível",rankedMmr(win,loss))