from tkinter import ttk
import nltk
from nltk.tokenize import word_tokenize
import tkinter as tk

# Download the necessary resources for the taggers
# nltk.download('averaged_perceptron_tagger')
# nltk.download('universal_tagset')

def perform_pos_tagging(tagset='default'):
    """Function to perform part-of-speech tagging based on the selected tagset"""
    text = input_text.get("1.0", "end").strip()
    tokens = word_tokenize(text)
    
    if tagset == 'default':
        tagged_words = nltk.pos_tag(tokens)
        tagset_name = 'Penn Treebank (Default) tagset'
    else:
        tagged_words = nltk.pos_tag(tokens, tagset='universal')
        tagset_name = 'universal'
    
    result_text.delete("1.0", "end")
    result_text.insert("1.0", f"{tagset_name} Tagset:\n")
    result_text.insert("end", tagged_words)

# Create the main window
window = tk.Tk()
window.title("POS Tagger")
window.geometry("400x300")

# Create the input label and text box
input_label = ttk.Label(window, text="Enter a sentence:")
input_label.pack()
input_text = tk.Text(window, height=3)
input_text.pack()

# Create the method selection label and radio buttons
method_label = ttk.Label(window, text="Select a method:")
method_label.pack()
method_var = tk.StringVar(value="default")
default_radio = ttk.Radiobutton(window, text="Penn Treebank (Default) tagset", variable=method_var, value="default")
default_radio.pack()
penn_radio = ttk.Radiobutton(window, text="universal Tagset", variable=method_var, value="universal")
penn_radio.pack()

# Create the button to trigger the tagging
tag_button = ttk.Button(window, text="Tag", command=lambda: perform_pos_tagging(method_var.get()))
tag_button.pack()

# Create the result container
result_label = ttk.Label(window, text="Result:")
result_label.pack()
result_text = tk.Text(window, height=10)
result_text.pack()

# Start the main loop
window.mainloop()