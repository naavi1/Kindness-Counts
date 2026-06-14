import sys
import time

# -- Global Game State --

name = ""
aura = 10


def start_game():
    global name, aura
    print("Hello!")
    name = input("What's your name? \n>").capitalize()
    print("\nWelcome to Kindness Counts, ", name)
    age = int(input("\nHow old are you? \n>"))
    aura = 10

    if age >= 18:
        print(
            "\nYou are old enough to play! You are starting with ", aura, "aura points"
        )
    else:
        print("\nSorry, you're a baby.")
        sys.exit()

    wants_to_play = input("Do you want to play? (Y/N) \n>").upper()
    if wants_to_play == "Y":
        print("Yay! Let's go!")
        print()
        story_introduction()
    else:
        print("Thanks for stopping by!")
        sys.exit()


def story_introduction():
    print(
        f"""Once upon a time, there lived a kind young woman named {name}.
After the death of her father, she was forced to live with
her cruel stepmother and two selfish stepsisters."""
    )
    time.sleep(4)
    print()
    print(
        f"""While they enjoyed a life of comfort, {name.capitalize()} spent her days
cooking, cleaning, and doing endless chores."""
    )
    time.sleep(4)
    print()
    print(f"Despite the hardships, {name} never lost her kindness or hope.")
    print()

    # --- The Announcement ---
    print(
        "One sunny morning, a royal messenger rode through the village, carrying exciting news:"
    )
    time.sleep(3)
    print()
    print(
        """Hear ye, hear ye! he shouted.
By royal proclamation, His Majesty the King commands that
every eligible maiden in the land attend the royal ball tonight"""
    )
    time.sleep(4)

    # --- Player Reflection ---
    print(" ")
    print("Your heart skips a beat. A chance to visit the palace...")
    time.sleep(3)
    print(" ")
    print("A chance to dance... \nA chance for your life to change forever...")
    time.sleep(5)
    print(
        "\nYour stepmother narrows her eyes and smiles coldly. \nOh, you'll only attend if every chore is completed, she says."
    )
    time.sleep(3)
    print("\nShe drops a long list of tasks onto the table.")
    time.sleep(3)

    main_choice()


def main_choice():
    global aura
    print(
        "What will you do?\n1. Start the chores immediately.\n2. Ask your stepsisters for help.\n3. Sneak away to learn more about the royal ball."
    )
    choice = int(input("""What do you pick? 1/2/3: 
        >"""))
    time.sleep(2)

    if choice == 1:
        choice_1_start_chores()
    elif choice == 2:
        choice_2_ask_sisters()
    elif choice == 3:
        choice_3_sneak_away()
    else:
        print("Invalid")
        main_choice()
        return


# -- BRANCH 1: Start Chores Immediately --


def choice_1_start_chores():
    global aura
    aura += 5
    print(" ")
    print(
        "You roll up your sleeves and get to work. \nThe kitchen is a mess, the floors are dusty, and the laundry basket is overflowing. \nAfter several hours of hard work, you hear laughter from the garden. \nYour stepsisters are enjoying tea while you do all the work.")
    time.sleep(3)
    print("You wipe sweat from your forehead and glance at the clock. \nYou still have time before sunset.")
    print(
        "What do you do?\n1. Continue working\n2. Confront your stepsisters.\n3. Take a short break"
    )
    choice2 = int(input("What do you pick? 1, 2 or 3: "))

    if choice2 == 1:
        aura += 2
        print(" ")
        print(
            "You swallow your pride, roll up your sleeves, and get to work. The kitchen is a \nmess, the floors are dusty, and the laundry basket is overflowing. OOF... You begin working"
        )
        finish_chores_and_meet_old_woman()

    elif choice2 == 2:
        aura -= 3

        print(
            f"\nThe sisters laugh in your face and make fun of you. You lost 3 aura points. You have {aura} points now\n"
        )
        print()
        print("What do you do now?\n1. Continue working\n3. Sneak away")
        choice2_sub = int(input("What do you pick? 1 or 3: "))

        if choice2_sub == 1:
            print(" ")
            print("\nYou swallow your pride and go back to work.")
            finish_chores_and_meet_old_woman()
        elif choice2_sub == 3:
            attic_game_over()

    elif choice2 == 3:
        print(
            "You decide to rest. However, your stepmother catches you slacking off! \nShe locks you up in the attic as punishment for not finishing your chores. You lost."
        )
        attic_game_over()


