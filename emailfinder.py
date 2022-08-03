import re
hand=open('text_File_Name.txt')
for line in hand:
    line=line.rstrip()
    if re.search('^From:',line):
        print(line)
