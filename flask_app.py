from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Load the model from the .pkl file
with open('wine_quality_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract input data from the request
    citric_acid = float(request.form['citric_acid'])
    residual_sugar = float(request.form['residual_sugar'])  
    alcohol = float(request.form['alcohol'])  
    # Preprocess the input data and make predictions using the loaded model
    prediction = loaded_model.predict([[citric_acid, residual_sugar, alcohol]])
    return jsonify({'prediction': str(prediction[0])}) 


if __name__ == '__main__':
    app.run(debug=True)