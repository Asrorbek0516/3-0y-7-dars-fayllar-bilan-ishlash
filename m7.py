with open("talabalar.txt", "r") as f:
    for qator in f:
        ism, baho = qator.strip().split(",")
        baho = int(baho)

        if baho > 80:
            print(ism, baho)