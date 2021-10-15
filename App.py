import streamlit as st 
import pandas as pd
import pickle
import time
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score, accuracy_score 

st.write("# Fraud Detection Data App")
st.write("Este aplicativo realiza predições de fraude, com base nos dados inseridos.")

d1 = st.sidebar.slider("D1",-5.64,2.45,0.5)
d2 = st.sidebar.slider("D2",-5.64,2.45,0.5)
d3 = st.sidebar.slider("D3",-5.64,2.45,0.5)
d4 = st.sidebar.slider("D4",-5.64,2.45,0.5)
d5 = st.sidebar.slider("D5",-5.64,2.45,0.5)
d6 = st.sidebar.slider("D6",-5.64,2.45,0.5)
d7 = st.sidebar.slider("D7",-5.64,2.45,0.5)
d8 = st.sidebar.slider("D8",-5.64,2.45,0.5)
d9 = st.sidebar.slider("D9",-5.64,2.45,0.5)
d10 = st.sidebar.slider("D10",-5.64,2.45,0.5)
d11 = st.sidebar.slider("D11",-5.64,2.45,0.5)
d12 = st.sidebar.slider("D12",-5.64,2.45,0.5)
d13 = st.sidebar.slider("D13",-5.64,2.45,0.5)
d14 = st.sidebar.slider("D14",-5.64,2.45,0.5)
d15 = st.sidebar.slider("D15",-5.64,2.45,0.5)
d16 = st.sidebar.slider("D16",-5.64,2.45,0.5)
d17 = st.sidebar.slider("D17",-5.64,2.45,0.5)
d18 = st.sidebar.slider("D18",-5.64,2.45,0.5)
d19 = st.sidebar.slider("D19",-5.64,2.45,0.5)
d20 = st.sidebar.slider("D20",-5.64,2.45,0.5)
d21 = st.sidebar.slider("D21",-5.64,2.45,0.5)
d22 = st.sidebar.slider("D22",-5.64,2.45,0.5)
d23 = st.sidebar.slider("D23",-5.64,2.45,0.5)
d24 = st.sidebar.slider("D24",-5.64,2.45,0.5)
d25 = st.sidebar.slider("D25",-5.64,2.45,0.5)
d26 = st.sidebar.slider("D26",-5.64,2.45,0.5)
d27 = st.sidebar.slider("D27",-5.64,2.45,0.5)
d28 = st.sidebar.slider("D28",-5.64,2.45,0.5)
time = st.sidebar.slider("Tempo",-5.64,2.45,0.5)
amount = st.sidebar.slider("Valor",-5.64,2.45,0.5)

modelo = open("dump.pkl", "rb")
lr = pickle.load(modelo)
modelo.close()

dados = {
	"D1": d1,  
	"D2": d2, 
	"D3": d3,
	"D4": d4,
	"D5": d5,
	"D6": d6,
	"D7": d7,
	"D8": d8,
	"D9": d9,
	"D10": d10,
	"D11": d11,
	"D12": d12,
	"D13": d13,
	"D14": d14,
	"D15": d15,
	"D16": d16,
	"D17": d17,
	"D18": d18,
	"D19": d19,
	"D20": d20,
	"D21": d21,
	"D22": d22,
	"D23": d23,
	"D24": d24,
	"D25": d25,
	"D26": d26,
	"D27": d27,
	"D28": d28,
	"Tempo": time,
  	"Valor": amount
}

st.write("### Dados de Entrada")
entrada = pd.DataFrame(dados, index=[0])
st.write(entrada)

my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)

st.write("### Resultado da Análise")
predicao = lr.predict(entrada)
#st.write(predicao)

if(predicao == 0):
	st.success("NÃO FRAUDE")
elif(predicao == 1):
	st.error("FRAUDE")

with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')



