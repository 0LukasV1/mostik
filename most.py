import random
import tkinter as tk
imageIsland = tk.PhotoImage(file = "obrazky/ostrov0.png")
imageIsland2 = tk.PhotoImage(file = "obrazky/ostrov3.png")
imageMostHor = tk.PhotoImage(file = "obrazky/ostrov1.png")
imageMostVer = tk.PhotoImage(file = "obrazky/ostrov2.png")
imageKruhBlue = tk.PhotoImage(file = "obrazky/ostrov_kruh0.png")
imageKruhOrange = tk.PhotoImage(file = "obrazky/ostrov_kruh1.png")
win = tk.Tk()
widthVar = 500
heightVar = 500
pictureWidth = 50
pictureHeight = 50
randX = random.randrange(4,7)
randY = random.randrange(3,10)
water = []
islands = []
canvas= tk.Canvas(width = randX * pictureWidth + 100, height = randY * pictureHeight, background="gray")
canvas.pack()

def more(e):
    global water
    print("klikol si")
    zoz = canvas.find_overlapping(e.x, e.y, e.x + 1, e.y + 1)
    if (len(zoz) != 0 and zoz[0] in water) and status == False:
        print("iba voda")
        newX = (e.x // pictureWidth) * pictureWidth
        newY = (e.y // pictureHeight) * pictureHeight
        temp = zoz[0]
        canvas.delete(temp)
        water.remove(temp)
        canvas.create_image(newX, newY, anchor="nw", image=imageMostHor, tag="bridge")
    elif (len(zoz) != 0 and zoz[0] in water) and status == True:
        print("iba voda")
        newX = (e.x // pictureWidth) * pictureWidth
        newY = (e.y // pictureHeight) * pictureHeight
        temp = zoz[0]
        water.remove(temp)
        canvas.create_image(newX, newY, anchor="nw", image=imageIsland, tag="bridge")

def load(e):
    zoz = canvas.find_overlapping(e.x, e.y, e.x + 1, e.y + 1)
    canvas.itemcget(zoz[0], "image")
    print(canvas.itemcget(zoz[0], "image"))
    if canvas.itemcget(zoz[0], "image") == "pyimage3":
        canvas.itemconfig(zoz[0], image=imageMostVer)
    else:
        canvas.itemconfig(zoz[0], image=imageMostHor)

def start():
    global water, islands
    for y in range(randY):
        for x in range(randX):
            resultIsland = random.randrange(0, 101)
            if resultIsland <= 20:
                islands.append(canvas.create_image(pictureWidth * x, pictureHeight * y, anchor='nw', image=imageIsland))

            else:
                water.append(canvas.create_image(pictureWidth * x, pictureHeight * y, anchor='nw', image=imageIsland2))
    canvas.create_image(randX * pictureWidth + 25, 0, anchor="nw", tags="kruh", image=imageKruhBlue)

def dirt(e):
    global status
    zoz = canvas.find_overlapping(e.x, e.y, e.x + 1, e.y + 1)
    canvas.itemcget(zoz[0], "image")
    print(canvas.itemcget(zoz[0], "image"))
    print(status)
    if canvas.itemcget(zoz[0], "image") == "pyimage5":
        status = True
        canvas.itemconfig(zoz[0], image=imageKruhOrange)
    else:
        status = False
        canvas.itemconfig(zoz[0], image=imageKruhBlue)

start()
canvas.tag_bind("bridge", "<Button-1>", load)
canvas.tag_bind("kruh", "<Button-1>", dirt)
canvas.bind("<Button-1>", more)
win.mainloop()