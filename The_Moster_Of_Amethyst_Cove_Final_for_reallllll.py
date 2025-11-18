import random
import sys
import subprocess
def story_end():
    #Call this after every ending function
    print("The end! Thank you so much for playing!")
    print("If you're not satisfied with your ending, try to find all 8 of them!")
    while True:
        end_choice = input("Would you like to quit?").strip().lower()
        if end_choice == "yes":
            exit()
        elif end_choice == "no":
            print("Restarting the game...")
            #used for restarting the program
            subprocess.call([sys.executable] + sys.argv)
        else:
            print("Please respond with 'yes' or 'no'")
            continue

def cowards_ending():
    #Call this function whenever user enters "run" as an option
    print("You achieved the cowards ending!")
    print("You bolt down the mountain and make a run for it, leaving all the villagers in the dust.")
    print("You read in the news paper next week that their town was destroyed with massive casualties.")

def not_my_problem_ending():
    print("You achieved the not my problem ending!")
    print("You could have taken on this quest, but who cares, right?")
    print(r"At the end of the day, it's not your problem anyway.¯\_(ツ)_/¯")

def betrayal_ending():
    print("You achieved the betrayal ending!")
    print("You took your opportunity to strike while the dragon's guard was lowered.")
    print("With one more swift attack, you have successfully slayed the dragon!")
    print("The town praises you as a hero, and they even hold a parade in your honor!")
    print("While you are flattered, you don't quite feel right about what you did...")

def best_friend_ending():
    print("You achieved the best friend ending!")
    print("You explain to the dragon that you do not want to hurt them, and that they were just lonely.")
    print("You tell them that you think they just need a friend.")
    print("The dragon nudges you up onto its back and begins to fly away.")
    print("You fly off into the sunset and live happily ever after with your new found friend.")

def you_tried_ending():
    print("You achieved the you tried ending!")
    print("You stayed in your hiding spot for too long.")
    print("The dragon eventually found you and killed you.")
    print("The dragon then went on an angry rampage and destroyed the village. But at least you tried...right?")

def heroes_ending():
    print("You achieved the heroes ending!")
    print("You slayed the dragon and saved the lives of the villagers!")
    print("While you were celebrating your victory, the walls of the cave collapsed in on themselves, crushing you to death.")
    print("Your sacrifice was worth saving the village. They put up a statue in your honor.")

def players_ending():
    print("You achieved the players ending!")
    print("The lovely compliment you gave the dragon alerted it to your presence.")
    print("Feeling so threatened by the mirror, it did not hesitate to swiftly kill you.")

def rogue_ending():
    print("You achieved the rogues ending!")
    print("By sheer luck, you were able to sneak your way out of the cave and barely escape with your life.")
    print("You decide to flee from the village in the dead of night so you are not caught abandoning your duties.")

def mage_spells():
    spell_list = ["Fireball", "Ice Knife", "Magic Missile"]
    print(*spell_list, sep=" | ")
    while True:
        (spell_choice) = input("Pick your spell:").strip().lower()
        if spell_choice == "fireball":
            print("You channel your magic and cast a powerful fireball at the dragon.")
            break
        elif spell_choice == "ice knife":
            print("You conjure up a ring of razor sharp ice shards and hurl them at the dragon's chest.")
            break
        elif spell_choice == "magic missile":
            print("You summon three glowing darts of magic energy and fling them towards the dragon.")
            break
        else:
            print("Now is not the time to fool around!")
            continue

def knight_weapons():
    weapon_list = ["Greatsword", "Mace", "Javelin"]
    print(*weapon_list, sep=" | ")
    while True:
        weapon_choice = input("Pick your weapon:").strip().lower()
        if weapon_choice == "greatsword":
            print("You draw your steel greatsword and slash at one of the dragon's wings.")
            break
        elif weapon_choice == "mace":
            print("You swing your heavy, spiked mace, dealing severe damage to the dragon's leg.")
            break
        elif weapon_choice == "javelin":
            print("You charge toward the dragon with your javelin in hand and stab it in the chest.")
            break
        else:
            print("Now is not the time to fool around!")
            continue

