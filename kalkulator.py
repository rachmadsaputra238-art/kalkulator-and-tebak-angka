def penjumlahan(a,b):
    print(f"{a} + {b} = {a+b}")

def pengurangan(a,b):
    print(f"{a} - {b} = {a-b}")

def pembagian(a,b):
    print(f"{a} / {b} = {a/b}")

def perkalian(a,b):
    print(f"{a} * {b} = {a*b}")

status = True

while status:
    print("="*20)
    print("kalkulator".center(20))
    print("="*20)
    print()
    print("pilihan opsi:")
    print()
    print("1. penjumlahan")
    print("2. pengurangan")
    print("3. pembagian")
    print("4. perkalian")
    print("5. keluar")
    print("="*20)

    opsi = (input("pilihlah opsi yang tersedia di atas :"))

    if opsi == "5":
        print("anda telah keluar dari kalkulator")
        status = False

    elif opsi in ("1", "2", "3", "4"):

        num1 = int(input("tolong masukkan angka pertama anda :"))
        num2 = int(input("tolong masukkan angka kedua anda :"))

        if opsi == "1":
            print(f"{penjumlahan(num1,num2)}")

        elif opsi == "2":
            print(f"{pengurangan(num1,num2)}")

        elif opsi == "3":
            print(f"{pembagian(num1,num2)}")

        elif opsi == "4":
            print(f"{perkalian(num1,num2)}")
