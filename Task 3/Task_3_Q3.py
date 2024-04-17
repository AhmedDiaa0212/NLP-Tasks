import tkinter as tk
from tkinter import ttk
from nltk.corpus import stopwords

def get_stopwords(language):
    stop_words = stopwords.words(language)
    return stop_words

def show_stopwords():
    selected_language = language_combobox.get()
    stopwords_list = get_stopwords(selected_language)
    stopwords_text.delete(1.0, tk.END)
    print( "   -   ".join(stopwords_list))
    stopwords_text.insert(tk.END, "\n".join(stopwords_list))

# Create the main window
window = tk.Tk()
window.title("Common Stop Words in Various Languages")

# Create a title label
title_label = ttk.Label(window, text="Common Stop Words in Various Languages", font=("Helvetica", 14, "bold"))
title_label.pack(pady=20)

# Create a language selection label and combobox
language_label = ttk.Label(window, text="Select a Language:")
language_label.pack()
language_combobox = ttk.Combobox(window, values=['english', 'spanish', 'french', 'german'])
language_combobox.pack(pady=10)

# Create a button to display the stop words
show_button = ttk.Button(window, text="Show Stop Words", command=show_stopwords)
show_button.pack(pady=10)

# Create a text widget to display the stop words
stopwords_text = tk.Text(window, height=10, width=50)
stopwords_text.pack()

# Start the main event loop
window.mainloop()