import random

def determine_damage(dice_count, sides_per_die):
    damage = 0
    for die in range(dice_count):
        rolled = random.randrange(1, sides_per_die) 
        print("You rolled a " + str(rolled))
        damage += rolled
    return damage


dice_max_size = 20
dice_min_size = 2
dice_max_count = 6
dice_min_count = 1

dice_count = random.randint(dice_min_count, dice_max_count)
sides = random.randint(dice_min_size, dice_max_size)
print("You rolled " + str(dice_count) + "D" + str(sides))

sub_total = determine_damage(dice_count, sides)
print("Rolled Damage: " + str(sub_total))


