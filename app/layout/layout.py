from ttkbootstrap import Frame, Label, Button, Image, ImageTk, PhotoImage, Entry, StringVar, Labelframe, DoubleVar
from ttkbootstrap.tooltip import ToolTip
from customtkinter import CTkButton

from app.database.data import *
from app.utils.process import *


class Window(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=2)
        self.master.rowconfigure(1, weight=5)
        self.master.rowconfigure(2, weight=2)
        self.master.rowconfigure(3, weight=2)
        self.vin = DoubleVar()
        self.vo = DoubleVar()
        self.io = DoubleVar()
        self.f = DoubleVar()
        self.n = DoubleVar()
        self.alpha = DoubleVar()
        self.b = DoubleVar()
        self.ku = DoubleVar()
        self.vd = DoubleVar()
        self.data = {}
        self.frame_one = Frame(self.master, height=100, width=800)
        self.frame_two_one = Frame(self.master, height=200, width=800)
        self.frame_two_two = Frame(self.master, height=200, width=800)
        self.frame_two_three = Frame(self.master, height=200, width=800)
        self.frame_three_one = Frame(self.master, height=100, width=800)
        self.frame_three_two = Frame(self.master, height=100, width=800)
        self.frame_three_three = Frame(self.master, height=100, width=800)
        self.frame_fourth = Frame(self.master, height=100, width=800)
        self.logo_ud = ImageTk.PhotoImage(Image.open(
            "app/assets/UD_LOGO.jpg").resize((100, 100)))
        self.three_phase_transformer_image = ImageTk.PhotoImage(Image.open("app/assets/three_phase_transformer.png").resize((400, 250)))
        self.widgets()
        self.reset_form()
    
    def widgets(self):

        self.frame_one.grid(column=0, row=0, sticky="nsew")
        self.frame_one.columnconfigure([0, 1, 2], weight=1)
        self.frame_one.rowconfigure(0, weight=1)

        self.frame_two_one.grid(column=0, row= 1, sticky="nsew")
        self.frame_two_one.columnconfigure([0,1], weight = 1)
        self.frame_two_one.rowconfigure(0, weight=1)

        self.frame_two_two.grid(column=0, row=1, sticky="nsew")
        self.frame_two_two.columnconfigure(0, weight=1)
        self.frame_two_two.columnconfigure(1, weight=3)
        self.frame_two_two.columnconfigure(2, weight=1)
        self.frame_two_two.columnconfigure(3, weight=1)
        self.frame_two_two.rowconfigure(
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], weight=1)

        self.frame_two_three.grid(column=0, row=1, sticky="nsew")
        self.frame_two_three.columnconfigure(0, weight=2)
        self.frame_two_three.columnconfigure(1, weight=1)
        self.frame_two_three.columnconfigure(2, weight=2)
        self.frame_two_three.columnconfigure(3, weight=1)
        self.frame_two_three.rowconfigure(
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12], weight=1)

        self.frame_three_one.grid(column=0, row=2, sticky="nsew")
        self.frame_three_one.columnconfigure(0, weight=1)
        self.frame_three_one.rowconfigure(0, weight=1)

        self.frame_three_two.grid(column=0, row=2, sticky="nsew")
        self.frame_three_two.columnconfigure([0, 1], weight=1)
        self.frame_three_two.rowconfigure(0, weight=1)

        self.frame_three_three.grid(column=0, row=2, sticky="nsew")
        self.frame_three_three.columnconfigure([0,1], weight=1)
        self.frame_three_three.rowconfigure(0, weight=1)

        self.frame_fourth.grid(column=0, row=3, sticky="nsew")
        self.frame_fourth.columnconfigure([0,1], weight=1)
        self.frame_fourth.rowconfigure(0, weight=1)

        Label(self.frame_one, text="photo_UD",
              image=self.logo_ud).grid(column=0, row=0)
        Label(self.frame_one, text='Three-Phase Transformer Design',
              background='white', font=('black', 30, "bold")).grid(column=1, row=0)
        Label(self.frame_fourth, text='Universidad Distrital Francisco José de Caldas',
              background='white', font=('black', 12, "bold"), ).grid(column=0, row=0)
        Label(self.frame_fourth, text='Mateo Salamanca Pulido - 20211005107 \nMichael Andres Olivares Herrera - 20212005063', background='white', font=('black', 12, "bold")).grid(column=1, row=0)
        self.frame_two_one.tkraise()
        self.frame_three_one.tkraise()
        self.step_one()
        
    def step_one(self):
        CTkButton(self.frame_three_one, text='Start', command=lambda: (self.frame_two_two.tkraise(), self.frame_three_two.tkraise(), self.step_two()), font=('white', 12, 'bold')).grid(
            column=0, row=0, ipadx=10, ipady=10)
        Label(self.frame_two_one, text=step_one_information_english["description"], width=40, justify="right").grid(column=0, row=0)
        Label(self.frame_two_one, text="photo_transformer", image=self.three_phase_transformer_image).grid(column=1, row=0)
        
        
    def step_two(self):

        CTkButton(self.frame_three_two, text='Back', command=lambda: (self.frame_two_one.tkraise(), self.frame_three_one.tkraise()),  fg_color="gray").grid(
            column=0, row=0, ipadx=10, ipady=10)
        CTkButton(self.frame_three_two, text='Calculate', command=self.calculate).grid(
            column=1, row=0, ipadx=10, ipady=10)
         # validate number entry
        vcmd = self.master.register(self.validate)
        ivcmd = self.master.register(self.on_invalid)
        for index, _input in enumerate(input_magnitudes):
            Label(
                    self.frame_two_two,
                    text=_input,
                    padding=1,
                    justify='right'
                ).grid(column=0, row=index, sticky='nse', pady=1, padx=2)
            if index == 3:
                Label(self.frame_two_two, text=static_values_english[0]).grid(
                column=1, row=index, sticky='nsew')
            elif index == 4:
                Label(self.frame_two_two, text=static_values_english[1]).grid(
                column=1, row=index, sticky='nsew')
            elif index == 9:
                Label(self.frame_two_two, text=static_values_english[2]).grid(
                column=1, row=index, sticky='nsew')
            else:
                entry = Entry(
                    self.frame_two_two,
                    textvariable=getattr(self, variables_magnitudes[index]),
                    validate='focusout',
                    validatecommand=(vcmd, '%P'),
                    invalidcommand= ivcmd,
                    )
                entry.grid(column=1, row=index, sticky='nsew')
                ToolTip(entry, text="Only numbers")



    def step_three(self):
        dic1 = dict(list(self.data.items())[(len(self.data) + 1)//2:])
        dic2 = dict(list(self.data.items())[:(len(self.data) + 1)//2])
        dic_unit = dict_for_units(output_magnitudes, list_units)
        count = 0
        count_aux = 0
        CTkButton(self.frame_three_three, text='Recalculate', command=lambda: (self.frame_two_two.tkraise(), self.frame_three_two.tkraise(), self.reset_form()),  fg_color="gray").grid(
            column=0, row=0, ipadx=10, ipady=10)
        CTkButton(self.frame_three_three, text='Finish', command=lambda: self.master.quit()).grid(column=1, row=0, ipadx=10, ipady=10)
        for _key in dic2:
            Label(self.frame_two_three, text=_key, font=("black", 12, "bold")).grid(column=0, row= count, sticky='nse')
            if str(dic_unit[_key]) == "":
                value = str(dic2[_key]) + str(dic_unit[_key])
            else:
                value = str(dic2[_key]) + " [" + str(dic_unit[_key]) + "]"
            Label(self.frame_two_three, text=value).grid(column=1, row= count, sticky='nsew')
            count += 1
        for _key in dic1:
            Label(self.frame_two_three, text=_key, font=("black", 12, "bold")).grid(column=2, row= count_aux, sticky='nse')
            if str(dic_unit[_key]) == "":
                value = str(dic1[_key]) + str(dic_unit[_key])
            else:
                value = str(dic1[_key]) + " [" + str(dic_unit[_key]) + "]"
            Label(self.frame_two_three, text=value).grid(column=3, row= count_aux, sticky='nsew')
            count_aux += 1
        
    def calculate(self):
        try:
            if self.vin.get() == 0.0 or self.vo.get() == 0.0 or self.io.get() == 0.0 or self.f.get() == 0.0 or self.n.get() == 0.0 or self.alpha.get() == 0.0 or self.b.get() == 0.0 or self.ku.get() == 0.0 or self.vd.get() == 0.0:
                Label(self.frame_two_two, text="Has a empty fields, please check").grid(column=0, columnspan=2, row=12)
            else:
                data = {
                "Input Voltage": self.vin.get(),
                "Output Voltage": self.vo.get(),
                "Output Current": self.io.get(),
                "Frequency": self.f.get(),
                "Efficiency": self.n.get(),
                "Regulation": self.alpha.get(),
                "Flux Density": self.b.get(),
                "Window Utilization": self.ku.get(),
                "Diode Drop": self.vd.get()
                }
                self.data = calculus(data, "en")
                self.step_three()
                self.frame_two_three.tkraise()
                self.frame_three_three.tkraise()
        except: 
            Label(self.frame_two_two, text="Has a empty fields, please check", font=("red", 12), foreground="red").grid(column=0, columnspan=2, row=12)

    def validate(self, number):
        if number == "0.0":
            return False
        elif number.isdigit():
            return True
        elif str(number).replace('.','',1).isdigit():
            return True
        else:
            return False

    def on_invalid(self):
        print('index ')

    def reset_form(self):
        self.vin.set("")
        self.vo.set("")
        self.io.set("")
        self.f.set("")
        self.n.set("")
        self.alpha.set("")
        self.b.set("")
        self.ku.set("")
        self.vd.set("")
        self.data = {}

