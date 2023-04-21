import tkinter as tk
from tkinter import ttk
from dataExt import *
from PIL import ImageTk, Image


#functions for dropdown

#branch
countBranch=1
def show_hidebranch():
    global countBranch
    countBranch+=1
    if countBranch%2==0:
        branchlistbox.pack()
    elif countBranch%2==1:
        branchlistbox.pack_forget()


#location
countLocation=1
def show_hidelocation():
    global countLocation
    countLocation+=1
    if countLocation%2==0:
        locationlistbox.pack()
    elif countLocation%2==1:
        locationlistbox.pack_forget()


#college
countCollege=1
def show_hidecollege():
    global countCollege
    countCollege+=1
    if countCollege%2==0:
        collegelistbox.pack()
    elif countCollege%2==1:
        collegelistbox.pack_forget()





#listbox functions

#branch listbox
selectedBranch=[]     #global variables for branch selection
dataBranch=[]
def updateBranch(dataBranch):
    branchChoice.delete(0,tk.END)
    i=0
    #printing the listbox
    for item in dataBranch:
        branchChoice.insert(tk.END, item)
        if item in selectedBranch:
            branchChoice.select_set(i)
        i+=1

def checkBranch(event):
    global dataBranch
    global selectedBranch
    typed = branchEntry.get()
    
    #updating the lisbox in each search
    temp=[]
    for i in branchChoice.curselection():
        temp.append(branchChoice.get(i))
        if branchChoice.get(i) not in selectedBranch:
            selectedBranch.append(branchChoice.get(i))

    for i in dataBranch: 
        if (i in selectedBranch) and (i not in temp):
            selectedBranch.remove(i)

    #updating dataBranch
    if typed == '':
        dataBranch = branchLst
    else:
        dataBranch = []
        for item in branchLst:
            if typed.lower() in item.lower():
                dataBranch.append(item)
    
    updateBranch(dataBranch)




#location listbox
selectedlocation=[]     #global variables for location selection
datalocation=[]
def updatelocation(datalocation):
    locationChoice.delete(0,tk.END)
    i=0
    #printing the listbox
    for item in datalocation:
        locationChoice.insert(tk.END, item)
        if item in selectedlocation:
            locationChoice.select_set(i)
        i+=1

def checklocation(event):
    global datalocation
    global selectedlocation
    typed = locationEntry.get()
    
    #updating the lisbox in each search
    temp=[]
    for i in locationChoice.curselection():
        temp.append(locationChoice.get(i))
        if locationChoice.get(i) not in selectedlocation:
            selectedlocation.append(locationChoice.get(i))

    for i in datalocation: 
        if (i in selectedlocation) and (i not in temp):
            selectedlocation.remove(i)

    #updating datalocation
    if typed == '':
        datalocation = locationLst
    else:
        datalocation = []
        for item in locationLst:
            if typed.lower() in item.lower():
                datalocation.append(item)
    
    updatelocation(datalocation)




#college listbox
selectedcollege=[]     #global variables for college selection
datacollege=[]
def updatecollege(datacollege):
    collegeChoice.delete(0,tk.END)
    i=0
    #printing the listbox
    for item in datacollege:
        collegeChoice.insert(tk.END, item)
        if item in selectedcollege:
            collegeChoice.select_set(i)
        i+=1

def checkcollege(event):
    global datacollege
    global selectedcollege
    typed = collegeEntry.get()
    
    #updating the lisbox in each search
    temp=[]
    for i in collegeChoice.curselection():
        temp.append(collegeChoice.get(i))
        if collegeChoice.get(i) not in selectedcollege:
            selectedcollege.append(collegeChoice.get(i))

    for i in datacollege: 
        if (i in selectedcollege) and (i not in temp):
            selectedcollege.remove(i)

    #updating datacollege
    if typed == '':
        datacollege = collegeLst
    else:
        datacollege = []
        for item in collegeLst:
            if typed.lower() in item.lower():
                datacollege.append(item)
    
    updatecollege(datacollege)






