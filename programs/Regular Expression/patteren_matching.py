import re

count = 0
pattern = re.compile('ab')
#matcher = pattern.finditer('abaababa')
matcher = re.finditer('ab','abaababa')
matcher = re.finditer('[abc]','abaababa')
for match in matcher:
    count = count+1
    print('start:{}, end:{}, group:{}'.format(match.start(),match.end(),match.group()))
print('occurance {}'.format(count))
