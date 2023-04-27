import tkinter
from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import ImageTk, Image

con=mysql.connector.connect(host='localhost', user='sqluser',password='password',db='registration')
cur=con.cursor(buffered=True)

window = tkinter.Tk()
'''
img1=Image.open('D:\Computer_project_tkinter\job_pics\login1fi.png')
photo=ImageTk.PhotoImage(img1)
bg_panel=Label(window,image=photo)
bg_panel.image=photo
bg_panel.pack(fill='both',expand='yes')'''
window.configure(bg='#FFB5C5')
window.title("Login form")
window.geometry('2000x1000')


 
def login():
    username = "user"
    password = "pass"
    if username_entry.get()==username and password_entry.get()==password:
        window.destroy()
        window2= Tk()
        window2['bg']='grey'
        window2.geometry("1500x800")
        img=Image.open('D:\Computer_project_tkinter\job_pics\wind2fin.png')
        photo1=ImageTk.PhotoImage(img)
        bg1=Label(window2,image=photo1)
        bg1.image=photo1
        bg1.pack(fill='both',expand='yes')
        
   
        def openNewWindow1(): 
            def linkwindow1():
                def openlastWindow1():
                    lastWindow1 = Toplevel(window2)
                    lastWindow1.title("New Window 1")
                    lastWindow1.geometry("1500x800")
                    linkwindow1.destroy()
                    img10=Image.open('D:\Computer_project_tkinter\job_pics\lastfin2.png')
                    photo10=ImageTk.PhotoImage(img10)
                    bg10=Label(lastWindow1,image=photo10)
                    bg10.image=photo10
                    bg10.pack(fill='both',expand='yes')

                addReg="insert into engineering(name, DOB, contact_no, gender, address, email, 12th_grade, skills, languages, Branch, CGPA) values ('" + en1.get() + "','"
                addReg= addReg + en3.get() + "',"
                addReg= addReg + en4.get() + ",'"
                addReg= addReg + var.get() + "','"
                addReg= addReg + en6.get() + "','"
                addReg= addReg + en7.get() + "',"
                addReg= addReg + en8.get() + ",'"
                addReg= addReg + en9.get() + "','"
                addReg= addReg + en10.get() + "','"
                addReg= addReg + en11.get() + "',"
                addReg= addReg + en12.get() + ");"
                #addReg="insert into job(name, DOB, contact_no, gender, address, email, 12th_grade, skills, languages, Branch, CGPA) values ('" + en1.get()+ "',"+
                #,",en3.get(),en4.get(),var.get(),en6.get(),en7.get(),en8.get(),en9.get(),en10.get(),en11.get(),en12.get());"
                print(addReg)
                cur.execute(addReg)
                con.commit()
                linkwindow1= tkinter.Toplevel(window2)
                linkwindow1.title("New Window")
                linkwindow1.geometry("1500x800")
                newWindow1.destroy()
                imag4=Image.open('D:\Computer_project_tkinter\job_pics\link.png')
                photo04=ImageTk.PhotoImage(imag4)
                bg4=Label(linkwindow1,image=photo04)
                bg4.image=photo04
                bg4.pack(fill='both',expand='yes')
                var11=StringVar()
                var11.set("radio1")
                Label(linkwindow1,text ="COMPANIES OFFERED",font=("Arial",10 )).pack()
                Radio1=Radiobutton(linkwindow1, text="Bosch ENGINEERING",command=openlastWindow1, padx=5,font=("Arial",15 ),variable=var11, value="MH").place(x=180, y=250)  
                Radio1=Radiobutton(linkwindow1, text="Infosys PVT.LMT",command=openlastWindow1, padx =10,font=("Arial",15 ),variable=var11, value="Infosys").place(x=180,y=400)  
                Radio1=Radiobutton(linkwindow1, text="Wipro ENGINEERS",command=openlastWindow1, padx=15,font=("Arial",15 ), variable=var11, value="THL").place(x=180,y=550)
                
                
                #Label(linkwindow1,text ="links for engineering").pack()
                
                
            newWindow1 = tkinter.Toplevel(window2)
            newWindow1.title("New Window")
            
            newWindow1.geometry("1500x800")
            
            #tkinter.Label(newWindow1,text ="Engineering").pack()
            
            newWindow1['bg']='snow'
            img1=Image.open('D:\Computer_project_tkinter\job_pics\Engipic2png.png')
            photo=ImageTk.PhotoImage(img1)
            bg_panel=Label(newWindow1,image=photo)
            bg_panel.image=photo
            bg_panel.pack(fill='both',expand='yes')
            lb1= tkinter.Label(newWindow1, text="Name", width=10, font=("arial",12))
            lb1['bg']='white'
            lb1.place(x=20, y=120)  
            en1= tkinter.Entry(newWindow1)
            en1.place(x=200, y=120)  
 
            lb3= tkinter.Label(newWindow1, text="DOB", width=10, font=("arial",12)) 
            lb3['bg']='white' 
            lb3.place(x=19, y=160)  
            en3= tkinter.Entry(newWindow1)  
            en3.place(x=200, y=160)  
 
            lb6= tkinter.Label(newWindow1, text="Enter Email", width=13,font=("arial",12)) 
            lb6['bg']='white'
            lb6.place(x=19, y=320)  
            en6= tkinter.Entry(newWindow1)  
            en6.place(x=200, y=320)  
 
            lb4= tkinter.Label(newWindow1, text="Contact Number", width=13,font=("arial",12)) 
            lb4.place(x=19, y=200) 
            lb4['bg']='white'  
            en4= tkinter.Entry(newWindow1)  
            en4.place(x=200, y=200)  
 
            lb7= tkinter.Label(newWindow1, text="Address", width=15,font=("arial",12))  
            lb7.place(x=21, y=360)  
            lb7['bg']='white' 
            en7 =tkinter.Entry(newWindow1)  
            en7.place(x=200, y=360)  
 
 
            lb5= tkinter.Label(newWindow1, text="Select Gender", width=15, font=("arial",12))  
            lb5.place(x=5, y=240) 
            lb5['bg']='white'  
            var = StringVar()
            var.set("Radio")
            radio=tkinter.Radiobutton(newWindow1, text="Male", padx=5,variable=var,value="Male").place(x=180,y=240)  
            radio=tkinter.Radiobutton(newWindow1, text="Female", padx=10,variable=var,value="Female").place(x=240,y=240)  
            radio=tkinter.Radiobutton(newWindow1, text="Other", padx=15, variable=var,value="Other").place(x=310,y=240)
 
            lb8= tkinter.Label(newWindow1, text="12 th grade(%)", width=15,font=("arial",12))  
            lb8.place(x=19, y=390) 
            lb8['bg']='white' 
            en8= tkinter.Entry(newWindow1)  
            en8.place(x=200, y=390)
 
            lb9= tkinter.Label(newWindow1, text="Skills", width=13,font=("arial",12))  
            lb9.place(x=19, y=430)
            lb9['bg']='white' 
            en9= tkinter.Entry(newWindow1)  
            en9.place(x=200, y=430)
 
            lb10= tkinter.Label(newWindow1, text="Languages known",font=("arial",12)) 
            lb10['bg']='white' 
            lb10.place(x=19, y=480)  
            en10= tkinter.Entry(newWindow1)  
            en10.place(x=200, y=480)
 
            lb11= tkinter.Label(newWindow1, text="Branch of engineering", width=16,font=("arial",12))  
            lb11.place(x=23, y=520) 
            lb11['bg']='white' 
            en11= tkinter.Entry(newWindow1)  
            en11.place(x=200, y=520)
 
            lb12= tkinter.Label(newWindow1, text="Final year (cgpa)", width=17,font=("arial",12))  
            lb12.place(x=23, y=580) 
            lb12['bg']='white' 
            en12= tkinter.Entry(newWindow1)  
            en12.place(x=200, y=580)

            tkinter.Button(newWindow1, text="Confirm",command=linkwindow1, width=10).place(x=200,y=630)
            try:
                #print("in first try block")
                cur.execute("use registration")
            except:
                #print("in first exception block")
                cur.execute("create database registration")
                cur.execute("use registration")

            try:
                #print("in second try block")
                cur.execute("describe engineering")

            except:
                print("in second exception block")
                cur.execute("create table engineering(id int primary key auto_increment, name varchar(20), DOB varchar(20), contact_no bigint,gender varchar(10), email varchar(50),address varchar(100),12th_grade int, skills varchar(150), languages varchar(50),Branch varchar(30),CGPA int))")
           
            '''try:
                print("in third try block")
                addReg="insert into job(name, DOB, contact_no, gender, address, email, 12th_grade, skills, languages, Branch, CGPA) values ({en1.get()},{en3.get()},{en4.get()},{var.get()},{en6.get()},{en7.get()},{en8.get()},{en9.get()},{en10.get()},{en11.get()},{en12.get()});"
                print(addReg)
                cur.execute(addReg)
                #con.commit()
            except:
                print("in third exception allowed")'''
            #registration()
                
            newWindow1.mainloop()
 
        def openNewWindow2():
            
            def linkwindow2():
                def openlastWindow2():
                    lastWindow2= Toplevel(window2)
                    lastWindow2.title("New Window 2")
                    lastWindow2.geometry("1500x800")
                    linkwindow2.destroy()
                    img12=Image.open('D:\Computer_project_tkinter\job_pics\lastfin2.png')
                    photo12=ImageTk.PhotoImage(img12)
                    bg12=Label(lastWindow2,image=photo12)
                    bg12.image=photo12
                    bg12.pack(fill='both',expand='yes')
                addReg2="insert into entertainment(name, DOB, contact_no, gender, email, address, languages, skills, ART, Degree, 12thmarks) values ('" + en1.get() + "','"
                addReg2= addReg2 + en3.get() + "',"
                addReg2= addReg2 + en4.get() + ",'"
                addReg2= addReg2 + var2.get() + "','"
                addReg2= addReg2 + en6.get() + "','"
                addReg2= addReg2 + en7.get() + "','"
                addReg2= addReg2 + en8.get() + "','"
                addReg2= addReg2 + en9.get() + "','"
                addReg2= addReg2 + en10.get() + "','"
                addReg2= addReg2 + en11.get() + "',"
                addReg2= addReg2 + en12.get() + ");"
                #addReg="insert into job(name, DOB, contact_no, gender, address, email, 12th_grade, skills, languages, Branch, CGPA) values ('" + en1.get()+ "',"+
                #,",en3.get(),en4.get(),var.get(),en6.get(),en7.get(),en8.get(),en9.get(),en10.get(),en11.get(),en12.get());"
                print(addReg2)
                cur.execute(addReg2)
                con.commit()
            
                linkwindow2= Toplevel(window2)
                linkwindow2.title("New Window")
                linkwindow2.geometry("1500x800")
                Label(linkwindow2,text ="links for entertainment industry").pack()
               
                Label(linkwindow2,text ="COMPANIES OFFERED",font=("Arial",10 )).pack()
                newWindow2.destroy()
                img5=Image.open('D:\Computer_project_tkinter\job_pics\link.png')
                photo5=ImageTk.PhotoImage(img5)
                bg5=Label(linkwindow2,image=photo5)
                bg5.image=photo5
                bg5.pack(fill='both',expand='yes')
                varl2 = StringVar()
                varl2.set("radio")
                radio2=Radiobutton(linkwindow2, text="POP ENTERTAINMENT", command=openlastWindow2, padx=5,font=("Arial",15),variable=varl2, value="POP").place(x=180, y=250)  
                radio3=Radiobutton(linkwindow2, text="ON ENTERTAINMENT ",command=openlastWindow2, padx =10,font=("Arial",15 ),variable=varl2, value="ON").place(x=180,y=400)  
                radio4=Radiobutton(linkwindow2, text="BSL ENTERTAINMENT",command=openlastWindow2,  padx=15,font=("Arial",15 ), variable=varl2, value="BSL").place(x=180,y=550)
                
            newWindow2 = Toplevel(window2)
            newWindow2.title("New Window2")
            newWindow2.geometry("1500x800")
            #tkinter.Label(newWindow2,text ="Entertainment Industry").pack()
            img4=Image.open('D:\Computer_project_tkinter\job_pics\entPicfin.png')
            photo4=ImageTk.PhotoImage(img4)
            bg4=Label(newWindow2,image=photo4)
            bg4.image=photo4
            bg4.pack(fill='both',expand='yes')
            lb4= tkinter.Label(newWindow2, text="Name", width=10, font=("arial",12))  
            lb4.place(x=21, y=120) 
            lb4['bg']='white'
            en1= tkinter.Entry(newWindow2)  
            en1.place(x=200, y=120)  
 
            lb3= tkinter.Label(newWindow2, text="DOB", width=10, font=("arial",12))  
            lb3.place(x=21, y=160)
            lb3['bg']='white'
            en3= tkinter.Entry(newWindow2)  
            en3.place(x=200, y=160)  
 
            lb6= tkinter.Label(newWindow2, text="Enter Email", width=13,font=("arial",12))  
            lb6.place(x=21, y=320) 
            lb6['bg']='white'
            en6= tkinter.Entry(newWindow2)  
            en6.place(x=200, y=320)  
 
            lb4= tkinter.Label(newWindow2, text="Contact Number", width=13,font=("arial",12))  
            lb4.place(x=21, y=200)
            lb4['bg']='white'  
            en4= tkinter.Entry(newWindow2)  
            en4.place(x=200, y=200)  
 
            lb7= Label(newWindow2, text="Address", width=15,font=("arial",12))  
            lb7.place(x=21, y=360)
            lb7['bg']='white' 
            en7 =tkinter.Entry(newWindow2)  
            en7.place(x=200, y=360)  
 
 
            lb5= tkinter.Label(newWindow2, text="Select Gender", width=15, font=("arial",12))  
            lb5.place(x=5, y=240)
            lb5['bg']='white' 
            var2 = StringVar()
            var2.set("Radio")
            radio=Radiobutton(newWindow2, text="Male", padx=5,variable=var2, value='Male').place(x=180, y=240)  
            radio=Radiobutton(newWindow2, text="Female", padx =10,variable=var2,value='Female').place(x=240,y=240)  
            radio=Radiobutton(newWindow2, text="Other", padx=15, variable=var2,value='Other').place(x=310,y=240)  
            
            lb8= tkinter.Label(newWindow2, text="Languages known", width=15,font=("arial",12))  
            lb8.place(x=19, y=390) 
            lb8['bg']='white'
            en8=tkinter.Entry(newWindow2)  
            en8.place(x=200, y=390)
 
            lb9= tkinter.Label(newWindow2, text="Skills", width=13,font=("arial",12))  
            lb9.place(x=19, y=430) 
            lb9['bg']='white'
            en9= tkinter.Entry(newWindow2)  
            en9.place(x=200, y=430)
 
            lb10= tkinter.Label(newWindow2, text="Form of Art",width=13, font=("arial",12))  
            lb10.place(x=23, y=480) 
            lb10['bg']='white'
            en10= tkinter.Entry(newWindow2)  
            en10.place(x=200, y=480)
 
            lb11= tkinter.Label(newWindow2, text="Degree", width=16,font=("arial",12))  
            lb11.place(x=23, y=520)
            lb11['bg']='white'
            en11= tkinter.Entry(newWindow2)  
            en11.place(x=200, y=520)
 
            lb12=tkinter.Label(newWindow2, text="12th%", width=17,font=("arial",12))  
            lb12.place(x=23, y=580) 
            lb12['bg']='white'
            en12=tkinter.Entry(newWindow2)  
            en12.place(x=200, y=580)
 
            tkinter.Button(newWindow2, text="Confirm",command=linkwindow2,width=10).place(x=200,y=630)
            
            try:
                #print("in first try block")
                cur.execute("use registration")
            except:
                #print("in first exception block")
                cur.execute("create database registration")
                cur.execute("use registration")

            try:
                #print("in second try block")
                cur.execute("describe entertainment")

            except:
                print("in second exception block")
                cur.execute("create table entertainment(id int primary key auto_increment, name varchar(20), DOB varchar(20), contact_no bigint, gender varchar(10), email varchar(50),address varchar(100), languages varchar(50), skills varchar(100), ART varchar(50),Degree varchar(50), 12thmarks int)")
             
            newWindow2.mainloop()  
 
        def openNewWindow3():
            
            def linkwindow3():
                def openlastWindow3():
                    lastWindow3= Toplevel(window2)
                    lastWindow3.title("New Window3")
                    lastWindow3.geometry("1500x800")
                    linkwindow3.destroy()
                    img13=Image.open('D:\Computer_project_tkinter\job_pics\lastfin2.png')
                    photo13=ImageTk.PhotoImage(img13)
                    bg13=Label(lastWindow3,image=photo13)
                    bg13.image=photo13
                    bg13.pack(fill='both',expand='yes')
                addReg3="insert into education1(name, DOB, contact_no, gender, email, address, 12thmarks, bed_score, languages, Hobbies, subject) values ('" + en1.get() + "','"
                addReg3= addReg3 + en3.get() + "',"
                addReg3= addReg3 + en4.get() + ",'"
                addReg3= addReg3 + vars.get() + "','"
                addReg3= addReg3 + en6.get() + "','"
                addReg3= addReg3 + en7.get() + "',"
                addReg3= addReg3 + en8.get() + ","
                addReg3= addReg3 + en9.get() + ",'"
                addReg3= addReg3 + en10.get() + "','"
                addReg3= addReg3 + en11.get() + "','"
                addReg3= addReg3 + en12.get() + "');"
                #addReg="insert into job(name, DOB, contact_no, gender, address, email, 12th_grade, skills, languages, Branch, CGPA) values ('" + en1.get()+ "',"+
                #,",en3.get(),en4.get(),var.get(),en6.get(),en7.get(),en8.get(),en9.get(),en10.get(),en11.get(),en12.get());"
                print(addReg3)
                cur.execute(addReg3)
                con.commit()
            
                linkwindow3= Toplevel(window2)
                linkwindow3.title("New Window")
                linkwindow3.geometry("1500x800")
                #Label(linkwindow2,text ="links for entertainment industry").pack()
                newWindow3.destroy()
                img6=Image.open('D:\Computer_project_tkinter\job_pics\link.png')
                photo6=ImageTk.PhotoImage(img6)
                bg6=Label(linkwindow3,image=photo6)
                bg6.image=photo6
                bg6.pack(fill='both',expand='yes')
                varl2 = StringVar()
                varl2.set("radio")
                radio2=Radiobutton(linkwindow3, text="National Public School", command=openlastWindow3, padx=5,font=("Arial",15),variable=varl2, value="NPS").place(x=180, y=250)  
                radio3=Radiobutton(linkwindow3, text="ST. XAVIERS ",command=openlastWindow3, padx =10,font=("Arial",15 ),variable=varl2, value="XAVIERS").place(x=180,y=400)  
                radio4=Radiobutton(linkwindow3, text="Schhol of India",command=openlastWindow3,  padx=15,font=("Arial",15 ), variable=varl2, value="SOI").place(x=180,y=550)
            newWindow3 = Toplevel(window2)
            newWindow3.title("New Window")
            newWindow3.geometry("1500x800")
            img3=Image.open('D:\Computer_project_tkinter\job_pics\eduPic1.png')
            photo3=ImageTk.PhotoImage(img3)
            bg3=Label(newWindow3,image=photo3)
            bg3.image=photo3
            bg3.pack(fill='both',expand='yes')
            Label(newWindow3,text ="Education Department",font=("arial",30)).pack()
            lb1= Label(newWindow3, text="Name", width=10, font=("arial",12))  
            lb1.place(x=20, y=120)
            lb1['bg']='white' 
            en1= Entry(newWindow3)  
            en1.place(x=200, y=120)  
 
            lb3= Label(newWindow3, text="DOB", width=10, font=("arial",12))  
            lb3.place(x=19, y=160)
            lb3['bg']='white'   
            en3= Entry(newWindow3)  
            en3.place(x=200, y=160)  
 
            lb6= Label(newWindow3, text="Enter Email", width=13,font=("arial",12))  
            lb6.place(x=19, y=320)
            lb6['bg']='white'  
            en6= Entry(newWindow3)  
            en6.place(x=200, y=320)  
 
            lb4= Label(newWindow3, text="Contact Number", width=13,font=("arial",12))  
            lb4.place(x=19, y=200)
            lb4['bg']='white'  
            en4= Entry(newWindow3)  
            en4.place(x=200, y=200)  
 
            lb7= Label(newWindow3, text="Address", width=15,font=("arial",12))  
            lb7.place(x=21, y=360)
            lb7['bg']='white'  
            en7 =Entry(newWindow3)  
            en7.place(x=200, y=360)  
 
 
            lb5= Label(newWindow3, text="Select Gender", width=15, font=("arial",12))  
            lb5.place(x=5, y=240)
            lb5['bg']='white' 
            vars = StringVar()  
            radio=tkinter.Radiobutton(newWindow3, text="Male", padx=5,variable=vars, value="Male").place(x=180, y=240)  
            radio=tkinter.Radiobutton(newWindow3, text="Female", padx =10,variable=vars, value="Female").place(x=240,y=240)  
            radio=tkinter.Radiobutton(newWindow3, text="others", padx=15, variable=vars, value="Other").place(x=310,y=240)  
 
            lb8= Label(newWindow3, text="12 th grade(%)", width=15,font=("arial",12))  
            lb8.place(x=19, y=390)
            lb8['bg']='white' 
            en8= Entry(newWindow3)  
            en8.place(x=200, y=390)
 
            lb9= Label(newWindow3, text="B.ed Score", width=13,font=("arial",12))  
            lb9.place(x=19, y=430)
            lb9['bg']='white' 
            en9= Entry(newWindow3)  
            en9.place(x=200, y=430)
 
            lb10= Label(newWindow3, text="Languages known",font=("arial",12))  
            lb10.place(x=19, y=480)
            lb10['bg']='white'  
            en10= Entry(newWindow3)  
            en10.place(x=200, y=480)
 
            lb11= Label(newWindow3, text="Hobbies", width=16,font=("arial",12))  
            lb11.place(x=23, y=520)
            lb11['bg']='white'
            en11= Entry(newWindow3)  
            en11.place(x=200, y=520)
 
            lb12= Label(newWindow3, text="Subject Specialization", width=17,font=("arial",12))  
            lb12.place(x=23, y=580)
            lb12['bg']='white' 
            en12= Entry(newWindow3)  
            en12.place(x=200, y=580)
 
 
            Button(newWindow3, text="Confirm",command = linkwindow3, width=10).place(x=200,y=630)  
            try:
                #print("in first try block")
                cur.execute("use registration")
            except:
                #print("in first exception block")
                cur.execute("create database registration")
                cur.execute("use registration")

            try:
                #print("in second try block")
                cur.execute("describe education1")

            except:
                print("in second exception block")
                cur.execute(")create table education1(id int primary key auto_increment, name varchar(20), DOB varchar(20), contact_no bigint, gender varchar(10), email varchar(50),address varchar(100), 12thmarks int, bed_score int, languages varchar(50), Hobbies varchar(50), subject varchar(50))")
             
             
 
            newWindow3.mainloop()
            
 
        menu2= StringVar()
        menu2.set("Select profession")
        button1 = Button( window2, text = "Engineering" , command = openNewWindow1,font=("Arial",20 )).place(x=900,y=200)
        button2 = Button( window2, text = "Entertainment Industry" , command = openNewWindow2,font=("Arial",20 )).place(x=900,y=300)
        button3 = Button( window2 , text = "Education System" , command = openNewWindow3,font=("Arial",20 )).place(x=900,y=400)
        menu2.pack()
        button1.pack()
        button2.pack()
        button3.pack()
   
        window2.mainloop()
 
 
    else:
        messagebox.showerror(title="Error", message="Invalid login.")
 
frame = tkinter.Frame(bg='#FFB5C5')
# Creating widgets
login_label = tkinter.Label(
    frame, text="Login", bg='#FFB5C5', fg="#FF3399", font=("Arial", 30))
username_label = tkinter.Label(
    frame, text="Username", bg='#FFB5C5', fg="#FFFFFF", font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
password_label = tkinter.Label(
    frame, text="Password", bg='#FFB5C5', fg="#FFFFFF", font=("Arial", 16))
login_button = tkinter.Button(
    frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)

# Placing widgets on the screentkinter
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)
 
frame.pack()
window.mainloop()
