import time

import keyboard as kb
import start_window as sw


if __name__ == '__main__':
    s = sw.StartWindow()
    s.after(2000, s.destroy)
    s.mainloop()
    k = kb.Keyboard()
    k.mainloop()