def rogue_skills():
    skill_list = ["Double Daggers", "Sneak Attack", "Duck and Roll"]
    print(*skill_list, sep=" | ")
    while True:
        skill_choice = input("Pick your skill:").strip().lower()
        if skill_choice == "double daggers":
            print("You grab your double daggers and dash beneath the dragon, injuring its leg.")
            break
        elif skill_choice == "sneak attack":
            print("You throw something to distract the dragon. While it's not looking, you slash at its side.")
            break
        elif skill_choice == "duck and roll":
            print("You easily avoid the dragon charging towards you, causing it to crash into the wall of the cave.")
            break
        else:
            print("Now is not the time to fool around!")
            continue

def attack():
    #Call this function on the first round of combat
    if player_class == "Mage":
        mage_spells()
    elif player_class == "Knight":
        knight_weapons()
    elif player_class == "Rogue":
        rogue_skills()

player_name= input("Welcome brave traveller! What is your name?").strip()
print("Greetings " + player_name)

class_list = ["Mage", "Knight", "Rogue"]

print("What is your class?")
print(*class_list, sep=" | ")

while True:
    player_class = input("Chose your class:").strip()
    if player_class == "Mage":
        print(player_class + ", Excellent choice!")
        break
    elif player_class == "Knight":
        print(player_class + ", Excellent choice!")
        break
    elif player_class == "Rogue":
        print(player_class + ", Excellent choice!")
        break
    else:
        print("Sorry, what was that?")
        continue

while True:
    choice = input("Are you ready to take on this quest?:").strip().lower()
    if choice == "yes":
        print("Great! Let me tell you about the history of Amethyst Cove...")
        break
    elif choice == "no":
        not_my_problem_ending()
        story_end()
    else:
        print("Sorry, what was that?")
        continue

print("Amethyst Cove is a beautiful seaside town known for the vibrant crystals jutting out from the cliffside.\n")
print("However, the town is in great danger. A local legend states that a powerful ancient gem dragon resides atop the tallest mountain.\n")
print("You have been tasked by the local adventurer's guild to take down this dragon. But first, you need some information...\n")

location_list = ["Talk to the locals", "Go to the Cedar and Smoke Tavern", "Go to the Ocean's Potions Magic Shop"]
print(*location_list, sep=" | ")
while True:
    location = input("Where would you like to go first?:").strip().lower()
    if location in ["talk to the locals", "talk to locals", "locals", "local"]:
        print("You find a fisherman sitting alone on a pier. He is an older man with a scruffy white beard. \n")
        print("'Oh, you're trying to fight that dragon? Its about time someone does something about that old beast...'\n")
        print("'He's been on that mountain for at least 500 years. I imagine he's pretty lonely up there...' \n")
        break

    elif location in ["go to the Cedar and Smoke Tavern", "go to the Tavern", "tavern", "go to tavern"]:
        print("You walk into a loud bustling tavern. It's a busy time of day. A band of goblins are playing some sea shanties while the bartender pours a brimming glass of ale.\n")
        print("The bartender greets you with a smile and says, 'So, I hear you're the brave new adventurer who is here to fix our city!' \n")
        print("'I will warn you... Any of my patrons who have attempted to slay the dragon never came back... I wish you the best of luck.'\n")
        break

    elif location in ["go to the ocean's potions magic shop", "go to the magic shop", "magic shop", "shop", "go to magic shop"]:
        print("You walk into an old and dusty shop. Rows of ancient looking books line rickety bookshelves. You see scattered notes and half filled potion bottles on a desk in the back of the shop. \n")
        print("A young elven woman with large, round glasses looks up at you. 'Hello and welcome to the Ocean's Potions Magic Shop! I've heard through the grape vine that a young traveler would be in town.' \n")
        print("'I'm afraid that I don't have much in stock right now, but I do have some advice! The dragon seems to be terrified of its own reflection. That's why it never leaves its cave.'\n")
        break

    else:
        print("Sorry, what was that? Please try again.")
        continue


