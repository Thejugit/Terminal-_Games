no = ["11", "12", "13", "21", "22", "23", "31", "32", "33"]
print("\nWELCOME TO X/O GAME\n")

print("  ________________")
print("3 |    |    |    |")
print("  |--------------|")
print("2 |    |    |    |")
print("  |--------------|")
print("1 |    |    |    |")
print("  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
print("    1     2    3  ")

print("\nSample Input:")
print("Enter the coordinates you want to enter for X: 11")
print("In the place of 11 you can place any other coordinates in this format...\n")

a = "________________"
b_ = "|    |    |    |"  #2, 7, 12
c = "|--------------|"
d_ = "|    |    |    |"  #
e = "|--------------|"
f_ = "|    |    |    |"  #
g = "‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"

ls_b = []
ls_d = []
ls_f = []

n = 0

final_str_f = ""
final_str_d = ""
final_str_b = ""

for i in b_:
    ls_b.append(i)
for j in d_:
    ls_d.append(j)
for k in f_:
    ls_f.append(k)

def prt():
    global final_str_f
    global final_str_d
    global final_str_b
    for i in ls_f:
        final_str_f += i
    for j in ls_d:
        final_str_d += j
    for k in ls_b:
        final_str_b += k
    print(a)
    print(final_str_b)
    print(c)
    print(final_str_d)
    print(e)
    print(final_str_f)
    print(g)

while True:
    final_str_f = ""
    final_str_d = ""
    final_str_b = ""

    if n >= 9:
        break
    if n%2 == 0:
        choice = input("Enter the coordinates you want to enter for X:")
        n += 1
        if choice == "11":
            ls_f[2] = "X"
            prt()
        if choice == "12":
            ls_f[7] = "X"
            prt()
        if choice == "13":
            ls_f[12] = "X"
            prt()
        if choice == "21":
            ls_d[2] = "X"
            prt()
        if choice == "22":
            ls_d[7] = "X"
            prt()
        if choice == "23":
            ls_d[12] = "X"
            prt()
        if choice == "31":
            ls_b[2] = "X"
            prt()
        if choice == "32":
            ls_b[7] = "X"
            prt()
        if choice == "33":
            ls_b[12] = "X"
            prt()
        if choice not in no:
            print("Please enter a valid coordinate")
            n -= 1
    elif n%2 != 0:
        choice = input("Enter the coordinates you want to enter for O:")
        n += 1
        if choice == "11":
            ls_f[2] = "O"
            prt()
        if choice == "12":
            ls_f[7] = "O"
            prt()
        if choice == "13":
            ls_f[12] = "O"
            prt()
        if choice == "21":
            ls_d[2] = "O"
            prt()
        if choice == "22":
            ls_d[7] = "O"
            prt()
        if choice == "23":
            ls_d[12] = "O"
            prt()
        if choice == "31":
            ls_b[2] = "O"
            prt()
        if choice == "32":
            ls_b[7] = "O"
            prt()
        if choice == "33":
            ls_b[12] = "O"
            prt()
        if choice not in no:
            print("Please enter a valid coordinate")
            n -= 1
    if n >= 5:
        if ls_b[2] == ls_b[7] and ls_b[7] == ls_b[12] and ls_b[7] == "X" and ls_b[2] == "X" and ls_b[12] == "X" or ls_b[7] == "O" and ls_b[2] == "O" and ls_b[12] == "O":
            print(ls_b[7], "Wins the Match")
            break
        elif ls_d[2] == ls_d[7] and ls_d[7] == ls_d[12] and ls_d[7] == "X" and ls_d[12] == "X" and ls_d[2] == "X" or ls_d[7] == "O" and ls_d[12] == "O" and ls_d[2] == "O":
            print(ls_d[7], "Wins the Match")
            break
        elif ls_f[2] == ls_f[7] and ls_f[7] == ls_f[12] and ls_f[7] == "X" and ls_f[2] == "X" and ls_f[12] == "X" or ls_f[7] == "O" and ls_f[2] == "O" and ls_f[12] == "O":
            print(ls_f[7], "Wins the Match")
            break
        elif ls_b[2] == ls_d[7] and ls_d[7] == ls_f[12] and ls_d[7] == "X" and ls_b[2] == "X" and ls_f[12] == "X" or ls_d[7] == "O" and ls_b[2] == "O" and ls_f[12] == "O":
            print(ls_f[12], "Wins the Match")
            break
        elif ls_b[12] == ls_d[7] and ls_d[7] == ls_f[2] and ls_d[7] == "X" and ls_b[12] == "X" and ls_f[2] == "X" or ls_d[7] == "O" and ls_b[12] == "O" and ls_f[2] == "O":
            print(ls_f[2], "Wins the Match")
            break
        elif ls_b[2] == ls_d[2] and ls_d[2] == ls_f[2] and ls_d[2] == "X" and ls_b[2] == "X" and ls_f[2] == "X" or ls_d[2] == "O" and ls_b[2] == "O" and ls_f[2] == "O":
            print(ls_f[2], "Wins the Match")
            break
        elif ls_b[7] == ls_d[7] and ls_d[7] == ls_f[7] and ls_d[7] == "X" and ls_b[7] == "X" and ls_f[7] == "X" or ls_d[7] == "O" and ls_b[7] == "O" and ls_f[7] == "O":
            print(ls_f[7], "Wins the Match")
            break
        elif ls_b[12] == ls_d[12] and ls_d[12] == ls_f[12] and ls_d[12] == "X" and ls_b[12] == "X" and ls_f[12] == "X" or ls_d[12] == "O" and ls_b[12] == "O" and ls_f[12] == "O":
            print(ls_f[12], "Wins the Match")
            break
        else:
            continue
