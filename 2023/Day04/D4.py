f = open('scratchers.txt')
windict = {}
total = {}
cardPoints = 0
grandtotal = 0
for line in f:
    line = line[line.index('d')+1:-1]
    cardNum = line[:line.index(':')].strip()
    nums = line[line.index(':') + 1:].split('|')
    wins = nums[0].strip().split()
    picks = nums[1].strip().split()
    winCount = 0
    for vals in picks:
        if vals in wins:
            winCount += 1
    if winCount > 0:
        cardPoints += 2 ** (winCount - 1)
    windict[int(cardNum)] = winCount
    total[int(cardNum)] = 1
f.close()
for i in total:
    for j in range(i+1, i+1+windict[i]):
        total[j] += total[i]
    grandtotal += total[i]
print(f'Total Points: {cardPoints} | Total Cards: {grandtotal}')
