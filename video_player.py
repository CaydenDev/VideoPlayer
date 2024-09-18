import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

class VideoPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Video Player")

        self.canvas = tk.Canvas(master, width=640, height=480)
        self.canvas.pack()

        self.btn_open = tk.Button(master, text="Open Video", command=self.open_video)
        self.btn_open.pack()

        self.video_source = None

    def open_video(self):
        self.video_source = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mov;*.mkv")])
        if self.video_source:
            self.play_video()

    def play_video(self):
        cap = cv2.VideoCapture(self.video_source)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = np.array(frame)
            frame = cv2.resize(frame, (640, 480))

            
            self.photo = tk.PhotoImage(image=cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

            self.master.update_idletasks()
            self.master.update()

        cap.release()

if __name__ == "__main__":
    root = tk.Tk()
    video_player = VideoPlayer(root)
    root.mainloop()
