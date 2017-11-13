import string

from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


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
    stemmer = PorterStemmer()
    stemmed = map(lambda word: stemmer.stem(word), word_list)
    return list(stemmed)


def make_keywords(text):
    normalized_text = normalize(text)
    tokens = word_tokenize(normalized_text)
    tokens_without_stopwords = remove_stopwords(tokens)
    keywords = stemming(tokens_without_stopwords)
    return keywords
