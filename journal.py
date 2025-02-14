from fn import *
import csv

with open("active_save.txt", "r") as active:
    save_key = active.read()

journal = open(f"journal_{save_key}.txt", "r")

printy("Enter the ID of the entry you wish to view.")
for id in journal.readlines():
    print(id, end = "")

# pretty sure it's this bit that doesn't work properly...
select = "oi stop looking at the code"
while select not in journal.readlines():
    printy("Select an ID from above.")
    select = input("> ")

for i in range(len(journal.readlines())):
    if journal.readlines()[i] == select:
        entities = csv.reader("enemies.csv")
        for entry in entities:
            if entry[0] == select:
                printy(entry[2])