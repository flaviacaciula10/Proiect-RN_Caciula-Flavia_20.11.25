import cv2
import numpy as np
import mediapipe as mp

# Inițializare MediaPipe Selfie Segmentation
# Model 1 = landscape (mai rapid), 0 = general
mp_selfie_segmentation = mp.solutions.selfie_segmentation
segmenter = mp_selfie_segmentation.SelfieSegmentation(model_selection=0)

def preprocesare_varsta(path_imagine, afiseaza=False, target_size=(200, 200)):
    """
    Procesează imaginea pentru detecția vârstei:
    1. Elimină fundalul (MediaPipe)
    2. Decupează doar fața/capul cu padding
    3. Redimensionează cu 'letterboxing' (benzi negre) pentru a nu deforma fața.
    """
    # 1. Încărcare imagine
    img = cv2.imread(path_imagine)
    if img is None:
        print(f"Eroare: Nu pot citi {path_imagine}")
        return None

    h, w = img.shape[:2]

    # 2. MediaPipe funcționează cu RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = segmenter.process(img_rgb)
    mask = results.segmentation_mask

    # 3. Aplicăm masca (prag de 0.5)
    # Tot ce e > 0.5 este persoană, restul e fundal
    condition = np.stack((mask,) * 3, axis=-1) > 0.5
    
    # Fundal negru
    bg_image = np.zeros(img.shape, dtype=np.uint8)
    # Putem pune gri dacă preferi: bg_image[:] = (128, 128, 128)
    
    img_no_bg = np.where(condition, img, bg_image)

    # 4. Decupare inteligentă (Crop)
    # Găsim coordonatele pixelilor care NU sunt negri
    points = cv2.findNonZero((mask > 0.1).astype(np.uint8))
    
    if points is not None:
        x, y, w_box, h_box = cv2.boundingRect(points)
        
        # Adăugăm un pic de margine (padding) ca să nu tăiem urechile/bărbia
        pad = int(max(w_box, h_box) * 0.15) # 15% padding
        
        x1 = max(0, x - pad)
        y1 = max(0, y - pad)
        x2 = min(w, x + w_box + pad)
        y2 = min(h, y + h_box + pad)
        
        img_cropped = img_no_bg[y1:y2, x1:x2]
    else:
        img_cropped = img_no_bg # Fallback dacă nu găsește nimic

    # 5. Resize cu păstrarea proporțiilor (Letterbox)
    # Vrem să ajungem la target_size (ex: 200x200) fără să "turtim" poza
    final_img = resize_and_pad(img_cropped, target_size)

    if afiseaza:
        cv2.imshow("Final", final_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return final_img

def resize_and_pad(img, target_size):
    """Redimensionează imaginea păstrând aspect ratio și adaugă benzi negre."""
    h, w = img.shape[:2]
    target_w, target_h = target_size

    scale = min(target_w / w, target_h / h)
    new_w, new_h = int(w * scale), int(h * scale)

    resized = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)
    
    # Creăm canvas negru
    canvas = np.zeros((target_h, target_w, 3), dtype=np.uint8)
    
    # Centrăm
    x_offset = (target_w - new_w) // 2
    y_offset = (target_h - new_h) // 2
    
    canvas[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = resized
    return canvas