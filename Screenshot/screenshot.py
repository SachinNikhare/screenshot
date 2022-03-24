import time
import pyautogui
import tkinter as tk

def screenshot():
    name=int(round(time.time()*1000))
    name="{}.png".format(name)
    img=pyautogui.screenshot(name)
    img.show()


root= tk.Tk()
root.title("Screenshot")
root.geometry("120x60")
root.minsize(120,60)
root.maxsize(120,60)
frame = tk.Frame(root,bg="white")
frame.pack(side=tk.LEFT)
photo = tk.PhotoImage(file="cam.png")
button = tk.Button(frame,image=photo,command=screenshot)
button.pack(side=tk.LEFT)
qphoto = tk.PhotoImage(file="quit.png")
closebtn = tk.Button(frame,image=qphoto,command=quit)
closebtn.pack(side=tk.LEFT)
    
root.mainloop()
