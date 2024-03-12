import pandas as pd
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Load the CSV dataset
data = pd.read_csv("C:\\Users\\HP\\Documents\\GitHub\\NLP-Tasks\\Task 2\\Reddit_Data.csv")  

# Check for missing values
data = data.dropna(subset=["clean_comment"])  # Drop rows with missing 'clean_comment' values

# Define functions for tokenization and stemming
def tokenize(text):
    return word_tokenize(text.lower())  # Convert to lowercase

def stem(tokens):
    stemmer = PorterStemmer()
    return [stemmer.stem(token) for token in tokens]

# Apply tokenization and stemming
data["clean_comment"] = data["clean_comment"].apply(str)  # Convert 'clean_comment' column to string
data["clean_comment"] = data["clean_comment"].apply(tokenize)  
data["clean_comment"] = data["clean_comment"].apply(stem)

# Print the modified DataFrame
print(data)