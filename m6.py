kalit_suz = input("Kalit suzni kiriting: ")

with open("matn.txt",'r') as f:
    matn = f.read()

    soni = matn.count(kalit_suz)
print(f"matn textida {kalit_suz} kalit soz {soni} marta uchradi")