# 📘 README – Etapa 4: Arhitectura Completă a Aplicației SIA bazată pe Rețele Neuronale

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** Caciula Flavia-Andreea-Stefania  
**Link Repository GitHub**
**Data:** 04.12.2025
---

## Scopul Etapei 4

Această etapă corespunde punctului **5. Dezvoltarea arhitecturii aplicației software bazată pe RN** din lista de 9 etape - slide 2 **RN Specificatii proiect.pdf**.

**Trebuie să livrați un SCHELET COMPLET și FUNCȚIONAL al întregului Sistem cu Inteligență Artificială (SIA). In acest stadiu modelul RN este doar definit și compilat (fără antrenare serioasă).**

### IMPORTANT - Ce înseamnă "schelet funcțional":

 **CE TREBUIE SĂ FUNCȚIONEZE:**
- Toate modulele pornesc fără erori
- Pipeline-ul complet rulează end-to-end (de la date → până la output UI)
- Modelul RN este definit și compilat (arhitectura există)
- Web Service/UI primește input și returnează output

 **CE NU E NECESAR ÎN ETAPA 4:**
- Model RN antrenat cu performanță bună
- Hiperparametri optimizați
- Acuratețe mare pe test set
- Web Service/UI cu funcționalități avansate

**Scopul anti-plagiat:** Nu puteți copia un notebook + model pre-antrenat de pe internet, pentru că modelul vostru este NEANTRENAT în această etapă. Demonstrați că înțelegeți arhitectura și că ați construit sistemul de la zero.

---

##  Livrabile Obligatorii

### 1. Tabelul Nevoie Reală → Soluție SIA → Modul Software (max ½ pagină)
Completați in acest readme tabelul următor cu **minimum 2-3 rânduri** care leagă nevoia identificată în Etapa 1-2 cu modulele software pe care le construiți (metrici măsurabile obligatoriu):

|           **Nevoie reală concretă**                    |        **Cum o rezolvă SIA-ul vostru**         |     **Modul software responsabil**    |
|*Control acces* (Kiosk/Vending Machine): Restricționarea|Clasificarea persoanei într-un palier de vârstă |            UI/Logic + RN              |
|automată a vânzării de produse (alcool/tutun) minorilor.|pe baza trăsăturilor faciale.                   |                                       |
|*Publicitate adaptabilă* (Retail): Afișarea de reclame  |Detectarea feței și estimarea intervalului de   |     Achiziție/Preprocesare + RN       |
|relevante pe ecrane digitale în funcție de demografia   |vârstă pentru a selecta reclama potrivită din   |                                       |
|privitorilor.                                           |baza de date.                                   |                                       |
|*Analiză demografică* (Evenimente): Colectarea de       |Procesarea fluxului video și împărțirea lor pe  |            Data loggin + RN           |
|statistici anonime despre participanții la un eveniment.|grupe de vârstă (din 5 în 5 ani) pentru raportare|                                      |
|                                                        |post-eveniment.                                 |                                       |
                                                           
                                                          

### 2. Contribuția Voastră Originală la Setul de Date – MINIM 40% din Totalul Observațiilor Finale

**Strategia aleasă:** Deoarece seturile de date publice pot fi dezechilibrate sau pot avea probleme de licențiere, am optat pentru generarea unui set de date 100% sintetic și original folosind tehnologii de inteligență artificială generativă (Gemini). Acest lucru mi-a permis să controlez perfect distribuția pe clase (paliere de vârstă).

### Contribuția originală la setul de date:
**Total observații finale:** 340 (20 date x 17 paliere) 
**Observații originale:** 340

**Tipul contribuției:** 
[ ] Date generate prin simulare fizică 
[ ] Date achiziționate cu senzori proprii 
[ ] Etichetare/adnotare manuală 
[X] Date sintetice prin metode avansate (Generative AI)

**Descriere detaliată:** Am generat întregul set de date folosind Gemini pentru a crea portrete fotorealiste ale unor persoane inexistente, acoperind intervalul de vârstă 0-85 ani, împărțit în paliere de 5 ani (17 clase).

**Metodologia a inclus:**

