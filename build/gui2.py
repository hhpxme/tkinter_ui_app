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
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame2")


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

link_root = 'https://firebasestorage.googleapis.com/v0/b/videodetect-ae8df.appspot.com/o/'

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


# Login State
button_image_register = PhotoImage(
    file=relative_to_assets("button_register.png"))
button_register = Button(
    master=window,
    image=button_image_register,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: register_toplevel(),
    relief="flat"
)
button_image_login = PhotoImage(
    file=relative_to_assets("button_login.png"))
button_login = Button(
    master=window,
    image=button_image_login,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: login_toplevel(),
    relief="flat"
)
button_image_logout = PhotoImage(
    file=relative_to_assets("button_logout.png"))
button_logout = Button(
    master=window,
    image=button_image_logout,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: logout_account(),
    relief="flat",
)


def logout_account():
    q = messagebox.askokcancel('Logout', 'Do you want to logout ?')
    if q:
        login_flag.set(False)
        login_show()
        delete_all_video()
    else:
        pass


def login_show():
    button_register.place(
        x=1260.0,
        y=18.0,
        width=150.0,
        height=40.0
    )
    button_login.place(
        x=1100.0,
        y=18.0,
        width=150.0,
        height=40.0
    )
    button_logout.place_forget()


def logout_show():
    button_logout.place(
        x=1370.0,
        y=18.0,
        width=40.0,
        height=40.0
    )
    button_login.place_forget()
    button_register.place_forget()


if login_flag.get():
    logout_show()
else:
    login_show()


