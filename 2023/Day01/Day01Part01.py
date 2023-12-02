import re

f = open('input.txt')

sum = 0

for line in f:
    line = re.sub("[a-zA-Z]", "", line)

    num = int(line[0]) * 10 + int(line[-2])
    
    sum += num

print(f'Sum of all calibration numbers is: {sum}')

f.close()
