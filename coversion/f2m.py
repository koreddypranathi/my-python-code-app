from tkinter import Tk,Button,Label,DoubleVar,Entry

window=Tk()
window.title("feet to meter conversion app")
window.configure(background="pink")
window.geometry('328x328')
window.resizable(width=False,height=True)
def convert():
    val=float(ft_entry.get())
    meter=val*0.3848
    mt_value.set("%.4f" % meter)
def clear():
    mt_entry.delete(0,"end")
    ft_entry.delete(0,"end")

ft_lbl = Label(window,text="Feet",bg="purple",fg="white",width=14)
ft_lbl.grid(column=0,row=0,padx=15,pady=15)
ft_value=DoubleVar()
ft_entry=Entry(window,textvariable=ft_value,bg="purple",fg="white",width=14)
ft_entry.grid(column=1,row=0)
ft_entry.delete(0,'end')
mt_value=DoubleVar()
mt_lbl=Label(window,text="Meter",bg="purple",fg="white",width=14)
mt_lbl.grid(column=0,row=1,padx=15,pady=15)
mt_entry=Entry(window,textvariable=mt_value,bg="purple",fg="white",width=14)
mt_entry.grid(column=1,row=1)
mt_entry.delete(0,'end')
c_btn=Button(window,text="convert",bg="purple",fg="white",width=14,command=convert)
c_btn.grid(column=0,row=3,padx=15,pady=40)
cl_btn=Button(window,text="clear",bg="purple",fg="white",width=14,command=clear)
cl_btn.grid(column=1,row=3,padx=15,pady=40)





















window.mainloop()
