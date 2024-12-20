# flask_api.py
from flask import Flask, request, jsonify
import pandas as pd
from pycaret.classification import load_model, predict_model

# Load the model
model = load_model('best_automl_classifier')

# Mappings for categorical features
origin_mapping = {'Ahmedabad': 0, 'Bangalore': 1, 'Chennai': 2, 'Delhi': 3, 'Hyderabad': 4,
                  'Jaipur': 5, 'Kolkata': 6, 'Lucknow': 7, 'Mumbai': 8, 'Pune': 9}

destination_mapping = {'Ahmedabad': 0, 'Bangalore': 1, 'Chennai': 2, 'Delhi': 3, 'Hyderabad': 4,
                       'Jaipur': 5, 'Kolkata': 6, 'Lucknow': 7, 'Mumbai': 8, 'Pune': 9}

vehicle_type_mapping = {'Container': 0, 'Lorry': 1, 'Trailer': 2, 'Truck': 3, 'nan': 4}

weather_conditions_mapping = {'Clear': 0, 'Fog': 1, 'Rain': 2, 'Storm': 3}

traffic_mapping = {'Heavy': 0, 'Light': 1, 'Moderate': 2}

# Initialize Flask app
app = Flask(__name__)

def predict_shipment(input_data):
    column_names = ['Origin', 'Destination', 'Shipment Date', 'Planned Delivery Date',
                    'Vehicle Type', 'Distance (km)', 'Weather Conditions', 'Traffic Conditions']

    df_test = pd.DataFrame([input_data], columns=column_names)

    try:
        df_test['Origin'] = df_test['Origin'].map(origin_mapping)
        df_test['Destination'] = df_test['Destination'].map(destination_mapping)
        df_test['Vehicle Type'] = df_test['Vehicle Type'].map(vehicle_type_mapping)
        df_test['Weather Conditions'] = df_test['Weather Conditions'].map(weather_conditions_mapping)
        df_test['Traffic Conditions'] = df_test['Traffic Conditions'].map(traffic_mapping)
        df_test['Shipment Date'] = pd.to_datetime(df_test['Shipment Date'])
        df_test['Planned Delivery Date'] = pd.to_datetime(df_test['Planned Delivery Date'])
        date_columns = ['Shipment Date', 'Planned Delivery Date']

        for col in date_columns:
            df_test[col] = pd.to_datetime(df_test[col], errors='coerce')
            df_test[f'{col}_timestamp'] = df_test[col].view('int64') / 10**9 

        df_test.columns = [col.replace(" ", "_") for col in df_test.columns]
        prediction = predict_model(model, data=df_test)

        return (1 if prediction['prediction_score'].values[0] > 0.7 else 0)
    except Exception as e:
        return str(e)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the request
        data = request.get_json()

        if not data:
            return jsonify({"error": "No input data provided"}), 400

        # Input data format
        input_data = [
            data['Origin'], data['Destination'], data['Shipment Date'], data['Planned Delivery Date'],
            data['Vehicle Type'], data['Distance'], data['Weather Conditions'], data['Traffic Conditions']
        ]

        # Get prediction
        prediction = predict_shipment(input_data)

        # Return prediction as Delayed (1) or On Time (0)
        if isinstance(prediction, str):  # In case of error message
            return jsonify({'error': prediction}), 500
        return jsonify({'Prediction': 'Delayed' if prediction == 1 else 'On Time'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
