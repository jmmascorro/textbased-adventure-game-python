import logging

logging.basicConfig(filename="logfile.log", level=logging.DEBUG)

class Player:
    def __init__(self, name="", turns=5, inventory=[]):
        self._name = name
        self.turns = turns
        self.inventory = inventory
    
    @property
    def get_Name(self):  
        return self._name

    def set_Name(self, value):
        self._name = value

player1 = Player()

def trek():
    print("You start heading down the mountain, following behind Dorian.")
    print("It's dark and cold as you slowly trek down the moutain")
    print("You're exhausted and and hungry.")
    player1.turns = player1.turns - 1
    print("Life = ", player1.turns)
    print("")
    print("You finally make it to the bottom of the moutain") 
    print("Dorian: Finally, off this mountain, lets see if we can find any other survivors.")
    print("As you walk along the new terrain, snow and ice seem to be prevalent on this planet.")
    print("Suddenly you hear light cracking underneath your feet and realize you are walking on a frozen body of water.")
    print("")
    print("Dorian: We're walking on some type of frozen lake. We are already half way across.")
    answer = (input("Should we continue to the other side or turn back? (continue/back): ")).lower()
    if answer == "continue":
        print("Dorian: Okay, let's carefully pace ourseslves off this ice.")
        print("You almost make it to the end of the lake when you the ice underneath you begins breaking apart.")
        print("")

def shelter():
    print("Dorian: Okay, I might of seen a cave on my way here from where I crashed.")
    print("You follow Dorian to the cave and enter the dark cold opening.")
    print("Suddenly, you hear a loud shrieking coming from inside the cave.")
    print("")
    answer = (input("Do you continue in the cave to investigate or turn around to trek down the moutain? (investigate/trek): ")).lower()
    if answer == "investigate":
        print("Dorian: I wonder what that was? Let's continue into this cave and hope it's not anything we can't handle.")
        print("Dorian lights a torch and you continue into the cave away from the outside cold and happen upon two large wolf-like creatures.")
        if ("pistol" in player1.inventory):
            print("Without hesitation, you get the pistol out and blow two bullets through one of the creatures.")
            print("Dorian takes out another pistol and blasts two bullets through the other beast.")
            print("")
        else:
            print("Dorian takes out pistol and blows two bullets into one of the creatures as the other leaps toward you knocking you to the ground.")
            print("You lay on the ground bleeding as Dorian blasts two bullets through the beast.")
            player1.turns = player1.turns - 1
            print("Life = ", player1.turns)
        print("Dorian: Phew, that was a close one. I'm thinking a little too close. Let's get out of this cave, while we still can.")
        print("")
        trek()
    elif answer == "trek":
            trek() 

def main():
    logging.info("The game started")
    print("Welcome to the adventure game!")
    print("Life = ", player1.turns)
    print("The year is 3010...A deluge of massive Astroids impacted Earth and destroyed most life forms and almost pushed the human race to extinction.")
    print("THE FEW as we call ourselves, ventured into the dark abyss of space in an interstellar spacecraft, named The Savior, carrying selected families and civilians to colonize the Alpha Centauri planetary system.")
    print("Before our reach to our destination, an alien robot breached the Savior's hull. Forced to evacuate the mothership in numerous short-range Alpha spacecrafts, scores of colonists crash on a nearby habitable planet.")
    print("You emerge from a what felt as a deep sleep and are woken by an umfamiliar voice and a forceful sudden shake....")
    print("")
    print("Wake Up, Are you alright?")
    print("You finally are able to focus and make sense of your surroundings.")
    print("Good, you're awake. I am Dorian Bates.")
    player1.set_Name(input("What is your name? "))
    print("")
    print("Dorian: Hello, ", player1._name)
    logging.info("Player gets name")
    print("Dorian: I almost left you for dead. My Alpha space-craft crash landed not too far from yours and I am the only survivor.")
    print("Dorian: It appears you are the only survior of yours as well.")
    print("Dorian: We need to get you out of this belt and out of this space-craft.")
    print("Dorian: We are dangerously close to plummeting to our deaths if we don't hurry.")
    print("")

    answer = (input("Dorian: Can you release yourself from the belt? (yes/no): ")).lower()

    if answer == "yes":
        print("Dorian: Great, free yourself and let's get off this death trap!")
        print("You free yourself and quickly grab rope on your way out.")
        player1.inventory.append("rope")
        print("you equip", player1.inventory)
    else: 
        print("Dorian: Okay, let me cut you out and let's get off this death trap!")
    print("")

    print("After finally departing the space-craft, you find yourself standing on what appears to be the top of a moutain blanketed in snow.")
    print("As you take a step away from the space-craft, you feel a shudden shift behind you and watch as the space-craft slowly plummets toward the base of the mountain, smashing into its side before loudly exploding.")
    print("Dorian: Well, there goes any extra items we might have needed.")
    print("Dorian: Oh well, I have few things we might need to survive.")
    print("")
    answer = (input("Dorian: Can you shoot a firearm? (yes/no): ")).lower()

    if answer == "yes":
        print("Dorian: Here, take this pistol just in case.")
        player1.inventory.append("pistol")
        print("You equip", player1.inventory)
    else:
        print("Okay, I can take care of blasting away any misfortunes we might encounter.")
    print("")

    print("Dorian: Okay it's getting late, we should probably try to find shelter or trek head down this mountain before nightfall.")
    answer = (input("Dorian: What do you think we should do? (shelter/trek): ")).lower()
    print("")

    if answer == "shelter":
        shelter()
        logging.info("Player chooses to shelter")
    elif answer == "trek":
        print("Dorian: Okay, it's going to be a long trek")
        logging.info("Player chooses to trek")
        trek()
main()
