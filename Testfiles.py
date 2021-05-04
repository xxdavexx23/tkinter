import tkinter as tk
from tkinter import ttk
from tkinter import HORIZONTAL
import math
from PIL import ImageTk, Image
import socket
import time
from multiprocessing import Process
import random, socket, time
import threading
import keyboard
import msvcrt
dev = None
dist = 0
degr = 0
import random
import time
import math
from rssi_receiver import objective_function, PSO,Particle, get_angle
import matplotlib.pyplot as plt

count = 0
s1 = 0

Array1 = [[2, 2, -86], [3.5, 3, -75], [4.5, 4, -75], [4.5, 6, -68], [6, 7, -50]]
Array2 = [[3.5, 2.5, -75], [4, 3, -68], [4.5, 3, -65], [4.5, 3.5, -64], [4.5, 4, -66], [4.5, 5, -66], [4.5, 6.5, -80], [5.5, 6.5, -71], [7, 6.5, -69], [8, 6.5, -68], [4, 6, -52]]
Array3 = [[2, 2.5, -92], [2.5, 2.5, -81], [3.5, 2.5, -83], [4, 3, -95], [4.5, 4, -84], [4.5, 5, -84], [4.5, 6, -72], [5, 6.5, -75], [6, 6.5, -68], [6, 7.5, -61], [6, 8, -61], [6, 9, -60], [6, 10.5, -54]]


#SERVER

def randr(mn, mx, rnd):
    return round(random.random() * (mx - mn) + mn, rnd)


def send_msg(sock, *msgs):
    for msg in msgs:
        msg = bytes(str(msg), 'utf-8')
        sock.sendall(msg)



ip = socket.gethostbyname(socket.gethostname())
port = 45004

s = socket.socket()
s.bind((ip, port))
s.listen(5)
global_rssi = 0

def handle(sock):
    while True:
        msg = str(sock.recv(3), 'utf-8')
        print(msg)
        if msg == 'pu\n' or msg == 'sc\n' or msg == 'sp\n' or msg == 'of\n':
            with open('../ledstrip/python/mode_' + msg[0:2] + '.txt', 'w') as f:
                pass
        if msg == 'qqq' or len(msg) == 0:
            return
port = 46002
def server():
    global global_rssi
    s2 = socket.socket()
    s2.connect(('10.0.0.118',port))

    while True:
        message = str(s2.recv(100),'utf-8')
        message = message.replace('\n', '')
        if message.find('|') == -1:
            continue
        address,rssi = message.split('|')

        if address == 'DD:33:0A:11:1C:87':
            print(address)
            print(rssi)
            global_rssi = int(rssi)

    '''while True:
        print('Listening on {} port {}'.format(ip, port))
        sock, addr = s.accept()
        print('Accepted connection from {}'.format(addr))
        send_msg(s,'battery|80\n')
        handle(sock)
        sock.close()'''
#SERVER

class Device:
    def __init__(self, name, mac_address):
        self._name = name
        self._mac = mac_address
        self._distance = 0

    def last_known_distance(self):
        pass

class ExampleApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.angle = 0
        self.user = 'David'
        self.count_path=0
        self.items=0
        self.distance = 0
        self.path = []
        self.attributes('-fullscreen',True)
        self.my_devices = []
        self.add_device()
        self.label1 = tk.Label(self, text=f'Distance: {self.distance} ', font=10, bg="#FFD670", padx=40, pady=20)
        self.rssi_label = tk.Label(self, text=f'Distance: {global_rssi} ', font=10, bg="#FFD670", padx=40, pady=20)

        #self['background']='#e8c3d2'


    def rotate(self,arr,i):
        '''Animation loop to rotate the line by 10 degrees every 100 ms'''
        try:
            self.label1.destroy()
            self.rssi_label.destroy()
            Array = arr[i]
            self.items +=1
            vector = get_angle(count,s1,Array)
            angle = vector[0]
            self.distance = vector[1]
            print(self.distance)
            a = math.radians(angle)
            r = 50
            x0, y0 = (200,200)
            x1 = x0 + r*math.cos(a)
            y1 = y0 + r*math.sin(a)
            x2 = x0 + -r*math.cos(a)
            y2 = y0 + -r*math.sin(a)
            self.canvas.coords("line", x1,y1,x2,y2)
            #self.after(100, lambda angle=angle+10: self.rotate(angle))
            self.label1 = tk.Label(self, text=f'Distance: {self.distance} ', font=10, bg="#FFD670", padx=40, pady=20)
            time.sleep(5)
            self.label1.pack()

            #return self.distance
        except:
            self.count_path +=1
            self.items =0
            print('path reached')
            pass

    def add_device(self):
        a = Device('keys', 'DD:DA:12:23:34')
        self.my_devices.append(a)
        self.clear_window()
        self.welcome_window()

    def myClick(self):
        self.search_window()


    def welcome_window(self):
        self.choose_path()
        self.background_image = ImageTk.PhotoImage(Image.open('Pictures/pexels-photo-1591447.jpeg'))
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.pack()
        label1 = tk.Label(self, text=f'Welcome: {self.user}', font=10)
        label1.place(x=0, y=0)

        ip = socket.gethostbyname(socket.gethostname())
        port = 45002
        ip_label = tk.Label(self, text=f'IP address: {ip}    Port: {port}', font = 10)
        ip_label.place(x=125,y=50)
        x=250
        y=100
        for i in range(len(self.my_devices)):
            button = tk.Button(self,
                            text=f'Device: {i + 1}  \n {self.my_devices[i]._name} \n Distance:  {self.my_devices[i]._distance}',
                            font=10, padx=10, pady=20, command=self.myClick, bg='#b5c3d2', fg='white')
            button.place(x=x, y=y)
            y+=150

        button = tk.Button(self,
                           text=f'Add a Device',
                           font=10, padx=10, pady=20, command=self.add_device, bg='#b5c3d2', fg='white')
        button.place(x=x, y=y)

    def click_return_welcome(self):
        self.clear_window()
        self.welcome_window()



    def choose_path(self):
        self.items = 0
        if self.count_path % 3 == 0:
            self.path = Array1
        elif self.count_path % 3 == 1:
            self.path = Array2
        elif self.count_path % 3 == 2:
            self.path = Array3
        return self.path



    def clear_window(self):
        for w in self.winfo_children():
            w.destroy()
        self['background']='#FFD670'
        self.update()

    def myClick_start_search(self):

        self.clear_window()
        self.title('Search Window')


        label1 = tk.Label(self, text=f'Searching', font=10, bg="#FFD670", padx=40, pady=20)
        label1.pack()
        my_progress = ttk.Progressbar(self, orient=HORIZONTAL, length=300, mode='determinate')
        my_progress.pack()


        for x in range(5):
            my_progress['value'] += 20
            self.update_idletasks()
            time.sleep(3)
            print('iteration')
            if my_progress['value'] == 100:
                my_progress.stop()
            if keyboard.is_pressed('q'):
                my_progress.stop()
                return self.click_return_welcome()

        self.clear_window()
        label1 = tk.Label(self, text=f'Device 1 looking!', font=10, bg="#ffd770", padx=40, pady=20)
        label1.pack()
        self.canvas = tk.Canvas(self, bg='#ffd770', borderwidth=0, highlightthickness=0)
        self.canvas.pack()
        self.canvas.create_line(0, 50, 100, 100, tags=("line",), arrow="last")



        #label1 = tk.Label(self, text=f'Distance: {self.distance} ', font=10, bg="#FFD670", padx=40, pady=20)
        #label1.pack()

        button = tk.Button(self, text=f'update arrow',
                           font=10, padx=10, pady=20, command= lambda: self.rotate(self.path,self.items), bg='#b5c3d2', fg='white')
        button.pack()
        button = tk.Button(self, text=f'Return to Home',
                           font=10, padx=10, pady=20, command=self.click_return_welcome, bg='#b5c3d2', fg='white')
        button.pack()

    def search_window(self):

        self.clear_window()
        self.title('Search Window')
        #self.restore_background()
        label1 = tk.Label(self, text=f'Begin Searching for Device', font=10, bg="#FFD670", padx=40, pady=20)
        label1.pack()

        button = tk.Button(self, text=f'SEARCH',
                        font=10, padx=10, pady=20, command=self.myClick_start_search, bg='#b5c3d2', fg='white')
        button.pack()


y = threading.Thread(target=server)
y.start()
app = ExampleApp()
x = threading.Thread(target=app.mainloop())
x.start()
