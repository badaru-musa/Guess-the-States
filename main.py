import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def  get_mouse_click_cor(x, y):
#     print(x,y)
#
#
# turtle.onscreenclick(get_mouse_click_cor)
answer = turtle.textinput(title="Guess the State", prompt="What's another state name?")

data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
all_turtle = []
states = set()

game_on = True

while len(states) < 50:
    answer = turtle.textinput(title=f"Guess the State? You have {len(states)}/50 states ",
                              prompt="What's another state name?")
    n_answer = answer.title()
    if n_answer == "Exit":
        missed_states = [state for state in state_list if state not in states]
        learn = {"states": missed_states}
        learn_data = pandas.DataFrame(learn)
        learn_data.to_csv("States  i Forgot.csv")
        break
    
    if n_answer in state_list and len(all_turtle) < 50:
        states.add(n_answer)
        row = data[data.state == n_answer]
        x_cor = int(row.x)
        y_cor = int(row.y)
        t = turtle.Turtle()
        t.pu()
        t.hideturtle()
        t.goto(x=x_cor, y=y_cor)
        t.write(arg=f"{answer.capitalize()}", font=("Arial", 7, "normal"))
        all_turtle.append(t)
turtle.mainloop()
