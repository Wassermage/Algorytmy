from random import randint
from Queue import Queue


def playHotPotato(players):
    q = Queue()

    for player in players:
        q.enqueue(player)
    
    while q.size() > 1:
        q.rotate(randint(q.size()*2, q.size()*3))
        print(f"Gracz {q.dequeue()} odpada z gry.")

    winner = q.dequeue()
    print(f"Gracz {winner} zwyciezyl!")
    return winner

playHotPotato(["Adam", "Grzesiek", "Janek", "Wojtek"])