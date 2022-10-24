'''
class Person:

    def __init__(self, hairColor, height, weight, name):
        self.hairColor = hairColor
        self.height = height
        self.weight = weight
        self.name = name
        self.alive = True

    def playSoccer(self, skill):
        if skill > 5:
            print("Wow, he scored")
        elif skill > 1:
            print("Wow, he misssed")
        else:
            self.alive = False

    def getAlive(self):
        return self.alive


def main():
    Ryan = Person ("Black", "180 cm", "45 kg", "Ryan Cao")
    Ryan.playSoccer(7)
    Ryan.getAlive()
    Ryan.playSoccer(1)
    Ryan.getAlive()

if __name__ == "__main__":
    main()
    '''


    
myS = ""
print(myS)

#concatenate
newS = "Mr." + "Considine"
print (newS)

'''for i in range (5):
    print (i)
    myS = myS + "Python "
'''

'''for i in range(len(newS)):
    print(newS[i])'''
    #error
    #if newS[i] == " ":
        #newS = "Mr,Philips"
i = 0
while (len(newS) > 11):
    print (newS[i])
    if newS[i] == " ":
        newS = "Mr.Philips"
        i = i + 1


print (newS)
