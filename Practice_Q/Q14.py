from tkinter import *
import math

# function to handle click event
def click(event):
    global  scvalue,Screen
    try:
        text=event.widget.cget('text')

        Screen.update()
        if text=="=":
            if scvalue.get().isdigit():
                value=int(scvalue.get())
            else :            
                value=eval(scvalue.get())
            scvalue.set(value)
            Screen.update()

        elif text=="C":
            scvalue.set("")
            Screen.update()

        else:
            scvalue.set(scvalue.get()+text)

    except SyntaxError:
        scvalue.set('Error')
        Screen.update()
        print('Error')
def main():
    window=Tk()
    window.geometry('440x580')
    window.config(bg='grey')
    global Screen,scvalue
    scvalue=StringVar()
    Screen=Entry(window,textvariable=scvalue,font='comicsanms 40 bold')
    Screen.pack(pady=10,padx=5)

    f1=Frame(window,bg='white')
    f1.pack(pady=5,side=BOTTOM)
    f2=Frame(window,bg='white')
    f2.pack(pady=5,side=BOTTOM)
    f3=Frame(window,bg='white')
    f3.pack(pady=5,side=BOTTOM)
    f4=Frame(window,bg='white')
    f4.pack(pady=5,side=BOTTOM)
 
    list1=['0','1','2','3','4','5','6','7','8','9','+','-','*','/','%','=','C','**']
    for i in list1:
        if list1.index(i)<5:
            b=Button(f4,text=i,bg='black',fg='white',font='lucida 37 bold')
            b.pack(side=LEFT,padx=5,pady=5)
            b.bind('<Button-1>',click)
            
        
        elif list1.index(i)<10 and list1.index(i)>=5:
            b=Button(f3,text=i,bg='black',fg='white',font='lucida 37 bold')
            b.pack(side=LEFT,padx=5,pady=5)
    
            b.bind('<Button-1>',click)
        elif  list1.index(i)>=10 and list1.index(i)<15:
            b=Button(f2,text=i,bg='black',fg='white',font='lucida 37 bold')
            b.pack(side=LEFT,padx=5,pady=5)
            b.bind('<Button-1>',click)
        elif list1.index(i)>=15 and list1.index(i)<20:
            b=Button(f1,text=i,bg='black',fg='white',font='lucida 31 bold')
            b.pack(side=LEFT,padx=2,pady=5)
            b.bind('<Button-1>',click)

    #  display window 
    window.mainloop()

if __name__=="__main__":
    main()
    