#Extracting data from the csv file
diction={}
dataExtract(diction)



#creating the window
root=tk.Tk()
root.title("College Predictor")
root.state("zoomed")
root.minsize(700, 550)
bgimg = ImageTk.PhotoImage(Image.open("exam.jpg"))
panel = tk.Label(root, image = bgimg)
panel.place(x=0, y=0)



# Define the style for combobox widget
style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "#F4EEE0", background= "#6D5D6E")
style.master.option_add( '*TCombobox*Listbox.selectBackground','#6D5D6E')
style.master.option_add( '*TCombobox*Listbox.background', '#F4EEE0')



#creating the form frames
form=tk.Frame(root, relief="sunken", bg="#393646")
form.pack(expand= False, padx=20, pady=80)

rank=tk.Frame(form,relief="sunken", bg="#393646")
rank.pack(fill=tk.BOTH, expand= True, pady=20, padx=20)

quota=tk.Frame(form,relief="sunken", bg="#393646")
quota.pack(fill=tk.BOTH, expand= True, pady=20, padx=20)

branch=tk.Frame(form,relief="sunken", bg="#393646")
branch.pack(fill=tk.BOTH, expand= True, pady=20, padx=20)
branchframe=tk.Frame(branch,relief="sunken", bg="#393646")
branchdropdown=tk.Frame(branchframe,relief="sunken", bg="#393646")
branchlistbox=tk.Frame(branchframe,relief="sunken", bg="#393646")

location=tk.Frame(form,relief="sunken", bg="#393646")
location.pack(fill=tk.BOTH, expand= True, pady=20, padx=20)
locationframe=tk.Frame(location,relief="sunken", bg="#393646")
locationdropdown=tk.Frame(locationframe,relief="sunken", bg="#393646")
locationlistbox=tk.Frame(locationframe,relief="sunken", bg="#393646")

college=tk.Frame(form,relief="sunken", bg="#393646")
college.pack(fill=tk.BOTH, expand= True, pady=20, padx=20)
collegeframe=tk.Frame(college,relief="sunken", bg="#393646")
collegedropdown=tk.Frame(collegeframe,relief="sunken", bg="#393646")
collegelistbox=tk.Frame(collegeframe,relief="sunken", bg="#393646")



#Initialising to string variable
rankVar=tk.StringVar()
btnimg = ImageTk.PhotoImage(Image.open("btn.png"))



#creating rank form elements
rankLabel=tk.Label(rank, text="Enter your Rank*:           ", font=("Ubuntu", 18), fg="#F4EEE0", bg="#393646")
rankEntry=tk.Entry(rank, textvariable=rankVar, font=("Times New Roman", 20), relief="sunken", highlightbackground="#6D5D6E", highlightthickness=2, background="#F4EEE0")

quotaLst=quota_lst(diction)
quotaLabel=tk.Label(quota, text="Select Category*:                               ", font=("Ubuntu", 18), fg="#F4EEE0", bg="#393646")
quotaEntry=ttk.Combobox(quota, value=quotaLst,width=29, height=15, justify="center")
quotaEntry.current(0)

