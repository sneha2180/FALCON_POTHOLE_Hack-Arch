# importing dependencies
import streamlit as st
from PIL import Image
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import smtplib
import ssl
import random
import imghdr
from email.message import EmailMessage
import os

# Load Images
@st.cache
def load_image(img_file):
    img = Image.open(img_file)
    return img


st.title('Pothole Detection')
st.subheader('By Team Resonate')
img = st.file_uploader('Upload an Image file',type = ['png','jpeg','jpg'])

if img is not None :
    # see details
    # st.write({"Filename":img.name})
    st.image(load_image(img))
    if st.button("Predict"):
        ctx = ssl.create_default_context()

        password = os.environ["PASSWORD"]   # Your app password goes here
        model = load_model('keras_model-hackatarch.h5')
        # Create the array of the right shape to feed into the keras model
        # The 'length' or number of images you can put into the array is
        # determined by the first position in the shape tuple, in this case 1.
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        # Replace this with the path to your image
        image = Image.open(img)

        #resize the image to a 224x224 with the same strategy as in TM2:
        #resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)

        #turn the image into a numpy array
        image_array = np.asarray(image)

        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

        # Load the image into the array
        data[0] = normalized_image_array

        # run the inference
        result = model.predict(data)
 
        print("="*20)
        print(result)
        print("="*20)
        print("result[0]: "+str(result[0]))
        print("result[0][0]: "+str(result[0][0]))
        print("result[0][1]: "+str(result[0][1]))

        if result[0][0] > result[0][1]:
            prediction = 'pothole'
        else:
            prediction = 'normal'
        print(f"Prediction: {prediction}")
        st.subheader(f"Prediction: {prediction}")


        #! sends mail
        if result[0][0] >= 0.6:
            Sender_Email = os.environ["SENDER_MAIL"]
            Reciever_Email = os.environ["RECIEVER_MAIL"]
            newMessage = EmailMessage()                         
            newMessage['Subject'] = "𝐏𝐨𝐭𝐡𝐨𝐥𝐞 𝐃𝐞𝐭𝐞𝐜𝐭𝐞𝐝" 
            newMessage['From'] = Sender_Email                   
            newMessage['To'] = Reciever_Email
            location = ["Ollur","Viyyur","Kurukkanchery","Mundoor"]
            current_loc = random.choice(location)                   
            newMessage.set_content(f"Pothole Detected with severity more than 80% at {current_loc}") 
            image_data = img.read()
            image_type = img.type.split('/')[1]
            image_name = img.name

            print(f"1: {image_data}",f"2: {image_type}",f"3: {image_name}")
            newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(Sender_Email, password)              
                smtp.send_message(newMessage)
                print("Mail sent ✅")
                st.subheader("Mail sent ✅")
