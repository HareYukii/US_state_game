import turtle
import pandas
from write_state import WriteState

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_answer = []
game_is_on = True

data = pandas.read_csv("50_states.csv")
missing_states = pandas.read_csv("missing_states.csv")
with open("try_num.txt", mode="r") as try_num:
    the_number_of_trying = int(try_num.read())
# Use a loop to allow the user to keep guessing
while game_is_on:
    if the_number_of_trying == 0:
        score = f"{len(correct_answer)}/50"
    else:
        score = f"{len(correct_answer)}/{len(missing_states)}"
    answer_state = screen.textinput(title=f"({score}) Guess the states",
                                    prompt="What's another state's name?")
    # Convert the guess to Title case
    answer_state = answer_state.title()

    # Exit when answer is "exit"
    if answer_state == "Exit":
        # Save the missing states to a .csv

        for state in correct_answer:
            answer_state_index = data.index[data["state"] == state].tolist()[0]
            missing_states = missing_states.drop(answer_state_index)
            missing_states.to_csv("missing_states.csv")
        break

    # Record the number of trying
    else:
        the_number_of_trying += 1
        with open("try_num.txt", mode="w") as try_num:
            try_num.write(f"{the_number_of_trying}")

    # Check if the guess is among the 50 states
    answer_is_correct = False
    for state in data["state"]:
        if answer_state == state:
            answer_is_correct = True

    # Write correct guesses onto the map
    if answer_is_correct:
        correct_answer.append(answer_state)
        state_dataframe = data[data.state == answer_state]
        x_position = state_dataframe.iloc[0, 1]
        y_position = state_dataframe.iloc[0, 2]
        write_state = WriteState()
        write_state.write_state_name(answer_state, x_position, y_position)

    if len(correct_answer) == 50:
        game_is_on = False



screen.mainloop()