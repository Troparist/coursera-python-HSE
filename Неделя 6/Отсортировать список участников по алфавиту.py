inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
new = []
for line in inFile:
    new += [line.split()]
new.sort()
for i in range(len(new)):
    print(new[i][0], new[i][1], new[i][3], file=outFile)
inFile.close()
outFile.close()
