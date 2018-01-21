import matplotlib.pyplot as plt

sizes = [
    (1700, 53), (2100, 44), (1900, 59),
    (1300, 82), (1600, 50), (2200, 68)]

sizes = [
    (1300, 88000), (1400, 72000), (1600, 94000),
    (1900, 86000), (2100, 112000), (2300, 98000)]

xs, ys = zip(*sizes)

median_sizes = []

for i in range(0, len(sizes), 2):
    x1 = sizes[i][0]
    y1 = sizes[i][1]

    x2 = sizes[i + 1][0]
    y2 = sizes[i + 1][1]

    xmean = (x1 + x2) / 2
    ymean = (y1 + y2) / 2
    median_sizes.append((xmean, ymean))


# for size, price in sizes:
#     cost_per_area = float(price) / size
#     print "$/ft2=", cost_per_area, "ft2=", size, " + $", price
#     print size * cost_per_area, price
#     print

def bar_chart(data, c='b'):
    xs, ys = zip(*data)
    plt.bar(xs, ys, 75, align='center', color=c)
    plt.xticks(xs)


bar_chart(sizes)
bar_chart(median_sizes, 'r')
plt.show()
