from collections import deque

mydict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

f = open('input.txt')

ans = 0

for line in f:
    mystack = deque()
    
    for i in range(0, len(line)):
        if line[i].isdigit():
            if len(mystack) < 2:
                mystack.append(int(line[i]))
            else:
                mystack.pop()
                mystack.append(int(line[i]))
        else:
            substr = line[i:]
            for key in mydict:
                    if substr.find(key) == 0:
                        if len(mystack) < 2:
                            mystack.append(mydict[key])
                        else:
                            mystack.pop()
                            mystack.append(mydict[key])
                        i = len(key) - 2
    
    num = mystack[0] * 10 + mystack[-1]

    ans += num

print(f'Sum of all calibration numbers is: {ans}')


f.close()
