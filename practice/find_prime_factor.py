def find_prime_factor(num):
    factors = []
    divisor = 2

    while (divisor <= num):
        if (num % divisor) == 0:
            factors.append(divisor)
            num = (num/divisor)
        else:
            divisor += 1
    print(factors)

    

find_prime_factor(630)
