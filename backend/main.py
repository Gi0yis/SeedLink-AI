from app import create_app

app = create_app()

app.add_url_rule("/model1", "model1", model1_predict, methods=["POST"])
app.add_url_rule("/model2", "model2", model2_predict, methods=["POST"])
app.add_url_rule("/model3", "model3", model3_predict, methods=["POST"])
app.add_url_rule("/model4", "model4", model4_predict, methods=["POST"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)