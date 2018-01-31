import math
import pandas as pd


class Id3Alg(object):
    def __init__(self, data):
        self.data = pd.DataFrame(data)

    def best_attribute(self, class_attr):
        dt_others = self.data.drop(class_attr, axis=1)
        dt_class = self.data[class_attr]
        print dt_class
        pass

    def predict(self, class_attr, x):
        done = False

        while not done:
            print "A = best attribute"
            A = self.best_attribute(class_attr)
            done = True

    def entropy_from_data(self, data):
        freq = data.value_counts()
        values = freq.keys()

        possibilities = []
        for value in values:
            # print value, freq[value], len(dt)
            p = 1. * freq[value] / len(data)
            possibilities.append(p)

        return self.entropy(possibilities)

    def information_gain(self, target_attr, class_attr):
        dt = self.data

        base_entropy = self.entropy_from_data(dt[class_attr])

        result = 0.

        freq = dt[target_attr].value_counts()
        for k in freq.keys():
            # print target_attr, "=", k, ", the distribution of", class_attr
            filtered_dt = dt[dt[target_attr] == k]
            freq_inner = filtered_dt[class_attr].value_counts()

            plist = []
            for fi in freq_inner.keys():
                p = 1. * freq_inner[fi] / len(filtered_dt)
                # print "\t\t", fi, p
                plist.append(p)
            prob = 1. * len(filtered_dt) / len(dt[target_attr])
            entropy = self.entropy(plist)
            # print "plist =", entropy, prob
            result += entropy * prob

        return base_entropy - result

    def entropy(self, possibilities):
        e = 0.
        for p in possibilities:
            e += p * math.log(p, 2)
        return -e

    def predict_old(self, class_attr, x):
        tree = {}
        dt = self.data

        gained_infos = {}
        for attr in dt.columns.values:
            if attr == class_attr: continue
            gained_infos[attr] = self.information_gain(attr, class_attr)

        print gained_infos
        max_attr = max(gained_infos)
        print max_attr, gained_infos[max_attr]

        for val in dt[max_attr].value_counts().keys():
            print val
            if not tree.has_key(max_attr):
                tree[max_attr] = {}
            tree[max_attr][val] = {}

        to_iterate_attr = []
        for val in tree[max_attr]:
            print val
            data = dt[dt[max_attr] == val][class_attr]

            e = self.entropy_from_data(data)
            if e == 0:
                tree[max_attr][val] = data.iloc[0]
            else:
                to_iterate_attr.append(val)

        print to_iterate_attr
        print tree

    def build_tree(self, class_attr):
        dt = self.data
        print dt
        print self.calc_entropy(dt[class_attr])
        print "o", self.calc_p(dt[class_attr])

        # decided_attr = dt["X"]
        # p_attr = self.calc_p(decided_attr)
        # print "x", p_attr
        # vals = decided_attr.unique()
        # for val in vals:
        #     class_values = dt[decided_attr == val][class_attr]
        #     print "e(class_values,",val,")=", self.calc_entropy(class_values)

        for val in dt["X"].unique():
            print self.calc_entropy_on_attr("X", val, class_attr)

        # print self.calc_entropy(dt["Y"])
        # print "y", self.calc_p(dt["Y"])

    def calc_entropy_on_attr(self, attr, val, class_attr):
        dt = self.data
        decided_attr = dt[attr]
        possibilities = self.calc_p(decided_attr)
        print attr, possibilities
        vals = decided_attr.unique()
        for val in vals:
            class_values = dt[decided_attr == val][class_attr]
            print "e(class_values,", val, ")=", self.calc_entropy(class_values)

    def calc_entropy(self, series):
        vals = series.values
        freq = series.value_counts()
        total = len(vals)
        e = 0.
        for value, frequency in freq.iteritems():
            p = 1. * frequency / total
            e += p * math.log(p, 2)
        return -e

    def calc_p(self, series):
        vals = series.values
        freq = series.value_counts()
        total = len(vals)
        result = []
        for value, frequency in freq.iteritems():
            p = 1. * frequency / total
            result.append(p)
        return result
