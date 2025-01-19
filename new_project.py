from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import datetime
import mysql.connector
import webbrowser 
import random

myconn = mysql.connector.connect(user="root", password="#Deepti2003", host="127.0.0.1", database="priti")
cursor = myconn.cursor()

root = Tk()
root.state("zoomed") 
root.resizable(False,False)

session = {}

home_bg_image = ImageTk.PhotoImage(Image.open("b6.png").resize((1600,800)))
login_bg_image = ImageTk.PhotoImage(Image.open("b4.png").resize((1600,800)))
forgot_bg_image = ImageTk.PhotoImage(Image.open("password.png").resize((1600,800)))
registor_bg_image = ImageTk.PhotoImage(Image.open("v.png").resize((1600,900)))
admin_bg_image = ImageTk.PhotoImage(Image.open("a10.png").resize((1200,720)))
faculty_bg_image = ImageTk.PhotoImage(Image.open("a7.png").resize((1200,800)))
student_bg_image = ImageTk.PhotoImage(Image.open("a8.png").resize((1200,800)))
principal_bg_image = ImageTk.PhotoImage(Image.open("a11.png").resize((1200,800)))
function_bg_image = ImageTk.PhotoImage(Image.open("a5.png").resize((1200,800)))

canvas = Canvas(root, width=1550, height=800)
canvas.pack(fill="both", expand=True)

def set_background(image):
    canvas.delete("all")
    canvas.create_image(0,0, image=image, anchor="nw")

def Cancel():
    print("Form Cancelled")
    root.quit()

def side_frame():
    frame = Frame(root, bg="#290916", relief="groove", bd=3)
    frame.place(x=2, y=71, width=350, height=730)
    # Create the canvas within the frame
    canvas = Canvas(frame, bg="#290916", highlightthickness=0)
    canvas.place(x=0, y=0, relwidth=1, relheight=1)
    
    # Add the image to the canvas
    canvas.create_image(0,-76, anchor="nw", image=login_bg_image)

def lower_frame():
    frame = Frame(root, bg="#290916", relief="groove",bd=0)
    frame.place(x=0, y=785, width=1600, height=60) 
    Button(root, text="LOGOUT", bg="#2B6CB0", fg="#E2E8F0", font=("Arial", 11, "bold"),  width=8, bd=5, command= home_page).place(x=1390, y=795)

def clear_frame():
    for widget in root.winfo_children():
        if widget != canvas:
            widget.destroy()

def create_canvas_text(canvas, x, y, text, font, fill, anchor="center"):
    canvas.create_text(x, y, text=text, font=font, fill=fill, anchor=anchor)

def on_enter(e):
    e.widget.config(bg="#290916", fg="orange")

def on_leave(e):
    e.widget.config(bg="orange", fg="black")

def open_link(url):
    webbrowser.open_new(url)
 
def create_3dot_menu():
    # Create a menu
    menu = Menu(root, tearoff=0)
    menu.add_command(label="Registration", command=lambda: register("students"))
    menu.add_command(label="login", command=lambda: login("students"))
    menu.add_command(label="About", command=lambda: about_us_page("About"))
    menu.add_separator()
    menu.add_command(label="Exit", command=lambda: Cancel(root.quit()))

    # Create the 3-dot button
    def show_menu(event):
        """Show the menu on right-click or button click."""
        menu.post(event.x_root, event.y_root)

    # Add the button for the 3-dot menu
    button = Button(root, text="☰", font=("Arial", 16), bg="cyan", fg="black", bd=0)
    button.place(x=50, y=10)  # Position the 3-dot button
    button.bind("<Button-1>", show_menu)  # Bind left-click to show menu

def add_header():
    frame = Frame(root, bg="#290916", relief="groove",bd=3)
    frame.place(x=0, y=0, width=1600, height=60) 

def header():
    canvas.create_rectangle(0, 0, 1600, 60, fill="#290916")
    call_label = Label(root, text="Call Us: 415-555-1234", font=("Arial", 12), bg="#290916", fg="white", cursor="hand2")
    call_label.place(x=100, y=20)
    call_label.bind("<Button-1>", lambda e: open_link("tel:4155551234"))

    mail_label = Label(root, text="Mail Us: info@globaltechnology.com", font=("Arial", 12), bg="#290916", fg="white", cursor="hand2")
    mail_label.place(x=300, y=20)
    mail_label.bind("<Button-1>", lambda e: open_link("mailto:info@globaltechnology.com"))

    location_label = Label(root, text="Location: ODISHA, INDIA", font=("Arial", 12), bg="#290916", fg="white", cursor="hand2")
    location_label.place(x=600, y=20)
    location_label.bind("<Button-1>", lambda e: open_link("https://maps.google.com?q=ODISHA,+INDIA"))
    
    b1 = Button(root, text="HOME", font=("Arial", 12, "bold"), bg="chocolate3", fg="black", bd=2,width=12,height=1, command=home_page)
    b1.place(x=980, y=71)
    b1.bind("<Enter>", on_enter)
    b1.bind("<Leave>", on_leave)
    b2 = Button(root, text="CONTACT", font=("Arial", 12, "bold"), bg="chocolate3", fg="black", bd=2,width=12,height=1, command=contact_us_page)
    b2.place(x=1120, y=71)
    b2.bind("<Enter>", on_enter)
    b2.bind("<Leave>", on_leave)
    b3 = Button(root, text="EVENTS", font=("Arial", 12, "bold"), bg="chocolate3", fg="black", bd=2,width=12,height=1, command=about_us_page)
    b3.place(x=1260, y=71)
    b3.bind("<Enter>", on_enter)
    b3.bind("<Leave>", on_leave)
    b4 = Button(root, text="COURSES", font=("Arial", 12, "bold"), bg="chocolate3", fg="black", bd=2,width=12,height=1, command=courses_page)
    b4.place(x=1400, y=71)
    b4.bind("<Enter>", on_enter)
    b4.bind("<Leave>", on_leave)

def home_page():
    clear_frame()
    canvas.delete("all") 
    root.title("GLOBAL TECHNOLOGY")
    canvas.create_image(0, 0, image=home_bg_image, anchor="nw")
    header()
    lower_frame()
    create_3dot_menu()
        
    canvas.create_text(760, 300, text=" WELCOME  TO  OUR \n GLOBAL  TECHNOLOGY", font=("Rockwell", 40, "bold"), fill="white")
    canvas.create_text(720, 380, text="Raising concerns is the first step towards resolution and progress.", font=("Arial", 14), fill="white")

    # Button style configuration
    button_style = {"font": ("Arial", 20, "bold"), "width": 16, "height":2, "relief": "raised"}
    
    # Admin Button - Burgundy
    admin_btn = Button(root, text=" 👤\nADMIN", bg="#CD5700", fg="white", **button_style, bd=6, command=lambda: login('admin'))
    admin_btn.place(x=30, y=100)
    admin_btn.bind("<Enter>", on_enter)
    admin_btn.bind("<Leave>", on_leave)

    # Student Button - Royal Blue
    student_btn = Button(root, text="🎓\nSTUDENT", bg="#CD5700", fg="white", **button_style, bd=6, command=lambda: login('students'))
    student_btn.place(x=30, y=250)
    student_btn.bind("<Enter>", on_enter)
    student_btn.bind("<Leave>", on_leave)

    # Faculty Button - Forest Green
    faculty_btn = Button(root, text="🧑‍🏫\nFACULTY", bg="#CD5700", fg="white", **button_style, bd=6, command=lambda: login('faculty'))
    faculty_btn.place(x=30, y=400)
    faculty_btn.bind("<Enter>", on_enter)
    faculty_btn.bind("<Leave>", on_leave)

    # Principal Button - Goldenrod
    principal_btn = Button(root, text="🏢\nPRINCIPAL", bg="#CD5700", fg="white", **button_style, bd=6, command=lambda: login('principal'))
    principal_btn.place(x=30, y=550)
    principal_btn.bind("<Enter>", on_enter)
    principal_btn.bind("<Leave>", on_leave)

    # Cancel Button - Crimson
    Button(root, text="Cancel", bg="maroon", fg="white", font=("Arial", 11, "bold"), width=8, bd=5,command=Cancel).place(x=790, y=780)

def contact_us_page():
    clear_frame() 
    root.title(" CONTACT US ")
    canvas.delete("all") 
    canvas.create_image(0, 0, image=registor_bg_image, anchor="nw")
    header()
    create_canvas_text(canvas, 800, 100, "CONTACT US", ("Rockwell", 30, "bold"), "white")
    create_canvas_text(canvas, 800, 150, "For inquiries, call us at 415-555-1234 or email us at info@globaltechnology.com.", ("Arial", 16), "white")

def about_us_page():
    clear_frame()
    root.title(" EVENTS ")
    canvas.delete("all") 
    canvas.create_image(0, 0, image=registor_bg_image, anchor="nw")
    header()
    lower_frame()
    
    create_canvas_text(canvas, 800, 100, "UPCOMING EVENTS", ("Rockwell", 30, "bold"), "white")
    create_canvas_text(canvas, 800, 150, "Join us for exciting events and workshops at Global Technology.", ("Arial", 16), "white")

def courses_page():
    clear_frame()
    root.title(" COURSES ")
    canvas.delete("all") 
    canvas.create_image(0, 0, image=registor_bg_image, anchor="nw")
    header()
    lower_frame()

    create_canvas_text(canvas, 800, 100, "AVAILABLE COURSES", ("Rockwell", 30, "bold"), "white")
    create_canvas_text(canvas, 800, 150, "Explore our range of courses and find the right one for you.", ("Arial", 16), "white")