print("With your new found information, you begin your trek up the town's tallest mountain.\n")
print("After what felt like hours of traveling, you make it to the mountain top. The cave is much larger than you expected.")

while True:
    cave_choice = input("Do you stay and fight, or do you run?:").strip().lower()
    if cave_choice == "run":
       cowards_ending()
       story_end()
    elif cave_choice == "fight":
        print("You slowly make your way into the cave.")
        print("Suddenly, you hear a deafening roar as the dragon locks eyes with you. It has large, deep purple amethyst gems for scales, and it looks like it's running straight for you!")
        break


fight_options_1 = ["Attack", "Run"]
print(*fight_options_1, sep=" | ")
while True:
    fight_choice_1 = input("What do you do?:").strip().lower()
    if fight_choice_1 == "attack":
        attack()
        break
    elif fight_choice_1 == "run":
        cowards_ending()
        story_end()
    else:
        print("Now's not the time to fool around!")
        continue

print("You're fighting well, but you're starting to get fatigued.")
print("Do you want to keep fighting or would you like to try to reason with the dragon?")

fight_options_2 = ["Attack", "Reason", "Run"]
print(*fight_options_2, sep=" | ")
while True:
    fight_choice_2 = input("What do you do?:").strip().lower()
    if fight_choice_2 == "attack":
        print("Before you continue fighting, you need to catch your breath.")
        print("You run and hide behind a nearby rock.")
        print("You stumble upon a skeleton of what you assume to be one of the dragon's last victims.")
        while True:
            fight_choice_3 = input("But wait! It's holding a mirror. Do you grab it and use it against the dragon?").strip().lower()
            if fight_choice_3 in ["yes", "y"]:
                print("You hold up the mirror and direct it at the dragon. It's stunned and completely frozen in place.")
                while True:
                    fight_choice_5 = input("Now's your chance! Do you finish the job or compliment the dragon on how they look in the mirror?").strip().lower()
                    if fight_choice_5 in ["fight","fighting","finish the job","finish job","job"]:
                        heroes_ending()
                        story_end()
                        break
                    elif fight_choice_5 in ["compliment","compliments","reason","talk"]:
                        players_ending()
                        story_end()
                        break
                    else:
                        print("Now's not the time to fool around!")
                        continue
            elif fight_choice_3 in ["no", "n"]:
                    if player_class == "Rogue":
                        chance = random.randint(1,20)
                        if chance > 15:
                            rogue_ending()
                            story_end()
                            break
                        elif chance <= 15:
                            you_tried_ending()
                            story_end()
                    else:
                        you_tried_ending()
                        story_end()
                        break
            else:
                print("Now's not the time to fool around!")
                continue
    if fight_choice_2 == "reason":
        print("You put your weapon down and your hands up.")
        print("You call out to the dragon and say that you dont want any trouble.")
        print("Calmly, you ask the dragon to leave the villagers be. The dragon does not look pleased doesn't rush to attack you.")
        while True:
            fight_choice_4 = input("Do you take this chance to keep talking, or do you cast the final blow?:").strip().lower()
            if fight_choice_4 in ["talk","keep talking","reason","talking"]:
                best_friend_ending()
                story_end()
                break
            elif fight_choice_4 in ["fight","keep fighting","fighting","final blow","cast the final blow", "cast final blow"]:
                betrayal_ending()
                story_end()
                break
            else:
                print("Now's not the time to fool around!")
                continue
    if fight_choice_2 == "run":
        cowards_ending()
        story_end()
    else:
        print("Now's not the time to fool around!")
        continue