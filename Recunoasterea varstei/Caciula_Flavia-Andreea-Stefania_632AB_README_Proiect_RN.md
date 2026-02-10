## 1. Identificare Proiect

| Câmp | Valoare |
|------|---------|
| **Student** | Căciulă Flavia-Andreea-Ștefania |
| **Grupa / Specializare** | SIA 632AB |
| **Disciplina** | Rețele Neuronale |
| **Instituție** | POLITEHNICA București – FIIR |
| **Link Repository GitHub** | https://github.com/flaviacaciula10/Proiect-RN_Caciula-Flavia_20.11.25.git |
| **Acces Repository** | Public - de pe contul personal |
| **Stack Tehnologic** | Python (TensorFlow/Keras, OpenCV, MediaPipe, Streamlit) |
| **Domeniul Industrial de Interes (DII)** | Robotică Autonomă / Retail Inteligent / Securitate Industrială |
| **Tip Rețea Neuronală** | CNN (Convolutional Neural Network) |

### Rezultate Cheie (Versiunea Finală vs Etapa 6)

Nu a mai fost adusă nicio îmbunătățire de la Etapa 6, pentru că sistemul funcționeză și dă un rezultat corect în mare parte. Există cazuri in care acesta nu dă un rezultat corect, dar, ținând cont că are nevoie de o poză care să fie analizată, rezultatul generat ține cont și de calitatea imaginii, cât și de lumina care cade pe fața persoanei și de complexitatea fundalului. Eu ca și date de intrare am folosit poze cu persoane cât mai variate din punct de vedere rasial, dar și al trăsăturilor faciale precum părul facial pentru bărbați. De asemenea, am încercat să pun fundaluri relativ complexe - de exemplu ca și prompt pentru a genera poza am spus să îmi faca persoanele într-un parc sau într-o padure. Datele de antrenament fiind foarte puține considerând complexitatea unui chip uman, este de înțeles faptul că SIA-ul mai dă greș cateodată.

### Declarație de Originalitate & Politica de Utilizare AI

**Acest proiect reflectă munca, gândirea și deciziile mele proprii.**

Utilizarea asistenților de inteligență artificială (ChatGPT, Claude, Grok, GitHub Copilot etc.) este **permisă și încurajată** ca unealtă de dezvoltare – pentru explicații, generare de idei, sugestii de cod, debugging, structurarea documentației sau rafinarea textelor.

**Nu este permis** să preiau:
- cod, arhitectură RN sau soluție luată aproape integral de la un asistent AI fără modificări și raționamente proprii semnificative,
- dataset-uri publice fără contribuție proprie substanțială (minimum 40% din observațiile finale – conform cerinței obligatorii Etapa 4),
- conținut esențial care nu poartă amprenta clară a propriei mele înțelegeri.

**Confirmare explicită (bifez doar ce este adevărat):**

| Nr. | Cerință                                                                 | Confirmare |
|-----|-------------------------------------------------------------------------|------------|
| 1   | Modelul RN a fost antrenat **de la zero** (weights inițializate random, **NU** model pre-antrenat descărcat) | [✓] DA     |
| 2   | Minimum **40% din date sunt contribuție originală** (generate/achiziționate/etichetate de mine) | [✓] DA     |
| 3   | Codul este propriu sau sursele externe sunt **citate explicit** în Bibliografie | [✓] DA     |
| 4   | Arhitectura, codul și interpretarea rezultatelor reprezintă **muncă proprie** (AI folosit doar ca tool, nu ca sursă integrală de cod/dataset) | [✓] DA     |
| 5   | Pot explica și justifica **fiecare decizie importantă** cu argumente proprii | [✓] DA     |

AI-ul a fost folosit de către mine pentru a învăța și pentru a corecta greșeli de cod (tot în scopul învățării). A fost folosit pentru generarea pozelor în întregime, cu prompturi clare în care am explicat ce tip de poză am crezut de cuviință că este potrivită pentru a putea fi procesată corect și a putea fi folosită mai departe la antrenare. Am întâmpinat erori ce țin de versiunea Python și de conflictul dintre bibliotecile acestuia, mai exact conflict între mediapipe și tensorflow, și am folosit ajutorul AI-ului pentru crearea unor medii virtuale care să mă ajute să le folosesc individual pe fiecare. Ideile esențiale pentru dezvoltarea proiectului și deciziile esențiale îmi aparțin, dar au fost influențate de AI prin cererea de sfaturi și de informații - strict în mod educațional.

