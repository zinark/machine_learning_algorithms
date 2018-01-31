from DataSource import DataSource


class Question:
    def __init__(self, column, value):
        self.column = column
        self.value = value

    def match(self, example):
        val = example[self.column]
        if isinstance(val, int) or isinstance(val, float):
            return val >= self.value
        return val == self.value

    def __str__(self):
        condition = "=="
        if isinstance(self.value, int) or isinstance(self.value, float):
            condition = ">="
        return "%s %s %s" % (str(self.column), condition, self.value)


d = DataSource.fruits()


def unique_vals(rows, col):
    return set(row[col] for row in rows)


print unique_vals(d, 0)


def class_counts(rows):
    counts = {}
    for row in rows:
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts

def partition (rows, question):
    true_rows, false_rows = [], []
    for row in rows:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows


print class_counts(d)
print Question(1, "Green")
tlist, flist = partition(d, Question(0, "Red"))
print tlist
print flist