def login(user_type=None,event=None):
    clear_frame()
    side_frame()
    root.title(" LOGIN PAGE ")
    canvas.delete("all") 
    canvas.create_image(0, 0, image=login_bg_image, anchor="nw")
    header()
    lower_frame()
    create_3dot_menu()
    
    # Button style configuration
    button_style = {"font": ("Arial", 20, "bold"), "width": 16, "height":2, "relief": "raised"}
    
    # Admin Button - Burgundy
    admin_btn = Button(root, text=" 👤\nADMIN", bg="#C21E56", fg="white", **button_style, bd=6, command=lambda: login('admin'))
    admin_btn.place(x=30, y=100)
    admin_btn.bind("<Enter>", on_enter)
    admin_btn.bind("<Leave>", on_leave)

    # Student Button - Royal Blue
    student_btn = Button(root, text="🎓\nSTUDENT", bg="#C21E56", fg="white", **button_style, bd=6, command=lambda: login('students'))
    student_btn.place(x=30, y=250)
    student_btn.bind("<Enter>", on_enter)
    student_btn.bind("<Leave>", on_leave)

    # Faculty Button - Forest Green
    faculty_btn = Button(root, text="🧑‍🏫\nFACULTY", bg="#C21E56", fg="white", **button_style, bd=6, command=lambda: login('faculty'))
    faculty_btn.place(x=30, y=400)
    faculty_btn.bind("<Enter>", on_enter)
    faculty_btn.bind("<Leave>", on_leave)

    # Principal Button - Goldenrod
    principal_btn = Button(root, text="🏢\nPRINCIPAL", bg="#C21E56", fg="white", **button_style, bd=6, command=lambda: login('principal'))
    principal_btn.place(x=30, y=550)
    principal_btn.bind("<Enter>", on_enter)
    principal_btn.bind("<Leave>", on_leave)

    # Cancel Button - Crimson
    Button(root, text="Cancel", bg="maroon", fg="white", font=("Arial", 11, "bold"),  width=8, bd=8, command=Cancel).place(x=890, y=795)

    user_id_entry = StringVar()
    password_entry = StringVar()

    title = str(user_type).capitalize() if user_type else "Login"
    create_canvas_text(canvas,945,230, f"{title.upper()}  LOGIN", font=("Rockwell",35, "bold  underline"), fill="cyan")
    
    def toggle_password():
        if password_input.cget('show') == '*':
            password_input.config(show='')
            see_password_button.config(text="🔓")
        else:
            password_input.config(show='*')
            see_password_button.config(text="🔒")


    create_canvas_text(canvas, 770, 380, "🔑", font=("Arial", 30, "bold"), fill="#F1C6B1", anchor="w")
    user_id_input = Entry(root,textvariable=user_id_entry, font=("Arial", 18), bg="light gray",width=22)
    user_id_input.place(x=820, y=370)
    user_id_label = Label(root, text="User ID", font=("Arial", 10), bg="light gray")
    user_id_label.place(x=1020, y=375)
    user_id_input.focus_set()
    user_id_input.bind("<Return>", lambda event: password_input.focus())

    create_canvas_text(canvas,770, 445, "🔒", font=("Arial", 30, "bold"), fill="#F1C6B1", anchor="w")
    password_input = Entry(root,textvariable=password_entry, font=("Arial", 18), bg="light gray", show="*",width=22)
    password_input.place(x=820, y=435) 
    user_id_label = Label(root, text="Password", font=("Arial", 10), bg="light gray")
    user_id_label.place(x=1010, y=440)  
    password_input.bind("<Return>", lambda event: b1.focus())

    see_password_button = Button(root, text="🔒", font=("Arial", 11), bg="light gray",bd=0, command=toggle_password)
    see_password_button.place(x=1071, y=436)

    def handle_login():
        username = user_id_entry.get().strip()
        password = password_entry.get().strip()

        if not username and not password:
            messagebox.showinfo("Warning", "Both username and password are required.")
            user_id_input.focus_set()
            return
        if not username:
            messagebox.showinfo("Error","username required.")
            user_id_input.focus_set()
            return
        if not password:
            messagebox.showinfo("Error","password required.")
            password_input.focus_set()
            return

        user_table_map = {
            "admin": "admin",
            "faculty": "faculty",
            "students": "students",
            "principal": "principal",
        }
        table = user_table_map.get(user_type)

        if not table:
            messagebox.showerror("Error", "Invalid user type.")
            return

        conn = mysql.connector.connect(
            user='root',
            password='#Deepti2003',
            host='127.0.0.1',
            database='priti'
        )
        cursor = conn.cursor()
        cursor.execute(f"SELECT USER_ID FROM {table} WHERE USER_ID = %s", (username,))
        user_exists = cursor.fetchone()

        if not user_exists:
            messagebox.showinfo("Error", f"The user ID '{username}' does not exist in the {user_type} records.")
            if conn.is_connected():
               conn.close()
            return

        cursor.execute("SELECT attempts, blocked_until FROM login_attempts WHERE user_id = %s", (username,))
        result = cursor.fetchone()
        if result:
            attempts, blocked_until = result
            if blocked_until and datetime.datetime.now() < blocked_until:
                remaining_time = blocked_until - datetime.datetime.now()
                formatted_time = str(remaining_time).split(".")[0]
                messagebox.showinfo("Blocked", f"User is blocked. Try again after {formatted_time}.")
                return
        else:
            cursor.execute("INSERT INTO login_attempts (user_id) VALUES (%s)", (username,))
            conn.commit()
            attempts = 0

        query = f"SELECT USER_ID FROM {table} WHERE USER_ID=%s AND PASSWORD=%s"
        cursor.execute(query, (username, password))
        user_result = cursor.fetchone()

        if user_result:
            login_user_id = user_result[0]

            cursor.execute("UPDATE login_attempts SET attempts = 0, blocked_until = NULL WHERE user_id = %s", (username,))
            conn.commit()

            if table == "admin":
                admin_dashboard(login_user_id)
            elif table == "faculty":
                faculty_dashboard(login_user_id)
            elif table == "students":
                student_dashboard(login_user_id)
            elif table == "principal":
                principal_dashboard(login_user_id)
        else:
            attempts += 1
            if attempts >= 3:
                blocked_until = datetime.datetime.now() + datetime.timedelta(hours=24)
                cursor.execute("UPDATE login_attempts SET attempts = %s, blocked_until = %s WHERE user_id = %s", (attempts, blocked_until, username))
                messagebox.showinfo("Blocked", "Too many failed attempts. User is blocked for 24 hours.")
            else:
                cursor.execute("UPDATE login_attempts SET attempts = %s WHERE user_id = %s", (attempts, username))
                messagebox.showinfo("Login Failed", f"Invalid username or password. {3 - attempts} attempts remaining.")
            conn.commit()

        if conn.is_connected():
            conn.close()

    b1 = Button(root, text="SUBMIT", bg="#2B6CB0", fg="#E2E8F0", font=("Arial", 11, "bold"), width=8, bd=5, command=handle_login)
    b1.place(x=900, y=520)
    b1.bind("<Return>", lambda event: handle_login())
    rg = canvas.create_text(1040, 620, text="Register Here!  ->", font=("Arial",16, "bold"), fill="white", anchor="nw")
    canvas.tag_bind(rg, "<Button-1>", lambda event: register(user_type))
    fb = canvas.create_text(680, 620, text="Forgot password?", font=("Arial", 16, "bold"), fill="white", anchor="nw")
    canvas.tag_bind(fb, "<Button-1>", lambda event: forgot_password(user_type))
    Button(root, text="◄-- BACK", bg="#2B6CB0", fg="#E2E8F0", font=("Arial", 11, "bold"), width=8, bd=5, command=home_page).place(x=100, y=785)

def fetch_user_name(user_type, login_user_id):
    """Fetch the name of the logged-in user from the database."""
    try:
        # Validate the table name based on user_type
        user_table_map = {
            "admin": "admin",
            "faculty": "faculty",
            "students": "students",
            "principal": "principal",
        }
        table = user_table_map.get(user_type)
        if not table:
            raise ValueError(f"Invalid user type: {user_type}")

        # Establish the database connection
        conn = mysql.connector.connect(user="root", password="#Deepti2003", host="127.0.0.1", database="priti")
        cursor = conn.cursor()

        # Query the name of the user
        cursor.execute(f"SELECT FULL_NAME FROM {table} WHERE USER_ID = %s", (login_user_id,))
        result = cursor.fetchone()

        # Close the connection
        conn.close()

        # Return the name if found, otherwise a default value
        return result[0] if result else "Unknown User"
    except Exception as e:
        print(f"Error fetching user name: {e}")
        return "Unknown User"

def admin_dashboard(login_user_id=None):
    root.title("ADMIN DASHBOARD")
    clear_frame()
    canvas.delete("all")
    canvas.create_image(350, 50, image=admin_bg_image, anchor="nw") 
    create_canvas_text(canvas, 1010, 600, "Welcome to Admin Dashboard", font=("Rockwell",40, "bold "), fill="cyan")
    create_sidebar("admin", login_user_id)
    header()
    lower_frame()
    create_3dot_menu()

    Button(root, text="◄-- BACK", bg="#2B6CB0", fg="#E2E8F0", font=("Arial", 11, "bold"), width=8, bd=5, command=lambda: login(user_type="admin")).place(x=20, y=795)

def student_dashboard(login_user_id=None):
    root.title(" SUTDENT DASHBOARD ")
    clear_frame()
    canvas.delete("all")  
    canvas.create_image(350, 50, image=student_bg_image, anchor="nw")  
    create_canvas_text(canvas,900,200,"Welcome to Students Dashboard", font=("Rockwell",35, "bold italic underline"), fill="cyan")
    create_sidebar("students", login_user_id)
    header()
    lower_frame()
    create_3dot_menu()

    Button(root, text="◄-- BACK", bg="#2B6CB0", fg="#E2E8F0", font=("Arial", 11, "bold"), width=8, bd=5, command=lambda: login(user_type="students")).place(x=20, y=795)

def faculty_dashboard(login_user_id=None):
    root.title(" FACULTY DASHBOARD ")
    clear_frame()
    canvas.delete("all")  
    canvas.create_image(350,50, image=faculty_bg_image, anchor="nw")  
    create_canvas_text(canvas,890,200, "Welcome to Faculty Dashboard", font=("Rockwell",35, "bold italic underline"), fill="cyan") 
    create_sidebar("faculty", login_user_id)
    header()
    lower_frame()
    create_3dot_menu()

    Button(root, text="◄-- BACK", bg="#2B6CB0", fg="#E2E8F0", font=("Arial", 11, "bold"),  width=8, bd=5, command=lambda: login(user_type="faculty")).place(x=20, y=795)  

def principal_dashboard(login_user_id=None):
    root.title(" PRINCIPAL DASHBOARD ")
    clear_frame()
    canvas.delete("all")  
    canvas.create_image(350, 50, image=principal_bg_image, anchor="nw") 
    create_canvas_text(canvas,890,200,"Welcome to Principal Dashboard", font=("Rockwell",35, "bold italic underline"), fill="cyan")
    create_sidebar("principal", login_user_id)
    header()
    lower_frame()
    create_3dot_menu()
 
    Button(root, text="◄-- BACK", bg="#2B6CB0", fg="#E2E8F0", font=("Arial", 11, "bold"),  width=8, bd=5, command=lambda: login(user_type="principal")).place(x=20, y=795)

