with open("countries.txt") as file:
    shortest = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    results = []
    for line in file:
        line = line.strip("\n")
        if len(line) <= len(shortest):
            shortest = line
            results.append(line)
    results.sort(key = len)
    shortest = results[0]
    length = len(shortest)
    final_list = []
    for name in results:
        if len(name) <= length:
            final_list.append(name)
print(final_list)