branchLabel=tk.Label(branch, text="Select Preferred Branches*:                ", font=("Ubuntu", 18), fg="#F4EEE0", bg="#393646")
branchEntry=tk.Entry(branchdropdown, font=("Times New Roman", 15), width=17, relief="sunken", highlightbackground="#6D5D6E", highlightthickness=1, background="#F4EEE0")
branchEntry.pack(side=tk.LEFT)
scrollbar=tk.Scrollbar(branchlistbox, orient=tk.VERTICAL)
branchChoice=tk.Listbox(branchlistbox, width=29, relief="sunken", highlightbackground="#6D5D6E", highlightthickness=1, background="#F4EEE0", selectbackground="#6D5D6E", selectmode=tk.MULTIPLE, height=8, yscrollcommand=scrollbar.set)
branchChoice.configure(exportselection=False)
scrollbar.config(command=branchChoice.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
branchChoice.pack()
branchLst=branch_lst(diction)
branchButton=tk.Button(branchdropdown, width=15, height=20, font=("Times New Roman", 10), image=btnimg, justify="center", bg="#6D5D6E", command=show_hidebranch)

branchEntry.bind("<KeyRelease>", checkBranch)
updateBranch(branchLst)


locationLabel=tk.Label(location, text="Select Preferred Locations:                ", font=("Ubuntu", 18), fg="#F4EEE0", bg="#393646")
locationEntry=tk.Entry(locationdropdown, font=("Times New Roman", 15), width=17, relief="sunken", highlightbackground="#6D5D6E", highlightthickness=1, background="#F4EEE0")
locationEntry.pack(side=tk.LEFT)
scrollbar=tk.Scrollbar(locationlistbox, orient=tk.VERTICAL)
locationChoice=tk.Listbox(locationlistbox, width=29, relief="sunken", highlightbackground="#6D5D6E", highlightthickness=1, background="#F4EEE0", selectbackground="#6D5D6E", selectmode=tk.MULTIPLE, height=8, yscrollcommand=scrollbar.set)
locationChoice.configure(exportselection=False)
scrollbar.config(command=locationChoice.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
locationChoice.pack()
locationLst=location_lst(diction)
locationButton=tk.Button(locationdropdown, width=15, height=20, font=("Times New Roman", 10), image=btnimg, justify="center", bg="#6D5D6E", command=show_hidelocation)

locationEntry.bind("<KeyRelease>", checklocation)
updatelocation(locationLst)




collegeLabel=tk.Label(college, text="Select Preferred Colleges:                 ", font=("Ubuntu", 18), fg="#F4EEE0", bg="#393646")
collegeEntry=tk.Entry(collegedropdown, font=("Times New Roman", 15), width=17, relief="sunken", highlightbackground="#6D5D6E", highlightthickness=1, background="#F4EEE0")
collegeEntry.pack(side=tk.LEFT)
scrollbary=tk.Scrollbar(collegelistbox, orient=tk.VERTICAL)
scrollbarx=tk.Scrollbar(collegelistbox, orient=tk.HORIZONTAL)
collegeChoice=tk.Listbox(collegelistbox, width=29, relief="sunken", highlightbackground="#6D5D6E", highlightthickness=1, background="#F4EEE0", selectbackground="#6D5D6E", selectmode=tk.MULTIPLE, height=8, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
collegeChoice.configure(exportselection=False)
scrollbary.config(command=collegeChoice.yview)
scrollbarx.config(command=collegeChoice.xview)
scrollbary.pack(side=tk.RIGHT, fill=tk.Y)
scrollbarx.pack(side=tk.BOTTOM, fill=tk.X)
collegeChoice.pack()
collegeLst=college_lst(diction)
collegeButton=tk.Button(collegedropdown, width=15, height=20, font=("Times New Roman", 10), image=btnimg, justify="center", bg="#6D5D6E", command=show_hidecollege)

collegeEntry.bind("<KeyRelease>", checkcollege)
updatecollege(collegeLst)





#placing the form elements
rankLabel.pack(side=tk.LEFT)
rankEntry.pack(side=tk.LEFT)

quotaLabel.pack(side=tk.LEFT)
quotaEntry.pack(side=tk.LEFT)

branchLabel.pack(side=tk.LEFT, anchor=tk.NW)
branchframe.pack(side=tk.LEFT, anchor=tk.NE)
branchdropdown.pack()
branchButton.pack(side=tk.LEFT)

locationLabel.pack(side=tk.LEFT, anchor=tk.NW)
locationframe.pack(side=tk.LEFT, anchor=tk.NW)
locationdropdown.pack()
locationButton.pack(side=tk.LEFT)

collegeLabel.pack(side=tk.LEFT, anchor=tk.NW)
collegeframe.pack(side=tk.LEFT, anchor=tk.NE)
collegedropdown.pack()
collegeButton.pack(side=tk.LEFT)




root.mainloop()