# -- BRANCH 2: Ask Stepsisters for Help --


def choice_2_ask_sisters():
    global aura
    aura -= 3
    print(
        f"\nThe sisters laugh in your face and make fun of you. You lost 3 points. You have {aura} points now."
    )
    print()
    print("What do you do now?\n1. Start working\n3. Sneak away")
    choice2 = int(input("What do you pick? 1 or 3: "))

    if choice2 == 1:
        aura += 2
        print(" ")
        print(
            "\nYou swallow your pride, roll up your sleeves, and get to work. The kitchen is a mess, the floors are dusty, and the laundry basket is overflowing. OOF... You begin working"
        )
        finish_chores_and_meet_old_woman()
    elif choice2 == 3:
        attic_game_over()


# -- BRANCH 3: Sneak Away Immediately --


def choice_3_sneak_away():
    print(
        "You get caught while escaping through the backdoor by your stepmother. \nShe locks you up in the attic as punishment. No happily ever after for you."
    )
    attic_game_over()


# -- THE CONTINUATION (Where successful paths meet) --


def finish_chores_and_meet_old_woman():
    global aura
    time.sleep(10)
    print(
        f"\nAfter hours of hard work and a lot of sweat, {name} was finally done with all the chores"
    )
    time.sleep(4)
    print(
        "\nYou sneak outside to relax and sit beneath an old oak tree. \nAs the breeze rustles the leaves, you notice an elderly woman struggling to carry a basket."
    )
    time.sleep(3)
    choice3 = int(input("What do you do? (1/2)\n1. Help her.\n2. Ignore her.\n"))

    if choice3 == 1:
        aura += 10
        print(
            "You rush over and carry the basket for her. The woman smiles warmly. \nKindness is always rewarded, she says mysteriously. \nBefore leaving, she gives you a small crystal charm."
        )
    elif choice3 == 2:
        aura -= 5
        print(
            "You decide you don't have time. The woman walks away silently. \nFor some reason, you feel guilty."
        )

    market_trip()


def market_trip():
    global aura
    print()
    time.sleep(4)
    print(
        "Later that evening, for some more chores, your cruel stepmother asks \nyou to go to the market to buy her daughters gowns for the ball"
    )
    choice4 = input("Do you comply? (Y/N) ").upper()

    if choice4 == "Y":
        aura += 3
        print(f"She hands you money and orders you to go. Your aura is now {aura}.")
    elif choice4 == "N":
        aura -= 3
        print(
            f"She screams at you and orders you to go anyway. \nYou lost 3 aura points. Your aura is now {aura}."
        )

    time.sleep(4)
    print("{Arriving at the market}")
    print(
        "\nAs you arrive at the market, the air is filled with excitement and chatter. Villagers hurry between stalls, gathering ribbons, flowers, and fine fabrics for the Prince's upcoming ball."
    )
    print()
    time.sleep(2)
    print("\nYou make your way to the finest gown shop in the village")
    print()

    old_man()


def old_man():
    global aura
    print(
        """As you walk through the market, you notice an old man sitting beside a fountain.
His clothes are torn, and he looks weak.
'Please...' he says softly. 'I haven't eaten in two days.'"""
    )

    print("1. Buy him food\n2. Give him a small coin\n3. Ignore him")
    choice_oldman = int(input("What do you do? (1/2/3): "))

    if choice_oldman == 1:
        aura += 10
        print(
            "You buy him a warm meal. He smiles as if he hasn't felt kindness in years."
        )
    elif choice_oldman == 2:
        aura += 5
        print("You give him some coins. It's not much, but he thanks you deeply.")
    elif choice_oldman == 3:
        aura -= 5
        print("You walk away. Something about his eyes stays with you.")

    time.sleep(2)

    little_girl()


