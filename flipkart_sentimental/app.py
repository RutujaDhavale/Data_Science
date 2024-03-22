from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load your machine learning model
model = joblib.load("best_models/LR.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        text_predict = request.form.get('data')
        prediction_result = model.predict([text_predict])[0]
        return render_template("predict.html", prediction=prediction_result)
    return render_template("predict.html", prediction="")

if __name__ == "__main__":
    app.run(debug=True)
