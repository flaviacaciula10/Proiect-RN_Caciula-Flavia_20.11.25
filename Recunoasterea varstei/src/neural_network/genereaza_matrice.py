import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
import os

MODEL_PATH = 'modele_salvate/trained_model.h5' 
TEST_DIR = '../../data/test'
IMG_SIZE = (200, 200)

def main():
    if not os.path.exists(MODEL_PATH):
        print(f"EROARE: Nu gasesc modelul la {MODEL_PATH}")
        MODEL_PATH_ALT = 'modele_salvate/model_varsta.keras'
        if os.path.exists(MODEL_PATH_ALT):
            print(f"Am gasit varianta .keras! Folosesc: {MODEL_PATH_ALT}")
            model = tf.keras.models.load_model(MODEL_PATH_ALT)
        else:
            return
    else:
        model = tf.keras.models.load_model(MODEL_PATH)

    print("Citesc datele de test...")
    test_ds = tf.keras.utils.image_dataset_from_directory(
        TEST_DIR,
        image_size=IMG_SIZE,
        batch_size=32,
        shuffle=False
    )

    class_names = test_ds.class_names
    print(f"Clase: {class_names}")
    print("Fac predictii pe tot setul de test...")
    y_true = []
    y_pred = []

    for images, labels in test_ds:
        preds = model.predict(images, verbose=0)
        y_true.extend(labels.numpy())
        y_pred.extend(np.argmax(preds, axis=1))

    cm = confusion_matrix(y_true, y_pred)

    plt.figure(figsize=(12, 10))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=class_names, yticklabels=class_names)
    plt.xlabel('Predictie')
    plt.ylabel('Adevarat')
    plt.title('Matrice de Confuzie - Model Varsta')
    
    plt.savefig('../../docs/confusion_matrix.png')
    print("Matricea a fost salvata in docs/confusion_matrix.png")
    plt.show()

if __name__ == "__main__":
    main()