def fact(primelist,n):
    result = 0
    for i in primelist:
        if n%i != 0:
            result = 1
            continue
            
        else:
            result = 0
            break
    return result
    
def factors(n):
    prime_list = [2]
    factor_list = [1,n]
    for i in range(3,n,2):
        if fact(prime_list,i) == 1:
            prime_list.append(i)
        else:
            continue
    for i in prime_list:
        if n%i == 0:
            factor_list.append(i)
    
    factor_list = set(factor_list)
    factor_list = list(factor_list)
    factor_list.sort()
    print(factor_list)
    print(prime_list)
    print(len(prime_list))
num = 0
while not num:
    try:
        num = int(input('Enter the number you want to find factors of: '))
    except:
        print('Please enter a number')
factors(num)