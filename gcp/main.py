from flask import Flask, request, jsonify
from google.cloud import storage
import tensorflow as tf
from PIL import Image
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


model = None
class_names = ["Early Blight", "Late Blight", "Healthy"]
BUCKET_NAME = "plant-disease-scanner-bucket"


def download_blob(bucket_name, source_blob_name, destination_file_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")


@app.route('/predict', methods=['POST'])
def predict():
    global model

    # Load model if not already loaded
    if model is None:
        try:
            download_blob(BUCKET_NAME, "models/potatoes.h5", "/tmp/potatoes.h5")
            model = tf.keras.models.load_model("/tmp/potatoes.h5")
        except Exception as e:
            return jsonify({"error": "Model loading failed: " + str(e)}), 500

    # Check if the file part is in the request
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        # Process image and predict
        image = Image.open(file).convert("RGB").resize((256, 256))
        image = np.array(image) / 255.0  # Normalize the image
        img_array = tf.expand_dims(image, 0)  # Add batch dimension

        predictions = model.predict(img_array)
        predicted_class = class_names[np.argmax(predictions[0])]
        confidence = round(100 * np.max(predictions[0]), 2)

        return jsonify({"class": predicted_class, "confidence": confidence})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# GCP Cloud Function entry point
def handle_request(request):
    """Entry point for Google Cloud Functions."""
    return app(request)

