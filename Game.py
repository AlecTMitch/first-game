import time
import random
def game_over():
    time_print("...")
    time_print("...")
    time_print("You have run out of HP")
    time_print("You can no longer go on")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print()
    print("                 ░░░░░░░░░▄░░░░░░░░░░░░░░▄")
    print("                 ░░░░░░░░▌▒█░░░░░░░░░░░▄▀▒▌")
    print("                 ░░░░░░░░▌▒▒█░░░░░░░░▄▀▒▒▒▐")
    print("                 ░░░░░░░▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐")
    print("                 ░░░░░▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐")
    print("                 ░░░▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌")
    print("                 ░░▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌")
    print("                 ░░▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐")
    print("                 ░▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌")
    print("                 ░▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌")
    print("                 ▌▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐")
    print("                 ▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌")
    print("                 ▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐")
    print("                 ░▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌")
    print("                 ░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐")
    print("                 ░░▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌")
    print("                 ░░░░▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀")
    print("                 ░░░░░░▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀")
    print("                 ░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▀▀")
    print()
    print()
    print("                   You Fucking Died lol")
    print("                        Gay Over")
    print()
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    exit()

class Player:
    def __init__(self, name, hp, strength, dexterity, intelligence, charm, speed, luck, money, alcohol, description, racial_bonus) -> None:
        self.name = name
        self.hp = hp
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.charm = charm
        self.speed = speed
        self.luck = luck
        self.money = money
        self.alcohol = alcohol
        self.description = description
        self.racial_bonus = racial_bonus

    def __setattr__(self, name, value):
        if name == "hp" and value == 0:
            game_over()
        object.__setattr__(self, name, value)

    def print_stats(self):
        print(f"{self.name.upper()}'S STATS")
        print("HP:", self.hp)
        print("Str:", self.strength)
        print("Dex:", self.dexterity)
        print("Int:", self.intelligence)
        print("Chrm:", self.charm)
        print("Spd:", self.speed)
        print("Lck:", self.luck)
        print("Mny:", self.money)
        print("Alc:", self.alcohol)
        print(self.description)
        print("Racial Bonus:", self.racial_bonus)

    def print_combat_stats(self):
        print(f"{self.name.upper()}'S STATS")
        print("HP:", self.hp)
        print("Str:", self.strength)
        print("Spd:", self.speed)
        print("Alc:", self.alcohol)
        print(self.description)
        print("Racial Bonus:", self.racial_bonus)
       
Trey = Player("Trey", hp=30, strength=8, dexterity=6, intelligence=5, charm=6, speed=10, luck=7, money=5, alcohol=0, description="A sad bleb to be sure", racial_bonus="Depression")
Jacob = Player("Jacob", hp=25, strength=12,dexterity= 5,intelligence= 5, charm=8, speed=6, luck=4, money=5, alcohol=0, description="A Giga Chad that likes women too much", racial_bonus="Drunken Strength")
Jamie = Player("Jamie", hp=20, strength=10,dexterity= 4,intelligence= 10, charm=-4, speed=5, luck=6, money=5, alcohol=0, description="Is always right except for when he is wrong", racial_bonus="Asshole")
Kaleb = Player("Kaleb", hp=25, strength=12,dexterity= 8,intelligence= 8, charm=10, speed=9, luck=6, money=5, alcohol=0, description="A quiet cutie",  racial_bonus="ADHD")

class Npc:
    def __init__(self, name, hp, strength, speed, love, description, racial_bonus) -> None:
        self.name = name
        self.hp = hp       
        self.strength = strength
        self.speed = speed
        self.love = love
        self.description = description
        self.racial_bonus = racial_bonus

    def print_npc_stats(self):
        print(f"{self.name.upper()}'S STATS")
        print("HP:", self.hp)
        print("Str:", self.strength)
        print("Spd:", self.speed)
        print(self.description)
        print("Racial Bonus:", self.racial_bonus)

Stacy = Npc("Stacy", hp=15, strength=3, speed=5, love=0, description="A hungry and FAT bitch", racial_bonus="Obesity")
Haley = Npc("Haley", hp=36, strength=8, speed=8, love=0, description="A book worm, but not actually a worm", racial_bonus="Learned")

def time_print(text):
    time.sleep(1)
    print(text)

start = input("Are you ready to play? (Yes/No)    ")
if start.lower().strip() != "yes":
    game_over()

