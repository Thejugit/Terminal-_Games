import random
global ans
def game():

    all_list = ["snake", "happy", "smile", "peace", "charm", "grace", "fresh", "bonus", "magic", "come", "bear", "play", "sing", "bird", "bean", "game", "rice", "four", "fish", "gold", "girl", "boy", "toy", "cool", "hot", "fire", "feel", "gone", "goat", "man", "wan", "can", "any", "health", "follow", "wealth", "reward", "action", "genius", "number", "people", "system", "help", "great", "work", "bread", "dog", "cat", "youth", "name", "phone", "charger", "laptop", "watch", "curtain", "cupboard", "case", "red", "blue", "white", "black", "pink", "camera", "hole", "one", "two", "six", "seven", "table", "knot", "speed", "car", "bike", "van", "bus", "scooter", "teacher", "students", "watermelon", "mango", "banana", "carrot", "pineapple"]

    random_no = random.randint(0, len(all_list)-1)

    word = all_list[random_no]
    chance = 1
    print("\nWelcome to Wordle!\n")
    print("The word contains", len(word), "letters")
    print("If a word more than ", len(word), "letters are entered, the first", len(word),"letters will be considered")
    print("If a word less than ", len(word), "letters are entered, the remaining letters will be considered as space")
    print("you will have 6 guesses till you find the word")
    while chance <= 6:
        guess = input("\nyour guess: ")
            
        ls = []
        ls1 = []
        
        for i in word:
            ls.append(i)
        for k in guess:
            ls1.append(k)
        space = len(word) - len(ls1)
        
        if len(guess) < len(word):
            print("Word smaller than", len(word), "letters")
            while space != 0:
                ls1.append(" ")
                space -= 1
            print("The remaining letters will be considered as a space")
                
        #print(ls)
        #print(ls1)
        a = 0
        j = 0
        matching = ""
        n_matching = ""
        wrong = ""
        while j <= len(word)-1:
            if ls1[j] in ls:
                #print("test")
                if ls1[j] == ls[j]:
                    #print("matching")
                    matching += ls1[j]
                elif ls1[j] != ls[j]:
                    #print("not matching")
                    n_matching += ls1[j]
            else:
                #print("False")
                wrong  += ls1[j]
            j += 1

        print("Letter matching and in correct position: ", matching)
        print("Letter matching but in wrong position: ", n_matching)
        print("Wrong letters : ", wrong)
        chance += 1
        if guess == word:
            print("\n-----------------------------------------")
            print("|  yay! you guessed the word correctly  |")
            print("-----------------------------------------")
            break
        if chance > 6:
            print("\nYou ran out of guesses")
            print("please try again later!")
            print("The correct word is", word)
x = 0
while x <= 5:
    ans = input("\nDo you want to continue(y/n): ")
    if ans == "y" or ans == "Y":
        game()
        x += 1
    else:
        print(" -- ")
        break
