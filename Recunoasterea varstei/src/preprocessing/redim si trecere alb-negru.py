import cv2
import os
import config.config as cfg

def preprocess_image(input_image_path, output_category_dir):
    """
    Încarcă o imagine, o redimensionează la TARGET_SIZE și o convertește la scală de gri.
    Salvează imaginea procesată în directorul specificat.
    """
    # 1. Citirea imaginii
    image = cv2.imread(input_image_path) 
    
    if image is None:
        print(f"Eroare: Nu s-a putut citi imaginea {input_image_path}")
        return False

    # 2. Redimensionarea imaginii (la 150x150)
    # Folosim cv2.INTER_AREA, optim pentru micșorare
    resized_image = cv2.resize(image, cfg.TARGET_SIZE, interpolation=cv2.INTER_AREA)
    
    # 3. Convertirea la scală de gri (dacă este activată în config.py)
    if cfg.GRAYSCALE_ENABLED:
        # BGR2GRAY convertește imaginea color în scală de gri (un singur canal)
        final_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    else:
        final_image = resized_image
        
    # 4. Construirea căii de ieșire
    file_name = os.path.basename(input_image_path)
    base_name, _ = os.path.splitext(file_name)
    # Salvăm ca .png pentru a păstra calitatea
    output_path = os.path.join(output_category_dir, f"{base_name}_proc.png")
    
    # 5. Salvarea imaginii procesate
    cv2.imwrite(output_path, final_image)
    return True

# --- Funcția Principală de Rulare ---
def run_preprocessing():
    """
    Parcurge toate directoarele din INPUT_DIR și aplică preprocesarea.
    """
    input_root_dir = cfg.INPUT_DIR
    output_root_dir = cfg.OUTPUT_DIR
    
    if not os.path.exists(output_root_dir):
        os.makedirs(output_root_dir)
        
    print(f"Începe preprocesarea de bază: Redimensionare la {cfg.TARGET_SIZE} și Grayscale={cfg.GRAYSCALE_ENABLED}")

    # Parcurgerea structurii de foldere (categoriile de vârstă)
    for root, dirs, files in os.walk(input_root_dir):
        if root == input_root_dir:
            continue
            
        category_name = os.path.basename(root)
        output_category_dir = os.path.join(output_root_dir, category_name)
        
        if not os.path.exists(output_category_dir):
            os.makedirs(output_category_dir)
            
        print(f"\nProcesează categoria: {category_name}")
        
        for file_name in files:
            input_path = os.path.join(root, file_name)
            if preprocess_image(input_path, output_category_dir):
                print(f"  Procesat: {file_name}")

if __name__ == '__main__':
    run_preprocessing()