player = None
while player == None:
    print("\n")
    print("     |--------------------|")
    print("     |                    |")
    print("     |    Trey's Game     |")
    print("     |                    |")
    print("     |--------------------|")
    print("\n")
    race = input("Choose a race: (Trey, Jacob, Jamie, or Kaleb)  ")
    if race == "Trey":
        Trey.print_stats()
        race_confirm = input("Are you sure you want this loser? (Yes/No)")
        if race_confirm.lower().strip() == "yes":
            time_print("\n Trey chosen for some reasen\n")
            player = Trey
        else:
            continue
    elif race == "Jacob":
        Jacob.print_stats()
        race_confirm = input("Are you sure you want 'Jacob'? (Yes/No)")
        if race_confirm.lower().strip() == "yes":
            time_print("\n Jacob Selected\n")
            player = Jacob
        else:
            continue
    elif race == "Jamie":
        Jamie.print_stats()
        race_confirm = input("Are you sure you want 'Jamie'? (Yes/No)")
        if race_confirm.lower().strip() == "yes":
            time_print("\n Jamie Selected\n")
            player = Jamie
        else:
            continue
    elif race == "Kaleb":
        Kaleb.print_stats()
        race_confirm = input("Are you sure you want 'Kaleb'? (Yes/No)")
        if race_confirm.lower().strip() == "yes":
            time_print("\n Kaleb Selected \n")
            player = Kaleb
        else:
            continue

def intro():
    print("-------------------------------------------------------------")
    print("         NOTE: In this game, yOuR cHoIceS MatTeR")
    print("-------------------------------------------------------------\n")
    time_print("Your alarm goes off. It's 7am.")
    time_print("Ugh! Mondays. \n")
    print("1: Hit the snooze and stay in bed for an extra 45 minutes.")
    print("2: Get up and brush your teeth and shower.")
    print("Stats: show current stats \n")
    choice = input("What is your choice? (1/2/Stats)    ")
    print()
    if choice == "1":
        intro1()
    elif choice == "2":
        intro2()
    elif choice == "Stats":
        player.print_stats()
        intro()
    else:
        intro()
def intro1():
    time_print("It's always nice to get a few extra Z's.")
    time_print("And you know what? They really help.")
    time_print("Those extra minutes ensure that you are well rested for the rest of the day.")
    time_print("...")
    time_print("You gain +5 HP!")
    player.hp += 5
    time_print("...")
    time_print("Poggers! \n")
def intro2():
    if race == "Trey":
        time_print("Depression can be especially bad in the morning.")
        time_print("...")
        time_print("You take -2 HP")
        player.hp -= 2
        time_print("...")
        time_print("Nevertheless")
    else:
        pass
    time_print("Good hygiene is important!")
    time_print("And the warm water relaxes your muscles.")
    time_print("...")
    time_print("You gain +1 Dex and +1 Chrm.")
    time_print("...")
    time_print("It's important to take care of yourself and maintain a healthy lifestyle")
    player.dexterity += 1
    player.charm += 1
    print()

def day1():
    print("\n")
    time_print("Class starts soon. Better get going")
    time_print("On the way to class you see a dog")
    time_print("The dog is out of the way, and you might be late to class if you go see the woofer")
    time_print("But it looks so cute!")
    time_print("What would you like to do? \n")
    print("1: Go and pet the dog")
    print("2: Keep a steady pace on towards class.")
    print("Stats: Show current stats \n")
    choice = input("What is your choice? (1/2/Stats)    ")
    print()
    if choice == "1":
        day1_1()
    elif choice == "2":
        day1_2()
    elif choice == "Stats":
        player.print_stats()
        day1()
    else:
        day1()
def day1_1():
    print("\n")
    time_print("The dog notices you coming towards it")
    time_print("The dog starts wagging its tail with extreme excitement")
    time_print("The dog even does a cute little dance")
    time_print("You bend down and start petting the good boy")
    time_print("There you have it. You CAN pet the dog in this game")
    time_print("But suddenly the dog bolts away, but looks back as if it expects you to follow it")
    time_print("Oh. Its a grand dog, but you're already late as is. \n")
    print("1: Chase after that cute lil' fucker. He wants to show you something truly poggers")
    print("2: Class is about to start. I need to get back on track")
    print("Stats: Show me them stitties")
    choice = input("What is your choice (1/2/Stats)    ")
    print()
    if choice == "1":
        day1_1_1()
    elif choice == "2":
        day1_2()
    elif choice == "Stats":
        player.print_stats()
        day1_1()
    else:
        day1_1()
