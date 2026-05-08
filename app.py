from flask import Flask, jsonify, render_template, request
import requests
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/classify', methods=['POST'])
def classify():
    data = request.get_json()
    name = data.get('name')
    
    if name is None:
        return jsonify({'error': 'Missing or empty name parameter'}), 400
    
    if not isinstance(name, str):
        return jsonify({'error': 'Name is not a string'}), 422
    
    name = name.strip()
    if not name:
        return jsonify({'error': 'Missing or empty name parameter'}), 400
    
    if name.isnumeric():
        return jsonify({'error': 'Name is not a string'}), 422
    
    url = f"https://api.genderize.io?name={name}"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        request_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        formatted_data = {
            'name': data.get('name'),
            'gender': data.get('gender'),
            'probability': data.get('probability'),
            'sample_size': data.get('count'),
            'is_confident': True if data.get('probability') > 0.7 and data.get('count') >= 100 else False,
            'request_time': request_time
        }
        return jsonify(formatted_data)
    else:
        return jsonify({'error': 'Failed to fetch data from Genderize API'}), 500

@app.route('/api/classify/<int:index>', methods=['DELETE'])
def delete_result(index):
    # This route acknowledges the deletion request
    # The actual deletion is handled on the client-side by removing from the array
    return jsonify({'message': 'Row deleted successfully', 'deleted_index': index}), 200
    
    
if __name__ == '__main__':   
    app.run(debug=True)