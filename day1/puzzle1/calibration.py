import re

# Open the file in read mode
def calibrate(filepath): 
    with open(filepath, 'r') as file:
        # Iterate through each line in the file
        sum = 0
        for line in file:
            #remove all non digits
            pattern = re.compile(r"[^\d]+")
            line = pattern.sub("", line)
            if (len(line) > 0):
                linesum = line[0] + line[len(line)-1]
            sum = sum + int(linesum)
    return sum

print("Day 1 Puzzle 1 answer is " + str(calibrate('day1/uncalibrated.txt')))




