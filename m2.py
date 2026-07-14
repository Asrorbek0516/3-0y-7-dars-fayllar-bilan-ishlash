with open("ismlar.txt",'w') as f:
    for i in range(5):
        ism = input(f"{i+1} - ismni kiriting: ")
        data = f.write(ism + '\n')

with open("ismlar.txt",'r') as f:
    data = f.read()
print(data)