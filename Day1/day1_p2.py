f = open("input.txt", "r")
possible_digits = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def find_num(line, rev) :
    temp = 0
    temp_2 = 0
    idx_2 = 99999
    idx = 0
    for digit, num in possible_digits.items() :
        if rev : idx_tmp = line.find(digit[::-1])
        else : idx_tmp = line.find(digit)
        if idx_tmp == -1 : continue
        if idx_tmp < idx_2 :
            idx_2 = idx_tmp
            temp_2 = int(num) * 10
    for c in line :
        if c.isdigit() and temp == 0:
            temp = int(c) * 10
            idx = line.find(str(c))
    if idx_2 < idx : temp = temp_2
    return temp
    
tot = 0
for line in f.readlines() :
    tot += find_num(line, 0)
    tot += int(find_num(line[::-1], 1) / 10)
    
print(tot)
f.close()