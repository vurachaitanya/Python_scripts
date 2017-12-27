result = []
for x in range(2):
    for y in range(1,5):
        if y%3 == 0:
            break
        result.append(x)
        print result
