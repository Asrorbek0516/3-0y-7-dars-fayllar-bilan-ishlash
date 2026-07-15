with open("matnn.txt", "r") as f:
    matn = f.read()

sozlar = matn.split()

hisob = {}

for soz in sozlar:
    if soz in hisob:
        hisob[soz] += 1
    else:
        hisob[soz] = 1

with open("statistika.txt", "w") as f:
    for soz, soni in hisob.items():
        f.write(f"{soz}: {soni}\n")