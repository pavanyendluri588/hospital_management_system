import tkinter as tk
from tkinter import ttk
from turtle import width
from urllib import response
from PIL import Image, ImageTk

#private files are importing:
import login_check
#import main_page

class main_window():
    def __init__(self):
       self.root1 = tk.Tk()
       self.screem_width=int(self.root1.winfo_screenwidth())
       self.screem_height=int(self.root1.winfo_screenheight())
       self.root1.geometry(f'{self.screem_width-20}x{self.screem_height-20}+0+0')
       self.root1.resizable(True,True)
       self.root1.title("HMS")
    def login_page(self):
        self.login_page_frame1= tk.Frame(self.root1,width=self.screem_width,height=self.screem_height-5)
        self.login_page_frame1.place(x=0,y=0)

        """
        self.bg = tk.PhotoImage(file = "home_image.png")
  
        # Show image using label
        self.label1 = ttk.Label( self.login_page_frame1, image = self.bg)
        self.label1.place(x = 0, y = 0)
        
        self.image = Image.open('home_image.png')
        self.resize_image = self.image.resize((self.screem_width, self.screem_height))        self.img = ImageTk.PhotoImage(self.resize_image)
        self.img = ImageTk.PhotoImage(self.resize_image)
        # create label and add resize image
        self.label1 = tk.Label(self.login_page_frame1,image=self.img)
        self.label1.image = self.img
        self.label1.place(x=1,y=1)
   
        self.img = tk.PhotoImage(file='home_image.png')
        self.label = tk.Label(self.login_page_frame1,image=self.img,width=self.screem_width,height=self.screem_height)

        self.label.place(x=0, y=0)
        """
        #declaring string variables to store role and reg_id and password
        self.value_inside = tk.StringVar(self.login_page_frame1)
        self.reg_id_var=tk.StringVar(self.login_page_frame1)
        self.password_var=tk.StringVar(self.login_page_frame1)

        self.home_title=tk.Label(self.login_page_frame1,text='HOSPITAL MANAGEMENT SYSTEM',font=('calibre',45,'italic'),fg='green')
        self.home_title.place(x=250, y=200)



        self.role = ttk.Label(self.login_page_frame1,text='user role',font=('calibre',15))
        self.role.place(x=600, y=430)
        self.reg_id = ttk.Label(self.login_page_frame1,text="Reg ID",font=('calibre',15))
        self.reg_id.place(x=600, y=470)
        self.password=ttk.Label(self.login_page_frame1,text='Password',font=('calibre',15))
        self.password.place(x=600, y=510)


        self.value_inside.set('select role')
        self.roles_list = ["Accountant","Clerical Staff","Admin","Doctor","House Keeping","Janitorial Staff","Nurse","Physician","Receptionist"]
        self.role_entry = ttk.OptionMenu(self.login_page_frame1,self.value_inside , *self.roles_list)
        self.role_entry.configure(width=38)

        self.role_entry.place(x=720,y=430)
        print("the valuse on the roles:",self.value_inside.get())

        self.reg_id_entry = tk.Entry(self.login_page_frame1,textvariable= self.reg_id_var,font=('calibre',17)).place(x=720,y=470)
        self.password_entry = tk.Entry(self.login_page_frame1, textvariable = self.password_var, font=('calibre',17),show="*").place(x=720,y=510)
        
        
        
        self.submit_botton = tk.Button(self.login_page_frame1,text='submit',width=13,height=1,bg='red',command=self.login_check_fun)
        #,command=logincheck
        #submit_botton.config(width=50,height=5)
        self.submit_botton.place(x=690,y=570)
        self.reset_button = tk.Button(self.login_page_frame1,text='Reset',width=13,height=1,bg='red',command=self.reser_button_responce)
        #,command=logincheck
        self.reset_button.place(x=840,y=570)
        #role_entry = tk.Entry(root,textvariable=role_var,font=('calibre',17)).place(x=720,y=430)
        self.root1.mainloop()
        

    def reser_button_responce(self):
        self.value_inside.set('select role')
        self.reg_id_var.set('')
        self.password_var.set('')

    def login_check_fun(self):
              print(self.value_inside.get(),self.reg_id_var.get(),self.password_var.get())
              self.response = login_check.username_password_check(login_check.mydb,self.value_inside.get(),self.reg_id_var.get(),self.password_var.get())
              if self.response == 'true':
                       #return  self.response
                       self.login_page_frame1.destroy()
                       self.main_page()
                       
              else:
                       #return  self.response
                       pass

    def main_page(self):
        self.frame_view1=tk.Frame(self.root1,bg='red')
        self.frame_view1.pack(ipadx=770,ipady=20,side='top',fill='y')
        self.frame_view1['borderwidth']=0

        self.frame_view2=tk.Frame(self.root1,bg='yellow')
        self.frame_view2.pack(ipadx=70,ipady=100,side='left',fill='y')
        self.frame_view2['borderwidth']=0



        self.label1= tk.Button(self.frame_view2,text="destroy1")
        self.label1.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label11= tk.Button(self.frame_view2,text="search_button",command=self.search_button)
        self.label11.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label12= tk.Button(self.frame_view2,text="destroy3")
        self.label12.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label13= tk.Button(self.frame_view2,text="destroy4")
        self.label13.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label14= tk.Button(self.frame_view2,text="destroy5")
        self.label14.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label15= tk.Button(self.frame_view2,text="destroy6")
        self.label15.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label16= tk.Button(self.frame_view2,text="destroy7")
        self.label16.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label17= tk.Button(self.frame_view2,text="destroy8")
        self.label17.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        #side='top',


        self.frame_view3=tk.Frame(self.root1,bg='blue')
        self.frame_view3.pack(ipadx=550,ipady=370,side='top')
        self.frame_view3['borderwidth']=0

        self.label2= tk.Label(self.frame_view3,text="frame_view3")
        self.label2.pack(side='left')
        self.label21= tk.Label(self.frame_view3,text="frame_view3")
        self.label21.pack(side='bottom')
        self.label22= tk.Label(self.frame_view3,text="frame_view3")
        self.label22.pack(side='right')
        self.label23= tk.Label(self.frame_view3,text="frame_view3")
        self.label23.pack(side='top')

        self.frame_view4=tk.Frame(self.root1,bg='green')
        self.frame_view4['borderwidth']=0

        self.label3= tk.Label(self.frame_view4,text="frame_view4")
        self.label3.pack(side='left')
        self.label31= tk.Label(self.frame_view4,text="frame_view4")
        self.label31.pack(side='bottom')
        self.label32= tk.Label(self.frame_view4,text="frame_view4")
        self.label32.pack(side='right')
        self.label33= tk.Label(self.frame_view4,text="frame_view4")
        self.label33.pack(side='top')
        self.label1.config(command=self.destroy_frame_view3)

        self.frame_view5=tk.Frame(self.root1,bg='black')
        self.frame_view5['borderwidth']=0

        self.label4= tk.Label(self.frame_view4,text="frame_view5")
        self.label4.pack(side='left')
        self.label41= tk.Label(self.frame_view4,text="frame_view5")
        self.label41.pack(side='bottom')
        self.label42= tk.Label(self.frame_view4,text="frame_view5")
        self.label42.pack(side='right')
        self.label43= tk.Label(self.frame_view4,text="frame_view5")
        self.label43.pack(side='top')
        self.label1.config(command=self.destroy_frame_view3)

    def frames_status(self):

             print("frame_view1 status:",self.frame_view1)
             print("frame_view2 status:",self.frame_view2)
             print("frame_view3 status:",self.frame_view3)
             print("frame_view4 status:",self.frame_view4)
             print("frame_view5 status:",self.frame_view5)
    def search_button(self):
        print("search_button function")
        if self.frame_view4 == None:
                pass
        else:
                self.frame_view4.destroy()
        self.frame_view4 = None
        #self.frame_view4.destroy()
        if self.frame_view5 == None:
            pass
        else:
                  self.frame_view5.pack(ipadx=550,ipady=370,side='top')


    def destroy_frame_view3(self):
             print("destroy_frame_view3 function")
             if self.frame_view3 == None:
                pass
             else:
                self.frame_view3.destroy()
             self.frame_view3 = None
             self.frames_status()
             if self.frame_view4 == None:
                   pass
             else:
                 self.frame_view4.pack(ipadx=550,ipady=370,side='top')
    
    
        
        

  



x=main_window()
x.login_page()
my = login_check.mydb
my.close()

       
     