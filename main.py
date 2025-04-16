# main.py

from tkinter import messagebox
from Model import CareerPredictor

# Create a CareerPredictor object
predictor = CareerPredictor()

# Load and train the model
predictor.load_and_train()

def submit_form(user_profile):
    """
    Handles the prediction logic based on the user profile.
    """
    try:
        # Predict the top careers
        predictions = predictor.predict(user_profile, top_n=3)
        prediction_text = "\n".join([f"{career}: {score}%" for career, score in predictions])
        messagebox.showinfo("Predicted Careers", prediction_text)
    except Exception as e:
        messagebox.showerror("Error", str(e))