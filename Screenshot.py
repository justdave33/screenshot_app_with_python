import pyautogui
import time
import tkinter as tk

def screenshot():
    time.sleep(5)
    name = time.time()
    name = 'C:/Users/Just-Dave/Desktop/My Portfolio/screenshot_app_with_python/{}.png'.format(name)
    img= pyautogui.screenshot()
    img.save(name)
    img.show()
   
         
root = tk.Tk()
frame =tk.Frame(root)
frame.pack()

button = tk.Button(frame,text="Take Screenshot",command=screenshot)
button.pack(side=tk.LEFT)  

close = tk.Button(frame,text="Quit",command=quit)
close.pack(side=tk.LEFT)

root.mainloop()

    
    
    