def day1_1_1():
    print("\n")
    time_print("You chase after the pup, but he takes off again before you can reach him")
    time_print("OH NO! \n He's running towards the busy road!")
    time_print("You full sprint to try and save the dog but...")
    if player.speed >= 8:
        time_print("...")
        time_print("You only just reach him in time to grab his collar before the street.")
        time_print("The dog acknowledges its carelessness")
        time_print("He walks over to a patch of grass near the road and starts digging")
        time_print("He kicks up dirt everywhere, but eventually uncovers a box")
        time_print("Inside the box is some illegally printed but unmarked USD and a very thought provoking fortune cookie")
        time_print("...")
        time_print("You gain +2 Mny and +2 Int")
        player.money += 2
        player.intelligence += 2
        time_print("Awesome, now you better get to class. Better late than never.")
        day1_1_2()
    else:
        time_print("...")
        time_print("You were'nt fast enough")
        time_print("The dog ran into the middle of the road")
        time_print("The dogs breifly looks around in confusion before, making eye contact with you using his sad puppy eyes")
        time_print("Behond those watery mirrors you can see the dog wondering what might have been if you were just a little faster")
        time_print("The dog is then hit by large truck going well above the speed limit")
        time_print("All that is left is a cloud of red mist")
        time_print("...")
        time_print("The image leaves a scar on your brain and you take -5 HP")
        time_print("And all that running made you really sweaty")
        time_print("Plus you got some blood on you")
        time_print("...")
        time_print("You also recieve -2 Chrm")
        player.hp -= 5
        player.charm -= 2
        time_print("...")
        time_print("Well, better get to class")
        day1_1_2()
def day1_1_2():
    time_print("You show up to class a little late")
    time_print("Fortunately there is no punishment, but you miss out on some lecture material")
    time_print("On your way to your seat, Stacy makes a snarky remark about you being late.\n")
    print("1: Ignore her and just go sit down")
    print("2: Call her a bitch")
    print("3: Slap her across the face")
    print("Stats: what the numbers doing \n")
    choice = input("Do you choose violence this day? (1/2/3/Stats)    ")
    print()
    if choice == "1":
        time_print("No violence for the moment, anyway.")
        time_print("You feel good about your decision, as you take your seat \n")
        time_print("Upon turning the other cheek you recieve +3 HP and +1 Lck")
        player.hp += 3
        player.luck += 1
        time_print("Well done, Ghandi \n")
    elif choice == "2":
        time_print("Such aggresion cannot go unanswered!")
        time_print("You turn to look at her with a serious gaze")
        time_print("She lifts one brow, as if waiting for a response")
        time_print("You tell her to her face that she is one massive bitch")
        time_print("Her jaw drops as you also hit her with a quick BMI check \n")
        time_print("She does not pass \n")
        time_print("You owned that libtard hard. Stacy loses 5 HP")
        Stacy.hp -= 5
        time_print("This makes you look like a total jerk and lose 1 CHRM, but you still take pride in your actions")
        player.charm -= 1
        time_print("Looking smug, you take your seat")
        time_print("Good thing the teacher didn't see that exchange")
        day1_3()
    elif choice == "3":
        time_print("Talk shit, get hit")
        time_print("You open your palm and take a wide swing")
        time_print("WHAP!")
        time_print(f"Contact is made with Stacy's stupid chubby face and she takes {player.strength} HP in damage")
        time_print("That'll show her, right? \n")
        time_print("Well, in extreme anger she returns with a double slap!")
        time_print("Each one of your tender cheeks takes 3 HP. Thats 6 HP total")
        time_print("Furthermore, you now look like a total asshole if you werent already one")
        time_print("Stacy isnt that popular, so you only lose 2 Chrm, but you cant help but feel like bad like may be coming your way. You also lose 2 Lck")
        player.charm -= 2
        player.luck -= 2
        time_print("Maybe that was too far, you think, as you sit down")
        day1_3()
    elif choice == "Stats":
        player.print_stats()
        day1_1_2()

def day1_2():
    time_print("You show up to class with plenty of time left")
    time_print("You take your seat and get ready to take notes")
    time_print("Today's Lecture is 'Why connor is the most hated creature on the planet'")
    time_print("You already know everything there is to know about this! You could have just stayed in bed and skipped")
    time_print("Oh well. There were still some interesting reasons that you had forgotten about \n")
    time_print("The metaphorical jogging your memory did awards you with +2 Int.\n")
    player.intelligence += 2
    time_print("Not too shabby")
    day1_3()

def day1_3():
    time_print("Class concludes and its now 12pm")
    time_print("You should probably get something to eat")
    time_print("You start the small trek towards the college's dining hall")
    time_print("You reach the bridge that connects the two halves of campus which are bisected by train tracks")
    time_print("You get halfway across the bridge when you realize there is someone on the opposite side just standing there, as if waiting for you")
    time_print("Upon closer inspection, you see that it is your classmate Stacy")
    time_print("You approach her. \n")
    if Stacy.hp == 15:
        day1_3_1()
    else:
        time_print("As you get closer you realize that she is pissed")
        time_print("Like... completely fuming")
        time_print("She gets right to it and demands that you give her 4 Mny")
        time_print("'NOW!', she screams\n")
        print("1: Give her 4 Mny")
        print("2: Decline her humble offer")
        print("3: Show me some stats!")
        choice = input("How do you proceed, king?  (1/2/Stats)     ")
        print()
        if choice == "1":
            time_print("She greedily takes your Mny and scoffs")
            time_print("'That's what I thought, bitch'")
            time_print("She leaves for the dining hall")
            time_print("You lose 4 Mny!")
            player.money -= 4
            day1_4()
        elif choice == "2":
            time_print("'You're dead!', she shouts")
            time_print("A battle brews!")
            Stacy_fight()
        elif choice == "Stats":
            print()
            player.print_stats()
        else:
            day1_3()
