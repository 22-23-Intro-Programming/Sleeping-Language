def q1():
    intList = [1,2,3,4,7,6]
    for i in range(len(intList)):
        if intList[i] == 7:
            if intList [i+1] == 7:
                return "True"
                stop

    return "False"


def q2():
    total = 0
    sumList = [1,2,3,23,5,0,2,2]
    for a in range(len(sumList)):
        if sumList[a] == 0:
            break
        total = total + sumList[a]
    print(total)

def q3():
    Total = 0
    sumlist = [1,2,4,5,6,3,7,8,9]
    b = 0
    while b < len(sumlist):
        
        if sumlist[b] == 2:
            b = b + 1
            break
        
        else:
            Total = Total + sumlist[b]
            b = b + 1

    while b < len(sumlist):
        if sumlist[b] == 3:
            b = b + 1
            break
        else:
            b = b + 1

        
    while b < len(sumlist):
        Total = Total + sumlist[b]
        b = b + 1

    print (Total)
            

    
    

def main():
    #print(q1())
    #q2()
    q3()


if __name__ == "__main__":
    main()