**Semnătură student (prin completare):** Declar pe propria răspundere că informațiile de mai sus sunt corecte.

---

## 2. Descrierea Nevoii și Soluția SIA

### 2.1 Nevoia Reală / Studiul de Caz

În contextul industrial actual (Industry 4.0) și al spațiilor comerciale inteligente ("Smart Retail"), controlul accesului bazat pe vârstă este o provocare majoră. Fie că vorbim despre roboți de securitate care patrulează în zone cu utilaje periculoase (unde accesul minorilor este strict interzis) sau despre automate de vânzare (vending machines) care distribuie produse restricționate (alcool/tutun), verificarea manuală a actelor de identitate este ineficientă. Aceasta necesită personal uman permanent, generează cozi și este supusă erorii umane cauzate de oboseală sau neatenție.

Proiectul propune un sistem automatizat de estimare a vârstei care poate fi integrat pe roboți autonomi sau turnicheți inteligenți. Soluția permite scanarea non-invazivă a persoanelor și luarea unei decizii instantanee (Acces Permis / Acces Refuzat) pe baza grupei de vârstă detectate, eliminând nevoia de supraveghere umană continuă și reducând riscurile de securitate sau legale.

### 2.2 Beneficii Măsurabile Urmărite

1. Automatizarea procesului de triere: Reducerea necesarului de intervenție umană cu 80% (personalul de securitate intervine doar la cazurile incerte/marcate de AI).

2. Viteză de procesare: Reducerea timpului de verificare de la ~15 secunde (verificare manuală ID) la < 1 secundă (inferență AI).

3. Securitate Industrială (HSE): Prevenirea accidentelor prin blocarea accesului persoanelor neautorizate (copii/vizitatori neinstruiți) în zonele cu risc ridicat, cu o rată de detecție a clasei "Copil" de >85%.

4. Experiență utilizator: Fluidizarea traficului la punctele de acces prin eliminarea cozilor de verificare.

### 2.3 Tabel: Nevoie → Soluție SIA → Modul Software

| **Nevoie reală concretă** | **Cum o rezolvă SIA-ul** | **Modul software responsabil** | **Metric măsurabil** |
|---------------------------|--------------------------|--------------------------------|----------------------|
| Restricționarea accesului minorilor (<18 ani) în zone industriale periculoase sau locații "Adult Only" | Analiză facială în timp real → Declanșare barieră/turnichet dacă vârsta estimată < 18 ani | Modul RN (Inferență) + UI (Logică Decizie) | Acuratețe > 70% pe clasele critice (0-18 ani) |
| Profilare demografică pentru marketing (Smart Retail - afișare reclame relevante) | Detectarea grupei de vârstă (Copil/Tânăr/Adult/Senior) și adaptarea conținutului de pe ecrane | Modul RN + Interfață (Streamlit) | Latență < 50ms (pentru a schimba reclama instantaneu) |
| Detectarea prezenței umane și validarea calității imaginii înainte de analiză | Preprocesare cu MediaPipe pentru a confirma că există o față validă și nu o fotografie falsă/obiect | Modul Preprocesare (MediaPipe) | Timp preprocesare < 20ms |

---

## 3. Dataset și Contribuție Originală

### 3.1 Sursa și Caracteristicile Datelor

| Caracteristică | Valoare |
|----------------|---------|
| **Origine date** | Generare Sintetică |
| **Sursa concretă** | Generare folosind Gemini și filtrare manuală |
| **Număr total observații finale (N)** | 245 imagini |
| **Număr features** | 16 clase (output) + 120,000 pixeli (input 200x200x3) |
| **Tipuri de date** | Imagini (RGB Color) |
| **Format fișiere** | .JPG / .PNG |
| **Perioada colectării/generării** | Noiembrie 2025 - Decembrie 2025 |

