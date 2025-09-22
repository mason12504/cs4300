# task 3
# Mason Andersen
# CS 4300

# Control structures

# if statement to check positive, negative, or zero
def pnz(n):
    if n > 0:
        result = "+"
    elif n < 0:
        result = "-"
    elif n == 0:
        result = "0"
    # just in case it's a string or something 
    else:
        result = None 

    return result 

# print the first 10 prime numbers 
def printPrimes():
    resultList = []
    n = 1
    for i in range(10):
        n = nextPrime(n)
        print(n)
        resultList.append(n)
    return(resultList)

# kind of janky but wanted to practice solving this on my own rather than using an existing solution
def nextPrime(n):
    
    loopCond = True
    
    # 2 is the first prime and all primes are positive
    if n < 2:
        return 2
    
    else:
        # we need the Next Prime: so if n is already prime we gotta add 1 or we'll just return n
        n = n + 1
        # test every number division to make sure there are no divisors of n
        while (loopCond == True):
            divisors = 0 
            for i in range(2, n+1):
                if(n % i) == 0: 
                    divisors = divisors + 1
                if divisors > 1:
                    break # no sense in continuing checking
            # if prime, return value, break loop
            if divisors == 1:
                result = n 
                loopCond = False
            # if not prime, try next 
            else:
                n = n + 1
    # return the next prime after n
    return result 

# calculate the sum of all numbers 1 through 100 
def sum100():
    i = 1
    total = 0 
    while (i <= 100):
        total = total + i 
        i = i + 1
    return total
