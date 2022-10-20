class Cat:
    #The constructor method. Defines how the cat is initially created
    def __init__(self, name, age, color):
        #create instance variables
        self.fur = "fluffy"
        self.age = age
        self.color = color
        self.name = name

    def getAge(self):
        return self.age

    def getName(self):
        return self.name
        

def main():
    C = Cat("Mittens", 20, "Black")
    D = Cat("Leo", 12, "Brown")

    print("Hi cat, what is your name?")

    print(C.getName())

    print(D.getName())

    print("Cat ages: ")
    print(C.getName()+ ":" + str(C.getAge()))
    print(D.getName()+ ":" + str(C.getAge()))

    

if __name__ == "__main__":

    main()
