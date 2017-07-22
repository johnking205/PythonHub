#Project Euler Problem 1
#Script that calculates the sum of
#all multiples of 3 and 5 below 1000

#Given upper limit, summate multiples of 3 and 5 below that limit
def Multiples3and5(limit):
    sum = 0
    for i in range(limit):
        if not (i % 3) or not (i % 5):
            sum += i
    return sum

print(Multiples3and5(1000))