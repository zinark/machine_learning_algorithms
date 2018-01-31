# Classification
# Iris Flower Set
# Graphviz
# Decision Tree Algorithms : ID3, CART, Gini, Entropy, Information Gain
# Regression
# Regularization
# HR Attribute Prediction
# conda create --name test_dt spyder jupyter seaborn scikit-learn
# conda info --envs
# activate test_dt

from sklearn import tree


def test_train():
    X = [[0, 0], [1, 2], [5, 6], [7, 8]]
    y = [0, 1, 2, 3]
    clf = tree.DecisionTreeClassifier()
    clf.fit(X, y)
    input = [5., 4.]
    print clf.predict([input])
    print clf.predict_proba([input])


def test_tree():
    import sklearn
    from sklearn.datasets import load_iris
    iris = load_iris()
    # print iris.target_names
    # print iris.feature_names
    # print iris.data[:5]
    X = iris.data[:, ]
    y = iris.target
    print X
    print y
    clf = sklearn.tree.DecisionTreeClassifier(random_state=10, presort=True)
    clf.fit(X, y)
    from sklearn.tree import export_graphviz
    # http://www.webgraphviz.com/
    dot_data = export_graphviz(clf,
                               out_file="tree.dot",
                               feature_names=iris.feature_names,
                               class_names=iris.target_names,
                               rounded=True,
                               filled=True
                               )


def test_visualize():
    global X, y, clf
    import numpy as np
    import seaborn as sns
    sns.set_style("whitegrid")
    import matplotlib.pyplot as plt
    df = sns.load_dataset("iris")
    col = ['petal_length', 'petal_length']
    df["tmp"] = df["species"].map({
        "setosa": 0,
        "versicolor": 1,
        "virginica": 2
    })
    X = df.loc[:, col]
    y = df["tmp"]
    clf = tree.DecisionTreeClassifier()
    clf.fit(X, y)
    Xv = X.values.reshape(-1, 1)
    h = 0.02
    x_min, x_max = Xv.min(), Xv.max() + 1
    y_min, y_max = y.min(), y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    z = z.reshape(xx.shape)
    fig = plt.figure(figsize=(16, 10))
    ax = plt.contourf(xx, yy, z, cmap='afmhot', alpha=0.3)
    plt.scatter(X.values[:, 0], X.values[:, 1], c=y, s=80, alpha=.9, edgecolors='g')
    plt.show()


def line_chart_1():
    import matplotlib.pyplot as plt
    x = [1, 2, 3]
    y = [3, 5, 1]
    x2 = [1, 2, 3]
    y2 = [10, 20, 30]
    plt.plot(x, y, label="f1")
    plt.plot(x2, y2, label="f2")
    plt.xlabel("input")
    plt.ylabel("value")
    plt.legend()
    plt.title("test\nAnother title")
    plt.show()


def bar_chart_2():
    import matplotlib.pyplot as plt
    x = [2, 4, 6, 8, 10]
    y = [6, 7, 8, 2, 4]
    x2 = [1, 3, 5, 7, 9]
    y2 = [4, 2, 3, 4, 1]
    plt.bar(x, y, label="b1", color='green')
    plt.bar(x2, y2, label="b2", color='red')
    plt.title("chart 2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()


def hist_chart_2d_3():
    import matplotlib.pyplot as plt
    ages = [20, 21, 22, 22, 26, 24, 25, 25, 25, 38, 38, 32, 55, 56, 55, 57, 57, 39, 36, 36, 78, 88, 99, 101]
    plt.hist(ages, histtype='bar', rwidth=0.8)
    plt.show()


def chart_4():
    import matplotlib.pyplot as plt
    x = [1, 2, 3, 4, 5]
    y = [10, 5, 1, 50, 10]
    y2 = [5, 10, 15, 20, 1]
    plt.scatter(x, y, label='y1', color='red', marker='+', s=50)
    plt.scatter(x, y2, label='y2', color='green', marker='*', s=100)
    plt.show()


def chart_stacked_plot_5():
    import matplotlib.pyplot as plt
    days = [1, 2, 3]
    sleep = [7, 6, 9]
    eat = [1, 2, 1]
    play = [3, 4, 1]
    plt.stackplot(days, sleep, labels=['sleep'])
    plt.stackplot(days, play, labels=['play'])
    plt.stackplot(days, eat, labels=['eat'])

    plt.legend()
    plt.show()


def chart_6():
    import matplotlib.pyplot as plt
    slices = [7, 12, 10, 3]
    labels = ['sleep', 'eat', 'work', 'play']
    plt.pie(slices, labels=labels, startangle=90, shadow=True, explode=(0, .1, 0, 0), autopct='%1.1f%%')
    plt.legend()
    plt.show()


def chart_iris():
    import pandas as pd
    import numpy as np
    from sklearn.datasets import load_iris
    import matplotlib.pyplot as plt
    from sklearn.tree import tree

    def create_training_data(dt):
        training_data = dt[["petal length (cm)", "petal width (cm)", "target"]]
        training_x = []
        training_y = []
        for i, row in training_data.iterrows():
            x1 = row["petal length (cm)"]
            x2 = row["petal width (cm)"]
            y = row["target"]
            training_x.append([x1, x2])
            training_y.append(y)
        return training_x, training_y

    def convert_to_dataframe(iris):
        dt = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        dt['target'] = iris.target
        # iris.target_names[iris.target]
        return dt

    def plot_data(dt):
        for t in dt["target"].unique():
            label = iris.target_names[t]
            x = dt[dt["target"] == t]["petal length (cm)"].values
            y = dt[dt["target"] == t]["petal width (cm)"].values
            plt.scatter(x, y, label=label, s=10)
        plt.xlabel("petal length")
        plt.ylabel("petal width")
        plt.legend()

    iris = load_iris()
    dt = convert_to_dataframe(iris)
    training_x, training_y = create_training_data(dt)
    clf = tree.DecisionTreeClassifier()
    clf.fit(training_x, training_y)
    x_range = np.arange(0.5, 7, 0.01)
    y_range = np.arange(0, 3, 0.01)
    xx, yy = np.meshgrid(x_range, y_range)
    z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    z = z.reshape(xx.shape)
    print z
    plt.contourf(xx, yy, z, cmap='afmhot', alpha=0.3)
    plot_data(dt)
    plt.show()


chart_iris()
