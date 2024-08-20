from tkinter import *
import tkinter.font as font
import random
from tkinter import messagebox

player_score = 0
computer_score = 0
rounds = 0
total_rounds = 5  # Default total number of rounds

options = [('rock', 0), ('paper', 1), ('scissors', 2)]

def determine_winner(player, computer):
    global player_score, computer_score, rounds
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        player_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "Computer wins!"

def player_choice(player_option):
    global rounds
    if rounds < total_rounds:
        player_choice_label.config(text=f"Your Selected : {player_option[0].capitalize()}")
        computer_option = random.choice(options)
        computer_choice_label.config(text=f"Computer Selected : {computer_option[0].capitalize()}")
        result = determine_winner(player_option[0], computer_option[0])
        winner_label.config(text=result)
        player_score_label.config(text=f"Your Score : {player_score}")
        computer_score_label.config(text=f"Computer Score : {computer_score}")
        rounds += 1
        rounds_label.config(text=f"Round: {rounds}/{total_rounds}")
        if rounds == total_rounds:
            show_final_winner()
    else:
        messagebox.showinfo("Game Over", "Game Over! Reset the game to play again.")

def show_final_winner():
    if player_score > computer_score:
        final_winner = "Congratulations! You won the game!"
    elif player_score < computer_score:
        final_winner = "Sorry, the computer won the game."
    else:
        final_winner = "It's a tie!"
    messagebox.showinfo("Final Result", final_winner)

def reset_game():
    global player_score, computer_score, rounds
    player_score = 0
    computer_score = 0
    rounds = 0
    player_choice_label.config(text="Your Selected : ---")
    computer_choice_label.config(text="Computer Selected : ---")
    player_score_label.config(text="Your Score : -")
    computer_score_label.config(text="Computer Score : -")
    winner_label.config(text="Let's Start the Game...")
    rounds_label.config(text=f"Round: {rounds}/{total_rounds}")

def set_rounds():
    global total_rounds
    try:
        total_rounds = int(rounds_entry.get())
        reset_game()
        rounds_label.config(text=f"Round: 0/{total_rounds}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number of rounds.")

game_window = Tk()
game_window.title("Rock Paper Scissors Game")

game_window.configure(bg='#2e2e2e')  # Dark grey background

app_font = font.Font(size=12)

game_title = Label(text='Rock Paper Scissors', font=font.Font(size=20), fg='white', bg='#2e2e2e')
game_title.pack()

winner_label = Label(text="Let's Start the Game...", fg='lime', font=font.Font(size=13), pady=8, bg='#2e2e2e')
winner_label.pack()

input_frame = Frame(game_window, bg='#2e2e2e')
input_frame.pack()

player_options = Label(input_frame, text="Your Options : ", font=app_font, fg='white', bg='#2e2e2e')
player_options.grid(row=0, column=0, pady=8)

rock_btn = Button(input_frame, text='Rock', width=15, bd=0, bg='#ff5c5c', fg='white', pady=5, command=lambda: player_choice(options[0]))
rock_btn.grid(row=1, column=1, padx=8, pady=5)

paper_btn = Button(input_frame, text='Paper', width=15, bd=0, bg='#c0c0c0', fg='black', pady=5, command=lambda: player_choice(options[1]))
paper_btn.grid(row=1, column=2, padx=8, pady=5)

scissors_btn = Button(input_frame, text='Scissors', width=15, bd=0, bg='#5c85d6', fg='white', pady=5, command=lambda: player_choice(options[2]))
scissors_btn.grid(row=1, column=3, padx=8, pady=5)

score_label = Label(input_frame, text='Score : ', font=app_font, fg='white', bg='#2e2e2e')
score_label.grid(row=2, column=0)

player_choice_label = Label(input_frame, text='Your Selected : ---', font=app_font, fg='white', bg='#2e2e2e')
player_choice_label.grid(row=3, column=1, pady=5)

player_score_label = Label(input_frame, text='Your Score : -', font=app_font, fg='white', bg='#2e2e2e')
player_score_label.grid(row=3, column=2, pady=5)

computer_choice_label = Label(input_frame, text='Computer Selected : ---', font=app_font, fg='white', bg='#2e2e2e')
computer_choice_label.grid(row=4, column=1, pady=5)

computer_score_label = Label(input_frame, text='Computer Score : -', font=app_font, fg='white', bg='#2e2e2e')
computer_score_label.grid(row=4, column=2, padx=(10, 0), pady=5)

rounds_label = Label(input_frame, text=f"Round: 0/{total_rounds}", font=app_font, fg='cyan', bg='#2e2e2e')
rounds_label.grid(row=5, column=1, pady=8)

reset_button = Button(input_frame, text='Reset Game', width=15, bd=0, bg='#ffa500', fg='white', pady=5, command=reset_game)
reset_button.grid(row=5, column=2, padx=8, pady=8)

rounds_frame = Frame(game_window, bg='#2e2e2e')
rounds_frame.pack(pady=10)

rounds_label_entry = Label(rounds_frame, text="Set Number of Rounds:", font=app_font, fg='white', bg='#2e2e2e')
rounds_label_entry.grid(row=0, column=0, padx=5)

rounds_entry = Entry(rounds_frame, font=app_font, width=5, bg='#c0c0c0', fg='black')
rounds_entry.grid(row=0, column=1, padx=5)

set_rounds_button = Button(rounds_frame, text="Set", width=10, bd=0, bg='#32cd32', fg='white', command=set_rounds)
set_rounds_button.grid(row=0, column=2, padx=5)

game_window.geometry('700x400')
game_window.mainloop()
