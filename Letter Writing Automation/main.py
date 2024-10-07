WORD = "[name]"

with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letters = letter_file.read()
    for name in names:
        name=name.strip()
        new_letter = letters.replace(WORD,name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt",mode='w') as completed_letter:
            completed_letter.write(new_letter)
