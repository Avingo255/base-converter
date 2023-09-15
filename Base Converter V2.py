from tkinter import ttk
from tkinter import messagebox
import time
from tkinter import *
def write(user_list):
    for item in user_list:
        for letter in item:
            print(letter, end='')
            time.sleep(0.01)
        print("")
    

intro_line_list = ["Welcome to My Base Converter!",
                   "I can convert ANYTHING to ANYTHING!",
                   "Have Fun!",
                   "😀😀😂🤣😃😄"]

write(intro_line_list)
    
window = Tk()
window.title("Base Converter")
window.configure(cursor="dotbox")
window.configure(bg='black')
window.geometry('1010x100')
window.minsize(750,100)
Grid.rowconfigure(window, 0, weight=1)
Grid.columnconfigure(window, 0, weight=1)
leftFrame = Frame(window)
secondFrame = Frame(window)
thirdFrame = Frame(window)

leftFrame.grid(row=0,column=0, sticky=N+S+E+W)
secondFrame.grid(row=0,column=1, sticky=N+S+E+W)
thirdFrame.grid(row=0,column=2, sticky=N+S+E+W)


def hexadecimal_to_decimal():
    initial = str(one_entry.get())
    dividend = int(initial,16)
    result.delete(0, END)
    result_number = dividend
    write(initial,"in hexadecimal =",result_number,"in Decimal")
    result.insert(0,result_number)
    print("")    

def numberbases_to_decimal():
    initial = str(one_entry.get())
    dividend = int(initial,int(one_base_options.get()))
    result.delete(0, END)
    result_number = dividend
    print(initial,"in",int(one_base_options.get()),"=",result_number,"in Decimal")
    result.insert(0,result_number)
    print("")
    
def numberbases_to_numberbases():
    initial_one = int(two_base_options.get())
    initial = str(one_entry.get())
    dividend = int(initial,int(one_base_options.get()))
    result_number =""
    divisor = initial_one

    while True:
        quotient = dividend // divisor
        remainder = dividend % divisor
        dividend= quotient
        result_number += str(remainder)
        if dividend == 0:
            break
    result.delete(0, END)
    print(initial,"in base",int(one_base_options.get())," =",result_number[::-1],"in base",divisor)
    result.insert(0,result_number[::-1])
    print("")
    
def decimal_to_hexadecimal():
    print("Decimal to Hexadecimal Conversion")
    hex1_initial = int(one_entry.get())
    hex1_dividend =  hex(hex1_initial)
    hex_result_number = ""
    result.delete(0, END)
    hex_result_number = hex1_dividend
    print(hex1_initial,"in decimal =",hex_result_number,"in Hexadecimal")
    print("")
    write(["N.B. The '0x' part of the result is not acutally hexadecimal.","It is just python putting it there for some reason.","Just pretend it doesn't exist."])
    result.insert(0,hex_result_number)
    print("") 

def begin_conversion():
    if two_base_options.get() == one_base_options.get():
        messagebox.showerror("ERROR", "Oh no! The base you tried to convert to was the same base you tried to convert from!")
    
    elif str(one_base_options.get()) != "Decimal" and str(one_base_options.get()) != "Hexadecimal" and str(two_base_options.get()) == "Hexadecimal":
        messagebox.showwarning("Error","Looks like you're trying to convert something that's not Decimal to Hexadecimal.\nUnfortunately, I can only convert Decimal to Hexadecimal and vice versa. You'll have to do two conversions. Sorry.")
    
    elif str(one_base_options.get()) == "Hexadecimal" and str(two_base_options.get()) != "Hexadecimal" and str(two_base_options.get()) != "Decimal":
        messagebox.showwarning("Error","Looks like you're trying to convert something from Hexadecimal to something that's not Decimal.\nUnfortunately, I can only convert Decimal to Hexadecimal and vice versa. You'll have to do two conversions. Sorry.")      
    
    elif str(two_base_options.get()) == "Hexadecimal" and str(one_base_options.get()) == "Decimal":
        decimal_to_hexadecimal()
    
    elif one_base_options.get() == "Decimal" and two_base_options.get() != "Hexadecimal":
        global initial_one
        initial_one = int(two_base_options.get())
        result_number = ""
        dividend = int(one_entry.get())
        divisor = initial_one

        while True:
            quotient = dividend // divisor
            remainder = dividend % divisor
            dividend= quotient
            result_number += str(remainder)
            if dividend == 0:
                break
        result.delete(0, END)
        print(int(one_entry.get()),"in decimal =",result_number[::-1],"in base",divisor)
        result.insert(0,result_number[::-1])
        print("")
    elif str(two_base_options.get()) == "Decimal" and one_base_options.get() != "Decimal" \
         and one_base_options.get() != "Hexadecimal":
        numberbases_to_decimal()
    elif str(two_base_options.get()) != "Decimal" and one_base_options.get() != "Decimal" \
         and one_base_options.get() != "Hexadecimal"\
         and str(two_base_options.get()) != "Decimal":
        numberbases_to_numberbases()
    elif str(two_base_options.get()) == "Decimal" and one_base_options.get() == "Hexadecimal":
        hexadecimal_to_decimal()
    
    
    else:
        messagebox.showwarning("Error", "Uh Oh! Looks whatever you tried to do wasn't valid. Perhaps you didn't enter a proper base? Maybe try checking your spelling?")
        
    
one_base_text = Text(leftFrame, bg = "grey20", fg = "orange", font = ("Microsoft JhengHei Light",20), height = 1, width = 8)
one_base_text.pack(expand=True,fill='both')
one_base_text.insert('1.0','Convert')

one_base_options = ttk.Combobox(secondFrame,font=("Microsoft JhengHei Light",20), width=7)
one_base_options['values']= (2, 3, 4, 5,6,7,8,9,"Decimal","Hexadecimal")
one_base_options.current(8)
one_base_options.pack(expand=True,fill='both')

one_entry = Entry(thirdFrame,bg="grey30",fg="white",font=("Microsoft JhengHei Light",20), width = 20)
one_entry.pack(expand=True,fill='both')

two_base_text = Text(leftFrame, bg = "grey20", fg = "orange", font = ("Microsoft JhengHei Light",20), height = 1, width = 8)
two_base_text.pack(expand=True,fill='both')
two_base_text.insert('1.0','To Base')

two_base_options = ttk.Combobox(secondFrame,font=("Microsoft JhengHei Light",20), width=7)
two_base_options['values']= (2, 3, 4, 5,6,7,8,9,"Decimal","Hexadecimal")
two_base_options.current(0)
two_base_options.pack(expand=True,fill='both')

divisor_initial = int(two_base_options.get())

result = Entry(thirdFrame,bg="grey30",fg="white",font=("Microsoft JhengHei Light",20), width = 20)
result.pack(expand=True,fill='both')

begin_conversion = Button(window, text="Convert", fg = 'orange', bg = 'grey20', font=("Corbel Light", 28), width = 7,command = begin_conversion)
begin_conversion.grid(row=0, column=3, sticky=N+S+E+W, rowspan=2)

window.mainloop()