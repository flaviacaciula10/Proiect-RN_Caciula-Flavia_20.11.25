import tensorflow as tf
import os

# Setări
IMG_SIZE = (200, 200)
BATCH_SIZE = 32
TEST_DIR = '../../data/test'
MODEL_PATH = 'modele_salvate/model_varsta.keras'

def main():
    # 1. Verificăm dacă există modelul
    if not os.path.exists(MODEL_PATH):
        print("EROARE: Nu găsesc fișierul model_varsta.keras! Ai rulat antrenarea?")
        return

    # 2. Încărcăm modelul antrenat
    print("Încărcăm modelul...")
    model = tf.keras.models.load_model(MODEL_PATH)

    # 3. Încărcăm datele de test
    print("Citim datele de test...")
    test_ds = tf.keras.utils.image_dataset_from_directory(
        TEST_DIR,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        shuffle=False # Nu le amestecăm, ca să putem verifica ordinea dacă e nevoie
    )

    # 4. Evaluăm
    print("\n--- REZULTATE EVALUARE ---")
    loss, accuracy = model.evaluate(test_ds)
    
    print(f"\nAcuratețe (Precizie): {accuracy * 100:.2f}%")
    print(f"Pierdere (Loss): {loss:.4f}")

    if accuracy > 0.60:
        print("✔ Rezultat DECENT pentru un prim proiect!")
    elif accuracy > 0.80:
        print("✔✔ Rezultat FOARTE BUN!")
    else:
        print("⚠ Rezultat SLAB. Mai este nevoie de date.")

if __name__ == "__main__":
    main()