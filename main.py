from tkinter import *
from tkinter import messagebox, filedialog
import os
import datetime

window = Tk()

window.geometry("680x490")
window.configure(bg="#ffffff")

path = 'C:\\Users\\john karl\\PycharmProjects\\SavedDocuments'
#start reading at the bottom
#==========================================frames========================================

frame = Frame(window, bg="#ffffff", height=490, width=680, bd=0, highlightthickness=0)
frame.pack(fill='both', expand=1)
frame1 = Frame(window, bg="#ffffff", height=490, width=680, bd=0, highlightthickness=0)
frame2 = Frame(window, bg="#ffffff", height=490, width=680, bd=0, highlightthickness=0)

#==========================================images========================================
#The images used in this code are defined globally so that other objects can access them

background_img1 = PhotoImage(file=f"second//background1.png")
background_img = PhotoImage(file=f"background.png")
background_img2 = PhotoImage(file=f"third//background.png")
img0 = PhotoImage(file=f"img0.png")
image0 = PhotoImage(file=f'second//image0.png')
image1 = PhotoImage(file=f"second//image1.png")
ts_button_img0 = PhotoImage(file=f"third//img0.png")
ts_button_img1 = PhotoImage(file=f"third//img1.png")

#======================================globalVariables====================================

identifier = ''
check_user = ''
ts_entry0 = ''
ts_entry1 = ''
ts_entry2 = ''
ts_entry3 = ''
ts_entry4 = ''
ts_entry5 = ''
ts_entry6 = ''


def forget_frames():
    frame.pack_forget()
    frame1.pack_forget()
    frame2.pack_forget()


#opens a file dialog so that the user can easily access the information written in the PC's local database

def show_directory():
    filedialog.askopenfilename(initialdir='SavedDocuments', title='Information Directory')


#this is the transition object between second and third frame in case the user wants to jump between the frames

def back():
    forget_frames()
    second_frame()


