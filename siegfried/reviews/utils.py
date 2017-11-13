import string

from nltk.corpus import stopwords
from nltk.stem.snowball import PorterStemmer


def normalize(text):
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    text = text.lower()
    text = ' '.join(text.split())
    return text


def remove_stopwords(word_list):
    stops = set(stopwords.words('english'))
    filtered = [word for word in word_list if word not in stops]
    return filtered


def stemming(word_list):
    stemmer = PorterStemmer('english')
    stemmed = map(lambda word: stemmer.stem(word), word_list)
    return list(stemmed)
