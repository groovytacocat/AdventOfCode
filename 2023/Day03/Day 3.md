# Day 3

## --- Day 3: Gear Ratios ---

### --- Part One ---
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

```
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
```

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

### My Thoughts

So this was probably the hardest problem I've solved to date. Even now as I was writing this I discovered that I had pushed the wrong versions of my answers to here and deleted the slightly more polished versions and had to go back and work my way back just slightly

Took me slightly over 24 hours to finish (I think I submitted the answer to earn the 2nd start ~12:28am on Day 4). Conceptually it seemed easy, just go through each line when you find a symbol (as defined by the problem) look around it to see if any numbers are bordering it, then add any numbers you find

In practice it was an order of magnitude more complex than I realized. Once I got the basics out of the way and created my matrix, I was able to identify locations of the symbols and even create slices to print and help me visualize the corresponding sub-matrix.
The very first solution I had that did anything besides print the matrices was ~100+ lines long and was a giant mess of chaining if-elses that themselves had nested if-elses and loops. Next attempt involved what I thought was clever slicing/checking through the submatrix for any numbers and I thought it was great until I realized: I was only getting 3 digit numbers!

I spoke with a friend about this and he told me his solution (which I still can't figure out even in my head), which further bolstered my stubborness to make the matrix work

Finally I accepted that I wasn't going to get out of bounds-checking and that a while loop would not be particularly optimal or \~elite\~ but simplest. This allowed for me to capture any/all numbers adjacent to the symbol regardless of length, position, and would even catch numbers in the same row

```python
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
        if not matrix[i][j].isalnum() and not matrix[i][j] == '.':
            for val in range(i-1, i+2):
                ans += numCheck(val, j)
print(f'No shot?: {ans}')
```


### --- Part Two ---

The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

```
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
```
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?

### My Thoughts

Part 2 was not the beast that Part 1 proved to be. I think I honestly spent more time adding print statements of values and submatrices and then going through almost every single one trying to figure out where my numbers weren't getting pulled correctly before realizing that I submitted a typo instead of copy/pasting the output (insert any rendition of a meme/emoji where someone is smiling on the outside but crying/dead on the inside)

The non-human input error portion of Part 2 I struggled with and I'm sure there's a much cleaner way of doing was just creating the list of gear ratios as I wasn't (and still aren't fully) comfortable/proficient with lists and indexing them in Python.

Nevertheless persistence (that's my resume-talk way of saying bruteforce) was the hero of Day 3. I'd like to think I learned a lot from this and will use that going forward.

(Pro tip for anyone reading this: Make Methods!! When I have done exercises in C# or C for coursework or other personal projects one of the first things I do is try to abstract everything into various methods/functions however that has definitely not been my standard MO for python, but it was very helpful for this one when creating numBuild and numCheck!)



```python
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
```
