from datetime import datetime

hozir = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("jurnal.txt", "a") as f:
    f.write(f"Dastur ishga tushdi: {hozir}\n")

print("Yangi yozuv jurnal.txt fayliga qushildi.")
