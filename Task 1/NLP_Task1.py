import tkinter as tk
import nltk

"""
Example:
NLTK is a leading platform for building Python programs to work with human language data. NLTK is available for Windows, Mac OS X, and Linux. Best of all, NLTK is a free, open source, community-driven project.
"""
def perform_operation():
    """Performs the selected tokenization and displays the result."""
    text = text_entry.get("1.0", tk.END).strip()
    choice = choice_var.get()

    if choice == "print tokenized words":
        result = nltk.word_tokenize(text)
        print("Choice number 1: ", result)  # Print tokenized words
    elif choice == "print tokenized sentences":
        result = nltk.sent_tokenize(text)
        print("Choice number 2: ", result)  # Print tokenized sentences
    elif choice == "print output using split function.":
        result = text.split()
        print("Choice number 3: ", result)  # Print output using split function
    else:
        result = "Invalid choice. Please enter a valid option (1, 2, or 3)."
        print(result) # Print invalid choice message

    result_text.configure(state="normal")
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, str(result))
    result_text.configure(state="disabled")

# Create the Tkinter window
window = tk.Tk()
window.title("Text Tokenizer")

# Text entry field
text_label = tk.Label(window, text="Enter a text:")
text_label.pack()
text_entry = tk.Text(window, height=5)
text_entry.pack()

# Choice dropdown
choice_label = tk.Label(window, text="Choose an option:")
choice_label.pack()
choice_var = tk.StringVar()
choice_dropdown = tk.OptionMenu(window, choice_var, "print tokenized words",
                                "print tokenized sentences",
                                "print output using split function.")
choice_dropdown.pack()

# Button to perform the operation
perform_button = tk.Button(window, text="Perform", command=perform_operation)
perform_button.pack()

# Result text field
result_label = tk.Label(window, text="Result:")
result_label.pack()
result_text = tk.Text(window, height=10, state="disabled")
result_text.pack()

# Start the Tkinter event loop
window.mainloop()