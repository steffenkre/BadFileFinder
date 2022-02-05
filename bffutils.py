import os, re
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
        for path in savefile.read().splitlines():
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

def search(parentwidget, listname, searchterm, paths):
    parentwidget.config(cursor="wait")
    if searchterm != "":
        list = parentwidget.children[listname]
        list.delete(0,'end')
        for path in paths:
            #check if path is valid
            if os.path.isdir(path):
                for p,d,f in os.walk(path):
                    for i in f:
                        match = re.match(searchterm.lower(), i.lower())
                        if  match:
                            list.insert(0, p.replace("\\", "/")+"/"+i)
    parentwidget.config(cursor="")


def open_selection(parentwidget, listname):
    list = parentwidget.children[listname]
    os.system(list.get(list.curselection()) )

