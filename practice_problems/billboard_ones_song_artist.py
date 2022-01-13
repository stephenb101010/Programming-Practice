with open("billboard100_2000.csv") as file:
    number_ones = {}
    for line in file:
        line = line.strip("\n")
        line = line.split(",")
        if line[0] == "rank":
            continue
        if line[0] == "1":
            number_ones[line[1]] = line[2]
    print("These were the number one songs of 2000:")
    for key in number_ones:        
        print(f'"{key}" - {number_ones[key]}')