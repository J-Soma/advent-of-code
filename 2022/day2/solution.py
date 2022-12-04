with open('input.txt', 'r') as input_file:
    total_score_part1 = 0
    total_score_part2 = 0

    for line in input_file:
        line = line.replace('\n', '')

        if (len(line) == 3):
            opponent = ord(line[0]) % 64
            response = (ord(line[2]) - 88 + 65) % 64

            # Part 1
            total_score_part1 += response 

            if (opponent == response):
                total_score_part1 += 3
            else:
                total_score_part1 += (6 if opponent == 1 and response == 2
                                 else 6 if opponent == 2 and response == 3 
                                 else 6 if opponent == 3 and response == 1
                                 else 0)

            # Part 2
            if (response == 1):# Loss
                total_score_part2 += (3 if opponent == 1
                                 else 2 if opponent == 3
                                 else 1)
            elif (response == 2):# Draw
                total_score_part2 += 3 + opponent
            else:# Win
                total_score_part2 += 6 + (1 if opponent == 3
                                     else 2 if opponent == 1
                                     else 3)

    print(total_score_part1)
    print(total_score_part2)