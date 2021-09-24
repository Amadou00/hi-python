import random

class RPS:
    mouvChoices = ["Rock", "Paper", "Scissors"]

    def testMouv(self, mouv:int) -> int:
        global mouvName
        global randomMouv
        
        while True:
            try:
                if (self.mouvChoices[mouv-1]):
                    mouvName = self.mouvChoices[mouv-1]
                    randomMouv = random.randint(0, 2)
                    break
                    
            except IndexError:
                mouv:int = int(input("Le mouvement que vous venez d'effectué n'est pas valide\n"))

        return randomMouv

    def rulesFight(self, mouvPlayer:int, mouvComputer:int) -> str :
        resultFight = ["gagner", "perdu", "égalité"]
        mouvPlayer = mouvPlayer - 1
        global res

        if (mouvPlayer == mouvComputer):
            res = resultFight[2]

        elif (mouvPlayer == 0 and mouvComputer == 2):
            res = resultFight[0]

        elif(mouvPlayer == 1 and mouvComputer == 0):
            res = resultFight[0]
        
        elif(mouvPlayer == 2 and mouvComputer == 1):
            res = resultFight[0]

        else:
            res = resultFight[1]

        return res

    def game(self):
        mouv:int = int(input("\nVeuillez choisir entre 1(Rock), 2(Paper) et 3(Scissors)\n"))
        randomMouv:int = self.testMouv(mouv)
        res:str = self.rulesFight(mouv, randomMouv)
        print("Joueur: " + str(self.mouvChoices[mouv-1]) + " / Ordinateur: " + str(self.mouvChoices[randomMouv]) + "\n\n Vous avez " + res + "\n")

partie = RPS()
partie.game()

