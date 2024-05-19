"""This is program for search."""


import tkinter as tk
from tkinter import ttk
import threading
import fun


##################################### logical block ###################################

processed_list =  []
results_list = []
count = 0
update_id = None
proccess_flag = False


def start_function():
    """This function started search"""
    fun.update_label(lbl_wait, 'Please, wait...')
    fun.show_progress(progressbar)
    threading.Thread(target=main_function).start()



def main_function():
    """This function starting a main script."""
    global proccess_flag
    proccess_flag = True
    global count
    count =  0

    root.update()
    processed_list.clear()
    results_list.clear()
    path = fun.read_entry(where)
    target = fun.read_entry(what)

    if check_subfolders.get() == 1 and r_dirfiles.get() == 3:
        fun.with_sub_dir(path, processed_list)
        fun.with_sub_files(path, processed_list)
    if check_subfolders.get() == 1 and r_dirfiles.get() == 2:
        fun.with_sub_dir(path, processed_list)
    if check_subfolders.get() == 1 and r_dirfiles.get() == 1:
        fun.with_sub_files(path, processed_list)
    if check_subfolders.get() == 0 and r_dirfiles.get() == 3:
        fun.single_dir(path, processed_list)
        fun.single_file(path, processed_list)
    if check_subfolders.get() == 0 and r_dirfiles.get() == 2:
        fun.single_dir(path, processed_list)
    if check_subfolders.get() == 0 and r_dirfiles.get() == 1:
        fun.single_file(path, processed_list)
    

    if check_reg.get() == 1:
        target = target.lower()
        for index, item in enumerate(processed_list):
            processed_list[index] = item.lower()

    for i in processed_list:
        if target in i:
            count += 1
            results_list.append(i)
    fun.insert_results(text_field, results_list)
    fun.reset_results_numb(lbl_results, count)
    print(f"Processed: {len(processed_list)}")
    print(f"Results: {len(results_list)}")
    print(count)
    fun.update_label(lbl_wait, 'Done')
    fun.hide_progress(progressbar)
    proccess_flag = False

####################################### graphic block ###############################

root = tk.Tk()
root.title("Seeker")
root.geometry("1000x750+100+50")
check_subfolders = tk.IntVar(value=1)
check_reg = tk.IntVar(value=1)
var_for_bar = tk.IntVar
r_dirfiles = tk.IntVar(value=3)


top_frame = tk.LabelFrame(root, text='Menu')
bottom_frame = tk.LabelFrame(root, text='Results')
top_frame.place(relheight=0.48, relwidth=0.98, relx=0.01, rely=0.01)
bottom_frame.place(relheight=0.48, relwidth=0.98, relx=0.01, rely=0.51)

text_field = tk.Text(bottom_frame, font='Arial 14', padx=5, pady=5)
text_field.place(relheight=0.88, relwidth=1, relx=0, rely=0)

y_scroll = tk.Scrollbar(text_field, orient='vertical', command=text_field.yview)
y_scroll.pack(side='right', fill="y")

where = tk.Entry(top_frame)
where.configure(font=("Arial", 14))
where.place(relx=0.25, rely=0.1, relheight=0.07, relwidth=0.6)

lbl_where = tk.Label(top_frame, font=("Arial, 14"), text='Where are we looking?')
lbl_where.place(relx=0.01, rely=0.1, relheight=0.07, relwidth=0.23)

what = tk.Entry(top_frame)
what.configure(font=("Arial", 14))
what.place(relx=0.25, rely=0.2, relheight=0.07, relwidth=0.6)

lbl_what = tk.Label(top_frame, font=("Arial, 14"), text='What are we looking?')
lbl_what.place(relx=0.01, rely=0.2, relheight=0.07, relwidth=0.23)

btn_start = tk.Button(top_frame, font=("Arial, 14"), text="Start search", command=start_function)
btn_start.place(relheight=0.1, relwidth=0.2, rely=0.85, relx=0.78)


checkbtn_subfolders = tk.Checkbutton(top_frame, text='Search with subfolders',
                                     variable=check_subfolders)
checkbtn_subfolders.place(relx=0.01, rely=0.4)

checkbtn_register = tk.Checkbutton(top_frame, text='Ignore register',
                                     variable=check_reg)
checkbtn_register.place(relx=0.01, rely=0.5)


r_btn_in_both = ttk.Radiobutton(top_frame, text='Search folders and files',
                                variable=r_dirfiles, value=3)
r_btn_in_dir = ttk.Radiobutton(top_frame, text='Search only folders',
                                variable=r_dirfiles, value=2)
r_btn_in_files = ttk.Radiobutton(top_frame, text='Search only files',
                                variable=r_dirfiles, value=1)
r_btn_in_both.place(relx=0.25, rely=0.4)
r_btn_in_dir.place(relx=0.25, rely=0.5)
r_btn_in_files.place(relx=0.25, rely=0.6)

btn_browser = tk.Button(top_frame, text="Browse", font=("Arial, 14"),
                         command=lambda: fun.select_path(where))
btn_browser.place(relx=0.875, rely=0.1, relheight=0.07, relwidth=0.1)


lbl_results = tk.Label(bottom_frame, font="Arial, 14")
lbl_results.place(relheight=0.1, relwidth=0.2, rely=0.89, relx=0.78)

lbl_wait=tk.Label(bottom_frame, font="Arial, 14")
lbl_wait.place(relheight=0.1, relwidth=0.22, rely=0.89, relx=0.02)

progressbar = ttk.Progressbar(bottom_frame, orient='horizontal', variable=var_for_bar)

root.mainloop()



