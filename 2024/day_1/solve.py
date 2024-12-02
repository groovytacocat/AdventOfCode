f = open('input.txt')

left_ids = []
right_ids = []

part_1 = 0
for line in f:
    vals = line.strip().split()
    left_ids.append(int(vals[0]))
    right_ids.append(int(vals[1]))

f.close()

left_ids.sort()
right_ids.sort()

part_1 = 0
for i in range(0, len(left_ids)):
    part_1 += abs(left_ids[i] - right_ids[i])

print(f'Answer for Part 1 is: {part_1}')

part_2 = 0
for i in range(0, len(left_ids)):
    part_2 += left_ids[i] * right_ids.count(left_ids[i])

print(f'Answer for Part 2 is: {part_2}')
