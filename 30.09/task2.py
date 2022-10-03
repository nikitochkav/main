testList = [1,2,2,[3,4],(1,2,3),"1",{1,2,3}]
printSet = set()
n = []
for elem in testList:
	try:
        printSet.add(elem)
	except:
		printSet.update(elem)
		n.append(elem)
if len(n) == 0:
    print(True)
else:
    print(False,n,sep='\n')