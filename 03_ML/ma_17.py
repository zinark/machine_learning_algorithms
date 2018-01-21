from prep_terrain_data import makeTerrainData
from pretty_picture import prettyPicture
from sklearn.naive_bayes import GaussianNB

features_train, labels_train, features_test, labels_test = makeTerrainData()
clf = GaussianNB()
clf.fit(features_train, labels_train)


def accuracy_score():
    global corrects, total_points
    print "score", clf.score(features_test, labels_test)
    corrects = 0.
    total_points = len(features_test)
    for i in range(total_points):
        input = features_test[i]
        output = labels_test[i]
        if output == clf.predict([input]):
            corrects += 1


print "accuracy", corrects / total_points
prettyPicture(clf, features_test, labels_test)
