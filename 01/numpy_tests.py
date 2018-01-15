import numpy as np
import matplotlib.pyplot as plt


def io_processes_file():
    a = np.loadtxt('data.txt', skiprows=1, unpack=False)
    print a
    print np.rot90(a)

    b = np.genfromtxt('data.txt', skip_header=1, filling_values=-999)
    print b

    c = np.random.random((5, 5))
    print c
    np.savetxt('saved.txt', c, delimiter=',')
    np.savez_compressed('saved', c)


def creating_arrays_and_matrixes():
    a = [[1, 2, 3, 4], [2, 3, 4, 5]]
    # print np.array(a)
    print np.ones((1, 2))
    print np.zeros([2, 1], dtype=np.double)
    print np.empty([1, 2])
    print np.random.random((2, 1))
    print np.full((2, 3), 7)
    print np.arange(0, 100, 5)
    print np.linspace(0, 2, 9)
    print;
    print
    print "identity ve eye"
    print;
    print
    print "eye"
    print np.eye(4)
    print "identity"
    print np.identity(4)
    m = np.random.random((3, 3))
    print m
    print np.identity(3)
    print m * np.identity(3)


def inspect_arrays():
    a = np.array([[1, 2, 3], [2, 3, 4], [9, 3, 1], [1, 1, 1]])
    print a
    print a.astype(float)

    print 'dimensions:', a.ndim
    print 'size:', a.size
    print 'bytes', a.nbytes
    print 'itemsize', a.itemsize
    print 'shape', a.shape

    # broadcasting

    x = np.ones((3, 4))
    print x.shape
    y = np.random.random((3, 4))
    print y.shape

    print x + y

    a = np.ones((3, 4))
    b = np.arange(0, 4, 1)

    print a
    print b
    print a - b


def broadcast_one():
    x = np.ones((3, 4))
    y = np.random.random((5, 1, 4))
    print 'x'
    print x, x.shape
    print 'y'
    print y, y.shape
    print;
    print 'x+y'
    print x + y


def arithmetic_matrixs():
    x = np.ones((2, 3))
    y = np.ones((2, 3))
    print np.add(x, y)
    print np.subtract(x, y)
    print np.multiply(x, y)
    print np.divide(x, y)
    print np.remainder(x, y)

    a = np.array([
        [1, 2, 3],
        [10, 20, 30]
    ])

    print a
    print "sum", a.sum()
    print "min", a.min()
    print "max", a.max()

    print "min-axis=0", a.min(axis=0)
    print "max-axis=0", a.max(axis=0)

    print "min-axis=1", a.min(axis=1)
    print "max-axis=1", a.max(axis=1)

    print "cumsum", a.cumsum()
    print "cumsum-axis=0", a.cumsum(axis=0)
    print "cumsum-axis=1", a.cumsum(axis=1)

    print a.mean()
    print a.std()

    print np.logical_and(a, np.zeros((2, 3)))
    print np.logical_or(a, np.zeros((2, 3)))
    print np.logical_not(a, np.ones((2, 3)))

    print np.transpose(a)
    print a.T


def resize_matrix():
    a = np.array([
        [1, 2, 3, 4, 5, 6]
    ])

    b = np.array([
        [1, 2, 3, 4, 5, 6]
    ])

    b.resize((3, 3))
    print "b", b

    print a.reshape((1, 6))
    print a.reshape((2, 3))
    print a.reshape((3, 2))
    print a.reshape((6, 1))

    print "a", a.ravel()


def append():
    a = np.array([[1, 2], [2, 3]])

    print a
    print np.append(a, [[5], [5]], axis=1)
    print np.append(a, [[5, 5]], axis=0)

    print np.insert(a, 0, [5, 50], axis=0)
    print np.delete(a, [1])


def visualize():
    a = np.array([[10, 20, 25, 20], [1, 2, 1, 2]])
    print np.histogram(a)
    print a

    plt.hist(a.ravel(), bins=range(0, 30))
    plt.title('Frequency of My 3D Array Elements')
    plt.grid()
    # plt.show()

    print np.meshgrid(a)


def visualize_2():
    points = np.arange(-5, 5, 0.1)
    xs, ys = np.meshgrid(points, points)
    print "XS", xs
    print "YS", ys

    z = np.sqrt(xs ** 2 + ys ** 2)
    print z

    plt.imshow(z, cmap=plt.cm.gray)
    plt.colorbar()
    plt.show()

