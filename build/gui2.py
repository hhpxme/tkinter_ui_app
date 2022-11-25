from datetime import date, time
from pathlib import Path
from tkinter import Tk, Toplevel, Canvas, Entry, Label, Button, PhotoImage, messagebox
from tkinter import Scrollbar
from tkinter.ttk import Treeview
from tkinter import StringVar, IntVar, BooleanVar, DoubleVar
from tkinter import RIGHT, BOTH, END
from tkcalendar import DateEntry
import webbrowser
import get_link
import account

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"Y:\untitled_2\build\assets\frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Window Initialize
window = Tk()
# window.title = "App"
window.geometry("1440x1024")
window.configure(bg="#FFFFFF")
window.resizable(False, False)

# Variable
login_flag = BooleanVar(value=False)
notification_flag = BooleanVar(value=False)

link_root = 'https://firebasestorage.googleapis.com/v0/b/upload-video-536b1.appspot.com/o/'

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=1024,
    width=1440,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    1440.0,
    75.0,
    fill="#9CD0FA",
    outline=""
)

canvas.create_rectangle(
    0.0,
    975.0,
    1440.0,
    1024.0,
    fill="#FF6161",
    outline=""
)

canvas.create_rectangle(
    30.0,
    175.0,
    1410.0,
    950.0,
    fill="#FFFFFF",
    outline="#9CD0FA",
    width=5
)

# Date Text
canvas.create_text(
    35.0,
    18,
    anchor="nw",
    text=str(date.today().day) + '/' + str(date.today().month) + '/' + str(date.today().year),
    fill="#000000",
    font=("InriaSans Light", 36 * -1)
)


