f = open('seeds.txt')

seedList = []
mapvals = []
for line in f:
    if line.startswith('seeds'):
        seedList = list(map(int, line[line.index(':') + 1:].strip().split()))
    elif len(line) == 1:
        mapvals.append('----')
    elif line[0].isdigit():
        nums = list(map(int, line.strip().split()))
        mapvals.append(nums)
f.close()

mapvals.append('----')

interval = []

def seedCheck(seed):
    for i in range(len(interval)):
        if seed >= interval[i][1] and seed < interval[i][1] + interval[i][2]:
            return seed + (interval[i][0] - interval[i][1])
    return seed
def convertSeed(vals):
    for i in range(len(vals)):
        convseed = seedCheck(vals[i])
        vals[i] = convseed

def seedmap(dest, src, rng):
    interval.append([dest, src, rng])
for i in range(1, len(mapvals)):
    if not mapvals[i] =='----':
        seedmap(mapvals[i][0], mapvals[i][1], mapvals[i][2])
    else:
        convertSeed(seedList)
        interval.clear()
print(f'Now that every thing is done:\n {min(seedList)}')
