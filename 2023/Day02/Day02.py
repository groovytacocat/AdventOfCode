import re

f = open('dice.txt')

ans = 0

powersum = 0

for line in f:
    gamenum = int(re.search('\d+', line).group())

    reds = re.findall('\d+ red', line)
    greens = re.findall('\d+ green', line)
    blues = re.findall('\d+ blue', line)

    redlist = []
    greenlist = []
    bluelist = []

    for r in reds:
        redlist.append(int(re.search('\d+', r).group()))
    for g in greens:
        greenlist.append(int(re.search('\d+', g).group()))
    for b in blues:
        bluelist.append(int(re.search('\d+',b).group()))

    powersum += (max(redlist) * max(bluelist) * max(greenlist))

    if max(redlist) <= 12 and max(greenlist) <= 13 and max(bluelist) <= 14:
        ans += gamenum

print(f'game sum is: {ans} || power sum is: {powersum}')
