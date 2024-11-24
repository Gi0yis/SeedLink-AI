import torch
import numpy as np

MODEL_PATH = "./models/ml/climate_predictor.pt"

import torch
from flask import request, jsonify

model1 = torch.load("./model1.pth")

def model1_predict():
    try:
        data = request.json
        input_data = torch.tensor(data["input"])
        with torch.no_grad():
            output = model1(input_data)
        predictions = output.tolist()
        return jsonify({"predictions": predictions})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
