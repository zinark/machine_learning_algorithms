from DataSource import DataSource
from Id3Alg import Id3Alg

id3 = Id3Alg()
id3.fit(DataSource.sample_decision_data())

print id3.predict("Transportation", ["Male", 1, "Standard", "High"])
# print id3.predict("Transportation", ["Male", 0, "Cheap", "Medium"])
# print id3.predict("Transportation", ["Female", 1, "Cheap", "High"])
