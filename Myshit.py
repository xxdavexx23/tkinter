import keyboard
while True:
    try:
        if keyboard.is_pressed('s'):
            print("stop")
        elif keyboard.is_pressed('p'):
            print("pause")
    except:
        pass