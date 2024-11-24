import torch
import numpy as np

MODEL_PATH = "./models/ml/soil_predictor.pt"

class SoilModel:
    def __init__(self):
        self.model = torch.load(MODEL_PATH)
        self.model.eval() 

    def predict(self, features):
        """
        features: Dict con datos del suelo (nitrógeno, fósforo, potasio, pH)
        """
        input_data = torch.tensor([[
            features["nitrogen"],
            features["phosphorus"],
            features["potassium"],
            features["pH"]
        ]], dtype=torch.float32)
        
        with torch.no_grad():
            prediction = self.model(input_data)
        
        return prediction.numpy().tolist()[0]
