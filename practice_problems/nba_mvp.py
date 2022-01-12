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
    name_list = []
    for mvp in mvp_list:
        if mvp_list.count(mvp) > 1:
            multi_mvp[mvp_list.count(mvp)] = [name_list.append(mvp)] #Not adding names. Why?
print(multi_mvp)