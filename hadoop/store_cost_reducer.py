import sys

def reducer():
    sales_total = 0
    oldkey = None

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        thiskey, thissale = data

        if oldkey and oldkey != thiskey:
            print ("%s\t%s" % (oldkey, sales_total))
            sales_total = 0
        oldkey = thiskey
        sales_total += float(thissale)

    if oldkey != None:
        print ("%s\t%s" % (oldkey, sales_total))

def main():
    reducer()

if __name__ == '__main__':
    main()