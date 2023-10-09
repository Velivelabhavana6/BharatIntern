import tkinter as tk
from tkinter import messagebox
import random

# Quiz questions and answers
questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['Paris', 'London', 'Berlin', 'Madrid'],
        'correct_answer': 'Paris',
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['Mars', 'Venus', 'Jupiter', 'Saturn'],
        'correct_answer': 'Mars',
    },
    {
        'question': 'What is the largest mammal on Earth?',
        'options': ['Elephant', 'Giraffe', 'Blue Whale', 'Hippopotamus'],
        'correct_answer': 'Blue Whale',
    },
    {
        'question': 'What is the largest planet in our solar system?',
        'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
        'correct_answer': 'Jupiter',
    },
    {
        'question': 'Which gas makes up the majority of Earth\'s atmosphere?',
        'options': ['Oxygen', 'Nitrogen', 'Carbon Dioxide', 'Hydrogen'],
        'correct_answer': 'Nitrogen',
    },
]

# Shuffle the questions for randomness
random.shuffle(questions)

# Quiz variables
current_question_index = 0
score = 0
total_questions = len(questions)
total_marks = total_questions  # Each question is worth 1 mark

# Function to start the quiz
def start_quiz():
    instructions_label.pack_forget()  # Hide the instructions
    start_button.pack_forget()  # Hide the start button
    show_question()  # Show the first question
    next_button.pack()  # Show the "Next" button

# Function to check the answer
def check_answer():
    global current_question_index, score
    selected_option = var.get()
    if selected_option == questions[current_question_index]['correct_answer']:
        score += 1
    current_question_index += 1

    if current_question_index < total_questions:
        show_question()
    else:
        messagebox.showinfo("Quiz Completed", f"You scored {score}/{total_marks}")
        window.quit()

# Function to display the current question
def show_question():
    question_label.config(text=questions[current_question_index]['question'])
    var.set(None)  # Clear the selection
    for i, option in enumerate(option_buttons):
        option.config(
            text=questions[current_question_index]['options'][i],
            value=questions[current_question_index]['options'][i],
            fg='black',  # Text color
            bg='#DDDDDD',  # Background color
        )

# Create the main window
window = tk.Tk()
window.title("Quiz App")

# Create a label for instructions
instructions_text = "Welcome to the Quiz!\n"
instructions_text += f"This is a small set of {total_questions} general questions.\n"
instructions_text += f"Each question is worth 1 mark.\n"
instructions_label = tk.Label(window, text=instructions_text, font=("Helvetica", 16), fg='blue')

# Create a "Start Quiz" button
start_button = tk.Button(window, text="Start Quiz", command=start_quiz, font=("Helvetica", 14), bg='green', fg='white')

# Create a label for the question
question_label = tk.Label(window, text="", font=("Helvetica", 16), fg='blue')

# Create radio buttons for options
var = tk.StringVar()

option_buttons = []
for i in range(4):
    option_button = tk.Radiobutton(window, text="", variable=var, font=("Helvetica", 12))
    option_buttons.append(option_button)

# Create a "Next" button (initially hidden)
next_button = tk.Button(window, text="Next", command=check_answer, font=("Helvetica", 14), bg='green', fg='white')
next_button.pack_forget()  # Hide the "Next" button initially

# Pack widgets
instructions_label.pack(pady=20)
start_button.pack(pady=10)
question_label.pack(pady=20)
for option_button in option_buttons:
    option_button.pack(pady=5)

# Start the GUI main loop
window.mainloop()
