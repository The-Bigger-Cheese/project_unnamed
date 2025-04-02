import sys, time, random, pandas as pd, csv, json

def printy(txt, delay = 0.02, delay1 = 0.25, delay2 = 0.5, end = "\n"):
    for char in txt:
        sys.stdout.write(char)
        if char in ",:":
            time.sleep(delay1)

        elif char in "!.?":
            time.sleep(delay2)

        else:
            time.sleep(delay)

    sys.stdout.write(end)
    sys.stdout.flush()

class enemy:

    def __init__(self, id, lvl):
        with json.load("data\\entities.json", "r") as en_all:
            for dict in en_all:
                if dict["id"] == id:
                    en_one = dict
                    break

        self.id = id
        self.name = en_one["name"]
        self.type = en_one["type"]
        self.elements = en_one["elements"]
        self.desc = en_one["desc"]
        self.lvl = lvl
        self.hp = en_one["hp"]
        self.max_hp = en_one["hp"]
        self

class stats:

    def update(save_key, lvl = "", hp = "", max_hp = "", mp = "", max_mp = "", atk_base = "", def_base = "", spd_base = "", xp = "", levels_cleared = "", chits = "", atk_multi = "", def_multi = "", spd_multi = ""):
        pl_stats = stats.get(save_key)
        if lvl != "":
            pl_stats[1] = f"{lvl}\n"

        if hp != "":
            pl_stats[2] = f"{hp}\n"

        if max_hp != "":
            pl_stats[3] = f"{max_hp}\n"

        if mp != "":
            pl_stats[4] = f"{mp}\n"

        if max_mp != "":
            pl_stats[5] = f"{max_mp}\n"

        if atk_base != "":
            pl_stats[6] = f"{atk_base}\n"

        if def_base != "":
            pl_stats[7] = f"{def_base}\n"

        if spd_base != "":
            pl_stats[8] = f"{spd_base}\n"

        if xp != "":
            pl_stats[9] = f"{xp}\n"

        if levels_cleared != "":
            pl_stats[10] = f"{levels_cleared}\n"
        
        if chits != "":
            pl_stats[11] = f"{chits}\n"

        if atk_multi != "":
            pl_stats[12] = f"{atk_multi}\n"

        if def_multi != "":
            pl_stats[13] = f"{def_multi}\n"

        if spd_multi != "":
            pl_stats[14] = f"{spd_multi}\n"

        with open(f"data_{save_key}.txt", "w") as data:
            data.write(pl_stats[0])

        with open(f"data_{save_key}.txt", "a") as data:
                data.writelines(pl_stats[1:])

    def get(save_key):
        alldata = pd.DataFrame(pd.read_json("saves.json"))
        for save in alldata:
            if save["key"] == save_key:
                return save

