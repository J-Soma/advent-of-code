with open('input.txt', 'r') as input_file:
    
    priorities = 0
    group_priorities = 0
    group = []

    for index, line in enumerate(input_file):
        line = line.replace('\n','')

        if (len(line) != 0):
            first_compartment = line[:round(len(line) / 2)]
            second_compartment = line[len(first_compartment):]

            item = set(first_compartment).intersection(set(second_compartment)).pop()
            priorities += ord(item) - (96 if item.islower() else 64 -26)

            group.append(line)

            if (len(group) == 3):
                badge = set(group[0]).intersection(set(group[1])).intersection(set(group[2])).pop()
                group_priorities += ord(badge) - (96 if badge.islower() else 64 -26)

                group.clear()

    print(priorities)
    print(group_priorities)