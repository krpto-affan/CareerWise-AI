import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import numpy as np

class CareerPredictor:
    def __init__(self, dataset_path='/Users/affansmacbook/Coding/College/PBL/Sem6/AI Career Counsellor/career_dataset.csv'):
        self.dataset_path = dataset_path
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.label_encoder = LabelEncoder()
        self.trained = False
        self.features = []

    def load_and_train(self):
        df = pd.read_csv(self.dataset_path)
        X = df.drop(columns=['Career'])
        y = self.label_encoder.fit_transform(df['Career'])

        self.features = list(X.columns)
        self.model.fit(X, y)
        self.trained = True

    def predict(self, user_input: dict, top_n=3):
        if not self.trained:
            raise Exception("Model not trained. Call load_and_train() first.")

        # Ensure input is in the correct order
        input_features = [user_input.get(feature, 0) for feature in self.features]
        input_array = np.array(input_features).reshape(1, -1)

        # Predict probabilities
        probabilities = self.model.predict_proba(input_array)[0]

        # Get top N predictions
        top_indices = np.argsort(probabilities)[::-1][:top_n]
        top_careers = self.label_encoder.inverse_transform(top_indices)
        top_scores = probabilities[top_indices]

        # Convert to float to avoid np.float64 issue
        top_scores = [float(score) for score in top_scores]

        return list(zip(top_careers, (np.array(top_scores) * 100).round(2)))