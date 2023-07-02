
def calculate_quarters(n, coins):
    while n > 25:
        n -= 25
        coins += 1
    return n, coins
        
def calculate_dimes(n, coins):
    while n > 10:
        n -= 10
        coins += 1
    return n, coins

def calculate_nickels(n, coins):
    while n > 5:
        n -= 5
        coins += 1
    return n, coins

def calculate_pennies(n, coins):
    while n > 0:
        n -= 1
        coins += 1
    return n, coins
    
while(True):
    n = int(input("Change owed: "))
    if(n > 0):
        break
    else:
        continue
        
coins = 0

n, coins = calculate_quarters(n, coins)
n, coins =calculate_dimes(n, coins)
n, coins = calculate_nickels(n, coins)
n, coins = calculate_pennies(n, coins)
print(coins)


