import sys
from io import StringIO

def mapper():
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 6:
            continue
        data, time, store, item, cost, payment = data
        print("%s\t%s" % (store, cost))

test_text = """2013-10-09\t13:22\tMiami\tBoots\t99.95\tVisa
2013-10-09\t13:22\tNew York\tDVD\t9.50\tMasterCard
2013-10-09 13:22:59 I/O Error
^d8x28orz28zoijzu1z1zp1OHH3du3ixwcz114<f
1\t2\t3"""

def main():
    sys.stdin = StringIO(test_text)
    mapper()
    sys.stdin = sys.__stdin__

if __name__ == '__main__':
    main()