# Button Register
def register_toplevel():
    toplevel = Toplevel(window)
    toplevel.geometry("640x520")
    toplevel.configure(bg="#FFFFFF")
    toplevel.resizable(False, False)

    em_var = StringVar(master=toplevel)
    pw_var = StringVar(master=toplevel)
    cpw_var = StringVar(master=toplevel)

    cv = Canvas(
        toplevel,
        bg="#FFFFFF",
        width=640,
        height=520,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    cv.place(x=0, y=0)
    cv.create_rectangle(
        0.0,
        0.0,
        640.0,
        100.0,
        fill="#D9D9D9",
        outline=""
    )
    cv.create_rectangle(
        1.5,
        100.0,
        638.5,
        518.5,
        fill="#FFFFFF",
        outline="#F88077",
        width=3
    )

    cv.create_text(
        45.0,
        10.0,
        anchor="nw",
        text="Register",
        fill="#000000",
        font=("InriaSans Regular", 48 * -1)
    )
    cv.create_text(
        45.0,
        65.0,
        anchor="nw",
        text="You need an account to use the application",
        fill="#000000",
        font=("InriaSans Regular", 16 * -1)
    )

    cv.create_text(
        45.0,
        125.0,
        anchor="nw",
        text="Email:",
        fill="#000000",
        font=("InriaSans Regular", 24 * -1)
    )

    cv.create_text(
        45.0,
        225.0,
        anchor="nw",
        text="Password:",
        fill="#000000",
        font=("InriaSans Regular", 24 * -1)
    )

    cv.create_text(
        45.0,
        325.0,
        anchor="nw",
        text="Confirm Password:",
        fill="#000000",
        font=("InriaSans Regular", 24 * -1)
    )

    entry_email = Entry(
        master=toplevel,
        bd=2,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=2,
        highlightcolor="#9CD0FA",
        font=("InriaSans Regular", 24 * -1),
        textvariable=em_var
    )
    entry_email.place(
        x=45.0,
        y=160.0,
        width=550.0,
        height=50.0
    )
    entry_password = Entry(
        master=toplevel,
        bd=2,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=2,
        highlightcolor="#9CD0FA",
        font=("InriaSans Regular", 24 * -1),
        show='*',
        textvariable=pw_var
    )
    entry_password.place(
        x=45.0,
        y=260.0,
        width=550.0,
        height=50.0
    )
    entry_repassword = Entry(
        master=toplevel,
        bd=2,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=2,
        highlightcolor="#9CD0FA",
        font=("InriaSans Regular", 24 * -1),
        textvariable=cpw_var
    )
    entry_repassword.place(
        x=45.0,
        y=360,
        width=550.0,
        height=50.0
    )

    def submit_press():
        # Validation input
        if em_var == '' or pw_var == '':
            messagebox.showerror(
                "Error",
                "Email and Password cannot be blank!"
            )
        elif str(em_var.get()).find('@gmail.com') == -1:
            messagebox.showerror(
                "Error",
                "Type of Email is wrong!"
            )
        elif cpw_var == '':
            messagebox.showerror(
                "Error",
                "Please input password again in re-password"
            )
        elif em_var != '' and pw_var != '' and cpw_var != '':
            e = em_var.get()
            p = pw_var.get()
            cpw = cpw_var.get()
            if cpw != p:
                messagebox.showerror(
                    "Error",
                    "Confirm-password is wrong.\nPlease checking again."
                )
            else:
                try:
                    account.register(e, p)
                    messagebox.showwarning("Information", "A link has been sent to your email\nPlease check your email and verified your account\nIf after 15 days, account was not verified. Account will be deleted")
                    messagebox.showinfo("Information", "Register Successfully")
                    toplevel.destroy()
                except:
                    messagebox.showinfo("Information", "Register Failed")

    button_submit = Button(
        master=toplevel,
        text='Submit',
        bg="#FFFFFF",
        borderwidth=2,
        highlightthickness=2,
        highlightcolor="#9CD0FA",
        command=lambda: submit_press(),
        relief='raised',
        font=("InriaSans Regular", 28 * -1)
    )
    button_submit.place(
        x=220.0,
        y=440.0,
        width=200.0,
        height=40.0
    )


# Button Login
def login_toplevel():
    toplevel = Toplevel(window)
    toplevel.geometry("640x360")
    toplevel.configure(bg="#FFFFFF")
    toplevel.resizable(False, False)

    em_var = StringVar(master=toplevel)
    pw_var = StringVar(master=toplevel)

    cv = Canvas(
        toplevel,
        bg="#FFFFFF",
        width=640,
        height=360,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    cv.place(x=0, y=0)
    cv.create_rectangle(
        0.0,
        0.0,
        640.0,
        100.0,
        fill="#9CD0FA",
        outline=""
    )
    cv.create_rectangle(
        0.0,
        100.0,
        638.5,
        358.5,
        fill="#FFFFFF",
        outline="#F88077",
        width=3
    )

    cv.create_text(
        45.0,
        10.0,
        anchor="nw",
        text="Welcome",
        fill="#000000",
        font=("InriaSans Regular", 48 * -1)
    )
    cv.create_text(
        45.0,
        65.0,
        anchor="nw",
        text="Login to continue your work",
        fill="#000000",
        font=("InriaSans Regular", 16 * -1)
    )

    cv.create_text(
        45.0,
        145.0,
        anchor="nw",
        text="Email:",
        fill="#000000",
        font=("InriaSans Regular", 36 * -1)
    )

    cv.create_text(
        45.0,
        215.0,
        anchor="nw",
        text="Password:",
        fill="#000000",
        font=("InriaSans Regular", 36 * -1)
    )

    entry_email = Entry(
        master=toplevel,
        bd=2,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=2,
        highlightcolor="#9CD0FA",
        font=("InriaSans Regular", 24 * -1),
        textvariable=em_var
    )
    entry_email.place(
        x=245.0,
        y=140.0,
        width=350.0,
        height=50.0
    )
    entry_password = Entry(
        master=toplevel,
        bd=2,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=2,
        highlightcolor="#9CD0FA",
        font=("InriaSans Regular", 24 * -1),
        show='*',
        textvariable=pw_var
    )
    entry_password.place(
        x=245.0,
        y=210.0,
        width=350.0,
        height=50.0
    )

    def submit_press():
        # Validation input
        if em_var == '' or pw_var == '':
            messagebox.showerror(
                "Error",
                "Email and Password cannot be blank!"
            )
        elif str(em_var.get()).find('@gmail.com') == -1:
            messagebox.showerror(
                "Error",
                "Type email is wrong!"
            )
        else:
            e = em_var.get()
            p = pw_var.get()
            flag = account.login(e, p)
            # if login success then destroy toplevel and delete button login, register
            if flag >= 0:
                messagebox.showinfo("Information", "Login Successfully")
                login_flag.set(True)
                toplevel.destroy()
                logout_show()
                get_video()
            elif flag == -2:
                messagebox.showwarning("Verified Request", 'Please verified account to use app')
            elif flag == -1:
                messagebox.showinfo("Information", "Login Failed, Please again!")
                login_flag.set(False)
                toplevel.destroy()

    button_submit = Button(
        master=toplevel,
        text='Submit',
        bg="#FFFFFF",
        borderwidth=2,
        highlightthickness=2,
        highlightcolor="#9CD0FA",
        command=lambda: submit_press(),
        relief='raised',
        font=("InriaSans Regular", 28 * -1)
    )
    button_submit.place(
        x=220,
        y=287.0,
        width=200.0,
        height=40.0
    )


# Listbox link video    30.0, 175.0, 1410.0, 950.0
treeview_columns = ('name', 'date_created', 'ip')
treeview = Treeview(
    window,
    columns=treeview_columns,
    show='headings',
)
treeview.heading('name', text='Name')
treeview.heading('date_created', text='Date Created')
treeview.heading('ip', text='From IP')
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


def delete_all_video():
    for item in treeview.get_children():
        treeview.delete(item)


def get_video():
    if login_flag.get():
        video_data = get_link.get_video_data()
        i = 0
        delete_all_video()
        for data in video_data:
            treeview.insert('', END, values=data)
            if i >= 1000:
                break
    else:
        pass


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


button_image_show = PhotoImage(
    file=relative_to_assets("button_show.png"))
button_show = Button(
    image=button_image_show,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: get_video(),
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
    if login_flag.get():
        delete_all_video()

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
    else:
        pass


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
