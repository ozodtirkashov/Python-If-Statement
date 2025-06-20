price = int(input("Omonot summasini kiriting: "))

if price < 100000:
    print("5%")

if 100000 <= price <= 500000:
    print("7%")

if price >= 500000:
    print("10%")