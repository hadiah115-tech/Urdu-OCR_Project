import gradio as gr
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch
import os

# Load model directly from Hugging Face Hub
model_path = "hadia-tech/urdu-ocr-si26-hadia"
processor = TrOCRProcessor.from_pretrained(model_path)
model = VisionEncoderDecoderModel.from_pretrained(model_path)
model.eval()

def extract_urdu_text(image):
    """Takes an image, returns extracted Urdu text."""
    if image is None:
        return 'Please upload an image'
    pixel_values = processor(image, return_tensors='pt').pixel_values
    with torch.no_grad():
        generated_ids = model.generate(pixel_values)
    text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return text if text else 'Could not extract text from this image'

interface = gr.Interface(
    fn=extract_urdu_text,
    inputs=gr.Image(type='pil', label='Upload Urdu Image'),
    outputs=gr.Textbox(label='Extracted Urdu Text'),
    title='Urdu OCR -- Code Saviours SI-26',
    description='Upload an image containing Urdu text and get the extracted text.',
    examples=[]
)

interface.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))
