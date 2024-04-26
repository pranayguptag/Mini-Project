from flask import Flask, render_template, request, send_from_directory
from crop_ml import predict_crop  # Assuming crop_ml.py has a predict function

app = Flask(__name__)

@app.route("/", methods=["GET"])  # Route for displaying the form
def index():
    # Display the form on GET request
    return render_template("index.html")

@app.route("/predict_scrollbar", methods=["POST"])  # Route for handling prediction request
def scrollbar():
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
    return render_template("search.html", scrollbar_prediction=prediction)


@app.route("/predict_dropdown", methods=["POST"])
def drop_down():
    # Sample location data (can be replaced with an actual data source)
    location_data = {
        "Delhi, India": {
            "nitrogen": 120.5,
            "phosphorus": 50.2,
            "potassium": 180.1,
            "temperature": 28.7,
            "humidity": 65.4,
            "ph": 7.2,
            "rainfall": 0.0  # Assuming no recent rainfall for this example
        },
        "Bangalore, India": {
            "nitrogen": 105.3,
            "phosphorus": 42.1,
            "potassium": 168.9,
            "temperature": 25.8,
            "humidity": 78.2,
            "ph": 6.8,
            "rainfall": 3.1  # Assuming some recent rainfall
        },
        # Add more locations as needed...
    }

    # Extract user-selected location from the request (if provided)
    selected_location = request.form.get("location")

    # Use default location data if none is selected
    #location_data_to_use = location_data.get("Bangalore, India")  # Default location
    if selected_location and selected_location in location_data:
        location_data_to_use = location_data[selected_location]

    # Extract crop data from the location data
    nitrogen = location_data_to_use["nitrogen"]
    phosphorus = location_data_to_use["phosphorus"]
    potassium = location_data_to_use["potassium"]
    temperature = location_data_to_use.get("temperature")
    humidity = location_data_to_use.get("humidity")
    ph = location_data_to_use.get("ph")
    rainfall = location_data_to_use.get("rainfall")

    # Call your machine learning model
    prediction = predict_crop(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall)

    # Render the template with the prediction (optional, can redirect to success page)
    return render_template("search.html", dropdown_prediction=prediction)

@app.route('/show_loan')
def show_loan():
    return render_template('loan.html')

@app.route('/show_form')
def show_form():
    return render_template('forms.html')

@app.route('/showpredict')
def show_search():
    return render_template('search.html')

@app.route('/ads.txt')
def ads_txt():
    # Adjust the path if your ads.txt is located elsewhere
    return send_from_directory(app.static_folder, 'ads.txt')

@app.route('/kisan_seva_logo')
def website_logo():
    # Adjust the path if your ads.txt is located elsewhere
    return send_from_directory(app.static_folder, 'kisan_seva_logo.png')

if __name__ == "__main__":
    app.run(debug=True)