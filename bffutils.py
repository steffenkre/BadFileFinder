import os, re
from tkinter import filedialog, messagebox
import tkinter

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
        savefile.writelines(i)
        #add new line if not last line
        if i != paths[-1]:
            savefile.write("\n")
    savefile.close()

def delete_path(parentwidget, listname, paths):
    list = parentwidget.children[listname]
    MsgBox = messagebox.askquestion ('Delete Path','Do you want to delete the selected path?')
    if MsgBox == 'yes':
        try:
            delete_index = list.curselection()[0]
            list.delete(delete_index)
            paths.pop(delete_index)
            save_paths(paths)
        except IndexError:
            print("no path selected")

def mute_path(parentwidget, listname, paths):
    list = parentwidget.children[listname]
    try:
        mute_index = list.curselection()[0]
        print(mute_index)
        mute_value = list.get(mute_index)
        if "- (muted)" not in mute_value:
            list.delete(mute_index) 
            list.insert(mute_index, mute_value + " - (muted)")
            paths[mute_index] = mute_value + " - (muted)"
        else:
            list.delete(mute_index) 
            list.insert( mute_index, mute_value.replace(" - (muted)", "") )
            paths[mute_index] = mute_value.replace(" - (muted)", "")
        save_paths(paths)
    except IndexError:
        print("cant mute path")


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
    path = list.get(list.curselection())
    #ecape spaces in path for os.system
    path = path.replace(" ", "\\ ")
    print (path)
    os.system(path)

def add_to_favorites(parentwidget, pathlistname, listname):
    pathlist = parentwidget.children[pathlistname]
    favlist = parentwidget.children[listname]
    path = pathlist.get(pathlist.curselection())
    favlist.insert(0, path)
    pass

def remove_from_favorites(parentwidget, listname):
    favlist = parentwidget.children[listname]
    try:
        for i in favlist.curselection():
            favlist.delete(i)
    except IndexError:
        print("no favorite selected")

def clear_favorites(parentwidget, listname):
    favlist = parentwidget.children[listname]
    #remove all entries from list
    favlist.delete(0, 'end')

def export_to_bash(parentwidget, listname):
    #create save file dialog
    savefile = filedialog.asksaveasfile(mode='w', defaultextension=".sh")
    if savefile != None:
        list = parentwidget.children[listname]
        for i in list.get(0, 'end'):
            savefile.write( "cp '"+ i +"'\n")
        savefile.close()