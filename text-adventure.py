import logging
import time
import pandas as pd 

logging.basicConfig(filename="logfile.log", level=logging.DEBUG)

class Player:
    def __init__(self, name="", turns=5, inventory=[], bleeding=False):
        self._name = name
        self.turns = turns
        self.inventory = inventory
        self.bleeding = bleeding
    
    @property
    def get_Name(self):  
        return self._name

    def set_Name(self, value):
        self._name = value

player1 = Player()
required = "Choose only a or b"

def theFire():
    if player1.bleeding == True:
        player1.turns = player1.turns - 1  
        print("You've been slowly bleeding from the wolf-like creature wound. Life = ", player1.turns)
        logging.info("Player has been bleeding from wound and loses 1 life")
        if player1.turns == 0:
            print("Sorry, you ran out of lives. GAME OVER...........")
            logging.info("Player has no more life left and loses game")
            time.sleep(3)
            main()
        else:
            time.sleep(2)  
    else:
        print("Life = ", player1.turns)
        time.sleep(2)
    print("Dorian: Look over in the distance. There's smoke in the air.")
    print("You and Dorian head toward the smoke to investigate.")
    print("")
    time.sleep(2)
    logging.info("Player sees smoke in distance and heads to investigate")
    def alienRobot():
        print("Just when you thought it couldn't get any worse, suddenly an alien Robot appears out of nowwhere!")
        answer = (input("Do you try to run and escape from the alien robot or do you try to reason with robot? (a: run/ b: reason): " )).lower()
        if answer == "a":
            logging.info("Player decides to run from robot")
            print("You and Dorian take off back in the direction in which you came.")
            print("You run and run until you can't run anymore.")
            print("You seem to have lost the robot, however you are lost.")
            logging.info("Player gets lost")
            print("")
            time.sleep(2)
            print("You find a small clearing and head that way.")
            theFire()
        elif answer == "b":
            print("You hesitantly take a step toward the robot with open hands in the air.")
            print("You find yourself communicating with the robot enough and let your gaurd down.")
            print("The robot turns out to be docile and leads you to where the smoke is coming from.")
            print("There you are reconnected with surviving colonists that have already set up camp and attemping to contact outside help.")
            logging.info("Player reasons with robot and robot leads player to safety")
            print("")
            time.sleep(2)
            print("You have reached the end of the game..... The rest is to be continued in the near future.")
            print("you have survived with Life = ", player1.turns)
            logging.info("Player survives and game ends")
            print("")
            time.sleep(4)
        else:
            print(required)
            alienRobot()
    alienRobot()



def trek():
    print("You start heading down the mountain, following behind Dorian.")
    print("It's dark and cold as you slowly trek down the moutain")
    print("You're exhausted and and hungry.")
    player1.turns = player1.turns - 1
    logging.info("Player is tired and hungry and loses 1 life")
    if player1.turns == 0:
        print("Sorry, you ran out of lives. GAME OVER...........")
        time.sleep(3)
        main()
    else:
        print("Life = ", player1.turns)
        time.sleep(2)
    print("")
    print("You finally make it to the bottom of the moutain") 
    print("Dorian: Finally, off this mountain, lets see if we can find any other survivors.")
    print("As you walk along the new terrain, snow and ice seem to be prevalent on this planet.")
    print("Suddenly you hear light cracking underneath your feet and realize you are walking on a frozen body of water.")
    time.sleep(2)
    print("")
    print("Dorian: We're walking on some type of frozen lake. We are already half way across and it's starting to break underneath our feet.")
    logging.info("Player reaches frozen lake")
    answer = (input("Should we pace the rest of the way of the lake or make a run for it? (a: pace/ b: run): ")).lower()
    if answer == "a":
        logging.info("Player chooses to pace off the lake")
        print("Dorian: Okay, let's carefully pace ourseslves off this ice.")
        print("Dorian safely makes across the lake and is able to set foot on land.")
        print("")
        print("You almost make it to the end of the lake when you the ice underneath you begins breaking apart.")
        print("")
        time.sleep(2)
        if ("rope" in player1.inventory):
            print("You remember that you grabbed rope on your way out of he space-craft and quickly toss the rope to Dorian.")
            print("He quickly grabs it and pulls you out of the lake and you escape from falling into the freezing lake.")
            print("")
            time.sleep(2)
            logging.info("Player had rope and is able to safely get off lake")
        else:
            print("The ice completely breaks froms underneath your feet and you drop down into the freezing lake.")
            print("Dorian manages to safely make his way back to you and after several extruciating minutes he is able to pull you out to land.")
            player1.turns = player1.turns - 2
            print("Life = ", player1.turns)
            logging.info("Player doesn't have rope and falls in lake and pays 2 life")
            print("")
            time.sleep(2)
    elif answer == "b":
        print("Dorian: Okay, let's make a run for it!")
        print("You both take off as fast as you can to avoid falling through the lake.")
        print("Dorian: We made it off this lake in one piece. Let's continue on our way.")
        logging.info("Player chooses to run off lake and makes it off unscathed")
    else:
        print(required)
        trek()
        

