class Mobile():
    def __init__(self, name):
        self.name = name
    def attack(self, attack_type):
        print("{name} {action} {attack_type} for {action_option} damage".format(name=self.name, action=self.action, attack_type=attack_type, action_option=self.action_options.get(attack_type, 0)))

class Wizard(Mobile):
    def __init__(self, name):
        super().__init__(name)
        self.c_class = "Wizard"
        self.hp = 80
        self.mp = 120
        self.action_options = {"Fireball": 2, "Magic Missile": 3, "Snowball": 4 }
        self.action = "Casts"
    
class Fighter(Mobile):
    def __init__(self, name):
        super().__init__(name)
        self.c_class = "Fighter"
        self.hp = 120
        self.mp = 80
        self.action_options = {"Sword": 2, "Mace": 3, "Halbred": 4 }
        self.action = "Swings"


class Monster(Mobile):
    def __init__(self, name, level):
        super().__init__(name)
        self.level = level
        self.hp = 5 * level


def character_creation():
    character_name = input("Enter name: ")
    character_selection = input("Choose class - (W)izard or (F)ighter: ")
    character_cut = character_selection[0].capitalize()
    character = build_character(character_name, character_cut)
    return character

def build_character(name, character_select):
    if character_select == "W":
       character = Wizard(name)
       return character       
    elif character_select == "F":
        character = Fighter(name)
        return character
    else:
        print("You entered an invalid class. Restarting character creation.")
        character_creation()

def new_monster(name, level):
    monster = Monster(name, level)
    return monster

character = character_creation()
monster = new_monster("Aardvark", 1)

continue_game = True
while continue_game:
    player_action = input("How will you handle the {monster_name}? {action_list} or X to exit: ".format(monster_name=monster.name, action_list=character.action_options.keys()))
    if player_action != "X":
        character.attack(player_action)
        damage_dealt = character.action_options.get(player_action)
        monster.hp -= damage_dealt
        if monster.hp <= 0:
            print("The {monster_name} has been slain!".format(monster_name=monster.name))
            continue_game = False
        else:
            print("The {monster_name} has {hp_remaining} hp remaining".format(monster_name=monster.name, hp_remaining=monster.hp))

    if player_action == "X":
        continue_game = False
