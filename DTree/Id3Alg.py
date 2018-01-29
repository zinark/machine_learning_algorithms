import math
import pandas as pd


class Id3Alg(object):
    def fit(self, data):
        self.data = pd.DataFrame(data)

    def information_gain(self, target_attr, class_attr):
        dt = self.data

        freq = dt[class_attr].value_counts()
        values = freq.keys()

        possibilities = []
        for value in values:
            print value, freq[value], len(dt)
            p = 1. * freq[value] / len(dt)
            possibilities.append(p)

        base_entropy = self.entropy(possibilities)

        result = 0.

        freq = dt[target_attr].value_counts()
        for k in freq.keys():
            print target_attr, "=", k, ", the distribution of", class_attr
            filtered_dt = dt[dt[target_attr] == k]
            freq_inner = filtered_dt[class_attr].value_counts()

            plist = []
            for fi in freq_inner.keys():
                p = 1. * freq_inner[fi] / len(filtered_dt)
                print "\t\t", fi, p
                plist.append(p)
            prob = 1. * len(filtered_dt) / len(dt[target_attr])
            entropy = self.entropy(plist)
            print "plist =", entropy, prob
            result += entropy * prob
        return base_entropy - result

    def entropy(self, possibilities):
        e = 0.
        for p in possibilities:
            e += p * math.log(p, 2)
        return -e

    def predict(self, class_attr, x):
        dt = self.data
        for attr in dt.columns.values:
            if attr == class_attr: continue
            print "================="
            print self.information_gain(attr, class_attr)
        pass
