import tkinter as tk
from tkinter import scrolledtext
from qa_logic import load_qa, find_answer  # Import functions from qa_logic.py

# Load the Q&A Excel file
qa_df = load_qa("questions_answers.xlsx")  # Replace with your Excel file path

# Function to handle sending messages
def send_message():
    user_input = entry.get().strip()  # Get user input
    if user_input:
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "You: " + user_input + "\n")
        entry.delete(0, tk.END)  # Clear input field

        bot_response = find_answer(user_input, qa_df)
        chat_window.insert(tk.END, bot_response + "\n")

        chat_window.yview(tk.END)
        chat_window.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Chatbot with Excel Q&A")
root.geometry("400x500")

# Create a scrolled text widget for the chat display
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, state=tk.DISABLED)
chat_window.grid(column=0, row=0, padx=10, pady=10, columnspan=2)

# Create an entry widget for user input
entry = tk.Entry(root, width=40)
entry.grid(column=0, row=1, padx=10, pady=10)
entry.bind("<Return>", lambda event: send_message())

# Create a send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(column=1, row=1, padx=10, pady=10)

# Run the GUI event loop
root.mainloop()
