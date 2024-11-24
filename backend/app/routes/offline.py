from flask import Blueprint, request, jsonify
from ..models.llama_model import LlamaModel
from ...database.sqlite_manager import DatabaseManager

offline_bp = Blueprint("offline", __name__)
llama_model = LlamaModel()
db_manager = DatabaseManager()

@offline_bp.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        user_input = data.get("input", "")
        if not user_input:
            return jsonify({"error": "No se proporcionó entrada"}), 400

        prediction = llama_model.predict(user_input)
        db_manager.insert_input(user_input, prediction)

        return jsonify({"input": user_input, "prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@offline_bp.route('/history', methods=['GET'])
def get_history():
    try:
        history = db_manager.get_all_inputs()
        return jsonify({"history": history})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
