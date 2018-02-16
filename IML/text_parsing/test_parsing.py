import os
import string
import pickle

from nltk.stem.snowball import SnowballStemmer
data = {}
limit = -1
with open ('from_chris.txt', 'r') as f:
    lines = f.read().split()
    data['chris'] = {
        "files" : lines[:limit]
    }

with open ('from_sara.txt', 'r') as f:
    lines = f.read().split()
    data['sara'] = {
        "files" : lines[:limit]
    }

stemmer = SnowballStemmer('english')
from_data = []
word_data = []

for name in data.keys():
    data[name]["words"] = []
    for file in data[name]["files"]:
        print name, "->", file
        file = os.path.join("/Volumes/MAC/Users/ferhat", file)

        from_data.append(0 if name == "sara" else 1)

        with open(file, 'r') as f:
            content = f.read().split("X-FileName:")[1]
            content = str(content.translate(string.maketrans("", ""), string.punctuation))
            for i in ["sara", "shackleton", "chris", "germani"]:
                content = content.replace(i, "")

            word_list = [stemmer.stem(x) for x in content.split()]
            words = string.join(word_list, " ")
            data[name]["words"].append(words)
            word_data.append(words)

pickle.dump(data, open ("authors_and_words.pkl", "w"))
pickle.dump(from_data, open ("your_email_authors.pkl", "w"))
pickle.dump(word_data, open ("your_word_data.pkl", "w"))