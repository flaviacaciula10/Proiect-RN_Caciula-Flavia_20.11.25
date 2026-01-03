import os
import shutil
import random

# Căile tale (bazate pe structura trimisă)
SOURCE_DIR = "data/processed"
ROOT_DIR = "data"
CLASSES = [
    "0-5 ani", 
    "5-10 ani", 
    "10-15 ani", 
    "15-20 ani", 
    "20-25 ani", 
    "25-30 ani", 
    "30-35 ani", 
    "35-40 ani", 
    "40-45 ani", 
    "45-50 ani", 
    "50-55 ani", 
    "55-60 ani", 
    "60-65 ani", 
    "65-70 ani", 
    "70-75 ani", 
    "75-80 ani"
]

def create_split():
    # Procente
    TRAIN_RATIO = 0.7
    VAL_RATIO = 0.15
    # Restul de 0.15 rămâne pentru TEST

    for class_name in CLASSES:
        # Calea către folderul cu poze procesate (ex: data/processed/0-5 ani)
        src_path = os.path.join(SOURCE_DIR, class_name)
        
        # Verificăm dacă există folderul
        if not os.path.exists(src_path):
            print(f"Nu am găsit folderul: {src_path}")
            continue

        # Luăm toate pozele
        images = os.listdir(src_path)
        # Le amestecăm aleatoriu
        random.shuffle(images)

        # Calculăm câte punem în fiecare parte
        train_count = int(len(images) * TRAIN_RATIO)
        val_count = int(len(images) * VAL_RATIO)
        
        # Împărțim lista de poze
        train_imgs = images[:train_count]
        val_imgs = images[train_count:train_count + val_count]
        test_imgs = images[train_count + val_count:]

        # Funcție ajutătoare pentru copiere
        def copy_images(image_list, folder_type):
            dest_path = os.path.join(ROOT_DIR, folder_type, class_name)
            os.makedirs(dest_path, exist_ok=True) # Creăm folderul dacă nu există
            
            for img in image_list:
                shutil.copy(os.path.join(src_path, img), os.path.join(dest_path, img))
            print(f"Copiat {len(image_list)} imagini în {folder_type}/{class_name}")

        # Copiem fizic fișierele
        copy_images(train_imgs, "train")
        copy_images(val_imgs, "validation")
        copy_images(test_imgs, "test")

if __name__ == "__main__":
    create_split()