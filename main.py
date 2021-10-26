import turtle
import time
from random import randint
import csv

kidN = 1
kids = []
singleStat = (0,0,0)

# kn = int(input("How many kids do we have? (up to 80) "))
# print("\n")
#
# for i in range(kn):
#     g = int(input("Georgian language grade for student "+str(i+1)+": "))
#     e = int(input("English language grade for student "+str(i+1)+": "))
#     m = int(input("Mathematics grade for student "+str(i+1)+": "))
#     kids.append((g,e,m))
#     print("\n")

kn = 42
file = open('Book2.csv')
type(file)
csvreader = csv.reader(file)
rows = []
for row in csvreader:
        kids.append((int(row[0]),int(row[1]),int(row[2]),row[3]))

mc = int(input("Coefficient for Maths: "))
gc = int(input("Coefficient for Georgian Language: "))
ec = int(input("Coefficient for English Language: "))

kids = list(map(lambda x: (x[0]*gc,x[1]*ec,x[2]*mc,x[3]), kids))


# gn = int(input("How many groups do we want to have? (up to 8) "))
gn = 6

gcs = []
for i in range(gn):
    gcs.append(kn//gn)
for i in range(kn%gn):
    gcs[i] += 1

kidsNormed = []
for kid in kids:
    kidsNormed.append(int(kid[0]+kid[1]+kid[2]))

kidsWithNames = []

# for i in range(len(kids)):
#     kidsWithNames.append((kidsNormed[i], kids[i][3]))

ctgs = []
kidsSorted = sorted(kidsNormed)
n = 0
for c in gcs:
    m = n
    n += c
    ctg = []
    for i in range(m,n):
        rv = kidsSorted[i]
        for k in range(len(kidsNormed)):
            if kidsNormed[k] == rv:
                check = True
                for ct in ctgs:
                    for kt in ct:
                        if kt[0] == k:
                            check = False
                for ct in ctg:
                    if ct[0] == k:
                        check = False
                if check:
                    r = k
        ctg.append((r,kidsSorted[i]))
    ctgs.append(ctg)

groups = []
for x in range(gn):
    groups.append([])
i = 0

for cc in ctgs:
    for kcc in cc:
        groups[i].append(kcc[0])
        i += 1
        if(i == len(groups)):
            i = 0


turtle.bgcolor("black")
turtle.colormode(255)
style = ('Courier', 30, 'italic')
turtle.penup()
turtle.goto(0,375)
turtle.color("white")
turtle.pendown()
turtle.Screen()
turtle.hideturtle()
turtle.write('Visualization:', font=style, align='center')
print(ctgs)
print(groups)

balls = []
texts = []
grtexts = []

for i in range(kn):
    x = turtle.Turtle()
    turtle.colormode(255)
    x.shape("circle")
    balls.append(x)

for i in range(kn):
    x = turtle.Turtle()
    texts.append(x)

for i in range(gn):
    x = turtle.Turtle()
    grtexts.append(x)

style1 = ('Courier', 12)
style2 = ('Courier', 20)

yco = 350
xco = -400
grcou = 0


for gr in ctgs:
    grtexts[grcou].penup()
    grtexts[grcou].goto(-370,yco+20)
    grtexts[grcou].color("white")
    grtexts[grcou].pendown()
    grtexts[grcou].write("Category "+str(grcou+1)+":", font=style2, align='center')
    grtexts[grcou].hideturtle()

    xco = -400
    for k in gr:
        k=k[0]
        balls[k].penup()
        balls[k].color(randint(0,255), randint(0,255), randint(0,255))
        balls[k].goto(xco,yco)
        balls[k].pendown()
        texts[k].penup()
        texts[k].color("white")
        texts[k].goto(xco,yco-30)
        texts[k].pendown()
        texts[k].write(str(kids[k][0])+","+str(kids[k][1])+","+str(kids[k][2]), font=style1, align='center')
        texts[k].hideturtle()
        xco += 95
    yco -= 130
    grcou += 1

time.sleep(1.5)
for t in range(len(texts)):
    texts[t].clear()
    texts[t].write(kidsNormed[t], font=style1, align='center')
    texts[t].hideturtle()

time.sleep(1.5)
for t in range(len(texts)):
    texts[t].clear()
    texts[t].write(kids[t][3], font=style1, align='center')
    texts[t].hideturtle()

time.sleep(1.5)
yc = 350
for gr in range(len(grtexts)):
    sum = 0
    for k in ctgs[gr]:
        sum += kidsNormed[k[0]]
    grtexts[gr].clear()
    grtexts[gr].goto(-300,yc+20)
    grtexts[gr].write("Category "+str(gr+1)+": Sum - " + str(sum), font=style2, align='center')
    yc -= 130

time.sleep(3)
for gr in grtexts:
    gr.clear()

for gr in texts:
    gr.clear()

yco = 350
xco = -400
grcou = 0

for gr in groups:
    grtexts[grcou].penup()
    grtexts[grcou].goto(-380,yco+20)
    grtexts[grcou].color("white")
    grtexts[grcou].pendown()
    grtexts[grcou].write("Group "+str(grcou+1)+":", font=style2, align='center')
    grtexts[grcou].hideturtle()

    xco = -400
    for k in gr:
        balls[k].penup()
        balls[k].color(randint(0,255), randint(0,255), randint(0,255))
        balls[k].goto(xco,yco)
        balls[k].pendown()
        texts[k].penup()
        texts[k].color("white")
        texts[k].goto(xco,yco-30)
        texts[k].pendown()
        texts[k].write(str(kids[k][0])+","+str(kids[k][1])+","+str(kids[k][2]), font=style1, align='center')
        texts[k].hideturtle()
        xco += 95
    yco -= 130
    grcou += 1


time.sleep(2)
for t in range(len(texts)):
    texts[t].clear()
    texts[t].write(kidsNormed[t], font=style1, align='center')
    texts[t].hideturtle()

time.sleep(1.5)
yc = 350
for gr in range(len(grtexts)):
    sum = 0
    for k in groups[gr]:
        sum += kidsNormed[k]
    grtexts[gr].clear()
    grtexts[gr].goto(-300,yc+20)
    grtexts[gr].write("Group "+str(gr+1)+": Sum - " + str(sum), font=style2, align='center')
    yc -= 130

time.sleep(1.5)
for t in range(len(texts)):
    texts[t].clear()
    texts[t].write(kids[t][3], font=style1, align='center')
    texts[t].hideturtle()



turtle.mainloop()
