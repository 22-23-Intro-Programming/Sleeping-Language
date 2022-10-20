class Snake:
    
    def __init__(self, name, age, length, color):
        
        self.length = length
        self.age = age
        self.color = color
        self.name = name

    def getAge(self):
        return self.age

    def getName(self):
        return self.name

    def getLength(self):
        return self.length

    def getColor(self):
        return self.color
        

def main():
    A = Snake("Sunny", 20, 20, "Black")
    B = Snake("Leo", 12, 2, "Brown")
    C = Snake("Dora", 100, 10, "Red and white")
    D = Snake("Bob", 1, 123, "Rainbow")
    

    print("Snake names: ")
    print(A.getName())
    print(B.getName())
    print(C.getName())
    print(D.getName())

    print("Snake ages: ")
    print(A.getName()+ ":" + str(A.getAge()))
    print(B.getName()+ ":" + str(B.getAge()))
    print(C.getName()+ ":" + str(C.getAge()))
    print(D.getName()+ ":" + str(D.getAge()))

    print("Snake lengths: ")
    print(A.getName()+ ":" + str(A.getLength()))
    print(B.getName()+ ":" + str(B.getLength()))
    print(C.getName()+ ":" + str(C.getLength()))
    print(D.getName()+ ":" + str(D.getLength()))

    print("Snake colors: ")
    print(A.getName()+ ":" + str(A.getColor()))
    print(B.getName()+ ":" + str(B.getColor()))
    print(C.getName()+ ":" + str(C.getColor()))
    print(D.getName()+ ":" + str(D.getColor()))

    

if __name__ == "__main__":

    main()
