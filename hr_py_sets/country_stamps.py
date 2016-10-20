# https://www.hackerrank.com/challenges/py-set-add

def main():
   n = int(input().strip())
   country_names = set()
   for i in range(n):
       country_names.add(input().strip())

   print(len(country_names))



if __name__ == '__main__':
    main()