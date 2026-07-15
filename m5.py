with open("sonlar.txt", 'r') as f:
    data = list(map(int,f.readlines()))

    juft_sonlar = list(filter(lambda x: x%2==0, data))

    print(juft_sonlar)
