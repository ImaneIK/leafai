from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
<<<<<<< HEAD
import os
import psutil
=======
>>>>>>> 959934cb435c03e1e259ee7c02cc54d2b9fecc46

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000/predict",
]
app.add_middleware(
    CORSMiddleware,
<<<<<<< HEAD
    allow_origins="*",
=======
    allow_origins=origins,
>>>>>>> 959934cb435c03e1e259ee7c02cc54d2b9fecc46
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

<<<<<<< HEAD
# Measure memory before loading the model
process = psutil.Process(os.getpid())
before_load = process.memory_info().rss / (1024 * 1024)

=======
>>>>>>> 959934cb435c03e1e259ee7c02cc54d2b9fecc46
MODEL = tf.keras.models.load_model("./models/1")

CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

<<<<<<< HEAD
# Measure memory after loading the model
after_load = process.memory_info().rss / (1024 * 1024)
print(f"Memory used by model: {after_load - before_load:.2f} MB")
=======
>>>>>>> 959934cb435c03e1e259ee7c02cc54d2b9fecc46

@app.get("/ping")
async def ping():
    return "Hello, I am alive"


def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image


@app.post("/predict")
async def predict(
        file: UploadFile = File(...)
):
<<<<<<< HEAD

=======
>>>>>>> 959934cb435c03e1e259ee7c02cc54d2b9fecc46
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)

    predictions = MODEL.predict(img_batch)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
<<<<<<< HEAD

    # Measure memory after inference
    after_inference = process.memory_info().rss / (1024 * 1024)
    print(f"Memory used during inference: {after_inference - after_load:.2f} MB")

=======
>>>>>>> 959934cb435c03e1e259ee7c02cc54d2b9fecc46
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }


<<<<<<< HEAD
#if __name__ == "__main__":
#    uvicorn.run(app, host='localhost', port=8000)
=======
if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
>>>>>>> 959934cb435c03e1e259ee7c02cc54d2b9fecc46
