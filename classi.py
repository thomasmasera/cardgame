class Carta:
    seme = ["cuori", "quadri", "fiori", "picche"]
    valore = [None, "asso", "due", "tre", "quattro", "cinque", "sei", "sette", "gobbo", "donna", "re"]
    
    def __init__(self, seme, valore):
        self.seme = seme
        self. valore = valore
    
    def minoredi(self, c2):
        if self.valore < c2.valore:
            return True
        if self.valore == c2.valore:
            if self.seme < c2.seme:
                return True
            else:
                return False
    
    def maggioredi(self, c2):
        if self.valore > c2.valore:
            return True
        if self.valore == c2.valore:
            if self.seme > c2.seme:
                return True
            else:
                return False
            
    def nome(self):
        n = self.valore[self.valore] + " of " + self.seme[self.seme]
        return n
    
from random import shuffle

class Mazzo:
    def __init__(self):
        self.carte = []
        for i in range(1, 10):
            for j in range(1, 4):
                self.carte.append(Carta(i, j))
        shuffle(self.carte)

    def rimaste(self):
        if len(self.carte) == 0:
            return
        return self.carte.pop()


class Giocatore:
    def __init__(self, nome):
        self.nome = nome
        self.vittorie = 0
        self.carta = None

class partita:
    def __init__(self):
        nome1 = input("nome del giocatore 1")
        nome2 = input("nome del giocatore 2")
        self.mazzo = Mazzo
        self.g1 = Giocatore(nome1)
        self.g2 = Giocatore(nome2)

    def vittorie(self, vincitore):
        v = "{} ha vinto la partita"
        v = v.format(vincitore)
        print(v)

    def pesca(self, g1nome, g1carta, g2nome, g2carta):
        p = "{} ha pescato {} {} ha pescato {}"
        p = p.format(g1nome, g1carta, g2nome, g2carta)
        print(p)

    def gioca_partita(self):
        carte = self.mazzo.carte
        print("inizia la partita")
        while len(carte) >= 2:
            m = "premi e per uscire, una tasto qualsiasi per continuare"
            risposta = input(m)
            if risposta == "e":
                break
        g1carta = self.mazzo.rimaste()
        g2carta = self.mazzo.rimaste()
        g1nome = self.g1.nome
        g2nome = self.g2.nome
        self.pesca(g1nome, g1carta, g2nome, g2carta)
        if g1carta > g2carta:
            self.g1.vittorie += 1
            self.vittorie(self.g1.nome)
        else:
            self.g2.vittorie += 1
            self.vittorie(self.g2.nome)

        # vittoria = self.vincitore(self.g1, self.g2)
        # print("la partita è finita. {} ha vinto!".format(vittoria))
        
        # def vincitore(self, g1, g2):
        #     if p1.vittorie 

    

