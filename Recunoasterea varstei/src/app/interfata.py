import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), '../neural_network/modele_salvate/model_varsta.keras')
IMG_SIZE = (200, 200)

CLASE = [
    '0-5 ani',
    '10-15 ani',
    '15-20 ani',
    '20-25 ani',
    '25-30 ani',
    '30-35 ani',
    '35-40 ani',
    '40-45 ani',
    '45-50 ani',
    '5-10 ani',
    '50-55 ani',
    '55-60 ani',
    '60-65 ani',
    '65-70 ani',
    '70-75 ani',
    '75-80 ani'
]

@st.cache_resource
def incarca_modelul():
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        return model
    except Exception as e:
        st.error(f"Nu am gasit modelul la calea: {MODEL_PATH}")
        st.error(f"Eroare detaliata: {e}")
        return None

def proceseaza_si_prezice(image, model):
    image = ImageOps.fit(image, IMG_SIZE, Image.Resampling.LANCZOS)
    
    img_array = np.array(image)
    
    if len(img_array.shape) == 2:
        img_array = np.stack((img_array,)*3, axis=-1)

    img_array = np.expand_dims(img_array, 0)
    predictii = model.predict(img_array)
    score = tf.nn.softmax(predictii[0])
    index_castigator = np.argmax(score)
    clasa = CLASE[index_castigator]
    incredere = 100 * np.max(score)
    
    return clasa, incredere

st.title("Detectare Varsta")
st.write("Incarca o poza cu o fata, iar Reteaua Neuronala va estima varsta.")

model = incarca_modelul()

uploaded_file = st.file_uploader("Alege o imagine...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None and model is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Imagine incarcata', use_container_width=True)
    st.write("Clasificam...")
    
    label, confidence = proceseaza_si_prezice(image, model)
    
    st.success(f"Rezultat: {label}")
    st.info(f"Probabilitate: {confidence:.2f}%")