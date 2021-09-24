import random

class GuessingGame :
    randomNb:int
    red = '\033[91m'
    redS = '\33[41m'
    orange = '\33[33m'
    green = '\33[92m'
    end = '\033[0m'

    def clue(self, number:int):
        if (self.randomNb - number > 30 and self.randomNb - number < 60 or number - self.randomNb > 30 and number - self.randomNb < 60):
            print(self.red + "Vous êtes trop loin, ajoutez ou retirer quelques dizaines sur ton chiffre\n" + self.end)

        elif (self.randomNb - number >= 20 and self.randomNb - number <= 30 or number - self.randomNb >= 20 and number - self.randomNb <= 30):
            print(self.red + "Vous y êtes presque, mais votre chiffre est trop éloigné\n" + self.end)

        elif (self.randomNb - number > 10 and self.randomNb - number < 20 or number - self.randomNb > 10 and number - self.randomNb < 20):
            print(self.orange + "Vous êtes proche de deviner le nombre, ajoutez ou retirer encore un peu sur votre chiffre ;)\n" + self.end)

        elif (self.randomNb - number >= 1 and self.randomNb - number <= 10 or number - self.randomNb >= 1 and number - self.randomNb <= 10):
            print(self.orange + "Vous bruler, vous êtes proche de la vérité\n" + self.end)

        else:
            print(self.redS + "Je peux te tutoyer? T'es beaucoup trop loin, c'est inquiétant \nTu peux réessayer Roronoa Zorro" + self.end)

    def game(self, minRange, maxRange):
        self.randomNb = random.randint(minRange, maxRange)
        number:int = int(input("\nVeuillez choisir un chiffre entre " + str(minRange) + " et " + str(maxRange) + ":\n"))
        while True:

            if (number == self.randomNb):
                print(self.green + "Bien joué ! La réponse était bien " + str(self.randomNb) + self.end + " \n")
                break

            else:
                self.clue(number)
                number:int = int(input("\nVeuillez choisir un chiffre entre " + str(minRange) + " et " + str(maxRange) + ":\n"))

partie = GuessingGame().game(0, 500)
