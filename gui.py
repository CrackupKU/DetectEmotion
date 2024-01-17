import tkinter as tk
import random

# config
w,h = 500,500
radius = 300
threshold = 0.5
offset_x = (w-radius)/2
offset_y = (h-radius)/2

#root
root = tk.Tk()
root.title("Random Loop Animation")
canvas = tk.Canvas(root, width=w, height=h, bg='white')
canvas.pack()

# Create a circle on the canvas
circle = canvas.create_oval(20, 20, 50, 50, fill='blue')
mid = canvas.create_oval(10, 10, 20, 20, fill='black')
canvas.moveto(mid,w/2,h/2)
border = canvas.create_oval(0, 0, radius, radius)
canvas.moveto(border,offset_x,offset_y)
  
#border
rect = canvas.create_rectangle(10,10, 100, 30, fill='red' )



#label
anger = canvas.create_text(233,75, text="Anger", fill="black", anchor=tk.NW)
disgust = canvas.create_text(350,115, text="Disgust", fill="black", anchor=tk.NW)
happy = canvas.create_text(410,230, text="Happy", fill="black", anchor=tk.NW)
contempt = canvas.create_text(365,355, text="Contempt", fill="black", anchor=tk.NW)
neutral = canvas.create_text(228,410, text="Neutral", fill="black", anchor=tk.NW)
fear = canvas.create_text(110,355, text="Fear", fill="black", anchor=tk.NW)
sad = canvas.create_text(55,230, text="Sad", fill="black", anchor=tk.NW)
surprise = canvas.create_text(100,115, text="Surprise", fill="black", anchor=tk.NW)

canvas.itemconfigure(anger)

def find_main(ind):
    if ind == 0:
        canvas.moveto(rect, 205,70)
        canvas.itemconfigure(anger)
    elif ind == 1:
        canvas.moveto(rect, 345,350)
        canvas.itemconfigure(contempt)
    elif ind == 2:
        canvas.moveto(rect, 330,110)
        canvas.itemconfigure(disgust)   
    elif ind == 3:
        canvas.moveto(rect, 80,350)
        canvas.itemconfigure(fear)
    elif ind == 4:
        canvas.moveto(rect, 385,225)
        canvas.itemconfigure(happy)
    elif ind == 5:
        canvas.moveto(rect, 203,405)
        canvas.itemconfigure(neutral)
    elif ind == 6:
        canvas.moveto(rect, 20,225)
        canvas.itemconfigure(sad)
    elif ind == 7:
        canvas.moveto(rect, 80,110)
        canvas.itemconfigure(surprise)


#constant
EDGE = (2**0.5 /2 )
POC = [(0,1), (EDGE,-EDGE), (EDGE,EDGE), (-EDGE,-EDGE), (1,0), (0,-1), (-1,0), (-EDGE,EDGE)]

def move_circle(values):
    dx,dy = 0,0
    c = 0
    for i in range(len(values)):
        if values[i] >threshold:
            c+=1
            dx += POC[i][0]*values[i]
            dy += POC[i][1]*values[i]
    if c >0:
        max_ind = values.argmax()
        if values[max_ind] >threshold:
            find_main(max_ind)
        dx/=c
        dy/=c
        dx = (dx+1)/2
        dy = 1- ((dy +1) / 2)
        # Update the position of the circle
        canvas.moveto(circle,offset_x+ (radius*dx)-15,offset_y+(radius*dy)-15)
        root.update()

# root.mainloop()