def day1_3_1():
    time_print("She explains that she forgot to bring her lunch to school today.")
    time_print("And she is asking for 2 Mny so she can buy herself some food.")
    time_print("How annoying! Doesn't she realize that you also need to save your money so you can eat.\n")
    print("1: Give her 2 Mny")
    print("2: Say no")
    print("Stats: Stit for Stat")
    choice = input("How do you handle this request? (1/2/Stats)    ")
    print()
    if choice == "1":
        time_print("You feel generous and don't want to deal with any conflict right now, so you hand her the 2 Mny. \n")
        player.money -= 2
        time_print("She takes it and expresses her gratitude.")
        time_print("She also apologizes for being rude to you sometimes and says she'll try and be nicer.")
        time_print("She turns and heads to the dining hall.")
        time_print("You don't get much of anything else out of the exchange, except a lighter wallet.")
        day1_4()
    elif choice == "2":
        day1_3_2()      
def day1_3_2():
    time_print("Stacy's humble asking mood quickly shifts, to be more agitated.")
    time_print("She demands that she gets the Mny becuase she 'Totes needs it more than you'.")
    time_print("She holds out her hand expecting to get the Mny 'NOW!'\n")
    print("1: Give her the Mny. You don't want a fight")
    print("2: Refuse to hand over the Mny")
    print("Stats: Statties for daddies\n")
    choice = input("Will you heed her demands? (1/2/Stats)     ")
    print()
    if choice == "1":
        time_print("She snags the Mny before you can even give it to her")
        time_print("'Eugh!', she says before storming off to get lunch")
        time_print("Well... you lose 2 Mny and gain nothing")
        player.money -= 2
        day1_4()
    elif choice == "2":
        time_print("Stacy is now furious")
        time_print("She starts rushing towards you.")
        time_print("If she's so hungry, then you'll just have to feed her a freshly made knuckle sandwich.")
        time_print("FIGHT!")
        Stacy_fight()
    elif choice == "Stats":
        print()
        player.print_stats()
    else: 
        day1_3_2()

def Stacy_fight():
    time_print("-------------------------------------------------------------------------------------------------------------------------------------------------")
    Stacy.print_npc_stats()
    print()
    player.print_combat_stats()
    print()
    while Stacy.hp > 0:
        print(f"You have {player.hp} HP")
        print(f"Stacy has {Stacy.hp} HP")
        if (player.speed / Stacy.speed) > 2:
            player_attack()
            if Stacy.hp < 0:
                break
            player_attack()
            if Stacy.hp < 0:
                break
            stacy_attack()
        elif 2 > (player.speed / Stacy.speed) > 1:
            player_attack()
            if Stacy.hp < 0:
                break
            stacy_attack()
        else:
            stacy_attack()
            player_attack()
    time_print("Stacy has run out of HP")
    time_print("Stacy explodes in a puff of smoke")
    time_print("Stacy defeated!")
    time_print("You recieve 2 Mny for winning!")
    player.money += 2
    time_print("-------------------------------------------------------------------------------------------------------------------------------------------------")
    day1_4()
def stacy_attack():
    print()
    time_print("Stacy's Turn")
    print()
    if random.randint(1,2) == 1:
        time_print("\n Stacy gives you a slap to the face")
        time_print(f"You take {Stacy.strength} damage!")
        player.hp -= Stacy.strength
        if player.hp < 0:
            game_over()
        print()
    else:
        time_print("Stacy reaches into her pocket and pulls out a fist full of mashed potatoes")
        time_print("She shoves it in her mouth and restores 3 HP")
        Stacy.hp += 3
        print()

def player_attack():
    print()
    time_print("It's your turn \n")
    print("1: Throw a punch")
    print("2: Do Nothing")
    choice = input("What is your move? (1/2)      ")
    if choice == "1":
        time_print("You throw a punch")
        time_print(f"The enemy takes {player.strength} damage")
        Stacy.hp -= player.strength
        print()
    elif choice == "2":
        time_print("You simply exist, nothing more")
        print()
    else:
        player_attack()

def day1_4():
    time_print("\nYou continue on your way to the dining hall")
    time_print("When you arrive, you pay the 1 Mny fee to enter the cafeteria")
    player.money -= 1
    time_print("You grab an assortment of what looks good and grab a drink")
    time_print("Next you start to look for a place to sit and see some options \n")
    if Stacy.hp <= 0:
        day1_4_1()
    else:
        day1_4_2()
