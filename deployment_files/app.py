import streamlit as st
from load_css import local_css
from PIL import Image
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
from torchvision import models
import matplotlib.pyplot as plt
import io
from PIL import Image
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from image_classification import get_prediction
from plot_probs import plot_solution

local_css("style.css")

t = "<body> Welcome To <span class = 'bigcoral'> ACAA </span class = 'bigcoral> <br> \
<span class = 'littleteal'> the <span class = 'bigcoral'>A</span class = 'bigcoral>sphalt \
    <span class = 'bigcoral'>C</span class = 'bigcoral>ondition \
        <span class = 'bigcoral'>A</span class = 'bigcoral>ssessment \
            <span class = 'bigcoral'>A</span class = 'bigcoral>ssistant! </span class ='littleteal'> </body>"

st.markdown(t, unsafe_allow_html = True)

t = " <body>  <span class ='littleteal'> get started by uploading an image </span class ='littleteal'>  </body> "

st.markdown(t, unsafe_allow_html = True)

file_up = st.file_uploader("Please upload and image file", type = ["jpg"])

info = "<body> <span class = 'blue' > DETECT AND IDENTIFY PAVEMENT DEFICIENCIES <br> </span class = 'blue'>  <br> \
     </body>"

st.markdown(info, unsafe_allow_html = True)
button_text = "<body> Inspect </body>"

if file_up is not None:
    image = Image.open(file_up)
    st.image(image, use_column_width=True)
    if st.button("Predict Condition"):
        st.write("")
        y_hat, label, outputs = get_prediction(file_up)
        answer = "<body> <span class = bigcoral> Condition Prediction is: </ span class = bigcoral>"
        formatted_label =  label + "</body>" 
        answer = answer + formatted_label
        st.write("")
        st.markdown(answer, unsafe_allow_html=True)

        if y_hat == 0 or y_hat == 2 or y_hat ==3:
            info_1 = "For further information on potential causes and mitigation strategies please refer to the links below: "
            info_2 = "[OHMPA's ABC Series](http://www.onasphalt.org/publications/ohmpa_publications/abc_series.html)"
            info_3 = "[Asphalt Institute - Pavement Distress Summary](http://www.asphaltinstitute.org/engineering/maintenance-and-rehabilitation/pavement-distress-summary/)"
            st.markdown(info_1)
            st.markdown(info_2)
            st.markdown(info_3)
        elif y_hat == 1:
            info = "Continue to complete regular inspections and maintentence to maintain pavement quality."
            st.markdown(info)
        
        info = "<body> <span class = blue> See Confidence Information Below </span class = blue> <body>"
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.markdown(info, unsafe_allow_html = True)
        st.write("")
        st.write("")
        st.write("")
        df = plot_solution(outputs)
        st.write(df)