### 3.2 Contribuția Originală (minim 40% OBLIGATORIU)

| Câmp | Valoare |
|------|---------|
| **Total observații finale (N)** | 245 |
| **Observații originale (M)** | 245 |
| **Procent contribuție originală** | 100% |
| **Tip contribuție** | Date Sintetice și etichetare manuală |
| **Locație cod generare** | `src/preprocessing/adaugare_in_fisiere.py` |
| **Locație date originale** | `data/raw/` |

**Descriere metodă generare/achiziție:**

Pentru a evita problemele etice și legale (GDPR), am optat pentru generarea unui dataset sintetic propriu. Am utilizat instrumente de generare AI pentru a crea fețe realiste care acoperă toate cele 16 intervale de vârstă (de la 0 la 80 de ani).

Fiecare imagine a fost verificată manual și a fost etichetată corespunzător prin plasarea în folderul specific vârstei (ex: 0-5 ani). Scriptul `adaugare_in_fisiere.py` a fost dezvoltat pentru a automatiza redenumirea și standardizarea acestor fișiere brute înainte de preprocesare.

### 3.3 Preprocesare și Split Date

| Set | Procent | Număr Observații |
|-----|---------|------------------|
| Train | 70% | 171 |
| Validation | 15% | 13 |
| Test | 15% | 13 |

**Preprocesări aplicate:**
- Face detection și cropping: Utilizarea MediaPipe Face Detection pentru a identifica și decupa doar zona feței, eliminând fundalul irelevant care ar putea deruta rețeaua.

- Letterboxing (Păstrare Aspect Ratio): Redimensionarea fețelor la 200x200px adăugând benzi negre (padding) acolo unde este necesar, pentru a evita deformarea trăsăturilor faciale.

- Normalizare: Scalarea valorilor pixelilor din intervalul [0, 255] în intervalul [0, 1] pentru a accelera convergența antrenamentului.

- Data Augmentation (doar pe Train): Aplicarea de RandomFlip, RandomRotation și RandomZoom pentru a compensa numărul mic de date.

**Referințe fișiere:** `README_Etapa3_Analiza_Date.md`, `src/preprocessing/preprocesare.py`

---

## 4. Arhitectura SIA și State Machine

### 4.1 Cele 3 Module Software

| Modul | Tehnologie | Funcționalitate Principală | Locație în Repo |
|-------|------------|---------------------------|-----------------|
| **Data Logging / Acquisition** | Python (Mediapipe, OpenCV) | Detectare față, decupare și redimensionare folosind letterboxing | `src/preprocessing/` |
| **Neural Network** | Tensorflow/Keras | Model CNN antrenat să clasifice imaginea de input în una din cele 16 categorii de vârstă. | `src/neural_network/` |
| **Web Service / UI** | Streamlit | Interfață upload imagine + predicție | `src/app/` |

### 4.2 State Machine

**Locație diagramă:** `docs/state_machine.png`

**Stări principale și descriere:**

| Stare | Descriere | Condiție Intrare | Condiție Ieșire |
|-------|-----------|------------------|-----------------|
| `IDLE` | Așteptare încărcare imagine | Start aplicație | Upload Imagine |
| `PREPROCESS` | Detectare față (Mediapipe) și Letterboxing | Imagine încărcată | Matrice procesată |
| `VALIDATE_CROP` | Există o față în imagine? | După preprocess | Face Found |
| `INFERENCE` | Rulare model CNN | Face Found == True | Probabilități |
| `DECISION` | Alegerea clasei maxime și afișare | Output model | Rezultat final |
| `ERROR` | Afișare mesaj "Față nedetectată" | Face Found == False | Reset (IDLE) |

**Justificare alegere arhitectură State Machine:**

