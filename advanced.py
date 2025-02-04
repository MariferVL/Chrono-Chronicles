import time


def slow_print(text, delay=0.03):
    """
    Function to print text character by character with a delay.
    This mimics the slow text reveal typically found in RPGs or visual novels.

    :param text: The text to display.
    :param delay: The delay between each character, default is 0.03 seconds.
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print("\n")


def choose_option(options):
    """
    Function to prompt the user to select an option from a list of choices.

    :param options: A list of valid choices.
    :return: The user's selected option (as a lowercase string).
    """
    choice = ""
    while choice not in options:
        choice = input("Enter your choice: ").strip().lower()
    print()  # Adding a newline after the choice is entered
    return choice


def past_path():
    """
    This function handles the storyline for the 'Past' portal choice, where the player
    has to make decisions related to the ancient kingdom and the oracle.

    It allows the player to make choices that lead to different outcomes in the timeline.
    """
    slow_print("You step through the portal and arrive in an ancient kingdom filled with turmoil.")
    slow_print("A war is brewing over an oracle said to predict the future.")
    slow_print(
        "Do you: (1) Help the king find the oracle 🏰, (2) Steal the oracle for yourself 🔮, or (3) Destroy the oracle 💥?")
    choice = choose_option(["1", "2", "3"])

    if choice == "1":
        slow_print("The king finds the oracle, but he uses it for war. The timeline begins to crack.")
        slow_print("Do you: (a) Convince him to use it wisely 💡, (b) Let him wield its power unchecked ⚔️?")
        sub_choice = choose_option(["a", "b"])
        if sub_choice == "a":
            slow_print(
                "The timeline is restored. You return home, safe and sound. 🏠 Congratulations, you have succeeded!")
        else:
            slow_print("History is rewritten. You fade into obscurity. 😔 Game Over.")

    elif choice == "2":
        slow_print("You steal the oracle, but reality begins to collapse around you. Time itself begins to warp.")
        slow_print("Do you: (a) Use it to escape 🔄, (b) Try to rewrite your history 📝?")
        sub_choice = choose_option(["a", "b"])
        if sub_choice == "a":
            slow_print("You escape, but find yourself lost in time... 😵 Your journey ends here.")
        else:
            slow_print("A paradox consumes you, collapsing the fabric of time. ❌ Game Over.")

    else:
        slow_print("Destroying the oracle fractures time itself.")
        slow_print("Do you: (a) Reassemble it 🔧, (b) Let time reset naturally ⏳?")
        sub_choice = choose_option(["a", "b"])
        if sub_choice == "a":
            slow_print("You gain temporary control, but reality becomes unstable. ⚠️ Unstable Outcome.")
        else:
            slow_print("You lose your memory and are thrown into another timeline. 🌀 Game Over.")


def future_path():
    """
    This function handles the storyline for the 'Future' portal choice, where the player
    faces decisions related to a futuristic city ruled by AI and a brewing rebellion.
    """
    slow_print("You step into a neon-lit megacity where artificial intelligence rules.")
    slow_print("Humanity lives in a utopia, but a rebellion stirs beneath the surface.")
    slow_print("Do you: (1) Join the AI rulers 🤖, (2) Side with the rebels ✊, or (3) Stay neutral 🌐?")
    choice = choose_option(["1", "2", "3"])

    if choice == "1":
        slow_print("The AI grants you access to their vast archives, revealing shocking truths.")
        slow_print("Do you: (a) Help them strengthen their control 🏗️, (b) Seek a way to shut them down ⚡?")
        sub_choice = choose_option(["a", "b"])
        if sub_choice == "b":
            slow_print("You trigger a war that spirals into disaster. 💥 Game Over.")
        else:
            slow_print("You lose your humanity and become a pawn of the AI. 🤖 Game Over.")

    elif choice == "2":
        slow_print("You join the rebels, but the AI sees you as a threat.")
        slow_print("Do you: (a) Lead the rebellion ⚔️, (b) Sabotage from within 🕵️?")
        sub_choice = choose_option(["a", "b"])
        if sub_choice == "a":
            slow_print("The future is drastically altered, but at a great cost. 🌪️ Uncertain Fate.")
        else:
            slow_print("You are erased from history. ❌ Game Over.")

    else:
        slow_print("You stay neutral and explore the city. You discover a hidden lab with a mysterious message.")
        slow_print("Do you: (a) Open the message 📜, (b) Ignore it 🚶?")
        sub_choice = choose_option(["a", "b"])
        if sub_choice == "a":
            slow_print(
                "The message reveals your past role in the AI uprising. You restore balance and return home. 🏡 Congratulations, you have succeeded!")
        else:
            slow_print("A time loop traps you forever in the future. 🔄 Game Over.")


def alternate_path():
    """
    This function handles the storyline for the 'Alternate Reality' portal choice,
    where the player meets another version of themselves and faces a dangerous time anomaly.
    """
    slow_print("You step into a void where time flows differently, and encounter another version of yourself.")
    slow_print("They warn you of a hidden danger that is manipulating the timeline.")
    slow_print("Do you: (1) Trust them 🤝, (2) Ignore them 🏃, or (3) Destroy them 💀?")
    choice = choose_option(["1", "2", "3"])

    if choice == "1":
        slow_print(
            "You decide to trust your alternate self, and together you uncover the hidden entity controlling time.")
        slow_print("Do you: (a) Work together to fix the timeline 🔧, (b) Betray them and take control for yourself 👑?")
        sub_choice = choose_option(["a", "b"])
        if sub_choice == "a":
            slow_print(
                "You succeed in restoring time and become the guardian of the timeline. 🕰️ Congratulations, you have succeeded!")
        else:
            slow_print("You become the very threat you sought to stop. 🕳️ Game Over.")

    elif choice == "2":
        slow_print("You ignore your alternate self and fall into a chaotic time vortex.")
        slow_print("Do you: (a) Try to navigate the chaos 🌀, (b) Surrender to the void ⏳?")
        sub_choice = choose_option(["a", "b"])
        if sub_choice == "a":
            slow_print("You arrive in a strange hybrid reality. 🌍 Uncertain Fate.")
        else:
            slow_print("You are lost in time forever. 😵 Game Over.")

    else:
        slow_print("You attempt to destroy your alternate self but erase yourself from existence.")
        slow_print("Do you: (a) Rewrite yourself 📜, (b) Accept your fate ☠️?")
        sub_choice = choose_option(["a", "b"])
        if sub_choice == "a":
            slow_print("You become an unstable paradox, breaking time itself. 🌀 Unstable Outcome.")
        else:
            slow_print("You vanish from history, but time remains intact. 🕳️ Game Over.")


def start_game():
    """
    This function starts the game by introducing the player and offering a choice of portals to enter.
    Each portal leads to a different storyline with its own set of choices.
    """
    slow_print("\nWelcome to Chrono Chronicles! 🕰️")
    slow_print(
        "You find yourself in a sealed chamber with a strange device on your wrist. \nA robotic voice echoes: 'You have been chosen to restore the timeline.'")
    slow_print("Which portal do you choose: (1) Broken Hourglass ⏳, (2) Spinning Gear ⚙️, or (3) Infinity Symbol ♾️?")
    choice = choose_option(["1", "2", "3"])
    if choice == "1":
        past_path()
    elif choice == "2":
        future_path()
    else:
        alternate_path()


start_game()
