import tensorflow as tf
import numpy as np
import sys

MODEL_PATH = 'modele_salvate/model_varsta.keras'
IMG_SIZE = (200, 200)

# Categoriile tale (trebuie să fie în ordine alfabetică, așa cum le citește TensorFlow din foldere)
# Verifică în data/train ordinea. De obicei e:
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
    # 1. Încărcăm modelul
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
    except:
        print("Nu găsesc modelul! Rulează antrenare.py întâi.")
        return

    # 2. Încărcăm și pregătim imaginea
    print(f"Analizez imaginea: {cale_imagine} ...")
    
    try:
        # O redimensionăm la 200x200 cum a învățat modelul
        img = tf.keras.utils.load_img(cale_imagine, target_size=IMG_SIZE)
        img_array = tf.keras.utils.img_to_array(img)
        
        # O transformăm într-un "batch" de o singură poză (rețeaua așteaptă liste de poze)
        img_array = tf.expand_dims(img_array, 0) 
        
        # 3. Facem predicția
        predictii = model.predict(img_array)
        score = tf.nn.softmax(predictii[0]) # Transformăm în procente

        # 4. Afișăm rezultatul
        clasa_castigatoare = CLASE[np.argmax(score)]
        incredere = 100 * np.max(score)

        print(f"\nRezultat: {clasa_castigatoare}")
        print(f"Siguranță: {incredere:.2f}%")
        
    except Exception as e:
        print(f"Eroare la citirea imaginii: {e}")

if __name__ == "__main__":
    # Poți schimba aici calea către o poză de test de la tine din PC
    # Sau poți rula scriptul dându-i calea ca argument
    if len(sys.argv) > 1:
        cale = sys.argv[1]
    else:
        # PUNE AICI O CALE CĂTRE O POZĂ REALĂ CA SĂ TESTEZI RAPID
        cale = "../../data/test.1.jpg"
        
    prezice_varsta(cale)