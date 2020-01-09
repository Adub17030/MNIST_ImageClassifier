import cv2
import numpy as np 
from model import ImageNerualNet
import ctypes

#create our image classifier NN or brain
brain = ImageNerualNet()

###brain.show_performance()

#creating 600 x 600 canvas for drawing
canvas = np.ones((600, 600), dtype="uint8") * 255.0
#marking 400 x 400 area of interest to be black
canvas[150:450, 150:450] = 0

start_pt = None
end_pt = None
is_drawing_stroke = None

def draw_line(img, start_at, end_at):
    cv2.line(img, start_at, end_at, 255, 20)

def on_mouse_events(event, x, y, flags, params):
    global start_pt
    global end_pt
    global canvas
    global is_drawing_stroke
    if event == cv2.EVENT_LBUTTONDOWN:
        if is_drawing_stroke:
            start_pt = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE:
        if is_drawing_stroke:
            end_pt = (x, y)
            draw_line(canvas, start_pt, end_pt)
            start_pt = end_pt
    elif event == cv2.EVENT_LBUTTONUP:
        is_drawing_stroke = False

ctypes.windll.user32.MessageBoxW(0, "Press \'s\' to begin drawing\nPress \'p\' for the NN to predict your drawing\nPress \'c\' to clear the canvas\nPress \'q\' to quit", "Number Classifier controls", 1)
cv2.namedWindow("Drawing Board")
cv2.setMouseCallback("Drawing Board", on_mouse_events)

while (True):
    cv2.imshow("Drawing Board", canvas)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        is_drawing_stroke = True
    elif key == ord('c'):
        canvas[150:450, 150:450] = 0
    elif key == ord('p'):
        image = canvas[150:450, 150:450]
        prediction = brain.predict(image)
        print("PREDICTION: ", prediction)

cv2.destroyAllWindows()