#this is how I save and organize the information scanned by the user. Enjoy reading!XD
def save_info():
    day = datetime.date.today()
    direct = 'C:\\Users\\john karl\\PycharmProjects\\test\\SavedDocuments'

    count = 0
    mon = f'{day.month}-{day.year}'
    new_folder = mon
    older = os.listdir(direct)

    if ts_entry0.get() == '' or ts_entry1.get() == '' or ts_entry2.get() == ''\
            or ts_entry3.get() == '' or ts_entry4.get() == '' or ts_entry5.get() == '' or\
            ts_entry6.get() == '':
        messagebox.showinfo('Signature Authentication System', 'Empty Information!')
    else:
        for folder in older:
            if folder == new_folder:
                count += 1

        file_now = datetime.datetime.now().date()
        cur_date = file_now.day
        print(count)

        if count != 1:
            os.chdir(direct)
            os.makedirs(new_folder)
            os.chdir(new_folder)
            os.makedirs(f'1st week')
            if cur_date <= 7:
                with open(f'{direct}\\{new_folder}\\1st week\\{file_now}.csv', 'w') as my_file:
                    my_file.write(f'Name,Middle Name, Last Name, Age, Sex, Personnel-in-Charge, Date of Transaction\n'
                                  f'{ts_entry0.get()},{ts_entry1.get()},{ts_entry2.get()},{ts_entry3.get()},'
                                  f'{ts_entry4.get()},{ts_entry5.get()}, {ts_entry6.get()}\n')
            os.makedirs(f'2nd week')
            if 7 < cur_date <= 14:
                with open(f'{direct}\\{new_folder}\\2nd week\\{file_now}.csv', 'w') as my_file:
                    my_file.write(f'Name,Middle Name, Last Name, Age, Sex, Personnel-in-Charge, Date of Transaction\n'
                                  f'{ts_entry0.get()},{ts_entry1.get()},{ts_entry2.get()},{ts_entry3.get()},'
                                  f'{ts_entry4.get()},{ts_entry5.get()}, {ts_entry6.get()}\n')
            os.makedirs(f'3rd week')
            if 14 < cur_date <= 21:
                with open(f'{direct}\\{new_folder}\\3rd week\\{file_now}.csv', 'w') as my_file:
                    my_file.write(f'Name,Middle Name, Last Name, Age, Sex, Personnel-in-Charge, Date of Transaction\n'
                                  f'{ts_entry0.get()},{ts_entry1.get()},{ts_entry2.get()},{ts_entry3.get()},'
                                  f'{ts_entry4.get()},{ts_entry5.get()}, {ts_entry6.get()}\n')
            os.makedirs(f'4th week')
            if cur_date > 21:
                with open(f'{direct}\\{new_folder}\\4th week\\{file_now}.csv', 'w') as my_file:
                    my_file.write(f'Name,Middle Name, Last Name, Age, Sex, Personnel-in-Charge, Date of Transaction\n'
                                  f'{ts_entry0.get()},{ts_entry1.get()},{ts_entry2.get()},{ts_entry3.get()},'
                                  f'{ts_entry4.get()},{ts_entry5.get()}, {ts_entry6.get()}\n')
        else:
            file_dir = os.listdir(f'{direct}//{new_folder}')
            for folder in file_dir:
                for sub in folder:
                    if cur_date <= 7 and sub == '1':
                        with open(f'{direct}\\{new_folder}\\1st week\\{file_now}.csv', 'r+') as my_file:
                            my_file.write(
                                f'{ts_entry0.get()},{ts_entry1.get()},{ts_entry2.get()},{ts_entry3.get()},'
                                f'{ts_entry4.get()},{ts_entry5.get()}, {ts_entry6.get()}\n')
                    elif 7 < cur_date <= 14 and sub == '2':
                        with open(f'{direct}\\{new_folder}\\2nd week\\{file_now}.csv', 'a') as my_file:
                            my_file.write(
                                f'{ts_entry0.get()},{ts_entry1.get()},{ts_entry2.get()},{ts_entry3.get()},'
                                f'{ts_entry4.get()},{ts_entry5.get()}, {ts_entry6.get()}\n')
                    elif 14 < cur_date <= 21 and sub == '3':
                        with open(f'{direct}\\{new_folder}\\3rd week\\{file_now}.csv', 'a') as my_file:
                            my_file.write(
                                f'{ts_entry0.get()},{ts_entry1.get()},{ts_entry2.get()},{ts_entry3.get()},'
                                f'{ts_entry4.get()},{ts_entry5.get()}, {ts_entry6.get()}\n')
                    elif cur_date > 21 and sub == '4':
                        with open(f'{direct}\\{new_folder}\\4th week\\{file_now}.csv', 'a') as my_file:
                            my_file.write(
                                f'{ts_entry0.get()},{ts_entry1.get()},{ts_entry2.get()},{ts_entry3.get()},'
                                f'{ts_entry4.get()},{ts_entry5.get()}, {ts_entry6.get()}\n')
                    else:
                        continue

        messagebox.showinfo('Signature Authentication System', 'Information Saved')
        ts_entry0.delete(0, END)
        ts_entry1.delete(0, END)
        ts_entry2.delete(0, END)
        ts_entry3.delete(0, END)
        ts_entry4.delete(0, END)


#====================================Third Frame/Information Frame============================================

