import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string
import os

# map met de originele tekstbestanden
input_dir = "C:\\Project 1 informatica\\Trivauto\\origineel"

# map waar de opgeschoonde bestanden moeten worden opgeslagen
output_dir = "C:\\Project 1 informatica\\Trivauto\\prepped"

def preprocess_text(text):

    # Tokenization
    tokens = word_tokenize(text)

    # Stopwoordverwijdering
    stop_words = set(stopwords.words('dutch'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

    # Stemming en lemmatization
    ps = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    stemmed_tokens = [ps.stem(token) for token in filtered_tokens]
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

    # Verwijderen van leestekens en speciale tekens
    table = str.maketrans('', '', string.punctuation)
    stripped_tokens = [token.translate(table) for token in lemmatized_tokens]

    # Lowercasing
    lowercase_tokens = [token.lower() for token in stripped_tokens]

    # Return de gezuiverde tekst
    return " ".join(lowercase_tokens)

for filename in os.listdir(input_dir):
    if filename.endswith(".txt"):
        # pad naar het huidige bestand
        input_path = os.path.join(input_dir, filename)

        # lees de inhoud van het bestand
        with open(input_path, "r", encoding="utf-8") as f:
            text = f.read()

        # voer de preprocessing uit op de tekst
        prepped_text = preprocess_text(text)

        # bepaal de nieuwe bestandsnaam (met "prepped" erin)
        output_filename = filename.replace(".txt", "_prepped.txt")
        output_path = os.path.join(output_dir, output_filename)

        # schrijf de opgeschoonde tekst naar het nieuwe bestand
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(prepped_text)
