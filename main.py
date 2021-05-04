from tkinter import*
from tkinter import ttk
import time
import math
from multiprocessing import Process
import random, socket, time

dev = None
dist = 0
degr = 0

#SERVER

def randr(mn, mx, rnd):
    return round(random.random() * (mx - mn) + mn, rnd)


def send_msg(sock, *msgs):
    for msg in msgs:
        msg = bytes(str(msg), 'utf-8')
        sock.sendall(msg)


ip = '10.0.0.17'
port = 45002

s = socket.socket()
s.bind((ip, port))
s.listen(5)


def handle(sock):
    while True:
        msg = str(sock.recv(3), 'utf-8')
        print(msg)
        if msg == 'pu\n' or msg == 'sc\n' or msg == 'sp\n' or msg == 'of\n':
            with open('../ledstrip/python/mode_' + msg[0:2] + '.txt', 'w') as f:
                pass
        if msg == 'qqq' or len(msg) == 0:
            return

def server():
    while True:
        print('Listening on {} port {}'.format(ip, port))
        sock, addr = s.accept()
        print('Accepted connection from {}'.format(addr))
        handle(sock)
        sock.close()
#SERVER
window = Tk()
window.geometry('400x250')
window.title('Main Window')
window['background']='#e8c3d2'
user = 'David Cohen'



window.geometry('500x500')

class Device:

    def __init__(self, name, mac_address):
        self._name = name
        self._mac = mac_address
        self._distance = 0

    def last_known_distance(self):
        pass

a = Device('keys', 'DD:DA:12:23:34')
my_devices = []

my_devices.append(a)

def myClick():
    search_window(window)


'''def myClick_start_search():
    for x in range(5):
         my_progress['value'] += 20
         root.update_idletasks()
         time.sleep(1)
         if my_progress['value']==100:
            my_progress.stop()
            
    canvas = Canvas(window, bg= '#e8c3d2')
    canvas.grid(row= 2, column= 0)
    canvas.create_line(0, 0, 100, 100, arrow=LAST)'''



def welcome_window():
    column_tracker = 0;
    row_tracker = 0;
    label1 = Label(window, text= f'Welcome: {user}', font = 10 ,bg= "#e8c3d2", padx = 40, pady=20)
    label1.grid(row = row_tracker, column=column_tracker)
    column_tracker += 1
    row_tracker +=1
    for i in range(len(my_devices)):
        button = Button(window, text=f'Device: {i+1}  \n {my_devices[i]._name} \n Distance:  {my_devices[i]._distance}', font = 10, padx=10, pady=20, command=myClick, bg='#b5c3d2', fg='white')
        button.grid(row=row_tracker, column=column_tracker)
        row_tracker += 1;


def search_window(window):



    def myClick_start_search():
        for x in range(5):
            my_progress['value'] += 20
            window.update_idletasks()
            time.sleep(1)
            if my_progress['value'] == 100:
                my_progress.stop()
        canvas = Canvas(window, bg= '#e8c3d2', borderwidth = 0, highlightthickness = 0 , width=400, height=400)
        canvas.grid(row=2, column=0)
        canvas.create_line(200,200, 200,200, tags=("line",), arrow="last")
        angle = 140
        a = math.radians(angle)
        r = 50
        x0, y0 = (200,200)
        x1 = x0 + r*math.cos(a)
        y1 = y0 + r*math.sin(a)
        x2 = x0 + -r*math.cos(a)
        y2 = y0 + -r*math.sin(a)
        canvas.coords("line", x1, y1, x2, y2)

    for w in window.winfo_children():
        w.destroy()
    window.title('Search Window')
    column_tracker = 0;
    row_tracker = 0;
    label1 = Label(window, text= f'Begin Searching for Device', font = 10 ,bg= "#e8c3d2", padx = 40, pady=20)
    label1.grid(row = row_tracker, column=column_tracker)
    row_tracker +=1
    my_progress = ttk.Progressbar(window, orient=HORIZONTAL, length=300, mode='determinate')
    my_progress.grid(row=row_tracker, column=column_tracker)
    row_tracker += 1

    button = Button(window, text=f'SEARCH',
                    font=10, padx=10, pady=20, command=myClick_start_search, bg='#b5c3d2', fg='white')
    button.grid(row=row_tracker, column=column_tracker)

welcome_window()

'''def say_hi():
    tkinter.Label(window, text = "Hi").pack()

tkinter.Label(window, text="Click Me!", command = say_hi).pack()'''

p1 = Process(target=window.mainloop())
p1.start()
p2 = Process(target=server)
p2.start()
p1.join()
p2.join()
window.mainloop()