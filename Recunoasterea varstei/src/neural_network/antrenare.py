import tensorflow as tf
from tensorflow.keras import layers, models
import os

IMG_SIZE = (200, 200)
BATCH_SIZE = 16
EPOCHS = 40
BASE_DIR = '../../data'
TRAIN_DIR = os.path.join(BASE_DIR, 'train')
VAL_DIR = os.path.join(BASE_DIR, 'validation')

def main():
    print("Citim imaginile din foldere...")

    train_ds = tf.keras.utils.image_dataset_from_directory(
        TRAIN_DIR,
        seed=123,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE
    )

    val_ds = tf.keras.utils.image_dataset_from_directory(
        VAL_DIR,
        seed=123,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE
    )

    class_names = train_ds.class_names
    print(f"Clase găsite: {class_names}")

    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

    print("Construim Reteaua Neuronala...")

    model = models.Sequential([
        layers.Rescaling(1./255, input_shape=(IMG_SIZE[0], IMG_SIZE[1], 3)),

        layers.Conv2D(16, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),

        layers.Conv2D(32, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),

        layers.Conv2D(64, 3, padding='same', activation='relu'),

        layers.GlobalAveragePooling2D(),

        layers.Dense(128, activation='relu'),

        layers.Dense(len(class_names))
    ])

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])

    model.summary()

    print("START ANTRENARE...")
    
    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=EPOCHS
    )

    print("Salvare model...")
    if not os.path.exists('modele_salvate'):
        os.makedirs('modele_salvate')
        
    model.save('modele_salvate/model_varsta.keras')
    print("SUCCES! Modelul a fost salvat in folderul 'src/neural_network/modele_salvate'.")

if __name__ == "__main__":
    main()
