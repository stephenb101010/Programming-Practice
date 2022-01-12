def get_years(team: str):
    with open("nba_finals.csv") as file:
        finals_details = {}
        for line in file:
            line = line.strip("\n")
            parts = line.split(",")
            if parts[0] == "Year":
                continue
            finals_details[parts[0]] = parts[1]
    champ_years = []
    for entry in finals_details:
        if finals_details[entry] == team: #This is not working. If I use "Miami Heat" instead of team, it works.
            champ_years.append(entry)

print(get_years("Miami Heat"))