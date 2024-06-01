import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np


# Function to load the EfficientNet model
@st.cache(allow_output_mutation=True)
def load_efficientnet_model():
    model = load_model('efficientnet_model.h5')
    return model


# Function to preprocess the uploaded image
def preprocess_image(image):
    image = image.resize((224, 224))
    image = np.array(image)
    image = image / 255.0  # Rescale the image
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image


# Class labels (Replace these with your actual class names)
class_names = ['Aipan Art (Uttarakhand)', 'Assamese Miniature Painting (Assam)', 'Basholi Painting (Jammu and Kashmir)',
               'Bhil Painting (Madhya Pradesh)', 'Chamba Rumal (Himachal Pradesh)', 'Cheriyal Scroll Painting (Telangana)',
               'Dokra Art(West Bengal)', 'Gond Painting (Madhya Pradesh)', 'Kalamkari Painting (Andra Pradesh and Telangana)',
               'Kalighat Painting (West Bengal)', 'Kangra Painting (Himachal Pradesh)', 'Kerala Mural Painting (Kerala)',
               'Kondapalli Bommallu (Andra Pradesh)', 'Kutch Lippan Art (Gujarat)', 'Leather Puppet Art (Andra Pradesh)',
               'Madhubani Painting (Bihar)', 'Mandala Art', 'Mandana Art (Rajasthan)', 'Mata Ni Pachedi (Gujarat)',
               'Meenakari Painting (Rajasthan)', 'Mughal Paintings', 'Mysore Ganjifa Art (Karnataka)', 'Pattachitra Painting (Odisha and Bengal)',
               'Patua Painting (West Bengal)', 'Pichwai Painting (Rajasthan)', 'Rajasthani Miniature Painting (Rajasthan)', 'Rogan Art from Kutch (Gujarat)',
               'Sohrai Art (Jharkhand)', 'Tikuli Art (Bihar)', 'Warli Folk Painting (Maharashtra)']


# Streamlit UI
st.title("Folk Art Image Classification")
st.write("Upload an image of folk art, and the model will predict its category.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load and preprocess the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    model = load_efficientnet_model()
    processed_image = preprocess_image(image)

    # Make prediction
    predictions = model.predict(processed_image)
    predicted_class = np.argmax(predictions[0])
    confidence = np.max(predictions[0])

    st.write(f"Predicted Class: {class_names[predicted_class]}")
    st.write(f"Confidence: {confidence:.2f}")
