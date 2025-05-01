# server.py
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import re
import os
app = Flask(__name__)
CORS(app) 

# Folder where we want to save files
SAVE_FOLDER = 'All_Problems'

# Make sure the folder exists
if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

def clean_filename(title):
    # Example Title: "643. Maximum Average Subarray I"
    match = re.match(r"(\d+)\.\s(.+)", title)
    if match:
        problem_number = match.group(1)
        problem_name = match.group(2).replace(' ', '_').replace('-', '_')
        filename = f"#{problem_number}-{problem_name}.py"
    else:
        # fallback if title parsing fails
        filename = title.replace(' ', '_').replace('.', '').replace('-', '_') + '.py'
    return filename

@app.route('/upload', methods=['POST'])
def upload_code():
    data = request.get_json()
    #print('Received data:', data)  # Log the received data

    title = data.get('title')
    code = data.get('code')

    if not title or not code:
        return jsonify({"message": "Invalid data"}), 400

    filename = clean_filename(title)
    filepath = os.path.join(SAVE_FOLDER, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(code)

    print(f"✅ Saved {filename} successfully!")

    return jsonify({"message": "Code saved successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
