from tkinter import*


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
        #label1name = Label(window, text = f'Device: {i+1}  {my_devices[i]._name}', font = 5, )
        #label1name.grid(row=row_tracker, column=column_tracker)
        #row_tracker += 1
        #label2name = Label(window, text = f'Distance:  {my_devices[i]._distance}', font = 5)
        #label2name.grid(row=row_tracker, column=column_tracker)
        #row_tracker += 1


    #button = Button(window, text='submit', padx=10, pady=20, command=myClick, bg='blue', fg='white')
    #button.grid(row=row_tracker, column=column_tracker)

def search_window(window):
    for w in window.winfo_children():
        w.destroy()
    window.title('Search Window')
    column_tracker = 0;
    row_tracker = 0;
    label1 = Label(window, text= f'Begin Searching for Device', font = 10 ,bg= "#e8c3d2", padx = 40, pady=20)
    label1.grid(row = row_tracker, column=column_tracker)
    column_tracker += 1
    row_tracker +=1
    button = Button(window, text=f'SEARCH',
                    font=10, padx=10, pady=20, command=myClick, bg='#b5c3d2', fg='white')
    button.grid(row=row_tracker, column=column_tracker)

welcome_window()

'''def say_hi():
    tkinter.Label(window, text = "Hi").pack()

tkinter.Label(window, text="Click Me!", command = say_hi).pack()'''



window.mainloop()