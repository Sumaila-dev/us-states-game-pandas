import turtle
import pandas
screen = turtle.Screen()
screen.title("US states Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states_data= data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct",prompt="What's another state's name? type 'exit' to quit game").title()
    if answer_state == "Exit":
        missing_states =[]
        for state in all_states_data:
            if state not in guessed_states:
                missing_states.append(state)
            missed_states_data = pandas.DataFrame(missing_states)
            missed_states_data.to_csv("missed_states.csv")
        turtle.bye()
        break

    if answer_state in all_states_data:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(state_data.state.item())

#screen.exitonclick()

