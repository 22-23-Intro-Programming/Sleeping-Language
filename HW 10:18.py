'''def greeting():
    name = input("Please enter your name:")

    print("Oh, ", name , ", is it? It is nice to meet you!")
    print("Have a good day!")

greeting()

def IsMultiple(num1, num2):
    if (num1 % num2):
        print(num1, " is a muitiple of ", num2)
    else:
        print(num1, " is not a muitiple of ", num2)

def main():
    print (IsMultiple(2,10))

main()'''
   
    
def IsPalindrome(string):
    length = len(string)
    x = 0
    y = length - 1
    while x < y:
        if string[x] != string[y]:
            print ("False")
            break
        x = x + 1
        y = y - 1
    print ("True")
    
    


def g():
    IsPalindrome("ahidhs")

g()
