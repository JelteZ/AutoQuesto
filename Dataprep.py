import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

word = "running"
lemma = lemmatizer.lemmatize(word, pos='v') # specify part of speech to disambiguate
print(lemma) # output: runimport nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

word = "running"
lemma = lemmatizer.lemmatize(word, pos='v') # specify part of speech to disambiguate
print(lemma) # output: run