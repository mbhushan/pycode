import math
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR = "Cannot normalize zero vector!"

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, other):
        ans = [i+j for i, j in zip(self.coordinates, other.coordinates)]
        return Vector(ans)

    def __sub__(self, other):
        ans = [i-j for i, j in zip(self.coordinates, other.coordinates)]
        return Vector(ans)

    def scalar_multiply(self, num):
        ans = [(Decimal(num) * x) for x in self.coordinates]
        return Vector(ans)

    def magnitude(self):
        sumsqr = sum([x*x for x in self.coordinates])
        mag = math.sqrt(sumsqr)
        return mag

    def normalize(self):
        try:
            mag = self.magnitude()
            return self.scalar_multiply(Decimal(1./mag))
        except ZeroDivisionError:
            raise Exception("Can not normalize zero vector!")

    def dot_product(self, other):
        prod = [i*j for i, j in zip(self.coordinates, other.coordinates)]
        return sum(prod)

    def calc_angle(self, other, in_degree=False):
        v1_mag = self.magnitude()
        v2_mag = other.magnitude()
        dot_prod = self.dot_product(other)
        denom = v1_mag * v2_mag
        value = 0 if denom == 0 else (Decimal(dot_prod / Decimal(denom)))
        radian = math.acos(value)
        degree = (radian * 180) / math.pi
        return degree if in_degree else radian

    def is_parallel(self, other):
        if self.is_zero_vector() or other.is_zero_vector():
            return True

        relation = [x/y for x, y in zip(self.coordinates, other.coordinates) if y != 0]
        if len(relation) == len(self.coordinates):
            return all([round(x, 3) == round(relation[0], 3) for x in relation])

        return False

    def is_zero_vector(self):
        return all([round(x, 3) == 0 for x in self.coordinates])

    def is_orthogonal(self, other):
        if self.is_zero_vector() or other.is_zero_vector():
            return True
        return round(self.dot_product(other), 3) == 0

    def projection(self, b):
        norm_b = b.normalize()
        c = self.dot_product(norm_b)
        ans = norm_b.scalar_multiply(c)
        return ans

    def perpendicular(self, b):
        v_proj = self.projection(b)
        ans = self - v_proj
        return ans

    def cross_product(self, v):
       if (len(self.coordinates) == 3) and (len(v.coordinates) == 3):
           a1, a2, a3 = self.coordinates
           b1, b2, b3 = v.coordinates
           return Vector([
               a2 * b3 - a3 * b2,
               a3 * b1 - a1 * b3,
               a1 * b2 - a2 * b1
           ])
       else:
           print("invalid vectors for cross product found!")


    def area_parallelogram(self, v):
        w = self.cross_product(v)
        return w.magnitude()


    def area_triangle(self, v):
        area = self.area_parallelogram(v)
        return area * 0.5


