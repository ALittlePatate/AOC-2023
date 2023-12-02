import math

f = open("input", "r")
CUBES = {"red": 0, "green": 0, "blue": 0}
tot = 0
for line in f.readlines() :
    curr_id = int(line.split(':')[0][5:])
    l = line.split(f"Game {curr_id}:")[1]
    sets = l.split(';')
    for s in sets :
        vals = s.split(',')
        for c in vals :
            c  = c[1:].replace('\n', '')
            if int(c.split(' ')[0]) > CUBES[c.split(' ')[1]] :
                CUBES[c.split(' ')[1]] = int(c.split(' ')[0])
    tot += math.prod(dict.values(CUBES))
    CUBES = dict.fromkeys(CUBES, 0)
print(tot)
