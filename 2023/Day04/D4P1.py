f = open('input.txt')
grid = []
for line in f:
	line = line[line.index(':')+1:-1]
	grid.append(line)
f.close()

ans = 0

for rows in grid:
	nums = rows.split('|')
	wins = nums[0].split()
	mine = nums[1].split()
	winCount = 0
	pts = 0

	for vals in mine:
		if vals in wins:
			winCount += 1
	if winCount > 0:
		pts = 2 ** (winCount - 1)
	else:
		pts = 0
	ans += pts

print(ans)
