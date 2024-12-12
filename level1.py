import time, random
import fn

#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⠁⠀⠀⠀⠀⠀⠂⠃⠉⠌⣰⣀⣀⣀⣀⠀⢨⡌⠌⠴⠰⣐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠰⠰⠰⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢪⠀⠀⠀⠀⠀⠀⣀⡸⠎⠃⠁⠀⠀⠀⠂⠃⠉⠍⠀⠀⠀⠀⠃⠍⢰⡀⠀⢀⡠⠸⠎⠃⠁⢀⡰⠀⠀⢯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢪⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡹⠎⠃⠀⠀⠀⡠⠎⠁⠀⠀⠀⢪⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠼⠲⠴⠰⠜⠇⠁⠀⠀⡰⠰⣰⡰⠰⠰⠸⠌⠀⠀⠀⠀⠀⠀⠀⢠⠞⠁⠀⠀⠀⠀⢠⠞⠀⠀⠀⠀⠀⠀⢪⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢪⠀⠀⠀⠀⠀⠀⠀⠀⠀⠭⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⡗⣀⡀⠀⠀⠀⠀⠀⣪⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠪⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠬⢰⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡐⠀⠀⠀⠀⠇⢡⠕⠀⠀⠀⠀⠀⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⢐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠃⠋⠍⢌⠔⠀⠀⠀⠀⠀⢀⡺⠀⠀⠀⠀⠀⢠⣗⡀⠀⠀⠀⠀⢪⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#   ⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⢀⡠⠟⠇⠀⠀⠀⣠⡸⠞⠏⣯⣽⣴⣐⠀⠀⡚⠀⠀⠀⠀⢀⣰⣧⣰⣼⢴⣰⡀⠀⠀⢂⠟⠁⠀⠀⢠⠕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#   ⠀⠀⠀⠀⠀⠀⠀    ⠀⢀⡸⠇⠀⠀⠀⠀⢠⡞⠁⠀⠀⣺⢿⣿⣿⣿⣵⣨⠁⢀⣀⡰⠜⣻⣿⣿⣿⣿⡕⠂⠯⣴⠀⠗⠀⠀⠀⢠⣷⢼⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠗⠀⠀⠀⠀⠀⢨⠗⠀⠀⠀⢪⠀⠀⣿⣿⣿⣿⡗⠃⠃⠀⠀⡒⠀⢪⣿⣿⣿⣽⠀⠀⠊⣕⠀⠀⠀⠀⠃⠀⢪⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⠅⠀⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⢪⣐⣠⣿⣿⣿⣿⡕⠀⠀⠀⢪⣵⣀⣺⣿⣿⣿⡗⠀⠀⠀⢯⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀               a boykisser helped
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢫⡀⠀⠀⠀⠀⠀⢪⡕⠀⠀⠀⠀⢪⣿⣿⣿⣿⣿⣿⡕⠀⠀⠀⠊⣿⣿⣿⣿⣿⣿⠅⠀⠀⠀⢪⠀⢨⡀⠀⣠⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀        test this code :3
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠭⡐⠀⠀⠀⠀⠪⡕⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⢯⣿⣿⣿⣿⠗⠀⠀⠀⠀⣿⠀⠀⠃⠃⠃⣣⠕⠀⠀⠀⠀⢀⡰⠜⠎⠃⠃⠀⠀⠀⠀⠀
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⢴⣨⡌⠴⠰⢿⡀⠀⠀⠀⠀⠂⠯⢿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠋⠏⠏⠁⠀⠀⠀⠀⣪⠕⠀⠀⠀⣠⠜⠁⠀⠀⠀⡠⠞⠁⠀⠀⠀⠀⠀⢀⡘⠁⠀⠀    they were also the one
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠭⣐⠀⠀⠋⠴⡀⡀⠀⠀⠀⠀⠀⠀⠀⠨⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣸⠗⠀⣰⠌⠇⠀⠀⠀⠀⢀⡞⠁⠀⠀⠀⠀⠀⠀⢠⠖⠀⠀⠀⠀        to put this ascii art
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠍⠴⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠰⡠⠔⠏⠁⠀⠀⠂⢔⠀⠀⠪⡤⣐⡾⠀⠀⠀⠀⠀⠀⠀⢀⡗⠀⠀⠀⠀⠀            in here -.-
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡕⠀⠀⠀⠀⢀⣀⠀⠀⠴⠰⠞⠉⠰⠰⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢪⠀⠀⠀⢵⠀⠁⠀⠀⠀⠀⠀⠀⠀⢪⠀⠀⠀⠀⠀⠀
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢵⣠⠘⢮⠃⠁⢄⠨⢜⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠃⠃⢋⡜⠤⢐⡪⠀⠀⠀⢪⠀⠀⠀⠀⠀⠀⠀⠀⠀⢪⠀⠀⠀⠀⠀⠀
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠁⠀⠀⡕⠀⠂⡔⠀⠃⠋⡔⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢪⠀⠀⢪⠀⠀⢠⢰⢪⠀⠀⠀⠀⠀⠀⠀⠀⠀⢪⠀⠀⠀⠀⠀⠀
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢫⡀⠀⠪⡐⠀⠀⣵⠜⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣺⠀⠀⣪⣠⠘⠁⠊⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢪⠀⠀⠀⠀⠀⠀
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣕⠀⠀⢭⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡗⠀⠀⡗⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢪⠀⠀⠀⠀⠀⠀
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠎⠃⠃⢪⡀⠀⠀⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢪⠕⠀⠀⠕⠃⠃⠃⠃⠬⡐⠀⠀⠀⠀⠀⠀⠀⠀⡗⠀⠀⠀⠀⠀⠀
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣪⠁⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⢭⠀⠀⠀⠀⠀⠀⠀⡪⠁⠀⠀⠀⠀⠀⠀
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⠰⠰⠰⡐⠀⠀⠀⠀⠀⠀⠀⠌⠌⢌⠤⠰⢀⡀⠀⠀⢨⠀⠀⠀⠀⠀⣀⡀⠀⠀⣪⠀⠀⠀⠀⠀⠀⡨⠅⠀⠀⠀⠀⠀⠀⠀
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠭⠰⣰⡰⠸⠏⠴⠰⠰⢜⠁⠀⠀⠀⠀⢪⠀⠀⠀⠀⠀⠀⠪⣐⠀⠀⢀⡺⠁⡫⠅⣠⠕⠀⠀⠀⠀⣠⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⡐⠀⠀⠀⠀⠀⡕⠀⠀⠀⠀⠀⠀⠀⠃⠃⠃⠀⠀⠭⠎⠁⠀⢀⣀⠸⠆⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠝⠀⠀⠀⠀⠀⢩⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠂⠁⠌⠌⠌⠃⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠗⠀⠀⠀⠀⠀⠀⢀⠂⡔⠀⠀⠀⠀⠀⠂⡕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣕⠀⠀⠀⢀⣀⠰⠌⠁⠀⠊⢰⡀⠀⠀⠀⠀⡕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠋⠎⠇⠃⠀⠀⠀⠀⠀⠀⠀⠃⠍⠌⠌⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

