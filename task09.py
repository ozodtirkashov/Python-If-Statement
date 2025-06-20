a_tomon = int(input("1-tomonni kiriting: "))
b_tomon =int(input("2-tomonni kiriting: "))
c_tomon =int(input("3-tomonni kiriting: "))

if a_tomon == b_tomon == c_tomon:
    print("Teng tomonli")

if a_tomon == b_tomon != c_tomon:
    print("Teng yonli")

if a_tomon != b_tomon != c_tomon:
    print("Turli tomonli")