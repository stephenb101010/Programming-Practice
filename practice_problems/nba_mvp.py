with open("nba_finals.csv") as file:
    mvp_list = []
    for line in file:
        line = line.strip("\n")
        parts = line.split(",")
        if parts[0] == "Year":
            continue
        if (parts[4] != ''):
            mvp_list.append(parts[4])
    times_won = []
    total = set()
    for name in mvp_list:
        if mvp_list.count(name) > 1:
            times_won.append(name)
            total.add(mvp_list.count(name))
    tot_list =  list(total)
    tot_list.sort(reverse= True)
    for num in tot_list:
        names = set()
        for name in mvp_list:
            if num == mvp_list.count(name):
                names.add(name)
        print(f"{num} times: {names}")