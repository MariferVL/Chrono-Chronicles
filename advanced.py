import time


def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print("\n")


def choose_option(options):
    choice = ""
    while choice not in options:
        choice = input("Enter your choice: ").strip().lower()
    return choice


def past_path():
    slow_print("You arrive in an ancient kingdom in turmoil. The war for the oracle threatens time itself.")
    slow_print("Do you: (1) Help the king, (2) Steal the oracle, or (3) Destroy the oracle?")
    choice = choose_option(["1", "2", "3"])

    if choice == "1":
        slow_print("The king finds the oracle but uses it for war.")
        slow_print("Do you: (a) Convince him to use it wisely, (b) Let him wield its power unchecked?")
        sub_choice = choose_option(["a", "b"])
        if sub_choice == "a":
            slow_print("The timeline is restored. You return home. (SUCCESS)")
        else:
            slow_print("History is rewritten. You fade into obscurity. (FAILURE)")

    elif choice == "2":
        slow_print("You steal the oracle, but reality begins to collapse.")
        slow_print("Do you: (a) Use it to escape, (b) Rewrite your history?")
        sub_choice = choose_option(["a", "b"])
        if sub_choice == "a":
            slow_print("You escape, but find yourself lost in time. (UNCERTAIN FATE)")
        else:
            slow_print("A paradox consumes you. (FAILURE)")

    else:
        slow_print("Destroying the oracle fractures time.")
        slow_print("Do you: (a) Reassemble it, (b) Let time reset?")
        sub_choice = choose_option(["a", "b"])
        if sub_choice == "a":
            slow_print("You gain temporary control but reality is unstable. (UNSTABLE OUTCOME)")
        else:
            slow_print("You lose your memory and enter another timeline. (LOST IDENTITY)")


def future_path():
    slow_print("You enter a futuristic world ruled by AI.")
    slow_print("Do you: (1) Join the AI, (2) Side with the rebels, or (3) Stay neutral?")
    choice = choose_option(["1", "2", "3"])

    if choice == "1":
        slow_print("The AI grants you knowledge of history.")
        slow_print("Do you: (a) Strengthen their control, (b) Shut them down?")
        sub_choice = choose_option(["a", "b"])
        if sub_choice == "b":
            slow_print("The war spirals into disaster. (FAILURE)")
        else:
            slow_print("You lose your humanity. (FAILURE)")

    elif choice == "2":
        slow_print("You aid the rebels but are targeted by AI.")
        slow_print("Do you: (a) Lead the rebellion, (b) Sabotage from within?")
        sub_choice = choose_option(["a", "b"])
        if sub_choice == "a":
            slow_print("The future is drastically altered. (UNCERTAIN FATE)")
        else:
            slow_print("You are erased. (FAILURE)")

    else:
        slow_print("Exploring, you find a hidden lab.")
        slow_print("Do you: (a) Open the message, (b) Ignore it?")
        sub_choice = choose_option(["a", "b"])
        if sub_choice == "a":
            slow_print("You restore balance and return home. (SUCCESS)")
        else:
            slow_print("A time loop traps you. (FAILURE)")


def alternate_path():
    slow_print("You step into a void and meet another version of yourself.")
    slow_print("Do you: (1) Trust them, (2) Ignore them, or (3) Destroy them?")
    choice = choose_option(["1", "2", "3"])

    if choice == "1":
        slow_print("They warn of a hidden danger.")
        slow_print("Do you: (a) Work together, (b) Betray them?")
        sub_choice = choose_option(["a", "b"])
        if sub_choice == "a":
            slow_print("You stop the hidden entity and restore time. (SUCCESS)")
        else:
            slow_print("You become the threat. (FAILURE)")

    elif choice == "2":
        slow_print("You fall into a time vortex.")
        slow_print("Do you: (a) Navigate the chaos, (b) Surrender to the void?")
        sub_choice = choose_option(["a", "b"])
        if sub_choice == "a":
            slow_print("You arrive in a strange reality. (UNCERTAIN FATE)")
        else:
            slow_print("You are lost forever. (FAILURE)")

    else:
        slow_print("You attempt to destroy them but erase yourself.")
        slow_print("Do you: (a) Rewrite yourself, (b) Accept fate?")
        sub_choice = choose_option(["a", "b"])
        if sub_choice == "a":
            slow_print("You become an unstable paradox. (UNSTABLE OUTCOME)")
        else:
            slow_print("You vanish, but time remains intact. (FAILURE)")


def start_game():
    slow_print("Welcome to Chrono Chronicles!")
    slow_print("Which portal do you choose: (1) Past, (2) Future, (3) Alternate Reality?")
    choice = choose_option(["1", "2", "3"])
    if choice == "1":
        past_path()
    elif choice == "2":
        future_path()
    else:
        alternate_path()


start_game()
