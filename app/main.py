import streamlit as st
import pandas as pd
from PIL import Image
import subprocess
import os
import base64
import pickle

## model descriptors

def desc_calc():
    bashCommand = "java -Xms1G -Xmx1G -Djava.awt.headless=true -jar ./PaDEL-Descriptor/PaDEL-Descriptor.jar -removesalt -standardizenitro -fingerprints -descriptortypes ./PaDEL-Descriptor/PubchemFingerprinter.xml -dir ./ -file descriptors_output.csv"
    process = subprocess.Popen(bashCommand.split(),stdout=subprocess.PIPE)
    output,error = process.communicate()
    os.remove("molecule.smi")

def file_download(df):
    csv = df.to_csv
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="prediction.csv">Download Predictions</a>'
    return href

# Model building
def build_model(input_data):
    # Reads in saved regression model
    load_model = pickle.load(open('acetylcholinesterase_model.pkl', 'rb'))
    # Apply model to make predictions
    prediction = load_model.predict(input_data)
    st.header('**Prediction output**')
    prediction_output = pd.Series(prediction, name='pIC50')
    molecule_name = pd.Series(load_data[1], name='molecule_name')
    df = pd.concat([molecule_name, prediction_output], axis=1)
    st.write(df)
    st.markdown(filedownload(df), unsafe_allow_html=True)

image = Image.open('logo.png')

st.image(image,use_column_width=True)

st.markdown("""
# Bioactivity Prediction App

This app allows you to predict the bioactivity towards inhibting the `Acetylcholinesterase` enzyme. `Acetylcholinesterase` is a drug target for Alzheimer's disease.

**Credits**
- App built in `Python` + `Streamlit` by Anish 
- Descriptor calculated using [PaDEL-Descriptor](http://www.yapcwsoft.com/dd/padeldescriptor/) [[Read the Paper]](https://doi.org/10.1002/jcc.21707).
---
""")

with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input file", type=['txt'])
    st.sidebar.markdown("""
[Example input file](https://raw.githubusercontent.com/dataprofessor/bioactivity-prediction-app/main/example_acetylcholinesterase.txt)
""")

if st.sidebar.button("Predict"):
    load_df = pd.read_csv(uploaded_file,sep=" ",header=None)
    load_df.to_csv("molecule.smi",sep="\t",header=False,index=False)

    st.header('**Original input data**')
    st.write(load_df)

    with st.spinner("Calculating Descriptors"):
        desc_calc()

    st.header('**Calculated molecular descriptors**')
    desc = pd.read_csv('descriptors_output.csv')
    st.write(desc)
    st.write(desc.shape)

    st.header("*** Subset of selected fingerprints chosen from previous models ***")
    Xlist = list(pd.read_csv("descriptors_output.csv").column)
    subset = desc[Xlist]
    st.write(subset)
    st.write(subset.shape)


    build_model(subset)
else:
    st.info("Upload input data in the sidebar")

