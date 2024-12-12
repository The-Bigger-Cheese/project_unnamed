import time, random, csv
import fn

save_key = ""
player_type = 69

while not player_type in [1, 2]:
    fn.printy("Press 1 for: NEW SAVE FILE")
    time.sleep(0.5)
    fn.printy("Press 2 for: EXISTING SAVE FILE")
    player_type = input("> ")
    if player_type.isdigit():
        player_type = int(player_type)

    else:
        fn.printy("ERROR: Invalid input")

    if player_type > 2 or player_type < 1:
        fn.printy("ERROR: Invalid input")

player_type = int(player_type)
if player_type == 1:
    while True:
        try:
            fn.printy("Choose a Save Key:")
            save_key = input("> ")
            open(f"data_{save_key}.txt")
            fn.printy("This Save Key already exists. Pick a different one.")
        except FileNotFoundError:
            break
    with open("active_save.txt", "w") as active:
        active.write(save_key)
    fn.printy(f"Your Save Key is: {save_key}")
    with open(f"data_{save_key}.txt", "w") as data:
        data.write(f"{save_key}\n{1}\n{20}\n{20}\n{10}\n{10}\n{5}\n{5}\n{5}\n{0}\n{0}\n{0}\n{1}\n{1}\n{1}")

    fn.printy("Skip Exposition? (Y/N)")
    skip = input("> ")
    while skip != "Y" and skip != "N":
        fn.printy("Input must be either Y or N.")
        skip = input("> ")
    
    if skip == "N":
        fn.printy("A young warrior stands outside his front door.\n")
        fn.printy("This young warrior has decided that today is the day he leaves the kingdom, in order to defeat the Dark Lord Malgazzo.")
        fn.printy("It just so happens that this young warrior is the one chosen by the Gods to take on this very task.")
        fn.printy("It was just over 14 years ago that this young warrior was given life, but it is only today that he will be given a name.")
        fn.printy("What is this young warrior's name?")
        fake_name = input("> ")
        if fake_name in ["Zoosmell Pooplord", "John Egbert", "Flighty Broad", "Rose Lalonde", "Insufferable Prick", "Dave Strider", "Farmstink Buttlass", "Jade Harley"]:
            fn.printy("Ah, I see you got the reference then.")
        
        fn.printy(f"This young warrior's name is {fake_name}. What is it that {fake_name} will do first?")
        time.sleep(3)
        fn.printy("The answer is, it doesn't matter.")
        fn.printy(f"It doesn't matter because you are not this young warrior. In fact, {fake_name} exists in an entirely separate world to your own.")
        fn.printy("You are a scientist. You sit at your desk, going over all of your research from the past couple of months, trying to make sense of it all.")
        fn.printy("What are these creatures? Why is all of this happening?")
        fn.printy("You think it's about time you went out into the field, in hopes of finding an answer to all of this.")
        fn.printy("Luckily, you happen to have a spare empty journal lying around, enabling you to document any findings.")

    try:
        with open(f"data_{save_key}.txt", "a") as data:
            data.write(f"\n{fake_name}")

    except NameError:
        with open(f"data_{save_key}.txt", "a") as data:
            data.write(f"\npenisface")

elif player_type == 2:
    while True:
        fn.printy("Enter Save Key:")
        save_key = input("> ")
        try:
            with open("active_save.txt", "w") as active:
                active.write(save_key)
                break

        except FileNotFoundError:
            fn.printy("There is no Save File on this device with that Save Key.")

while True:
    save_data = fn.stats.get(save_key)
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

    fn.printy("Your stats:")
    time.sleep(0.5)
    fn.printy(f"Level: {pl_lvl}")
    time.sleep(0.5)
    fn.printy(f"You need {xp_req - xp} more XP to reach Level {pl_lvl + 1}.")
    fn.printy(f"HP: {pl_hp} / {pl_max_hp}")
    time.sleep(0.5)
    fn.printy(f"MP: {mp} / {max_mp}")
    time.sleep(0.5)
    fn.printy(f"Attack: {pl_atk}")
    time.sleep(0.5)
    fn.printy(f"Defence: {pl_def}")
    time.sleep(0.5)
    fn.printy(f"Speed: {pl_spd}")
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

    fn.printy("What will you do?")
    fn.printy("<=0: Set off")
    fn.printy("==1: Shop")
    fn.printy("==2: Journal")
    fn.printy("==3: Lab")
    fn.printy(">=4: Gamble away your life savings")
    choice = input("> ")
    while not choice.isdigit():
        fn.printy("Enter a number from 0 to 4.")
        choice = input("> ")

    choice = int(choice)
    if choice <= 0:
        fn.printy("Where will you go?")

        for x in range(0, len(unlocked_level_nums)):
            print(f"{unlocked_level_nums[x]}: {unlocked_level_titles[x]}")
        
        fn.printy("Input Level number:")
        selected_level = input("> ")

        while True:
            try:
                selected_level = int(selected_level)
                while selected_level not in unlocked_level_nums:
                    raise ValueError
                break
            except:
                fn.printy("Please input a number shown above.")
                selected_level = input("> ")
        
        exec(open(f"level{selected_level}.py").read())

    elif choice == 1:
        exec(open("shop.py").read())