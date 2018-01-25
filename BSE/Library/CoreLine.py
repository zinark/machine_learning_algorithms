from decimal import Decimal, getcontext

getcontext().prec = 30

from BSE.Library.CoreVector import CoreVector


class CoreLine(object):
    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

        if not normal_vector:
            all_zeros = ['0'] * self.dimension
            normal_vector = CoreVector(all_zeros)
        self.normal_vector = CoreVector(normal_vector)
        self.dimension = len(normal_vector)

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()

    def is_parallel(self, other):
        n1 = self.normal_vector
        n2 = other.normal_vector
        return n1.is_parallel_with(n2)
        # it is also possible by calculating with slope
        # n_self = self.normal_vector.is_parallel_with(other)
        # n_other = other.normal_vector
        # m_self = n_self.coords[0] / n_self.coords[1]
        # m_other = n_other.coords[0] / n_other.coords[1]
        # return m_self == m_other

    def __eq__(self, other):
        if not self.is_parallel(other):
            return False

        x0 = self.basepoint
        y0 = other.basepoint
        basepoint_diff = x0.sub(y0)
        n = self.normal_vector
        return basepoint_diff.is_orthogonal_with(n)

        # Dirty one
        a = self.normal_vector.coords[0]
        b = self.normal_vector.coords[1]
        k = self.constant_term

        p1 = [0, k / b]
        p2 = [k / a, 0]

        o_a = other.normal_vector.coords[0]
        o_b = other.normal_vector.coords[1]
        o_k = other.constant_term

        o_p1 = [0, o_k / Decimal(o_b)]
        o_p2 = [o_k / o_a, 0]

        if round(p1[1], 3) == round(o_p1[1], 3):
            return True
        return False

    def intersection(self, other):
        if self.is_parallel(other):
            if self.__eq__(other):
                return 999999999999999999999
            else:
                return None
            # raise ValueError("no solution")

        A, B = self.normal_vector.coords
        C, D = other.normal_vector.coords
        k1 = self.constant_term
        k2 = other.constant_term

        # x_num = D * k1 - B * k2
        # y_num = - C * k1 + A * k2
        # one_over_denom = Decimal('1') / (A * D - B * C)
        # return CoreVector([x_num, y_num]).scale(one_over_denom)
        x = Decimal(D * k1 - B * k2) / Decimal(A * D - B * C)
        y = Decimal(-C * k1 + A * k2) / Decimal(A * D - B * C)
        return (x, y)

    def set_basepoint(self):
        # print self.normal_vector, self.constant_term
        # try:
        n = self.normal_vector.coords
        c = self.constant_term
        basepoint_coords = ['0'] * self.dimension

        initial_index = CoreLine.first_nonzero_index(n)
        initial_coefficient = n[initial_index]

        basepoint_coords[initial_index] = c / initial_coefficient
        self.basepoint = CoreVector(basepoint_coords)

        # except Exception as e:
        #     if str(e) == CoreLine.NO_NONZERO_ELTS_FOUND_MSG:
        #         self.basepoint = None
        #     else:
        #         raise e

    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector.coords

        try:
            initial_index = CoreLine.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i == initial_index)) + 'x_{}'.format(i + 1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output

    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(CoreLine.NO_NONZERO_ELTS_FOUND_MSG)


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps
