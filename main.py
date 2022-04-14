import tkinter, bffutils
from tkinter import ttk

pathlist = bffutils.load_paths()
root = tkinter.Tk()

root.title("Bad File Finder 0.02 Alpha")
root.minsize(395, 400)
root.geometry("640x700")
root.config(cursor="arrow")
# window.iconbitmap("path/to/icon.ico") #window icon

#dirty helper function
def return_pressed(e):
    bffutils.search(maincontainer, "resultlistbox" ,search_entry.get(), pathlist)

# styles
red_fg_style = ttk.Style()
red_fg_style.configure('Delete.TButton', foreground='red')

#file menu
menubar = tkinter.Menu(root)
filemenu = tkinter.Menu(root)
filemenu.add_command(label="Export Copy-Bashfile", command=lambda:bffutils.export_to_bash(maincontainer, "favoriteslistbox") )
filemenu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)


# maincontainers
maincontainer= tkinter.Frame(root, padx=2, pady=2)
maincontainer.pack(fill=tkinter.BOTH, expand=True)    

#subcontainers
search_container = tkinter.Frame(maincontainer)
path_container = tkinter.Frame(maincontainer)
result_container = tkinter.Frame(maincontainer)
favorites_container = tkinter.Frame(maincontainer, pady=2)

# searchbar
search_Label = ttk.Label(maincontainer,text="Search by Regular Expression",font=("Calibri", 12))
search_entry = ttk.Entry(search_container)
search_entry.bind("<Return>", return_pressed ) 
search_button = ttk.Button(search_container,text="Search 🔍", width=20 ,command=lambda:bffutils.search(maincontainer, "resultlistbox" ,search_entry.get(), pathlist) )

# path widgets
paths_label = ttk.Label(maincontainer,text="Paths",font=("Calibri", 12))
path_list = tkinter.Listbox(maincontainer, name="pathlistbox" ,listvariable=tkinter.StringVar(value=bffutils.load_paths()), height=5)
mute_button = ttk.Button(path_container, text="Mute Paths", width=20 ,command= lambda:bffutils.mute_path(maincontainer, "pathlistbox", pathlist) )
addpath_button = ttk.Button(path_container, text="Add Path 📌", width=20 ,command= lambda:bffutils.add_path(maincontainer, "pathlistbox", pathlist) )
deletepath_button = ttk.Button(path_container, text="Delete Path ❌", width=20 ,style="Delete.TButton", command= lambda:bffutils.delete_path(maincontainer, "pathlistbox",pathlist))

# result widgets
result_label = ttk.Label(maincontainer,text="Results",font=("Calibri", 12))
result_list = tkinter.Listbox(maincontainer, name="resultlistbox" , listvariable=[], height=2)
add_to_favorites_button = ttk.Button(result_container, text="↓ Add to Favorites ↓",width=20, command= lambda:bffutils.add_to_favorites(maincontainer, "resultlistbox","favoriteslistbox") )
open_button = ttk.Button(result_container, text="Open 📁",width=20 , command= lambda:bffutils.open_selection(maincontainer, "resultlistbox") )

#favorite widgets
favorite_list = tkinter.Listbox(maincontainer, name="favoriteslistbox", selectmode='multiple',listvariable=[], height=2)
# export_favorites_to_sh = ttk.Button(favorites_container, text="Export Bashscript ✔",width=20, command=lambda:bffutils.export_to_bash(maincontainer, "favoriteslistbox") )
remove_favorite = ttk.Button(favorites_container, text="Remove Favorite",width=20, command=lambda:bffutils.remove_from_favorites(maincontainer, "favoriteslistbox") )
clear_favorites = ttk.Button(favorites_container, text="Clear Favorites ❌",width=20, style="Delete.TButton", command=lambda:bffutils.clear_favorites(maincontainer, "favoriteslistbox") )

# pack subcontainers
search_entry.pack(side="left", fill="x", expand=True)
search_button.pack(fill="x", expand=True)
addpath_button.pack(side="right")
mute_button.pack(side="right")
deletepath_button.pack(side="right")
open_button.pack(side="right")
add_to_favorites_button.pack(side="right", fill="x", expand=True)
# export_favorites_to_sh.pack(side="left", fill="x", expand=True)
clear_favorites.pack(side="right")
remove_favorite.pack(side="right")

# pack to maincontainer
search_Label.pack(fill="x", anchor="n")
search_container.pack(fill="x", anchor="n")
paths_label.pack(fill="x", anchor="n")
path_list.pack(fill="x", anchor="n")
path_container.pack(fill="x", anchor="n")
result_label.pack(fill="x", anchor="n")
result_list.pack(fill="both", expand=True, anchor="n")
result_container.pack(fill="x", anchor="n")
favorite_list.pack(fill="both", expand=True, anchor="n")
favorites_container.pack(fill="x", anchor="s")

maincontainer.pack()

if __name__ == "__main__":
    root.mainloop()

