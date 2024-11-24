import torch
import numpy as np

MODEL_PATH = "./models/ml/crop_predictor.pt"

class CropModel:
    def __init__(self):
        self.model = torch.load(MODEL_PATH)
        self.model.eval()

    def recommend(self, features):
        """
        features: Dict con datos del suelo y clima combinados.
        """
        input_data = torch.tensor([[
            features["nitrogen"],
            features["phosphorus"],
            features["potassium"],
            features["temperature"],
            features["humidity"],
            features["pH"],
            features["rainfall"]
        ]], dtype=torch.float32)
        
        with torch.no_grad():
            recommendation = self.model(input_data)

        return recommendation.numpy().tolist()[0]
