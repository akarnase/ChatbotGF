import tkinter as tk
from tkinter import scrolledtext

# Function to handle sending messages
def send_message():
    user_input = entry.get().strip()  # Get user input
    if user_input:  # If input is not empty
        # Display user message in the chat window
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "You: " + user_input + "\n")
        entry.delete(0, tk.END)  # Clear the input field

        # Simulate a bot response (replace with actual chatbot logic)
        bot_response = "Bot: " + "I received: " + user_input + "\n"
        chat_window.insert(tk.END, bot_response)

        # Auto-scroll to the latest message
        chat_window.yview(tk.END)
        chat_window.config(state=tk.DISABLED)  # Disable editing of chat history

# Create the main window
root = tk.Tk()
root.title("Simple Chatbot GUI")
root.geometry("400x500")  # Set window size

# Create a scrolled text widget for the chat display
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, state=tk.DISABLED)
chat_window.grid(column=0, row=0, padx=10, pady=10, columnspan=2)

# Create an entry widget for user input
entry = tk.Entry(root, width=40)
entry.grid(column=0, row=1, padx=10, pady=10)
entry.bind("<Return>", lambda event: send_message())  # Send message on pressing Enter

# Create a send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(column=1, row=1, padx=10, pady=10)

# Run the GUI event loop
root.mainloop()
----------------
import tkinter as tk
from tkinter import scrolledtext
import pandas as pd

# Load the Excel sheet containing questions and answers
def load_qa(file_path):
    try:
        df = pd.read_excel(file_path)  # Read the Excel file
        return df
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return None

# Function to find the answer based on user input
def find_answer(user_input, qa_df):
    if qa_df is not None:
        # Search for the keyword in the "Question" column
        matches = qa_df[qa_df["Question"].str.contains(user_input, case=False, na=False)]
        if not matches.empty:
            return matches.iloc[0]["Answer"]  # Return the first matching answer
    return "Bot: I don't know the answer to that."

# Function to handle sending messages
def send_message():
    user_input = entry.get().strip()  # Get user input
    if user_input:  # If input is not empty
        # Display user message in the chat window
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "You: " + user_input + "\n")
        entry.delete(0, tk.END)  # Clear the input field

        # Find and display the bot's response
        bot_response = find_answer(user_input, qa_df)
        chat_window.insert(tk.END, bot_response + "\n")

        # Auto-scroll to the latest message
        chat_window.yview(tk.END)
        chat_window.config(state=tk.DISABLED)  # Disable editing of chat history

# Load the Q&A Excel file
qa_df = load_qa("questions_answers.xlsx")  # Replace with your Excel file path

# Create the main window
root = tk.Tk()
root.title("Chatbot with Excel Q&A")
root.geometry("400x500")  # Set window size

# Create a scrolled text widget for the chat display
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, state=tk.DISABLED)
chat_window.grid(column=0, row=0, padx=10, pady=10, columnspan=2)

# Create an entry widget for user input
entry = tk.Entry(root, width=40)
entry.grid(column=0, row=1, padx=10, pady=10)
entry.bind("<Return>", lambda event: send_message())  # Send message on pressing Enter

# Create a send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(column=1, row=1, padx=10, pady=10)

# Run the GUI event loop
root.mainloop()
