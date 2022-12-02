from graphics import *
from Button import *

def darken(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i,j)
            r, g, b = pix[0], pix[1], pix[2]
            if r > 30:
                r = r - 30
            else:
                r = 0
            if g > 30:
                g = g - 30
            else:
                g = 0
            if b > 30:
                b = b - 30
            else:
                b = 0
            
            dColor = color_rgb(r,g,b)
            img.setPixel(i, j, dColor)

def lighten(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i,j)
            r, g, b = pix[0], pix[1], pix[2]
            if r < 225:
                r = r + 30
            else:
                r = 255
            if g < 225:
                g = g + 30
            else:
                g = 255
            if b < 225:
                b = b + 30
            else:
                b = 255
            
            lColor = color_rgb(r,g,b)
            img.setPixel(i, j, lColor)

def grayscale(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            avg = r + b + g
            avg = avg // 3

            gColor = color_rgb(avg, avg, avg)
            img.setPixel(i, j, gColor)

def contrast(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            avg = r + g + b
            avg = avg/3
            if avg <= 127:
                if r > 20:
                    r = r - 20
                else:
                    r = 0
                if g > 20:
                    g = g - 20
                else:
                    g = 0
                if b > 20:
                    b = b - 20
                else:
                    b = 0
            else:
                if r < 235:
                    r = r + 20
                else:
                    r = 255
                if g < 235:
                    g = g + 20
                else:
                    g = 255
                if b < 235:
                    b = b + 20
                else:
                    b = 255
                
                
                
            
            

            cColor = color_rgb(r, g, b)
            img.setPixel(i, j, cColor)
    
    



def main():
    
    win = GraphWin("Image Editor", 800, 600)
    win.setBackground("#FFAA00")
    I = Image(Point(300, 300), "veitchii.png")
    I.draw(win)
    
    B = Button(win, Point(600, 100), Point(700, 175), "tomato", "Darken")
    B1 = Button(win, Point(600, 200), Point(700, 275), "tomato", "Lighten")
    B2 = Button(win, Point(600, 300), Point(700, 375), "tomato", "Grayscale")
    B3 = Button(win, Point(600, 400), Point(700, 475), "tomato", "Contrast")


    Q = Button(win, Point(675, 500), Point(775, 575), "misty rose", "QUIT")

    while True:
        m = win.getMouse()
        
        if B.isClicked(m):
            darken(I)
            
        if B1.isClicked(m):
            lighten(I)

        if B2.isClicked(m):
            grayscale(I)

        if B3.isClicked(m):
            contrast(I)

        if Q.isClicked(m):
            break

    win.close()

if __name__ == "__main__":
    main()    
            
