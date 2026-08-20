# Urdu OCR Project

## Code Saviours Summer Internship 2026

This project is an Urdu Optical Character Recognition (OCR) system that extracts Urdu text from images using a fine-tuned Microsoft TrOCR model.

---

# Why This Project Matters

Urdu handwritten text is difficult for traditional OCR systems because of connected characters, complex ligatures, the Nastaliq writing style, and variations in handwriting.

This project explores the use of transformer-based OCR to recognize Urdu text from images and demonstrates the challenges of applying pretrained OCR models to Urdu script.

---

# Week 1 Progress

* ✅ Google Colab Setup
* ✅ GitHub Repository Created
* ✅ Hugging Face Account Created
* ✅ Project Environment Configured
* ✅ Collected 100+ Urdu Images
* ✅ Created `labels.csv`

---

# Week 2 Progress

* ✅ Image Preprocessing
* ✅ Applied Grayscale Conversion
* ✅ Noise Removal
* ✅ Thresholding (Binarization)
* ✅ Tested OCR using Tesseract
* ✅ Documented OCR Results

---

# Week 3 Progress

* ✅ Expanded Dataset to 200+ Urdu Images
* ✅ Updated `labels.csv`
* ✅ Created Custom PyTorch Dataset Class
* ✅ Split Dataset into Training and Testing Sets
* ✅ Created DataLoaders
* ✅ Successfully Loaded Dataset

---

# Week 4 Progress

* ✅ Loaded Microsoft TrOCR Pretrained Model
* ✅ Configured GPU Runtime in Google Colab
* ✅ Fine-tuned TrOCR on Urdu Dataset
* ✅ Trained Model for 3 Epochs
* ✅ Evaluated Model Performance
* ✅ Saved Fine-tuned Model to Google Drive

## Week 4 Challenges Faced

During model training, the main challenges were:

* ⚠️ **Model Compatibility**
  * TrOCR Base Printed was originally designed for English printed text, making Urdu Nastaliq adaptation difficult.

* ⚠️ **Limited Dataset**
  * The dataset contained around 200 Urdu images, which limited model performance.

* ⚠️ **Limited Training**
  * Due to computational and time constraints, the model was trained for only 3 epochs.

---

# Week 5 Progress

## Build OCR Application and Deployment

* ✅ Created OCR application structure for model inference
* ✅ Prepared deployment files
* ✅ Created Hugging Face Space for project deployment
* ✅ Tested deployment environment
* ✅ Configured project files for online hosting

## Week 5 Deployment Challenges

* ⚠️ **Hugging Face Space Limitations**
  * The available free Space configuration had limitations for Gradio and Docker deployment.

* ⚠️ **Static Environment Limitations**
  * The Static Space environment could not support heavy machine learning libraries such as PyTorch and Transformers.

* ⚠️ **Deployment Adjustment**
  * Alternative deployment approaches were explored to make the OCR project accessible online.

---

# Week 8 Progress

## Project Polishing and Final Preparation

During Week 8, the project was prepared for final submission and presentation.

* ✅ Cleaned and organized the GitHub repository
* ✅ Reviewed project files and folder structure
* ✅ Updated project documentation
* ✅ Added project description and purpose
* ✅ Added model results and training information
* ✅ Added local setup instructions
* ✅ Final project submission

---

# What It Does

The Urdu OCR project takes an Urdu text image as input and attempts to extract the written Urdu text using a fine-tuned Microsoft TrOCR model.

The image is processed and passed through the OCR model, which generates predicted text as output.

---

# How It Works

The project first collects and preprocesses Urdu images by applying techniques such as grayscale conversion, noise removal, and thresholding.

The processed images are then used to fine-tune Microsoft TrOCR on the Urdu dataset.

After training, the model can be used for OCR inference by providing an Urdu image and generating predicted text.

---

# Live Demo

The Urdu OCR project was prepared for deployment on Hugging Face Spaces.

