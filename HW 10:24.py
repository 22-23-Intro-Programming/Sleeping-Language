
def factorial(num):
    output = 0
    i = 0
   
    while(i <= num):
        output = output + i
        i = i + 1
    print(output)
        
    


'''
def doubleIt():
    string = input("please enetr a phrase that you would like to 'Double': ")
    output=""
    for i in string:
        output = output + i*2
    print(output) 
'''

'''
def camelCase():
    a = input("please enter a file name")
    i = 0
    while (i < len(a)):
        if a[i] == " ":
            a = a.replace(a[i], "")
            a = a.upper(a[i+1])
        elif a[i] == "/":
            a = a.replace(a[i], "-")
        i = i + 1

    print("your file name should be: " + a)
'''
   
                          

def main():
    
    factorial(5)
    #doubleIt()
    #camelCase()
    

main()
