import random

angka = random.randint(1, 25)
kesempatan = 5

while kesempatan > 0:
    tebak = int(input("Ayo bermain tebak angka silakan kamu menebak angka mulai dari 1-25: "))

    if tebak == angka:
        print("yey jawaban kamu Benar!")
        break

    print("maaf jawaban kamu terlalu kecil!" if tebak < angka else "maaf jawaban kamu terlalu besar!")
    kesempatan -= 1
    print("Sisa kesempatan kamu adalah:", kesempatan)

print("jawaban yang benar adalah:", angka)
