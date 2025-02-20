import pandas as pd

# Load the Excel sheet containing questions and answers
def load_qa(file_path):
    try:
        df = pd.read_excel(file_path)  # Read the Excel file
        print("Loaded DataFrame:")  # Debugging: Print the DataFrame
        print(df.head())  # Debugging: Print the first few rows
        print("Columns:", df.columns.tolist())  # Debugging: Print column names
        return df
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return None

# Function to determine the answer type and format response
def format_answer(answer):
    try:
        if isinstance(answer, (int, float)):  # If it's a number
            return f"Bot: {answer:.2f}" if isinstance(answer, float) else f"Bot: {answer}"
        elif isinstance(answer, str):  # If it's a string
            return f"Bot: {answer}"
        else:
            return "Bot: I don't know the answer to that."
    except Exception as e:
        print(f"Error formatting answer: {e}")
        return "Bot: Unable to process the answer."

# Function to find the answer based on user input
def find_answer(user_input, qa_df):
    if qa_df is not None:
        qa_df.columns = qa_df.columns.str.strip().str.lower()  # Standardize column names

        if "question" in qa_df.columns and "answer" in qa_df.columns:
            user_input = user_input.lower().strip()  # Standardize user input
            qa_df["question"] = qa_df["question"].str.lower().str.strip()  # Standardize "question" column

            matches = qa_df[qa_df["question"].str.contains(user_input, case=False, na=False)]
            if not matches.empty:
                answer = matches.iloc[0]["answer"]  # Fetch the first match
                return format_answer(answer)  # Format the answer correctly
        else:
            print("Error: 'question' or 'answer' column not found in DataFrame.")
    return "Bot: I don't know the answer to that."
