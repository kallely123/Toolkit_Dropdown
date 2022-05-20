from tkinter import *
root=Tk()
mymenu=Menu(root)
root.config(menu=mymenu)
submenu=Menu(mymenu)
def np():
    print("New projrct opend")
def ns():
    print("New file searched")
def op():
    print("open file")
def sa():
    print("Save to folder")
def psm():
    print("Power save mode on")
def ex():
    exit()
def ut():
    print("Undo")
def re():
    print("Redo file")
def cut():
    print("cutfile")
def cpr():
    print("Copy past reference")
def Delt():
    print("Delete file")
def fd():
    print("Find file")
def tw():
    print("Tool window file opened!")
def app():
    print("Apperence")
def Qd():
    print("Quik defnition file")
def qtp():
    print("Quik type defnition  file")
def quick_doc():
    print("quik documention file")
def pii():
    print("oParameter information ")
def back():
    print("Back to previous file")
def fwd():
    print("Forward  file")
def se():
    print("search Everywhere")
def cls():
    print("class")
def fle():
    print("File")
def smbl():
    print("Symbol")
def lc():
    print("Line Column")
def fd():
    print("Find file")
def qm():
    print("qverrid Method")
def im():
    print("Implement methods")
def gnr():
    print("Generate ")
def cc():
    print("Code Complition file")
def ic():
    print("Inspect code")
def cc_clc():
    print("code cleanup")
mymenu.add_cascade(label="file",menu=submenu)
submenu.add_command(label="New Project",command=np)
submenu.add_command(label="New search File",command=ns)
submenu.add_separator()
submenu.add_command(label="open..",command=op)
submenu.add_command(label="save As...",command=sa)
submenu.add_separator()
submenu.add_command(label="Power Save mode",command=psm)
submenu.add_command(label="Exit",command=ex)
newmenu1=Menu(mymenu)
mymenu.add_cascade(label="Edit",menu=newmenu1)
newmenu1.add_command(label="Undu Typing",command=ut)
newmenu1.add_command(label="Redo",command=re)
newmenu1.add_separator()
newmenu1.add_command(label="Cut",command=cut)
newmenu1.add_command(label="Copy/Path/Reference..",command=cpr)
newmenu1.add_separator()
newmenu1.add_command(label="Delete",command=Delt)
newmenu1.add_command(label="Find",command=fd)
newmenu2=Menu(mymenu)
mymenu.add_cascade(label="Veiw",menu=newmenu2)
newmenu2.add_command(label="Tool Windows",command=tw)
newmenu2.add_command(label="Appearence",command=app)
newmenu2.add_separator()
newmenu2.add_command(label="Quik Defnition",command=Qd)
newmenu2.add_command(label="Quik Type Defnition",command=qtp)
newmenu2.add_separator()
newmenu2.add_command(label="Quik Documentaion",command=quick_doc)
newmenu2.add_command(label="parameter info",command=pii)
newmenu3=Menu(mymenu)
mymenu.add_cascade(label="Navigate",menu=newmenu3)
newmenu3.add_command(label="Back",command=back)
newmenu3.add_command(label="Forward",command=fwd)
newmenu3.add_separator()
newmenu3.add_command(label="Search Everywhare",command=se)
newmenu3.add_command(label="class..",command=cls)
newmenu3.add_separator()
newmenu3.add_command(label="File..",command=fle)
newmenu3.add_command(label="Symbol",command=smbl)
newmenu3.add_command(label="line column....",command=lc)
newmenu4=Menu(mymenu)
mymenu.add_cascade(label="Code",menu=newmenu4)
newmenu4.add_command(label="Quverrid Methods...",command=qm)
newmenu4.add_command(label="implement Methods...",command=im)
newmenu4.add_separator()
newmenu4.add_command(label="Generate...",command=gnr)
newmenu4.add_command(label="Code Complition",command=cc)
newmenu4.add_separator()
newmenu4.add_command(label="Inspect Code",command=ic)
newmenu4.add_command(label="Code cleanup",command=cc_clc)
root.mainloop()