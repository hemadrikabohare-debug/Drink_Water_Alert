from plyer import notification
import winsound
import threading
import time
import tkinter as tk


running = False

def Drink_Water_Alert():
    global running

    while running:
        notification.notify(
            title = "Drink Water Alert",
            message = "Time to drink water !"
        )
        winsound.PlaySound("water.wav", winsound.SND_FILENAME)
        time.sleep(10) # wait for 10 seconds before sending the next notification

def Start_Alert():
    global running

    if not running:
        running = True
        alert_thread = threading.Thread(target = Drink_Water_Alert)
        alert_thread.start()

def Stop_Alert():
    global running
    running = False

root = tk.Tk()
root.title("Drink Water Alert")
root.geometry("300x150")

tk.Button(root, text="Start Alert", command=Start_Alert).pack(pady= 20)
tk.Button(root, text="Stop Alert", command=Stop_Alert).pack(pady= 20)

root.mainloop()