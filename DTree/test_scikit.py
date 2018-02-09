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
import math


def chart_iris():
    import pandas as pd
    import numpy as np
    from sklearn.datasets import load_iris
    import matplotlib.pyplot as plt
    from sklearn.tree import tree
    x1_input = "sepal length (cm)"
    x2_input = "sepal width (cm)"

    def create_training_data(dt):
        training_data = dt[[x1_input, x2_input, "target"]]
        training_x = []
        training_y = []
        for i, row in training_data.iterrows():
            x1 = row[x1_input]
            x2 = row[x2_input]
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
            x = dt[dt["target"] == t][x1_input].values
            y = dt[dt["target"] == t][x2_input].values
            plt.scatter(x, y, label=label, s=10)
        plt.xlabel(x1_input)
        plt.ylabel(x2_input)
        plt.legend()

    iris = load_iris()
    dt = convert_to_dataframe(iris)
    training_x, training_y = create_training_data(dt)
    clf = tree.DecisionTreeClassifier(criterion='gini')
    clf.fit(training_x, training_y)
    x_range = np.arange(4, 8, 0.01)
    y_range = np.arange(1, 4, 0.01)
    xx, yy = np.meshgrid(x_range, y_range)
    z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    z = z.reshape(xx.shape)
    plt.contourf(xx, yy, z, cmap='afmhot', alpha=0.3)
    plot_data(dt)
    plt.show()

    # http://www.webgraphviz.com/
    # dot -Tpng tree.dot > tree_entropy.png
    from sklearn.tree import export_graphviz
    dot_data = export_graphviz(clf,
                               out_file="tree.dot",
                               feature_names=iris.feature_names[:2],
                               class_names=iris.target_names,
                               rounded=False,
                               filled=True
                               )


def gini_vs_entropy():
    import numpy as np
    import matplotlib.pyplot as plt
    def gini(p):
        return p * (1 - p) + (1 - p) * p

    def entropy(p):
        return - p * math.log(p, 2) + (1 - p) * math.log(1 - p, 2)

    def error(p):
        return 1 - max([p, 1 - p])

    x = np.arange(0.0, 1.0, 0.01)

    ent = [entropy(p) if p != 0 else None for p in x]

    sc_ent = [e * 0.5 if e else None for e in ent]
    err = [error(i) for i in x]

    fig = plt.figure(figsize=(10, 8))
    ax = plt.subplot(111)
    for i, lab, ls, c, in zip([ent, sc_ent, gini(x), err],
                              ['Entropy', 'Entropy (scaled)',
                               'Gini Impurity',
                               'Misclassification Error'],
                              ['-', '-', '--', '-.'],
                              ['black', 'lightgray',
                               'red', 'green', 'cyan']):
        line = ax.plot(x, i, label=lab,
                       linestyle=ls, lw=2, color=c)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),
              ncol=3, fancybox=True, shadow=False)
    ax.axhline(y=0.5, linewidth=1, color='k', linestyle='--')
    ax.axhline(y=1.0, linewidth=1, color='k', linestyle='--')
    plt.ylim([0, 1.1])
    plt.xlabel('p(i=1)')
    plt.ylabel('Impurity Index')
    plt.show()

chart_iris()