# Button Register
def register_toplevel():
    toplevel = Toplevel(window)
    toplevel.geometry("460x280")
    toplevel.configure(bg="#FFFFFF")
    toplevel.resizable(False, False)

    em_var = StringVar(master=toplevel)
    pw_var = StringVar(master=toplevel)
    rpw_var = StringVar(master=toplevel)
    c_var = IntVar(master=toplevel)
    code = IntVar(master=toplevel)

    cv = Canvas(
        toplevel,
        bg="#FFFFFF",
        height=280,
        width=460,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    cv.place(x=0, y=0)
    cv.create_text(
        71.0,
        12.0,
        anchor="nw",
        text="Register a new account",
        fill="#000000",
        font=("InriaSans Regular", 32 * -1)
    )

    cv.create_text(
        20.0,
        75.0,
        anchor="nw",
        text="Email:",
        fill="#000000",
        font=("InriaSans Regular", 20 * -1)
    )

    cv.create_text(
        20.0,
        115.0,
        anchor="nw",
        text="Password:",
        fill="#000000",
        font=("InriaSans Regular", 20 * -1)
    )

    cv.create_text(
        20.0,
        155.0,
        anchor="nw",
        text="Re-password:",
        fill="#000000",
        font=("InriaSans Regular", 20 * -1)
    )

    cv.create_text(
        20.0,
        195.0,
        anchor="nw",
        text="Verification Code:",
        fill="#000000",
        font=("InriaSans Regular", 20 * -1)
    )

    entry_email = Entry(
        master=toplevel,
        bd=1,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=1,
        highlightcolor="#9CD0FA",
        font=("InriaSans Regular", 20 * -1)
    )
    entry_email.place(
        x=80.0,
        y=72.5,
        width=350.0,
        height=28.0
    )
    entry_password = Entry(
        master=toplevel,
        bd=1,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=1,
        highlightcolor="#9CD0FA",
        font=("InriaSans Regular", 20 * -1)
    )
    entry_password.place(
        x=115.0,
        y=112.5,
        width=315.0,
        height=28.0
    )
    entry_repassword = Entry(
        master=toplevel,
        bd=1,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=1,
        highlightcolor="#9CD0FA",
        font=("InriaSans Regular", 20 * -1)
    )
    entry_repassword.place(
        x=145.0,
        y=152.5,
        width=285.0,
        height=28.0
    )
    entry_code = Entry(
        master=toplevel,
        bd=1,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=1,
        highlightcolor="#9CD0FA",
        font=("InriaSans Regular", 20 * -1)
    )
    entry_code.place(
        x=180.0,
        y=192.5,
        width=155.0,
        height=28.0,
    )

    def sendcode_press():
        if em_var.get() == '':
            messagebox.showerror(
                "Error",
                "Email cannot be blank!"
            )
        else:
            messagebox.showinfo(
                "Information",
                "Verification code have been send to your email.\nChecking email and input your code in here."
            )
            code.set(account.send_code(em_var.get()))
            print(code.get())

    button_sendcode = Button(
        master=toplevel,
        text='send code',
        bg="#FFFFFF",
        borderwidth=2,
        highlightthickness=2,
        highlightcolor="#9CD0FA",
        command=lambda: sendcode_press(),
        relief='raised',
        font=("InriaSans Regular", 14 * -1)
    )
    button_sendcode.place(
        x=345.0,
        y=191.0,
        width=85.0,
        height=30.0
    )

    def submit_press():
        # Validation input
        if em_var == '' or pw_var == '':
            messagebox.showerror(
                "Error",
                "Email and Password cannot be blank!"
            )
        elif rpw_var == '':
            messagebox.showerror(
                "Error",
                "Please input password again in re-password"
            )
        elif c_var == '':
            messagebox.showerror(
                "Error",
                "Verification code have been send to your email.\nChecking email and input your code in here."
            )
        elif em_var != '' and pw_var != '' and rpw_var != '' and c_var != '':
            e = em_var.get()
            p = pw_var.get()
            rpw = rpw_var.get()
            c = c_var.get()
            if rpw != p:
                messagebox.showerror(
                    "Error",
                    "Re-password is wrong.\nPlease checking again."
                )
            else:
                if c == code.get():
                    flag = account.register(e, p)
                    # if register success then destroy toplevel
                    if flag:
                        messagebox.showinfo("Information", "Register Successfully")
                        toplevel.destroy()
                    else:
                        messagebox.showinfo("Information", "Register Failed, Please again!")
                        toplevel.destroy()
                else:
                    messagebox.showerror(
                        "Error",
                        "Verification code is wrong.\nChecking email and input your code in here."
                    )

    button_submit = Button(
        master=toplevel,
        text='submit',
        bg="#FFFFFF",
        borderwidth=2,
        highlightthickness=2,
        highlightcolor="#9CD0FA",
        command=lambda: submit_press(),
        relief='raised',
        font=("InriaSans Regular", 16 * -1)
    )
    button_submit.place(
        x=193.0,
        y=235.0,
        width=75.0,
        height=30.0
    )


button_image_register = PhotoImage(
    file=relative_to_assets("button_register.png"))
button_register = Button(
    image=button_image_register,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: register_toplevel(),
    relief="flat"
)
button_register.place(
    x=1260.0,
    y=18.0,
    width=150.0,
    height=40.0
)


# Button Login
def login_toplevel():
    toplevel = Toplevel(window)
    toplevel.geometry("460x240")
    toplevel.configure(bg="#FFFFFF")
    toplevel.resizable(False, False)

    em_var = StringVar(master=toplevel)
    pw_var = StringVar(master=toplevel)
    c_var = IntVar(master=toplevel)
    code = IntVar(master=toplevel)

    cv = Canvas(
        toplevel,
        bg="#FFFFFF",
        height=240,
        width=460,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    cv.place(x=0, y=0)
    cv.create_text(
        71.0,
        12.0,
        anchor="nw",
        text="Login",
        fill="#000000",
        font=("InriaSans Regular", 32 * -1)
    )

    cv.create_text(
        20.0,
        75.0,
        anchor="nw",
        text="Email:",
        fill="#000000",
        font=("InriaSans Regular", 20 * -1)
    )

    cv.create_text(
        20.0,
        115.0,
        anchor="nw",
        text="Password:",
        fill="#000000",
        font=("InriaSans Regular", 20 * -1)
    )

    cv.create_text(
        20.0,
        155.0,
        anchor="nw",
        text="Verification Code:",
        fill="#000000",
        font=("InriaSans Regular", 20 * -1)
    )

    entry_email = Entry(
        master=toplevel,
        bd=1,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=1,
        highlightcolor="#9CD0FA",
        font=("InriaSans Regular", 20 * -1),
        textvariable=em_var
    )
    entry_email.place(
        x=80.0,
        y=72.5,
        width=350.0,
        height=28.0
    )
    entry_password = Entry(
        master=toplevel,
        bd=1,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=1,
        highlightcolor="#9CD0FA",
        font=("InriaSans Regular", 20 * -1),
        show='*',
        textvariable=pw_var
    )
    entry_password.place(
        x=115.0,
        y=112.5,
        width=315.0,
        height=28.0
    )
    entry_code = Entry(
        master=toplevel,
        bd=1,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=1,
        highlightcolor="#9CD0FA",
        font=("InriaSans Regular", 20 * -1),
        textvariable=c_var
    )
    entry_code.place(
        x=180.0,
        y=152.5,
        width=155.0,
        height=28.0,
    )

    def sendcode_press():
        if em_var.get() == '' or pw_var.get() == '':
            messagebox.showerror(
                "Error",
                "Email and Password cannot be blank!"
            )
        else:
            messagebox.showinfo(
                "Information",
                "Verification code have been send to your email.\nChecking email and input your code in here."
            )
            code.set(account.send_code(em_var.get()))
            print(code.get())

    button_sendcode = Button(
        master=toplevel,
        text='send code',
        bg="#FFFFFF",
        borderwidth=2,
        highlightthickness=2,
        highlightcolor="#9CD0FA",
        command=lambda: sendcode_press(),
        relief='raised',
        font=("InriaSans Regular", 16 * -1)
    )
    button_sendcode.place(
        x=345.0,
        y=151.0,
        width=85.0,
        height=30.0
    )

    def submit_press():
        # Validation input
        if em_var == '' or pw_var == '':
            messagebox.showerror(
                "Error",
                "Email and Password cannot be blank!"
            )
        elif c_var == '':
            messagebox.showerror(
                "Error",
                "Verification code have been send to your email.\nChecking email and input your code in here."
            )
        elif em_var != '' and pw_var != '' and c_var != '':
            e = em_var.get()
            p = pw_var.get()
            c = c_var.get()
            if str(c) == str(code.get()):
                flag = account.login(e, p)
                # if login success then destroy toplevel and delete button login, register
                if flag:
                    messagebox.showinfo("Information", "Login Successfully")
                    toplevel.destroy()
                    canvas.delete(button_image_register)
                    canvas.delete(button_image_register)
                    canvas.delete(button_register)
                    canvas.delete(button_login)
                else:
                    messagebox.showinfo("Information", "Login Failed, Please again!")
                    toplevel.destroy()
            else:
                messagebox.showerror(
                    "Error",
                    "Verification code is wrong.\nChecking email and input your code in here."
                )

    button_submit = Button(
        master=toplevel,
        text='submit',
        bg="#FFFFFF",
        borderwidth=2,
        highlightthickness=2,
        highlightcolor="#9CD0FA",
        command=lambda: submit_press(),
        relief='raised',
        font=("InriaSans Regular", 16 * -1)
    )
    button_submit.place(
        x=193.0,
        y=195.0,
        width=75.0,
        height=30.0
    )


button_image_login = PhotoImage(
    file=relative_to_assets("button_login.png"))
button_login = Button(
    image=button_image_login,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: login_toplevel(),
    relief="flat"
)
button_login.place(
    x=1100.0,
    y=18.0,
    width=150.0,
    height=40.0
)

# Listbox link video    30.0, 175.0, 1410.0, 950.0
treeview_columns = ('name', 'date_created')
treeview = Treeview(
    window,
    columns=treeview_columns,
    show='headings',
)
treeview.heading('name', text='Name')
treeview.heading('date_created', text='Date Created')

video_data = get_link.get_video_data()
i = 0
# for name in file_name:
#     print(name)
for data in video_data:
    treeview.insert('', END, values=data)
    if i >= 1000:
        i = 0
        break

treeview.place(
    x=32.5,
    y=177.5,
    width=1375,
    height=770,
)

scroll_bar = Scrollbar(treeview)
scroll_bar.pack(side=RIGHT, fill=BOTH, pady=1)
treeview.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=treeview.yview)


def select_press():
    for selected_item in treeview.selection():
        item = treeview.item(selected_item)
        record = item['values'][0]
        webbrowser.open(link_root + str(record) + '?alt=media')


# Button Select
button_image_select = PhotoImage(
    file=relative_to_assets("button_select.png"))
button_select = Button(
    image=button_image_select,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: select_press(),
    relief="flat"
)
button_select.place(
    x=30.0,
    y=100.0,
    width=195.0,
    height=50.0
)


# Button show full list video
def show_press():
    for item in treeview.get_children():
        treeview.delete(item)

    v_data = get_link.get_video_data()
    c = 0
    for d in v_data:
        treeview.insert('', END, values=d)
        if c >= 1000:
            break


button_image_show = PhotoImage(
    file=relative_to_assets("button_show.png"))
button_show = Button(
    image=button_image_show,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_press(),
    relief="flat"
)
button_show.place(
    x=600.0,
    y=100.0,
    width=195.0,
    height=50.0
)

# Filter Area
entry_image_dentry_start = PhotoImage(
    file=relative_to_assets("entry.png"))
entry_bg_dentry_start = canvas.create_image(
    935.0,
    125.0,
    image=entry_image_dentry_start
)
entry_dentry_start = DateEntry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 22 * -1)
)
entry_dentry_start.place(
    x=813.0,
    y=103.0,
    width=244.0,
    height=44.0
)

