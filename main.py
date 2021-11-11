import tkinter
from tkinter import *
from tkinter import filedialog
root = Tk()
root.title('letter for you')
root.geometry('500x500')
root.config(bg="#77ACF1")
panda = []
global T
global ent1,ent2,ent3,ent4,ent5,ent6,ent7,ent8,ent9,ent10
rname = tkinter.StringVar()
radd = tkinter.StringVar()
rdesg = tkinter.StringVar()
sname= tkinter.StringVar()
sadd = tkinter.StringVar()
sdesg = tkinter.StringVar()
date = tkinter.StringVar()
sroll = tkinter.StringVar()
sclass = tkinter.StringVar()
reason = tkinter.StringVar()
instname = tkinter.StringVar()
options= [
    "PERMISSION FOR LEAVE COLLEGE/SCHOOL",
    "INVITATION FOR",
    "LETTER OF APPRECIATION",
    "GET WELL SOON HEALTH RELATED"

]
global count
count=0
def back():
    global ent1, ent2, ent3, ent4, ent5, ent6, ent7, ent8, ent9, ent10

    data=panda[0]
    panda.clear()
    data.destroy()
    ent1.delete(0,"end")
    ent2.delete(0, "end")
    ent3.delete(0, "end")
    ent4.delete(0, "end")
    ent5.delete(0, "end")
    ent6.delete(0, "end")
    ent7.delete(0, "end")
    ent8.delete(0, "end")
    ent9.delete(0,"end" )
    ent10.delete(0, "end")



def delt():
    global labl1, labl2, labl3, labl4, labl5, labl6, labl7, labl8, labl9,lab10
    global ent1, ent2, ent3, ent4, ent5, ent6, ent7, ent8, ent9, ent10
    labl1.destroy()
    labl2.destroy()
    labl3.destroy()
    labl4.destroy()
    labl5.destroy()
    labl6.destroy()
    labl7.destroy()
    labl8.destroy()
    labl9.destroy()
    lab10.destroy()
    ent1.destroy()
    ent2.destroy()
    ent3.destroy()
    ent4.destroy()
    ent5.destroy()
    ent6.destroy()
    ent7.destroy()
    ent8.destroy()
    ent9.destroy()
    ent10.destroy()








def save_file():
    text_file=filedialog.asksaveasfilename(defaultextension=".*",initialdir = "C:\Desktop",filetypes=(("Text Files","*.txt"),("HTML files","*.html"),("PDF files","*,pdf"),("ALL FILES","*.*")))
    if text_file:
        text_file = open(text_file,'w')
        text_file.write(T.get(1.0,END))
        text_file.close
def subt1():
    global T
    global count
    count = 1
    receiver_name = str(rname.get())
    receiver_desg = str(rdesg.get())
    reciever_add = str(radd.get())

    sender_name = str(sname.get())
    sender_desg = str(sdesg.get())
    sender_add = str(sadd.get())
    sender_branch = str(sclass.get())
    sender_roll = str(sroll.get())

    nreason = str(reason.get())

    ndate= str(date.get())
    totdate = str(instname.get())

    data = Toplevel(root)
    data.title("your letter")
    data.geometry("750x600")
    panda.append(data)

    letter = ("""
           To,
           %s
           %s
           %s
           DATE: %s
           Dear Sir/Ma'am
           
           Subject: Permission for leave due to %s
           
           With utmost courtesy, I would like to bring into your kind concern 
           that I am %s and I am studying in %s of your institution  as a student.
           
           I am writing this letter in order to seek your kind permission 
           for approval of  leave for %s days.  Reason being %s. 
           I will not be able to continue my duties for the above said days.  
           
           I ensure I will be joining back after %s days and all my pending work 
           will be covered at the earliest. For any assistance related to work, 
           I will be available on calls/ e-mails.
           
           Kindly consider this as genuine. I shall be highly served.

           Yours Truly,
           %s
           %s

    
    
    
    """%(receiver_name,receiver_desg,reciever_add,ndate,nreason,sender_name,sender_branch,totdate,nreason,totdate,sender_name,sender_desg))

    T = Text(data, height=30, width=90)
    T.insert(tkinter.END,letter)
    savebtn =Button(data,text = "SAVE",command = save_file)
    savebtn.place(x=350,y=500)
    T.pack()
    exitbtn = Button(data,text = "main menu",command = back)
    exitbtn.place(x=500,y=500)


