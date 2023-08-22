import ttkbootstrap as ttk
import customtkinter as ctk
from settings import * #! imports everything from settings
try:
    from ctypes import windll, byref, c_int, sizeof
except:
    pass    

class BMI_APP(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color= GREEN)

        self.title('')
        self.geometry('400x400')
        self.iconbitmap('PythonTkinter/5BMI/0 window setup/empty.ico')
        self.resizable(False,False)
        self.change_title_bar_color()

        self.mainloop()

    def change_title_bar_color(self): #TODO: implement this and make sure it does not crash on other OS as this only works on windows
        try:

            HWND = windll.user32.GetParent(self.winfo_id())
            color  = TITLE_HEX_COLOR

            windll.dwmapi.DwmSetWindowAttribute(
                HWND,
                35,
                byref(c_int(color)),
                sizeof(c_int)
            )
        except:
            pass
        
if __name__ == '__main__':
    BMI_APP()