def battle(save_key, en_id, isBoss = False):

    save_data = stats.get(save_key)
    pl_lvl = int(save_data[1])
    pl_hp = int(save_data[2])
    pl_max_hp = int(save_data[3])
    mp = int(save_data[4])
    max_mp = int(save_data[5])
    pl_atk_base = int(save_data[6])
    pl_def_base = int(save_data[7])
    pl_spd_base = int(save_data[8])
    xp = int(save_data[9])
    xp_req = int(round(((1.5 ** pl_lvl) + 10), 0))
    levels_cleared = int(save_data[10])
    chits = int(save_data[11])
    pl_atk_multi = float(save_data[12])
    pl_def_multi = float(save_data[12])
    pl_spd_multi = float(save_data[13])
    pl_atk = int(round((pl_atk_base * pl_atk_multi), 0))
    pl_def = int(round((pl_def_base * pl_def_multi), 0))
    pl_spd_full = int(round((pl_spd_base * pl_spd_multi), 0))
    pl_spd = pl_spd_full

    with open("enemies.csv", "r") as enemies:
        enemies = csv.reader(enemies)
        for enemy in enemies:
            if enemy[0] == en_id:
                en_stats = enemy
                break
        
    try:
        with open(f"journal_{save_key}.txt", "r") as journal:
            if en_id in journal.readlines():
                en_name = en_stats[1]

            else:
                en_name = "[ENTITY UNNAMED]"

    except FileNotFoundError:
        en_name = "[ENTITY UNNAMED]"

    en_desc = en_stats[2]
    en_lvl = int(en_stats[3])
    en_hp = int(en_stats[4])
    en_max_hp = en_hp
    en_atk = int(en_stats[5])
    en_def = int(en_stats[6])
    en_spd_full = int(en_stats[7])
    en_spd = en_spd_full

    print("\n\n+-----INITIATING BATTLE-----+")
    printy("ENEMY:")
    printy(f"{en_id}: {en_name} - {en_hp} HP")    
    while pl_hp > 0 and en_hp > 0:
        if pl_spd > en_spd:
            printy("\nYOUR TURN")
            print(f"HP: {pl_hp}")
            print(f"MP: {mp}")
            print(f"Enemy HP: {en_hp}")
            printy("What will you do?")
            print("<=1: Attack")
            print("==2: Examine")
            print("==3: Capture")
            print(">=4: Heal Self")
            move = input("> ")
            while not move.isdigit():
                printy("ERROR: Input must be an integer.")
                move = input("> ")

            move = int(move)
            
            if move <= 1:
                dmg = (pl_atk) / ((en_def / 100) + 1)
                dmg = round(dmg, 0)
                dmg = int(dmg)
                accuracy = random.randint(1, 100)
                if accuracy < en_spd - pl_spd:
                    printy("The enemy is just too fast for you, and your attack misses.")

                else:
                    printy(f"A hit! You strike the enemy, dealing {dmg} damage.")
                    en_hp -= dmg

            elif move == 2:
                printy(f"{en_id}: {en_desc}")
                en_name = en_stats[1]
                with open(f"journal_{save_key}.txt", "r") as journal:
                    if en_id not in journal.readlines():
                        with open(f"journal_{save_key}.txt", "a") as journal:
                            journal.write(f"\n{en_id}")
                            printy(f"You decide to document the entity in your Journal under the name of {en_name}.")
                    else:
                        printy("You have already written a Journal entry on this Entity.")
            
            elif move == 3:
                capchance = random.randint(1, en_hp)
                if capchance <= pl_lvl:
                    printy("Success! The entity is captured and automatically molecularly transmitted to the Lab.")
                    with open(f"lab_{save_key}.txt", "a") as lab:
                        lab.write(f"\n{en_id}")
                    en_hp = 0
                    
                else:
                    printy("Failure. The entity evaded capture.")

            elif move == 4:
                printy("How much MP will you attempt to convert to HP?")
                hl = input("> ")
                while not hl.isdigit():
                    printy("Please input a number.")
                    hl = input("> ")

                hl = int(hl)

                if mp >= hl:
                    pl_hp += hl
                    if pl_hp > pl_max_hp:
                        pl_hp = pl_max_hp
                    printy(f"You convert {hl} MP to {hl} HP.")
                    mp -= hl

                else:
                    printy(f"You attempt to convert {hl} MP to {hl} HP, but fail due to insufficient MP.")
        
            pl_spd -= en_spd_full

        else:
            printy("\nENEMY'S TURN")
            if en_hp >= en_max_hp / 4 and isBoss:
                en_action = random.randint(1,3)
                if en_action == 1:
                    en_heal = random.randint(int(round((en_max_hp / 6), 0)), int(round(en_max_hp / 2), 0))
                    en_hp += en_heal
                    if en_hp > en_max_hp:
                        en_hp = en_max_hp
                    
                    printy(f"{en_name} heals {en_heal} of its HP.")
                
            printy(f"{en_name} attacks!")
            dmg = (en_atk) / ((pl_def / 100) + 1)
            dmg = round(dmg, 0)
            dmg = int(dmg)
            if isBoss:
                dmg = random.randint(dmg, dmg * 2)
            accuracy = random.randint(1, 100)
            if accuracy < pl_spd - en_spd:
                printy("You manage to outspeed the enemy, avoiding its attack.")

            else:
                pl_hp -= dmg
                printy(f"The enemy lands a hit on you, dealing {dmg} damage.")
                if pl_hp <= 0:
                    printy(f"The entity has killed you. You are dead.")
                    exit()

            en_spd -= pl_spd_full
    
    else:
        printy("You win!")
        if move == 1:
            printy(f"You gain {en_max_hp} XP and {en_max_hp} Chits.")
            xp += en_max_hp
            chits += en_max_hp

    if xp >= xp_req:
        xp = 0
        pl_lvl += 1
        printy(f"Level Up! You are now Level {pl_lvl}.")
        pl_max_hp = pl_lvl * 10
        pl_hp = pl_max_hp
        max_mp = pl_max_hp
        mp = max_mp
        pl_atk_base = pl_max_hp / 2
        pl_atk_base = round(pl_atk_base, 0)
        pl_atk_base = int(pl_atk_base)
        pl_def_base = pl_max_hp / 2
        pl_def_base = round(pl_def_base, 0)
        pl_def_base = int(pl_def_base)
        pl_spd_base = pl_max_hp / 2
        pl_spd_base = round(pl_spd_base, 0)
        pl_spd_base = int(pl_spd_base)
    
    stats.update(save_key, xp = xp, lvl = pl_lvl, hp = pl_hp, max_hp = pl_max_hp, mp = mp, max_mp = max_mp, atk_base = pl_atk_base, def_base = pl_def_base, spd_base = pl_spd_base)