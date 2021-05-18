from images import IMAGES,totalLetters
import random
def load_word():
    #Change File Name
    fileptr = open(r"E:\Stuff\ruby\hangman-cli\words.txt","r")
    filelist = fileptr.readline().split()
    fileptr.close()
    word = filelist[random.randint(0,len(filelist)-1)]
    hashmap = {}
    for i in range(len(word)):
        if word[i] not in hashmap:
            hashmap[word[i]]=[i]
        else:
            hashmap[word[i]].append(i)
    return hashmap,len(word),word

def main():
    word,lengthofword,print_word = load_word()
    ans = ["__"]*lengthofword
    count =0
    lives = 0
    hint = 0
    while True:
        print("No of lives: ",8-lives)
        print("Available Letters: ",*sorted(totalLetters),sep="",end="\n\n")
        print(*ans)
        letter = input("Type a letter to guess\n").lower()
        if letter not in totalLetters and letter!="hint":
            print("Invalid input correct input is between a-z or letter already used")
            continue
        elif letter=="hint" and hint==0:
            hint+=1
            letter = random.choice(list(word.keys()))
            
        elif letter=="hint" and hint>0:
            print("already used the hint")
            continue

        totalLetters.remove(letter)
        if letter in word:
            count+=1
            for j in word[letter]:
                ans[j]=letter
            word.pop(letter)
            if 0==len(word):
                print("You Win :D You guessed the correct word which was\n",print_word,sep="")
                break  
        else:
            if lives == 8:
                print("You Lose :( the correct word was\n",print_word,sep="")
                break
            print(IMAGES[lives])
            lives+=1        
print("Welcome to The Game")
input("press any Key to Start the game... ")
main()  