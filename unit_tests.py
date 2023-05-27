import unittest
import tkinter as tk
import keyboard as kb
import settings as st

class TestMyApplication(unittest.TestCase):
    def setUp(self):
        self.app = kb.Keyboard()

    def test_select(self):
        for key in self.app.keys:
            exceptions = ['ALT', 'CLEAR', 'SPACE', 'READ', 'settings', 'Backspace', 'Enter', 'CORRECT']
            if key not in exceptions:
                self.app.select(key)
                self.assertEqual(self.app.text_box.get(1.0), key)
                self.app.text_box.delete(1.0)

    def test_textbox_deactivation(self):
        self.app.text_box.insert(tk.INSERT, 'lorem ipsum')
        self.assertNotEqual(self.app.text_box.get(1.0, tk.END), 'lorem ipsum\n')

    def test_backspace(self):
        self.app.text_box.configure(state="normal")
        self.app.text_box.insert(tk.INSERT, 'lorem ipsum')
        self.app.select('Backspace')
        self.app.text_box.configure(state="disabled")
        self.assertEqual(self.app.text_box.get(1.0, tk.END), 'lorem ipsu\n')

    def test_clear(self):
        self.app.text_box.configure(state="normal")
        self.app.text_box.insert(tk.INSERT, 'lorem ipsum')
        self.app.select('CLEAR')
        self.app.text_box.configure(state="disabled")
        self.assertEqual(self.app.text_box.get(1.0, tk.END), '\n')

    def test_correct_eng(self):
        self.app.text_box.configure(state="normal")
        self.settings = st.Settings(self.app)
        self.settings.change_language("ENGLISH")
        self.app.text_box.insert(tk.INSERT, 'THYS IS A TETS OF TWXT CORRECTIOON')
        self.app.select("CORRECT")
        self.assertEqual(self.app.text_box.get(1.0, tk.END), 'THIS IS A TEST OF TEXT CORRECTION\n\n')

    def test_correct_pl(self):
        self.app.text_box.configure(state="normal")
        self.settings = st.Settings(self.app)
        self.settings.change_language("POLISH")
        self.app.text_box.insert(tk.INSERT, 'TO JEEST TETS KOREKCI TEKSSTU')
        self.app.select("CORRECT")
        self.assertEqual(self.app.text_box.get(1.0, tk.END), 'TO JEST TEST KOREKCJI TEKSTU\n\n')

    def test_tts_lang_changeToEn(self):
        self.settings = st.Settings(self.app)
        self.settings.change_language("ENGLISH")
        self.assertEqual(self.app.tts.language, "en_GB")

    def test_tts_lang_changeToPl(self):
        self.settings = st.Settings(self.app)
        self.settings.change_language("POLISH")
        self.assertEqual(self.app.tts.language, "pl_PL")

    def test_update_volume_DOWN(self):
        self.settings = st.Settings(self.app)
        previous = self.app.tts.volume
        self.settings.update_volume("DOWN")
        if previous > 0.01:
            self.assertLess(self.app.tts.volume, previous)
        else:
            self.assertEqual(self.app.tts.volume, previous)

    def test_update_volume_UP(self):
        self.settings = st.Settings(self.app)
        self.settings.update_volume("DOWN")
        self.settings.update_volume("DOWN")
        #reduce volume, maximum volume won't check if UP command works
        previous = self.app.tts.volume
        self.settings.update_volume("UP")
        if previous < 1:
            self.assertGreater(self.app.tts.volume, previous)
        elif previous == 1:
            self.assertEqual(self.app.tts.volume, previous)

    def test_update_rate_SLOW(self):
        self.settings = st.Settings(self.app)
        previous = self.app.tts.rate
        self.settings.update_rate("SLOW")
        if previous > 70:
            self.assertLess(self.app.tts.rate, previous)
        else:
            self.assertEqual(self.app.tts.rate, previous)

    def test_update_rate_FAST(self):
        self.settings = st.Settings(self.app)
        previous = self.app.tts.rate
        self.settings.update_rate("FAST")
        if previous < 330:
            self.assertGreater(self.app.tts.rate, previous)
        else:
            self.assertEqual(self.app.tts.rate, previous)

    def tearDown(self):
        self.app.destroy()


if __name__ == '__main__':
    unittest.main()
