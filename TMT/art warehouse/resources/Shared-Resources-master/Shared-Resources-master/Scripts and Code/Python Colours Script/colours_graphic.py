import random
import turtle
import tkinter

color = []
generated = []
low = 30
count = 0
y = 370

wn = turtle.Screen()
wn.colormode(255)
draw = turtle.Turtle()
draw.penup()
draw.speed(10)
draw.goto(-750, y)
print('check')

with open('colours.txt', 'r+') as colours:
    used = colours.read().splitlines()

    for i in range(400):
        count += 1
        color = []
        r, g, b = random.randint(0,254), random.randint(low, low+30), random.randint(0, 254)
        color.extend([r, g, b])
        low += 60
        if count == 30:
            y -= 50
            draw.goto(-750, y)
            count = 0
        if low > 230:
            low -= 210
        if str(color) not in used:
            print('NOT USED')
            draw.fillcolor(color)
            draw.begin_fill()
            for i in range(4):
                draw.forward(50)
                draw.right(90)
            draw.forward(50)
            draw.end_fill()
            used.append(str(color))
            generated.append(color)
            colours.write('\n%s' % (color))
        else:
            print('HAS BEEEN USED!!')
            pass

for i in generated:
    print('%s' % (i))
tkinter.mainloop()
    
