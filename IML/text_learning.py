# coding=utf-8
import pandas as pd

docs = [
    "Feature extraction is very different from Feature selection",
    "The former consists in transforming arbitrary data, such as text or images, into numerical features usable for machine learning.",
    "The latter is a machine learning technique applied on these features."
]

ys = [1, 0, 0]

def bag_of_words():
    from sklearn.feature_extraction.text import CountVectorizer
    vectorizer = CountVectorizer(decode_error='replace', strip_accents='unicode', stop_words='english')
    data = vectorizer.fit_transform(docs).toarray()
    df = pd.DataFrame(data, columns=vectorizer.get_feature_names())
    return df


def tf_idf():
    """
    TF : term frequency

    IDF : inverse document frequency
    """
    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer(stop_words='english')
    data = vectorizer.fit_transform(docs).toarray()
    df = pd.DataFrame(data, columns=vectorizer.get_feature_names())
    return df


df = tf_idf()
from sklearn.naive_bayes import GaussianNB

clf = GaussianNB ()
clf.fit(df, ys)


print clf.score(df, ys)
