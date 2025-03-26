import time, random, csv, pandas as pd
from fn import *

save_key = ""
player_type = 69

while not player_type in [1, 2]:
    printy("Press 1 for: NEW SAVE FILE")
    time.sleep(0.5)
    printy("Press 2 for: EXISTING SAVE FILE")
    player_type = input("> ")
    if player_type.isdigit():
        player_type = int(player_type)

    else:
        printy("ERROR: Invalid input")

    if player_type > 2 or player_type < 1:
        printy("ERROR: Invalid input")

player_type = int(player_type)
if player_type == 1:
    printy("Choose a Save Key:")
    save_key = input("> ")
    alldata = pd.DataFrame(pd.read_json("saves.json"))
    while True:
        for save in alldata:
            if save["key"] == save_key: # this bit doesn't work as it's taking "key" as the first item in the list rather than the dictionary containing all the save data. this means it's trying to *index* the string "key" instead of the dictionary. if it took the first item of the list to be the dictionary then i'm pretty sure it would take "key" as a perfectly valid index, with it being a literal key within the dictionary.
                printy("That Save Key already exists. Pick a different one.")
                save_key = input("> ")
                continue

        break

    with open("active_save.txt", "w") as active:
        active.write(save_key)
    printy(f"Your Save Key is: {save_key}")
    with open(f"data_{save_key}.txt", "w") as data:
        data.write(f"{save_key}\n{1}\n{20}\n{20}\n{10}\n{10}\n{5}\n{5}\n{5}\n{0}\n{0}\n{0}\n{1}\n{1}\n{1}")

    printy("Skip Exposition? (Y/N)")
    skip = input("> ")
    while skip != "Y" and skip != "N":
        printy("Input must be either Y or N.")
        skip = input("> ")
    
    if skip.upper() == "N":
        printy("A young warrior stands outside his front door.\n")
        printy("This young warrior has decided that today is the day he leaves the kingdom, in order to defeat the Dark Lord Malgazzo.")
        printy("It just so happens that this young warrior is the one chosen by the Gods to take on this very task.")
        printy("It was just over 14 years ago that this young warrior was given life, but it is only today that he will be given a name.")
        printy("What will be this young warrior's name?")
        fake_name = input("> ")
        if fake_name in ["Zoosmell Pooplord", "John Egbert", "Flighty Broad", "Rose Lalonde", "Insufferable Prick", "Dave Strider", "Farmstink Buttlass", "Jade Harley"]:
            printy("Ah, I see you got the reference then.")
        
        printy(f"This young warrior's name is {fake_name}. What is it that {fake_name} will do first?")
        time.sleep(3)
        printy("The answer is, it doesn't matter.")
        printy(f"It doesn't matter because you are not this young warrior. In fact, {fake_name} exists in an entirely separate world to your own.")
        printy("You are a scientist. You sit at your desk, going over all of your research from the past couple of months, trying to make sense of it all.")
        printy("What are these creatures? Why is all of this happening?")
        printy("You think it's about time you went out into the field, in hopes of finding an answer to all of this.")
        printy("Luckily, you happen to have a spare empty journal lying around, enabling you to document any findings.")

    try:
        with open(f"data_{save_key}.txt", "a") as data:
            data.write(f"\n{fake_name}")

    except NameError:
        with open(f"data_{save_key}.txt", "a") as data:
            data.write(f"\npenisface")

elif player_type == 2:
    while True:
        printy("Enter Save Key:")
        save_key = input("> ")
        try:
            with open("active_save.txt", "w") as active:
                active.write(save_key)
                break

        except FileNotFoundError:
            printy("There is no Save File on this device with that Save Key.")

while True:
    save_data = stats.get(save_key)
    pl_lvl = int(save_data[1])
    pl_hp = int(save_data[2])
    pl_max_hp = int(save_data[3])
    mp = int(save_data[4])
    max_mp = int(save_data[5])
    pl_atk = int(save_data[6])
    pl_def = int(save_data[7])
    pl_spd = int(save_data[8])
    xp = int(save_data[9])
    xp_req = int(round(((1.25 ** pl_lvl) + 10), 0))
    levels_cleared = int(save_data[10])
    chits = int(save_data[11])
    pl_atk_multi = float(save_data[12])
    pl_def_multi = float(save_data[13])
    pl_spd_multi = float(save_data[14])

    printy("Your stats:")
    time.sleep(0.5)
    print(f"Level: {pl_lvl}")
    time.sleep(0.5)
    print(f"You need {xp_req - xp} more XP to reach Level {pl_lvl + 1}.")
    print(f"HP: {pl_hp} / {pl_max_hp}")
    time.sleep(0.5)
    print(f"MP: {mp} / {max_mp}")
    time.sleep(0.5)
    print(f"Attack: {pl_atk}")
    time.sleep(0.5)
    print(f"Defence: {pl_def}")
    time.sleep(0.5)
    print(f"Speed: {pl_spd}")
    time.sleep(0.5)

    with open("levels.csv") as levels:
        levels = csv.reader(levels)
        unlocked_level_nums = []
        unlocked_level_titles = []
        for row in levels:
            if int(row[0]) <= levels_cleared + 1:
                level_num = row[0]
                level_title = row[1]
                unlocked_level_nums.append(int(level_num))
                unlocked_level_titles.append(level_title)

            else:
                break

    printy("What will you do?")
    print("<=0: Set off")
    print("==1: Shop")
    print("==2: Journal")
    print("==3: Lab")
    print(">=4: Gamble away your life savings")
    choice = input("> ")
    while not choice.isdigit():
        printy("Enter a number from 0 to 4.")
        choice = input("> ")

    choice = int(choice)
    if choice <= 0:
        printy("Where will you go?")

        for x in range(0, len(unlocked_level_nums)):
            print(f"{unlocked_level_nums[x]}: {unlocked_level_titles[x]}")
        
        printy("Input Level number:")
        selected_level = input("> ")

        while True:
            try:
                selected_level = int(selected_level)
                while selected_level not in unlocked_level_nums:
                    raise ValueError
                break
            except:
                printy("Please input a number shown above.")
                selected_level = input("> ")
        
        exec(open(f"level{selected_level}.py", encoding = "utf8").read())

    elif choice == 1:
        exec(open("shop.py").read())

    elif choice == 2:
        exec(open("journal.py").read())