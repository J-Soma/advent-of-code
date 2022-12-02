with open('input.txt', 'r') as input_file:
    food_calories_by_elf = []
    i = 0

    for line in input_file:
        line = line.replace('\n', '')

        if (len(line) == 0):
            i += 1
        else:
            if (len(food_calories_by_elf) != i + 1):
                food_calories_by_elf.append(int(line))
            else:
                food_calories_by_elf[i] += (int(line))

    food_calories_by_elf.sort(reverse=True)

    print(food_calories_by_elf[0]) #Part 1
    print(sum(food_calories_by_elf[:3])) #Part 2