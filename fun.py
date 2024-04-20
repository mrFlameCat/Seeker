""" Module contains functions for this program"""
import os
import time
import tkinter as tk
from tkinter import filedialog


def insert_results(widget, the_list):
    """This function take text widget and insert results of searching"""
    widget.delete("1.0", "end")
    for result in the_list:
        widget.insert("end", result + '\n')


def read_entry(entry_widget):
    """Read entry widget and return a value."""
    return entry_widget.get()


def single_dir(path, processed_list):
    """ This function take path and empty list for process.
     Do one level search only in directories"""
    if os.path.exists(path):
        for adress, directs, files in os.walk(path):
            for direct in directs:
                processed_list.append(os.path.join(adress, direct))
            break
        return processed_list
    else:
        print("The path don't exist")
        return "The path don't exist"


def single_file(path, processed_list):
    """ This function take path and empty list for process.
     Do one level search only in files"""
    if os.path.exists(path):
        for adress, directs, files in os.walk(path):
            for file in files:
                processed_list.append(os.path.join(adress, file))
            break
        return processed_list
    else:
        print("The path don't exist")
        return "The path don't exist"


def with_sub_dir(path, processed_list):
    """ This function take path and empty list for process.
     Searching only in folders with subfolders """
    if os.path.exists(path):
        for adress, directs, files in os.walk(path):
            for direct in directs:
                processed_list.append(os.path.join(adress, direct))
        return processed_list
    else:
        print("The path don't exist")
        return "The path don't exist"


def with_sub_files(path, processed_list):
    """ This function take path and empty list for process.
     Searching only files in folders and subfolders """
    if os.path.exists(path):
        for adress, directs, files in os.walk(path):
            for file in files:
                processed_list.append(os.path.join(adress, file))
        return processed_list
    else:
        print("The path don't exist")
        return "The path don't exist"


def reset_results_numb(label, var):
    """This function show number of search results"""
    label.config(text=f"Found {var} results.")


def select_path(entry):
    """This function insert path from filedialog to entry"""
    dialog_path = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, dialog_path)


def update_label(label, ins_text):
    """This function update text in the label"""
    label.config(text=ins_text)


def show_progress(my_progressbar):
    """this function show and start progressbar"""
    my_progressbar.place(relheight=0.05, relwidth=0.5, rely=0.915, relx=0.26)
    my_progressbar.start()


def hide_progress(my_progressbar):
    """This function stop and hide a progressbar"""
    my_progressbar.stop()
    my_progressbar.place_forget()