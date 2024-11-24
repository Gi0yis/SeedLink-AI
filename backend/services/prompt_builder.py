def build_prompt(climate_predictions, soil_parameters):
    prompt = "Predicciones futuras:\n"
    for i, day in enumerate(climate_predictions, start=1):
        prompt += f"Day {i}: Temperature={day['Temperature']}, Humidity={day['Humidity']}, Rainfall={day['Rainfall']}\n"
    prompt += "---\nNitrogen,Phosphorus,Potassium,pH\n"
    prompt += f"{soil_parameters['Nitrogen']},{soil_parameters['Phosphorus']},{soil_parameters['Potassium']},{soil_parameters['pH']}\n---"
    return prompt
