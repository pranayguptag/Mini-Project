from flask import Flask, render_template, request
from crop_ml import predict_crop  # Assuming crop_ml.py has a predict function

app = Flask(__name__)

@app.route("/", methods=["GET"])  # Route for displaying the form
def index():
    # Display the form on GET request
    return render_template("index.html")

@app.route("/predict", methods=["POST"])  # Route for handling prediction request
def predict():
    # Get user input on POST request
    nitrogen = float(request.form["nitrogen"])
    phosphorus = float(request.form["phosphorus"])
    potassium = float(request.form["potassium"])
    temperature = float(request.form.get("temperature"))  # Handle potential missing key
    humidity = float(request.form.get("humidity"))  # Handle potential missing key
    ph = float(request.form.get("ph"))  # Handle potential missing key
    rainfall = float(request.form.get("rainfall"))  # Handle potential missing key

    # Call your machine learning model
    prediction = predict_crop(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall)

    # Render the template with the prediction (optional, can redirect to success page)
    return render_template("index.html", prediction=prediction)

@app.route('/show_form')
def show_form():
    return render_template('forms.html')

@app.route('/show_loan')
def show_loan():
    return render_template('loan.html')

if __name__ == "__main__":
    app.run(debug=True)