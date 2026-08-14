from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        open_price = float(request.form["open"])
        high_price = float(request.form["high"])
        low_price = float(request.form["low"])
        volume = float(request.form["volume"])

        # Prepare input
        input_data = [[open_price, high_price, low_price, volume]]

        # Make prediction
        prediction = model.predict(input_data)[0]

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)