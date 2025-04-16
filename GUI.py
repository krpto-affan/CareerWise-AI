import customtkinter as ctk
from main import submit_form  # Import the submit_form function from main.py

def build_gui(root): # Encapsulate the GUI code in a function
    # --- Bento Grid Layout ---
    title_label = ctk.CTkLabel(root, text="Rate your Skills and Interests", font=ctk.CTkFont(size=20, weight="bold"))
    title_label.grid(row=0, column=0, columnspan=7, padx=20, pady=(10, 10), sticky="ew")

    subjects_skills = [
        "Maths", "Biology", "Chemistry", "Physics",
        "Coding", "Writing", "Public Speaking", "Drawing",
        "Management", "Psychology", "Finance", "Logic Reasoning",
        "Creativity", "CGPA", "Hobbies/Interests",  # Grouped checkboxes
        "Leadership", "Problem Solving", "Research Interest"
    ]

    radio_vars = {}
    widgets = {}

    for i, item in enumerate(subjects_skills):
        row = i + 1  # Start from row 1 to leave space for the title
        label_text = item

        # Label in the first column
        label = ctk.CTkLabel(root, text=label_text, anchor="w")
        label.grid(row=row, column=0, padx=(20, 10), pady=5, sticky="ew")

        if item not in ["CGPA", "Hobbies/Interests", "Leadership", "Problem Solving", "Research Interest"]:
            # Radio buttons for rating 0-5 in 6 columns
            radio_vars[item] = ctk.IntVar()
            radio_vars[item].set(-1)  # Initialize to no selection

            for j in range(6):  # Ratings 0 to 5
                radio_button = ctk.CTkRadioButton(root, text=str(j), value=j, variable=radio_vars[item])
                radio_button.grid(row=row, column=j + 1, padx=5, pady=5, sticky="w")
            widgets[item] = radio_vars[item]
        elif item == "CGPA":
            # Dropdown for CGPA
            cgpa_options = [str(i / 2) for i in range(10, 21)]  # CGPA options from 5.0 to 10.0
            cgpa_var = ctk.StringVar()
            cgpa_dropdown = ctk.CTkOptionMenu(root, variable=cgpa_var, values=cgpa_options)
            cgpa_dropdown.set("5.0")  # Set a default value
            cgpa_dropdown.grid(row=row, column=1, columnspan=6, padx=(10, 20), pady=5, sticky="ew")
            widgets[item] = cgpa_var
        elif item == "Hobbies/Interests":
            #  Checkboxes in one row
            hobby_tech_var = ctk.BooleanVar()
            hobby_reading_var = ctk.BooleanVar()
            interest_in_ai_var = ctk.BooleanVar()

            hobby_tech_checkbox = ctk.CTkCheckBox(root, text="Tech Hobby", variable=hobby_tech_var)
            hobby_reading_checkbox = ctk.CTkCheckBox(root, text="Reading Hobby", variable=hobby_reading_var)
            interest_in_ai_checkbox = ctk.CTkCheckBox(root, text="Interest in AI", variable=interest_in_ai_var)

            hobby_tech_checkbox.grid(row=row, column=1, columnspan=2, padx=(10, 0), pady=5, sticky="w")
            hobby_reading_checkbox.grid(row=row, column=3, columnspan=2, padx=(10, 0), pady=5, sticky="w")
            interest_in_ai_checkbox.grid(row=row, column=5, columnspan=2, padx=(10, 20), pady=5, sticky="w")

            widgets["Tech Hobby"] = hobby_tech_var  # Store each var individually
            widgets["Reading Hobby"] = hobby_reading_var
            widgets["Interest in AI"] = interest_in_ai_var

        elif item in ["Leadership", "Problem Solving", "Research Interest"]:
            # Radio buttons for Leadership, Problem Solving, Research Interest
            radio_vars[item] = ctk.IntVar()
            radio_vars[item].set(-1)

            for j in range(6):
                radio_button = ctk.CTkRadioButton(root, text=str(j), value=j, variable=radio_vars[item])
                radio_button.grid(row=row, column=j + 1, padx=5, pady=5, sticky="w")
            widgets[item] = radio_vars[item]

    # Submit button action
    def submit_button_action():
        user_profile = {}
        for item in subjects_skills:
            if item in radio_vars:
                user_profile[item] = radio_vars[item].get()
            elif item == "CGPA":
                user_profile[item] = widgets[item].get()
            elif item == "Hobbies/Interests":  # Handle grouped checkboxes
                user_profile["Tech Hobby"] = widgets["Tech Hobby"].get()
                user_profile["Reading Hobby"] = widgets["Reading Hobby"].get()
                user_profile["Interest in AI"] = widgets["Interest in AI"].get()
            elif item == "Leadership":
                user_profile[item] = radio_vars[item].get()
            elif item == "Problem Solving":
                user_profile[item] = radio_vars[item].get()
            elif item == "Research Interest":
                user_profile[item] = radio_vars[item].get()

        submit_form(user_profile)

    submit_button = ctk.CTkButton(root, text="Submit", command=submit_button_action)
    submit_button.grid(row=len(subjects_skills) + 1, column=0, columnspan=7, pady=20) #shift down

    # Configure column weights
    for i in range(1, 7):
        root.grid_columnconfigure(i, weight=1)

if __name__ == "__main__": #keep the if __name__ == "__main__": here
    app = ctk.CTk()
    app.geometry("800x850")
    app.title("AI Career Counselor")
    build_gui(app)
    app.mainloop()
