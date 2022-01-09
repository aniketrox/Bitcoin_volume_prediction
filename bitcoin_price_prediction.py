#==================Importing required Libraries========================#
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import seaborn as sns
#==========================================================================#



#===============making class named volume_prediction====================#

class volume_prediction:
    def __init__(self,root):
        self.root = root
        
        #=============making frame==============#
        self.root.title("Bitcoin Volume Prediction Window")
        self.root.minsize(1200,620+0+0)
        self.root.resizable(0,0)
        
        #===================adding background image=======================#
        path_bg = "bg.jpg"
        self.background = ImageTk.PhotoImage(file=path_bg)
        bg = Label(self.root, image=self.background).place(x=0,y=0,relwidth=1,relheight=1)
        
        
        #===================box image=======================#
        path_box = "box.jpg"
        self.box_image = ImageTk.PhotoImage(file=path_box)
        box = Label(self.root, image=self.box_image).place(x=740,y=35,width=400,height=550)
        
        #========================Prediction Frame===========================#
        pre_frame = Frame(self.root,bg="#FFFAF0").place(x=55,y=35,width=685,height=550)
        
        
            #========================Prediction label===========================#
        pre_title = Label(pre_frame,text="BITCOIN  VOLUME  PREDICTION",font=("candara",20,"bold"),bg="#FFFAF0",fg="#082A47").place(x=90,y=55)
        
            #===============================Open Price & entry field==================================#
        open_value = Label(pre_frame,text="Open Price ($)",font=("candara",15,"bold"),bg="#FFFAF0",fg="gray").place(x=90,y=125)
        self.open_frame= Entry(pre_frame,font=("candara",13),bg="light gray")
        self.open_frame.place(x=90,y=158,width=250)
        
            #===============================Closing Price & entry field==================================#
        close_value = Label(pre_frame,text="Closing Price ($)",font=("candara",15,"bold"),bg="#FFFAF0",fg="gray").place(x=420,y=125)
        self.close_frame= Entry(pre_frame,font=("candara",13),bg="light gray")
        self.close_frame.place(x=420,y=158,width=250)
        
            #===============================Highest Price & entry field==================================#
        high = Label(pre_frame,text="Highest Price ($)",font=("candara",15,"bold"),bg="#FFFAF0",fg="gray").place(x=90,y=198)
        self.high_frame= Entry(pre_frame,font=("candara",13),bg="light gray")
        self.high_frame.place(x=90,y=231,width=250)
        
            #===============================Lowest Price & entry field==================================#
        low = Label(pre_frame,text="Lowest Price ($)",font=("candara",15,"bold"),bg="#FFFAF0",fg="gray").place(x=420,y=198)
        self.low_frame = Entry(pre_frame,font=("candara",13),bg="light gray")
        self.low_frame.place(x=420,y=231,width=250)
        
            #==================================Volume Section==================================#
        self.Current_volume = IntVar()
        volume = Label(pre_frame,text="Predicted Market Volume ($)",font=("candara",15,"bold"),bg="#FFFAF0",fg="gray").place(x=420,y=271)
        self.volume_frame= Label(pre_frame,text="", textvariable=self.Current_volume,font=("candara",13,"bold"),bg="light gray")
        self.volume_frame.place(x=420,y=304,width=250)
        
        
            #===============================Market Cap & entry field==================================#
        cap = Label(pre_frame,text="Market Capital  ($)",font=("candara",17,"bold"),bg="#FFFAF0",fg="gray").place(x=90,y=271)
        self.cap_frame = Entry(pre_frame,font=("candara",13),bg="light gray")
        self.cap_frame.place(x=90,y=304,width=250)
        
          
        
        
        
        #============================Predict button============================#
        self.signup_image = ImageTk.PhotoImage(file="predict.png")
        btn_signup = Button(pre_frame,image=self.signup_image,bd=0,cursor="hand2",width=130,height=37,bg="yellow",command=self.signup).place(x=300,y=405)
        
        
        
         
        
        
        
    #========================Functionality & backend============================#
    
    
    
    
    def clear(self):
        self.open_frame.delete(0,END)
        self.close_frame.delete(0,END)
        self.high_frame.delete(0,END)
        self.low_frame.delete(0,END)
        self.cap_frame.delete(0,END)
    
    
    def signup(self):
        #-----------------------Data Importing-----------------------#
        train_data = pd.read_excel('train.xlsx')
        test_data = pd.read_csv('test.csv')
        #------------------------------------------------------------#

        #-----------------------Training and Testing Data-----------------------#
        train_x = train_data[['Open', 'High', 'Low', 'Close', 'Market Cap']]
        train_y = train_data['Volume']

        test_x = test_data[['Open', 'High', 'Low', 'Close', 'Market Cap']]
        test_y = test_data['Volume']
        #------------------------------------------------------------#
        if self.open_frame.get()=="" or self.close_frame.get()=="" or self.high_frame.get()=="" or self.low_frame.get()=="" or self.cap_frame.get()=="":
            messagebox.showerror("Alert","All fields are required to be filled",parent=self.root)
        else:
            try:
                a = self.open_frame.get()
                b = self.high_frame.get()
                c = self.low_frame.get()
                d = self.close_frame.get()
                e = self.cap_frame.get()
                

                #-----------------------Model And Fitting-----------------------#
                model = linear_model.LinearRegression()
                model.fit(train_x,train_y)
                #------------------------------------------------------------#

                #-----------------------Mean Squared Error-----------------------#
    
                ##test_y_predicted = model.predict(test_x)
                ##mse = mean_squared_error(test_y,test_y_predicted)
                ##print(mse)
    
                #------------------------------------------------------------#
                test_y_predicted = model.predict([[a,b,c,d,e]])
                self.Current_volume.set(int(test_y_predicted))
                self.clear()
            except Exception as es:
                messagebox.showerror("Alert",f"Error occured due to: {str(es)}",parent=self.root)
            
           
    
    
        
root = Tk()
obj = volume_prediction(root)
root.mainloop()
