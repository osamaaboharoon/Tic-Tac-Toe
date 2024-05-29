import random
import tkinter as tk

user_score = 0
computer_score = 0
current_player = "X"

def next_turn(game_btns, row, col, result_label, score_label):
    global current_player, user_score, computer_score
    if game_btns[row][col]["text"] == "" and not check_winner(game_btns) and not check_draw(game_btns):
        game_btns[row][col].config(text="X", bg="lightblue")
        if check_winner(game_btns):
            user_score += 1
            update_score(score_label)
            result_label.config(text="X Win!")
            return
        if check_draw(game_btns):
            result_label.config(text="Tie, No Winner")
            set_all_buttons_red(game_btns)
            return
        computer_turn(game_btns)
        if check_winner(game_btns):
            computer_score += 1
            update_score(score_label)
            result_label.config(text="Computer Wins!")
            return
        if check_draw(game_btns):
            result_label.config(text="Tie, No Winner")
            set_all_buttons_red(game_btns)
            return

def computer_turn(game_btns):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if game_btns[r][c]["text"] == ""]
    if empty_cells:
        row, col = random.choice(empty_cells)
        game_btns[row][col].config(text="O")

def check_winner(game_btns):
    for i in range(3):
        if game_btns[i][0]["text"] == game_btns[i][1]["text"] == game_btns[i][2]["text"] != "":
            return True
        if game_btns[0][i]["text"] == game_btns[1][i]["text"] == game_btns[2][i]["text"] != "":
            return True
    if game_btns[0][0]["text"] == game_btns[1][1]["text"] == game_btns[2][2]["text"] != "":
        return True
    if game_btns[0][2]["text"] == game_btns[1][1]["text"] == game_btns[2][0]["text"] != "":
        return True
    return False

def check_draw(game_btns):
    for row in range(3):
        for col in range(3):
            if game_btns[row][col]["text"] == "":
                return False
    return True

def set_all_buttons_red(game_btns):
    for row in range(3):
        for col in range(3):
            game_btns[row][col].config(bg="red")

def new_game(game_btns, result_label):
    global current_player
    current_player = "X"
    for row in range(3):
        for col in range(3):
            game_btns[row][col].config(text="", bg="lightgrey")
    result_label.config(text="")

def update_score(score_label):
    global user_score, computer_score
    score_label.config(text=f"You: {user_score}  Computer: {computer_score}")
