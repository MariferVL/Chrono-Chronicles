import time

# Introduction to the game
print("\nWelcome to Chrono Chronicles! 🕰️\n")
time.sleep(1)
print(
    "You find yourself in a sealed chamber with a strange device on your wrist. \nA robotic voice echoes: "
    "'You have been chosen to restore the timeline.'")
time.sleep(1)
print("Which portal do you choose: (1) Broken Hourglass ⏳, (2) Spinning Gear ⚙️, or (3) Infinity Symbol ♾️?")
time.sleep(1)

choice = input("Enter your choice: ").strip()

# Path based on the player's choice
if choice == "1":  # Past Portal
    print("You step through the portal and arrive in an ancient kingdom filled with turmoil.")
    time.sleep(1)
    print("A war is brewing over an oracle said to predict the future.")
    time.sleep(1)
    print(
        "Do you: (1) Help the king find the oracle 🏰, (2) Steal the oracle for yourself 🔮, or (3) Destroy the oracle 💥?")
    time.sleep(1)

    choice = input("Enter your choice: ").strip()

    if choice == "1":  # Help the king
        print("The king finds the oracle, but he uses it for war. The timeline begins to crack.")
        time.sleep(1)
        print("Do you: (a) Convince him to use it wisely 💡, (b) Let him wield its power unchecked ⚔️?")
        time.sleep(1)

        choice = input("Enter your choice: ").strip()

        if choice == "a":  # Convince him
            print("The timeline is restored. You return home, safe and sound. 🏠 Congratulations, you have succeeded!")
        else:  # Let him wield unchecked
            print("History is rewritten. You fade into obscurity. 😔 Game Over.")

    elif choice == "2":  # Steal the oracle
        print("You steal the oracle, but reality begins to collapse.")
        time.sleep(1)
        print("Do you: (a) Use it to escape 🔮, (b) Rewrite your history 📝?")
        time.sleep(1)

        choice = input("Enter your choice: ").strip()

        if choice == "a":  # Escape
            print("You escape, but find yourself lost in time. 🌌 Uncertain fate!")
        else:  # Rewrite history
            print("A paradox consumes you. 😱 Game Over.")

    else:  # Destroy the oracle
        print("You destroy the oracle, causing time to fracture.")
        time.sleep(1)
        print("Do you: (a) Reassemble it 🔧, (b) Let time reset naturally 🔄?")
        time.sleep(1)

        choice = input("Enter your choice: ").strip()

        if choice == "a":  # Reassemble it
            print("You gain temporary control, but reality is unstable. ⚠️ Unstable outcome!")
        else:  # Let time reset
            print("You lose your memory and enter another timeline. ❓ Lost identity!")

elif choice == "2":  # Future Portal
    print("You step through the portal and arrive in a futuristic world ruled by AI.")
    time.sleep(1)
    print("Humanity exists in a controlled utopia, but a rebellion is brewing underground.")
    time.sleep(1)
    print("Do you: (1) Join the AI rulers 🤖, (2) Side with the rebels ✊, or (3) Stay neutral and explore 👀?")
    time.sleep(1)

    choice = input("Enter your choice: ").strip()

    if choice == "1":  # Join the AI rulers
        print("The AI grants you knowledge of history, but also begins to control you.")
        time.sleep(1)
        print("Do you: (a) Strengthen their control ⚙️, (b) Try to shut them down 💥?")
        time.sleep(1)

        choice = input("Enter your choice: ").strip()

        if choice == "b":  # Try to shut them down
            print("The war spirals into disaster. ⚠️ Game Over.")
        else:  # Strengthen control
            print("You lose your humanity. 😢 Game Over.")

    elif choice == "2":  # Side with the rebels
        print("You aid the rebels, but the AI sees you as a threat.")
        time.sleep(1)
        print("Do you: (a) Lead the rebellion 💪, (b) Sabotage from within 🛠️?")
        time.sleep(1)

        choice = input("Enter your choice: ").strip()

        if choice == "a":  # Lead the rebellion
            print("The future is drastically altered. 🌟 Uncertain fate!")
        else:  # Sabotage from within
            print("You are erased by the AI. 💥 Game Over.")

    else:  # Stay neutral
        print("You explore and discover a hidden lab with a message for you.")
        time.sleep(1)
        print("Do you: (a) Open the message 📜, (b) Ignore it 🚶?")
        time.sleep(1)

        choice = input("Enter your choice: ").strip()

        if choice == "a":  # Open the message
            print(
                "You learn that you were responsible for the AI uprising. You find a way to restore balance. ✔️ Success!")
        else:  # Ignore the message
            print("A time loop traps you forever. ⏳ Game Over.")

else:  # Alternate Reality Portal
    print("You step into a void where time flows differently and meet another version of yourself.")
    time.sleep(1)
    print("They warn you about a hidden danger that threatens the timeline.")
    time.sleep(1)
    print(
        "Do you: (1) Trust them and work together 🤝, (2) Ignore them and move forward 🚶, or (3) Try to destroy them 💣?")
    time.sleep(1)

    choice = input("Enter your choice: ").strip()

    if choice == "1":  # Trust them
        print("Together, you restore the timeline and stop the hidden threat. ✔️ Success!")
        time.sleep(1)
    elif choice == "2":  # Ignore them
        print("You fall into a time vortex. 🌪️ Uncertain fate!")
    else:  # Destroy them
        print("You unknowingly erase yourself from existence. 💀 Game Over.")

