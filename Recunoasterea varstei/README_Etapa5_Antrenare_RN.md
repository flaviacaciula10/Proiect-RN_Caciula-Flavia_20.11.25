# 📘 README – Etapa 5: Configurarea și Antrenarea Modelului RN

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** Căciulă Flavia-Andreea-Ștefania 
**Link Repository GitHub:** https://github.com/flaviacaciula10/Proiect-RN_Caciula-Flavia_20.11.25.git 
**Data predării:** 11.12.2025

---

## Scopul Etapei 5

Această etapă corespunde punctului **6. Configurarea și antrenarea modelului RN** din lista de 9 etape - slide 2 **RN Specificatii proiect.pdf**.

**Obiectiv principal:** Antrenarea efectivă a modelului RN definit în Etapa 4, evaluarea performanței și integrarea în aplicația completă.

**Pornire obligatorie:** Arhitectura completă și funcțională din Etapa 4:
- State Machine definit și justificat
- Cele 3 module funcționale (Data Logging, RN, UI)
- Minimum 40% date originale în dataset

---

## PREREQUISITE – Verificare Etapa 4 (OBLIGATORIU)

**Înainte de a începe Etapa 5, verificați că aveți din Etapa 4:**

- [ ] **State Machine** definit și documentat în `docs/state_machine.*`
- [ ] **Contribuție ≥40% date originale** în `data/generated/` (verificabil)
- [ ] **Modul 1 (Data Logging)** funcțional - produce CSV-uri
- [ ] **Modul 2 (RN)** cu arhitectură definită dar NEANTRENATĂ (`models/untrained_model.h5`)
- [ ] **Modul 3 (UI/Web Service)** funcțional cu model dummy
- [ ] **Tabelul "Nevoie → Soluție → Modul"** complet în README Etapa 4

** Dacă oricare din punctele de mai sus lipsește → reveniți la Etapa 4 înainte de a continua.**

---

## Pregătire Date pentru Antrenare 

### Dacă ați adăugat date noi în Etapa 4 (contribuția de 40%):

**TREBUIE să refaceți preprocesarea pe dataset-ul COMBINAT:**

Exemplu:
```bash
# 1. Combinare date vechi (Etapa 3) + noi (Etapa 4)
python src/preprocessing/combine_datasets.py

# 2. Refacere preprocesare COMPLETĂ
python src/preprocessing/data_cleaner.py
python src/preprocessing/feature_engineering.py
python src/preprocessing/data_splitter.py --stratify --random_state 42

# Verificare finală:
# data/train/ → trebuie să conțină date vechi + noi
# data/validation/ → trebuie să conțină date vechi + noi
# data/test/ → trebuie să conțină date vechi + noi
```

** ATENȚIE - Folosiți ACEIAȘI parametri de preprocesare:**
- Același `scaler` salvat în `config/preprocessing_params.pkl`
- Aceiași proporții split: 70% train / 15% validation / 15% test
- Același `random_state=42` pentru reproducibilitate

**Verificare rapidă:**
```python
import pandas as pd
train = pd.read_csv('data/train/X_train.csv')
print(f"Train samples: {len(train)}")  # Trebuie să includă date noi
```

---

##  Cerințe Structurate pe 3 Niveluri

### Nivel 1 – Obligatoriu pentru Toți (70% din punctaj)

Completați **TOATE** punctele următoare:

1. **Antrenare model** definit în Etapa 4 pe setul final de date (≥40% originale)
2. **Minimum 10 epoci**, batch size 8–32
3. **Împărțire stratificată** train/validation/test: 70% / 15% / 15%
4. **Tabel justificare hiperparametri** (vezi secțiunea de mai jos - OBLIGATORIU)
5. **Metrici calculate pe test set:**
   - **Acuratețe ≥ 65%**
   - **F1-score (macro) ≥ 0.60**
