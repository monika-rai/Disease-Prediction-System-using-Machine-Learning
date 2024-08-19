from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Example input data
    age = int(request.form.get('age'))
    weight = float(request.form.get('weight'))
    blood_pressure = float(request.form.get('blood_pressure'))

    # Simple prediction logic (you would replace this with a real model)
    risk_score = (age / 50) + (weight / 100) + (blood_pressure / 120)
    if risk_score > 2:
        prediction = "High risk of disease"
    else:
        prediction = "Low risk of disease"

    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
