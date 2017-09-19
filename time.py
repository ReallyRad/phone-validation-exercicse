import re
pattern = """\(0                   #open bracket followed by a zero
                                     #then either:
               (
                   1                 #1
                                     #followed by either:
                   (
                       \d{3}         #3 digits
                       \)            #close bracket
                       \s            #single space
                       \d{6}         #6 digits
                   |                 #or
                       (
                           \d1       #a single digit followed by a 1
                       |             #or
                           1\d       #a 1 followed by a single digit
                       )
                       \)            #a close bracket
                       \s            #a single space
                       \d{3}         #3 digits
                       \s            #a single space
                       \d{4}         #4 digits
                   )
               |                     #or
                   2\d\)             #2 followed by a digit and a close bracket
                   \s                #a single space
                   \d{4}             #4 digits
                   \s                #a single space
                   \d{4}             #4 digits
               )$"""

file = open("phone list.txt")
list = file.read()
lines = list.splitlines(True)

#finds = re.findall(pattern, list)

for line in lines:
    #replace \n by )\n
    pattern = r'\n'
    correct_line = re.sub(pattern,')\n',line)

    #replace - in number by )(
    pattern = r'\d+-.*\n$'
    match = re.search(pattern,correct_line)
    correct_line = re.sub('-', ')(', match.group())

    #replace space before phone number by space and (
    correct_line = '(' + correct_line

    print(correct_line)
