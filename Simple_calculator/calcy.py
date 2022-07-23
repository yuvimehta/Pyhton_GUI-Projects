from tkinter import *
global operation
global equation 
root = Tk()
root.title("Tutorial Calculator")
entry = Entry(root, width= 20, borderwidth=5)
entry.grid(row= 0, column= 0, columnspan=3, padx= 10, pady= 10)





def button_add(number):
    first_number = entry.get()
    entry.delete(0,END)
    entry.insert(0,str(first_number)+ str(number))

    return

def clear():
    entry.delete(0, END)


def equal():
    global equation
    equation = entry.get()
    if operation == "addition":
        values = equation.split("+")
        
        for i in range(len(values)):
            ans = float(values[i-1])
            ans += float(values[i])
    if operation == "multiply":
        values = equation.split("*")
        for i in range(len(values)):
            ans = float(values[i-1])
            ans *= float(values[i])

    if operation == "minus":
        values = equation.split("-")
        
        rang = len(values)
        for i in range(len(values)):

            ans = float(values[i-1])
            ans -= float(values[i])

    if operation == "divide":
        values = equation.split("/")
        ans = 1
        for i in range(len(values)):
            ans = float(values[i-1])
            ans /= float(values[i])
        
    entry.delete(0,END)
    entry.insert(0,str(ans))

def add(number):
    button_add(number)
    global operation
    operation = "addition"

def multiply(number):
    button_add(number)
    global operation
    operation = "multiply"

def divide(number):
    button_add(number)
    global operation
    operation = "divide"

def minus(number):
    button_add(number)
    global operation
    operation = "minus"
def backspace():
    equation = entry.get()
    entry.delete(len(equation)-1,len(equation))
    return



button_1 =  Button(root,text="1", padx= 20,pady=15, command= lambda: button_add(1)).grid(row=4, column=0)
button_2 =  Button(root,text="2", padx= 20,pady=15, command=lambda: button_add(2)).grid(row=4, column=1)
button_3 =  Button(root,text="3", padx= 20,pady=15, command= lambda: button_add(3)).grid(row=4, column=2)
button_4 =  Button(root,text="4", padx= 20,pady=15, command= lambda: button_add(4)).grid(row=3, column=0)
button_5 =  Button(root,text="5", padx= 20,pady=15, command= lambda: button_add(5)).grid(row=3, column=1)
button_6 =  Button(root,text="6", padx= 20,pady=15, command= lambda: button_add(6)).grid(row=3, column=2)
button_7 =  Button(root,text="7", padx= 20,pady=15, command= lambda: button_add(7)).grid(row=2, column=0)
button_8 =  Button(root,text="8", padx= 20,pady=15, command= lambda: button_add(8)).grid(row=2, column=1)
button_9 =  Button(root,text="9", padx= 20,pady=15, command= lambda: button_add(9)).grid(row=2, column=2)
button_0 =  Button(root,text="0", padx= 55,pady=15, command= lambda: button_add(0)).grid(row=5, column=0,columnspan=2)
button_EQ = Button(root,text="=", padx=20,pady=40, command= equal).grid(row=4, column=3,rowspan=2)
button_AD = Button(root,text="+", padx= 20,pady=40, command= lambda: add("+")).grid(row=2, column=3,rowspan=2)
button_CL = Button(root,text="cl", padx= 20,pady=15, command= clear).grid(row=1, column=0)
button_ML = Button(root,text="*", padx= 20,pady=15, command=lambda: multiply("*")).grid(row=1,column=1)
button_DI = Button(root,text="/ ", padx= 20,pady=15, command= lambda: divide("/")).grid(row=1,column=2)
button_PO = Button(root,text=". ", padx= 20,pady=15, command= lambda: button_add(".")).grid(row=5,column=2)
button_MIN = Button(root,text="- ", padx= 20,pady=15, command= lambda: minus("-")).grid(row=1,column=3)
button_BS = Button(root,text="BS", padx= 15,pady=15, command=  backspace).grid(row=0,column=3)
    


    

root.mainloop()