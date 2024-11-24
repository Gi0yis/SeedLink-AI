from flask import Blueprint, request, jsonify
from ..models.ml_models.climate_model import ClimateModel
from ..models.ml_models.soil_model import SoilModel
from ..models.ml_models.crop_model import CropModel

ml_bp = Blueprint("ml", __name__)
climate_model = ClimateModel()
soil_model = SoilModel()
crop_model = CropModel()

@ml_bp.route('/predict/climate', methods=['POST'])
def predict_climate():
    try:
        data = request.json
        prediction = climate_model.predict(data)
        return jsonify({"climate_prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@ml_bp.route('/predict/soil', methods=['POST'])
def predict_soil():
    try:
        data = request.json
        prediction = soil_model.predict(data)
        return jsonify({"soil_prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@ml_bp.route('/recommend/crop', methods=['POST'])
def recommend_crop():
    try:
        data = request.json
        recommendation = crop_model.recommend(data)
        return jsonify({"crop_recommendation": recommendation})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
