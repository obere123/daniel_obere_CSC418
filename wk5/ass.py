import tkinter as tk
from PIL import Image, ImageTk
import cv2
import numpy as np

# ------------------------ Setup ------------------------
# Load YOLO
net = cv2.dnn.readNet('yolo_files/yolov3.weights', 'yolo_files/yolov3.cfg')
with open('yolo_files/coco.names', 'r') as f:
    classes = f.read().splitlines()
colors = np.random.uniform(0, 255, size=(len(classes), 3))
font = cv2.FONT_HERSHEY_PLAIN

# Load video
video_path = 'video1.mp4'
cap = cv2.VideoCapture(video_path)
playing = True  # Playback flag

# ------------------------ Tkinter GUI ------------------------
root = tk.Tk()
root.title("YOLO Video Player")

canvas = tk.Label(root)
canvas.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

def play_video():
    global playing
    if not playing:
        playing = True
        update_frame()

def pause_video():
    global playing
    playing = False

play_btn = tk.Button(button_frame, text="▶️ Play", command=play_video)
pause_btn = tk.Button(button_frame, text="⏸️ Pause", command=pause_video)
play_btn.pack(side=tk.LEFT, padx=10)
pause_btn.pack(side=tk.LEFT, padx=10)

# ------------------------ Video Processing Function ------------------------
def update_frame():
    global playing
    if not playing:
        return

    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Restart video
        ret, frame = cap.read()

    height, width, _ = frame.shape

    # Preprocessing
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    output_layers_names = net.getUnconnectedOutLayersNames()
    layer_outputs = net.forward(output_layers_names)

    boxes = []
    confidences = []
    class_ids = []

    for output in layer_outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    for i in indexes.flatten():
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        confidence = str(round(confidences[i], 2))
        color = colors[class_ids[i]]
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(frame, label + " " + confidence, (x, y - 10), font, 2, (255, 255, 255), 2)

    # Convert to Tkinter format
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)

    canvas.imgtk = imgtk
    canvas.configure(image=imgtk)

    root.after(30, update_frame)

# ------------------------ Close Handler ------------------------
def on_close():
    global playing
    playing = False
    cap.release()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

# Start video loop
update_frame()
root.mainloop()
