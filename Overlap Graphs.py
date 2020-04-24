# Declare our variables for the function.

rosalindlist = []
stringlist = []

prefix = []
suffix = []

counter = 0
counter2 = 0
counter3 = 0

# Grab the Rosalind names.

f = open("rosalind_grph.txt", "r")

temp = ''

for line in f:
    line = line.rstrip()
    if line[0] == '>':
        c = line.replace('>', '')
        rosalindlist.append(c)
        if temp != '':
            stringlist.append(temp)
            temp = ''
    else:
        line.replace(' ', '').replace('\t', '').replace('\n', '')
        temp += line

stringlist.append(temp)

# Do the business...

#print (stringlist)

while counter < len(stringlist):
    suffix.insert(counter, stringlist[counter][-3:])
    prefix.insert(counter, stringlist[counter][0:3])
    counter += 1

while counter2 < len(stringlist):
    if counter3 == len(stringlist):
        counter3 = 0
    #for i in range (0, len(prefix)):
    while counter3 < len(stringlist):
        if suffix[counter2] == prefix[counter3] and stringlist [counter2] != stringlist [counter3]:
            print (rosalindlist[counter2], rosalindlist[counter3])
        counter3 +=1
    counter2 += 1
