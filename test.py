def azalea(x, name):
    if name.upper() in ["RAVEN", "RAHHHVEN"]:
        if x.upper() in ["FREAK", "SLAG", "CUNT", "KYS", "KILL YOURSELF", "DIE"]:
            return "UNCIVIL BEHAVIOUR."
    if x.upper() in ["HE", "HIM", "HIS", "HIMSELF", "HE'S", "HE'D", "ISAAC", "ISSAC", "ISACC", "MALE", "BOY", "MAN"]:
        return "[EXTREMELY LOUD INCORRECT BUZZER]"
    elif x.upper() in ["SHE", "HER", "HERS", "HERSELF", "SHE'S", "SHE'D", "AZALEA", "AZZY", "FEMALE", "GIRL", "WOMAN"]:
        return "yippee"
    elif x.upper() in ["THEY", "THEM", "THEIR", "THEIRS", "THEMSELVES", "THEY'RE", "THEY'D", "THEY'VE"]:
        return "eh, ok i guess. i GUESS."
    elif x.upper() in ["TRANS", "TRANSGENDER", "CISN'T"]:
        return "i mean... yeah."
    else:
        return ""

name = input("who are you?\n> ")

sentence = input("type a sentence about me.\n> ")
word = ""
for char in sentence:
    if char == " ":
        print(azalea(word, name))
    else:
        word = f"{word}{char}"
print(azalea(word, name))