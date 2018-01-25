import math
from decimal import Decimal, getcontext

getcontext().prec = 30


class CoreVector:
    def __init__(self, coords):
        if not coords:
            raise ValueError("no coords")

        try:
            self.coords = ([Decimal(x) for x in coords])
            self.dimension = len(coords)

        except ValueError:
            raise ValueError("coords should be non-empty")

        except TypeError:
            raise TypeError("coords should be an iterable object")

    def __str__(self):
        return "Vector: {}".format([round(c, 3) for c in self.coords])

    def __eq__(self, other):
        return self.coords == other.coords

    def plus(self, other):
        result = [x + y for x, y in zip(self.coords, other.coords)]
        return CoreVector(result)

    def sub(self, other):
        result = [x - y for x, y in zip(self.coords, other.coords)]
        return CoreVector(result)

    def scale(self, scale):
        result = [Decimal(x * scale) for x in self.coords]
        return CoreVector(result)

    def magnitude(self):
        return Decimal(math.sqrt(sum([x ** 2 for x in self.coords])))


    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.scale(Decimal('1.0') / magnitude)
        except ZeroDivisionError:
            raise ValueError("magnitude is zero it can not have a direction")

    def dot(self, other):
        multiplications = [x * y for x, y in zip(self.coords, other.coords)]
        return Decimal(sum(multiplications))

    def area_of_parallelogram(self, other):
        return self.cross_product(other).magnitude()

    def cross_product(self, other):
        if self.dimension != 3:
            raise ValueError("dimension should be 3")

        result = [
            self.coords[1] * other.coords[2] - other.coords[1] * self.coords[2],
            - (self.coords[0] * other.coords[2] - other.coords[0] * self.coords[2]),
            self.coords[0] * other.coords[1] - other.coords[0] * self.coords[1]
        ]
        return CoreVector(result)

    def is_zero_vector(self):
        return round(self.magnitude(), 3) == 0

    def angle_with(self, other, in_degrees=False):
        u1 = self.normalized()
        u2 = other.normalized()
        dot = round(u1.dot(u2), 10)
        result = math.acos(float(dot))
        if in_degrees:
            return math.degrees(result)
        return result

    def is_parallel_with(self, other):
        if abs(self.magnitude()) < 1e-30:
            return True

        if abs(other.magnitude()) < 1e-30:
            return True

        return self.angle_with(other) % math.pi == 0

    def is_orthogonal_with(self, other):
        return round(self.dot(other), 3) == 0

    def component_orthogonal_to(self, other):
        return self.sub(self.component_parallel_to(other))

    def component_parallel_to(self, other):
        unit_vector = other.normalized()
        length = self.dot(unit_vector)  # vii
        projection = unit_vector.scale(length)
        if self.angle_with(other) <= math.pi:
            return projection
        else:
            return -projection
