import streamlit as st
from image_classification import classify_image

# Set the title
st.title("Image Classification App")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Save the uploaded image to a file
    with open("uploaded_image.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
    
    # Classify the uploaded image
    class_name, confidence_score = classify_image("uploaded_image.jpg")
    
    # Display the results
    st.write(f"Class: {class_name}")
    st.write(f"Confidence Score: {confidence_score}")