canvas.create_text(
    1075.0,
    110.0,
    anchor="nw",
    text="-",
    fill="#000000",
    font=("Inter", 24 * -1)
)

entry_image_dentry_end = PhotoImage(
    file=relative_to_assets("entry.png"))
entry_bg_dentry_end = canvas.create_image(
    1225.0,
    125.0,
    image=entry_image_dentry_end
)
entry_dentry_end = DateEntry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 22 * -1)
)
entry_dentry_end.place(
    x=1103.0,
    y=103.0,
    width=244.0,
    height=44.0
)


def date_filter():
    for item in treeview.get_children():
        treeview.delete(item)

    d_start = entry_dentry_start.get_date()
    d_end = entry_dentry_end.get_date()

    v_data = get_link.get_video_data()
    c = 0
    for n, d in v_data:
        date_data = str(d).split('-')
        if int(d_start.day) <= int(date_data[2]) <= int(d_end.day) and int(d_start.month) <= int(date_data[1]) <= int(d_end.month) and int(d_start.year) <= int(date_data[0]) <= int(d_end.year):
            treeview.insert('', END, values=[n, d])
            if c >= 1000:
                break


# Button OK
button_image_ok = PhotoImage(
    file=relative_to_assets("button_ok.png"))
button_ok = Button(
    image=button_image_ok,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: date_filter(),
    relief="flat"
)
button_ok.place(
    x=1360.0,
    y=100.0,
    width=50.0,
    height=50.0
)

# mainloop
window.mainloop()
