import customtkinter as ctk
from PIL import Image, ImageTk

import GUI  # Import the gui.py file

# Main application window
app = ctk.CTk()
app.geometry("1200x716")
app.title("CareerWise AI")

# Center the window
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width // 2) - (1200 // 2)
y = (screen_height // 2) - (716 // 2)
app.geometry(f"1200x716+{x}+{y}")

# Load the image
image_path = "LandingPage.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = ctk.CTkLabel(app, image=photo, text="")
image_label.pack()

def open_project_window():
    new_window = ctk.CTkToplevel(app)
    new_window.title("Project Info")
    new_window.geometry("1200x720+210+270")
    image_path = "Project InfoAI.jpg"
    try:
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        new_window.photo = photo
    except Exception as e:
        print(f"Error loading image: {e}")
        return
    image_label = ctk.CTkLabel(new_window, image=new_window.photo, text="")
    image_label.pack(expand=True, fill='both')

def open_team_window():
    new_window = ctk.CTkToplevel(app)
    new_window.title("Meet the Team")
    new_window.geometry("1020x480+210+270")
    image_path = "Meet the Team.png"
    try:
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        new_window.photo = photo
    except Exception as e:
        print(f"Error loading image: {e}")
        return
    image_label = ctk.CTkLabel(new_window, image=new_window.photo, text="")
    image_label.pack(expand=True, fill='both')

def open_help_window():
    new_window = ctk.CTkToplevel(app)
    new_window.title("Help")
    new_window.geometry("1020x480+210+270")
    image_path = "Help.png"
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    new_window.photo = photo
    image_label = ctk.CTkLabel(new_window, image=new_window.photo, text="")
    image_label.pack(expand=True, fill='both')

def open_get_started_window():
    # Create a new top-level window
    get_started_window = ctk.CTkToplevel(app)
    get_started_window.title("AI Career Counselor")
    get_started_window.geometry("800x850")

    # Call the code from gui.py to create the form inside the top-level window
    GUI.build_gui(get_started_window)  # Pass the toplevel window as the parent

button_project = ctk.CTkButton(master=app, text="Project Info", corner_radius=30, bg_color="#FFFFFF", hover_color="#FFC907", fg_color="#000000", border_width=0, text_color="#FFFFFF", command=open_project_window)
button_project.place(x=660, y=650)
button_Team = ctk.CTkButton(master=app, text="Meet the Team", corner_radius=30, bg_color="#FFFFFF", hover_color="#FFC907", fg_color="#000000", border_width=0, text_color="#FFFFFF", command=open_team_window)
button_Team.place(x=830, y=650)
button_Help = ctk.CTkButton(master=app, text="Help", corner_radius=30, bg_color="#FFFFFF", hover_color="#FFC907", fg_color="#000000", border_width=0, text_color="#FFFFFF", command=open_help_window)
button_Help.place(x=1010, y=650)
button_started = ctk.CTkButton(master=app, text="Get Started", corner_radius=30, bg_color="#FFFFFF", hover_color="#FFC907", fg_color="#000000", border_width=0, text_color="#FFFFFF", command=open_get_started_window, width=225, height=67)
button_started.place(x=200, y=570)
button_quit = ctk.CTkButton(master=app, text="Quit", corner_radius=30, bg_color="#FFFFFF", hover_color="#FFC907", fg_color="#000000", border_width=0, text_color="#FFFFFF", command=app.destroy, width=60)
button_quit.place(x=1060, y=21)

# Start the application
app.mainloop()
