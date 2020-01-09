# mainloop()
from PIL import ImageTk, Image, ImageDraw
import PIL
from tkinter import *

def main():
    
    width = 200
    height = 200
    #center = height//2
    white = (255, 255, 255)
    #green = (0,128,0)

    def save():
        filename = "tkInter_Canvas_Test\inner_folder\image.png"
        image1.save(filename)
        image1.resize((28, 28), 1).save("tkInter_Canvas_Test\inner_folder\image28x28.png")

    def paint(event):
        # python_green = "#476042"
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        cv.create_oval(x1, y1, x2, y2, fill="white",width=10)
        for x in range(100):
            draw.ellipse([x1, y1, x2, y2],fill="white",width=500)

    root = Tk()

    # Tkinter create a canvas to draw on
    cv = Canvas(root, width=width, height=height, bg='white')
    cv.pack()

    # PIL create an empty image and draw object to draw on
    # memory only, not visible
    image1 = PIL.Image.new("RGB", (width, height), (0,0,0))
    draw = ImageDraw.Draw(image1)

    # do the Tkinter canvas drawings (visible)
    # cv.create_line([0, center, width, center], fill='green')

    cv.pack(expand=YES, fill=BOTH)
    cv.bind("<B1-Motion>", paint)

    # do the PIL image/draw (in memory) drawings
    # draw.line([0, center, width, center], green)

    # PIL image can be saved as .png .jpg .gif or .bmp file (among others)
    # filename = "my_drawing.png"
    # image1.save(filename)
    button=Button(text="save",command=save)
    button.pack()
    root.mainloop()


main()