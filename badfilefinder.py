import tkinter, bffutils

from matplotlib.pyplot import fill
from unicodedata import name
from tkinter import ttk

pathlist = bffutils.load_paths()
root = tkinter.Tk()

root.title("Bad File Finder 0.01a")
root.minsize(340, 320)
root.geometry("640x700")
# window.iconbitmap("path/to/icon.ico") #window icon

# styles
red_fg_style = ttk.Style()
red_fg_style.configure('Delete.TButton', foreground='red')

# maincontainers
maincontainer= ttk.Frame(root)
# maincontainer.grid(row=0, column=0)    
maincontainer.pack(fill=tkinter.BOTH)    
maincontainer.rowconfigure(0, weight=0)
maincontainer.rowconfigure(6, weight=1)
maincontainer.columnconfigure(0, weight=1)

# searchbar
search_Label = ttk.Label(maincontainer,text="Search by Regular Expression",font=("Calibri", 12)).grid(row=0,column=0, pady=0, padx=2, sticky=tkinter.W, columnspan=1)
search_entry = ttk.Entry(maincontainer)
search_entry.grid(row=1,column=0, pady=2, padx=2, sticky=tkinter.W + tkinter.E, columnspan=3)
addpath_button = ttk.Button(maincontainer, text="Add Path", width=20, command= lambda:bffutils.add_path(maincontainer, "pathlistbox", pathlist) ).grid(row=4,column=2, pady=2, padx=2, sticky="e", columnspan=1)
search_button = ttk.Button(maincontainer,text="Search", width=20, command=lambda:bffutils.search(maincontainer, "resultlistbox" ,search_entry.get(), pathlist) ).grid(row=1,column=3, pady=2, padx=2, sticky=tkinter.W + tkinter.E, columnspan=1)

# path widgets
pathes_label = ttk.Label(maincontainer,text="Paths",font=("Calibri", 12)).grid(row=2,column=0, pady=0, padx=2, sticky="w", columnspan=1)
path_list = tkinter.Listbox(maincontainer, name="pathlistbox" ,listvariable=tkinter.StringVar(value=bffutils.load_paths()), height=5).grid(row=3,column=0, pady=2, padx=2, sticky=tkinter.W + tkinter.E, columnspan=4)
addpath_button = ttk.Button(maincontainer, text="Add Path", width=20, command= lambda:bffutils.add_path(maincontainer, "pathlistbox", pathlist) ).grid(row=4,column=2, pady=2, padx=2, sticky="e", columnspan=1)
deletepath_button = ttk.Button(maincontainer, text="Delete Path", width=20, style="Delete.TButton", command= lambda:bffutils.delete_path(maincontainer, "pathlistbox",pathlist)).grid(row=4,column=3, pady=2, padx=2, sticky="e", columnspan=1)

# results
result_label = ttk.Label(maincontainer,text="Results",font=("Calibri", 12)).grid(row=5,column=0, pady=0, padx=2, sticky="w", columnspan=1)
result_list = tkinter.Listbox(maincontainer, name="resultlistbox" ,listvariable=tkinter.StringVar([]), width=104, height=220).grid(row=6,column=0, pady=2, padx=2,sticky=tkinter.W + tkinter.E + tkinter.S + tkinter.N, columnspan=4)
open_button = ttk.Button(maincontainer, text="Open", width=20, command= lambda:bffutils.open_selection(maincontainer, "resultlistbox") ).grid(row=7,column=0, pady=2, padx=2, sticky=tkinter.W + tkinter.E + tkinter.S, columnspan=4)

maincontainer.pack() #needs to be packed after its content

if __name__ == "__main__":
    root.mainloop()