#Proejct Euler 2

#return array of fibonacci sequence up to limit
def FibonacciSeq(Limit):
    prevTerm = 1
    prevPrevTerm = 0
    fibo = []
    term = 0

    while term < Limit:
        term = prevTerm + prevPrevTerm
        fibo.append(term)

        prevPrevTerm = prevTerm
        prevTerm = term

    return(fibo)

#summate even numbers in input array
def sumEven(inputArray):
    sum = 0
    for i in inputArray:
        if not (i%2):
            sum += i
    return(sum)

#print sum of even numbers from fibonacci sequence up to 4000000
print(sumEven(FibonacciSeq(4000000)))
