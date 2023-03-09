import math

def factor_check(number):
    count = 0
    if number < 0:
        number = -number
    
    while count < number:
        factors = []
        count += 1
        count2 = 0
        while count2 < number:
            count2 += 1
            if count2 > math.ceil(number/2):
                continue
            elif count % count2 == 0:
                factors.append(count2)
    return factors
    
def quadratic(a,b,c):
    mult = a * c
    adtn = b
    factors = factor_check(mult)
    neg_factors = []

    for num in factors:
        neg_factors.append(-1 * num)

    factors.extend(neg_factors)
    
    fact_add = 0
    fact_mult = 0
    f1 = 0
    f2 = 0
    
    for f in factors:
        for g in factors:
            fact_mult = f * g
            fact_add = f + g
            f1 = f
            f2 = g
            if fact_add == adtn and fact_mult == mult:
                break
        else:
            continue
        break

    if a > 1:
        f1 /= a
        f2 /= a
    
    print(f"The values for the unknown in the quadratic equation are {-f1} and {-f2}" )

quadratic(2,1,-528)
    