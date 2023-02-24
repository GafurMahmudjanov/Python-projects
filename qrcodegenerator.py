from tkinter import *
import os
import qrcode

root =Tk()
root.title('QR generator')
root.geometry('1000x550')
root.config(bg='#2B3467')
root.resizable(False,False)

# image_icon=PhotoImage(file='QR/icon.png')
# root.iconphoto(False,image_icon)
def generate():
    try:
      name=title.get()
      text=entry.get()
      qr=qrcode.make(text)
      qr.save('QR/'+ str(name)+'.png')
    except:
         os.makedirs('QR')
         qr.save('QR/'+ str(name)+'.png')
    global Image
    Image = PhotoImage(file='QR/'+str(name)+'.png')
    Image_view.config(image=Image)
    Label(root,text='All done boss!',fg='#FCFFE7',bg='#2B3467',font=('Times',16,'bold')).place(x=60,y=500)

Image_view =Label(root,bg='#2B3467')
Image_view.pack(padx=50,pady=10,side=RIGHT)



Label(root,text='This is QR code Generator',fg='#FCFFE7',bg='#2B3467',font=('Open Sans',30,'bold')).place(x=270,y=20)


Label(root,text='Title for QR:',fg='#FCFFE7',bg='#2B3467',font=('Open Sans',16)).place(x=50,y=170)
Label(root,text='Content of QR:',fg='#FCFFE7',bg='#2B3467',font=('Open Sans',16)).place(x=50,y=240)
title=Entry(root,width=15,font=('arial',20,'bold'))
title.place(x=50,y=200)

entry = Entry(root,width=28,font=('arial',20,'bold'))
entry.place(x=50,y=270)

Button(root,text='Generate',width=10,height=2,bg='#EB455F',fg='#FCFFE7',font=('arial',12,'bold'),command=generate).place(x=368,y=320)
Label(root,text='Version 1.0 \n Developed by Gafur.M', fg='#FCFFE7',bg='#2B3467',font=('Times',12,'bold')).place(x=810,y=500)
root.mainloop()
