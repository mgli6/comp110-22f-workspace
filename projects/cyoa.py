"""EX06-CYOA."""
__author__ = "730571410"


points: int = 0
player: str = ""
hp: int = 20
atk: int = 5
DOOR: str = "\U0001F6AA"
CLIMB: str = "\U00002B06"
DESCEND: str = "\U00002B07"
EXPLORE: str = "\U0001F50D"
GEM: str = "\U0001F48E"
DAGGER: str = "\U0001F5E1"
KEY: str = "\U0001F5DD"
SHIELD: str = "\U0001F6E1"
MONSTER: str = "\U0001F479"



def greet() -> None:
    """Greeting message."""
    global player 
    player = input("Please enter a player name to continue: ")
    print(f"{player} awakens in a stone tower.")
    print(f"Looking around, {player} sees a door, a set of stair leading upward, and a message written on the wall:")
    print("Do not leave without the treasure.")



def new_room() -> None:
    global points
    have_key: bool = False
    have_gem: bool = False
    playing_chest: bool = True
    playing_gem: bool = True
    print("The door opens into a new room.")
    print("The door locks behind you.")
    print("There is another set of stairs leading downward.")
    print(f"What will {player} do?")
    choice_one: str = input(f"1. Descend {DESCEND} \n2. Explore room {EXPLORE}\n")
    if choice_one == "2":
        print(f"You found a key!{KEY}")
        have_key = True
        print("Adventure points +2")
        points += 2
        choice_gem: str = input(f"1. Descend {DESCEND} \n2. Continue exploring {EXPLORE}\n")
        if choice_gem == "2":
            print(f"You found a strange gem! {GEM}")
            have_gem = True
            print("Adventure points +2")
            points += 2
        print("After exploring the room, you follow the stairs down into a maze like room")
    else:
        print("You follow in the stairs down into a maze like room")
        print("Zone: Catacombs")
        print("Adventure points + 1")
        points += 1
    print("You hear a rumbling noise")
    while playing_chest == True and playing_gem == True:
        print("The path branches left and right")
        choice_turn: str = input("1. Turn left \n2. Turn right\n")
        if choice_turn == "1":
            print("You turn left and follow the path to find a locked chest")
            if playing_chest == True:
                print("Adventure points +1")
                points += 1
            if have_key == True:
                print("Would you like to try and open the chest with the key?")
                choice_chest: str = input("1. Open chest\n2. Return start of path\n")
                if choice_chest == "1":
                    print("The chest opens and a mysterious powder flies out")
                    print("The world fades to black")
                    print("Game over")
                    print(f"You ended with {points} adventure points")
                    return
                else:
                    print("You return to where you started")
                    print("The rumbling gets louder")
                    playing_chest = False
            else:
                input("Perhaps the chest could be opened with some sort of key (Press enter to continue)")
                playing_chest = False
                print("You return to where you started")
                print("The rumbling gets louder")
        if choice_turn == "2":
            print("You turn right and follow the path to find a statue of a soldier with a missing eye")
            if playing_gem == True:
                print("Adventure points +1")
                points += 1
            if have_gem == True:
                print("Would you like to place the strange gem in the empty socket?")
                choice_eye: str = input("1. Place gem\n2. Return start of path\n")
                if choice_eye == "1":
                    print("The wall behind the statue collapses to reveal a huge pile of treasure!")
                    print("You win!")
                    print(f"You ended with {points} adventure points")
                    return
                else:
                    playing_gem = False
                    print("You return to where you started")
                    print("The rumbling gets louder")  
            else:
                input("Perhaps something could be placed there (Press enter to continue)")
                playing_gem = False
                print("You return to where you started")
                print("The rumbling gets louder")
    print("The catacombs collapses")
    print("The world fades to black")
    print("Game over")
    print(f"You ended with {points} adventure points")
    return



def combat(pts:int) -> int:
    points: int = pts
    monster_hp: int = 20
    monster_counter: int = 20
    monster_atk: int = 5
    in_combat: bool = True
    global hp
    global atk
    from random import randint
    print(f"A monster appears, blocking the stairs! {MONSTER}")
    print("Adventure points +1")
    points += 1
    print(f"{player} vs Monster")
    print(f"{player} stats: hp-{hp}, atk-{atk}")
    print(f"Monster stats: hp-{monster_hp}, atk-{monster_atk}")
    input("The monster attacks! (Press enter to engage in combat)")
    if points == 3:
        new_hp: int = 30
    else:
        new_hp: int = 20
    while in_combat == True:
        if new_hp >= 0 and in_combat == True:
            new_hp -= randint(1, 5)
            print(f"The monster did {hp - new_hp} damage!")
            hp = hp - (hp - new_hp)
            input(f"You have {hp}hp remaining! (Press enter to continue)")
        if monster_hp <= 0 or hp <= 0: 
                in_combat = False
        if monster_counter >= 0 and in_combat == True:
            monster_counter -= randint(1, atk)
            print(f"You attack and deal {monster_hp - monster_counter} damage!")
            monster_hp = monster_hp - (monster_hp - monster_counter)
            input(f"The monster has {monster_hp}hp remaining! (Press enter to continue)")
        if monster_hp <= 0 or hp <= 0: 
                in_combat = False
    if monster_hp <= 0:
        input("The monster has been defeated! (Press enter to continue)")
        print("Adventure points +5")
        points += 5
        print("You climb to the top of the tower and find a pile of treasure!")
        print("You win!")
    if hp <= 0:
        input("You lose! (Press enter to continue)")
        print("Game over")
    return points



def main() -> None:
    """Play the game."""
    global points
    global hp
    global atk
    global armor
    playing: bool = True
    greet()
    while playing == True:
        print(f"You have {points} adventure points")
        print(f"What will {player} do? (Input a number)")
        choice_one: str = input(f"1. Check the door {DOOR} \n2. Climb the stairs {CLIMB} \n3. Quit game\n")
        print(choice_one)
        if choice_one == "1":
            new_room()
        if choice_one == "2":
            print("You enter a new room with another set of stairs")
            print("Adventure points +1")
            points += 1
            choice_dagger: str = input(f"1. Climb the stairs {CLIMB} \n2. Explore room {EXPLORE}\n")
            if choice_dagger == "2":
                print(f"You found a dagger! {DAGGER}")
                print("atk +5")
                print("Adventure points +1")
                atk += 5
                points += 1
                choice_armor: str = input(f"1. Climb the stairs {CLIMB} \n2. Continue exploring {EXPLORE}\n")
                if choice_armor == "2":
                    print(f"You found a shield! {SHIELD}")
                    print("hp +10")
                    print("Adventure points +1")
                    hp += 10
                    points += 1
                print("You continue forward")
            points = combat(points)
            print(f"You ended with {points} adventure points")       
        if choice_one == "3":
            print(f"The world fades to black. \nYou ended with {points} adventure points. \nGoodbye.")
            playing = False
            quit()

        
    

if __name__ == "__main__":
    main()