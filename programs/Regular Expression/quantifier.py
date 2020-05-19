import re

#macher = re.finditer('a*','abaabaaab')
macher = re.finditer('a?','abaabaaab')

for m in macher:
    print(m.start(),'----',m.group())
