while(True):
    n = int(input("Height: "))
    if(n >= 1 and n <= 8):
        break
    else:
        continue

for i in range(n):
    for j in range(n-(i+1)):
        print(" ", end='')
    for q in range(i+1):
        print("#", end='')
    print()