def sub2():
    global T
    global count
    count = 1
    receiver_name = str(rname.get())
    reciever_add = str(radd.get())
    sender_name = str(sname.get())

    sender_add = str(sadd.get())

    event_name = str(sdesg.get())
    event_time = str(sclass.get())
    event_date = str(sroll.get())
    event_venue = str(reason.get())


    ndate = str(date.get())


    data = Toplevel(root)
    data.title("your letter")
    panda.append(data)
    data.geometry("750x600")

    letter= ("""
            From,
            %s
            %s
            
            Date:%s
            
            To,
            %s
            %s
            
            Dear Sir/Ma'am
            
            I am pleased to inform you that are cordially invited to the %s.
            This event will be organized at %s and will
            be held on %s at %s . 
            
            Please make the event more auspicious with your presence.
            
            we look forward to your presence on the event.
            
            Yours Sincerely
            
            %s
            """%(sender_name,sender_add,ndate,receiver_name,reciever_add,event_name,event_venue,event_date,event_time,sender_name))

    T = Text(data, height=30, width=90)
    T.insert(tkinter.END, letter)
    savebtn = Button(data, text="SAVE", command=save_file)
    savebtn.place(x=350, y=500)
    exitbtn = Button(data, text="main menu", command=back)
    exitbtn.place(x=500, y=500)
    T.pack()



def sub5():
    global T
    global count
    count = 1

    receiver_name = str(rname.get())
    reciever_desg = str(rdesg.get())
    sender_name = str(sname.get())
    senders_desg  = str(sdesg.get())
    datee=str(sroll.get())
    comp_name = str(sclass.get())

    data = Toplevel(root)
    data.title("your letter")
    panda.append(data)
    data.geometry("750x600")
    letter = """
    
    %s
    %s
    %s
    
    
    
    %s
    Dear %s
        Subject: APPRECIATION LETTER FOR PERFORMANCE
        
    it is my honour and pleasure to inform you that the organization is impressed 
    with your performance.we are really glad for all the hard work you have done 
    to complete the given work, not only you have done it but we think it was done flawlessly.
    thus as a organization its our responsibility to appreciate such an hardworking person.
    we all are hope you continue working like this and achieve everything you have dreamt of .
    
    Thanking you 
    Yours sincerely
    
    %s
    %s """%(receiver_name,reciever_desg,comp_name,datee,receiver_name,sender_name,senders_desg)

    T = Text(data, height=30, width=90)
    T.insert(tkinter.END, letter)
    savebtn = Button(data, text="SAVE", command=save_file)
    savebtn.place(x=350, y=500)
    exitbtn = Button(data, text="main menu", command=back)
    exitbtn.place(x=500, y=500)
    T.pack()


def sub4():
    global T
    global count
    count = 1

    receiver_name = str(rname.get())
    sender_name = str(sname.get())
    valid = str(reason.get())
    data = Toplevel(root)
    data.title("your letter")
    panda.append(data)
    data.geometry("750x600")
    letter ="""
    Dear %s,

    I just heard  that you are suffering from the %s. 
    I am writing this letter to let you know how sorry I am to hear this. I hope that you will overcome 
    this disease soon but in the meantime, rest as much as possible.
    If you need any help in grocery shopping, cleaning home, cooking then don’t hesitate to call me, 
    I will be the happiest person to help you.
    Just make me a call whenever you need help. I will be there for you within no time.

    Take care, take your medicines in time and listen to what the doctor is saying.

    Yours sincerely,
    
    %s
        
    """%(receiver_name,valid,sender_name)

    T = Text(data, height=30, width=90)
    T.insert(tkinter.END, letter)
    savebtn = Button(data, text="SAVE", command=save_file)
    savebtn.place(x=350, y=500)
    exitbtn = Button(data, text="main menu", command=back)
    exitbtn.place(x=500, y=500)
    T.pack()



