import os
from tkinter import filedialog

def add_path(parentwidget, listname ,paths):
    x = filedialog.askdirectory()
    if x != "":
        paths.append(x)
        list = parentwidget.children[listname]
        list.insert(0, x)
        save_paths(paths)

def load_paths():
    pathlist = []
    if os.path.isfile("paths.txt"):
        savefile = open("paths.txt", "r")
        for path in savefile.readlines():
            pathlist.append(path)
        savefile.close()
    else:
        savefile = open("paths.txt", "w")
        print("file not found, created one")
    return pathlist

def save_paths(paths):
    print("saving: ", paths)
    savefile = open("paths.txt", "w")
    for i in paths:
        savefile.write(i + "\n") 
    savefile.close()

def delete_path(parentwidget, listname, paths):
    list = parentwidget.children[listname]
    try:
        delete_index = list.curselection()[0]
        list.delete(delete_index)
        paths.pop(-delete_index-1)
        save_paths(paths)
    except IndexError:
        print("no path selected")


# todo
def export_results(parentwidget, listname):
    pass

def search():
    pass