def little_girl():
    global aura, name
    print(" ")
    print("After collecting the gowns, you start to make your way back home")
    time.sleep(3)
    print(
        """On your way back, you spot a small girl crying near a stall.
'I lost my ribbon for the ball...' she sobs."""
    )
    print()
    print("1. Help her find it\n2. Buy her a new one\n3. Ignore her")
    choice_girl = int(input("What do you do? (1/2/3): "))

    if choice_girl == 1:
        aura += 7
        time.sleep(3)
        print("You help her search until you find it tucked under a crate.")
    elif choice_girl == 2:
        aura += 10
        time.sleep(3)
        print("You buy her a beautiful ribbon. She hugs you happily.")
    elif choice_girl == 3:
        aura -= 5
        time.sleep(3)
        print("You leave her crying.")

    backhome()


def backhome():
    global aura
    print("You return home with fine gowns for your stepsisters and stepmother.")
    print()
    print(
        "They rush forward, snatching the dresses from your \nhands without a word of thanks."
    )
    print()
    time.sleep(2)
    print("You hesitate for a moment before speaking softly...")
    print()
    time.sleep(2)
    print('"May I... come with you to the ball?"')
    print()
    time.sleep(2)
    print("They burst into laughter and turn away, already admiring their dresses.")

    print(
        f"{name} retreats back upstairs to the attic, the sound of laughter fading behind her."
    )

    time.sleep(3)

    print(
        """You close the door behind you.

In front of you is a small mirror, a bed, and a box of old fabric scraps and thread.

What do you do?"""
    )

    choice_dress = int(
        input("1. Sit by the window\n2. Stitch up a dress with what you can find\n> ")
    )

    if choice_dress == 1:
        aura -= 2
        print()
        time.sleep(3)
        print(
            """You sit by the window, watching the lights of the house flicker below.
The thought of the ball feels like it belongs to another world... not yours."""
        )
        garden_scene()
        return

    elif choice_dress == 2:
        aura += 8
        time.sleep(3)
        print()
        print(
            """You gather scraps of old fabric, ribbons, and thread.
If you cannot have a dress... you will try to make one yourself."""
        )
        ripscene()
        return

    else:
        print("Invalid Choice")
        backhome()
        return


def garden_scene():
    global aura

    time.sleep(2)

    print()
    print("Hours pass.")
    time.sleep(2)
    print("\nSoon, you hear the carriage carrying your stepmother and sisters away.")
    print()
    time.sleep(2)
    print("The house falls silent.")
    print()
    time.sleep(2)
    print(f"{name} wipes away a tear and wanders into the garden.")
    print()
    time.sleep(2)
    print("The palace lights shine in the distance.")
    print()
    time.sleep(3)
    print("A warm glow appears beside her.")
    print()
    time.sleep(3)
    print("'Why do you cry, my dear?' a gentle voice asks.")
    time.sleep(2)
    print(f"'Who are you?' {name} asks")
    print()
    print("The Fairy Godmother has arrived.")

    fairy_godmother()