def opt1():

    global ent1, ent2, ent3, ent4, ent5, ent6, ent7, ent8, ent9, ent10
    global labl1,labl2,labl3,labl4,labl5,labl6,labl7,labl8,labl9,lab10
    global count
    if count == 1:
        delt()

    labl1 = Label(root, text="Enter Receivers  Name:")
    labl1.place(x=40, y=150)
    ent1 = Entry(root, textvariable=rname)
    ent1.place(x=200, y=150)

    labl2 = Label(root, text="Enter Receivers Designation:")
    labl2.place(x=40, y=180)
    ent2 = Entry(root, textvariable=rdesg)
    ent2.place(x=200, y=180)

    labl3 = Label(root, text="Enter Receivers Address:")
    labl3.place(x=40, y=210)
    ent3 = Entry(root, textvariable=radd)
    ent3.place(x=200, y=210)

    labl4 = Label(root, text="Enter Senders Name:")
    labl4.place(x=40, y=240)
    ent4 = Entry(root, textvariable=sname)
    ent4.place(x=200, y=240)

    labl5 = Label(root, text="Enter Senders Designation:")
    labl5.place(x=40, y=270)
    ent5 = Entry(root, textvariable=sdesg)
    ent5.place(x=200, y=270)

    labl6 = Label(root, text="Enter Senders Address:")
    labl6.place(x=40, y=300)
    ent6 = Entry(root, textvariable=sadd)
    ent6.place(x=200, y=300)

    labl7 = Label(root, text="Enter senders roll number:")
    labl7.place(x=40, y=330)
    ent7 = Entry(root, textvariable=sroll)
    ent7.place(x=200, y=330)

    labl8 = Label(root, text="Enters Senders Class/Branch")
    labl8.place(x=40, y=360)
    ent8 = Entry(root, textvariable = sclass)
    ent8.place(x=200, y=360)

    labl8 = Label(root, text="Enter the DATE (ANY FORMAT)")
    labl8.place(x=40, y=390)
    ent8 = Entry(root, textvariable = date)
    ent8.place(x=230, y=390)

    labl9 = Label(root, text = " Enter your reason")
    labl9.place(x=40,y=420)
    ent9 = Entry(root, textvariable = reason)
    ent9.place(x= 200, y= 420)

    lab10 = Label(root,text= "Enter number of days:")
    lab10.place(x=40, y= 450)
    ent10 = Entry(root, textvariable = instname)
    ent10.place(x=200 , y= 450)

    count = 1
    submit = Button(root, text = "SUBMIT",bg ="yellow",fg="black",command = subt1)
    submit.place(x= 400,y=250)

# to get details for the second option
def opt2():

    global ent1, ent2, ent3, ent4, ent5, ent6, ent7, ent8, ent9, ent10
    global labl1, labl2, labl3, labl4, labl5, labl6, labl7, labl8, labl9,lab10
    global count
    if count == 1:
        delt()

    labl1 = Label(root, text="Enter Receivers  Name:")
    labl1.place(x=40, y=150)
    ent1 = Entry(root, textvariable=rname)
    ent1.place(x=200, y=150)

    labl2 = Label(root, text="Enter Receivers Address:")
    labl2.place(x=40, y=180)
    ent2 = Entry(root, textvariable=radd)
    ent2.place(x=200, y=180)

    labl3 = Label(root, text="Enter senders name:")
    labl3.place(x=40, y=210)
    ent3 = Entry(root, textvariable=sname)
    ent3.place(x=200, y=210)

    labl4 = Label(root, text="Enter Senders Address:")
    labl4.place(x=40, y=240)
    ent4 = Entry(root, textvariable=sadd)
    ent4.place(x=200, y=240)

    labl5 = Label(root, text="Enter date of letter:")
    labl5.place(x=40, y=270)
    ent5 = Entry(root, textvariable=date)
    ent5.place(x=200, y=270)

    labl6 = Label(root, text="Enter Event Name")
    labl6.place(x=40, y=300)
    ent6 = Entry(root, textvariable=sdesg)
    ent6.place(x=200, y=300)

    labl7 = Label(root, text="Enter Event date:")
    labl7.place(x=40, y=330)
    ent7 = Entry(root, textvariable=sroll)
    ent7.place(x=200, y=330)

    labl8 = Label(root, text="Enter the Event Time")
    labl8.place(x=40, y=390)
    ent8 = Entry(root, textvariable=sclass)
    ent8.place(x=200, y=390)

    labl9 = Label(root, text=" Enter Venue Address:")
    labl9.place(x=40, y=420)
    ent9 = Entry(root, textvariable=reason)
    ent9.place(x=200, y=420)

    count = 1
    submit = Button(root, text="SUBMIT", bg="yellow", fg="black", command= sub2)
    submit.place(x=400, y=250)