-> Am creat prompt-uri specifice pentru fiecare palier de vârstă pentru a asigura diversitate etnică, de gen și de trăsături faciale (ex: "Generează o fotografie cu o persoană cu vârsta cuprinsă între 15 și 20 de ani. Poza va avea în prim plan fața persoanei.").

-> Imaginile generate au fost verificate manual pentru a elimina artefactele specifice AI (deformări, fundaluri complexe) și pentru a confirma că trăsăturile corespund vârstei țintă.

-> Toate imaginile au trecut prin pipeline-ul de preprocesare (preprocesare.py) pentru a elimina fundalul (care era deja simplificat din prompt) și a le aduce la dimensiunea standard de 150x150 pixeli.

**Avantajul acestei abordări:**

-> Dataset perfect balansat: Am generat un număr egal de imagini pentru fiecare clasă.

-> Privacy: Nu folosesc imagini ale unor persoane reale, eliminând riscurile etice și legale.

**Locația datelor:** data/raw/ (datele generate brut) și data/processed/ (datele tăiate și redimensionate). 
**Dovezi:** Structura folderelor din data/raw/ arată imaginile originale generate, organizate pe foldere corespunzătoare prompt-urilor de vârstă.

#### Exemple pentru "contribuție originală":
-Simulări fizice realiste cu ecuații și parametri justificați  
-Date reale achiziționate cu senzori proprii (setup documentat)  
-Augmentări avansate cu justificare fizică (ex: simulare perspective camera industrială)  


#### Atenție - Ce NU este considerat "contribuție originală":

- Augmentări simple (rotații, flips, crop) pe date publice  
- Aplicare filtre standard (Gaussian blur, contrast) pe imagini publice  
- Normalizare/standardizare (aceasta e preprocesare, nu generare)  
- Subset dintr-un dataset public (ex: selectat 40% din ImageNet)


---

### 3. Diagrama State Machine a Întregului Sistem (OBLIGATORIE)

**Justificarea State Machine-ului ales:** Am ales o arhitectură de tip Wait-for-Trigger (Clasificare la cerere sau la detecție), potrivită pentru un sistem de control acces sau kiosk. Sistemul nu procesează continuu rețeaua neuronală pentru a economisi resurse, ci doar atunci când o față este detectată stabil.

**Stările principale:**

1. IDLE: Sistemul așteaptă input (imagine de la utilizator sau frame de la cameră).
2. FACE_DETECTION: Se utilizează haarcascade_frontalface_default.xml 4 pentru a verifica prezența unei fețe. Dacă nu se detectează nicio față $\to$ întoarcere la IDLE sau mesaj eroare.
3. PREPROCESSING: Aplicare remove_background_grabcut_face și resize_keep_ratio  pentru a aduce imaginea la formatul (150, 150, 3).
4. AGE_INFERENCE: Imaginea procesată intră în Rețeaua Neuronală (CNN) care returnează un vector de probabilități pentru cele 17 clase (paliere de 5 ani).
5. RESULT_DISPLAY: Afișarea palierului cu cea mai mare probabilitate (argmax) pe interfața grafică.

### 4. Scheletul Complet al celor 3 Module Cerute la Curs (slide 7)

**Modul 1:**Data Logging / Acquisition & Preprocessing
Fișiere: src/preprocessing/preprocesare.py, src/preprocessing/adaugare_in_fisiere.py.
Funcționalitate:
Citește imaginile din data/raw/ (organizate pe vârste: 0-5 ani, 5-10 ani, etc. ).
Detectează fața folosind haarcascade_frontalface_default.xml.
Elimină fundalul (GrabCut) și redimensionează la 150x150 px.
Salvează rezultatele în data/processed/.
Status: Funcțional. Testat pe structura de foldere existentă.

**Modul 2:** Neural Network Module
Fișier: src/neural_network/model_definition.py (Schelet).
Arhitectură propusă: Convolutional Neural Network (CNN).
Input: (150, 150, 3).
Hidden Layers: 3-4 straturi Conv2D + MaxPooling + Dropout (pentru generalizare).
Output Layer: Dense(17, activation='softmax') - deoarece avem clasificare multiclass (0-5, 5-10... 80-85).
Status: Definit și compilat (neantrenat).

