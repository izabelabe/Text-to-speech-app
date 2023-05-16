import keyboard as kb
import start_window as sw
import eye_tracking_mouse as et
import iris_tracking_mouse as it
import threading


def keyboard(finish_event):
        k = kb.Keyboard(finish_event)
        k.mainloop()


if __name__ == '__main__':
    s = sw.StartWindow()
    s.after(2000, s.destroy)
    s.mainloop()

    event = threading.Event()

    t1 = threading.Thread(target=keyboard, args=(event,))
    t1.start()
    t2 = threading.Thread(target=it.eyeTracking())
    t2.start()

    t2.join()
    event.set()
    t1.join()


