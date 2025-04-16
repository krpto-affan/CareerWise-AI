CareerWise AI 🎓🤖
An AI-powered career prediction tool that helps students discover suitable career paths based on their interests and strengths.

🔍 About the Project
CareerWise AI uses a trained Machine Learning model to suggest the top 3 career options based on your responses. The user interface is built using CustomTkinter and collects inputs through intuitive radio buttons, offering a smooth and accessible experience for students and career counselors.

🚀 Features
Predicts top 3 career paths based on user input

Simple and clean GUI using radio buttons (0–5 scale)

Built with CustomTkinter, scikit-learn, and Pandas

Lightweight and easy to run on most systems

🖥 How It Works
Select your interest/skill level (0 to 5) for each subject area using radio buttons

Click Submit

Get your top 3 recommended career paths!

🛠️ Installation
Clone the Repository

bash
Copy
Edit
git clone https://github.com/yourusername/CareerWise-AI.git
cd CareerWise-AI
Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the Application

bash
Copy
Edit
python Run.py
Make sure you’re using Python 3.8 or higher.

📂 Project Structure
graphql
Copy
Edit
CareerWise-AI/
├── Run.py                # Entry point to launch the application
├── GUI.py                # GUI layout using CustomTkinter
├── Model.py              # Career prediction model logic
├── requirements.txt      # Required libraries
└── README.md             # Project documentation
❓ Help
In the GUI, each question has options from 0 (lowest) to 5 (highest). Just select your level using the radio buttons for each field, then press Submit. The app will show your best-suited career options based on your input.