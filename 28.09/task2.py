a = "0139412831055230677798"
b = {}
for key in a:
    if key not in b.keys():
        b[key] = 1
    else:
        b[key] += 1
print(b)