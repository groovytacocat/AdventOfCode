# Day 1

## **Day 1: Trebuchet?!**

### --- Part One ---

Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

>1abc2
>
>pqr3stu8vwx
>
>a1b2c3d4e5f
>
>treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

[Here is a link to the actual .py file to run yourself](./Day01/Day01Part01.py)

This was relatively simple especially with using RegEx, just read each line from the file and use `re.sub` to remove all non-numeric values, then calculate that line's calibration number and adding it to the running total. (Using line[-2] since line[-1] is the newline character)

My initial solution was a mix of C and awk where I read each line of input and printed out only numbers delimited by spaces to a file and had awk read the file to create the correct calibration numbers and sum them, but I was given advice that it's generally best to solve each day's problem in 1 language if possible

```python
import re
f = open('input.txt')
sum = 0
for line in f:
    line = re.sub("[a-zA-Z]", "", line)
    num = int(line[0]) * 10 + int(line[-2]) 
    sum += num
print(f'Sum of all calibration numbers is: {sum}')
f.close()
```



### --- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

>two1nine
>
>eightwothree
>
>abcone2threexyz
>
>xtwone3four
>
>4nineeightseven2
>
>zoneight234
>
>7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?

[As before here is a link to my actual .py file](./Day01/Day01Part02.py)

This portion proved to be a more significant challenge for me especially since before today I've never done more than print Hello World/FizzBuzz with Python

My initial attempt was to read each line then iterate through my dictionary while making use of `string.replace()` to make the relevant substitutions

This proved ineffective as strings like 'eightwone' should parse to '821', so my next attempt was to iterate through the line character-by-character and if the character was a number adding a tuple of (index, value) to a list, then iterate through the dictionary using `string.find()` and in similar fashion add to a list a tuple containing the index the numberstring was found and the value

Then I would sort the list and perform the same math as in Part 1, this failed as a result of `string.find()` returning the **first** instance and never checking again so strings like 'eight512asdfabconeonethreeight' would add the tuple (0, 8). 

Thankfully a friend/mentor gave me a small piece of advice! Armed with that tidbit I finally realized a couple things:
  
  1) I could use a LIFO (Last In First Out) collection like a Stack instead of holding every instance of a number in a list as a tuple with its index then sort
  2) To solve the issue of repeated numberstring values in input, I could create a substring starting at a given position in the string and iterate through the dictionary and when  `string.find() == 0` I could add that numberstring value to my stack then move to the last character of that and continue checking the line

Resulting in the below: Personally I'm not a fan of all the nested if-else and the extra for loop but I'm attempting to solve these 

```python
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
```
