from time import sleep
import random

def check_win(ans1, ans2):
    global wins
    global draws
    global loses

    print(f"\nVocê jogou {ans1} e seu adversário jogou {ans2}")

    if ans1 == "pedra":
        if ans2 == "pedra":
            draws += 1
            print(draw)
        if ans2 == "papel":
            loses += 1
            print(lose)
        if ans2 == "tesoura":
            wins += 1
            print(win)

    elif ans1 == "papel":
        if ans2 == "pedra":
            wins += 1
            print(win)        
        if ans2 == "papel":
            draws += 1
            print(draw)
        if ans2 == "tesoura":
            loses += 1
            print(lose)

    elif ans1 == "tesoura":
        if ans2 == "pedra":
            loses += 1
            print(lose)
        if ans2 == "papel":
            wins += 1
            print(win)
        if ans2 == "tesoura":
            draws += 1
            print(draw)

def choose():
    player_ans = input("\nEscolha um: \n    1) Pedra \n    2) Papel \n    3) Tesoura \n")
    if player_ans == "1":
        return "pedra"
    elif player_ans == "2":
        return "papel"
    elif player_ans == "3":
        return "tesoura"
    else:
        print("\nResposta inválida. Escolha 1, 2 ou 3.\n")
        return "invalid"

def game():
    while True:
        player_ans = choose()
        if player_ans != "invalid":
            break

    game_ans = random.choice(["pedra", "papel", "tesoura"])

    print()

    for i in range(1, 4):
        print(f"{i}..."); sleep(0.5)

    check_win(player_ans, game_ans)
    print()
    print(f"vitórias: {wins}")
    print(f"empates: {draws}")
    print(f"derrotas: {loses}")
    print()

win = "Você ganhou!"
lose = "Você perdeu!"
draw = "Empate!"

wins = 0
loses = 0
draws = 0

ans = input("Jogar pedra, papel, tesoura? s|n \n")
if ans.lower() == "s" or ans.lower() == "sim":
    game()
    while True:
        ans = input("Quer jogar denovo? s|n \n")
        if ans.lower() == "s" or ans.lower() == "sim":
            game()
        else:
            break