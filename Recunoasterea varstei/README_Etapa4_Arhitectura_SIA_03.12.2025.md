# 📘 README – Etapa 4: Arhitectura Completă a Aplicației SIA bazată pe Rețele Neuronale

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** Căciulă Flavia-Andreea-Ștefania 
**Link Repository GitHub**
**Data:** 04.12.2025
---

## Scopul Etapei 4s

Această etapă corespunde punctului 5. Dezvoltarea arhitecturii aplicației software bazată pe RN. Obiectivul este livrarea unui SCHELET COMPLET și FUNCȚIONAL al sistemului (SIA), demonstrând fluxul de date de la intrare până la interfața cu utilizatorul.

##  Livrabile Obligatorii

### 1. Tabelul Nevoie Reală → Soluție SIA → Modul Software (max ½ pagină)
Completați in acest readme tabelul următor cu **minimum 2-3 rânduri** care leagă nevoia identificată în Etapa 1-2 cu modulele software pe care le construiți (metrici măsurabile obligatoriu):

| **Nevoie reală concretă** | **Cum o rezolvă SIA-ul vostru** | **Modul software responsabil** |
| Restricționarea accesului minorilor la conținut online (ex: social media, jocuri 18+) | Analiză facială și estimare vârstă → Blocare acces dacă vârsta < 18 ani (latență < 3 sec) | Modul RN + UI Web (Streamlit) |
| Profilarea demografică automată a clienților într-un magazin fizic | Detectare vârstă din flux video → Raportare statistici cu o acuratețe de min. 70% | Modul Preprocesare + RN |
| Adaptarea interfeței educaționale în funcție de vârsta elevului | Clasificare interval vârstă (ex: 5-10 ani) | UI (Logică) + RN |

### 2. Contribuția Voastră Originală la Setul de Date – MINIM 40% din Totalul Observațiilor Finale

**Total observații finale:** 245 imagini (în creștere) Observații originale: 245 (100%)

**Tipul contribuției:**
[X] Date generate prin simulare fizică  
[ ] Date achiziționate cu senzori proprii  
[X] Etichetare/adnotare manuală  
[ ] Date sintetice prin metode avansate  

**Descriere detaliată:**
Deoarece imaginile cu fețele minorilor sunt sensibile (GDPR), am optat pentru generarea unui dataset propriu folosind instrumente de sinteză AI și colectare manuală filtrată. Am generat imagini pentru 16 categorii de vârstă (intervale de 5 ani, de la 0 la 80 de ani). Fiecare imagine a fost trecută printr-un proces de curățare manuală și etichetare în foldere specifice. Ulterior, am aplicat un pipeline de preprocesare (MediaPipe) pentru a extrage doar ROI (Region of Interest - fața) și a elimina fundalul.

**Locația codului:** `src/preprocessing/adaugare_in_fisiere.py`
**Locația datelor:** `data/raw/ (sursa)` și `data/processed/`

**Dovezi:**
- Structura folderelor din `data/processed/` care conține cele 16 clase definite manual.

- Scripturile de preprocesare custom din `src/preprocessing/`.


### 3. Diagrama State Machine a Întregului Sistem (OBLIGATORIE)

**Justificarea State Machine-ului ales:**
Am ales o arhitectură de tip Event-Driven / Triggered Pipeline pentru că aplicația funcționează pe baza interacțiunii directe cu utilizatorul (încărcarea unei imagini). Nu este un proces continuu, ci unul discret.

**Stările principale sunt:**

- `IDLE:` Sistemul așteaptă ca utilizatorul să încarce o imagine prin interfața Web.

- `PREPROCESS:` Odată încărcată, imaginea este preluată de modulul MediaPipe care detectează fața, elimină fundalul și face resize la 200x200px (letterboxing).

- `INFERENCE:` Imaginea procesată intră în Rețeaua Neuronală (CNN), care calculează probabilitățile pentru cele 16 clase.

- `DISPLAY_RESULT:` Se afișează clasa cu probabilitatea maximă și scorul de încredere.

