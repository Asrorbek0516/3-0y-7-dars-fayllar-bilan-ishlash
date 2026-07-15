with open("a.txt", 'r') as f:
    data = f.read()

with open("b.txt", 'r') as f1:
    data1 = f1.read()

with open("result.txt", 'w') as f:
    f.write(data + ' ' + data1)

print("yozildi")