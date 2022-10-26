import streamlit as st
import pandas as pd
from pandas_datareader import wb

st.set_page_config(page_title='API', page_icon=':money_with_wings:', layout='centered')
st.title('Datos del Banco Mundial')

# Colocamos el codigo de identificación de cada indicador
codigo = st.text_input('Coloca el codigo de identificación:', value='NV.AGR.TOTL.ZS')
data = wb.download(indicator=codigo, country="all", start=1991, end=2021) 
data = data.reset_index()

# Creamos el DataFrame Final (Es el que va a recibir los cambios)
dataFinal = pd.DataFrame(data)

# Cantidad de columnas 
numeroColumnas = dataFinal.shape[1]
st.sidebar.text('Cantidad de columnas')
st.sidebar.success(numeroColumnas)

# Cantidad de filas 
numeroFilas = dataFinal.shape[0]
st.sidebar.text('Cantidad de filas')
st.sidebar.success(numeroFilas)

# Nombre de cada columna
nombreColumnas = list(dataFinal.columns)
columnaSeleccionada = st.sidebar.selectbox('Nombre de las columnas', nombreColumnas)

# Total de valores nulos
st.sidebar.text('Valores Nulos')
valoresNulos = dataFinal[columnaSeleccionada].isnull().sum()
if valoresNulos > 0:
    st.sidebar.success(valoresNulos)
else:
    st.sidebar.warning('No posee valores NULOS')

# Descargar DataSets
a = dataFinal.to_csv()
if st.sidebar.download_button(label='Descargar', data=a, file_name='archivo.csv', mime='csv'):
    st.sidebar.success('Descarga exitosa.')


info = ["Primeros 10 valores", "Descripción de los datos", "Descripción por país"]
seleccion = st.selectbox('Información del DataSets', info)



if seleccion == "Primeros 10 valores":
    st.checkbox("Expandir contenedor", value=False, key="use_container_width")
    df = dataFinal.head(10)
    st.dataframe(df, use_container_width=st.session_state.use_container_width)
elif seleccion == "Descripción de los datos":
    st.checkbox("Expandir contenedor", value=False, key="use_container_width")
    des = dataFinal.describe()
    st.dataframe(des, use_container_width=st.session_state.use_container_width)
elif seleccion == "Descripción por país":
    paises = list(dataFinal['country'].unique())
    seleccionPais = st.selectbox('Seleccionar País:', paises)
    st.checkbox("Expandir contenedor", value=False, key="use_container_width")
    pais = dataFinal[dataFinal['country'] == seleccionPais]
    st.dataframe(pais, use_container_width=st.session_state.use_container_width)
