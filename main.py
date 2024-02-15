# Specifikācija
# - 1pt Spelētāji sāk no lauciņa nr. 1, vispār 100 lauciņu. Ir divi spēlētāji. Vinē tas kurš pirmais sasniedz pēdējo lauciņu
# - 1pt Maksimāli - 25 raundi, ja beidzas raundi - neizšķirts
# - 1pt Viens pēc otra met kauliņu (ar nejauša ciparu ģenerātora palidzību) un iet uz priekšu
# - 1pt Ja trāpa uz lauciņu ar kāpnem:
# -- zilas kāpnes ved uz leju, 18 -> 7, 67 -> 46 , 80 -> 69, 74 -> 63
# -- sarkanas kāpnes ved uz augšu, 15 -> 24, 39 -> 48, 33 -> 52, 87 -> 96 
# - 1pt Katrā raundā tik drukāta informācija kur atrodas spēlētājs, dators un vai ir uzkāpts uz kāpnem

# Koda vertēšanas kritēriji
# - 1pt Kodā izmanto mainīgus, ciklus (for vai while), zarošanu (if)
# - 1pt Kods strādā bez kļūdam
# - 1pt Mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# - 1pt Kodam ir jēdzīgi komentāri, pirms "if, for" koda konstrukcijam
# - 1pt Izmaiņas saglabātas versiju vadības sistēmā Git

# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git

#Artjoms Petrovs

import random

player1 = 1
player2 = 1
# raundi 
for x in range(30):
    input("player 1 your turn: ")
    
    #spēlētāja 1 gājiens
    player1 = player1 + random.randint(1,6)
    print(player1)


    input("player 2 your turn: ")
    
    #spēlētāja 2 gājiens
    player2 = player2 + random.randint(1,6)
    print(player2)
    
    # -- zilas kāpnes ved uz leju, 18 -> 7, 67 -> 46 , 80 -> 69, 74 -> 63
    if player2 == 18:
        player2 = 7
        print("player 2 moves to 7")
    elif player2 == 67:
        player2 = 46
        print("player 2 moves to 46")
    elif player2 == 80:
        player2 = 69
        print("player 2 moves to 69")
    elif player2 == 74:
        player2 = 63
        print("player 2 moves to 63")
    # -- sarkanas kāpnes ved uz augšu, 15 -> 24, 39 -> 48, 33 -> 52, 87 -> 96 
    elif player2 == 15:
        player2 = 24
        print("player 2 moves to 24")
    elif player2 == 39:
        player2 = 48
        print("player 2 moves to 48")
    elif player2 == 33:
        player2 = 52
        print("player 2 moves to 52")
    elif player2 == 87:
        player2 = 96
        print("player 2 moves to 96")
    # -- zilas kāpnes ved uz leju, 18 -> 7, 67 -> 46 , 80 -> 69, 74 -> 63
    if player1 == 18:
        player1 = 7
        print("player 1 moves to 7")
    elif player1 == 67:
        player1 = 46
        print("player 1 moves to 46")
    elif player1 == 80:
        player1 = 69
        print("player 1 moves to 69")
    elif player1 == 74:
        player1 = 63
        print("player 1 moves to 63")
    # -- sarkanas kāpnes ved uz augšu, 15 -> 24, 39 -> 48, 33 -> 52, 87 -> 96
    elif player1 == 15:
        player1 = 24
        print("player 1 moves to 24")
    elif player1 == 39:
        player1 = 48
        print("player 1 moves to 48")
    elif player1 == 33:
        player1 = 52
        print("player 1 moves to 52")
    elif player1 == 87:
        player1 = 96
        print("player 1 moves to 96")
        
    #pārbaudījums, lai noskaidrotu, kurš uzvar.
    if player2 >= 100:
        print("player 2 wins")
        break
    
    #pārbaudījums, lai noskaidrotu, kurš uzvar.
    if player1 >= 100:
        print("player 1 wins")
        break
    

#pārbaudījums, ja beidzas raundi - neizšķirts
if player2 < 100 and player1 < 100:
    print("draw")






