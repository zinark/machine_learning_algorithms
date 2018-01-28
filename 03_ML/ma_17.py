from prep_terrain_data import makeTerrainData
from pretty_picture import prettyPicture
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

features_train, labels_train, features_test, labels_test = makeTerrainData()
clf_naive_bayes = GaussianNB()
clf_support_vector = SVC()
clf_neural_network = MLPClassifier(
    shuffle=False,
    max_iter=300,
    hidden_layer_sizes=(100,),
    solver='lbfgs')

clf_support_vector.fit(features_train, labels_train)
clf_naive_bayes.fit(features_train, labels_train)
clf_neural_network.fit(features_train, labels_train)

print clf_naive_bayes.score(features_test, labels_test)
print clf_support_vector.score(features_test, labels_test)
print clf_neural_network.score(features_test, labels_test)

prettyPicture(clf_neural_network, features_test, labels_test)


def accuracy_score():
    global corrects, total_points
    print "score", clf_support_vector.score(features_test, labels_test)
    corrects = 0.
    total_points = len(features_test)
    for i in range(total_points):
        input = features_test[i]
        output = labels_test[i]
        if output == clf_support_vector.predict([input]):
            corrects += 1

    print "accuracy", corrects / total_points
