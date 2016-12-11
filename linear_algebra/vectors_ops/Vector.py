class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
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
        ans = [(num * x) for x in self.coordinates]
        return Vector(ans)


def main():
    v1 = Vector([8.218, -9.341])
    v2 = Vector([-1.129, 2.111])
    v3 = v2 + v1
    print(v3)

    v1 = Vector([7.119, 8.215])
    v2 = Vector([-8.223, 0.878 ])
    v3 = v1 - v2
    print(v3)

    v1 = Vector([ 1.671, -1.012, -0.318])
    v2 = v1.scalar_multiply(7.41)
    print(v2)

if __name__ == '__main__':
    main()