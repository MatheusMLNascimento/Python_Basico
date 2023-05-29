a = [1,5,7,8,3]
b = [5,3,2,4,6]
i = 0
j = 0
while i <= len(a):
    j = 0
    while j <= len(b):
        if a[i] == b[j]:
            a.remove(b[j])
        j += 1
    i += 1
a.extend(b)
print(a)