def create_sidebar(user_type, login_user_id):
    """Creates a sidebar frame with user-specific options."""
    clear_frame()
    frame = Frame(root, bg="#290916", relief="solid",bd=0)
    frame.place(x=2, y=61, width=350, height=730) 
    # Fetch the user name
    user_name = fetch_user_name(user_type, login_user_id)
 
    if user_name is None:
        welcome_text = f"   (👤)\nWelcome {user_type.capitalize()}\nUser not found"
    else:
        welcome_text = f"  {user_type.capitalize()}\n   (👤)\n{user_name}"

    Label(frame, text=welcome_text, font=("Arial", 14, "bold"), bg="#290916", fg="white", wraplength=300).pack(pady=20)
    options = {
        "admin": [
            ("View self Profile", lambda: view_profile(user_type="admin", viewer_type="admin", login_user_id=login_user_id)),
            ("Update self Profile", lambda: update_information(user_type="admin", viewer_type="admin", login_user_id=login_user_id)),
            ("Delete self Profile", lambda: delete_information(user_type="admin", viewer_type="admin", login_user_id=login_user_id)),
            ("Change self Password", lambda: change_password(user_type="admin", viewer_type="admin", login_user_id=login_user_id)),
            ("View Faculty Info", lambda: view_profile(user_type="admin",target_user_type="faculty", viewer_type="admin", login_user_id=login_user_id)),
            ("Update faculty Info", lambda: update_information(user_type="admin",target_user_type="faculty", viewer_type="admin", login_user_id=login_user_id)),
            ("Delete Faculty Info", lambda: delete_information(user_type="admin",target_user_type="faculty", viewer_type="admin", login_user_id=login_user_id)),
            ("View Student Info", lambda: view_profile(user_type="admin",target_user_type="students", viewer_type="admin", login_user_id=login_user_id)),
            ("Update Student Info", lambda: update_information(user_type="admin",target_user_type="students", viewer_type="admin", login_user_id=login_user_id)),
            ("Delete Student Info", lambda: delete_information(user_type="admin",target_user_type="students", viewer_type="admin", login_user_id=login_user_id))

        ],
        "faculty": [
            ("View Profile", lambda: view_profile(user_type="faculty", viewer_type="faculty", login_user_id=login_user_id)),
            ("View Student Profile", lambda: view_profile(user_type="faculty",target_user_type="students", viewer_type="faculty", login_user_id=login_user_id)),
            ("Update Profile", lambda: update_information(user_type="faculty", viewer_type="faculty", login_user_id=login_user_id)),
            ("Change Password", lambda: change_password(user_type="faculty", viewer_type="faculty", login_user_id=login_user_id)),
            ("View Students Complaints", lambda: view_complaints_faculty_principal(user_type="faculty", login_user_id=login_user_id)),
            ("Update Complaints", lambda: handle_complaints(user_type="faculty", viewer_type="faculty"))
        ],
        "students": [
            ("View Profile", lambda: view_profile(user_type="students", viewer_type="students", login_user_id=login_user_id)),
            ("Update Profile", lambda: update_information(user_type="students", viewer_type="students", login_user_id=login_user_id)),
            ("Change Password", lambda: change_password(user_type="students", viewer_type="students", login_user_id=login_user_id)),
            ("Raise Complaint", lambda: raise_complaint(user_type="students",login_user_id=login_user_id)),
            ("View Complaints Status", lambda: view_complaints_feedback(user_type="students", viewer_type="students", login_user_id=login_user_id))
        ],
        "principal": [
            ("View Profile", lambda: view_profile(user_type="principal", viewer_type="principal", login_user_id=login_user_id)),
            ("Update Profile", lambda: update_information(user_type="principal", viewer_type="principal", login_user_id=login_user_id)),
            ("Change Password", lambda: change_password(user_type="principal", viewer_type="principal", login_user_id=login_user_id)),
            ("View Admin Info", lambda: view_profile(user_type="principal",target_user_type="admin", viewer_type="principal", login_user_id=login_user_id)),
            ("View Faculty Info", lambda: view_profile(user_type="principal",target_user_type="faculty", viewer_type="principal", login_user_id=login_user_id)),
            ("View Student Info", lambda: view_profile(user_type="principal",target_user_type="students", viewer_type="principal", login_user_id=login_user_id)),
            ("View Complaints", lambda: view_complaints_faculty_principal(user_type="principal", login_user_id=login_user_id))
        ]
    }

    for text, command in options.get(user_type, []):
        
        Button(frame, text=text, bg="chocolate3", fg="white", font=("Arial", 11, "bold"), command=command, width=25, bd=4).pack(pady=10)

