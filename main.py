import tkinter as tk
from tkinter import ttk
from dataExt import *
from PIL import ImageTk, Image
from tkinter import messagebox

def disp(Rank,Category,Branch,Location,College):
    global diction
    
    #creating display window
    dispWin=tk.Tk()
    dispWin.title("College Predictor")
    dispWin.state("zoomed")
    dispWin.minsize(700, 650)
    bgimg = ImageTk.PhotoImage(Image.open("exam.jpg"))
    panel = tk.Label(dispWin, image = bgimg)
    panel.place(x=0, y=0)


    lst=diction_location(diction["Location"])
    dataMain=[]
    #extracting data to dataMain
    for i in range(len(diction["College"])):
        if (diction["College"][i] in College) and (diction["Branch"][i] in Branch) and (lst[i] in Location) and (diction[Category][i] >= int(Rank)):
            data=(str(int(diction[Category][i])), diction["Branch"][i], diction["College"][i], diction["Location"][i], diction["CETCode"][i])
            dataMain.append(data)
    

    #creating display frame
    easyFrame=tk.Frame(dispWin, relief="sunken", bg="#393646")
    Easy=ttk.Treeview(easyFrame, selectmode="none", height=10)
    Easy['columns'] = ("Rank", "Branch", "College", "Location", "CET Code")
    Easy.column("#0", width=0, stretch=tk.NO)
    Easy.column("Rank", anchor=tk.CENTER, width=120)
    Easy.column("Branch", anchor=tk.CENTER, width=120)
    Easy.column("College", anchor=tk.CENTER, width=120)
    Easy.column("Location", anchor=tk.CENTER, width=120)
    Easy.column("CET Code", anchor=tk.CENTER, width=120)

    Easy.heading("#0", text="", anchor=tk.W)
    Easy.heading("Rank", text="Rank", anchor=tk.CENTER)
    Easy.heading("Branch", text="Branch", anchor=tk.CENTER)
    Easy.heading("College", text="College", anchor=tk.CENTER)
    Easy.heading("Location", text="Location", anchor=tk.CENTER)
    Easy.heading("CET Code", text="CET Code", anchor=tk.CENTER)

    for i in range(len(dataMain)):
        Easy.insert(parent='', index='end', iid=i, text="", values=dataMain[i])
    
    easyFrame.pack(fill=tk.BOTH, expand=True, padx=20, pady=80)
    Easy.pack(side=tk.TOP, pady=20, padx=20, fill=tk.X, expand=False)


    dispWin.mainloop()




