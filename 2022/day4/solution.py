import csv

pairs_fully_contained = 0
pairs_with_overlaps = 0

with open('input.txt', 'r') as input_file:
    csv_reader = csv.reader(input_file)

    for elf1, elf2 in csv_reader:
        elf1_assignments = [int(number) for number in elf1.split('-')]
        elf2_assignments = [int(number) for number in elf2.split('-')]

        # Part 1
        pairs_fully_contained += (1 if elf1_assignments[0] <= elf2_assignments[0] and elf1_assignments[1] >= elf2_assignments[1]
                             else 1 if elf2_assignments[0] <= elf1_assignments[0] and elf2_assignments[1] >= elf1_assignments[1]
                             else 0)

        # Part 2
        pairs_with_overlaps += (1 if elf1_assignments[0] >= elf2_assignments[0] and elf1_assignments[0] <= elf2_assignments[0]
                           else 1 if elf1_assignments[1] >= elf2_assignments[0] and elf1_assignments[1] <= elf2_assignments[1]
                           else 1 if elf2_assignments[0] >= elf1_assignments[0] and elf2_assignments[0] <= elf1_assignments[1]
                           else 1 if elf2_assignments[1] >= elf1_assignments[0] and elf2_assignments[1] <= elf1_assignments[1]
                           else 0)
    
    print(pairs_fully_contained)
    print(pairs_with_overlaps)