def ripscene():
    global aura

    print(
        f"After hours of sewing with old fabric, {name} finishes a simple pink dress."
    )
    time.sleep(2)
    print()
    print(
        f"{name} walks downstairs as her stepmother and sisters prepare for the ball."
    )
    time.sleep(1)

    print("For a moment, they stare in silence.")
    time.sleep(3)
    print("Then the laughter starts.")
    print()
    time.sleep(2)
    print("'That's your dress?' Drizella mocks.")

    time.sleep(2)

    print("Suddenly, Anastasia steps \nforward and grabs the fabric.")
    print()
    time.sleep(2)
    print("RIP!")
    time.sleep(3)
    print()
    print("The dress tears apart.")
    time.sleep(2)
    aura -= 5
    print("\nYou lost 5 aura points")
    print()
    time.sleep(2)
    print("Current aura points: ", aura)
    print()
    time.sleep(2)
    print(f"{name} is shoved back as they leave laughing.")
    print()
    print(f"{name} runs out into the garden, tears falling.")

    time.sleep(2)

    print("The night is quiet. The palace lights shine far away... too far.")
    print()
    time.sleep(3)
    print("A warm glow appears beside her.")
    print()
    time.sleep(3)
    print("'Why do you cry, my dear?' a gentle voice asks.")
    time.sleep(2)
    print(f"'Who are you?' {name} asks")
    print()
    print("The Fairy Godmother has arrived.")

    fairy_godmother()


def fairy_godmother():
    global aura

    print()
    time.sleep(2)

    print("'I am your Fairy Godmother,' she says with a smile.")
    time.sleep(3)
    if aura <= 15:
        print()
        print("'My dear, magic can only grow where kindness has been nurtured.'")
        time.sleep(2)
        print(
            "'You still have goodness in your heart, but tonight there is not enough magic for a transformation.'"
        )
        print()
        time.sleep(3)
        print("The glow fades.")
        print()
        time.sleep(3)
        print(f"{name} spends the evening watching the palace lights from afar.")
        print()
        print("ENDING: A lesson learnt...kindness is magic")
        print()
        play_again_screen()

    elif aura > 15 and aura < 30:
        print("'You have shown kindness today.'")
        time.sleep(2)
        print("'I cannot grant you everything, but I can give you a chance.'")
        time.sleep(3)
        print()
        print("✨ Simple magic surrounds you. ✨")
        time.sleep(2)
        print("✨ Your clothes become suitable for the ball. ✨")
        print()

        ball_arrival("partial")

    elif aura >= 30:
        print()
        print("'You have shown kindness even when others showed none.'")
        print("'Tonight, magic shall reward you.'")
        time.sleep(2)
        print()
        print("✨ A beautiful gown appears. ✨")
        time.sleep(3)
        print("✨ Glass slippers sparkle on your feet. ✨")
        time.sleep(3)
        print("✨ A magnificent carriage appears at the gate. ✨")
        print()

        ball_arrival("full")


def ball_arrival(transformation):
    global aura

    time.sleep(2)

    print("Soon, you arrive at the royal palace.")
    print("\nMusic spills from the ballroom.")
    print("\nAura Points:", aura)

    if transformation == "partial":
        aura -= 5
        print()
        print("Your stepmother notices you immediately.")
        time.sleep(2)
        print("'What are YOU doing here?!' she snaps.")
        time.sleep(1)

        if aura >= 25:
            print("Before she can continue, a royal guard steps between you.")
            print("'\nAll guests are welcome at the Prince's ball.'")
            time.sleep(3)
        else:
            print("She spends the evening trying to embarrass you.")
            print("\nYou do your best to ignore her.")
            aura -= 2
            time.sleep(3)

    else:
        print()
        print(
            "Your stepmother and sisters stare in shock. You look even more beautiful than before."
        )
        print("\nFor once, they are speechless.")
        print()

    time.sleep(2)

    print("You take a deep breath and step into the ballroom.")
    print()
    time.sleep(2)
    print("Crystal chandeliers sparkle overhead.")
    time.sleep(2)
    print("The room is filled with music, laughter, and swirling gowns.")
    print()

    time.sleep(2)

    print("For a moment, you simply stand there.")
    time.sleep(2)
    print("This is the world you dreamed about from your attic window.")
    print()

    time.sleep(2)

    print("Then you notice someone watching you.")
    print()
    time.sleep(2)
    print("The Prince.")
    print()

    prince_scene()


