from collections import Counter

inp_str = "GeeksforGeeks"

out = {x : inp_str.count(x) for x in set(inp_str )}
oup = Counter(inp_str)
freq = {}
for ele in inp_str:
    if ele in freq:
        freq[ele] += 1
    else:
        freq[ele] = 1
print ("Occurrence of all characters in GeeksforGeeks is :\n "+ str(out))
print ("Occurrence of all characters in GeeksforGeeks is :\n "+ str(oup))
print ("Occurrence of all characters in GeeksforGeeks is :\n "+ str(freq))

print(out.items())
print(max(out.items(), key = lambda x: x[1]))
print(max(out.values()))
print(oup.values())
print(freq.values())
