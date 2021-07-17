from flask import Blueprint, request, jsonify, Flask
from predict import make_prediction
import pandas as pd
import config




prediction_app = Flask('prediction_app')


@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        return 'ok'




@prediction_app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Step 1: Extract POST data from request body as JSON
        json_data = request.get_json()

        if type(json_data) == dict:
            json_data = pd.DataFrame(json_data)
        else:
            json_data = json_data
       
        #file = request.files['file']
        #json_data = pd.read_csv(file)
        json_data = json_data[config.FEATURES]

        # Step 3: Model prediction
        result = make_prediction(input_data=json_data)
      
        # Step 4: Convert numpy ndarray to list
        predictions = result.tolist()
        

        # Step 5: Return the response as JSON
        return jsonify({'predictions': predictions})




if __name__ == "__main__": 
		prediction_app.run(debug=True) 