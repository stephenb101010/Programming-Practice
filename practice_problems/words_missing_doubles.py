#What are all of the letters that never appear consecutively in an English word?
with open("sowpods.txt") as file:
    divided_pairs = set()
    for line in file:
        line = line.strip("\n")
        for i in range(len(line) - 2):
            if line[i] == line[i + 1]:
                divided_pairs.add(line[i:(i+2)])
    doubled = {'AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ', 'KK', 'LL', 'MM', 'NN', 'OO', 'PP', 'QQ', 'RR', 'SS', 'TT', 'UU', 'VV', 'WW', 'XX', 'YY', 'ZZ'}
    divided_pairs.symmetric_difference_update(doubled)
print(divided_pairs)