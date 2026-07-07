# Urdu OCR Project

## Code Saviours Summer Internship 2026

### Week 1 Progress

- ✅ Google Colab Setup
- ✅ GitHub Repository Created
- ✅ Hugging Face Account Created
- ✅ Project Environment Configured
- ✅ Collected 100+ Urdu Images
- ✅ Created `labels.csv`

---

## Week 2 Progress

- ✅ Image Preprocessing
- ✅ Applied Grayscale Conversion
- ✅ Noise Removal
- ✅ Thresholding (Binarization)
- ✅ Tested OCR using Tesseract
- ✅ Documented OCR Results

---

## Folder Structure

```text
Urdu-OCR_Project/
│── data/
│   ├── images/
│   ├── processed/
│   └── labels.csv
│── SI26_Week1_Hadia.ipynb
│── SI26_Week2_Hadia.ipynb
│── README.md
```

---

## Tools Used

- Google Colab
- GitHub
- Hugging Face
- OpenCV
- Tesseract OCR
- Pandas

---

## Why We Need a Better Model

Tesseract struggles to recognize handwritten Urdu because the Urdu Nastaliq script contains connected characters, complex ligatures, overlapping words, and different handwriting styles. Although image preprocessing improves image quality, Tesseract still produces inaccurate results. This highlights the need for a dedicated machine learning OCR model trained specifically for handwritten Urdu text.

---

## Tesseract OCR Results

### Image 80.png
**Output:**
```
/ ۷۷ لا ول نل ا
```

**Observation:** The OCR output is inaccurate and several Urdu words were not recognized correctly.

### Image 63.png
**Output:**
```
ملماول وا سا کا ان بد
```

**Observation:** Some words were partially recognized, but many characters and words are incorrect.

### Image 42.png
**Output:**
```
و
```

**Observation:** Most of the text was missed. Only one character was detected.

### Image 27.png
**Output:**
```
ا کی ار روا
```

**Observation:** The recognized text is incomplete and contains recognition errors.

### Image 59.png
**Output:**
```
نہ اک او ٹیو
```

**Observation:** The OCR result does not accurately match the original handwritten Urdu text.

---

## Conclusion

The preprocessing step successfully improved the image quality, but Tesseract OCR was unable to accurately recognize handwritten Urdu text. These results demonstrate the limitations of existing OCR tools and the need for a specialized OCR model trained on handwritten Urdu.