def day1_4_1():
    print("1: Sit at an empty table")
    print("2: Sit at Shady Sam's Table (Store)")
    print("Stats: Mr. Stattiken")
    choice = input("With whom do you sit? (1/2/Stats):    ")
    print()
    if choice == "1":
        day1_4_1_empty()
    elif choice == "2":
        day1_4_1_sam()
    elif choice == "Stats":
        player.print_stats()
    else:
        day1_4_1()
def day1_4_2():
    print("1: Sit at an empty table")
    print("2: Sit at Shady Sam's Table (Store)")
    print("3: Sit at a Table with Stacy")
    print("Stats: Statter-Brained")
    choice = input("With whom do you sit? (1/2/Stats):    ")
    print()
    if choice == "1":
        day1_4_1_empty()
    elif choice == "2":
        day1_4_1_sam()
    elif choice == "3":
        day1_4_1_stacy()
    elif choice == "Stats":
        player.print_stats()
    else:
        day1_4_2()

def day1_4_1_empty():
    time_print("You choose to sit at an empty table")
    if race == "Trey":
        time_print("This is likely because you have no friends")
        time_print("Your depression deals 5 damage to you")
        player.hp -= 5
        time_print("No one comes to sit with you and you eat your lunch alone")
        time_print("The food is not very good, but it is what it is")
        time_print("...")
        time_print("You gain 5 HP after eating")
        player.hp += 5
        time_print("...")
        time_print("How counter-productive")
        pass
    elif race == "Jacob":
        time_print("You eat your meal without any interuptions")
        time_print("The food is not very good, but it is waht it is")
        time_print("...")
        time_print("You gain 5 HP after eating")
        player.hp += 5
        time_print("...")
        time_print("How filling!")
        pass
    elif race == "Jamie":
        time_print("You eat your meal in complete solitude")
        time_print("Mainly because you're such an asswhole that no one would ever want to sit with you")
        time_print("Maybe if they were being paid")
        time_print("The food is not very good, but it is what it is")
        time_print("...")
        time_print("You gain 5 HP after eating")
        player.hp += 5
        time_print("...")
        time_print("How filling!")
        pass
    elif race == "Kaleb":
        time_print("You eat your meal alone")
        time_print("But you notice that there are a lot of girls AND guys checking you out")
        time_print("Must be because you're such a cutie ;)")
        time_print("The food is not very good, but it is what it is")
        time_print("...")
        time_print("You gain 5 HP after eating")
        player.hp += 5
        time_print("...")
        time_print("How filling!")
        pass
    day1_5()
def day1_4_1_sam():
    time_print("You sit next to Shady Sam")
    time_print("He is dressed up in his usual trenchcoat and black trilbe attire")
    time_print("He eyes you up")
    time_print("'Are you wearing a wi're, bruv?', He asks in a southern accent")
    time_print("A south England accent that is")
    time_print("You tell him you aren't")
    time_print("Then what the fuck are you 'ere for, slag")
    day1_sam_wares()
def day1_sam_wares():
    shopping = 1
    while shopping == 1:
        time_print("'Hurry up and pick somefink, yeah'")
        print("1: A bottle of SAARMS (2 Mny)")
        print("2: A can of 'Statty Lite' beer (2 Mny)")
        print("3: A Shadey Sam scratch off (1 Mny)")
        print("4: Nothing")
        time_print(f"You have {player.money} Mny")
        choice = input("What would you like to look at?")
        print()
        if choice == "1":
            print("SAARMS BOTTLE\n")
            print("Immediately grants +2 to Str")
            print("Probably has no side effects")
            choice1_confirm = input("Do you want this item (Yes/No)    ")
            print()
            if choice1_confirm == "Yes":
                if player.money < 2:
                    time_print("You cannot afford this")
                    day1_sam_wares()
                else:
                    player.money -= 2
                    time_print("You guzzle the pills down all at once")
                    time_print("...")
                    time_print("You gain +2 Str")
                    player.strength += 2
                    time_print("...")
                    time_print("You hope there aren't any side effects")
                    day1_sam_wares()
            else:
                day1_sam_wares()
        elif choice == "2":
            print("STATTY LITE BEER CAN\n")
            print("Grants +1 to Alc")
            print("Can be consumed to ignore damage taken for 2 turns")
            print("If player has 'Drunken Strength', it also increases Str by 2 for two turns")
            choice2_confirm = input("Do you want this item (Yes/No)    ")
            print()
            if choice2_confirm == "Yes":
                if player.money < 2:
                    time_print("You cannot afford this")
                    day1_sam_wares()
                else:
                    player.money -= 2
                    time_print("You pocket the can")
                    time_print("...")
                    time_print("You gain +1 Alc")
                    player.alcohol += 1
                    time_print("...")
                    time_print("You look forward to drinking this")
                    day1_sam_wares()
            else:
                day1_sam_wares()
        elif choice == "3":
            print("SHADEY SAM SCRATCH OFF\n")
            print("Has a 1 in 10 chance of granting +10 Mny")
            print("You prbably won't win")
            choice3_confirm = input("Do you want this item (Yes/No)    ")
            print()
            if choice3_confirm == "Yes":
                if player.money < 1:
                    time_print("You cannot afford this")
                    day1_sam_wares()
                elif player.money >= 1:
                    player.money -= 1
                    time_print("You scratch off the card")
                    time_print("...")
                    if random.randint(1, 10) == 1:
                        time_print("YOU ACTUALLY FUCKING WON!")
                        time_print("You gain +10 Mny")
                        player.money += 10
                        day1_sam_wares()
                    else:
                        time_print("Not a winner this time")
                        time_print("Sad. Oh well.")
                        day1_sam_wares()
            else:
                day1_sam_wares()
        elif choice == "4":
            choice4_confirm = input("Are you sure you want to leave? (Yes/No)     ")
            print()
            if choice4_confirm == "Yes":
                time_print("You leave without purchasing anything\n")
                shopping += 1
            else:
                day1_sam_wares()
        else:
            day1_sam_wares()
    time_print("After shopping you eat your food")
    time_print("It's cold now, but you still gain +3 HP")
    player.hp += 3
    day1_5()
