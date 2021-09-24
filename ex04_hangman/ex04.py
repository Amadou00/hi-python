import random

class Hangman():
    word:str
    letterFound = []
    vie:int
    red = '\033[91m'
    redS = '\33[41m'
    orange = '\33[33m'
    green = '\33[92m'
    end = '\033[0m'

    def randomWord(self):
        lstWord = ["poisson", "voiture", "dragon", "chevalier"]
        rdWord:int = random.randint(0, len(lstWord)-1)
        for i in range(len(lstWord[rdWord])):
            self.letterFound.insert(i, "_")

        self.word = lstWord[rdWord]

    def rulesPlaying(self, letterUser):
        lstLetters = list(self.word)
        letterGood = False
        count = 0
        for i in range(len(lstLetters)):
            if (letterUser == lstLetters[i]):
                self.letterFound[i] = letterUser
                letterGood = True
                count += 1

        if(letterGood != True):
            self.vie -= 1
            print(self.red + "Vous vous êtes trompé, nombre vies restante : " + self.end + str(self.vie))

    def game(self, nbVie:int):
        self.randomWord()
        self.vie = nbVie
        letterUser = str(input("\n" + self.orange + "Choisisez une lettre : " + self.end  + ' '.join(self.letterFound) + self.orange + "\ vie total : " + self.end + str(self.vie) + "\n"))

        while True and self.vie > 0:
            if(''.join(self.letterFound) == self.word):
                print(self.green + "Vous avez deviné le mot : " + self.end + self.word + "\n")
                break
            else:
                self.rulesPlaying(letterUser)
                letterUser = str(input(self.orange + "Choisisez une lettre : " + self.end + ' '.join(self.letterFound) + "\n"))
        else:
            print(self.red + "Vous avez perdu, le mot était : " + self.word + "\n" + self.end)

partie = Hangman().game(15)