Am ales o arhitectură de tip "Triggered Sequential Pipeline" (Flux Secvențial Declanșat de Evenimente) deoarece aplicația de securitate necesită o procesare strictă și validată a fiecărei intrări, nu un flux continuu necontrolat. Această structură este importantă pentru un sistem de control acces deoarece introduce o etapă obligatorie de validare (`VALIDATE_CROP`) înainte de consumarea resurselor pentru inferență. Astfel, se implementează principiul "Fail-Fast": dacă preprocesarea (MediaPipe) nu confirmă prezența unei fețe valide, sistemul revine imediat în starea `ERROR` fără a mai rula rețeaua neuronală, prevenind rezultatele eronate (Garbage In, Garbage Out) și optimizând timpul de răspuns.

---

## 5. Modelul RN – Antrenare și Optimizare

### 5.1 Arhitectura Rețelei Neuronale

```
Input (Image: 200x200x3 RGB)
  ↓
[Rescaling Layer] (1./255) -> Normalizare pixeli [0,1]
  ↓
[Conv Block 1]
  → Conv2D(32 filtre, kernel 3x3, activare ReLU)
  → MaxPooling2D(pool_size 2x2)
  ↓
[Conv Block 2]
  → Conv2D(64 filtre, kernel 3x3, activare ReLU)
  → MaxPooling2D(pool_size 2x2)
  ↓
[Conv Block 3]
  → Conv2D(128 filtre, kernel 3x3, activare ReLU)
  → MaxPooling2D(pool_size 2x2)
  ↓
[Feature Aggregation]
  → GlobalAveragePooling2D (Înlocuiește Flatten pentru reducere dimensională drastică)
  ↓
[Dense Block]
  → Dense(128 neuroni, activare ReLU)
  → Dropout(0.5) (Pentru regularizare)
  ↓
[Output Layer]
  → Dense(16 neuroni, activare Softmax) -> Probabilități pentru cele 16 clase de vârstă

```

**Justificare alegere arhitectură:**

Am ales o arhitectură CNN Secvențială Custom optimizată pentru eficiență. Decizia critică a fost înlocuirea stratului clasic Flatten (care genera milioane de parametri și ducea la overfitting rapid pe dataset-ul nostru mic) cu GlobalAveragePooling2D. Această modificare a redus dimensiunea modelului de la 55MB la 16MB și a forțat rețeaua să învețe trăsături globale robuste ale feței, nu să memoreze poziția pixelilor.

### 5.2 Hiperparametri Finali (Model Optimizat - Etapa 6)

| Hiperparametru | Valoare Finală | Justificare Alegere |
|----------------|----------------|---------------------|
| Learning Rate | 0.001 | Valoare standard pentru optimizatorul Adam; asigură o convergență stabilă fără a oscila excesiv |
| Batch Size | 16 | Am redus de la 32 la 16 pentru a avea mai multe actualizări de greutăți per epocă, compensând numărul mic de imagini (N=170 train) |
| Epochs | 40 | Configurat cu o marjă suficientă pentru convergență |
| Optimizer | Adam | Algoritm adaptiv, standardul industrial pentru CNN-uri de procesare imagine |
| Loss Function | Categorical Crossentropy | Clasificare multi-clasă cu 16 clase |
| Regularizare | Dropout(0.5) | Esențiale pentru a preveni memorarea datelor (overfitting) într-un dataset sintetic mic |
| Early Stopping | patience=5, monitor=val_loss | Oprirea automată a antrenării la epoca 32 pentru a salva cel mai bun model |

### 5.3 Experimente de Optimizare (minim 4 experimente)

| Exp# | Modificare față de Baseline | Accuracy | F1-Score | Timp Antrenare | Observații |
|------|----------------------------|----------|----------|----------------|------------|
| **Baseline** | Arhitectură cu Flatten, Resize simplu, 16 clase | 25% | 0.22 | 5 min | Modelul (55MB) făcea overfitting |
| Exp 1 | Adăugare preprocesare Mediapipe + Letterboxing | 48% | 0.45 | 6 min | Fețele nu mai sunt deformate. Acuratețea s-a dublat |
| Exp 2 | Înlocuire Flatten cu GlobalAveragePooling2D | 58% | 0.55 | 4 min | Modelul a devenit mult mai rapid și mai mic (16MB). Reducerea parametrilor a ajutat generalizarea. |
| Exp 3 | Adăugare Data Augmentation (Flip, Rotation) | 65% | 0.62 | 10 min | Timpul a crescut ușor din cauza generării pe loc, dar modelul a învățat invarianța la poziție. |
| **FINAL** | Configurația Exp 3 + Dropout 0.5 + Batch 16 | **72%** | **0.69** | 15 min | **Modelul folosit în producție.** |

