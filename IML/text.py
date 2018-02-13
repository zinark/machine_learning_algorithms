from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd

docs = [
    "At the current rate, the world's oceans on average will be at least 2 feet (61 centimeters) higher by the end of the century compared to today, according to researchers who published in Monday's Proceedings of the National Academies of Sciences.",
    "Outside scientists said even small changes in sea levels can lead to flooding and erosion.",
    "But the process is accelerating, and more than three-quarters of that acceleration since 1993 is due to melting ice sheets in Greenland and Antarctica, the study shows."
]

sw = stopwords.words("english")
stemmer = SnowballStemmer("english")
print stemmer.stem("unbelievable")
tvect = TfidfVectorizer()
tvect.fit_transform(docs)

cvect = CountVectorizer()
m = cvect.fit_transform(docs)
v = cvect.vocabulary_

a = np.array(tvect.fit_transform(docs))
