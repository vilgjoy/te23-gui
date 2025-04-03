import tkinter as tk
import random
import time

def start_game_1():
    print("Minigame 1 startar...")

def start_game_2():
    whack_a_mole()

def start_game_3():
    simon_says()

def show_main_menu():
    for widget in root.winfo_children():
        widget.destroy()
    
    tk.Label(root, text="Välj ett minigame:", font=("Arial", 14)).pack(pady=20)
    tk.Button(root, text="Minigame 1", command=start_game_1, width=20, height=2).pack(pady=5)
    tk.Button(root, text="Whack-a-mole!", command=start_game_2, width=20, height=2).pack(pady=5)
    tk.Button(root, text="simon says", command=start_game_3, width=20, height=2).pack(pady=5)
    tk.Button(root, text="avsluta", command=root.quit, width=20, height=2).pack(pady=20)

def whack_a_mole():
    global score, buttons, active_button
    
    for widget in root.winfo_children():
        widget.destroy()
    
    score = 0
    active_button = None
    
    label = tk.Label(root, text="Whack-a-Mole! Klicka på grönt!", font=("Arial", 14))
    label.pack(pady=10)
    
    score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 12))
    score_label.pack()
    
    grid_frame = tk.Frame(root)
    grid_frame.pack()
    
    buttons = []
    for i in range(3):
        row = []
        for j in range(3):
            btn = tk.Button(grid_frame, width=10, height=5)
            btn.config(command=lambda b=btn: check_hit(b, score_label))
            btn.grid(row=i, column=j, padx=5, pady=5)
            row.append(btn)
        buttons.append(row)
    
    back_button = tk.Button(root, text="Tillbaka", command=show_main_menu)
    back_button.pack(pady=10)
    
    update_mole()

def update_mole():
    global active_button
    
    if active_button:
        active_button.config(bg="SystemButtonFace")
    
    row, col = random.randint(0, 2), random.randint(0, 2)
    active_button = buttons[row][col]
    
    if random.random() < 0.75:
        active_button.config(bg="green")
    else:
        active_button.config(bg="red")
    
    root.after(1000, update_mole)

def check_hit(button, score_label):
    global score
    
    if button == active_button:
        if button.cget("bg") == "green":
            score += 1
            score_label.config(text=f"Score: {score}")
        else:
            game_over()

def game_over():
    for widget in root.winfo_children():
        widget.destroy()
    
    tk.Label(root, text="Game Over!", font=("Arial", 16), fg="red").pack(pady=20)
    tk.Button(root, text="Tillbaka", command=show_main_menu, width=20, height=2).pack(pady=20)

def simon_says():
    global sequence, player_sequence, color_buttons
    
    for widget in root.winfo_children():
        widget.destroy()
    
    sequence = []
    player_sequence = []
    
    tk.Label(root, text="simon Says, följ färg", font=("Arial", 14)).pack(pady=10)
    
    color_frame = tk.Frame(root)
    color_frame.pack()
    
    colors = ["red", "green", "blue", "yellow"]
    global color_buttons
    color_buttons = {}
    
    def create_button(color):
        def on_click():
            player_click(color)

        btn = tk.Button(color_frame, bg=color, width=10, height=3)
        btn.config(command=on_click)
        btn.grid(row=0, column=len(color_buttons), padx=5, pady=5)
        color_buttons[color] = btn

    for color in colors:
        create_button(color)
    # for color in colors:
    #     btn = tk.Button(color_frame, bg=color, width=10, height=3)
    #     btn.config(command=lambda c=color: player_click(c))
    #     btn.grid(row=0, column=len(color_buttons), padx=5, pady=5)
    #     color_buttons[color] = btn
    
    start_button = tk.Button(root, text="Start", command=start_sequence)
    start_button.pack(pady=10)
    
    back_button = tk.Button(root, text="Tillbaka", command=show_main_menu)
    back_button.pack(pady=10)

def start_sequence():
    global sequence, player_sequence
    player_sequence = []
    sequence.append(random.choice(["red", "green", "blue", "yellow"]))
    show_sequence()

def show_sequence():
    highlight_color(0)

def highlight_color(i):
    if i < len(sequence):
        color = sequence[i]
        color_buttons[color].config(bg="white")
        root.after(500, reset_color, color, i)

def reset_color(color, i):
    color_buttons[color].config(bg=color)
    root.after(500, highlight_color, i + 1)

def player_click(color):
    global player_sequence
    player_sequence.append(color)
    if player_sequence == sequence[:len(player_sequence)]:
        if len(player_sequence) == len(sequence):
            root.after(500, start_sequence)
    else:
        game_over()

root = tk.Tk()
root.title("Minigames Menu")
root.geometry("400x400")

show_main_menu()

root.mainloop()
