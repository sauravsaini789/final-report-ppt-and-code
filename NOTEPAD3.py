from tkinter import*
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def newfile():
    global file
    root.title("untitled-NOTPAD")
    file=None
    textarea.delete(1.0,END)
def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetype=[("all files","*.*"),("text doccuments","*.txt")])
    if file == "":
        file=None
    else:
        root.title(os.Path.basename(file)+"- NOTEPAD")
        textarea.delete(1.0,END)
        f=open(file,"r")
        textarea.insert(1.0,END)
def savefile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetype=[("all files","*.*"),("text doccuments",
                                                                                                                 "*.txt")])
        if file==" ":
            file=None
        else:
            f=open(file,"w")
            f.write(textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename((file) + "-NOTEPAD"))
    else:
        #save the file
        f=open(file,"w")
        f.write(textarea.get(1.0,END))
        f.close()
def quitapp():
    root.destroy()
def about():
    showinfo("NOTEPAD","notepad by saurav saini")

def cut():
    textarea.event_generate(("<<cut>>"))
def copy():
    textarea.event_generate(("<<copy>>"))
def paste():
    textarea.event_generate(("<<paste>>"))
if __name__ == '__main__':
    # #basic tkinter setup
    root=Tk()
    root.title("untitled-NOTPAD")
    root.geometry("644x788")
    #add text area
    # textarea=Text(root,font="lucida 13")
    file=None
    # textarea.pack(fill=BOTH)

    mymenue = Menu(root)
    m1 = Menu(mymenue, tearoff=0)
    m1.add_command(label="new", command=newfile)
    m1.add_command(label="open", command=openfile)
    m1.add_command(label="save", command=savefile)
    m1.add_command(label="exit", command=quitapp)

    mymenue.add_cascade(label="File", menu=m1)
    m2 = Menu(mymenue, tearoff=0)
    m2.add_command(label="cut", command=cut)
    m2.add_command(label="copy", command=copy)
    m2.add_command(label="paste", command=paste)
    root.config(menu=mymenue)
    mymenue.add_cascade(label="Edit", menu=m2)
    m3=Menu(mymenue,tearoff=0)
    m3.add_command(label="about",command=about)
    root.config(menu=mymenue)
    mymenue.add_cascade(label="about",menu=m3)
    scrollbar= Scrollbar(root)
    scrollbar.pack(side=RIGHT,fill=Y)
    textarea = Text(root,yscrollcommand=scrollbar.set, font="lucida 13")
    textarea.pack(fill=BOTH)
    scrollbar.config(command=textarea.yview)


    root.mainloop()