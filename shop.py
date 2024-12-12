import fn

with open("active_save.txt", "r") as active:
    save_key = active.read()
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
    xp_req = int(round(((1.5 ** pl_lvl) + 10), 0))
    levels_cleared = int(save_data[10])
    chits = int(save_data[11])
    pl_atk_multi = float(save_data[12])
    pl_def_multi = float(save_data[13])
    pl_spd_multi = float(save_data[14])

fn.printy("welcome to my shop, what can i do for you today?")         
while True:
    atk_upg_cost = int(round(((1.5 ** ((pl_atk_multi -1) * 100) + 10)), 0))
    def_upg_cost = int(round(((1.5 ** ((pl_def_multi -1) * 100) + 10)), 0))
    spd_upg_cost = int(round(((1.5 ** ((pl_spd_multi -1) * 100) + 10)), 0))  
    fn.printy(f"<=1: upgrade attack - {atk_upg_cost}C")
    fn.printy(f"==2: upgrade defence - {def_upg_cost}C")
    fn.printy(f"==3: upgrade speed - {spd_upg_cost}C")
    fn.printy(">=4: Leave")
    fn.printy(f"(You currently have {chits} Chits.)")
    choice = input("> ")
    while not choice.isdigit():
        fn.printy("i'm gonna need that as a number.")
        choice = input("> ")

    choice = int(choice)
    if choice <= 1:
        fn.printy(f"alright, that'll be {atk_upg_cost} chits please.")
        fn.printy("(Y/N)")
        confirmation = input("> ")
        while confirmation.upper() not in ["Y", "N", "YES", "NO"]:
            fn.printy("i'm sorry, what was that?")
            confirmation = input("> ")
        if confirmation.upper() in ["Y", "YES"]:
            if chits >= atk_upg_cost:
                fn.printy("thank you very much.")
                chits -= atk_upg_cost
                pl_atk_multi += 0.05

            else:
                fn.printy(f"i'm sorry, it looks like you're {atk_upg_cost - chits} chits short.")

        else:
            fn.printy("alright then.")

    elif choice == 2:
        fn.printy(f"alright, that'll be {def_upg_cost} chits please.")
        fn.printy("(Y/N)")
        confirmation = input("> ")
        while confirmation.upper() not in ["Y", "N", "YES", "NO"]:
            fn.printy("i'm sorry, what was that?")
            confirmation = input("> ")
        if confirmation.upper() in ["Y", "YES"]:
            if chits >= def_upg_cost:
                fn.printy("thank you very much.")
                chits -= def_upg_cost
                pl_def_multi += 0.05

            else:
                fn.printy(f"i'm sorry, it looks like you're {def_upg_cost - chits} chits short.")

        else:
            fn.printy("alright then.")

    elif choice == 3:
        fn.printy(f"alright, that'll be {spd_upg_cost} chits please.")
        fn.printy("(Y/N)")
        confirmation = input("> ")
        while confirmation.upper() not in ["Y", "N", "YES", "NO"]:
            fn.printy("i'm sorry, what was that?")
            confirmation = input("> ")
        if confirmation.upper() in ["Y", "YES"]:
            if chits >= spd_upg_cost:
                fn.printy("thank you very much.")
                chits -= spd_upg_cost
                pl_spd_multi += 0.05

            else:
                fn.printy(f"i'm sorry, it looks like you're {spd_upg_cost - chits} chits short.")

        else:
            fn.printy("alright then.")

    elif choice >= 4:
        fn.stats.update(save_key, atk_multi = pl_atk_multi, def_multi = pl_def_multi, spd_multi = pl_spd_multi, chits = chits)
        fn.printy("bye.")
        break