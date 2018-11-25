class LessThanOne(Exception):
    pass

def sieve(n):
    mylist = list(range(2,n+1))
    for i in range(0,len(mylist)):
        for j in mylist[i+1:]:
            if j%mylist[i] == 0:
                popping = mylist.index(j)
                mylist.pop(popping)
    print(mylist)
    print(len(mylist))
def main():
    try:
        number = int(input('Enter a number greater than 1: '))
        if number < 2:
            raise LessThanOne
        sieve(number)
        
    except ValueError:
        print('A number Please!!')
        main()
    except LessThanOne:
        print('A number greater than 1 please!')
        main()

if __name__ == '__main__':
    main()