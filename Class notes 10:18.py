
def main():
    #print("Hello World!")
    hello = "Hello class!"
    numStudents = 13
    print(hello + " There are " + str(numStudents) + " of you today")
    x = input("What is the weather today?")
    print(x)
    if x == "sunny":
        print("wow, what a great day to play outside!")
    else:
        print("June Gloom")

    y = input("What is your favourate number?")
    print(y)
    y = int(y)
    if y > 10:
        print(y / 2)
    else:
        print(y + 1)

    res = add3(12)
    print(res)
    print (add3(100))

    myString = input("What is your name?")
    firstChar = myString[0]
    print(firstChar)

    for char in myString:
        print(char)

def add3():
    #anything here is part of the add3 method definition
    result = x + 3
    

if __name__ == "__main__":
    main()
