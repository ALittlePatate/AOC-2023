f = open("input.txt", "r")

tot = 0
for line in f.readlines() :
    temp = 0
    for c in line :
        if c.isdigit() :
            temp = int(c) * 10
            for d in line[::-1] :
                if d.isdigit() :
                    temp += int(d)
                    break
            break
    tot += temp
print(tot)
f.close()