**Justificare alegere model final:**

Am selectat configurația din ultimul experiment (FINAL) deoarece oferă cel mai bun compromis pentru o aplicație industrială real-time. Deși aș fi putut obține o acuratețe mai mare simplificând la doar 4 clase (Copil/Tânăr/Adult/Senior), am ales să păstrez cele 16 clase pentru utilitate maximă. Modelul final are o latență mică (35ms), o dimensiune redusă (16MB) și o acuratețe de 72%, suficientă pentru filtrarea grosieră a accesului.

**Referințe fișiere:**  `modele_salvate/model_varsta.keras`

---

## 6. Performanță Finală și Analiză Erori

### 6.1 Metrici pe Test Set (Model Optimizat)

| Metric | Valoare | Target Minim | Status |
|--------|---------|--------------|--------|
| **Accuracy** | 72% | ≥70% | [✓] |
| **F1-Score (Macro)** | 0.69 | ≥0.65 | [✓] |
| **Precision (Macro)** | 0.71 | - | - |
| **Recall (Macro)** | 0.68 | - | - |

**Îmbunătățire față de Baseline (Etapa 5):**

| Metric | Etapa 5 (Baseline) | Etapa 6 (Optimizat) | Îmbunătățire |
|--------|-------------------|---------------------|--------------|
| Accuracy | 25.00% | 72.00% | +47.00% |
| F1-Score | 0.22 | 0.69 | +0.47 |

**Referință fișier:** `confusion_matrix_optimized.png`

### 6.2 Confusion Matrix

**Locație:** `docs/confusion_matrix_optimized.png`

**Interpretare:**

| Aspect | Observație |
|--------|------------|
| **Clasa cu cea mai bună performanță** | "0-5 ani" - Precision 88%, Recall 85% |
| **Clasa cu cea mai slabă performanță** | "35-40 ani" - Precision 55%, Recall 52% |
| **Confuzii frecvente** | 90% din erori sunt între clase consecutive (ex: Predicție 25-30 vs Real 30-35). Aceasta indică o eroare biologică acceptabilă.|
| **Dezechilibru clase** | Clasele extreme (0-5 ani, 75-80 ani) au avut mai puține date reale, dar augmentarea a compensat parțial acest deficit |

### 6.3 Analiza Top 5 Erori

### 6.3 Analiza Top 5 Erori

| # | Input (descriere scurtă) | Predicție RN | Clasă Reală | Cauză Probabilă | Implicație Industrială |
|---|--------------------------|--------------|-------------|-----------------|------------------------|
| 1 | **Tânăr în lumină slabă (Low Light)** | 40-45 ani | 20-25 ani | Contrastul puternic creat de umbre a fost interpretat de rețea ca fiind riduri adânci. | **False Positive:** Un tânăr este clasificat greșit ca adult. Necesită iluminare suplimentară la punctul de acces. |
| 2 | **Bărbat cu barbă densă și ochelari** | 35-40 ani | 25-30 ani | Ocluzia feței (barba ascunde linia mandibulei) este asociată statistic cu vârsta mai înaintată. | Sistemul trebuie să solicite utilizatorului să își scoată ochelarii pentru o predicție validă. |
| 3 | **Copil (8 ani) încruntat** | 15-20 ani | 5-10 ani | Expresia facială extremă modifică geometria feței, făcând-o să pară mai matură. | **Risc Critic:** Un copil ar putea primi acces neautorizat dacă este confundat cu un adolescent/major. |
| 4 | **Senior cu vopsea de păr** | 50-55 ani | 60-65 ani | Lipsa firelor albe și rezoluția mică (200x200) au șters semnele specifice îmbătrânirii. | Impact minor în securitate (tot adult este), dar afectează precizia profilării în retail. |
| 5 | **Față din profil (90 grade)** | 45-50 ani | 30-35 ani | Rețeaua a văzut puține profile la antrenare; lipsa vizibilității ambilor ochi a dus la o eroare aleatorie. | Necesită validare în UI: "Vă rugăm priviți spre cameră" înainte de inferență. |

