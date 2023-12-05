matrix = []

f = open('gears.txt')
for line in f:
    row = line[:-1]
    matrix.append(row)
f.close()

cols = len(matrix[0])
rows = len(matrix)

def isValid(x, y):
    if x >= rows or x < 0 or y >= cols or y < 0:
        return 0
    else:
        return 1
def numBuild(index, rownum, iterDirection):
    num = ''
    val = index + iterDirection
    while isValid(rownum, val) and matrix[rownum][val].isdecimal():
        if iterDirection > 0:
            num += matrix[rownum][val]
        else:
            num = matrix[rownum][val] + num
        val += iterDirection
    return num

def numCheck(rownum, symind):
    val = []
    if not matrix[rownum][symind].isdecimal():
        lnum = numBuild(symind, rownum, -1)
        if lnum:
            val.append(lnum)
        rnum = numBuild(symind, rownum, 1)
        if rnum:
            val.append(rnum)
    else:
        num = numBuild(symind,rownum,-1) + matrix[rownum][symind] + numBuild(symind, rownum, 1)
        if num:
            val.append(num)
    return val

ans = 0
for i in range(1, len(matrix)-1):
    for j in range(len(matrix[i])):
        if matrix[i][j] == '*':
            gears = []
            for val in range(i-1, i+2):
                if numCheck(val, j):
                    gears.append(numCheck(val, j))
            if len(gears) == 2:
                ans += int(gears[0][0]) * int(gears[1][0])
            elif len(gears) == 1 and len(gears[0]) == 2:
                ans += int(gears[0][0]) * int(gears[0][1])
print(f'No shot?: {ans}')