def day1_4_1_stacy():
    time_print("You see that Stacy is sitting alone, so you go to sit next to her")
    if Stacy.hp == 15:
        time_print("As you sit down, she looks at you")
        time_print("'Oh hi', she says")
        time_print("'Thanks for lending me that money'\n")
        print("1: 'You're Welcome'")
        print("2: 'Shut up, bitch, I'm trying to eat'")
        choice1 = input("What do you say? (1/2)    ")
        print()
        if choice1 == "1":
            time_print("She smiles")
            time_print("You have a nice lunch together")
            time_print("You talk about many things")
            time_print("Among the discussion you gradually eat your lunch")
            time_print("The food is not very good, but it is what it is")
            time_print("...")
            time_print("You gain +5 HP")
            player.hp += 5
            time_print("...")
            time_print("How filling!")
            time_print("Stacy gains +1 Lve")
            Stacy.love += 1
            pass
        elif choice1 == "2":
            time_print("She scoffs")
            time_print("'If you didn't want to talk then why didn't you sit at an empty table', she says")
            time_print("She may have a point")
            time_print("But you wouldn't be able to call her a bitch if you sat somewhere else so...")
            time_print("You simply ignore her because you have ceased caring, or rather, never did to begin with")
            time_print("After your absence of a remark she starts scoffing again")
            time_print("Because she jUsT caN't EveN rIgHt NoW")
            time_print("Among her scoffing, you eat your lunch")
            time_print("The food is not very good, but it is what it is")
            time_print("...")
            time_print("You gain +5 HP")
            player.hp += 5
            time_print("...")
            time_print("How filling!")
            pass
        else:
            day1_4_1_stacy()
    else:
        time_print("As you sit down, she looks at you")
        time_print("'Oh... hi', she says")
        time_print("'I suppose I should thank you for giving me your money'\n")
        print("1: 'You're Welcome'")
        print("2: 'Shut up, bitch, I'm trying to eat'")
        choice2 = input("What do you say? (1/2)    ")
        if choice2 == "1":
            time_print("She smiles")
            time_print("You have a nice lunch together")
            time_print("You talk about many things")
            time_print("She apologizes for being so angry earlier on the bridge and acknowledges that she deserved what she got in class")
            time_print("Among the discussion and apology you gradually eat your lunch")
            time_print("The food is not very good, but it is what it is")
            time_print("...")
            time_print("You gain +5 HP")
            player.hp += 5
            time_print("...")
            time_print("How filling!")
            time_print("and Stacy gains +1 Lve")
            Stacy.love += 1
            pass
        elif choice2 == "2":
            time_print("She scoffs")
            time_print("'If you didn't want to talk then why didn't you sit at an empty table', she says")
            time_print("She may have a point")
            time_print("But you wouldn't be able to call her a bitch if you sat somewhere else so...")
            time_print("You simply ignore her because you have ceased caring, or rather, never did to begin with")
            time_print("After your absence of a remark she starts scoffing again")
            time_print("Because she jUsT caN't EveN rIgHt NoW")
            time_print("Among her scoffing, you eat your lunch")
            time_print("The food is not very good, but it is what it is")
            time_print("...")
            time_print("You gain +5 HP")
            player.hp += 5
            time_print("...")
            time_print("How filling!")
            pass
        else:
            day1_4_1_stacy()
    day1_5()




