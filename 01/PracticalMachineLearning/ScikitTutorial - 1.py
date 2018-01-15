import numpy as np
from sklearn import svm
from sklearn import datasets

from matplotlib import pyplot as plt

# http://scikit-learn.org/stable/tutorial/basic/tutorial.html

# Supervised Learning
#   - Classification ( Vektorlere gore etiketle)
#                                           Ornek :  El yazisi numaralarin ne oldugunu bul
#
#   - Regression    ( Vektorlere gore deger bic)
#                                           Ornek : Balilarin agirliklarina ve yaslarina gore boyunu bul

# Unsupervised learning
#   - Clustering            (Vektorlerden gruplar olustur)
#   - Density Estimation    (Vecktorlerden yogunluk gruplari olustur)

# iris = datasets.load_iris()

digits = datasets.load_digits()
sample_index = 113


def ornek_resim():
    # Her resim 8x8
    sample_image = digits.images[sample_index]
    print "Ornek index :", sample_index
    print "Ornek resim :", sample_image
    print "Resim sekli : ", np.shape(sample_image)
    plt.imshow(sample_image)
    # plt.show()


def etiketler_ve_data():
    # Data'da tum ornekler 8x8 =64lik dizi olarak gosterilir.
    data = digits.data
    target = digits.target
    print "Ornek resmin tek satir dizi hali:", digits.data[sample_index]
    print "Ornegin etiketi : ", digits.target[sample_index]


ornek_resim()
etiketler_ve_data()

classifier = svm.SVC(gamma=0.001, C=100.)

print classifier.fit(digits.data[:-1], digits.target[:-1])
given_input = digits.data[113]
print "input : ", given_input
print classifier.predict([given_input])


# En basit sekilde bir ornek
data = np.array([[10,3], [20,4], [10, 100], [15, 50]])
labels = np.array([0, 0, 1, 1])
classifier = svm.SVC()
classifier.fit(data, labels)
print "Bulunan 1: ", classifier.predict([[10, 3]])
print "Bulunan 2: ", classifier.predict([[20, 4]])
print "Bulunan 3: ", classifier.predict([[10, 100]])
print "Bulunan 4: ", classifier.predict([[15, 50]])
print "Bulunan [3-4]: ", classifier.predict([[13, 75]])
print "Bulunan [1-2]: ", classifier.predict([[17, 9]])
