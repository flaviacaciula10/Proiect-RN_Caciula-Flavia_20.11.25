import cv2
import numpy as np
import mediapipe as mp

mp_selfie_segmentation = mp.solutions.selfie_segmentation
segmenter = mp_selfie_segmentation.SelfieSegmentation(model_selection=0)

def preprocesare_varsta(path_imagine, afiseaza=False, target_size=(200, 200)):
    img = cv2.imread(path_imagine)
    if img is None:
        print(f"Eroare: Nu pot citi {path_imagine}")
        return None

    h, w = img.shape[:2]

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = segmenter.process(img_rgb)
    mask = results.segmentation_mask

    condition = np.stack((mask,) * 3, axis=-1) > 0.5
    bg_image = np.zeros(img.shape, dtype=np.uint8)
    img_no_bg = np.where(condition, img, bg_image)

    gray = cv2.cvtColor(img_no_bg, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    points = None
    for cnt in contours:
        if cv2.contourArea(cnt) > 500:
            if points is None:
                points = cnt
            else:
                points = np.concatenate((points, cnt))
    
    if points is not None:
        x, y, w_box, h_box = cv2.boundingRect(points)
        
        pad = int(max(w_box, h_box) * 0.15)
        
        x1 = max(0, x - pad)
        y1 = max(0, y - pad)
        x2 = min(w, x + w_box + pad)
        y2 = min(h, y + h_box + pad)
        
        img_cropped = img_no_bg[y1:y2, x1:x2]
    else:
        img_cropped = img_no_bg

    final_img = resize_and_pad(img_cropped, target_size)

    if afiseaza:
        cv2.imshow("Final", final_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return final_img

def resize_and_pad(img, target_size):
    h, w = img.shape[:2]
    target_w, target_h = target_size

    scale = min(target_w/w, target_h/h)
    nw, nh = int(w * scale), int(h * scale)

    img_resized = cv2.resize(img, (nw, nh))

    top = (target_h - nh) // 2
    bottom = target_h - nh - top
    left = (target_w - nw) // 2
    right = target_w - nw - left

    img_padded = cv2.copyMakeBorder(img_resized, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0, 0, 0])
    return img_padded