def day1_5():
    print()
    time_print("You leave the building and come to a crossroads")
    time_print("Not really, but you do have some free time.")
    time_print("And with some free time, comes some 'free' choices\n")
    print("1: Go to the library")
    print("2: Go the the gym")
    print("3: Go to your dorm \n")
    print("4: Go into town\n")
    print("Stats: Show me STATS!")
    choice = input("Where would you like to spend your free time? (1/2/3/4/Stats:)    ")
    if choice == "1":
        day1_5_1()
    elif choice == "2":
        day1_gym()
    elif choice == "3":
        day1_5_3()
    elif choice == "4":
        day1_5_4()
    elif choice == "Stats":
        player.print_stats()
    else:
        day1_5()

def day1_5_1():
    time_print("You decide to go to the library")
    if random.randint(1,(10 - player.luck)) == 1:
        time_print("On your way to the library, you find 2 MNY")
        player.money += 2
        time_print("How lucky!")
        pass
    time_print("You walk into the library")
    time_print("It smells... \n like learning")
    time_print("You notice that Haley is working the front desk doing checkouts")
    time_print("Now that you have entered the building you must decide what you'd like to do\n")
    print("1: Look around and inspect the area")
    print("2: Do some learning")
    print("Stats: peruse your stats")
    choice = input("What would you like to do? (1/2)    ")
    if choice == "1":
        time_print("You look around and see...")
        time_print("...")
        time_print("Books you idiot, its a library")
        time_print("What did you expect?")
        time_print("Idiot")
        day1_library1()
    elif choice == "2":
        day1_library1()
    else:
        day1_library1()

def day1_library1():
    time_print("You walk around and peruse some of the books")
    time_print("You find one that looks particularly interesting")
    time_print("It's titled 'Hazing twinks for beginners' by Chad Chadington")
    time_print("It is full of really useful information that will help you later")
    time_print("Learning has been really great, you gain +2 Int")
    player.intelligence += 2
    time_print("Bigger brain!\n")
    time_print("After reading a little, you decide to checkout the book")
    time_print("You head over to the front desk")
    time_print("Haley is working there today")
    time_print("You hand her the book")
    time_print("She looks at it, then back at you.")
    time_print("'Hazing twinks for beginners?' she says.")
    time_print("You respond...\n")
    print("1: 'Yeah, you never know when you might need to haze a twink'")
    print("2: 'I'm glad that we have established that you can read'")
    print("3: Say nothing\n")
    print("Stats: show stats")
    choice = input("What do you say? (1/2/3/Stats):    ")
    if choice == "1":
        if player.charm >= 7:
            time_print("'Oh I know', she says")
            time_print("'I'm just surprised that someone like you is only checking out the beginner book'")
            time_print("You say that you just need to cite the book for a research paper")
            time_print("She nods in understaning")
            time_print("She finishes checking out your book, and hands it too you")
            time_print("As you turn to leave she gives you a little wink")
            time_print("Haley gains +1 Lve")
            Haley.love += 1
            day1_5_leave("library")
        else:
            time_print("She assumes you're joking, and does not take it well")
            time_print("She says, 'Hazing is bullying, and bullying is not cool")
            time_print("I can't beleive she doesn't understand that twinks are an exception to the rule")
            time_print("She angrily scans the book, then gives it to you")
            day1_5_leave("library")
    elif choice == "2":
        if player.intelligence >= 10:
            time_print("She giggles")
            time_print("'You're funny' she says")
            time_print("She doesn't realise that you weren't making a joke")
            time_print("But that's okay")
            time_print("It works out in your favor")
            time_print("She scans and gives you the book and serves it with a wink")
            time_print("Haley gains +1 Lve")
            Haley.love += 1
            day1_5_leave("library")
        else:
            time_print("She did not like that response")
            time_print("She takes it as an offense to her intelligence")
            time_print("She does not say anything. She just scans the book angrily then hands it to you")
            time_print("Your Chrm suffers as a result of this exchange")
            time_print("You lose 1 Chrm")
            player.charm -= 1
            day1_5_leave("library")
    elif choice == "3":
        time_print("She glances up at you")
        time_print("You don't say anything and just stare at her")
        time_print("She scans the book and gives it to you")
        day1_5_leave("library")
    elif choice == "Stats":
        player.print_stats
        day1_library1()
    else:
        day1_library1()

    
