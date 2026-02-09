import tensorflow as tf
import numpy as np
import sys

MODEL_PATH = 'modele_salvate/model_varsta.keras'
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

def prezice_varsta(cale_imagine):
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
    except:
        print("Nu gasesc modelul! Ruleaza antrenare.py intai.")
        return

    print(f"Analizez imaginea: {cale_imagine} ...")
    
    try:
        img = tf.keras.utils.load_img(cale_imagine, target_size=IMG_SIZE)
        img_array = tf.keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0) 
        
        predictii = model.predict(img_array)
        score = tf.nn.softmax(predictii[0])

        clasa_castigatoare = CLASE[np.argmax(score)]
        incredere = 100 * np.max(score)

        print(f"\nRezultat: {clasa_castigatoare}")
        print(f"Siguranta: {incredere:.2f}%")

    except Exception as e:
        print(f"Eroare la procesarea imaginii: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        prezice_varsta(sys.argv[1])
    else:
        print("Utilizare: python test_poza.py cale/catre/imagine.jpg")
