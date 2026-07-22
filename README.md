# Urdu OCR Project

## Code Saviours Summer Internship 2026

---

# Week 1 Progress

- ✅ Google Colab Setup
- ✅ GitHub Repository Created
- ✅ Hugging Face Account Created
- ✅ Project Environment Configured
- ✅ Collected 100+ Urdu Images
- ✅ Created `labels.csv`

---

# Week 2 Progress

- ✅ Image Preprocessing
- ✅ Applied Grayscale Conversion
- ✅ Noise Removal
- ✅ Thresholding (Binarization)
- ✅ Tested OCR using Tesseract
- ✅ Documented OCR Results

---

# Week 3 Progress

- ✅ Expanded Dataset to 200+ Urdu Images
- ✅ Updated `labels.csv`
- ✅ Created Custom PyTorch Dataset Class
- ✅ Split Dataset into Training and Testing Sets
- ✅ Created DataLoaders
- ✅ Successfully Loaded Dataset

---

# Week 4 Progress

- ✅ Loaded Microsoft TrOCR Pretrained Model
- ✅ Configured GPU Runtime
- ✅ Fine-tuned TrOCR on Urdu Dataset
- ✅ Trained Model for 3 Epochs
- ✅ Evaluated Model
- ✅ Saved Model to Google Drive

---

# Folder Structure

```text
Urdu-OCR_Project/
│── data/
│   ├── images/
│   ├── processed/
│   └── labels.csv
│
│── SI26_Week1_Hadia.ipynb
│── SI26_Week2_Hadia.ipynb
│── SI26_Week3_Hadia.ipynb
│── SI26_Week4_Hadia.ipynb
│── README.md
```

---

# Tools Used

- Google Colab
- GitHub
- Hugging Face Transformers
- PyTorch
- OpenCV
- Pandas
- Tesseract OCR

---

# Model Used

- Microsoft TrOCR Base Printed
- VisionEncoderDecoderModel
- TrOCRProcessor
- AdamW Optimizer

---

# Tesseract OCR Results

## Image 80.png

**Output**

```text
/ ۷۷ لا ول نل ا
```

**Observation**

The OCR output is inaccurate and several Urdu words were not recognized correctly.

---

## Image 63.png

**Output**

```text
ملماول وا سا کا ان بد
```

**Observation**

Some words were partially recognized, but many characters and words are incorrect.

---

## Image 42.png

**Output**

```text
و
```

**Observation**

Most of the text was missed. Only one character was detected.

---

## Image 27.png

**Output**

```text
ا کی ار روا
```

**Observation**

The recognized text is incomplete and contains recognition errors.

---

## Image 59.png

**Output**

```text
نہ اک او ٹیو
```

**Observation**

The OCR result does not accurately match the original handwritten Urdu text.

---

# Why We Need a Better OCR Model

Tesseract struggles to recognize handwritten Urdu because the Urdu Nastaliq script contains connected characters, complex ligatures, overlapping words, and different handwriting styles. Although preprocessing improves image quality, Tesseract still produces inaccurate results.

To overcome these limitations, Microsoft TrOCR was fine-tuned on a custom Urdu dataset using transfer learning. This approach aims to improve recognition performance on handwritten Urdu text.

---

# Training Results

| Epoch | Average Training Loss |
|-------|----------------------:|
| 1 | 3.9934 |
| 2 | 2.5148 |
| 3 | 2.4845 |

### Model Accuracy

**0.0%**

---

# Conclusion

This project successfully completed the complete OCR pipeline:

- Dataset collection
- Image preprocessing
- Dataset preparation
- Data loading using PyTorch
- Fine-tuning Microsoft TrOCR
- Model evaluation
- Model saving

The training loss decreased from **3.9934** to **2.4845**, indicating that the model learned from the available training data.

However, the final model accuracy remained **0.0%** because:

- Microsoft TrOCR Base Printed is pretrained for English text.
- The Urdu dataset is relatively small (around 200 images).
- The model was trained for only 3 epochs.
- Urdu Nastaliq script is significantly more complex than English printed text.

Future improvements include collecting a much larger handwritten Urdu dataset, training for more epochs, and using a model specifically designed for Urdu OCR.

---

**Code Saviours Summer Internship 2026**