def register(user_type=None):
    root.title(" REGISTRATION PANNEL ")
    clear_frame()
    canvas.delete("all") 
    canvas.create_image(0,0,image=registor_bg_image,anchor="nw")
    header()
    lower_frame()

    regd_no_entry = StringVar()
    name_entry = StringVar()
    user_id_entry = StringVar()
    password_entry = StringVar()
    mobile_entry = StringVar()
    email_entry = StringVar()
    gender_val = StringVar()
    gender_val = StringVar() 
    security_ans_entry = StringVar()
    selected_question = StringVar()

    form_frame = Frame(root, bg="steelblue", bd=2, relief="solid")
    form_frame.place(x=300, y=110, width=790, height=650)

    title = str(user_type).capitalize() if user_type else "Registration"
    title_label = Label(form_frame, text=f"{title.upper()} REGISTRATION", font=("Rockwell", 30, "bold italic underline"), fg="white",bg="steelblue")
    title_label.place(x=100, y=20)

    Label(form_frame, text="Emp_id/Stu_id:", font=("Arial", 16,"bold"), bg="steelblue", anchor="w").place(x=50, y=100)
    regd_no_input = Entry(form_frame, textvariable=regd_no_entry, font=("Arial", 14), bg="white",width=27)
    regd_no_input.place(x=50, y=140)

    Label(form_frame, text="Full Name:", font=("Arial",  16,"bold"), bg="steelblue", anchor="w",width=10).place(x=410, y=100)
    name_input = Entry(form_frame, textvariable=name_entry, font=("Arial", 14), bg="white",width=27)
    name_input.place(x=410, y=140)
    name_input.focus_set()
    name_input.bind("<Return>", lambda event: user_id_input.focus())

    Label(form_frame, text="User ID:", font=("Arial", 16,"bold"), bg="steelblue", anchor="w").place(x=50, y=190)
    user_id_input = Entry(form_frame, textvariable=user_id_entry, font=("Arial", 14), bg="white",width=27)
    user_id_input.place(x=50, y=230)
    user_id_input.bind("<Return>", lambda event: password_input.focus())

    Label(form_frame, text="Password:", font=("Arial",  16,"bold"), bg="steelblue", anchor="w").place(x=410, y=190)
    password_input = Entry(form_frame, textvariable=password_entry, font=("Arial", 14), bg="white", show="*",width=27)
    password_input.place(x=410, y=230)
    password_input.bind("<Return>", lambda event: mobile_input.focus()) 

    Label(form_frame, text="Mobile No.:", font=("Arial",  16,"bold"), bg="steelblue", anchor="w").place(x=50, y=280)
    mobile_input = Entry(form_frame, textvariable=mobile_entry, font=("Arial", 14), bg="white",width=27)
    mobile_input.place(x=50, y=320)
    mobile_input.bind("<Return>", lambda event: email_input.focus())

    Label(form_frame, text="Mail ID:", font=("Arial",  16,"bold"), bg="steelblue", anchor="w").place(x=410, y=280)
    email_input = Entry(form_frame, textvariable=email_entry, font=("Arial", 14), bg="white",width=27)
    email_input.place(x=410, y=320)
    email_input.bind("<Return>", lambda event: combobox.focus())

    Label(form_frame, text="Gender:", font=("Arial", 16,"bold"), bg="steelblue", anchor="w").place(x=50, y=390)
    Radiobutton(form_frame, text="Male", variable=gender_val, value="Male", bg="steelblue",fg="black", font=("Arial", 14)).place(x=280, y=390)
    Radiobutton(form_frame, text="Female", variable=gender_val, value="Female", bg="steelblue",fg="black", font=("Arial", 14)).place(x=440, y=390)
    Radiobutton(form_frame, text="Other", variable=gender_val, value="Other", bg="steelblue",fg="black", font=("Arial", 14)).place(x=600, y=390)

    Label(form_frame, text="Security Question:", font=("Arial",  16,"bold"), bg="steelblue", anchor="w").place(x=50, y=460)
    security_questions = [
        "What is your mother's maiden name?",
        "What was the name of your first pet?",
        "What was your first car?",
        "What elementary school did you attend?",
        "In what city were you born?"
    ]
    combobox = ttk.Combobox(form_frame, textvariable=selected_question, values=security_questions, state="readonly", width=40)
    combobox.place(x=50, y=500)
    combobox.bind("<Return>", lambda event: security_ans_input.focus())

    Label(form_frame, text="Security Answer:", font=("Arial", 16,"bold"), bg="steelblue", anchor="w").place(x=410, y=460)
    security_ans_input = Entry(form_frame, textvariable=security_ans_entry, font=("Arial", 14), bg="white",width=27)
    security_ans_input.place(x=410, y=500)
    security_ans_input.bind("<Return>", lambda event: b2.focus())    

    def generate_emp_id():
        conn = mysql.connector.connect(
            user='root',
            password='#Deepti2003',
            host='127.0.0.1',
            database='priti'
        )
        cursor = conn.cursor()
        prefix = {
            "admin": "ADM",
            "faculty": "FAC",
            "principal": "PRI",
            "students": "STU"
        }.get(user_type, "USR")
        cursor.execute(f"SELECT COUNT(*) FROM {user_type}")
        count = cursor.fetchone()[0] + 1
        random_number = random.randint(1000,9999)

        # Close the database connection
        conn.close()

        # Return the generated employee ID
        return f"{prefix}{random_number}"

    # Set the generated employee ID to the entry widget
    regd_no_entry.set(generate_emp_id())

    def handle_register():
        reg_no_val = regd_no_entry.get()
        name_val = name_entry.get()
        user_id_val = user_id_entry.get()
        password_val = password_entry.get()
        mobile_val = mobile_entry.get()
        email_val = email_entry.get()
        gender = gender_val.get()
        security_ans_val = security_ans_entry.get()
        selected_question_val = selected_question.get()

        if not name_val and not user_id_val and not password_val and not mobile_val and not email_val and not gender and not security_ans_val and not selected_question_val:
            messagebox.showinfo("Error","Please fill up all the details.")
            name_input.focus_set()
            return   
        if not reg_no_val:
            messagebox.showinfo("warning","please enter EMP_ID/REGD.NO")
            regd_no_input.focus_set()
            return
        if not name_val:
            messagebox.showinfo("warning","please enter your Full name.")
            name_input.focus_set()
            return
        if not user_id_val:
            messagebox.showinfo("warning","please enter Your User Id.")
            user_id_input.focus_set()
            return
        if not password_val: 
            messagebox.showinfo("warning","please enter Your Password.")
            password_input.focus_set()
            return
        if not len(password_val) >= 8:
            messagebox.showinfo("Warning","Password must be 8 characters or longer.")
            password_input.focus_set()
            return
        if not mobile_val:
            messagebox.showinfo("warning","please enter Your Mobile NO.")
            mobile_input.focus_set()
            return
        if not mobile_val.isdigit() or len(mobile_val) != 10:
            messagebox.showinfo("Warning", "Mobile number must be exactly 10 digits.")
            mobile_input.focus_set()
            return
        if not email_val:
            messagebox.showinfo("warning","please enter Your Email Id.")
            email_input.focus_set()
            return
        if "@" not in email_val or "." not in email_val:
            messagebox.showinfo("Warning", "Please enter a valid email address.")
            email_input.focus_set()
            return
        if not gender_val:
            messagebox.showinfo("warning","please Select Gender.")
            return
        if not security_ans_val:
            messagebox.showinfo("warning","please enter Your Security Answer.")
            security_ans_input.focus_set()
            return
        if not selected_question_val:
            messagebox.showinfo("warning","please Select A Security Question.")
            combobox.focus_set()
            return
        
        conn = mysql.connector.connect(
            user='root',
            password='#Deepti2003',
            host='127.0.0.1',
            database='priti'
        )
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {user_type} WHERE USER_ID = %s AND PASSWORD = %s AND EMP_ID = %s AND EMAIL_ID = %s AND PHONE_NO = %s", (user_id_val, password_val, reg_no_val, email_val, mobile_val))
        duplicate = cursor.fetchone()

        if duplicate:
            messagebox.showinfo("Error", "This user already exists! Redirecting to the login page.")
            conn.close()
            go_back()  
            return

        table = user_type
        sql = f"""INSERT INTO {table} (EMP_ID, FULL_NAME, USER_ID, PASSWORD, PHONE_NO, EMAIL_ID, GENDER, security_question, SECURITY_ANSWER)
                  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (reg_no_val, name_val, user_id_val, password_val, mobile_val, email_val, gender, selected_question_val, security_ans_val))
        conn.commit()

        messagebox.showinfo("Registration Successful", f"{str(user_type).capitalize()} registered successfully!")
        go_back()
        conn.close()

    def go_back():
        if user_type == "faculty":
            login(user_type="faculty")
        elif user_type == "students":
            login(user_type="students")
        elif user_type == "principal":
            login(user_type="principal")
        elif user_type == "admin":
            login(user_type="admin")
        else:
            home_page()

    def cancel():
        if user_type == "faculty":
            register(user_type="faculty")
        elif user_type == "students":
            register(user_type="students")
        elif user_type == "principal":
            register(user_type="principal")
        elif user_type == "admin":
            register(user_type="admin")
        else:
            home_page()

    b2 = Button(root, text="SUBMIT", bg="red", fg="white", font=("Arial", 11, "bold"), width=8, bd=8, command=handle_register)
    b2.place(x=730, y=700)
    b2.bind("<Return>", lambda event: handle_register())
    Button(root, text="◄-- BACK", bg="#2B6CB0", fg="#E2E8F0", font=("Arial", 11, "bold"),  width=8, bd=5, command=lambda: login(user_type="principal")).place(x=20, y=795)
    Button(root, text="CANCEL", bg="slate gray", fg="greenyellow", font=("Arial", 11, "bold"), width=8, bd=8, command=cancel).place(x=1400, y=700)

def view_profile(user_type=None, viewer_type=None, login_user_id=None, target_user_type=None):
    root.title(" VIEW PROFILE PANNEL ")
    clear_frame()
    canvas.delete("all")
    canvas.create_image(350, 50, image=function_bg_image, anchor="nw")
    create_sidebar(user_type=user_type, login_user_id=login_user_id)
    add_header()
    lower_frame()

    valid_user_types = ["admin", "faculty", "principal", "students"]
    if viewer_type not in valid_user_types:
        messagebox.showerror("Error", "Invalid viewer type!")
        return

    if target_user_type and target_user_type in valid_user_types:
        profile_user_type = target_user_type
    else:
        profile_user_type = user_type

    title = profile_user_type.capitalize()
    Label(root, text=f"{title.upper()} PROFILE", fg="white",bg="#290916", font=("Rockwell", 28, "bold italic underline")).place(x=750, y=6)

    conn = mysql.connector.connect(
        user='root',
        password='#Deepti2003',
        host='127.0.0.1',
        database='priti'
    )
    if not conn.is_connected():
        messagebox.showerror("Error", "Failed to connect to the database.")
        return
    cursor = conn.cursor()

    if profile_user_type == user_type:
        query = f"SELECT USER_ID, FULL_NAME, PHONE_NO, EMAIL_ID, GENDER FROM {user_type} WHERE USER_ID = %s"
        cursor.execute(query, (login_user_id,))
    # elif viewer_type == "admin":
    #     query = f"SELECT USER_ID, FULL_NAME, PHONE_NO, EMAIL_ID, GENDER FROM {valid_user_types[1]} UNION SELECT USER_ID, FULL_NAME, PHONE_NO, EMAIL_ID, GENDER FROM {valid_user_types[3]} WHERE USER_ID != %s"
    #     cursor.execute(query, (login_user_id,))
    elif viewer_type == "admin" and profile_user_type in ["faculty", "students"]:
        query = f"SELECT USER_ID, FULL_NAME, PHONE_NO, EMAIL_ID, GENDER FROM {profile_user_type}"
        cursor.execute(query)
    elif viewer_type == "principal" and profile_user_type in ["faculty", "students", "admin"]:
        query = f"SELECT USER_ID, FULL_NAME, PHONE_NO, EMAIL_ID, GENDER FROM {profile_user_type}"
        cursor.execute(query)
    elif viewer_type == "faculty" and profile_user_type in ["students"]:
        query = f"SELECT USER_ID, FULL_NAME, PHONE_NO, EMAIL_ID, GENDER FROM {profile_user_type}"
        cursor.execute(query)
    else:
        messagebox.showerror("Permission Denied", "You do not have permission to view this profile.")
        cursor.close()
        conn.close()
        return

    users = cursor.fetchall()

    if not users:
        messagebox.showinfo("No Data", f"No records found for {title}.")
        cursor.close()
        conn.close()
        return
    # Create a background frame
    frame = Frame(root, bg="#F5E1A4", bd=2, relief="groove")
    frame.place(x=600, y=200, width=800, height=500)  # Adjusted to fit content

    # Header labels
    header_y_position = 20
    Label(frame, text="User ID", font=("Arial", 12, "bold"), width=10, anchor="w", bg="#F5E1A4", fg="black").place(x=10, y=header_y_position)
    Label(frame, text="Full Name", font=("Arial", 12, "bold"), width=15, anchor="w", bg="#F5E1A4", fg="black").place(x=120, y=header_y_position)
    Label(frame, text="Mobile No", font=("Arial", 12, "bold"), width=15, anchor="w", bg="#F5E1A4", fg="black").place(x=290, y=header_y_position)
    Label(frame, text="Mail ID", font=("Arial", 12, "bold"), width=20, anchor="w", bg="#F5E1A4", fg="black").place(x=460, y=header_y_position)
    Label(frame, text="Gender", font=("Arial", 12, "bold"), width=10, anchor="w", bg="#F5E1A4", fg="black").place(x=660, y=header_y_position)

    # Content labels
    y_position = header_y_position + 30
    for user in users:
        Label(frame, text=user[0], font=("Arial", 10), width=10, anchor="w", bg="#F5E1A4", fg="black").place(x=10, y=y_position)
        Label(frame, text=user[1], font=("Arial", 10), width=15, anchor="w", bg="#F5E1A4", fg="black").place(x=120, y=y_position)
        Label(frame, text=user[2], font=("Arial", 10), width=15, anchor="w", bg="#F5E1A4", fg="black").place(x=290, y=y_position)
        Label(frame, text=user[3], font=("Arial", 10), width=20, anchor="w", bg="#F5E1A4", fg="black").place(x=460, y=y_position)
        Label(frame, text=user[4], font=("Arial", 10), width=10, anchor="w", bg="#F5E1A4", fg="black").place(x=660, y=y_position)
        y_position += 30

    def go_back():
        if viewer_type == "admin":
            create_sidebar(user_type="admin", login_user_id=login_user_id)
            admin_dashboard(login_user_id)
        elif viewer_type == "principal":
            create_sidebar(user_type="principal", login_user_id=login_user_id)
            principal_dashboard(login_user_id)
        elif viewer_type == "faculty":
            create_sidebar(user_type="faculty", login_user_id=login_user_id)
            faculty_dashboard(login_user_id)
        elif viewer_type == "students":
            create_sidebar(user_type="students", login_user_id=login_user_id)
            student_dashboard(login_user_id)
        else:
            home_page()

    Button(root, text="◄-- BACK", command=go_back, width=15, bd=5, bg="slate gray", fg="white").place(x=20, y=795)

    cursor.close()
    conn.close()

def update_information(user_type=None, viewer_type=None, login_user_id=None, target_user_type=None):
    root.title(" UPDATE INFO PANNEL ")
    clear_frame()
    canvas.delete("all") 
    canvas.create_image(350, 50, image=function_bg_image, anchor="nw")
    create_sidebar(user_type=user_type, login_user_id=login_user_id)
    add_header()
    lower_frame()

    valid_user_types = ["admin", "faculty", "principal", "students"]
    if viewer_type not in valid_user_types:
        messagebox.showerror("Error", "Invalid viewer type!")
        return

    if viewer_type == "admin":
        if not target_user_type:
            profile_user_type = "admin"
        elif target_user_type in ["faculty", "students"]:
            profile_user_type = target_user_type
        else:
            messagebox.showerror("Error", "Invalid target user type!")
            return
    else:
        profile_user_type = user_type

    title = "Admin" if profile_user_type == "admin" else f"{profile_user_type.capitalize()}"
    create_canvas_text(canvas, 1000, 150, f"{title.upper()} UPDATE", font=("Rockwell", 28, "bold italic underline"), fill="cyan")

    create_canvas_text(canvas, 700, 250, "ENTER USER ID:", font=("Arial", 18, "bold"), fill="#F1C6B1", anchor="w")
    user_id_combobox = None
    if profile_user_type in ["faculty", "students"] and viewer_type == "admin":
        user_id_combobox = ttk.Combobox(root, state="readonly", width=38)
        user_id_combobox.place(x=900, y=235)

        def populate_user_id_combobox():
            nonlocal user_id_combobox
            conn = mysql.connector.connect(
                user='root',
                password='#Deepti2003',
                host='127.0.0.1',
                database='priti'
            )
            cursor = conn.cursor()
            query = f"SELECT USER_ID FROM {profile_user_type}"
            cursor.execute(query)
            result = cursor.fetchall()
            user_ids = [str(row[0]) for row in result]
            user_id_combobox["values"] = user_ids
            conn.close()

        populate_user_id_combobox()
        user_id_entry = user_id_combobox
    else:
        user_id_entry = Entry(root, font=("Arial", 14), bg="white", width=40)
        user_id_entry.place(x=900, y=235)
        if isinstance(user_id_entry, Entry):
            user_id_entry.delete(0, END)
            user_id_entry.insert(0, login_user_id)
    
    create_canvas_text(canvas, 700, 320, "EMPLOYEE ID:", font=("Arial", 18, "bold"), fill="#F1C6B1", anchor="w")
    emp_id_entry = Entry(root, font=("Arial", 14), bg="white", width=40, state="disabled")
    emp_id_entry.place(x=900, y=305)

    create_canvas_text(canvas, 700, 390, "FULL NAME:", font=("Arial", 18, "bold"), fill="#F1C6B1", anchor="w")
    name_entry = Entry(root, font=("Arial", 14), bg="white", width=40)
    name_entry.place(x=900, y=375)
    name_entry.focus_set()

    create_canvas_text(canvas, 700, 460, "PHONE NO:", font=("Arial", 18, "bold"), fill="#F1C6B1", anchor="w")
    phone_entry = Entry(root, font=("Arial", 14), bg="white", width=40)
    phone_entry.place(x=900, y=445)

    create_canvas_text(canvas, 700, 530, "EMAIL ID:", font=("Arial", 18, "bold"), fill="#F1C6B1", anchor="w")
    email_entry = Entry(root, font=("Arial", 14), bg="white", width=40)
    email_entry.place(x=900, y=515)

    create_canvas_text(canvas, 700, 600, "GENDER:", font=("Arial", 18, "bold"), fill="#F1C6B1", anchor="w")
    gender_entry = ttk.Combobox(root, state="readonly", values=["Male", "Female", "Other"], width=38)
    gender_entry.place(x=900, y=585)

    def populate_details():
        conn = mysql.connector.connect(
            user='root',
            password='#Deepti2003',
            host='127.0.0.1',
            database='priti'
        )
        cursor = conn.cursor()

        user_id = user_id_entry.get().strip() if isinstance(user_id_entry, Entry) else user_id_combobox.get()

        query = f"SELECT USER_ID, EMP_ID, FULL_NAME, PHONE_NO, EMAIL_ID, GENDER FROM {profile_user_type} WHERE USER_ID = %s"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        conn.close()

        if result:
            if isinstance(user_id_entry, Entry):
                user_id_entry.delete(0, END)
                user_id_entry.insert(0, result[0])
            elif isinstance(user_id_combobox, ttk.Combobox):
                user_id_combobox.set(result[0])

            emp_id_entry.config(state="normal")
            emp_id_entry.delete(0, END)
            emp_id_entry.insert(0, result[1])
            emp_id_entry.config(state="disabled")

            name_entry.delete(0, END)
            name_entry.insert(0, result[2])
            phone_entry.delete(0, END)
            phone_entry.insert(0, result[3])
            email_entry.delete(0, END)
            email_entry.insert(0, result[4])
            gender_entry.set(result[5])
        else:
            messagebox.showinfo("Error", "No data found for the entered User ID.")

    def handle_update():
        user_id = user_id_entry.get()
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        gender = gender_entry.get()

        if not user_id and not name and not phone and not email and not gender:
            messagebox.showinfo("Warning", "All fields are required.")
            return
        if not name:
            messagebox.showinfo("warning","please enter your Full name.")
            name_entry.focus_set()
            return
        if not phone.isdigit() or len(phone) != 10:
            messagebox.showinfo("Warning", "Phone number must be exactly 10 digits.")
            phone_entry.focus_set()
            return
        if not email: 
            messagebox.showinfo("warning","please enter Your mail id.")
            email_entry.focus_set()
            return
        if not gender:
            messagebox.showinfo("warning","please Select Gender.")
            gender_entry.focus_set()
            return

        conn = mysql.connector.connect(
            user='root',
            password='#Deepti2003',
            host='127.0.0.1',
            database='priti'
        )
        cursor = conn.cursor()

        query = f"""
            UPDATE {profile_user_type} 
            SET FULL_NAME=%s, PHONE_NO=%s, EMAIL_ID=%s, GENDER=%s 
            WHERE USER_ID=%s
        """
        cursor.execute(query, (name, phone, email, gender, user_id))
        conn.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Success", "Information updated successfully.")
        else:
            messagebox.showinfo("Error", "Failed to update. Please check the User ID.")
        conn.close()

        update_information(user_type, viewer_type, login_user_id, target_user_type)

    def go_back():
        if viewer_type == "faculty":
            create_sidebar(viewer_type, login_user_id)
            faculty_dashboard(login_user_id)
        elif viewer_type == "students":
            create_sidebar(viewer_type, login_user_id)
            student_dashboard(login_user_id)
        elif viewer_type == "principal":
            create_sidebar(viewer_type, login_user_id)
            principal_dashboard(login_user_id)
        elif viewer_type == "admin":
            create_sidebar(viewer_type, login_user_id)
            admin_dashboard(login_user_id)
        else:
            home_page()

    b3 = Button(root, text="LOAD DETAILS", bg="slate gray", fg="greenyellow", font=("Arial", 12, "bold"), width=15, bd=8, command=populate_details)
    b3.place(x=850, y=700)
    b3.focus_set()
    b3.bind("<Return>", lambda event: populate_details())
    Button(root, text="UPDATE", bg="slate gray", fg="greenyellow", font=("Arial", 12, "bold"), width=15, bd=8, command=handle_update).place(x=1250, y=750)
    Button(root, text="◄-- BACK", bg="slate gray", fg="greenyellow", font=("Arial", 12, "bold"), width=15, bd=8, command=go_back).place(x=20, y=795)

def change_password(user_type=None, viewer_type=None, login_user_id=None):
    root.title(" CHANGE PASSWORD ")
    clear_frame()
    canvas.delete("all") 
    canvas.create_image(350, 50, image=function_bg_image, anchor="nw")
    create_sidebar(user_type=user_type, login_user_id=login_user_id)
    add_header()
    lower_frame()
    session["login_user_id"] = login_user_id

    if user_type not in ["admin", "faculty", "principal", "students"]:
        messagebox.showerror("Error", "Invalid user type!")
        return
    create_canvas_text(canvas, 1000, 150, f"RESET PASSWORD ({str(user_type).upper()})", font=("Rockwell", 28, "bold italic underline"), fill="cyan")
    
    create_canvas_text(canvas, 700, 250, "CURRENT PASSWORD:", font=("Arial", 18, "bold"), fill="#F1C6B1", anchor="w")
    current_password_entry = Entry(root, font=("Arial", 14), bg="white", show="*")
    current_password_entry.place(x=1050, y=235)

    create_canvas_text(canvas, 700, 350, "NEW PASSWORD:", font=("Arial", 18, "bold"), fill="#F1C6B1", anchor="w")
    new_password_entry = Entry(root, font=("Arial", 14), bg="white", show="*")
    new_password_entry.place(x=1050, y=335)

    create_canvas_text(canvas, 650, 450, "CONFIRM NEW PASSWORD:", font=("Arial", 18, "bold"), fill="#F1C6B1", anchor="w")
    confirm_new_password_entry = Entry(root, font=("Arial", 14), bg="white", show="*")
    confirm_new_password_entry.place(x=1050, y=435)

    def handle_change_password():
        current_password = current_password_entry.get()
        new_password = new_password_entry.get()
        confirm_new_password = confirm_new_password_entry.get()

        if not current_password and not new_password and not confirm_new_password:
            messagebox.showinfo("Warning", "All fields are required.")
            current_password_entry.focus_set()
            return
        if not current_password:
            messagebox.showinfo("Warning", "current password is required.")
            current_password_entry.focus_set() 
            return
        if not new_password:
            messagebox.showinfo("Warning", "new password is required.")
            new_password_entry.focus_set()
            return
        if not confirm_new_password:
            messagebox.showinfo("Warning", "confirm password is required.")
            confirm_new_password_entry.focus_set()
            return
        if new_password != confirm_new_password:
            messagebox.showinfo("Warning", "New passwords do not match.")
            new_password_entry.focus_set()
            return

        conn = mysql.connector.connect(
            user='root',
            password='#Deepti2003',
            host='127.0.0.1',
            database='priti'
        )
        cursor = conn.cursor()

        query = f"SELECT * FROM {user_type} WHERE password = %s"
        cursor.execute(query, (current_password,))
        result = cursor.fetchone()

        if result:
            update_query = f"UPDATE {user_type} SET password = %s WHERE password = %s"
            cursor.execute(update_query, (new_password, current_password))
            conn.commit()
            messagebox.showinfo("Success", "Your password has been updated successfully.")
            clear_frame()
            if user_type == "admin":
                admin_dashboard()
            else:
                home_page()
        else:
            messagebox.showerror("Error", "Incorrect current password.")

        conn.close()

    def go_back():
        login_user_id = session.get("login_user_id")
        if viewer_type == "faculty":
            create_sidebar(viewer_type, login_user_id)
            faculty_dashboard(login_user_id)
        elif viewer_type == "students":
            create_sidebar(viewer_type, login_user_id)
            student_dashboard(login_user_id)
        elif user_type == "principal":
            create_sidebar(viewer_type, login_user_id)
            principal_dashboard(login_user_id)
        elif user_type == "admin":
            create_sidebar(viewer_type, login_user_id)
            admin_dashboard(login_user_id)
        else:
            create_sidebar(viewer_type, login_user_id)
            home_page()

    def cancel():
        login_user_id = session.get("login_user_id")
        if user_type == "faculty":
            change_password(user_type="faculty")
        elif user_type == "students":
            change_password(user_type="students")
        elif user_type == "principal":
            change_password(user_type="principal")
        elif user_type == "admin":
            change_password(user_type="admin")
        else:
            home_page()
        session["login_user_id"] = login_user_id    

    Button(root, text="UPDATE PASSWORD", bg="slate gray", fg="greenyellow", font=("Arial", 12, "bold"), width=18, bd=8, command=handle_change_password).place(x=850, y=550)
    Button(root, text="◄-- BACK", bg="slate gray", fg="greenyellow", font=("Arial", 12, "bold"), width=8, bd=8, command=go_back).place(x=450, y=700)
    Button(root, text="CANCEL", bg="slate gray", fg="greenyellow", font=("Arial", 12, "bold"), width=8, bd=8, command=cancel).place(x=1250, y=700)

def forgot_password(user_type=None):
    root.title(" FORGOT PASSWORD PANNEL ")
    clear_frame()
    canvas.delete("all") 
    canvas.create_image(0, 50, image=forgot_bg_image, anchor="nw")
    add_header()
    lower_frame()

    if user_type not in ["admin", "faculty", "principal", "students"]:
        messagebox.showerror("Error", "Invalid user type!")
        return

    create_canvas_text(canvas, 690, 200, f"FORGOT PASSWORD ({str(user_type).upper()})", font=("Rockwell", 28, "bold italic underline"), fill="cyan")

    create_canvas_text(canvas, 390, 300,"USER ID:", font=("Arial", 18, "bold"), fill="#F1C6B1", anchor="w")
    user_id_entry = Entry(root, font=("Arial", 14), bg="white")
    user_id_entry.place(x=680, y=290)

    create_canvas_text(canvas, 390, 370, "SECURITY QUESTION:", font=("Arial", 18, "bold"), fill="#F1C6B1", anchor="w")
    question_label = Entry(root, font=("Arial", 14), bg="white", state="disabled", width=40)
    question_label.place(x=680, y=360)

    create_canvas_text(canvas, 390, 440, "SECURITY ANSWER:", font=("Arial", 18, "bold"), fill="#F1C6B1", anchor="w")
    security_ans_entry = Entry(root, font=("Arial", 14), bg="white")
    security_ans_entry.place(x=680, y=430)

    create_canvas_text(canvas, 390, 510, "NEW PASSWORD:", font=("Arial", 18, "bold"), fill="#F1C6B1", anchor="w")
    new_password_entry = Entry(root, font=("Arial", 14), bg="white", show="*")
    new_password_entry.place(x=680, y=500)

    create_canvas_text(canvas, 390, 580, "RE-ENTER PASSWORD:", font=("Arial", 18, "bold"), fill="#F1C6B1", anchor="w")
    con_new_password_entry = Entry(root, font=("Arial", 14), bg="white", show="*")
    con_new_password_entry.place(x=680, y=570)

    def fetch_security_question(event=None):  
        user_id_val = user_id_entry.get().strip()

        if not user_id_val:
            return

        conn = mysql.connector.connect(
            user='root',
            password='#Deepti2003',
            host='127.0.0.1',
            database='priti'
        )
        cursor = conn.cursor()

        sql = f"SELECT security_question FROM {user_type} WHERE user_id=%s"
        cursor.execute(sql, (user_id_val,))
        result = cursor.fetchone()

        if result:
            question_label.config(state="normal")
            question_label.delete(0, "end")
            question_label.insert(0, result[0])
            question_label.config(state="disabled")
        else:
            messagebox.showerror("Error", "User ID not found.")

        conn.close()

    def handle_submit():
        user_id_val = user_id_entry.get()
        security_answer = security_ans_entry.get()
        new_password = new_password_entry.get()
        confirm_password = con_new_password_entry.get()

        if not user_id_val and not security_answer and not new_password and not confirm_password:
            messagebox.showinfo("Warning", "Please fill in all the fields.")
            user_id_entry.focus_set()
            return
        if not user_id_val:
            messagebox.showinfo("Warning", "Pease enter user id.")
            user_id_entry.focus_set()
            return
        if not question_label:
            messagebox.showinfo("Warning", "Please select question .")
            question_label.focus_set()
            return
        if not security_answer:
            messagebox.showinfo("Warning", "Please enter your security answer.")
            security_ans_entry.focus_set()
            return    
        if not new_password:
            messagebox.showinfo("Warning", "Please enter your new password.")
            new_password_entry.focus_set()
            return
        if not confirm_password:
            messagebox.showinfo("Warning", "Please enter confirm password.")
            con_new_password_entry.focus_set()
            return
        if new_password != confirm_password:
            messagebox.showinfo("Warning", "your new password does not match with your confirm password.")
            con_new_password_entry.focus_set()
            return

        conn = mysql.connector.connect(
            user='root',
            password='#Deepti2003',
            host='127.0.0.1',
            database='priti'
        )
        cursor = conn.cursor()

        sql = f"SELECT * FROM {user_type} WHERE user_id=%s AND security_question=%s AND security_answer=%s"
        cursor.execute(sql, (user_id_val, question_label.get(), security_answer))
        result = cursor.fetchone()

        if result:
            sql_update = f"UPDATE {user_type} SET password=%s WHERE user_id=%s"
            cursor.execute(sql_update, (new_password, user_id_val))
            conn.commit()
            messagebox.showinfo("Success", "Your password has been updated successfully.")
            login()
        else:
            messagebox.showerror("Error", "Incorrect security answer.")

        conn.close()

    def go_back():
        if user_type == "faculty":
            login(user_type="faculty")
        elif user_type == "students":
            login(user_type="students")
        elif user_type == "principal":
            login(user_type="principal")
        elif user_type == "admin":
            login(user_type="admin")
        else:
            home_page()
    def cancel():
        if user_type == "faculty":
            forgot_password(user_type="faculty")
        elif user_type == "students":
            forgot_password(user_type="students")
        elif user_type == "principal":
            forgot_password(user_type="principal")
        elif user_type == "admin":
            forgot_password(user_type="admin")
        else:
            home_page()             

    question_label.bind("<Button-1>", fetch_security_question)
    Button(root, text="SUBMIT", bg="orange", fg="#E2E8F0", font=("Arial", 11, "bold"), width=8, bd=8, command=handle_submit).place(x=550, y=650)
    Button(root, text="◄-- BACK", bg="#2B6CB0", fg="#E2E8F0", font=("Arial", 11, "bold"), width=8, bd=8, command=go_back).place(x=20, y=795)
    Button(root, text="CANCEL", bg="orange", fg="#E2E8F0", font=("Arial", 12, "bold"), width=8, bd=8, command=cancel).place(x=750, y=650)

def delete_information(user_type=None, viewer_type=None, login_user_id=None, target_user_type=None):
    root.title(" DELETE INFO PANNEL ")
    clear_frame()
    canvas.delete("all") 
    canvas.create_image(350, 50, image=function_bg_image, anchor="nw")
    create_sidebar(user_type=user_type, login_user_id=login_user_id)
    add_header()
    lower_frame()
 
    valid_user_types = ["admin", "faculty", "principal", "students"]
    if viewer_type not in valid_user_types:
        messagebox.showerror("Error", "Invalid viewer type!")
        return

    if viewer_type == "admin":
        if not target_user_type:
            profile_user_type = "admin"
        elif target_user_type in ["faculty", "students"]:
            profile_user_type = target_user_type
        else:
            messagebox.showerror("Error", "Invalid target user type!")
            return
    else:
        profile_user_type = user_type

    title = "Admin" if profile_user_type == "admin" else f"{profile_user_type.capitalize()}"
    create_canvas_text(canvas, 1000, 150,f"DELETE ({title})", font=("Rockwell",28, "bold italic underline"), fill="cyan")
    
    create_canvas_text(canvas,700,250, "ENTER USER ID:", font=("Arial",18,"bold"), fill="#F1C6B1", anchor="w")
    user_id_combobox = None

    if profile_user_type in ["faculty", "students"] and viewer_type == "admin":
        user_id_combobox = ttk.Combobox(root, state="readonly", width=38)
        user_id_combobox.place(x=900, y=235)

        def populate_user_id_combobox():
            nonlocal user_id_combobox
            conn = mysql.connector.connect(
                user='root',
                password='#Deepti2003',
                host='127.0.0.1',
                database='priti'
            )
            cursor = conn.cursor()
            query = f"SELECT USER_ID FROM {profile_user_type}"
            cursor.execute(query)
            result = cursor.fetchall()
            user_ids = [str(row[0]) for row in result]
            user_id_combobox["values"] = user_ids
            conn.close()

        populate_user_id_combobox()
        user_id_entry = user_id_combobox
    else:
        user_id_entry = Entry(root, font=("Arial", 14), bg="white", width=40)
        user_id_entry.place(x=900, y=235)
        if isinstance(user_id_entry, Entry):
            user_id_entry.delete(0, END)
            user_id_entry.insert(0, login_user_id)
    create_canvas_text(canvas,700,300, "EMPLOYEE ID:", font=("Arial",18,"bold"), fill="#F1C6B1", anchor="w")
    emp_id_entry = Entry(root, font=("Arial", 14), bg="white", width=40, state="disabled")
    emp_id_entry.place(x=900, y=305)

    create_canvas_text(canvas,700,370, "FULL NAME:", font=("Arial",18,"bold"), fill="#F1C6B1", anchor="w")
    name_entry = Entry(root, font=("Arial", 14), bg="white", width=40)
    name_entry.place(x=900, y=375)

    create_canvas_text(canvas,700,440, "PHONE NO:", font=("Arial",18,"bold"), fill="#F1C6B1", anchor="w")
    phone_entry = Entry(root, font=("Arial", 14), bg="white", width=40)
    phone_entry.place(x=900, y=445)

    create_canvas_text(canvas,700,510, "EMAIL ID:", font=("Arial",18,"bold"), fill="#F1C6B1", anchor="w")
    email_entry = Entry(root, font=("Arial", 14), bg="white", width=40)
    email_entry.place(x=900, y=515)

    create_canvas_text(canvas,700,580, "GENDER:", font=("Arial",18,"bold"), fill="#F1C6B1", anchor="w")
    gender_entry =  ttk.Combobox(root, state="readonly", values=["Male", "Female", "Other"], width=40)
    gender_entry.place(x=900, y=585)

    def populate_details():
        conn = mysql.connector.connect(
            user='root',
            password='#Deepti2003',
            host='127.0.0.1',
            database='priti'
        )
        cursor = conn.cursor()

        user_id = user_id_entry.get().strip() if isinstance(user_id_entry, Entry) else user_id_combobox.get()

        query = f"SELECT USER_ID, EMP_ID, FULL_NAME, PHONE_NO, EMAIL_ID, GENDER FROM {profile_user_type} WHERE USER_ID = %s"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        conn.close()

        if result:
            if isinstance(user_id_entry, Entry):
                user_id_entry.delete(0, END)
                user_id_entry.insert(0, result[0])
            elif isinstance(user_id_combobox, ttk.Combobox):
                user_id_combobox.set(result[0])

            emp_id_entry.config(state="normal")
            emp_id_entry.delete(0, END)
            emp_id_entry.insert(0, result[1])
            emp_id_entry.config(state="disabled")

            name_entry.delete(0, END)
            name_entry.insert(0, result[2])
            phone_entry.delete(0, END)
            phone_entry.insert(0, result[3])
            email_entry.delete(0, END)
            email_entry.insert(0, result[4])
            gender_entry.set(result[5])
        else:
            messagebox.showinfo("Error", "No data found for the entered User ID.")

    def handle_delete():
        user_id = user_id_entry.get()
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        gender = gender_entry.get()

        if not user_id and not name and not phone and not email and not gender:
            messagebox.showinfo("Warning", "All fields are required.")
            return
        if not name:
            messagebox.showinfo("warning","please enter your Full name.")
            name_entry.focus_set()
            return
        if not phone.isdigit() or len(phone) != 10:
            messagebox.showinfo("Warning", "Phone number must be exactly 10 digits.")
            phone_entry.focus_set()
            return
        if not email: 
            messagebox.showinfo("warning","please enter Your Password.")
            email_entry.focus_set()
            return
        if not gender:
            messagebox.showinfo("warning","please Select Gender.")
            gender_entry.focus_set()
            return        
        
        conn = mysql.connector.connect(
            user='root',
            password='#Deepti2003',
            host='127.0.0.1',
            database='priti'
        )
        cursor = conn.cursor()

        query = f"DELETE FROM {profile_user_type} WHERE USER_ID = %s"
        cursor.execute(query, (user_id,))
        conn.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Success", f"{str(user_type).capitalize()} information deleted successfully.")
            delete_information(user_type)
        else:
            messagebox.showinfo("Error", "Failed to delete. Please check the User ID.")
        conn.close()

        delete_information(user_type, viewer_type, login_user_id, target_user_type)

    def go_back():
        if viewer_type == "faculty":
            create_sidebar(user_type=user_type, login_user_id=login_user_id)
            admin_dashboard(login_user_id)
        elif viewer_type == "students":
            create_sidebar(user_type=user_type, login_user_id=login_user_id)
            admin_dashboard(login_user_id)
        elif viewer_type == "principal":
            create_sidebar(user_type=user_type, login_user_id=login_user_id)
            admin_dashboard(login_user_id)
        elif viewer_type == "admin":
            create_sidebar(user_type=user_type, login_user_id=login_user_id)
            admin_dashboard(login_user_id)
        else:
            home_page()

    b4 = Button(root, text="LOAD DETAILS", bg="slate gray", fg="white", font=("Arial", 12, "bold"), width=15, bd=8, command=populate_details)
    b4.place(x=830, y=680)
    b4.focus_set()
    b4.bind("<Return>", lambda event: populate_details())
    Button(root, text="DELETE", bg="red", fg="white", font=("Arial", 12, "bold"), width=15, bd=8, command=handle_delete).place(x=1150, y=750)
    Button(root, text="◄-- BACK", bg="slate gray", fg="white", font=("Arial", 12, "bold"), width=15, bd=8, command=go_back).place(x=20, y=795)

def raise_complaint(login_user_id,user_type):
    root.title(" RAISE COMPLAINT PANNEL ")
    clear_frame()
    canvas.delete("all") 
    canvas.create_image(350, 50, image=function_bg_image, anchor="nw")
    create_sidebar(user_type=user_type, login_user_id=login_user_id)
    add_header()
    lower_frame()

    create_canvas_text(canvas, 1000, 150, "RAISE A COMPLAINT", font=("Rockwell", 28, "bold italic underline"), fill="cyan")

    create_canvas_text(canvas, 700, 250, "STUDENT ID:", font=("Arial", 18, "bold"), fill="#F1C6B1", anchor="w")
    user_id_entry = Entry(root, font=("Arial", 14), bg="white", width=40)
    user_id_entry.place(x=900, y=235)

    create_canvas_text(canvas, 700, 320, "FULL NAME:", font=("Arial", 18, "bold"), fill="#F1C6B1", anchor="w")
    name_entry = Entry(root, font=("Arial", 14), bg="white", width=40, state="disabled")
    name_entry.place(x=900, y=305)

    create_canvas_text(canvas, 700, 390, "COMPLAINT ID:", font=("Arial", 18, "bold"), fill="#F1C6B1", anchor="w")
    complaint_id_entry = Entry(root, font=("Arial", 14), bg="white", width=40, state="disabled")
    complaint_id_entry.place(x=900, y=375)

    create_canvas_text(canvas, 700, 460, "EMP ID:", font=("Arial", 18, "bold"), fill="#F1C6B1", anchor="w")
    emp_id_entry = Entry(root, font=("Arial", 14), bg="white", width=40, state="disabled")
    emp_id_entry.place(x=900, y=445)

    create_canvas_text(canvas, 700, 530, "COMPLAINT:", font=("Arial", 18, "bold"), fill="#F1C6B1", anchor="w")
    predefined_complaints = ["Select a predefined complaint", "Issue with Fees", "Issue with Faculty", "Issue with Exam Schedule", "Other"]
    complaint_var = StringVar(root)
    complaint_var.set(predefined_complaints[0]) 

    complaint_dropdown = OptionMenu(root, complaint_var, *predefined_complaints)
    complaint_dropdown.config(font=("Arial", 14), bg="white", width=38)
    complaint_dropdown.place(x=900, y=515)
 
    create_canvas_text(canvas, 670, 620, "WRITE COMPLAINT:", font=("Arial", 18, "bold"), fill="#F1C6B1", anchor="w")
    complaint_entry = Text(root, font=("Arial", 14), bg="white", width=30, height=6)
    complaint_entry.place(x=1000, y=585)

    def load_all_data():
        conn = mysql.connector.connect(user='root', password='#Deepti2003', host='127.0.0.1', database='priti')
        cursor = conn.cursor()

        cursor.execute("SELECT EMP_ID, FULL_NAME, USER_ID FROM students")
        all_data = cursor.fetchall()

        if all_data:
            user_found = False
            for emp_id, full_name, user_id in all_data:
                if user_id == login_user_id:
            
                    user_id_entry.config(state="normal")
                    user_id_entry.insert(0, user_id)
                    user_id_entry.config(state="disabled", fg="black")

                    name_entry.config(state="normal")
                    name_entry.insert(0, full_name)
                    name_entry.config(state="disabled", fg="black")

                    emp_id_entry.config(state="normal")
                    emp_id_entry.insert(0, emp_id)
                    emp_id_entry.config(state="disabled", fg="black")

                    cursor.execute("SELECT COUNT(*) FROM complaint")
                    count = cursor.fetchone()[0]
                    complaint_id = f"CMP{count + 1:03d}"

                    complaint_id_entry.config(state="normal")
                    complaint_id_entry.insert(0, complaint_id)
                    complaint_id_entry.config(state="disabled", fg="black")

                    user_found = True
                    break

            if not user_found:
                messagebox.showwarning("Error", "Logged-in user details not found.")
        else:
            messagebox.showinfo("Error", "No data available in the database.")

        cursor.close()
        conn.close()

    def submit_complaint():
        emp_id = emp_id_entry.get()
        full_name = name_entry.get()
        complaint_id = complaint_id_entry.get().strip()
        selected_complaint = complaint_var.get()
        written_complaint = complaint_entry.get("1.0", "end").strip()

        if selected_complaint == predefined_complaints[0] and not written_complaint:
            messagebox.showinfo("Error", "Please select or write a complaint.")
            complaint_entry.focus_set()
            return    
        complaint = selected_complaint if selected_complaint != "Other" else written_complaint

        if not (emp_id and full_name and complaint_id and complaint):
            messagebox.showinfo("Error", "All fields are required.")
            return

        conn = mysql.connector.connect(user='root', password='#Deepti2003', host='127.0.0.1', database='priti')
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM students WHERE USER_ID = %s", (login_user_id,))
        user_exists = cursor.fetchone()[0] > 0

        if user_exists:
            cursor.execute("SELECT COMPLAIN_ID FROM complaint WHERE COMPLAIN_ID = %s", (complaint_id,))
            existing_complaint = cursor.fetchone()

            if existing_complaint:
                cursor.execute("SELECT MAX(CAST(SUBSTRING(COMPLAIN_ID, 4) AS UNSIGNED)) FROM complaint")
                max_id = cursor.fetchone()[0] or 0
                complaint_id = f"CMP{max_id + 1:03d}"

            query = """
                INSERT INTO complaint (COMPLAIN_ID, EMP_ID, FULL_NAME, COMPLAIN, COMPLAIN_STATUS)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (complaint_id, emp_id, full_name, complaint, "Pending"))
            conn.commit()

            messagebox.showinfo("Success", f"Complaint submitted successfully!\nYour Complaint ID: {complaint_id}")
            raise_complaint(login_user_id)
        else:
            messagebox.showerror("Error", "User ID does not exist. Please check the User ID.")

        cursor.close()
        conn.close()
    def go_back():
        login_user_id = session.get("login_user_id")
        if user_type == "students":
            create_sidebar(user_type, login_user_id)
            student_dashboard(login_user_id)    

    Button(root, text="SUBMIT", bg="slate gray", fg="greenyellow", font=("Arial", 12, "bold"), width=12, bd=8, command=submit_complaint).place(x=800, y=750)
    Button(root, text="◄-- BACK", bg="slate gray", fg="greenyellow", font=("Arial", 12, "bold"), width=10, bd=8, command=go_back).place(x=20, y=795)

    load_all_data()