def opt3():

    #LETTER OF APPRECIATION
    global ent1, ent2, ent3, ent4, ent5, ent6, ent7, ent8, ent9, ent10
    global labl1, labl2, labl3, labl4, labl5, labl6, labl7, labl8, labl9,lab10
    global count
    if count == 1:
        delt()


    labl1 = Label(root, text="Enter Receivers  Name:")
    labl1.place(x=40, y=150)
    ent1 = Entry(root, textvariable=rname)
    ent1.place(x=200, y=150)

    labl2 = Label(root, text="Enter Receivers Designation:")
    labl2.place(x=40, y=180)
    ent2 = Entry(root, textvariable=rdesg)
    ent2.place(x=200, y=180)

    labl3 = Label(root, text="Enter recievers Address:")
    labl3.place(x=40, y=210)
    ent3 = Entry(root, textvariable=radd)
    ent3.place(x=200, y=210)

    labl4 = Label(root, text="Enter Senders Name:")
    labl4.place(x=40, y=240)
    ent4 = Entry(root, textvariable=sname)
    ent4.place(x=200, y=240)

    labl5 = Label(root, text="Enter Senders Designation:")
    labl5.place(x=40, y=270)
    ent5 = Entry(root, textvariable=sdesg)
    ent5.place(x=200, y=270)

    labl7 = Label(root, text="Enter Event date:")
    labl7.place(x=40, y=330)
    ent7 = Entry(root, textvariable=sroll)
    ent7.place(x=200, y=330)


    labl8 = Label(root, text="Enters companies name")
    labl8.place(x=40, y=300)
    ent8 = Entry(root, textvariable=sclass)
    ent8.place(x=200, y=300)

    count = 1

    submit = Button(root, text="SUBMIT", bg="yellow", fg="black", command=sub5)
    submit.place(x=400, y=250)

def opt4():
    #letter for get well soon

    global ent1, ent2, ent3, ent4, ent5, ent6, ent7, ent8, ent9, ent10
    global labl1, labl2, labl3, labl4, labl5, labl6, labl7, labl8, labl9,lab10
    global count
    if count == 1:
        delt()


    labl1 = Label(root, text="Enter Receivers  Name:")
    labl1.place(x=40, y=150)
    ent1 = Entry(root, textvariable=rname)
    ent1.place(x=200, y=150)
    labl2= Label(root,text="Enter the senders name:")
    labl2.place(x=40, y=180)
    ent2 = Entry(root, textvariable=sname)
    ent2.place(x=200, y=180)

    labl3 = Label(root, text="Enter the health issue:")
    labl3.place(x=40, y=210)
    ent3 = Entry(root, textvariable=reason)
    ent3.place(x=200, y=210)
    count = 1

    submit = Button(root, text="SUBMIT", bg="yellow", fg="black", command=sub4)
    submit.place(x=400, y=250)




#selsecting the index of the choice
def choice(val):
    if val == 0:
       opt1()
    elif val == 1:

        opt2()

    elif val == 2:
        opt3()

    elif val == 3:
        opt4()



#getting the selected index
def userin():
    index= options.index(selected.get())
    choice(index)


# main code
selected = StringVar()
selected.set(options[0])

drop = OptionMenu(root,selected,*options)
drop.config(bg="yellow")
drop.pack(pady=20)

subbtn= Button(root,text = "select",command = userin)
subbtn.pack()

root.mainloop()