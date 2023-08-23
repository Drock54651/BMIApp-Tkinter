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
        self.iconbitmap('5BMI/2 functionality/empty.ico')
        self.resizable(False,False)
        self.change_title_bar_color()

        #*Layout
        self.columnconfigure(0, weight = 1, uniform = 'a')
        self.rowconfigure((0,1,2,3), weight = 1, uniform= 'a')

        #* Data
        self.height_int = ctk.IntVar(value = 170)
        self.weight_float = ctk.DoubleVar(value = 65)
        self.bmi_string = ctk.StringVar()
        self.update_bmi()
    
        #* Tracing
        self.weight_float.trace('w', self.update_bmi)
        self.height_int.trace('w', self.update_bmi)

        
        

        #*Widgets
        ResultText(self, self.bmi_string)
        self.weight_input = WeightInput(self, self.weight_float)
        self.height_input = HeightInput(self, self.height_int)
        UnitSwitcher(self)

        self.mainloop()
    
    def update_bmi(self, *args):
        height_meter = self.height_int.get() /100
        weight_kg = self.weight_float.get() 
        bmi_result = weight_kg / height_meter ** 2
        self.bmi_string.set(round(bmi_result,2))
    


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
    def __init__(self, parent, bmi_string):
        font = ctk.CTkFont(family = FONT, size = MAIN_TEXT_SIZE, weight = 'bold')
        super().__init__(parent, text = 22.5, font = font, text_color = WHITE, textvariable = bmi_string)
        self.grid(row = 0, column = 0, rowspan = 2, sticky = 'news')

class WeightInput(ctk.CTkFrame):
    def __init__(self, parent,weight_float):
        super().__init__(parent, fg_color = WHITE)
        self.grid(row = 2, column = 0, sticky = 'enws', padx = 10, pady = 10)
        self.weight_float = weight_float
        
        #* Layout
        self.rowconfigure(0, weight = 1, uniform= 'a')
        self.columnconfigure((0), weight = 2, uniform = 'a')
        self.columnconfigure((1), weight = 1, uniform = 'a')
        self.columnconfigure((2), weight = 3, uniform = 'a')
        self.columnconfigure((3), weight = 1, uniform = 'a')
        self.columnconfigure((4), weight = 2, uniform = 'a')

        #TODO: update text to display current weight
        self.output_string = ctk.StringVar()
        self.update_weight()


        #* Label
        font = ctk.CTkFont(family = FONT, size = INPUT_FONT_SIZE)
        label = ctk.CTkLabel(self, textvariable = self.output_string, text_color = BLACK, font = font)
        label.grid(row = 0, column = 2)

        
        #* Buttons
        minus_button_big = ctk.CTkButton(self, 
                                         text= '-', 
                                         font = font, 
                                         text_color = BLACK, 
                                         fg_color = LIGHT_GRAY, 
                                         hover_color = GRAY, 
                                         corner_radius = BUTTON_CORNER_RADIUS,
                                         command  = lambda: self.update_weight(('minus','large')))
        
        minus_button_big.grid(row = 0, column = 0, sticky = 'news', padx  = 8, pady  = 8)

        minus_button_small = ctk.CTkButton(self, 
                                         text= '-', 
                                         font = font, 
                                         text_color = BLACK, 
                                         fg_color = LIGHT_GRAY, 
                                         hover_color = GRAY, 
                                         corner_radius = BUTTON_CORNER_RADIUS,
                                         command  = lambda: self.update_weight(('minus','small')))
        
        minus_button_small.grid(row = 0, column = 1, padx  = 4, pady  = 4)

        plus_button_big = ctk.CTkButton(self, 
                                         text= '+', 
                                         font = font, 
                                         text_color = BLACK, 
                                         fg_color = LIGHT_GRAY, 
                                         hover_color = GRAY, 
                                         corner_radius = BUTTON_CORNER_RADIUS,
                                         command  = lambda: self.update_weight(('plus','large')))
        
        plus_button_big.grid(row = 0, column = 4, sticky = 'news', padx  = 8, pady  = 8)

        plus_button_small = ctk.CTkButton(self, 
                                         text= '+', 
                                         font = font, 
                                         text_color = BLACK, 
                                         fg_color = LIGHT_GRAY, 
                                         hover_color = GRAY, 
                                         corner_radius = BUTTON_CORNER_RADIUS,
                                         command  = lambda: self.update_weight(('plus','small')))
        
        plus_button_small.grid(row = 0, column = 3, padx  = 4, pady  = 4)
    
    def update_weight(self, info = None):
        if info:
            

            if info[1] == 'large':
                amount = 1 

            else:
                amount = .1

       

            if info[0] == 'plus':
                self.weight_float.set(self.weight_float.get() + amount)

            else:
                self.weight_float.set(self.weight_float.get() - amount)

        self.output_string.set(f'{round(self.weight_float.get(),2)}kg')

class HeightInput(ctk.CTkFrame):


    def __init__(self,parent, height_int):
        super().__init__(parent, fg_color = WHITE)
        self.grid(row = 3, column = 0, sticky = 'news', padx = 10, pady = 10)
       
        #* Widgets
        slider = ctk.CTkSlider(self,
                               button_color = GREEN,
                               variable = height_int,
                               command = self.update_text,
                               from_= 100,
                               to = 250,
                               button_hover_color = GRAY,
                               progress_color = GREEN, #! makes left side green
                                fg_color = LIGHT_GRAY) #! makes right side gray
        slider.pack(side = 'left', fill = 'x', expand = True, padx = 10, pady = 10)


        self.output_string = ctk.StringVar() #! changes output label according to slider
        self.update_text(height_int.get())

        output_text = ctk.CTkLabel(self, textvariable = self.output_string, text_color = BLACK, font = ctk.CTkFont(family = FONT, size = INPUT_FONT_SIZE))
        output_text.pack(side = 'left', padx = 20)

    def update_text(self, amount):
        
            text_string = str(int(amount))
            meter = text_string[0]
            cm = text_string[1:]
            self.output_string.set(f'{meter}.{cm}m')
        
      


class UnitSwitcher(ctk.CTkLabel):
    def __init__(self,parent):
        super().__init__(parent, text = 'metric', text_color = DARK_GREEN, font = ctk.CTkFont(family = FONT, size = SWITCH_FONT_SIZE))
        self.place(relx = .95, rely = .01, anchor = 'ne', )

    

if __name__ == '__main__':
    BMI_APP()