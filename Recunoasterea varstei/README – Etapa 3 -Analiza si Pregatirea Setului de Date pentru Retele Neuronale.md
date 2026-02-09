# 📘 README – Etapa 3: Analiza și Pregătirea Setului de Date pentru Rețele Neuronale

**Instituție:** POLITEHNICA București – FIIR
**Student:** Căciulă Flavia-Andreea-Ștefania
**Proiect:** Sistem de Detectare a Vârstei pe baza Trăsăturilor Faciale
**Data:** 20 noiembrie 2025

---

## Introducere

Acest document descrie activitățile realizate în Etapa 3, concentrându-se pe colectarea, curățarea și structurarea setului de date de imagini faciale. Scopul este transformarea imaginilor brute (raw) într-un format standardizat (200x200px, centrat pe față) compatibil cu intrarea rețelei neuronale convoluționale (CNN).

##  1. Structura Repository-ului Github (versiunea Etapei 3)

Recunoasterea varstei/
├── README.md
├── README_Etapa3_Analiza_Date.md  <-- Acest fișier
├── data/
│   ├── raw/               # Imagini brute, organizate pe foldere (0-5 ani, etc.)
│   ├── processed/         # Imagini decupate (face crop) și redimensionate
│   ├── train/             # 70% din date (pentru antrenare)
│   ├── validation/        # 15% din date (pentru tuning hiperparametri)
│   └── test/              # 15% din date (pentru evaluarea finală)
├── src/
│   ├── preprocessing/     
│   │   ├── preprocesare.py            # Logică MediaPipe (crop + resize)
│   │   └── adaugare_in_fisiere.py     # Script iterare foldere
│   └── neural_network/    # (În lucru pentru Etapa 4)
├── split_data.py          # Script pentru împărțirea train/val/test
└── requirements.txt       # Dependențe (opencv, mediapipe, numpy)

##  2. Descrierea Setului de Date

### 2.1 Sursa datelor

* **Origine:** Imagini generate sintetic folosind instrumente AI generative pentru a asigura diversitatea trăsăturilor și a evita problemele de confidențialitate (GDPR) ale persoanelor reale.
* **Modul de achiziție:** Generare programatică și organizare manuală în categorii de vârstă.
* **Perioada colectării:** Sesiunea curentă de proiect.

### 2.2 Caracteristicile dataset-ului

* **Număr total de observații:** 245 imagini.
* **Număr de caracteristici (features):** 16 clase de vârstă (intervale de 5 ani: 0-5, 5-10 ... 75-80 ani).
* **Tipuri de date:** ☐ Numerice / ☐ Categoriale / ☐ Temporale / X Imagini
* **Format fișiere:** ☐ CSV / ☐ TXT / ☐ JSON / X PNG_JPG/ ☐ Altele: [...]

### 2.3 Descrierea fiecărei caracteristici

| **Caracteristică** | **Tip** | **Unitate** | **Descriere** | **Domeniu valori** |
| Imagine (input) | Matrice 3D | Variabilă (Raw) -> 200x200x3 (Processed) | Imaginea facială propriu-zisă |
| Etichetă | Categorial | 1 din 16 clase | Intervalul de vârstă asociat folderului |

**Fișier recomandat:**  `data/README.md`

---

##  3. Analiza Exploratorie a Datelor (EDA) – Sintetic

### 3.1 Statistici descriptive aplicate

* **Distribuția claselor:** Setul de date conține aproximativ 15-20 imagini per categorie de vârstă (distribuție relativ uniformă, dar redusă cantitativ).

* **Variabilitate:** Imaginile acoperă diverse etnii, condiții de iluminare și expresii faciale.

### 3.2 Analiza calității datelor

* **Zgomot de fond:** Imaginile brute conțin fundaluri diverse care nu sunt relevante pentru detecția vârstei.

* **Geometrie:** Fețele se află la distanțe și unghiuri diferite în imaginile originale.

### 3.3 Probleme identificate

* **Problemă:** Dimensiunea redusă a setului de date poate duce la overfitting.

* **Soluție propusă:** Utilizarea unei arhitecturi CNN optimizate (GlobalAveragePooling) și, opțional, gruparea claselor în categorii mai largi (Copii/Tineri/Adulți) în etapele următoare.

##  4. Preprocesarea Datelor

### 4.1 Curățarea datelor

* **Tehnologie:** Google MediaPipe Selfie Segmentation.

* **Proces:** Se generează o mască de segmentare; tot ce nu este "persoană" este înlocuit cu negru (0,0,0). Aceasta ajută rețeaua să se concentreze strict pe trăsăturile faciale

### 4.2 Transformarea caracteristicilor

* **Decupare:** Algoritmul calculează Bounding Box-ul feței și adaugă o margine (padding) de 15% pentru a nu tăia elemente esențiale (bărbie, frunte).

* **Letterboxing:** Pentru a aduce imaginile la dimensiunea țintă de 200x200 px fără a le deforma, se păstrează aspect ratio-ul original și se completează spațiul rămas cu benzi negre.

### 4.3 Structurarea seturilor de date

**Împărțire recomandată:**
* 70% – train - 171 imagini
* 15% – validation - 37 imagini
* 15% – test - 37 imagini

**Principii respectate:**
* Stratificare pentru clasificare
* Fără scurgere de informație (data leakage)
* Statistici calculate DOAR pe train și aplicate pe celelalte seturi

### 4.4 Salvarea rezultatelor preprocesării

* Date preprocesate în `data/processed/`
* Seturi train/val/test în foldere dedicate

##  5. Fișiere Generate în Această Etapă

* `data/raw/` – date brute
* `data/processed/` – date curățate & transformate
* `data/train/`, `data/validation/`, `data/test/` – seturi finale
* `src/preprocessing/` – codul de preprocesare
* `data/README.md` – descrierea dataset-ului

##  6. Stare Etapă (de completat de student)

- [X] Structură repository configurată
- [X] Dataset analizat (EDA realizată)
- [X] Date preprocesate
- [X] Seturi train/val/test generate
- [X] Documentație actualizată în README + `data/README.md`
