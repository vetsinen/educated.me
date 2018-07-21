import string
import collections

from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from pprint import pprint


def process_text(text, stem=True):
    """ Tokenize text and stem words removing punctuation """
    # text = text.translate(None, string.punctuation)
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)

    if stem:
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(t) for t in tokens]

    return tokens


def cluster_texts(texts, clusters=3):
    """ Transform texts to Tf-Idf coordinates and cluster texts using K-Means """
    vectorizer = TfidfVectorizer(tokenizer=process_text,
                                 stop_words=stopwords.words('english'),
                                 max_df=0.5,
                                 min_df=0.1,
                                 lowercase=True)

    tfidf_model = vectorizer.fit_transform(texts)
    km_model = KMeans(n_clusters=clusters)
    km_model.fit(tfidf_model)

    clustering = collections.defaultdict(list)

    for idx, label in enumerate(km_model.labels_):
        clustering[label].append(idx)

    return clustering


if __name__ == "__main__":
    articles = ['SQLAthanor: Serialization / Deserialization for SQLAlchemy ORM And now for something completely different',
     'Framework to do an application a schedule for a University',
     'A nice collection of often useful awesome Python frameworks and libraries',
     'How to use PyDrive to upload files to Google Drive through python', 'Ranking News Bias with Python',
     'I`ve made a clock using pyglet, but I want to change the window bg color every second.Why is the code I’ve used make the bg flicker and not go from white to black all the way',
     'Sending and pulling live data from server.Dreams In Text - Text Based Adventure',
     'I developed a package which will notify your github activity and it is working on mac windows and linux platform.',
     'Getting the active(foreground) window title on windows 10 using python',
     'Chameleon:An HTML / XML template engine for Python',
     'SubstanceDesigner now allows you to script its behavior using Python', 'Fuction and Home key in pyautogui',
     'How to install win32 on Windows 10', 'Python has brought computer programming to a vast new audience',
     'Exceptive: A Library Making Exception Handling More Programmatic and Debuggable']
    clusters = cluster_texts(articles, 3)
    pprint(dict(clusters))