from services.prompt_builder import build_prompt
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model4 = AutoModelForCausalLM.from_pretrained("./fine_tuned_model")
tokenizer4 = AutoTokenizer.from_pretrained("./fine_tuned_model")

def model4_predict():
    try:
        data = request.json
        prompt = build_prompt(data["climate_predictions"], data["soil_parameters"])
        inputs = tokenizer4(prompt, return_tensors="pt", padding=True, truncation=True, max_length=512)
        with torch.no_grad():
            outputs = model4.generate(inputs["input_ids"], max_length=500, attention_mask=inputs["attention_mask"])
        recommendation = tokenizer4.decode(outputs[0], skip_special_tokens=True)
        return jsonify({"prompt": prompt, "recommendation": recommendation})
    except Exception as e:
        return jsonify({"error": str(e)}), 500