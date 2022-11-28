from graphics import *
from Button import *

def palindrome(ans):
    answer = ans

    last = len(answer)-1
    start = answer[0]

    i = 0 
    for char in answer:
        if (answer[0+i] != answer[last-i]):
            return False
        i = i + 1
        
    return True


def main():
    win = GraphWin("Palindrome", 800, 600)
    win.setBackground("beige")

    Q = Button(win, Point(650, 500), Point(750, 575), "tomato", "Quit")
    P = Button(win, Point(350, 350), Point(450, 425), "cyan", "Check!")
    

    E = Entry(Point(400,300), 30)
    E.draw(win)

    T = Text(Point(400, 250), "Write someting below that you think is a palindrome")
    T.draw(win)


    while True:
        m = win.getMouse()
        if Q.isClicked(m):
            break
        if P.isClicked(m):
            pal = E.getText()
            print(palindrome(pal))
    
    win.close()


if __name__=="__main__":
    main()
