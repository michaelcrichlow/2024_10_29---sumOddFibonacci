def sumOddFibonacci(limit):
    a, b = 0, 1
    sum_of_odds = 0

    while b <= limit:
        if b % 2 != 0:
            sum_of_odds += b
        a, b = b, a + b
    
    return sum_of_odds

print(sumOddFibonacci(10))
print(sumOddFibonacci(1000))
print(sumOddFibonacci(4000000))