- `ERROR:` Stare critică în care ajungem dacă MediaPipe nu detectează nicio față în imaginea încărcată (ex: poză cu un peisaj).

**Tranzițiile critice:**

- IDLE → PREPROCESS: Trigger la upload.

- PREPROCESS → ERROR: Dacă face_detected == False.

- PREPROCESS → INFERENCE: Doar dacă imaginea este validă.

### 4. Scheletul Complet al celor 3 Module Cerute la Curs (slide 7)

|Modul|Tehnologie|Status Funcțional|
|1. Data acquisition și Processing|Python(MeiaPipe, OpenCV)|Funcțional. Scriptul `adaugare_in_fisiere.py` preia imaginile raw, elimină fundalul și le normalizează.|
|2. Neural Network|TensorFlow / Keras|Funcțional. Modelul CNN este definit în `antrenare.py`, compilat și salvat. Arhitectura suportă input 200x200x3.|
|3. Web Service / UI|Streamlit|Funcțional. Interfața permite upload de fișiere, apelează modelul și afișează predicția.|

#### Detalii per modul:

* **Modul 1:** Data Processing (`src/preprocessing/`)

- Script: `preprocesare.py`
- Rol: Standardizează input-ul. Indiferent de rezoluția pozei originale, modulul garantează ieșire 200x200px cu fața centrată, esențial pentru consistența datelor de intrare în RN.

* **Modul 2:** Neural Network (`src/neural_network/`)

- Script: antrenare.py (definire + antrenare)
- Arhitectură: CNN Secvențial (Conv2D -> MaxPooling -> GlobalAveragePooling -> Dense).
- Model salvat: models/trained_model.h5 (sau .keras).

* **Modul 3:** UI (`src/app/`)

- Script: `interfata.py`
- Framework: Streamlit.
- Flux: User Upload -> Backend Processing -> Display Age & Confidence.

## Structura Repository-ului la Finalul Etapei 4 (OBLIGATORIE)

**Verificare consistență cu Etapa 3:**

```
Recunoasterea varstei/
├── README.md
├── README_Etapa3_Analiza_Date.md
├── README_Etapa4_Arhitectura_SIA.md
│
├── docs/
│   ├── state_machine.png
│   └── screenshots/
│       └── ui_demo.png
│
├── data/                               
│   ├── raw/
│   ├── processed/
│   ├── train/
│   ├── validation/
│   └── test/
│
├── src/
│   ├── preprocessing/
│   │   ├── preprocesare.py
│   │   └── adaugare_in_fisiere.py
│   ├── neural_network/
│   │   ├── antrenare.py               
│   │   └── model.py (opțional)
│   └── app/
│       └── interfata.py
│
├── models/
│   └── trained_model.h5
│
├── split_data.py
└── requirements.txt
```

**Diferențe față de Etapa 3:**
- Adăugat `data/generated/` pentru contribuția dvs originală
- Adăugat `src/data_acquisition/` - MODUL 1
- Adăugat `src/neural_network/` - MODUL 2
- Adăugat `src/app/` - MODUL 3
- Adăugat `models/` pentru model neantrenat
- Adăugat `docs/state_machine.png` - OBLIGATORIU
- Adăugat `docs/screenshots/` pentru demonstrație UI


## Checklist Final – Bifați Totul Înainte de Predare

[x] Tabelul Nevoie → Soluție completat.
[x] Contribuție 100% date originale (Generated/Collected).
[x] Diagrama State Machine definită și justificată.
[x] Modul 1 (Procesare) funcțional.
[x] Modul 2 (RN) definit și salvat.
[x] Modul 3 (UI) funcțional (Streamlit).
[x] Structură repository organizată corect.

**Predarea se face prin commit pe GitHub cu mesajul:**  
`"Etapa 4 completă - Arhitectură SIA funcțională"`

**Tag obligatoriu:**  
`git tag -a v0.4-architecture -m "Etapa 4 - Skeleton complet SIA"`


