#6
d = open('notes.txt','r')
l = d.readlines()
string = l[0]
stringsplit = string.split()
print(stringsplit)
d = []
for i in stringsplit:
    d.append(len(i))
    e = max(d)
for j in stringsplit:
    if len(j) == e:
        print(j)