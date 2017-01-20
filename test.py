a = '6'
count = 0
for i in range(0, 10000):
    if a in str(i):
        count += str(i).count(a)
print(count)
