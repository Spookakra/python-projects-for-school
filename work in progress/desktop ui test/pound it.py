import tkinter as tk
import webbrowser

link = "deathgenerator.com"

window = tk.Tk()
window.title("death window")
window.geometry("600x500")

#result of button press
def grindsetevent(event):
    print("i am in a lot of pain")
    webbrowser.open(link)

#simple 1999 button
grindsetman = tk.Button(window, text = "click me")
grindsetman.grid(column=8, row=5)
grindsetman.bind('<Button-1>' ,grindsetevent)

#i am stuck in a perpetual loop of pain

window.mainloop()