with open("active_save.txt", "r") as active:
    save_key = active.readline()
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

completed = False
chest1_opened = False
chest2_opened = False

fn.printy("\n")
fn.printy("LEVEL: I")
time.sleep(1)
fn.printy("THE BEGINNING")

pos_x = 0
pos_y = 0
pos_z = 0
inventory = []

fn.printy("You enter the very long and thin Forest just outside your House.")
while not completed:
    fn.printy("\nWhat will you do now?")
    fn.printy("<=1: Go North")
    fn.printy("==2: Go South")
    fn.printy("==3: Go East")
    fn.printy("==4: Go West")
    fn.printy("==5: Search current Location")
    fn.printy(">=6: Use Item")
    if pos_z == 6:
        fn.printy("Use North and South to Ascend or Descend the Tower.")
    choice = input("> ")
    while not choice.isdigit():
        fn.printy("Please input a number.")
        choice = input("> ")

    choice = int(choice)
    if choice <= 1:
        if pos_z != 4:
            if pos_z == 6:
                fn.printy("You climb up the Tower.")
                pos_y += 1
                if pos_y == 3:
                    fn.printy("Upon entering the highest floor of the Tower, you immediately see a large Entity asleep on top of a massive pile of Chits.")
                    fn.printy("You attempt to write a Journal entry for this entity, but its incredibly sensitive ears pick up the sound of your pen, and it wakes up!")
                    fn.battle(save_key, "ID-A03/i", True)
                    completed = True
                    fn.printy("COMPLETION MESSAGE UNNAMED")
            else:
                pos_z += 1
                if pos_z != 6:
                    fn.printy("You move forwards through the Forest.")

                if pos_z == 3:
                    fn.printy("A Creature jumps out at you!")
                    fn.battle(save_key, "ID-A01/i")

                elif pos_z == 6:
                    fn.printy("You enter the Tower.")
                    
                elif pos_z == 4:
                    fn.printy("You come across a river. It looks too wide to jump across, and you're carrying some things that you REALLY don't want to get wet.")

                elif pos_z == 5:
                    fn.printy("You enter the Tower.")
        
        else:
            fn.printy("You cannot go North any further")

    elif choice == 2:
        if pos_z > 0 and pos_y == 0:
            fn.printy("You move backwards towards where you came from.")
            pos_z -= 1
        
        else:
            print("You cannot go South any further")

    elif choice == 3:
        if pos_z == 6:
            fn.printy("The walls of the Tower are blocking the way Eastward.")

        else:
            fn.printy("You cannot go East, for this would result in leaving the Forest.")

    elif choice == 4:
        if pos_z == 6:
            fn.printy("The walls of the Tower are blocking the way Westward.")

        else:
            fn.printy("You cannot go West, for this would result in leaving the Forest.")

    elif choice == 5:
        fn.printy("You look around, and find...")
        if pos_z == 2:
            fn.printy("A Boat, lying on the floor for seemingly no good reason.")
            fn.printy("You pick up the Boat and put it in your Inventory.")
            inventory.append("Boat")

        elif pos_z == 6 and pos_y == 1:
            if not chest1_opened:
                fn.printy("A Chest! Open it? (Y/N)")
                open_chest = input("> ")
                while open_chest.upper() not in ["Y", "N", "YES", "NO"]:
                    fn.printy("Please enter either Y or N.")
                    open_chest = input("> ")

                if open_chest.upper() in ["Y", "YES"]:
                    chest1_opened = True
                    fn.printy("You decide to open the Chest, and gain 50 Chits!")
                    chits += 50
                    fn.stats.update(save_key, chits = chits)
                    
                else:
                    fn.printy("You decide to leave the Chest alone.")
            
            else:
                fn.printy("A Chest! You have already opened it.")
                
        elif pos_z == 6 and pos_y == 2:
            if not chest2_opened:
                fn.printy("A Chest! Open it? (Y/N)")
                open_chest = input("> ")
                while open_chest.upper() not in ["Y", "N", "YES", "NO"]:
                    fn.printy("Please enter either Y or N.")
                    open_chest = input("> ")

                if open_chest.upper() in ["Y", "YES"]:
                    chest2_opened = True
                    fn.printy("You decide to open the Chest, and a monster jumps out!")
                    fn.battle(save_key, "ID-A02/i")
                
                else:
                    fn.printy("You decide to leave the Chest alone.")
            
            else:
                fn.printy("A Chest! You have already opened it.")

        else:
            fn.printy("Nothing.")

    elif choice >= 6:
        if inventory != []:
            fn.printy("Select an item to use:")
            for item in range(len(inventory)):
                fn.printy(f"{item + 1}: {inventory[item]}")
                while True:
                    try:
                        used_item = input("> ")
                        used_item = int(used_item) - 1
                        if inventory[used_item] == "Boat":
                            if pos_z == 4:
                                fn.printy("You deploy the Boat onto the river.")
                                fn.printy("You enter the Boat.")
                                fn.printy("The Boat takes you directly across the river!")
                                pos_z += 1
                                fn.printy("You see a large, rather imposing Tower in front of you.")

                            else:
                                fn.printy("You deploy the Boat onto the ground.")
                                fn.printy("Nothing happens.")
                                fn.printy("You pick the Boat up again, having thoroughly wasted a good few seconds.")
                        break

                    except:
                        fn.printy("Invalid input.")

if levels_cleared < 1:
    levels_cleared += 1

fn.stats.update(save_key, levels_cleared = levels_cleared)