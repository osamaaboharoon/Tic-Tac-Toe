import tkinter as tk
from logic import next_turn, new_game

def create_gui(window, game_btns, result_label, score_label):
    window.title("Tic-Tac-Toe Almdrasa")

    frame_buttons = tk.Frame(window)
    frame_buttons.pack()

    
    for row in range(3):
        for col in range(3):
            button = tk.Button(frame_buttons, text="", width=3, height=3, 
                               command=lambda row=row, col=col: next_turn(game_btns, row, col, result_label, score_label))
            button.grid(row=row, column=col)
            game_btns[row][col] = button

    return game_btns

def create_widgets(window, game_btns):
    
    score_label = tk.Label(window, text="Player 1 (X): 0  Player 2 (O): 0")
    score_label.pack()

    
    result_label = tk.Label(window, text="", font=("Helvetica", 16))
    result_label.pack()

    
    new_game_button = tk.Button(window, text="Restart", command=lambda: new_game(game_btns, result_label))
    new_game_button.pack()

    return score_label, result_label
