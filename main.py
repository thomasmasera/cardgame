from classi import Carta
from classi import Mazzo
from random import shuffle
nuovo = Mazzo

carte = []
for i in range(1, 10):
    for j in range(1, 4):
        carte.append(Carta(i, j))
shuffle(carte)
print(carte)