def FORM():
    #function to validate the information entered
    def validate():
        error = ""
        Rank=rankEntry.get()
        Category = []
        for i in quotaChoice.curselection():
            Category.append(quotaChoice.get(i))
        Branch = []
        for i in branchChoice.curselection():
            Branch.append(branchChoice.get(i))
        Location = []
        for i in locationChoice.curselection():
            Location.append(locationChoice.get(i))
        College = []
        for i in collegeChoice.curselection():
            College.append(collegeChoice.get(i))
        if Location == []:
            Location = locationLst
        if College == []:
            College = collegeLst
        if Rank.isnumeric() == False:
            error+="•Rank Invalid.\n"
        if Category == []:
            error+="•Category not chosen.\n"
        if Branch == []:
            error+="•Branch not chosen.\n"
        
        if error!="":
            messagebox.showerror("Invalid Input", error)
        else:
            root.destroy()
            disp(Rank,Category[0],Branch,Location,College)



    #functions for dropdown

    #Quota
    countquota=1
    def show_hidequota():
        nonlocal countquota
        countquota+=1
        if countquota%2==0:
            quotalistbox.pack()
        elif countquota%2==1:
            quotalistbox.pack_forget()


    #branch
    countBranch=1
    def show_hidebranch():
        nonlocal countBranch
        countBranch+=1
        if countBranch%2==0:
            branchlistbox.pack()
        elif countBranch%2==1:
            branchlistbox.pack_forget()


    #location
    countLocation=1
    def show_hidelocation():
        nonlocal countLocation
        countLocation+=1
        if countLocation%2==0:
            locationlistbox.pack()
        elif countLocation%2==1:
            locationlistbox.pack_forget()


    #college
    countCollege=1
    def show_hidecollege():
        nonlocal countCollege
        countCollege+=1
        if countCollege%2==0:
            collegelistbox.pack()
        elif countCollege%2==1:
            collegelistbox.pack_forget()





    #listbox functions

    #Quota listbox
    def filloutQuota(event):
        quotaEntry.delete(0, tk.END)
        for i in quotaChoice.curselection():
            quotaEntry.insert(0, quotaChoice.get(i))


    selectedQuota=[]     #nonlocal variables for Quota selection
    dataQuota=[]
    def updateQuota(dataQuota):
        quotaChoice.delete(0,tk.END)
        i=0
        #printing the listbox
        for item in dataQuota:
            quotaChoice.insert(tk.END, item)
            if item in selectedQuota:
                quotaChoice.select_set(i)
            i+=1

    def checkQuota(event):
        nonlocal dataQuota
        nonlocal selectedQuota
        typed = quotaEntry.get()
        
        #updating the lisbox in each search
        temp=[]
        for i in quotaChoice.curselection():
            temp.append(quotaChoice.get(i))
            if quotaChoice.get(i) not in selectedQuota:
                if selectedQuota != []:
                    selectedQuota.pop()
                selectedQuota.append(quotaChoice.get(i))


        #updating dataQuota
        if typed == '':
            dataQuota = quotaLst
        else:
            dataQuota = []
            for item in quotaLst:
                if typed.lower() in item.lower():
                    dataQuota.append(item)
        
        updateQuota(dataQuota)


    #branch listbox
    selectedBranch=[]     #nonlocal variables for branch selection
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
        nonlocal dataBranch
        nonlocal selectedBranch
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
    selectedlocation=[]     #nonlocal variables for location selection
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
        nonlocal datalocation
        nonlocal selectedlocation
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
    selectedcollege=[]     #nonlocal variables for college selection
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
        nonlocal datacollege
        nonlocal selectedcollege
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
    global diction
    diction={}
    dataExtract(diction)



    #creating the window
    root=tk.Tk()
    root.title("College Predictor")
    root.state("zoomed")
    root.minsize(700, 650)
    bgimg = ImageTk.PhotoImage(Image.open("exam.jpg"))
    panel = tk.Label(root, image = bgimg)
    panel.place(x=0, y=0)



    #creating the form frames
    form=tk.Frame(root, relief="sunken", bg="#393646")
    form.pack(expand= False, padx=20, pady=80)

    rank=tk.Frame(form,relief="sunken", bg="#393646")
    rank.pack(fill=tk.BOTH, expand= True, pady=20, padx=20)

    quota=tk.Frame(form,relief="sunken", bg="#393646")
    quota.pack(fill=tk.BOTH, expand= True, pady=20, padx=20)
    quotaframe=tk.Frame(quota,relief="sunken", bg="#393646")
    quotadropdown=tk.Frame(quotaframe,relief="sunken", bg="#393646")
    quotalistbox=tk.Frame(quotaframe,relief="sunken", bg="#393646")

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

    submit=tk.Frame(form, relief="sunken", bg="#393646")
    submit.pack(fill=tk.BOTH, expand= True, pady=20, padx=20)



    #Initialising to string variable
    rankVar=tk.StringVar()
    btnimg = ImageTk.PhotoImage(Image.open("btn.png"))



    #creating rank form elements
    rankLabel=tk.Label(rank, text="Enter your Rank*:                ", font=("Ubuntu", 18), fg="#F4EEE0", bg="#393646")
    rankEntry=tk.Entry(rank, textvariable=rankVar, font=("Times New Roman", 20), relief="sunken", highlightbackground="#6D5D6E", highlightthickness=2, background="#F4EEE0")


    quotaLabel=tk.Label(quota, text="Select Category*:", font=("Ubuntu", 18), fg="#F4EEE0", bg="#393646")
    quotaEntry=tk.Entry(quotadropdown, font=("Times New Roman", 15), width=17, relief="sunken", highlightbackground="#6D5D6E", highlightthickness=1, background="#F4EEE0")
    quotaEntry.pack(side=tk.LEFT)
    scrollbar=tk.Scrollbar(quotalistbox, orient=tk.VERTICAL)
    quotaChoice=tk.Listbox(quotalistbox, width=29, relief="sunken", highlightbackground="#6D5D6E", highlightthickness=1, background="#F4EEE0", selectbackground="#6D5D6E", height=5, yscrollcommand=scrollbar.set)
    quotaChoice.configure(exportselection=False)
    scrollbar.config(command=quotaChoice.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    quotaChoice.pack()
    global quotaLst
    quotaLst=quota_lst(diction)
    quotaButton=tk.Button(quotadropdown, width=15, height=20, font=("Times New Roman", 10), image=btnimg, justify="center", bg="#6D5D6E", command=show_hidequota)

    quotaChoice.bind("<<ListboxSelect>>", filloutQuota)
    quotaEntry.bind("<KeyRelease>", checkQuota)
    updateQuota(quotaLst)

    branchLabel=tk.Label(branch, text="Select Preferred Branches*:", font=("Ubuntu", 18), fg="#F4EEE0", bg="#393646")
    branchEntry=tk.Entry(branchdropdown, font=("Times New Roman", 15), width=17, relief="sunken", highlightbackground="#6D5D6E", highlightthickness=1, background="#F4EEE0")
    branchEntry.pack(side=tk.LEFT)
    scrollbar=tk.Scrollbar(branchlistbox, orient=tk.VERTICAL)
    branchChoice=tk.Listbox(branchlistbox, width=29, relief="sunken", highlightbackground="#6D5D6E", highlightthickness=1, background="#F4EEE0", selectbackground="#6D5D6E", selectmode=tk.MULTIPLE, height=5, yscrollcommand=scrollbar.set)
    branchChoice.configure(exportselection=False)
    scrollbar.config(command=branchChoice.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    branchChoice.pack()
    global branchLst
    branchLst=branch_lst(diction)
    branchButton=tk.Button(branchdropdown, width=15, height=20, font=("Times New Roman", 10), image=btnimg, justify="center", bg="#6D5D6E", command=show_hidebranch)

    branchEntry.bind("<KeyRelease>", checkBranch)
    updateBranch(branchLst)


    locationLabel=tk.Label(location, text="Select Preferred Locations:", font=("Ubuntu", 18), fg="#F4EEE0", bg="#393646")
    locationEntry=tk.Entry(locationdropdown, font=("Times New Roman", 15), width=17, relief="sunken", highlightbackground="#6D5D6E", highlightthickness=1, background="#F4EEE0")
    locationEntry.pack(side=tk.LEFT)
    scrollbar=tk.Scrollbar(locationlistbox, orient=tk.VERTICAL)
    locationChoice=tk.Listbox(locationlistbox, width=29, relief="sunken", highlightbackground="#6D5D6E", highlightthickness=1, background="#F4EEE0", selectbackground="#6D5D6E", selectmode=tk.MULTIPLE, height=5, yscrollcommand=scrollbar.set)
    locationChoice.configure(exportselection=False)
    scrollbar.config(command=locationChoice.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    locationChoice.pack()
    global locationLst
    locationLst=location_lst(diction)
    locationButton=tk.Button(locationdropdown, width=15, height=20, font=("Times New Roman", 10), image=btnimg, justify="center", bg="#6D5D6E", command=show_hidelocation)

    locationEntry.bind("<KeyRelease>", checklocation)
    updatelocation(locationLst)




    collegeLabel=tk.Label(college, text="Select Preferred Colleges:", font=("Ubuntu", 18), fg="#F4EEE0", bg="#393646")
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
    global collegeLst
    collegeLst=college_lst(diction)
    collegeButton=tk.Button(collegedropdown, width=15, height=20, font=("Times New Roman", 10), image=btnimg, justify="center", bg="#6D5D6E", command=show_hidecollege)

    collegeEntry.bind("<KeyRelease>", checkcollege)
    updatecollege(collegeLst)

    submitBtn=tk.Button(submit, text="Submit" , background="#F4EEE0", foreground="#4F4557", activebackground="#4F4557", activeforeground="#F4EEE0", font="Ubuntu 12 bold", justify="center", command=lambda:validate())





    #placing the form elements
    rankLabel.pack(side=tk.LEFT)
    rankEntry.pack(side=tk.RIGHT)

    quotaLabel.pack(side=tk.LEFT, anchor=tk.NW)
    quotaframe.pack(side=tk.RIGHT, anchor=tk.NE)
    quotadropdown.pack()
    quotaButton.pack(side=tk.LEFT)

    branchLabel.pack(side=tk.LEFT, anchor=tk.NW)
    branchframe.pack(side=tk.RIGHT, anchor=tk.NE)
    branchdropdown.pack()
    branchButton.pack(side=tk.LEFT)

    locationLabel.pack(side=tk.LEFT, anchor=tk.NW)
    locationframe.pack(side=tk.RIGHT, anchor=tk.NW)
    locationdropdown.pack()
    locationButton.pack(side=tk.LEFT)

    collegeLabel.pack(side=tk.LEFT, anchor=tk.NW)
    collegeframe.pack(side=tk.RIGHT, anchor=tk.NE)
    collegedropdown.pack()
    collegeButton.pack(side=tk.LEFT)

    submitBtn.pack()



    root.mainloop()

FORM()