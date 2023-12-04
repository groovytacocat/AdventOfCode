matrix = []

f = open('sample.txt')
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
def numBuild(index, rownum, mov):
    num = ''
    if mov == 'l':
        val = index - 1
        while isValid(rownum, val) and matrix[rownum][val].isdecimal():
            num = matrix[rownum][val] + num
            val -= 1
        return num
    elif mov == 'r':
        val = index + 1
        while isValid(rownum, val) and matrix[rownum][val].isdecimal():
            num += matrix[rownum][val]
            val += 1
        return num

def newCheck(rownum, symind):
    val = []
    if not matrix[rownum][symind].isdecimal():
        lnum = numBuild(symind, rownum, 'l')
    	if lnum:
            val.append(lnum)
        rnum = numBuild(symind, rownum, 'r')
    	if rnum:
            val.append(rnum)
    else:
        num = numBuild(symind,rownum,'l') + matrix[rownum][symind] + numBuild(symind, rownum, 'r')
        if num:
            val.append(num)
    return val

ans = 0
for i in range(1, len(matrix)-1):
    for j in range(len(matrix[i])):
        if matrix[i][j].isalnum() == '*':
            gears = []
            for val in range(i-1, i+2):
                gears.append(newCheck(val, j))
            print(gears)
            print()
    print()
print(f'No shot?: {ans}')
