a=[96,118,108,25,110,112,119,21,25,122,118,119,126,107,120,109,106,24]
d=[13,15,10,8,14,9,11,10,93,9,93,12,12,88,23,73,81,73]
b=""
for c in d:
    b += str(chr(c^57))
    print(b)

print(b)
