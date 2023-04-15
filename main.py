import tkinter as tk
from tkinter import ttk
from dataExt import *
from PIL import ImageTk, Image



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
form.pack(expand= False, padx=20, pady=200)

rank=tk.Frame(form,relief="sunken", bg="#454545")
rank.pack(fill=tk.BOTH, expand= True, pady=20, padx=20)

quota=tk.Frame(form,relief="sunken", bg="#454545")
quota.pack(fill=tk.BOTH, expand= True, pady=20, padx=20)

branch=tk.Frame(form,relief="sunken", bg="#454545")
branch.pack(fill=tk.BOTH, expand= True, pady=20, padx=20)



#Initialising to string variable
rankVar=tk.StringVar()




#creating rank form elements
rankLabel=tk.Label(rank, text="Enter your Rank:           ", font=("Times New Roman", 20), fg="#FFE6C7", bg="#454545")
rankEntry=tk.Entry(rank, textvariable=rankVar, font=("Times New Roman", 20), relief="sunken", highlightbackground="#FF6000", highlightthickness=2, background="#FFE6C7")

quotaLabel=tk.Label(quota, text="Select Category:                 ", font=("Times New Roman", 20), fg="#FFE6C7", bg="#454545")
quotaEntry=ttk.Combobox(quota, value=quota_lst(diction), justify="center")
quotaEntry.current(0)

branchLabel=tk.Label(branch, text="Select Branches:               ", font=("Times New Roman", 20), fg="#FFE6C7", bg="#454545")
branchEntry=ttk.Combobox(branch, value=branch_lst(diction), justify="center")
branchEntry.current(0)




#placing the form elements
rankLabel.pack(side=tk.LEFT)
rankEntry.pack(side=tk.LEFT)

quotaLabel.pack(side=tk.LEFT)
quotaEntry.pack(side=tk.LEFT)

branchLabel.pack(side=tk.LEFT)
branchEntry.pack(side=tk.LEFT)





root.mainloop()