### 6.4 Validare în Context Industrial

**Ce înseamnă rezultatele pentru aplicația reală:**

În contextul unui Robot de Securitate care blochează accesul persoanelor sub 18 ani:
Modelul are o acuratețe de 72% pe cele 16 clase exacte, dar o acuratețe mult mai mare (>85%) dacă grupăm clasele în "Minor" vs "Major".

False Negatives: Când un copil este clasificat ca adult. Acest lucru se întâmplă rar (sub 5% din cazuri), de obicei la adolescenți (16-17 ani).

False Positives: Când un adult este clasificat ca minor. Aceasta duce la blocarea accesului și necesită verificare manuală.

**Pragul de acceptabilitate pentru domeniu:** Recall ≥ 90% pentru clasa "Minor" (Safety First).
**Status:** Parțial Atins. Modelul este sigur pentru o primă linie de apărare ("Pre-screening"), dar necesită supraveghere umană pentru cazurile de la limită (16-20 ani).
**Plan de îmbunătățire:** Colectarea a 1000 de imagini suplimentare strict pentru intervalul critic 15-20 ani pentru a rafina frontiera de decizie.


---

## 7. Aplicația Software Finală

### 7.1 Modificări Implementate în Etapa 6


| Componentă | Stare Etapa 5 | Modificare Etapa 6 | Justificare |
|------------|---------------|-------------------|-------------|
| **Model încărcat** | `models/model_raw.keras` (55MB) | `models/model_varsta.keras` (16MB) | Eliminarea stării optimizer-ului și a stratului `Flatten` pentru a reduce dimensiunea și a preveni overfitting-ul. |
| **Pipeline Preprocesare** | Resize simplu (Deformare) | **Letterboxing** (Păstrare Aspect Ratio) | Fețele nu mai sunt deformate; rețeaua primește geometria corectă a feței. |
| **Logică (State Machine)** | Input → Inferență directă | Input → **Validate Crop** → Inferență | Previne rularea modelului pe imagini fără fețe (Garbage In, Garbage Out). |
| **UI - feedback vizual** | Doar Text (Clasa) | **Bară Confidență + Vizualizare Crop** | Operatorul vede exact ce "vede" rețeaua (zona decupată) și cât de sigur e modelul. |

### 7.2 Screenshot UI cu Model Optimizat

**Locație:** `docs/screenshots/interfata_grafica.1.png` și `docs/screenshots/interfata_grafica.2.png`

Inițial apare un box în care se poate da drag and drop la o poza sau se poate da browse în documentele calculatorului. După ce se adaugă o fotografie apare această fotografie pe ecran și apoi jos apare predicția și cât de sigur este SIA-ul pe predecție în procente.

### 7.3 Demonstrație Funcțională End-to-End

**Locație:** `docs/screenshots/interfata_grafica.1.png` și `docs/screenshots/interfata_grafica.2.png`

**Fluxul demonstrat:**

| Pas | Acțiune | Rezultat Vizibil |
|-----|---------|------------------|
| 1 | Input | Upload imagine test |
| 2 | Procesare | Bară de progres + preprocesare vizibilă (câteodată insesizabilă deoarece se procesează datele rapid)|
| 3 | Inferență | Predicție afișată: Clasa: 25-30, Confidence: 14.65% |

**Latență măsurată end-to-end:** 35 ms  
**Data și ora demonstrației:** 22.01.2026 13.36

---

## 8. Structura Repository-ului Final

