while True:
    population = int(input("Start size: "))

    if population < 9:
        continue
    else:
        break

while True:
    final = int(input("End size: "))

    if final < population:
        continue
    else:
        break

years = 0
while population < final:
    population += (population/3 - population/4)
    years += 1

print(f'Years: {years - 1}')