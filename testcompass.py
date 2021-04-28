from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.title('yes')
root.geometry("600x400")

def step():
    for x in range(5):
         my_progress['value'] += 20
         root.update_idletasks()
         time.sleep(1)
         if my_progress['value']==100:
            my_progress.stop()

my_progress = ttk.Progressbar(root,orient = HORIZONTAL, length=300, mode = 'determinate')
my_progress.pack(pady=20)

button = Button(root, text=f'start',
                font=10, padx=10, pady=20, command=step, bg='#b5c3d2', fg='white')
button.pack()

root.mainloop()