import tensorflow as tf
from tensorflow.keras import layers, models
import os

# --- SETĂRI ---
IMG_SIZE = (200, 200)  # Dimensiunea la care am procesat pozele
BATCH_SIZE = 16        # Câte poze învață deodată
EPOCHS = 40            # De câte ori trece prin materia de studiu

# Căile către date (relative la folderul src/neural_network)
BASE_DIR = '../../data'
TRAIN_DIR = os.path.join(BASE_DIR, 'train')
VAL_DIR = os.path.join(BASE_DIR, 'validation')

def main():
    print("1. Citim imaginile din foldere...")
    
    # Încărcăm datele de antrenament
    train_ds = tf.keras.utils.image_dataset_from_directory(
        TRAIN_DIR,
        seed=123,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE
    )

    # Încărcăm datele de validare (testele grilă)
    val_ds = tf.keras.utils.image_dataset_from_directory(
        VAL_DIR,
        seed=123,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE
    )

    class_names = train_ds.class_names
    print(f"Clase găsite: {class_names}")

    # Optimizare pentru viteză
    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

    print("2. Construim Rețeaua Neuronală...")
    
    # Arhitectura CNN (Convolutional Neural Network)
    model = models.Sequential([
        # Standardizăm pixelii (0-255 devine 0-1)
        layers.Rescaling(1./255, input_shape=(IMG_SIZE[0], IMG_SIZE[1], 3)),
        
        # Blocul 1 - Trăsături simple
        layers.Conv2D(16, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        
        # Blocul 2 - Trăsături medii
        layers.Conv2D(32, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        
        # Blocul 3 - Trăsături complexe (fața)
        layers.Conv2D(64, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        
        # Aplatizare (transformăm imaginea în listă de numere)
        layers.Flatten(),
        
        # Stratul de decizie (Dense)
        layers.Dense(128, activation='relu'),
        
        # Stratul final (Output) - Câte clase avem
        layers.Dense(len(class_names))
    ])

    # Compilare (Pregătire)
    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])

    model.summary()

    print("3. START ANTRENARE...")
    
    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=EPOCHS
    )

    print("4. Salvare model...")
    # Salvăm modelul ca să îl folosim mai târziu
    if not os.path.exists('modele_salvate'):
        os.makedirs('modele_salvate')
        
    model.save('modele_salvate/model_varsta.keras')
    print("✔ SUCCES! Modelul a fost salvat în folderul 'src/neural_network/modele_salvate'.")

if __name__ == "__main__":
    main()