**Hugging Face Space:** (https://huggingface.co/spaces/hadia-tech/Urdu-OCR)

---

# Results

## Training Loss

| Epoch | Average Training Loss |
| ----- | --------------------: |
| 1     |                3.9934 |
| 2     |                2.5148 |
| 3     |                2.4845 |

## Model Accuracy

**0.0%**

The accuracy remained low due to the limited dataset size, limited training epochs, and the difficulty of adapting a pretrained English OCR model to Urdu Nastaliq handwriting.

---

# How to Run Locally

Install the required libraries:

`pip install torch transformers pandas opencv-python pillow datasets accelerate`

Open the relevant Google Colab notebook and run the cells in order.

The project requires the dataset and model files to be available at the paths specified in the notebook.

---

# Folder Structure

Urdu-OCR_Project/

├── data/

│   ├── images/

│   ├── processed/

│   └── labels.csv

├── SI26_Week1_Hadia.ipynb

├── SI26_Week2_Hadia.ipynb

├── SI26_Week3_Hadia.ipynb

├── SI26_Week4_Hadia.ipynb

├── SI26_Week5_Hadia.ipynb

└── README.md

---

# Tools Used

* Google Colab
* GitHub
* Hugging Face
* Hugging Face Transformers
* PyTorch
* OpenCV
* Pandas
* Tesseract OCR

---

# Model Used

* Microsoft TrOCR Base Printed
* VisionEncoderDecoderModel
* TrOCRProcessor
* AdamW Optimizer

---

# Tesseract OCR Results

## Image 80.png

**Output:**

`/ ۷۷ لا ول نل ا`

**Observation:**

The OCR output is inaccurate and several Urdu words were not recognized correctly.

---

## Image 63.png

**Output:**

`ملماول وا سا کا ان بد`

**Observation:**

Some words were partially recognized, but many characters and words are incorrect.

---

## Image 42.png

**Output:**

`و`

**Observation:**

Most of the text was missed. Only one character was detected.

---

## Image 27.png

**Output:**

`ا کی ار روا`

**Observation:**

The recognized text is incomplete and contains recognition errors.

---

## Image 59.png

**Output:**

`نہ اک او ٹیو`

**Observation:**

The OCR result does not accurately match the original handwritten Urdu text.

---

# Why We Need a Better OCR Model

Tesseract struggles to recognize handwritten Urdu because the Urdu Nastaliq script contains connected characters, complex ligatures, overlapping words, and different handwriting styles.

Although preprocessing improves image quality, Tesseract still produces inaccurate results.

To overcome these limitations, Microsoft TrOCR was fine-tuned on a custom Urdu dataset using transfer learning. This approach aims to improve recognition performance on handwritten Urdu text.

---

# Training Results

| Epoch | Average Training Loss |
| ----- | --------------------: |
| 1     |                3.9934 |
| 2     |                2.5148 |
| 3     |                2.4845 |

### Model Accuracy

**0.0%**

---

# Conclusion

This project successfully completed the complete OCR pipeline:

* Dataset collection
* Image preprocessing
* Dataset preparation
* Data loading using PyTorch
* Fine-tuning Microsoft TrOCR
* Model evaluation
* Model saving
* Deployment exploration
* Project documentation and final preparation

The training loss decreased from **3.9934** to **2.4845**, indicating that the model learned from the available training data.

However, the final model accuracy remained **0.0%** because:

* Microsoft TrOCR Base Printed is pretrained for English text.
* The Urdu dataset is relatively small (around 200 images).
* The model was trained for only 3 epochs.
* Urdu Nastaliq script is significantly more complex than English printed text.

Future improvements include collecting a much larger handwritten Urdu dataset, training for more epochs, and using a model specifically designed for Urdu OCR.

---
# Built By

**Hadia Hameed** | **Code Saviours SI-26** | **2026**

---

**Code Saviours Summer Internship 2026**