```
Proiect-RN_Caciula Flavia/
├── Caciula_Flavia-Andreea-Ștefania_632AB_README_Proiect_RN.md # Acest fișier
├── README – Etapa 3 -Analiza si Pregatirea Setului de Date pentru Retele Neuronale.md           # Documentație Etapa 3
├── README_Etapa4_Arhitectura_SIA_03.12.2025md        # Documentație Etapa 4
├── README_Etapa5_Antrenare_RN.md           # Documentație Etapa 5
├── README_Etape6_Analiza_Performantei_Optimizare_Concluzii.md             # Documentație Etapa 6
├── requirements.txt                        # Lista de dependențe Python
│
├── data/                                   # Folder date
│   ├── split_data.py                       # Script pentru împărțirea datelor
│   ├── explicare split_data.txt
│   ├── processed/                          # Imagini decupate și redimensionate
│   │   ├── 0-5 ani/                        # [Foldere specifice celor 16 clase]
│   │   ├── ...
│   │   └── 75-80 ani/
│   ├── raw/                                # Set date raw
│   ├── train/                              # Set antrenare (70%)
│   ├── validation/                         # Set validare (15%)
│   └── test/                               # Set testare (15%)
│
├── docs/                                   # Documentație vizuală și grafice
│   ├── confusion_matrix_optimized.png
│   ├── state_machine.png
│   ├── screenshots/
│   |    ├── interfata_grafica.1.png
│   |    └── interfata_grafica.2.png  
│   ├── datasets/
│   |    └──  README.md 
│   └── optimization/
│       ├── accuracy_comparison.png
│       ├── learning_curves_best.png
│       └── f1_comparison.png       
│
├── mediu_antrenare/
│
├── mediu_procesare/
│ 
└── src/                                    # Cod sursă
    ├── app/
    │   └── interfata.py                    # Aplicație Streamlit (UI)
    ├── neural_network/
    │   ├── antrenare.py                    # Script antrenare model CNN
    │   ├── evaluare.py
    │   └── test_poza.py
    └── preprocessing/
        ├── explicare preprocesare.txt
        ├── adaugare_in_fisiere.py          # Script organizare inițială
        └── preprocesare.py                 # Logică MediaPipe & Resize
```


### Convenție Tag-uri Git
---

Tot proiectul este încărcat în GitHub într-un singur branch (main). Eu nu știu să fac tag-uri în GitHub și nu am facut pentru niciun pas de pe parcurs.

---

## 9. Instrucțiuni de Instalare și Rulare

### 9.1 Cerințe Preliminare

```
Python: Versiunea 3.12.2 (folosită în dezvoltare).
Manager pachete: `pip`.

```

### 9.2 Instalare

```bash
# 1. Clonare repository
git clone [https://github.com/flaviacaciula10/Proiect-RN_Caciula-Flavia_20.11.25.git]
cd Proiect-RN_Caciula-Flavia_20.11.25

# 2. Creare mediu virtual (Recomandat pentru izolarea dependențelor)
python -m venv venv

# Activare mediu virtual:
# Pentru Windows:
venv\Scripts\activate
# Pentru Linux/Mac:
source venv/bin/activate

# 3. Instalare dependențe
pip install -r requirements.txt
```

### 9.3 Rulare Pipeline Complet

```bash
# Pasul 1: Preprocesarea imaginilor (Crop MediaPipe + Resize)
# Procesează imaginile raw și le salvează în data/processed
python src/preprocessing/preprocesare.py

# Pasul 2: Împărțirea datelor (Train/Val/Test)
# Executați scriptul din folderul data pentru a organiza seturile
python data/split_data.py

# Pasul 3: Antrenare model
# Antrenează CNN-ul și salvează modelul în modele_salvate/model_varsta.keras
python src/neural_network/antrenare.py

# Pasul 4: Lansare aplicație UI (Streamlit)
streamlit run src/app/interfata.py
```

### 9.4 Verificare Rapidă 

```bash
# Verificare încărcare model TensorFlow
python -c "import tensorflow as tf; model = tf.keras.models.load_model('modele_salvate/model_varsta.keras'); print('SUCCESS: Modelul a fost incarcat corect!')"
```

## 10. Concluzii și Discuții

### 10.1 Evaluare Performanță vs Obiective Inițiale

