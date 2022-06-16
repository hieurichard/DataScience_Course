import numpy as np
import tensorflow as tf
from fastapi import FastAPI,File, UploadFile
import cv2
from PIL import Image
import uvicorn
import nest_asyncio
import os
from io import BytesIO
import base64

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

model = None
classes = None

app = FastAPI(title="Predicting Southeast Asia Plant")

def predict(image: Image.Image):

    image = np.asarray(image.resize((128, 128)))[..., :3]
    img = tf.keras.applications.efficientnet.preprocess_input(image)
    img = np.expand_dims(img, 0)
    

    result = model.predict(img).squeeze()
    response = []
    for i in reversed(np.argsort(result)[-2:]):
        response.append({classes[i]:'%.2f %%'%(result[i]*100)})

    return response


def read_imagefile(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image


@app.on_event("startup")
def load_model():
    global model
    global classes
    # Load classifier from pickle file
    if model is None:
        model = tf.keras.models.load_model("/app/asia_plant_b0_efficientnet_v2.h5")
    if classes is None:
        classes = ['bamboo',
                 'banana',
                 'cacao',
                 'cinnamon',
                 'coffeearabica',
                 'dragonfruit',
                 'durian',
                 'frangipani',
                 'guava',
                 'jackfruit',
                 'lychee',
                 'mango',
                 'mangosteen',
                 'nilam',
                 'papaya',
                 'passiflora',
                 'sawo',
                 'snakefruit',
                 'starfruit',
                 'sugarpalm',
                 'suweg',
                 'taro',
                 'vanilla',
                 'waterguava',
                 'whitepepper',
                 'zodia']


@app.get("/")
def home():
    return "Congratulations! Your API is working as expected. Now head over to http://localhost:8000/docs"


@app.post("/predict")
async def predict_api(file: UploadFile = File(...)):
    filename = file.filename
    extension = filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"

    # chuyển file image upload lên về dạng pil image
    image = read_imagefile(await file.read())
    
    # tiến hành dự đoán và trả về 2 kết quả cao nhất
    prediction = predict(image)

    if not os.path.exists('images_uploaded'):
        os.mkdir('images_uploaded')

    # Lưu ảnh vào một folder trong server (nếu trả về ảnh)
    cv2.imwrite(f'images_uploaded/{filename}', np.array(image.resize((256,256)))[...,[2,1,0]])
    

    with open(f'images_uploaded/{filename}', "rb") as image_file:
        encoded_image_string = base64.b64encode(image_file.read())
    # trả về kết quả predict
    return{
        'filename': file.filename,
        'prediction': prediction,
        'encoded_img': encoded_image_string,
    }

