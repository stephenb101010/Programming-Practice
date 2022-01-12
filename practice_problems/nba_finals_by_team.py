def get_years(team: str):
    finals_details = {}
    champ_years = []
    with open("nba_finals.csv") as file:
        for line in file:
            line = line.strip("\n")
            parts = line.split(",")
            if parts[0] == "Year":
                continue
            finals_details[parts[0]] = parts[1]               
    for entry in finals_details:
        if finals_details[entry] == team: 
            champ_years.append(entry)
    return champ_years

print(get_years("Miami Heat"))