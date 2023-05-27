import keyboard as kb
import start_window as sw
import threading
import iris_tracking_mouse as it

def keyboard():
        k = kb.Keyboard()
        k.mainloop()


if __name__ == '__main__':

    s = sw.StartWindow()
    s.after(2000, s.destroy)
    s.mainloop()

    t1 = threading.Thread(target=keyboard)
    t1.start()
    t2 = threading.Thread(target=it.eyeTracking())
    t2.start()

    t2.join()
    t1.join()