def view_complaints_feedback(user_type=None, viewer_type=None, login_user_id=None):
    root.title(" VIEW COMPLAINTS AND FEEDBACK PANNEL ")
    clear_frame()
    canvas.delete("all") 
    canvas.create_image(350, 50, image=function_bg_image, anchor="nw")
    create_sidebar(user_type=user_type, login_user_id=login_user_id)
    add_header()
    lower_frame()
    session["login_user_id"] = login_user_id

    create_canvas_text(canvas,1000,100, "VIEW COMPLAINTS", font=("Rockwell",28, "bold italic underline"), fill="cyan")    

    create_canvas_text(canvas,400,200, "COMPLAINT ID:", font=("Arial",12,"bold"), fill="#F1C6B1", anchor="w")
    create_canvas_text(canvas,550,200, "EMP ID:", font=("Arial",12,"bold"), fill="#F1C6B1", anchor="w")
    create_canvas_text(canvas,650,200, "FULL NAME:", font=("Arial",12,"bold"), fill="#F1C6B1", anchor="w")
    create_canvas_text(canvas,870,200, "COMPLAINT:", font=("Arial",12,"bold"), fill="#F1C6B1",anchor="w")
    create_canvas_text(canvas,1100,200, "STATUS:", font=("Arial",12,"bold"), fill="#F1C6B1",anchor="w")
    create_canvas_text(canvas,1260,200, "FEEDBACK:", font=("Arial",12,"bold"), fill="#F1C6B1",anchor="w")

    if not login_user_id:
        Label(root, text="Error: No user logged in.", font=("Arial", 14, "bold"), fg="red").place(x=370, y=150)
        return
        
    def go_back():
        login_user_id = session.get("login_user_id")
        if viewer_type == "students":
            create_sidebar(viewer_type, login_user_id)
            student_dashboard(login_user_id)
        else:
            home_page()

    conn = mysql.connector.connect(
        user='root',
        password='#Deepti2003',
        host='127.0.0.1',
        database='priti'
    )
    cursor = conn.cursor()

    # Fetch complaints for the logged-in student user
    query = """
    SELECT 
        c.COMPLAIN_ID, 
        c.EMP_ID, 
        s.FULL_NAME, 
        c.COMPLAIN, 
        c.COMPLAIN_STATUS, 
        c.FEEDBACK
    FROM 
        complaint c
    JOIN 
        students s 
    ON 
        c.EMP_ID = s.EMP_ID
    WHERE 
        s.USER_ID = %s
    """
    cursor.execute(query, (login_user_id,))

    complaints = cursor.fetchall()
    conn.close()

    if not complaints:
        Label(root, text="No complaints to display.", font=("Arial", 14, "bold"), fg="red").place(x=80, y=150)
        messagebox.showinfo("No complaints to display.", "You have no complaints!")
        go_back()
        return

    y_position = 250

    for complaint in complaints:
        Label(root, text=complaint[0], font=("Arial", 10), bg="#F5E1A4", width=15, anchor="w").place(x=400, y=y_position)
        Label(root, text=complaint[1], font=("Arial", 10), bg="#F5E1A4", width=10, anchor="w").place(x=550, y=y_position)
        Label(root, text=complaint[2], font=("Arial", 10), bg="#F5E1A4", width=15, anchor="w").place(x=650, y=y_position)
        Label(root, text=complaint[3], font=("Arial", 10), bg="#F5E1A4", width=25, anchor="w").place(x=830, y=y_position)
        Label(root, text=complaint[4], font=("Arial", 10), bg="#F5E1A4", width=10, anchor="w").place(x=1100, y=y_position)

        # Student view: submitting feedback
        feedback_spinbox = Spinbox(root, 
                                   values=("Resolved", "Not Resolved", "Pending", "Needs Attention"), 
                                   font=("Arial", 10), 
                                   width=15)
        default_feedback = complaint[5] if complaint[5] else "Select Feedback"
        feedback_spinbox.delete(0, "end") 
        feedback_spinbox.insert(0, default_feedback)  
        feedback_spinbox.place(x=1250, y=y_position)
        Button(
            root,
            text="Submit",
            font=("Arial", 10),
            bg="lightblue",
            command=lambda cid=complaint[0], sb=feedback_spinbox, ypos=y_position: submit_feedback(cid, sb, ypos)
        ).place(x=1400, y=y_position-7)

        y_position += 50

    def submit_feedback(complaint_id, spinbox_widget,y_pos):
        feedback = spinbox_widget.get().strip()
        conn = mysql.connector.connect(
            user='root',
            password='#Deepti2003',
            host='127.0.0.1',
            database='priti'
        )
        cursor = conn.cursor()
        update_query = "UPDATE complaint SET FEEDBACK = %s WHERE COMPLAIN_ID = %s"
        cursor.execute(update_query, (feedback, complaint_id))
        conn.commit()
        conn.close()
        
        spinbox_widget.delete(0, "end")   
        spinbox_widget.insert(0, feedback) 
        Label(root, text="Feedback submitted!", font=("Arial", 10), fg="green", bg="#F5E1A4").place(x=850, y=y_pos+20)

    Button(root, text="◄-- BACK", bg="slate gray", fg="greenyellow", font=("Arial", 12, "bold"), width=10, bd=8, command=go_back).place(x=20, y=795)
    Button(root, text="LOGOUT", bg="slate gray", fg="greenyellow", font=("Arial", 12, "bold"), width=10, bd=8, command=home_page).place(x=150, y=y_position + 20)

