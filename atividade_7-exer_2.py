a = [3, 4, 5, 8]
b = [6, 7, 5, 9]
if a[0] == b[0]:
    a.remove(b[0])
elif a[1] == b[1]:
    a.remove(b[1])
elif a[1] == b[2]:
    a.remove(b[2])
elif a[1] == b[3]:
    a.remove(b[3])
elif a[2] == b[0]:
    a.remove(b[0])
elif a[2] == b[1]:
    a.remove(b[1])
elif a[2] == b[2]:
    a.remove(b[2])
elif a[2] == b[3]:
    a.remove(b[3])
elif a[3] == b[0]:
    a.remove(b[0])
elif a[3] == b[1]:
    a.remove(b[1])
elif a[3] == b[2]:
    a.remove(b[2])
elif a[3] == b[3]:
    a.remove(b[3])
a.extend(b)
print(a)