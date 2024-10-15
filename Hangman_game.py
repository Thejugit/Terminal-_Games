import random
ArrMov = ["Vikram", "Coolie", "Bigil", "Thiruchitrbalam", "Kabali", "Mersal", "Thupakki", "Leo", "Goat", "Kalki", "Darbar", "Bahubali", "Vettiyan"]

rand_No = random.randint(0, len(ArrMov))
a = ArrMov[rand_No]

a1 = ""
ls = []
ls1 = []
cust = []

for i in a:
    a1 += i
    a1 += " "

def part1():
    for i in a:
        ls.append(i)
    global le
    le = len(a)/2 + 1
def part2():
    j = 1
    while j <= le:
        rand = random.randint(0, len(a)-1)
        if rand in ls1:
            j += 0
        else:
            ls1.append(rand)
            j += 1
def part3():
    global st
    global s
    st = ""
    s = ""
    for k in ls1:
        ls[k] = " _ "

    for z in ls:
        st = st + z

    abc = 0
    while abc < len(a):
        s += str(abc)
        s += " "
        abc += 1

part1()
part2()
part3()
print("Word to guess: ", st)
print("Index number: ", s)
bb = 0
while bb <= len(a)-3:
    ic = int(input("\nEnter the index number to guess: "))
    sg = input("Enter your guess: ")
    
    choice = a[ic]
    if choice == sg:
        s1 = ""
        print("\nCorrect guess")
        ls[ic] = choice
        #print(ls)
        for i in ls:
            s1 += i
            s1 += " "
        print(s1)
        print(s)
        bb += 1
        if s1 == a1:
            print("\nyou won the game")
        
    else:
        print("Wrong guess")