def prince_scene():
    global aura
    time.sleep(5)
    print("The Prince makes his way through the crowd toward you.")
    print()

    time.sleep(2)

    print("\n'I don't believe we've met,' he says with a smile.")
    print("\n'Would you care to dance?'")

    print()
    choice = int(input("1. Accept\n2. Politely decline\n> "))

    if choice == 1:
        aura += 5

        print()
        print("You place your hand in his.")
        print()
        print("\nAs the music begins, the two of you glide across the ballroom floor.")
        print()
        print("\nHours seem to pass in minutes.")
        print()
        print(
            "\nThe Prince laughs at your stories and listens carefully to every word."
        )

    else:
        aura += 10

        print()
        print("'Perhaps later,' you reply politely.")
        print()
        print("\nThe Prince seems surprised by your honesty.")
        print()
        print("\n'Then perhaps we can simply talk.'")

    final_test()


def final_test():
    global aura

    print()
    time.sleep(2)

    print("As the evening continues, a commotion breaks out nearby.")
    print()
    time.sleep(2)

    print("A young servant trips while carrying refreshments.")
    time.sleep(2)
    print("Silver trays crash onto the marble floor.")
    time.sleep(2)
    print()
    time.sleep(2)
    print("Several guests laugh.")

    print()
    time.sleep(2)
    print("What do you do?")
    print("1. Help the servant clean up.")
    print("2. Comfort the servant.")
    print("3. Ignore it and continue enjoying the ball.")

    choicefin = int(input("> "))

    if choicefin == 1:
        aura += 20
        print()
        print(
            "Without hesitation, you kneel beside the servant and help gather the scattered dishes."
        )
        print()
        print("\n'Thank you,' he whispers.")
        print("A voice speaks from behind you.")
        time.sleep(2)
        print("'That was very kind of you.'")

    elif choicefin == 2:
        aura += 10

        print()
        print("'Everyone makes mistakes,' you tell him.")
        print()
        time.sleep(1)
        print("\nThe servant's shoulders relax.")
        print("A voice speaks from behind you.")
        time.sleep(2)
        print("'That was very kind of you.'")

    else:
        aura -= 5

        print()
        print("You decide it isn't your problem.")

    ending()


def ending():
    global aura
    print()
    time.sleep(3)

    print()
    time.sleep(2)
    print("You turn around.")
    time.sleep(2)
    print("The Prince has witnessed everything.")

    if aura > 30:
        print()
        print("The Prince smiles warmly.")
        time.sleep(2)
        print()
        print("'All evening I have watched how you treat others.'")
        time.sleep(2)
        print("'Not servants. Not nobles. People.'")
        time.sleep(2)
        print()
        print("'Kindness cannot be sewn into a gown.'")
        time.sleep(1)
        print("'Nor can it be granted by magic.'")
        time.sleep(2)
        print()
        print("'It comes from the heart.'")
        print()
        time.sleep(2)
        print("The Prince turns toward the crowd.")
        time.sleep(2)
        print()
        print("'I have made my choice.'")
        time.sleep(5)
        print()
        print(f"'I choose {name} to be my Princess.'")
        time.sleep(5)
        print()
        print("The ballroom erupts into cheers.")
        print()
        print("Your stepmother and stepsisters stand frozen in disbelief.")
        print()
        print("ENDING: Happily Ever After")

    else:
        print()
        print("'You have a good heart,' the Prince says.")
        print()
        time.sleep(2)
        print("'But every journey begins somewhere.'")
        print()
        time.sleep(2)
        print("'I hope our paths cross again.'")
        print()
        time.sleep(2)
        print("You leave the palace with hope in your heart.")
        print()
        print("ENDING: A Night To Remember")

    play_again_screen()


def attic_game_over():
    print("\n🔒 You are locked in the attic. Your story ends here.")
    play_again_screen()


def play_again_screen():
    choice = input("\nWould you like to play again? (Y/N): ").upper()
    if choice == "Y":
        start_game()
    else:
        print("Thanks for playing!")
    sys.exit()


start_game()
