from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import os
import psutil

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow CORS requests from any origin

# Measure memory before loading the model
process = psutil.Process(os.getpid())
before_load = process.memory_info().rss / (1024 * 1024)

# Load the model
MODEL = tf.keras.models.load_model("./models/1")
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

# Measure memory after loading the model
after_load = process.memory_info().rss / (1024 * 1024)
print(f"Memory used by model: {after_load - before_load:.2f} MB")


@app.route('/ping', methods=['GET'])
def ping():
    return "Hello, I am alive", 200


def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image


@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    image = read_file_as_image(file.read())
    img_batch = np.expand_dims(image, 0)

    # Perform prediction
    predictions = MODEL.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])

    # Measure memory after inference
    after_inference = process.memory_info().rss / (1024 * 1024)
    print(f"Memory used during inference: {after_inference - after_load:.2f} MB")

    return jsonify({
        'class': predicted_class,
        'confidence': float(confidence)
    }), 200


#if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=8000)
