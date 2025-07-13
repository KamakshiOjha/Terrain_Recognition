from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
import cv2
import os
import base64
from io import BytesIO

app = Flask(__name__, static_folder='static', template_folder='templates')

# Load the saved model
model = None

def load_model():
    global model
    # Update this path to where your model file is stored
    model_path = 'terrin_weights.h5'
    if os.path.exists(model_path):
        model = tf.keras.models.load_model(model_path)
        print("Model loaded successfully!")
    else:
        print(f"Model file not found at {model_path}")

# Load model at startup instead of using before_first_request (which is deprecated)
with app.app_context():
    load_model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'image' not in request.files:
            return jsonify({'error': 'No image part'})
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No selected file'})
        
        try:
            # Read the image file
            img_data = file.read()
            img_np = np.frombuffer(img_data, np.uint8)
            img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)
            
            # Preprocess the image
            img_resized = cv2.resize(img, (224, 224))
            img_normalized = img_resized.astype('float32') / 255.0
            img_batch = np.expand_dims(img_normalized, axis=0)
            
            # Make prediction
            if model is not None:
                prediction = model.predict(img_batch)
                class_index = np.argmax(prediction, axis=1)[0]
                confidence = float(prediction[0][class_index]) * 100
                
                # Class mapping
                class_names = ['grassy', 'marshy', 'rocky', 'sandy']
                terrain_type = class_names[class_index]
                
                # Get image as base64 for display
                _, buffer = cv2.imencode('.jpg', img_resized)
                img_base64 = base64.b64encode(buffer).decode('utf-8')
                
                return jsonify({
                    'success': True,
                    'class': terrain_type,
                    'confidence': confidence,
                    'image': f'data:image/jpeg;base64,{img_base64}'
                })
            else:
                return jsonify({'error': 'Model not loaded'})
                
        except Exception as e:
            return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5001) 