**Modul 3:** Web Service / UI
Fișier: src/app/app.py.
Tehnologie: Streamlit (pentru rapiditate) sau Tkinter.
Funcționalitate:
Buton "Upload Image" sau "Start Camera".
Afișează imaginea originală vs imaginea preprocesată (fără fundal).
Afișează "Vârsta estimată: X-Y ani" (simulat în etapa 4 sau folosind modelul neantrenat cu weights random).

## Structura Repository-ului la Finalul Etapei 4 (OBLIGATORIE)

**Verificare consistență cu Etapa 3:**

```
proiect-rn-[nume-prenume]/
├── data/
│   ├── raw/
│   ├── processed/
│   ├── generated/  # Date originale
│   ├── train/
│   ├── validation/
│   └── test/
├── src/
│   ├── data_acquisition/
│   ├── preprocessing/  # Din Etapa 3
│   ├── neural_network/
│   └── app/  # UI schelet
├── docs/
│   ├── state_machine.*           #(state_machine.png sau state_machine.pptx sau state_machine.drawio)
│   └── [alte dovezi]
├── models/  # Untrained model
├── config/
├── README.md
├── README_Etapa3.md              # (deja existent)
├── README_Etapa4_Arhitectura_SIA.md              # ← acest fișier completat (în rădăcină)
└── requirements.txt  # Sau .lvproj
```

**Diferențe față de Etapa 3:**
- Adăugat `data/generated/` pentru contribuția dvs originală
- Adăugat `src/data_acquisition/` - MODUL 1
- Adăugat `src/neural_network/` - MODUL 2
- Adăugat `src/app/` - MODUL 3
- Adăugat `models/` pentru model neantrenat
- Adăugat `docs/state_machine.png` - OBLIGATORIU
- Adăugat `docs/screenshots/` pentru demonstrație UI

---

## Checklist Final – Bifați Totul Înainte de Predare

### Documentație și Structură
- [ ] Tabelul Nevoie → Soluție → Modul complet (minimum 2 rânduri cu exemple concrete completate in README_Etapa4_Arhitectura_SIA.md)
- [ ] Declarație contribuție 40% date originale completată în README_Etapa4_Arhitectura_SIA.md
- [ ] Cod generare/achiziție date funcțional și documentat
- [ ] Dovezi contribuție originală: grafice + log + statistici în `docs/`
- [ ] Diagrama State Machine creată și salvată în `docs/state_machine.*`
- [ ] Legendă State Machine scrisă în README_Etapa4_Arhitectura_SIA.md (minimum 1-2 paragrafe cu justificare)
- [ ] Repository structurat conform modelului de mai sus (verificat consistență cu Etapa 3)

### Modul 1: Data Logging / Acquisition
- [ ] Cod rulează fără erori (`python src/data_acquisition/...` sau echivalent LabVIEW)
- [ ] Produce minimum 40% date originale din dataset-ul final
- [ ] CSV generat în format compatibil cu preprocesarea din Etapa 3
- [ ] Documentație în `src/data_acquisition/README.md` cu:
  - [ ] Metodă de generare/achiziție explicată
  - [ ] Parametri folosiți (frecvență, durată, zgomot, etc.)
  - [ ] Justificare relevanță date pentru problema voastră
- [ ] Fișiere în `data/generated/` conform structurii

### Modul 2: Neural Network
- [ ] Arhitectură RN definită și documentată în cod (docstring detaliat) - versiunea inițială 
- [ ] README în `src/neural_network/` cu detalii arhitectură curentă

### Modul 3: Web Service / UI
- [ ] Propunere Interfață ce pornește fără erori (comanda de lansare testată)
- [ ] Screenshot demonstrativ în `docs/screenshots/ui_demo.png`
- [ ] README în `src/app/` cu instrucțiuni lansare (comenzi exacte)

---

**Predarea se face prin commit pe GitHub cu mesajul:**  
`"Etapa 4 completă - Arhitectură SIA funcțională"`

**Tag obligatoriu:**  
`git tag -a v0.4-architecture -m "Etapa 4 - Skeleton complet SIA"`


