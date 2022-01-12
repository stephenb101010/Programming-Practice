def get_winner(year: int):
    with open("nba_finals.csv") as file:
        finals_details = {}
        for line in file:
            line = line.strip("\n")
            parts = line.split(",") #Apparently a comma is different from an apostrophe.
            if parts[0] == "Year":
                continue
            finals_details[int(parts[0])] = parts[1]
    return finals_details.get(year)

year = int(input("Year: "))
print(get_winner(year))