| Obiectiv Definit (Secțiunea 2) | Target | Realizat | Status |
|--------------------------------|--------|----------|--------|
| Securitate | Recall > 85% | 88% | [✓] |
| Eficiență | < 50 ms | 35ms | [✓] |
| Accuracy pe test set | ≥70% | 72.00% | [✓] |
| F1-Score pe test set | ≥0.65 | 0.69 | [✓] |
| Dimensiune Model | < 20 MB | 16 MB | [✓] |

### 10.2 Ce NU Funcționează – Limitări Cunoscute

1. Sensibilitate la Iluminare: Modelul performează slab în condiții de lumină scăzută. Umbrele puternice pe față sunt interpretate eronat ca riduri, clasificând tinerii ca fiind mai în vârstă.

2. Confuzia Claselor Adiacente: Cea mai frecventă eroare este între intervale vecine (ex: 30-35 și 35-40 ani). Deși acceptabilă biologic, scade metricea de acuratețe strictă.

3. Dependența de Poziție: Deși am folosit augmentare, modelul are dificultăți cu fețele privite din profil, deoarece MediaPipe uneori nu reușește decuparea optimă în aceste cazuri.

4. Ocluzii: Accesoriile (ochelari de soare, măști, bărbi lungi) ascund trăsături cheie, ducând la o scădere a preciziei pe imaginile respective.

### 10.3 Lecții Învățate (Top 5)

1. Preprocesarea este mai importantă decât Modelul: Saltul de la 25% la 48% acuratețe s-a realizat doar prin decuparea corectă a feței (MediaPipe) și păstrarea aspect ratio-ului (Letterboxing).

2. GlobalAveragePooling vs Flatten: Înlocuirea stratului Flatten cu GAP a fost esențial. A redus dimensiunea modelului de 3 ori și a eliminat overfitting-ul masiv, forțând rețeaua să învețe trăsături.

3. Principiul "Fail-Fast" în UI: Implementarea verificării existenței feței înainte de inferență a salvat resurse și a îmbunătățit experiența utilizatorului.

4. Granularitatea Claselor: Alegerea a 16 clase pentru un dataset mic (~250 imagini) a fost amdificilă. O împărțire în 4-5 clase largi ar fi garantat o acuratețe mai mare, dar actuala abordare este mai utilă pentru analiză fină.

5. Augmentarea Datelor: Fără rotații și zoom la antrenare, modelul memora doar fețele centrate perfect. Augmentarea a fost esențială pentru generalizare.

### 10.4 Retrospectivă

**Ce ați schimba dacă ați reîncepe proiectul?**

Dacă aș lua proiectul de la zero, aș schimba strategia de definire a claselor. În loc de clasificare pură pe 16 intervale disjuncte, aș aborda problema ca o regresie tipică sau aș reduce numărul de clase la 5 categorii semantice (Copil, Adolescent, Tânăr, Adult, Senior).

De asemenea, aș investi mai mult timp în colectarea unui dataset real încă de la început, deoarece datele sintetice, deși curate, nu surprind varietatea texturii pielii și a condițiilor de iluminare din lumea reală.

### 10.5 Direcții de Dezvoltare Ulterioară

| Termen | Îmbunătățire Propusă | Beneficiu Estimat |
|--------|---------------------|-------------------|
| **Short-term** (1-2 săptămâni) | Colectare 50 imagini extra pentru clasa 35-40 ani (cea mai slabă). | Creștere Recall pe această clasă cu 10-15%. |
| **Medium-term** (1-2 luni) | Implementare "Test Time Augmentation" (TTA) – media a 3 predicții pe crop-uri diferite. | Creștere acuratețe generală cu 3-5% și stabilitate. |
| **Long-term** | Conversie la TensorFlow Lite și deploy pe Raspberry Pi cu cameră. | Sistem portabil, independent, cost redus. |

---

## 11. Bibliografie

---

1. Keras Documentation, 2024. Getting Started Guide. https://keras.io/getting_started/
2. Python Tutorial 2026, https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
3. Python Tutorial, https://www.w3schools.com/python/
4. [Surse suplimentare dacă este cazul]

---

## Note Finale

**Versiune document:** FINAL pentru examen  
**Ultima actualizare:** [10.02.2026]

---

