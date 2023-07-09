from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def mySubmit():
    # print('Hello Click')
    # lbl.configure(text='Hello ' + txt.get())
    # txt.delete(0,END)
    # txt.insert(INSERT,'It is a text box')
    # print(chk_status.get())
    # print(rd_status.get())
    # print(cmb.get())
    messagebox.showerror('Error','Wrong')
    messagebox.showinfo('Message Box','This is my message')


win = Tk()
win.geometry('1000x700')
win.title('It is my GUI')
lbl = Label(text = 'It is a Label', foreground = 'red',background = 'light blue',font = ('Arial',20),anchor = 'nw')
lbl.place(x=10, y=10)

txt = Entry(font = ('Arial',20),foreground = 'black',background = 'light grey')
txt.place(x='170',y='10')


btn = Button(text='Dabao yhn',font = ('Arial',15),foreground = 'black',background = 'light green',command = mySubmit)
btn.place(x=10,y=600)

chk_status = BooleanVar()
chk = Checkbutton(text='This is a checkBox',var = chk_status)
chk.place(x='10',y='200')

rd_status = IntVar()
rd1 = Radiobutton(text = 'Python', value = 0, variable = rd_status)
rd1.place(x=150,y=200)
rd2 = Radiobutton(text = 'Java', value = 1,variable = rd_status)
rd2.place(x=250,y=200)

cmb = ttk.Combobox(
     value = [
         'Python',
         'Java',
         'React Native',
         'React JS',
         'C# .net',
         'Flutter'
         ],
    stat = 'readonly',
    font = ('Arial',20)
)
cmb.current(0)
cmb.place(x=10,y=250)

spn = Spinbox(stat = 'readonly', font = ('Arial',20),from_= 10, to = 20)
spn.place(x=10,y=300)

MainMenu = Menu()
New_Project = Menu()
New_Project.add_command(label = 'New Project', command = mySubmit)
New_Project.add_command(label = 'New File', command = mySubmit)
MainMenu.add_cascade(label = 'File',menu = New_Project)
win.config(menu = MainMenu)

tab_obj = ttk.Notebook(width = 200, height = 150)
tab1 = ttk.Frame()
tab_obj.add(tab1,text = 'My Tab 1')

tab2 = ttk.Frame()
tab_obj.add(tab2,text = 'My Tab 2')

tab_obj.place(x=10,y=400)

lbl = Label(tab1,text = 'It is a Label', foreground = 'red',background = 'light blue',font = ('Arial',10),anchor = 'nw')
lbl.place(x=10,y=10)

lbl = Label(tab2,text = 'It is a Label', foreground = 'White',background = 'Black',font = ('Arial',10),anchor = 'nw')
lbl.place(x=10,y=10)


win.mainloop()