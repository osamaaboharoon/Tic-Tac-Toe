import tkinter as tk
from gui import create_gui, create_widgets

def main():
    
    window = tk.Tk()

    
    game_btns = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

   
    score_label, result_label = create_widgets(window, game_btns)
    game_btns = create_gui(window, game_btns, result_label, score_label)

   
    window.mainloop()

if __name__ == "__main__":
    main()