def shelter():
    print("Dorian: Okay, I might of seen a cave on my way here from where I crashed.")
    logging.info("Player enters cave")
    print("You follow Dorian to the cave and enter the dark cold opening.")
    print("Suddenly, you hear a loud shrieking coming from inside the cave.")
    time.sleep(2)
    print("")
    answer = (input("Do you continue in the cave to investigate or turn around to trek down the moutain? (a: investigate/ b: trek): ")).lower()
    if answer == "a":
        logging.info("Player chooses to investigate")
        print("Dorian: I wonder what that was? Let's continue into this cave and hope it's not anything we can't handle.")
        print("Dorian lights a torch and you continue into the cave away from the outside cold and happen upon two large wolf-like creatures.")
        time.sleep(2)
        print("")
        if ("pistol" in player1.inventory):
            print("Without hesitation, you get the pistol out and blow two bullets through one of the creatures.")
            print("Dorian takes out another pistol and blasts two bullets through the other beast.")
            print("")
            time.sleep(2)
            logging.info("Player had pistol so was able to defend from wolf-like creatures")
        else:
            print("Dorian takes out pistol and blows two bullets into one of the creatures as the other leaps toward you knocking you to the ground.")
            print("You lay on the ground bleeding as Dorian blasts two bullets through the beast.")
            time.sleep(2)
            player1.bleeding = True
            player1.turns = player1.turns - 1
            print("Life = ", player1.turns)
            logging.info("Player doesn't have pistol and cant defend from wolf-like creatures and pays 1 life")
        print("Dorian: Phew, that was a close one. I'm thinking a little too close. Let's get out of this cave, while we still can.")
        time.sleep(2)
        print("")
        trek()
    elif answer == "b":
            trek() 
    else:
        print(required)
        shelter()

def gettingLate():
        print("Dorian: Okay it's getting late, we should probably try to find shelter or trek head down this mountain before nightfall.")
        answer = (input("Dorian: What do you think we should do? (a : shelter/ b: trek): ")).lower()
        print("")
        time.sleep(2)

        if answer == "a":
            shelter()
            logging.info("Player chooses to shelter")
        elif answer == "b":
            print("Dorian: Okay, it's going to be a long trek")
            logging.info("Player chooses to trek")
            trek()
        else:
            print(required)
            gettingLate()

def main():
    player1 = Player()
    logging.info("The game started")
    print("")
    print("")
    print("Welcome to the adventure game!")
    print("Life = ", player1.turns)
    print("")
    time.sleep(2)
    print("The year is 3010...A deluge of massive Astroids impacted Earth and destroyed most life forms and almost pushed the human race to extinction.")
    print("THE FEW as we call ourselves, ventured into the dark abyss of space in an interstellar spacecraft, named The Savior, carrying selected families and civilians to colonize the Alpha Centauri planetary system.")
    print("Before our reach to our destination, an alien robot breached the Savior's hull. Forced to evacuate the mothership in numerous short-range Alpha spacecrafts, a few surviving colonists crash on a nearby habitable planet.")
    print("You emerge from a what felt as a deep sleep and are woken by an umfamiliar voice and a forceful sudden shake....")
    print("")
    time.sleep(2)
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
    time.sleep(2)

    answer = (input("Dorian: Can you release yourself from the belt? (a: yes/ b: no): ")).lower()

    if answer == "a":
        print("Dorian: Great, free yourself and let's get off this death trap!")
        print("You free yourself and quickly grab rope on your way out.")
        player1.inventory.append("rope")
        print("you equip", player1.inventory)
        logging.info("Player gets rope")
    elif answer == "b": 
        print("Dorian: Okay, let me cut you out and let's get off this death trap!")
        print("You struggle with the belt for longer than you'd like and don't have time to grab anything before your exit from the space-craft.")
        logging.info("Player doesn't get rope")
    else:
        print(required)
        main()
    print("")
    time.sleep(2)

    print("After finally departing the space-craft, you find yourself standing on what appears to be the top of a moutain blanketed in snow.")
    print("As you take a step away from the space-craft, you feel a shudden shift behind you and watch as the space-craft slowly plummets toward the base of the mountain, smashing into its side before loudly exploding.")
    print("Dorian: Well, there goes any extra items we might have needed.")
    print("Dorian: Oh well, I have few things we might need to survive.")
    print("")
    time.sleep(2)
    def canYouShoot():
        answer = (input("Dorian: Can you shoot a firearm? (a: yes/ b: no): ")).lower()

        if answer == "a":
            print("Dorian: Here, take this pistol just in case.")
            player1.inventory.append("pistol")
            print("You equip", player1.inventory)
            logging.info("Player gets pistol")
        elif answer == "b":
            print("Okay, I can take care of blasting away any misfortunes we might encounter.")
            logging.info("Player doesn't get pistol")
        else:
            print(required)
            canYouShoot()
        print("")
    canYouShoot()
    gettingLate()
    theFire()
    df = pd.read_csv ('logfile.log')
    df.to_csv('logfile.csv')
main()



