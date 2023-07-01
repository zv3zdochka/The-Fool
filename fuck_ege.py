
for i in range(100, 996):
    flag = False
    a = []
    sum = 0
    a.append(i)
    a.append(i+1)
    a.append(i+2)
    a.append(i+3)
    for i in a:
        if str(i)[1] == "0":
            flag = True
    if flag:
        continue
    for i in a:
        sum += (i / int(str(i)[1]))

    if sum == 2300.5:
        print(a)