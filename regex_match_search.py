import re

#* match checks for a match only at the beginning of the string, while search checks for a match anywhere in the string

line = "Cats are smarter than dogs"

matchObj = re.match(r'dogs', line, re.M|re.I)
searchObj = re.search(r'dogs', line, re.M|re.I)

if matchObj:
    print("matchObj", matchObj.group())
else:
    print("no match")
if searchObj:
    print("searchObj", searchObj.group())
else:
    print("no match")