def handle_complaints(user_type=None, viewer_type=None, login_user_id=None):
    root.title(" HANDEL COMPLAINTS ")
    clear_frame()
    canvas.delete("all") 
    canvas.create_image(350, 50, image=function_bg_image, anchor="nw")
    create_sidebar(user_type=user_type, login_user_id=login_user_id)
    session["login_user_id"] = login_user_id
    add_header()
    lower_frame()

    def fetch_complaints(status_filter=None):
        """Fetch complaints from the database with an optional status filter."""
        conn = mysql.connector.connect(
            user='root',
            password='#Deepti2003',
            host='127.0.0.1',
            database='priti'
        )
        cursor = conn.cursor()
        if status_filter:
            query = "SELECT COMPLAIN_ID, FULL_NAME, COMPLAIN, COMPLAIN_STATUS, FEEDBACK FROM complaint WHERE COMPLAIN_STATUS = %s"
            cursor.execute(query, (status_filter,))
        else:
            query = "SELECT COMPLAIN_ID, FULL_NAME, COMPLAIN, COMPLAIN_STATUS, FEEDBACK FROM complaint"
            cursor.execute(query)
        complaints = cursor.fetchall()
        conn.close()
        return complaints

    def fetch_feedback(complain_id):
        """Fetch feedback for a specific COMPLAIN_ID."""
        conn = mysql.connector.connect(
            user='root',
            password='#Deepti2003',
            host='127.0.0.1',
            database='priti'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT FEEDBACK FROM complaint WHERE COMPLAIN_ID = %s", (complain_id,))
        feedback = cursor.fetchone()
        conn.close()
        return feedback[0] if feedback else "No feedback"

    def display_complaints(status_filter=None):
        """Display complaints based on the selected filter."""
        root.title(" HANDEL COMPLAINTS ")
        clear_frame()
        canvas.delete("all") 
        canvas.create_image(350, 50, image=function_bg_image, anchor="nw")
        create_sidebar(user_type=user_type, login_user_id=login_user_id)
        session["login_user_id"] = login_user_id
        add_header()
        lower_frame()

        Label(root, text="UPDATE COMPLAINTS", fg="white", bg="#290916", font=("Rockwell", 24, "bold")).place(x=180, y=20)

        if viewer_type == "faculty":
            Button(root, text="PENDING", bg="orange", fg="white", font=("Arial", 12, "bold"), width=12, bd=5, 
                   command=lambda: display_complaints("Pending")).place(x=20, y=80)
            Button(root, text="NEW", bg="green", fg="white", font=("Arial", 12, "bold"), width=12, bd=5, 
                   command=lambda: display_complaints("new")).place(x=300, y=80)
            Button(root, text="COMPLETE", bg="blue", fg="white", font=("Arial", 12, "bold"), width=12, bd=5, 
                   command=lambda: display_complaints("complete")).place(x=550, y=80)
            Button(root, text="ALL", bg="blue", fg="white", font=("Arial", 12, "bold"), width=12, bd=5, 
                   command=lambda: display_complaints("")).place(x=750, y=80)

        Label(root, text="COMPLAINT ID", font=("Arial 12 bold underline"), width=12, anchor="nw").place(x=400, y=300)
        Label(root, text="FULL NAME", font=("Arial 12 bold underline"), width=10, anchor="nw").place(x=620, y=300)
        Label(root, text="COMPLAINT", font=("Arial 12 bold underline"), width=10, anchor="nw").place(x=850, y=300)
        Label(root, text="STATUS", font=("Arial 12 bold underline"), width=7, anchor="nw").place(x=1110, y=300)
        Label(root, text="FEEDBACK", font=("Arial 12 bold underline"), width=10, anchor="nw").place(x=1300, y=300)

        complaints = fetch_complaints(status_filter)
        y_position = 400

        if not complaints:
            Label(root, text="No complaints to display.", font=("Arial", 14, "bold"), fg="red").place(x=400, y=y_position)
            return

        for complaint in complaints:
            Label(root, text=complaint[0], font=("Arial", 10), width=15, anchor="w").place(x=400, y=y_position)
            Label(root, text=complaint[1], font=("Arial", 10), width=15, anchor="w").place(x=620, y=y_position)
            Label(root, text=complaint[2], font=("Arial", 10), width=30, anchor="w").place(x=820, y=y_position)
            Label(root, text=fetch_feedback(complaint[0]), font=("Arial", 10), width=15, anchor="w").place(x=1300, y=y_position)

            if viewer_type == "faculty":
               status_spinbox = Spinbox(root, values=("new", "pending", "Complete"), font=("Arial", 10), width=15)
               default_status = complaint[3] if complaint[3] else "Select Feedback"
               status_spinbox.delete(0, "end")
               status_spinbox.insert(0, default_status)
               status_spinbox.place(x=1100, y=y_position)

               Button(root, text="update", bg="slate gray", fg="greenyellow", font=("Arial", 12, "bold"), 
                       command=lambda cid=complaint[0], sb=status_spinbox: update_status(cid, sb.get())).place(x=1220, y=y_position - 5)

            y_position += 50

        def update_status(complaint_id, new_status):
          conn = mysql.connector.connect(
            user='root',
            password='#Deepti2003',
            host='127.0.0.1',
            database='priti'
          )
          cursor = conn.cursor()
          query = "UPDATE complaint SET COMPLAIN_STATUS = %s WHERE COMPLAIN_ID = %s"
          cursor.execute(query, (new_status, complaint_id))
          conn.commit()
          conn.close()
          messagebox.showinfo("Success", f"Complaint ID {complaint_id} status updated to {new_status}.")
          display_complaints(status_filter)

        def go_back():
            login_user_id = session.get("login_user_id")
            if viewer_type == "faculty":
                create_sidebar(user_type, login_user_id)
                faculty_dashboard(login_user_id)
            else:
                home_page()

        if viewer_type == "faculty": 
            Button(root, text="UPDATE", bg="slate gray", fg="greenyellow", font=("Arial", 12, "bold"), width=12, bd=8, 
                   command=update_status).place(x=250, y=500)

        Button(root, text="◄-- BACK", bg="slate gray", fg="greenyellow", font=("Arial", 12, "bold"), width=10, bd=8, 
               command=go_back).place(x=20, y=795)

    # Default display (no filter)
    display_complaints()

def view_complaints_faculty_principal(viewer_type=None,user_type=None, login_user_id=None):
    root.title(" VIEW ALL STUDENTS COMPLAINTS ")
    clear_frame()
    canvas.delete("all") 
    canvas.create_image(350, 50, image=login_bg_image, anchor="nw")
    create_sidebar(user_type=user_type, login_user_id=login_user_id)
    session["login_user_id"] = login_user_id
    add_header()
    lower_frame()
    create_canvas_text(canvas,1000,150, "VIEW ALL COMPLAINTS", font=("Rockwell",28, "bold italic underline"), fill="cyan")    

    Label(root, text="COMPLAINT ID", font=("Arial 12 bold underline"), bg="#F5E1A4", width=15, anchor="center").place(x=400, y=250)
    Label(root, text="FULL NAME", font=("Arial 12 bold underline"), bg="#F5E1A4", width=15, anchor="center").place(x=600, y=250)
    Label(root, text="COMPLAINT", font=("Arial 12 bold underline"), bg="#F5E1A4", width=30, anchor="center").place(x=800, y=250)
    Label(root, text="STATUS", font=("Arial 12 bold underline"), bg="#F5E1A4", width=10, anchor="center").place(x=1200, y=250)
    if user_type == "principal":
        Label(root, text="FEEDBACK", font=("Arial 12 bold underline"), bg="#F5E1A4", width=15, anchor="center").place(x=1400, y=250)

    conn = mysql.connector.connect(
        user='root',
        password='#Deepti2003',
        host='127.0.0.1',
        database='priti'
    )
    cursor = conn.cursor()

    query = """ SELECT COMPLAIN_ID, FULL_NAME, COMPLAIN, COMPLAIN_STATUS, FEEDBACK FROM complaint """
    cursor.execute(query)
    complaints = cursor.fetchall()
    conn.close()

    if not complaints:
        Label(root, text="No complaints to display.", font=("Arial", 14, "bold"), fg="red").place(x=600, y=300)
        return

    y_position = 350
    for complaint in complaints:
        Label(root, text=complaint[0], font=("Arial", 10), bg="#F5E1A4", width=15, anchor="center").place(x=410, y=y_position)
        Label(root, text=complaint[1], font=("Arial", 10), bg="#F5E1A4", width=15, anchor="center").place(x=610, y=y_position)
        Label(root, text=complaint[2], font=("Arial", 10), bg="#F5E1A4", width=30, anchor="center").place(x=830, y=y_position)
        Label(root, text=complaint[3], font=("Arial", 10), bg="#F5E1A4", width=10, anchor="center").place(x=1210, y=y_position)

        if user_type == "principal":
            Label(root, text=complaint[4], font=("Arial", 10), bg="#F5E1A4", width=15, anchor="center").place(x=1400, y=y_position)

        y_position += 40

    def go_back():
        login_user_id = session.get("login_user_id")
        if user_type == "faculty":
            create_sidebar(user_type, login_user_id)
            faculty_dashboard(login_user_id)
        elif user_type == "principal":
            create_sidebar(user_type, login_user_id)
            principal_dashboard(login_user_id)
        else:
            home_page()

    Button(root, text="◄-- BACK", bg="slate gray", fg="greenyellow", font=("Arial", 12, "bold"), width=10, bd=8, command=go_back).place(x=20, y=795)
home_page()
root.mainloop()