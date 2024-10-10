import turtle
import pandas as pd
FONT = ("Arial",20,"normal")

screen = turtle.Screen()
screen.title("District Game")
bd_map = "Bangladesh_Map.gif"
screen.addshape(bd_map)
turtle.shape(bd_map)




df = pd.read_csv("Bangladesh_District.csv")
all_district = df["District"].to_list()

already_guessed = []
missed_district = []
while len(already_guessed) < 64:
    answer = screen.textinput(f"{len(already_guessed)}/64 Correct", "Guess a District Name")
    if answer is None:  # Check if the user closed the dialog
        break  # Exit the loop if no input was given
    answer = answer.title()

    if answer == "Exit":
        for name in all_district:
            if name not in already_guessed:
                missed_district.append(name)
        m_df = pd.DataFrame(missed_district, columns=["Missed Districts"])
        m_df.to_csv("Missed_District.csv", index=False)
        print("The districts you missed are saved in Missed_District.csv. Check it and play again!")
        break  # Exit the loop after saving

    elif answer in all_district and answer not in already_guessed:
        already_guessed.append(answer)
        t = turtle.Turtle()
        t.penup()
        t.ht()
        district_data = df[df.District == answer]
        t.goto(int(district_data.x_cor.iloc[0]), int(district_data.y_cor.iloc[0]))
        t.write(f"{answer}")


