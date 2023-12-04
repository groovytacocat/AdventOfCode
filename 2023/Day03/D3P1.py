matrix = []

f = open('input.txt')
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
    val = 0
    if not matrix[rownum][symind].isdecimal():
        lnum = numBuild(symind, rownum, 'l')
        if lnum:
            print(f'Left built: {lnum}')
            val += int(lnum)
        rnum = numBuild(symind, rownum, 'r')
        if rnum:
            print(f'Right built: {rnum}')
            val += int(rnum)
    else:
        num = numBuild(symind,rownum,'l') + matrix[rownum][symind] + numBuild(symind, rownum, 'r')
        if num:
            print(f'Middle built: {num}')
        val += int(num)
    return val

ans = 0
for i in range(1, len(matrix)-1):
    for j in range(len(matrix[i])):
        if not matrix[i][j].isalnum() and not matrix[i][j] == '.':
            above = matrix[i-1][j-3:j+4]
            current = matrix[i][j-3:j+4]
            below = matrix[i+1][j-3:j+4]
            print(f'Matrix is:\n{above}\n{current}\n{below}')
            for val in range(i-1, i+2):
                ans += newCheck(val, j)
            print()
    print()
print(f'No shot?: {ans}')
