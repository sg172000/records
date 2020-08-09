from tkinter import *
from PIL import ImageTk
class Record:
    def __init__(self,root):
        self.root=root
        self.root.title=("PATIENT RECORD")
        self.root.geometry("1199x600+100+50")
        #=====bg img======
        self.bg=ImageTk.PhotoImage(file="1.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        #=====add patient frame====
        Frame_patient=Frame(self.root,bg="white")
        Frame_patient.place(x=50,y=80,height=350,width=570)
    

        title=Label(Frame_patient,text="PATIENT RECORD",font=("impact",35,"bold"),bg="white",fg="light blue").place(x=120,y=20)
        new_patient=Button(Frame_patient,text="ADD NEW PATIENT",bg="light blue",fg="white",bd=0,height="4",width="40",font=("times new roman",13)).place(x=100,y=100)
        existing_patient=Button(Frame_patient,text="EXISTING PATIENT",bg="light blue",fg="white",bd=0,height="4",width="40",font=("times new roman",13)).place(x=100,y=200)
    


        
root=Tk()
obj=Record(root)
root.mainloop()