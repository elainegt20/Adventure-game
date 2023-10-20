import time
import random
import words


def print_pause(string):
    print(string)
    time.sleep(2)


def intro(creature, weapon):
    print_pause("You find yourself standing in a open field,"
                " filled with grass and yellow wildflowers.")
    replace(creature, weapon, "Rumor has it that a {{creature}}"
            " is somewhere around here, and"
            " has been terrifying the near by village.")
    print_pause("In front of you is a house.")
    print_pause("To your right there is a dark cave.")
    print_pause("In your hand you hold your trusty"
                " (but no very effective) dagger.")


def fight(been_here, creature, weapon):

    if "cave" in been_here:
        replace(creature, weapon, "As the {{creature}} moves to attack,"
                " you unsheath  your new {{weapon}}.")
        replace(creature, weapon, "The {{weapon}} shines brightly in your"
                " hand as you brace yourself  for the attack.")
        replace(creature, weapon, "But the {{creature}} takes one look"
                " at your shiny new toy and"
                " runs away!")
        replace(creature, weapon, "You have rid the town of the"
                " {{creature}}.You are victorious!")
        print_pause("You won!")
    else:
        replace(creature, weapon,
                "You do your best...\n"
                "but your dagger is not match for the {{creature}}.")
        print_pause("You have been defeated!")
        print_pause("Sorry, you lost :(")


def cave(been_here, creature, weapon):

    print_pause("You peer cautiously into the cave.")
    if "cave" in been_here:
        print_pause("You've been here before, and gotten all the good"
                    "stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field")

    else:

        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        replace(creature, weapon, "You have found the magical {{weapon}}!")
        replace(creature, weapon, "You discard your silly old dagger and take"
                " the {{weapon}} with you.")
        print_pause("You walk back out to the field.")


def field():
    print_pause("You run back into the field.Luckily, you don't"
                " seem to have been followed.\n\n")


def house(creature, weapon):
    print_pause("You approach the door of the house.")
    replace(creature, weapon, "You are about to knock when the door"
            " opens and out steps a  {{creature}}.")
    replace(creature, weapon, "Eep! this is a wicked {{creature}}'s house!")
    replace(creature, weapon, "The wicked {{creature}} attacks you!")
    print_pause("You feel a bit under-prepared for this, what"
                " with only having a tiny dagger.")


def play_again():
    again = input("Would you like to play again? (y/n) ").lower()

    if again == 'y':
        print_pause("Excellent! Restarting the game.")
        main()
    if again == 'n':
        print_pause("Thanks for playing! See you next time.")
    else:
        play_again()


def options():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")


def replace(creature, weapon, scenario):
    index = 0

    # weapon = random.choice(weapons)
    # creature = random.choice(creatures)

    add_character = []
    while index < len(scenario):

        if scenario[index:index + 12] == "{{creature}}":
            add_character.append(creature)
            index += 12
        elif scenario[index:index + 10] == "{{weapon}}":
            add_character.append(weapon)
            index += 10
        else:
            add_character.append(scenario[index])
            index += 1

    add_character = "".join(add_character)

    print_pause(add_character)


def play_game(been_here, creature, weapon):
    user_input = input("(Please enter 1 or 2).\n")

    if user_input == '1':

        house(creature, weapon)
        what_next = input("What you like to (1) fight or (2) run away?")

        if what_next == '1':

            fight(been_here, creature, weapon)

            play_again()

        elif what_next == '2':
            field()
            options()
            play_game(been_here, creature, weapon)
        else:
            play_again()

    elif user_input == '2':

        cave(been_here, creature, weapon)
        been_here.append("cave")
        options()
        play_game(been_here, creature, weapon)

    else:
        play_game(been_here, creature, weapon)


def main():
    creature = random.choice(words.creatures)
    weapon = random.choice(words.weapons)
    been_here = []
    intro(creature, weapon)
    options()
    play_game(been_here, creature, weapon)


main()
