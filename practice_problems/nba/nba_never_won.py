with open("nba_finals.csv") as file:
    winners = set()
    losers = set()
    for line in file:
        line = line.strip("\n")
        parts = line.split(",")
        if parts[0] == "Year":
            continue
        winners.add(parts[1])
        losers.add(parts[2])
    for team in winners:
        if team in losers:
            losers.discard(team)
    print(losers)