6. **Salvare model antrenat** în `models/trained_model.h5` (Keras/TensorFlow) sau `.pt` (PyTorch) sau `.lvmodel` (LabVIEW)
7. **Integrare în UI din Etapa 4:**
   - UI trebuie să încarce modelul ANTRENAT (nu dummy)
   - Inferență REALĂ demonstrată
   - Screenshot în `docs/screenshots/inference_real.png`

#### Tabel Hiperparametri și Justificări (OBLIGATORIU - Nivel 1)

Completați tabelul cu hiperparametrii folosiți și **justificați fiecare alegere**:

| **Hiperparametru** | **Valoare Aleasă** | **Justificare** |
|--------------------|-------------------|-----------------|
|Learning rate | 0.001 | Valoare standard pentru optimizatorul Adam oferă un echilibru bun între viteza de învățare și stabilitate pe un dataset mic|
|Batch size | 16 | Am redus de la standardul 32 la 16 pentru a avea mai multe actualizări de greutăți per epocă, având puține date|
Number of epochs | 40 | Configurat cu Early Stopping (patience=5) pentru a opri antrenarea automat dacă loss-ul pe validare nu mai scade (evitare overfitting)|
|Optimizer | Adam | Cel mai eficient pentru CNN-uri standard; ajustează automat rata de învățare pentru fiecare parametru|
|Loss function | Sparse Categorical Crossentropy | Funcția corectă pentru clasificare multi-class cu 16 clase|
|Activation functions | ReLU (hidden), Softmax (output) | ReLU în straturile Convoluționale (evită vanishing gradient), Softmax la final pentru a obține probabilitățile celor 16 intervale de vârstă|

**Justificare detaliată batch size:**
Am ales un batch_size=16 (mai mic decât standardul de 32 sau 64) din cauza dimensiunii setului nostru de date:

Avem un total de 245 imagini, din care aprox. 170 sunt pentru antrenare (70%).
Calculul iterațiilor: 170 imagini / 16 batch ≈ 11 pași per epocă.

Dacă aș fi folosit batch_size=32, aș fi avut doar 5 pași per epocă, ceea ce este insuficient pentru ca rețeaua să își ajusteze greșelile de pe parcursul antrenării. 
Valoarea 16 este potrivită: oferă suficiente actualizări ale gradientului pentru a învăța trăsături, fără a introduce zgomot excesiv și fără a depăși memoria GPU/CPU.

