with open("nba_finals.csv") as file:
    mvp_list = []
    for line in file:
        line = line.strip("\n")
        parts = line.split(",")
        if parts[0] == "Year":
            continue
        if (parts[4] != ''):
            mvp_list.append(parts[4])
    multi_mvp = {}
    for mvp in mvp_list:
        if mvp_list.count(mvp) > 1:
            multi_mvp[mvp] = mvp_list.count(mvp)
    times_won = multi_mvp.items()
    print(times_won)
#Get values, sort, remove dupes. Get key for each value and print.