x = int(input()) 
#checksum
def checksum(n):
    sum = 0
    i = 0
    while n !=0:
        if i % 2 != 0:
            digit = (n % 10) * 2
            if digit >= 10:
                sum += (digit // 10) + (digit % 10)
            else:
                sum += digit
        else:
            sum += n % 10
        i += 1
        n //=10
    return sum
#brand
def checkBrand(n):
    if (n >= 34 * 10 ** 13) and (n < 35 * 10 ** 13) or (n >= 37 * 10 ** 13) and (n < 38 * 10 ** 13):
        print('AMEX\n')
    elif (n >= 4 * 10 ** 12) and (n < 5 * 10 ** 12) or (n >= 4 * 10 ** 15) and (n < 5 * 10 ** 15):
        print("VISA\n")
    elif(n >= 51 * 10 ** 14) and (n < 56 * 10 ** 14):
        print("MASTERCARD\n")
    else:
        print("INVALID\n")
        

if(checksum(x) % 10 == 0):
    checkBrand(x)
else:
    print("INVALID\n")