**Resurse învățare rapidă:**
- Împărțire date: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html (video 3 min: https://youtu.be/1NjLMWSGosI?si=KL8Qv2SJ1d_mFZfr)  
- Antrenare simplă Keras: https://keras.io/examples/vision/mnist_convnet/ (secțiunea „Training”)  
- Antrenare simplă PyTorch: https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html#training-an-image-classifier (video 2 min: https://youtu.be/ORMx45xqWkA?si=FXyQEhh0DU8VnuVJ)  
- F1-score: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html (video 4 min: https://youtu.be/ZQlEcyNV6wc?si=VMCl8aGfhCfp5Egi)


---

### Nivel 2 – Recomandat (85-90% din punctaj)

Includeți **TOATE** cerințele Nivel 1 + următoarele:

1. **Early Stopping** - oprirea antrenării dacă `val_loss` nu scade în 5 epoci consecutive
2. **Learning Rate Scheduler** - `ReduceLROnPlateau` sau `StepLR`
3. **Augmentări relevante domeniu:**
   - Vibrații motor: zgomot gaussian calibrat, jitter temporal
   - Imagini industriale: slight perspective, lighting variation (nu rotații simple!)
   - Serii temporale: time warping, magnitude warping
4. **Grafic loss și val_loss** în funcție de epoci salvat în `docs/loss_curve.png`
5. **Analiză erori context industrial** (vezi secțiunea dedicată mai jos - OBLIGATORIU Nivel 2)

**Indicatori țintă Nivel 2:**
- **Acuratețe ≥ 75%**
- **F1-score (macro) ≥ 0.70**

**Resurse învățare (aplicații industriale):**
- Albumentations: https://albumentations.ai/docs/examples/   
- Early Stopping + ReduceLROnPlateau în Keras: https://keras.io/api/callbacks/   
- Scheduler în PyTorch: https://pytorch.org/docs/stable/optim.html#how-to-adjust-learning-rate 

---

### Nivel 3 – Bonus (până la 100%)

**Punctaj bonus per activitate:**

| **Activitate** |  **Livrabil** |
|----------------|--------------|
| Comparare 2+ arhitecturi diferite | Tabel comparativ + justificare alegere finală în README |
| Export ONNX/TFLite + benchmark latență | Fișier `models/final_model.onnx` + demonstrație <50ms |
| Confusion Matrix + analiză 5 exemple greșite | `docs/confusion_matrix.png` + analiză în README |

**Resurse bonus:**
- Export ONNX din PyTorch: [PyTorch ONNX Tutorial](https://pytorch.org/tutorials/beginner/onnx/export_simple_model_to_onnx_tutorial.html)
- TensorFlow Lite converter: [TFLite Conversion Guide](https://www.tensorflow.org/lite/convert)
- Confusion Matrix analiză: [Scikit-learn Confusion Matrix](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html)

---

## Verificare Consistență cu State Machine (Etapa 4)

Antrenarea și inferența trebuie să respecte fluxul din State Machine-ul vostru definit în Etapa 4.

**Exemplu pentru monitorizare vibrații lagăr:**

| **Stare din Etapa 4** | **Implementare în Etapa 5** |
|-----------------------|-----------------------------|
| `ACQUIRE_DATA` | Citire batch date din `data/train/` pentru antrenare |
| `PREPROCESS` | Aplicare scaler salvat din `config/preprocessing_params.pkl` |
| `RN_INFERENCE` | Forward pass cu model ANTRENAT (nu weights random) |
| `THRESHOLD_CHECK` | Clasificare Normal/Uzură pe baza output RN antrenat |
| `ALERT` | Trigger în UI bazat pe predicție modelului real |

**În `src/app/main.py` (UI actualizat):**

Verificați că **TOATE stările** din State Machine sunt implementate cu modelul antrenat:

```python
# ÎNAINTE (Etapa 4 - model dummy):
model = keras.models.load_model('models/untrained_model.h5')  # weights random
prediction = model.predict(input_scaled)  # output aproape aleator

# ACUM (Etapa 5 - model antrenat):
model = keras.models.load_model('models/trained_model.h5')  # weights antrenate
prediction = model.predict(input_scaled)  # predicție REALĂ și corectă
```

---

## Analiză Erori în Context Industrial (OBLIGATORIU Nivel 2)

**Nu e suficient să raportați doar acuratețea globală.** Analizați performanța în contextul aplicației voastre industriale:

### 1. Pe ce clase greșește cel mai mult modelul?

Confusion Matrix arată o concentrare a erorilor în zona claselor de mijloc ("Adulți 30-50 ani"), unde modelul confundă frecvent intervalele adiacente (ex: predicție 30-35 ani vs real 35-40 ani).

Cauze posibile:
1.  **Similaritate Vizuală:** Diferențele biologice între un om de 32 de ani și unul de 37 sunt minime și greu de captat la rezoluția de 200x200px.
2.  **Subjectivitate:** Chiar și etichetarea umană în dataset-ul sintetic poate fi ambiguă în aceste intervale (fără riduri evidente).
În schimb, distincția critică Copil (0-10) vs Adult (20+) este robustă.

### 2. Ce caracteristici ale datelor cauzează erori?

Modelul are performanță slabă în următoarele condiții de iluminare și poziționare:

1.  **Supraexpunere (Lumină puternică):** "Șterge" ridurile și detaliile fine ale pielii, făcând persoanele în vârstă (Seniori) să fie clasificate greșit ca Adulți sau Tineri.
2.  **Ocluzii parțiale:** Ochelarii de vedere mari sau bărbile lungi ascund trăsături cheie (conturul feței, zona ochilor), ducând la confuzii majore.
3.  **Unghiuri extreme:** Deși MediaPipe detectează fața din profil, rețeaua neuronală a fost antrenată preponderent pe fețe frontale, deci eșuează la extragerea features-urilor din profil.

### 3. Ce implicații are pentru aplicația industrială?

În contextul unui sistem de **Restricționare Acces Minori (18+)**:

**FALSE POSITIVES (Minor clasificat ca Adult):**
- **CRITIC.** Un copil primește acces la conținut interzis. Risc legal și de siguranță major.
- **Prioritate 0:** Trebuie eliminat complet.

**FALSE NEGATIVES (Adult clasificat ca Minor):**
- **ACCEPTABIL.** Un adult este blocat eronat.
- **Consecință:** Utilizatorul este redirecționat către o verificare manuală (ex: upload buletin). Este doar un disconfort, nu un risc de securitate.

**Soluție Industrială:** Vom ajusta pragul de decizie. Dacă modelul prezice "18-25 ani" cu o confidență sub 80%, sistemul va clasifica preventiv utilizatorul ca "Incert/Minor" și va cere verificare suplimentară. Preferăm să blocăm 10 adulți decât să lăsăm un copil să treacă.

### 4. Ce măsuri corective propuneți?
Măsuri corective concrete:

1.  **Implementare "Ordinal Regression Loss":** Înlocuirea funcției de pierdere standard cu una care penalizează erorile în funcție de distanță (e.g., să confunzi 20 cu 25 e ok, dar 20 cu 70 e grav).
2.  **Validare Calitate Input:** Integrarea unui modul software înainte de inferență care respinge pozele întunecate, neclare sau din profil, cerând utilizatorului să facă o poză mai bună.
3.  **Extindere Dataset cu "Hard Samples":** Colectarea specifică de imagini cu "cazuri limită" (copii care par maturi, adulți cu trăsături juvenile) pentru a antrena rețeaua pe zonele de graniță (16-20 ani).

## Structura Repository-ului la Finalul Etapei 5

**Clarificare organizare:** Vom folosi **README-uri separate** pentru fiecare etapă în folderul `docs/`:

```
proiect-rn-[prenume-nume]/
├── README.md                           # Overview general proiect (actualizat)
├── etapa3_analiza_date.md         # Din Etapa 3
├── etapa4_arhitectura_sia.md      # Din Etapa 4
├── etapa5_antrenare_model.md      # ← ACEST FIȘIER (completat)
│
├── docs/
│   ├── state_machine.png              # Din Etapa 4
│   ├── loss_curve.png                 # NOU - Grafic antrenare
│   ├── confusion_matrix.png           # (opțional - Nivel 3)
│   └── screenshots/
│       ├── inference_real.png         # NOU - OBLIGATORIU
│       └── ui_demo.png                # Din Etapa 4
│
├── data/                               # Din Etapa 3-4 (NESCHIMBAT)
│   ├── raw/
│   ├── generated/                     # Contribuția voastră 40%
│   ├── processed/
│   ├── train/
│   ├── validation/
│   └── test/
│
├── src/
│   ├── data_acquisition/              # Din Etapa 4
│   ├── preprocessing/                 # Din Etapa 3
│   │   └── combine_datasets.py        # NOU (dacă ați adăugat date în Etapa 4)
│   ├── neural_network/
│   │   ├── model.py                   # Din Etapa 4
│   │   ├── train.py                   # NOU - Script antrenare
│   │   └── evaluate.py                # NOU - Script evaluare
│   └── app/
│       └── main.py                    # ACTUALIZAT - încarcă model antrenat
│
├── models/
│   ├── untrained_model.h5             # Din Etapa 4
│   ├── trained_model.h5               # NOU - OBLIGATORIU
│   └── final_model.onnx               # (opțional - Nivel 3 bonus)
│
├── results/                            # NOU - Folder rezultate antrenare
│   ├── training_history.csv           # OBLIGATORIU - toate epoch-urile
│   ├── test_metrics.json              # Metrici finale pe test set
│   └── hyperparameters.yaml           # Hiperparametri folosiți
│
├── config/
│   └── preprocessing_params.pkl       # Din Etapa 3 (NESCHIMBAT)
│
├── requirements.txt                    # Actualizat
└── .gitignore
```

**Diferențe față de Etapa 4:**
- Adăugat `docs/etapa5_antrenare_model.md` (acest fișier)
- Adăugat `docs/loss_curve.png` (Nivel 2)
- Adăugat `models/trained_model.h5` - OBLIGATORIU
- Adăugat `results/` cu history și metrici
- Adăugat `src/neural_network/train.py` și `evaluate.py`
- Actualizat `src/app/main.py` să încarce model antrenat

---

## Instrucțiuni de Rulare (Actualizate față de Etapa 4)

### 1. Setup mediu (dacă nu ați făcut deja)

```bash
pip install -r requirements.txt
```

### 2. Pregătire date (DACĂ ați adăugat date noi în Etapa 4)

```bash
# Combinare + reprocesare dataset complet
python src/preprocessing/combine_datasets.py
python src/preprocessing/data_cleaner.py
python src/preprocessing/feature_engineering.py
python src/preprocessing/data_splitter.py --stratify --random_state 42
```

### 3. Antrenare model

```bash
python src/neural_network/train.py --epochs 50 --batch_size 32 --early_stopping

# Output așteptat:
# Epoch 1/50 - loss: 0.8234 - accuracy: 0.6521 - val_loss: 0.7891 - val_accuracy: 0.6823
# ...
# Epoch 23/50 - loss: 0.3456 - accuracy: 0.8234 - val_loss: 0.4123 - val_accuracy: 0.7956
# Early stopping triggered at epoch 23
# ✓ Model saved to models/trained_model.h5
```

### 4. Evaluare pe test set

```bash
python src/neural_network/evaluate.py --model models/trained_model.h5

# Output așteptat:
# Test Accuracy: 0.7823
# Test F1-score (macro): 0.7456
# ✓ Metrics saved to results/test_metrics.json
# ✓ Confusion matrix saved to docs/confusion_matrix.png
```

### 5. Lansare UI cu model antrenat

```bash
streamlit run src/app/main.py

# SAU pentru LabVIEW:
# Deschideți WebVI și rulați main.vi
```

**Testare în UI:**
1. Introduceți date de test (manual sau upload fișier)
2. Verificați că predicția este DIFERITĂ de Etapa 4 (când era random)
3. Verificați că confidence scores au sens (ex: 85% pentru clasa corectă)
4. Faceți screenshot → salvați în `docs/screenshots/inference_real.png`

---

## Checklist Final – Bifați Totul Înainte de Predare

### Prerequisite Etapa 4 (verificare)
- [ ] State Machine există și e documentat în `docs/state_machine.*`
- [ ] Contribuție ≥40% date originale verificabilă în `data/generated/`
- [ ] Cele 3 module din Etapa 4 funcționale

### Preprocesare și Date
- [ ] Dataset combinat (vechi + nou) preprocesat (dacă ați adăugat date)
- [ ] Split train/val/test: 70/15/15% (verificat dimensiuni fișiere)
- [ ] Scaler din Etapa 3 folosit consistent (`config/preprocessing_params.pkl`)

### Antrenare Model - Nivel 1 (OBLIGATORIU)
- [ ] Model antrenat de la ZERO (nu fine-tuning pe model pre-antrenat)
- [ ] Minimum 10 epoci rulate (verificabil în `results/training_history.csv`)
- [ ] Tabel hiperparametri + justificări completat în acest README
- [ ] Metrici calculate pe test set: **Accuracy ≥65%**, **F1 ≥0.60**
- [ ] Model salvat în `models/trained_model.h5` (sau .pt, .lvmodel)
- [ ] `results/training_history.csv` există cu toate epoch-urile

### Integrare UI și Demonstrație - Nivel 1 (OBLIGATORIU)
- [ ] Model ANTRENAT încărcat în UI din Etapa 4 (nu model dummy)
- [ ] UI face inferență REALĂ cu predicții corecte
- [ ] Screenshot inferență reală în `docs/screenshots/inference_real.png`
- [ ] Verificat: predicțiile sunt diferite față de Etapa 4 (când erau random)

### Documentație Nivel 2 (dacă aplicabil)
- [ ] Early stopping implementat și documentat în cod
- [ ] Learning rate scheduler folosit (ReduceLROnPlateau / StepLR)
- [ ] Augmentări relevante domeniu aplicate (NU rotații simple!)
- [ ] Grafic loss/val_loss salvat în `docs/loss_curve.png`
- [ ] Analiză erori în context industrial completată (4 întrebări răspunse)
- [ ] Metrici Nivel 2: **Accuracy ≥75%**, **F1 ≥0.70**

### Documentație Nivel 3 Bonus (dacă aplicabil)
- [ ] Comparație 2+ arhitecturi (tabel comparativ + justificare)
- [ ] Export ONNX/TFLite + benchmark latență (<50ms demonstrat)
- [ ] Confusion matrix + analiză 5 exemple greșite cu implicații

### Verificări Tehnice
- [ ] `requirements.txt` actualizat cu toate bibliotecile noi
- [ ] Toate path-urile RELATIVE (nu absolute: `/Users/...` )
- [ ] Cod nou comentat în limba română sau engleză (minimum 15%)
- [ ] `git log` arată commit-uri incrementale (NU 1 commit gigantic)
- [ ] Verificare anti-plagiat: toate punctele 1-5 respectate

### Verificare State Machine (Etapa 4)
- [ ] Fluxul de inferență respectă stările din State Machine
- [ ] Toate stările critice (PREPROCESS, INFERENCE, ALERT) folosesc model antrenat
- [ ] UI reflectă State Machine-ul pentru utilizatorul final

### Pre-Predare
- [ ] `docs/etapa5_antrenare_model.md` completat cu TOATE secțiunile
- [ ] Structură repository conformă: `docs/`, `results/`, `models/` actualizate
- [ ] Commit: `"Etapa 5 completă – Accuracy=X.XX, F1=X.XX"`
- [ ] Tag: `git tag -a v0.5-model-trained -m "Etapa 5 - Model antrenat"`
- [ ] Push: `git push origin main --tags`
- [ ] Repository accesibil (public sau privat cu acces profesori)

---

## Livrabile Obligatorii (Nivel 1)

Asigurați-vă că următoarele fișiere există și sunt completate:

1. **`docs/etapa5_antrenare_model.md`** (acest fișier) cu:
   - Tabel hiperparametri + justificări (complet)
   - Metrici test set raportate (accuracy, F1)
   - (Nivel 2) Analiză erori context industrial (4 paragrafe)

2. **`models/trained_model.h5`** (sau `.pt`, `.lvmodel`) - model antrenat funcțional

3. **`results/training_history.csv`** - toate epoch-urile salvate

4. **`results/test_metrics.json`** - metrici finale:

Exemplu:
```json
{
  "test_accuracy": 0.7823,
  "test_f1_macro": 0.7456,
  "test_precision_macro": 0.7612,
  "test_recall_macro": 0.7321
}
```

5. **`docs/screenshots/inference_real.png`** - demonstrație UI cu model antrenat

6. **(Nivel 2)** `docs/loss_curve.png` - grafic loss vs val_loss

7. **(Nivel 3)** `docs/confusion_matrix.png` + analiză în README

---

## Predare și Contact

**Predarea se face prin:**
1. Commit pe GitHub: `"Etapa 5 completă – Accuracy=X.XX, F1=X.XX"`
2. Tag: `git tag -a v0.5-model-trained -m "Etapa 5 - Model antrenat"`
3. Push: `git push origin main --tags`

---

**Mult succes! Această etapă demonstrează că Sistemul vostru cu Inteligență Artificială (SIA) funcționează în condiții reale!**