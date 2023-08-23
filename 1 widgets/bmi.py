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

        #*Layout
        self.columnconfigure(0, weight = 1, uniform = 'a')
        self.rowconfigure((0,1,2,3), weight = 1, uniform= 'a')

        #*Widgets
        ResultText(self)
        WeightInput(self)
        HeightInput(self)
        UnitSwitcher(self)

        self.mainloop()

    def change_title_bar_color(self): 
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


class ResultText(ctk.CTkLabel):
    def __init__(self, parent):
        font = ctk.CTkFont(family = FONT, size = MAIN_TEXT_SIZE, weight = 'bold')
        super().__init__(parent, text = 22.5, font = font, text_color = WHITE)
        self.grid(row = 0, column = 0, rowspan = 2, sticky = 'news')

class WeightInput(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color = WHITE)
        self.grid(row = 2, column = 0, sticky = 'enws', padx = 10, pady = 10)

        #* Layout
        self.rowconfigure(0, weight = 1, uniform= 'a')
        self.columnconfigure((0), weight = 2, uniform = 'a')
        self.columnconfigure((1), weight = 1, uniform = 'a')
        self.columnconfigure((2), weight = 3, uniform = 'a')
        self.columnconfigure((3), weight = 1, uniform = 'a')
        self.columnconfigure((4), weight = 2, uniform = 'a')

        #* Label
        font = ctk.CTkFont(family = FONT, size = INPUT_FONT_SIZE)
        label = ctk.CTkLabel(self, text = '70kg', text_color = BLACK, font = font)
        label.grid(row = 0, column = 2)

        #* Buttons
        minus_button_big = ctk.CTkButton(self, 
                                         text= '-', 
                                         font = font, 
                                         text_color = BLACK, 
                                         fg_color = LIGHT_GRAY, 
                                         hover_color = GRAY, 
                                         corner_radius = BUTTON_CORNER_RADIUS)
        
        minus_button_big.grid(row = 0, column = 0, sticky = 'news', padx  = 8, pady  = 8)

        minus_button_small = ctk.CTkButton(self, 
                                         text= '-', 
                                         font = font, 
                                         text_color = BLACK, 
                                         fg_color = LIGHT_GRAY, 
                                         hover_color = GRAY, 
                                         corner_radius = BUTTON_CORNER_RADIUS)
        
        minus_button_small.grid(row = 0, column = 1, padx  = 4, pady  = 4)

        plus_button_big = ctk.CTkButton(self, 
                                         text= '+', 
                                         font = font, 
                                         text_color = BLACK, 
                                         fg_color = LIGHT_GRAY, 
                                         hover_color = GRAY, 
                                         corner_radius = BUTTON_CORNER_RADIUS)
        
        plus_button_big.grid(row = 0, column = 4, sticky = 'news', padx  = 8, pady  = 8)

        plus_button_small = ctk.CTkButton(self, 
                                         text= '+', 
                                         font = font, 
                                         text_color = BLACK, 
                                         fg_color = LIGHT_GRAY, 
                                         hover_color = GRAY, 
                                         corner_radius = BUTTON_CORNER_RADIUS)
        
        plus_button_small.grid(row = 0, column = 3, padx  = 4, pady  = 4)
        
class HeightInput(ctk.CTkFrame):


    def __init__(self,parent):
        super().__init__(parent, fg_color = WHITE)
        self.grid(row = 3, column = 0, sticky = 'news', padx = 10, pady = 10)

        #* Widgets
        slider = ctk.CTkSlider(self,
                               button_color = GREEN,
                               button_hover_color = GRAY,
                               progress_color = GREEN, #! makes left side green
                                fg_color = LIGHT_GRAY) #! makes right side gray
        slider.pack(side = 'left', fill = 'x', expand = True, padx = 10, pady = 10)

        output_text = ctk.CTkLabel(self, text = '1.80m', text_color = BLACK, font = ctk.CTkFont(family = FONT, size = INPUT_FONT_SIZE))
        output_text.pack(side = 'left', padx = 20)

#TODO: create the text in the top right
class UnitSwitcher(ctk.CTkLabel):
    def __init__(self,parent):
        super().__init__(parent, text = 'metric', text_color = DARK_GREEN, font = ctk.CTkFont(family = FONT, size = SWITCH_FONT_SIZE))
        self.place(relx = .95, rely = .01, anchor = 'ne', )
if __name__ == '__main__':
    BMI_APP()