def scan_image():
    global ts_entry0
    global ts_entry1
    global ts_entry2
    global ts_entry3
    global ts_entry4
    global ts_entry5
    global ts_entry6

    forget_frames()
    frame2.pack(fill='both', expand=1)
    ts_background = Label(frame2, image=background_img2)
    ts_background.pack()

    ts_b0 = Button(frame2, image=ts_button_img0, borderwidth=0, highlightthickness=0,
                   command=save_info, relief="flat")
    ts_b0.place(x=86, y=325, width=107, height=40)

    ts_b1 = Button(frame2, image=ts_button_img1, borderwidth=0, highlightthickness=0,
                   command=back, relief="flat")
    ts_b1.place(x=86, y=382, width=107, height=40)

    ts_entry0 = Entry(frame2, bd=0, bg="#c4c4c4", highlightthickness=0)
    ts_entry0.place(x=327.5, y=108, width=163.0, height=16)

    ts_entry1 = Entry(frame2, bd=0, bg="#c4c4c4", highlightthickness=0)
    ts_entry1.place(x=328.5, y=163, width=163.0, height=16)

    ts_entry2 = Entry(frame2, bd=0, bg="#c4c4c4", highlightthickness=0)
    ts_entry2.place(x=328.5, y=224, width=163.0, height=16)

    ts_entry3 = Entry(frame2, bd=0, bg="#c4c4c4", highlightthickness=0)
    ts_entry3.place(x=569.5, y=110, width=52.0, height=16)

    ts_entry4 = Entry(frame2, bd=0, bg="#c4c4c4", highlightthickness=0)
    ts_entry4.place(x=569.5, y=163, width=52.0, height=16)

    #since the name of personnel in charge is constant, We will just paste it directly on the entry box
    ts_entry5 = Entry(frame2, bd=0, bg="#c4c4c4", highlightthickness=0)
    ts_entry5.place(x=351.0, y=313, width=270.0, height=16)
    ts_entry5.insert(0, check_user)

    #so as the date
    our_date = datetime.datetime.now().date()
    ts_entry6 = Entry(frame2, bd=0, bg="#c4c4c4", highlightthickness=0)
    ts_entry6.place(x=569.5, y=365, width=52.0, height=16)
    ts_entry6.insert(0, str(our_date))


#=============================Second Frame/Operation Frame====================================

def second_frame():
    forget_frames()
    frame1.pack(fill='both', expand=1)
    ss_background = Label(frame1, image=background_img1)
    ss_background.pack()

    sf_b0 = Button(frame1, image=image0, borderwidth=0, highlightthickness=0, command=show_directory, relief="flat")
    sf_b0.place(x=154, y=280, width=104, height=40)

    sf_b1 = Button(frame1, image=image1, borderwidth=0, highlightthickness=0, command=scan_image, relief="flat")
    sf_b1.place(x=154, y=219, width=104, height=40)


#reset the initial state of the entry box and shows a messagebox containing some information

def verify():
    if identifier == 'correct':
        second_frame()
    elif identifier == 'wrong':
        messagebox.showinfo('Signature Authentication System', 'Wrong Credentials!')
    elif identifier == 'error':
        messagebox.showinfo('Signature Authentication System', 'Wrong Credentials!')
    else:
        messagebox.showinfo('Signature Authentication System', 'information box is empty!')

    user_entry.delete(0, END)
    password_entry.delete(0, END)


#checks for the validity of the credentials inputted by the user
def check():
    global identifier
    global check_user

    count = 0
    check_pass = password_entry.get()
    check_user = user_entry.get()

    with open('userinfo', 'r') as file:
        for line in file:
            if check_user in line:
                count += 1
                continue
            if check_pass in line:
                count += 1

    if check_user == '':
        count = 0
    if check_pass == '':
        count = 0

    if count == 2:
        identifier = 'correct'
        verify()
    elif count == 1:
        identifier = 'wrong'
        verify()
    elif count == 0 and len(check_user)+len(check_pass) > 0:
        identifier = 'error'
        verify()
    else:
        identifier = 'empty'
        verify()


#==================================first frame/Login Frame=========================================

fs_background = Label(frame, image=background_img)
fs_background.pack()

#entry box of username
user_entry = Entry(frame, bd=0, bg="#c4c4c4", highlightthickness=0)
user_entry.place(x=359.5, y=262, width=224.0, height=27)

#entry box of password
password_entry = Entry(frame, bd=0, bg="#c4c4c4", highlightthickness=0, show='*')
password_entry.place(x=360.5, y=339, width=222.0, height=29)

#in order to access the other object, we used the 'command=name of object' of Button Function
b0 = Button(frame, image=img0, borderwidth=0, highlightthickness=0, command=check, relief="flat")
b0.place(x=420, y=405, width=104, height=42)

window.resizable(False, False)
window.mainloop()
