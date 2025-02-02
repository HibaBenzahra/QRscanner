import cv2
import numpy as np
from pyzbar.pyzbar import decode
import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
from pygame import mixer  

# Initialize Sound
mixer.init()

# Initialize webcam
webcam = cv2.VideoCapture(0)
webcam.set(3, 640)
webcam.set(4, 480)

# GUI Setup
root = tk.Tk()
root.title("QR Code Scanner")
root.geometry("700x550")

lbl = Label(root)
lbl.pack()

running = False  # Webcam state
play_music =  True # Sound State

def scan_qr():
    global running
    global play_music
    if not running:
        return
    
    ret, frame = webcam.read()
    if not ret:
        return
    
    codes = decode(frame)

    if not codes:
        text, color = 'No QR Code Detected', (0, 0, 255)
        cv2.putText(frame, text, (200, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
        play_music = True
    else:
        for code in codes:
            QRdata = code.data.decode('utf-8')
            pts = np.array([code.polygon], np.int32).reshape((-1, 1, 2))

            try:
                with open('codes.txt') as f:
                    data_list = f.read().splitlines()

                # Check if QR code is authorized
                if QRdata in data_list:
                    text, color = 'Authorized', (0, 255, 0)
                else:
                    text, color = 'None Authorized', (0, 0, 255)

                # Draw bounding polygon
                cv2.polylines(frame, [pts], True, color, 3)
                x1, y1, w, h = code.rect
                cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

                # Play sound once when detecting a QR code
                if play_music:
                    mixer.music.load("tel3ni.MP3")  
                    mixer.music.play()
                    play_music = False  # Prevent repeated playback

            except FileNotFoundError:
                print("Error: codes.txt file not found.")


    
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = ImageTk.PhotoImage(Image.fromarray(img))
    lbl.config(image=img)
    lbl.image = img
    root.after(20, scan_qr)

def start():
    global running
    running = True
    scan_qr()

def stop():
    global running
    running = False


def close():
    webcam.release()
    cv2.destroyAllWindows()
    root.destroy()

start_btn = Button(root, text="Start Scan", command=start, bg="green", fg="white", font=("Arial", 14))
start_btn.pack(pady=10)

stop_btn = Button(root, text="Stop Scan", command=stop, bg="red", fg="white", font=("Arial", 14))
stop_btn.pack(pady=10)

exit_btn = Button(root, text="Exit", command=close, bg="black", fg="white", font=("Arial", 14))
exit_btn.pack(pady=10)

root.mainloop()
