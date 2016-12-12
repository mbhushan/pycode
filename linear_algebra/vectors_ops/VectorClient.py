from linear_algebra.vectors_ops.Vector import Vector


def quiz4():
    v1 = Vector([-7.579, -7.88])
    v2 = Vector([22.737, 23.64])
    print("is parallel: %s" % (v1.is_parallel(v2)) )
    print("is orthogonal: %s" % (v1.is_orthogonal(v2)) )

    v1 = Vector([-2.029, 9.97, 4.172])
    v2 = Vector([-9.231, -6.639, -7.245])
    print("is parallel: %s" % (v1.is_parallel(v2)) )
    print("is orthogonal: %s" % (v1.is_orthogonal(v2)) )

    v1 = Vector([-2.328, -7.284, -1.214])
    v2 = Vector([-1.821, 1.072, -2.94])
    print("is parallel: %s" % (v1.is_parallel(v2)) )
    print("is orthogonal: %s" % (v1.is_orthogonal(v2)) )

    v1 = Vector([2.118, 4.827])
    v2 = Vector([0, 0])
    print("is parallel: %s" % (v1.is_parallel(v2)))
    print("is orthogonal: %s" % (v1.is_orthogonal(v2)))

def quiz3():
    v1 = Vector([7.887, 4.138])
    v2 = Vector([-8.802, 6.776])
    print("dot product: %s" % (v1.dot_product(v2)))

    v1 = Vector([-5.955, -4.904, -1.874])
    v2 = Vector([-4.496, -8.755, 7.103])
    print("dot product: %s" % (v1.dot_product(v2)))

    v1 = Vector([3.183, -7.627])
    v2 = Vector([-2.668, 5.319])
    print("angle in radian: %s" % (v1.calc_angle(v2)))

    v1 = Vector([7.35, 0.221, 5.188])
    v2 = Vector([2.751, 8.259, 3.985])
    print("angle in degrees: %s" % (v1.calc_angle(v2, True)))


def quiz2():
    v1 = Vector([-0.221, 7.437])
    v2 = Vector([8.813, -1.331, -6.247])

    print(v1.magnitude())
    print(v2.magnitude())

    v1 = Vector([5.581, -2.136])
    v2 = Vector([1.996, 3.108, -4.554])
    print(v1.normalize())
    print(v2.normalize())
    # Vector: (0.9339352140866403, -0.35744232526233)
    # Vector: (0.3404012959433014, 0.5300437012984873, -0.7766470449528028)


def quiz1():
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

def main():
    quiz4()
    quiz3()
    quiz2()
    quiz1()


if __name__ == '__main__':
    main()

