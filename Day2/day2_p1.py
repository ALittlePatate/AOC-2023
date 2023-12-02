f = open("input", "r")
CUBES = {"red": 12, "green": 13, "blue": 14}
tot = 0
for line in f.readlines() :
    curr_id = int(line.split(':')[0][5:])
    l = line.split(f"Game {curr_id}:")[1]
    sets = l.split(';')
    tmp = 1
    for s in sets :
        vals = s.split(',')
        for c in vals :
            c  = c[1:].replace('\n', '')
            if int(c.split(' ')[0]) > CUBES[c.split(' ')[1]] :
                tmp = 0
    if tmp == 1 :
        tot += curr_id
print(tot)
