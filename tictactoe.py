from tkinter import *
import random


def next_turn(row, column):
    global player
    if buttons[row][column]["text"] == "" and winner_check() is False:
        if player == players[0]:
            buttons[row][column]["text"] = player
            if winner_check() is False:
                player = players[1]
                label.config(text = (players[1] + " Turn"))
            elif winner_check() is True:
                label.config(text = (player[0] + " Wins!"))
            elif winner_check() == "Tie":
                label.config(text=("Tie!"))
        else:
            buttons[row][column]["text"] = player
            if winner_check() is False:
                player = players[0]
                label.config(text = (players[0] + " Turn"))
            elif winner_check() is True:
                label.config(text = (player[0] + " Wins!"))
            elif winner_check() == "Tie":
                label.config(text= ("Tie!"))

def winner_check():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    elif check_empty() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="orange")
        return "Tie"
    else:
        return False

def check_empty():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True

def restart_game():
    global player
    player = random.choice(players)
    label.config(text = player + " Turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text = "", bg = "#F0F0F0")


# Window
window = Tk()
window.title("Tic-Tac-Toe")
players = ["X", "O"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]
label = Label(text = player + " turn", font = ("Times New Roman", 40))
label.pack(side = "top")

# Reset
reset_button = Button(text = "Restart", font = ("Times New Roman", 20), command = restart_game)
reset_button.pack(side = "top")

frame = Frame(window)
frame.pack()

# Rows
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text = "", font = ("Times New Roman", 40), width = 5, height = 2,
                                      command = lambda row = row, column = column: next_turn(row, column))
        buttons[row][column].grid(row = row, column = column)


# Main
window.mainloop()

