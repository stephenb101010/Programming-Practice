with open("sowpods.txt") as file:
    divided_pairs = set()
    for line in file:
        line = line.strip("\n")
        ending = len(line) - 1
        i = 0
        while (i + 2) < len(line):
            if line[i] == line[i + 1]:
                divided_pairs.add(line[i:(i+2)])
            i +=1
    print(divided_pairs)
    doubled = {'AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ', 'KK', 'LL', 'MM', 'NN', 'OO', 'PP', 'QQ', 'RR', 'SS', 'TT', 'UU', 'VV', 'WW', 'XX', 'YY', 'ZZ'}
    divided_pairs.symmetric_difference_update(doubled)
print(divided_pairs)