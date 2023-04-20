import tkinter as tk
from tkinter import ttk
from dataExt import *
from PIL import ImageTk, Image




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
#root.config(bg="#454545")
root.state("zoomed")
img = ImageTk.PhotoImage(Image.open("exam.jpg"))
panel = tk.Label(root, image = img)
panel.place(x=0, y=0)



# Define the style for combobox widget
style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "#FFE6C7", background= "#FFA559")
style.master.option_add( '*TCombobox*Listbox.selectBackground','#FF6000')
style.master.option_add( '*TCombobox*Listbox.background', '#FFE6C7')



#creating the form frames
form=tk.Frame(root, relief="sunken", bg="#454545")
form.pack(expand= False, padx=20, pady=80)

rank=tk.Frame(form,relief="sunken", bg="#454545")
rank.pack(fill=tk.BOTH, expand= True, pady=20, padx=20)

quota=tk.Frame(form,relief="sunken", bg="#454545")
quota.pack(fill=tk.BOTH, expand= True, pady=20, padx=20)

branch=tk.Frame(form,relief="sunken", bg="#454545")
branch.pack(fill=tk.BOTH, expand= True, pady=20, padx=20)
branchframe=tk.Frame(branch,relief="sunken", bg="#454545")
branchlistbox=tk.Frame(branchframe,relief="sunken", bg="#454545")

location=tk.Frame(form,relief="sunken", bg="#454545")
location.pack(fill=tk.BOTH, expand= True, pady=20, padx=20)
locationframe=tk.Frame(location,relief="sunken", bg="#454545")
locationlistbox=tk.Frame(locationframe,relief="sunken", bg="#454545")

college=tk.Frame(form,relief="sunken", bg="#454545")
college.pack(fill=tk.BOTH, expand= True, pady=20, padx=20)
collegeframe=tk.Frame(college,relief="sunken", bg="#454545")
collegelistbox=tk.Frame(collegeframe,relief="sunken", bg="#454545")



#Initialising to string variable
rankVar=tk.StringVar()




#creating rank form elements
rankLabel=tk.Label(rank, text="Enter your Rank:           ", font=("Times New Roman", 20), fg="#FFE6C7", bg="#454545")
rankEntry=tk.Entry(rank, textvariable=rankVar, font=("Times New Roman", 20), relief="sunken", highlightbackground="#FF6000", highlightthickness=2, background="#FFE6C7")

quotaLst=quota_lst(diction)
quotaLabel=tk.Label(quota, text="Select Category:                 ", font=("Times New Roman", 20), fg="#FFE6C7", bg="#454545")
quotaEntry=ttk.Combobox(quota, value=quotaLst, justify="center")
quotaEntry.current(0)

branchLabel=tk.Label(branch, text="Select Preferred Branches:               ", font=("Times New Roman", 20), fg="#FFE6C7", bg="#454545")
branchEntry=tk.Entry(branchframe, font=("Times New Roman", 20), width=11, relief="sunken", highlightbackground="#FF6000", highlightthickness=1, background="#FFE6C7")
branchEntry.pack()
scrollbar=tk.Scrollbar(branchlistbox, orient=tk.VERTICAL)
branchChoice=tk.Listbox(branchlistbox, width=23, relief="sunken", highlightbackground="#FF6000", highlightthickness=1, background="#FFE6C7", selectbackground="#FF6000", selectmode=tk.MULTIPLE, height=8, yscrollcommand=scrollbar.set)
scrollbar.config(command=branchChoice.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
branchChoice.pack()
branchLst=branch_lst(diction)

branchEntry.bind("<KeyRelease>", checkBranch)
updateBranch(branchLst)


locationLabel=tk.Label(location, text="Select Preferred Locations:               ", font=("Times New Roman", 20), fg="#FFE6C7", bg="#454545")
locationEntry=tk.Entry(locationframe, font=("Times New Roman", 20), width=11, relief="sunken", highlightbackground="#FF6000", highlightthickness=1, background="#FFE6C7")
locationEntry.pack()
scrollbar=tk.Scrollbar(locationlistbox, orient=tk.VERTICAL)
locationChoice=tk.Listbox(locationlistbox, width=23, relief="sunken", highlightbackground="#FF6000", highlightthickness=1, background="#FFE6C7", selectbackground="#FF6000", selectmode=tk.MULTIPLE, height=8, yscrollcommand=scrollbar.set)
scrollbar.config(command=locationChoice.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
locationChoice.pack()
locationLst=location_lst(diction)

locationEntry.bind("<KeyRelease>", checklocation)
updatelocation(locationLst)




collegeLabel=tk.Label(college, text="Select Preferred colleges:               ", font=("Times New Roman", 20), fg="#FFE6C7", bg="#454545")
collegeEntry=tk.Entry(collegeframe, font=("Times New Roman", 20), width=11, relief="sunken", highlightbackground="#FF6000", highlightthickness=1, background="#FFE6C7")
collegeEntry.pack()
scrollbar=tk.Scrollbar(collegelistbox, orient=tk.VERTICAL)
collegeChoice=tk.Listbox(collegelistbox, width=23, relief="sunken", highlightbackground="#FF6000", highlightthickness=1, background="#FFE6C7", selectbackground="#FF6000", selectmode=tk.MULTIPLE, height=8, yscrollcommand=scrollbar.set)
scrollbar.config(command=collegeChoice.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
collegeChoice.pack()
collegeLst=college_lst(diction)

collegeEntry.bind("<KeyRelease>", checkcollege)
updatecollege(collegeLst)





#placing the form elements
rankLabel.pack(side=tk.LEFT)
rankEntry.pack(side=tk.LEFT)

quotaLabel.pack(side=tk.LEFT)
quotaEntry.pack(side=tk.LEFT)

branchLabel.pack(side=tk.LEFT)
branchframe.pack(side=tk.LEFT)
branchlistbox.pack()

locationLabel.pack(side=tk.LEFT)
locationframe.pack(side=tk.LEFT)
locationlistbox.pack()

collegeLabel.pack(side=tk.LEFT)
collegeframe.pack(side=tk.LEFT)
collegelistbox.pack()





root.mainloop()