import tkinter as tk
from tkinter import ttk
from dataExt import *



#Extracting data from the csv file
diction={}
dataExtract(diction)



#creating the window
root=tk.Tk()
root.title("College Predictor")
root.config(bg="black")
root.state("zoomed")


#creating the form frames
form=tk.Frame(root, relief="sunken", bg="Black")
form.pack( expand= False, padx=20, pady=10)

rank=tk.Frame(form,relief="sunken", bg="Black")
rank.pack(fill=tk.BOTH, expand= True, pady=20)

quota=tk.Frame(form,relief="sunken", bg="Black")
quota.pack(fill=tk.BOTH, expand= True, pady=20)

branch=tk.Frame(form,relief="sunken", bg="Black")
branch.pack(fill=tk.BOTH, expand= True, pady=20)



#Initialising to string variable
rankVar=tk.StringVar()




#creating rank form elements
rankLabel=tk.Label(rank, text="Enter your Rank:           ", font=("Times New Roman", 20), fg="white", bg="black")
rankEntry=tk.Entry(rank, textvariable=rankVar, font=("Times New Roman", 20))

quotaLabel=tk.Label(quota, text="Choose your Quota:       ", font=("Times New Roman", 20), fg="white", bg="black")
quotaEntry=ttk.Combobox(quota, value=quota_lst(diction))
quotaEntry.current(0)

branchLabel=tk.Label(branch, text="Choose your Branch:     ", font=("Times New Roman", 20), fg="white", bg="black")
branchEntry=ttk.Combobox(branch, value=branch_lst(diction))
branchEntry.current(0)




#placing the form elements
rankLabel.pack(side=tk.LEFT)
rankEntry.pack(side=tk.RIGHT)

quotaLabel.pack(side=tk.LEFT)
quotaEntry.pack(side=tk.LEFT)

branchLabel.pack(side=tk.LEFT)
branchEntry.pack(side=tk.LEFT)





root.mainloop()