def day1_gym():
    chance = 0
    time_print("You make your way over to the gym")
    if random.randint(1,(10 - player.luck)) == 1 and chance == 0:
        time_print("On your way to the gym, you find 2 MNY")
        player.money += 2
        time_print("How lucky!")
        pass
    time_print("When you enter the building, you walk over to the check-in desk")
    time_print("Natalie is sitting at the desk and notices you coming over")
    time_print("'Hello, are you checking in?', she says.")
    time_print("You nod")
    time_print("'And are you going to the weight room or the pool today?'\n")
    print("1: I am going to the weight room")
    print("2: I am going to the pool")
    print("Stats: View you stats\n")
    choice = input("Where would you like to go? (1/2/Stats)    ")
    if choice == "1":
        day1_wr1()
    elif choice == "2":
        day1_pool1()
    elif choice == "Stats":
        player.print_stats
    else:
        chance += 1
        day1_gym()

def day1_wr1():
    time_print("'Alright, you're all set to use the weight room'")
    time_print("You head over to the weight room\n")
    print("1: Start lifting iron and pumping weights")
    print("2: Head over to the treadmill and start running")
    print("Stats: Check you stattilage")
    choice = input("What equipment would you like to use? (1/2/Stats:)      ")
    if choice == "1":
        time_print("You hit the weights hard")
        time_print("You do a full body workout with moderate weight")
        time_print("You can feel you mooscles getting bigger")
        time_print("...")
        time_print("You gain +2 Str")
        player.strength += 2
        time_print("...")
        time_print("You feel exhaisted now\n")
        print("1: You can keep going for longer!")
        print("2: Call it there for the gym")
        print("Stats: Show me Tain statting, please")
        choice2 = input("What do you do? (1/2/Stats)    ")
        if choice2 == "1":
            time_print("You continue lifting weights for a little longer")
            time_print("...")
            time_print("You overexert your body and lose 10 HP!")
            player.hp -= 10
            time_print("...")
            time_print("But there is no pain without gain")
            time_print("You gain an additional +1 Str")
            player.strength += 1
            day1_gym_leave()
        elif choice2 == "2":
            time_print("You decide to leave it at that")
            time_print("It's probably best not to push yourself too hard anyway")
            day1_gym_leave()
        elif choice2 == "Stats":
            player.print_stats
            day1_wr1()
        else:
            day1_wr1()            
    elif choice == "2":
        time_print("You hop on a treadmil and start jogging")
        time_print("You gradually alter your pace as needed")
        time_print("You run for a good bit and really improve your endurance and speed")
        time_print("You gain +2 Spd")
        player.speed += 2
        day1_gym_leave()
    elif choice == "Stats":
        player.print_stats
        day1_wr1()
    else:
        day1_wr1()

def day1_pool1():
    time_print("You head over to the indoor pool")
    time_print("You slip into your swim trunks that you carry around on you at all times")
    time_print("You get in the pool. That water is a little chilly")
    time_print("You swim laps and improve your stats")
    time_print("...")
    time_print("You gain +1 Str, +1 Dex, and +1 Spd")
    time_print("...")
    player.strength += 1
    player.dexterity += 1
    player.speed += 1
    time_print("Epic gains!")
    day1_gym_leave()

def day1_gym_leave():
    time_print("Before leaving, you first head over to the front desk to check out")
    time_print("You walk over to the desk")
    time_print("Natalie is getting ready to end her shift")
    time_print("She looks like she's in a hurry to leave")
    time_print("She notices you coming")
    time_print("'How was your time today? Are you ready to leave?'\n")
    print("1: 'It was good. I'm all set to leave'")
    print("2: It sucked. Get me out of here!")
    print("3: 'It was good. Why are you so eager to leave?")
    print("4: 'It sucked. And why are you trying to leave so quickly?")
    print("Stats: What my stats be?")
    choice = input("What would you like to say to Natalie?")
    if choice == "1":
        time_print("'Glad you enjoyed it. Alright let me get you checked-out'")
        time_print("'Alright you're all set to leave. Bye!'")
        day1_6()
    elif choice == "2":
        time_print("'I'm sorry to hear that. Well, let me get you checked-out'")
        time_print("'Alright. You're all set to leave.")
        day1_6()
    elif choice == "3":
        time_print("'Glad to hear you had a good time'")
        time_print("'Oh, my shift is over so I'm leaving'")
        time_print("'That's all there is to it.'")
        day1_gym_leave2()
    elif choice == "4":
        time_print("'I'm sorry to hear that'")
        time_print("'And my shift is over, so I'm leaving'")
        time_print("'Thats all there is to it'")
        day1_gym_leave2()
    elif choice == "Stats":
        player.print_stats
    else:
        day1_gym_leave()

def day1_gym_leave2():
    pass

def day1_5_3():
    pass
def day1_5_4():
    pass

def day1_5_leave(place):
    time_print("You make your way out of the" + place)
    time_print("It is almost time for your next class")
    time_print("You make your way to the next building where your class is")
    day1_6()

def day1_6():
    pass

while player.hp > 0:
    intro()
    day1()
game_over()