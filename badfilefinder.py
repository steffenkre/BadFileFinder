import tkinter, bffutils
from unicodedata import name
from tkinter import ttk

pathlist = []

root = tkinter.Tk()

root.title("Bad File Finder 0.01a")
root.minsize(80, 80)
root.geometry("640x700")
# window.iconbitmap("path/to/icon.ico") #window icon

# styles
red_bg_style = ttk.Style()
red_bg_style.configure('Delete.TButton', foreground='red')

# maincontainers
maincontainer= ttk.Frame(root)

# searchbar
search_Label = ttk.Label(maincontainer,text="Search",font=("Calibri", 12)).grid(row=0,column=0, pady=2, padx=2, sticky="w", columnspan=1)
search_entry = ttk.Entry(maincontainer, width=80).grid(row=1,column=0, pady=2, padx=2, sticky="w", columnspan=1)
search_button = ttk.Button(maincontainer,text="Search", width=20).grid(row=1,column=1, pady=2, padx=2, sticky="w", columnspan=1)

# path widgets
pathes_label = ttk.Label(maincontainer,text="Pathss",font=("Calibri", 12)).grid(row=2,column=0, pady=12, padx=2, sticky="w", columnspan=1)
path_list = tkinter.Listbox(maincontainer, name="pathlistbox" ,listvariable=tkinter.StringVar(value=bffutils.load_paths()), width=104, height=5).grid(row=3,column=0, pady=2, padx=2, sticky="w", columnspan=2)
addpath_button = ttk.Button(maincontainer, text="Add Path", width=20, command= lambda:bffutils.add_path(maincontainer, "pathlistbox", pathlist) ).grid(row=4,column=0, pady=2, padx=2, sticky="e", columnspan=1)
deletepath_button = ttk.Button(maincontainer, text="Delete Path", width=20, style="Delete.TButton", command= lambda:bffutils.delete_path(maincontainer, "pathlistbox",pathlist)).grid(row=4,column=1, pady=2, padx=2, sticky="e", columnspan=1)

# results
result_label = ttk.Label(maincontainer,text="Results",font=("Calibri", 12)).grid(row=5,column=0, pady=12, padx=2, sticky="w", columnspan=1)
result_list = tkinter.Listbox(maincontainer, name="resultlistbox" ,listvariable=tkinter.StringVar(value=pathlist), width=104, height=24).grid(row=6,column=0, pady=2, padx=2, sticky="w", columnspan=2)
export_button = ttk.Button(maincontainer, text="Export Results", width=20, command= lambda:bffutils.export_results(maincontainer, "resultlistbox") ).grid(row=7,column=0, pady=2, padx=2, sticky="e", columnspan=2)

maincontainer.pack() #needs to be packed after its content

if __name__ == "__main__":
    root.mainloop()