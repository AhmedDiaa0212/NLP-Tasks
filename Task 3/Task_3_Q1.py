from tkinter import *
from tkinter import ttk  
import spacy

"""
Example in English :
The cat sleeps. The sun shines. Birds sing. A car drives by. Time passes.
"""

"""
Example in Spanish:
El gato duerme. El sol brilla. Pájaros cantan. Un coche pasa. El tiempo pasa.
"""
"""

Example in French :
Le chat dort. Le soleil brille. Les oiseaux chantent. Une voiture passe. Le temps passe.
"""

def get_spacy_model(language):
  """
  This function maps language selections to their corresponding spaCy model names.
  """
  model_map = {
      "English": "en_core_web_sm",
      "French": "fr_core_news_sm",
      "Spanish": "es_core_news_sm",   
  }
  # Return None for unsupported languages
  return model_map.get(language, None)  


def tokenize_sentences(text, language):
  """
  This function tokenizes a text into sentences for a specific language.
  """
  # Load the spaCy model for the specified language
  nlp = spacy.load(language)
  # Process the text
  doc = nlp(text)
  # Extract sentences as a list of strings
  sentences = [sent.text.strip() for sent in doc.sents]
  return sentences

def process_text():
  text = text_entry.get()
  language = language_combo.get()
  # Get spaCy model name based on language selection
  spacy_model = get_spacy_model(language)
  # Tokenize the text
  sentences = tokenize_sentences(text, spacy_model)
  result_text.delete(1.0, END)
  # Display results
  for sentence in sentences:
    result_text.insert(END, sentence + "\n")

# Create the main window
root = Tk()
root.title("Text Tokenizer")

# Language selection combobox
language_options = ["English", "Spanish", "French"]
language_combo = ttk.Combobox(root, values=language_options)
language_combo.set(language_options[0])  # Set default selection
language_combo.pack(pady=10)

# Text entry field
text_label = Label(root, text="Enter text:")
text_label.pack()
text_entry = Entry(root)
text_entry.pack(pady=5)

# Process button
process_button = Button(root, text="Process Text", command=process_text)
process_button.pack(pady=20)

# Result display text box
result_label = Label(root, text="Results:")
result_label.pack()
result_text = Text(root, height=10)
result_text.pack()

root.mainloop()