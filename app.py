from flask import Flask, request, render_template, redirect, url_for
import pickle
import pandas as pd
import numpy as np
import random

app = Flask(__name__)

# Load trained model and encoder
with open("models/modelo.pkl", "rb") as f:
    model = pickle.load(f)

with open("models/encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

# Water quotes list 💧
water_quotes = [
    "💧 Save water, secure tomorrow.",
    "🌍 Every drop counts – use it wisely!",
    "🚿 Conserve water, conserve life.",
    "💙 Water is precious. Let’s not waste it.",
    "🌊 A small leak can empty a great ocean.",
    "🌧️ Rainwater is a gift – collect and use it.",
    "🌀 Don’t let our future go down the drain!",
    "🌱 Water smart, grow smart.",
    "🐟 Protect water like your life depends on it – because it does.",
    "🫧 Be cool, save the pool!"
]

# Image path utilities
def get_crop_image(crop_name):
    filename = crop_name.lower().replace(" ", "") + ".jpg"
    return f"/static/images/crops/{filename}"

def get_state_image(state_name):
    filename = state_name.lower().replace(" ", "") + ".jpg"
    return f"/static/images/states/{filename}"

# Store prediction history
prediction_history = []

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form.to_dict()
        area = float(data.pop("Area"))
        input_df = pd.DataFrame([data])

        # Encode and predict
        encoded_input = encoder.transform(input_df)
        prediction_per_hectare = model.predict(encoded_input)[0]
        total_prediction = prediction_per_hectare * area

        # Prepare data for result page
        item = {
            "crop": data['Crop'],
            "state": data['State_Name'],
            "district": data['District_Name'],
            "area": area,
            "prediction": round(total_prediction, 2)
        }
        prediction_history.append(item)

        # Pick a random water quote
        quote = random.choice(water_quotes)

        return render_template(
            "result.html",
            prediction_text=f"{item['prediction']} cubic meters",
            crop=item['crop'],
            state=item['state'],
            district=item['district'],
            area=item['area'],
            water_quote=quote,
            crop_img=get_crop_image(item['crop']),
            state_img=get_state_image(item['state'])
        )
    except Exception as e:
        return render_template("result.html", prediction_text=f"❌ Error: {e}")

@app.route('/history')
def history():
    return render_template("history.html", history=prediction_history)

if __name__ == "__main__":
    app.run(debug=True)
