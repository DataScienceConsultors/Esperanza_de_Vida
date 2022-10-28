import streamlit as st
from conexion import miConexion

# Paises elegidos
paises = ['Argentina','Chile','Brazil','Peru','China','Bolivia','Colombia','Canada' ,'United States','Mexico','Spain', 'Italy','Austria','Finland','Sweden','Norway','Russian Federation','Japan','India','Syrian Arab Republic','Australia','New Zealand','Nigeria','Morocco','South Africa','Senegal','Zimbabwe','Germany' ,'Angola', 'Uruguay']


# Metadata
st.set_page_config(page_title='Dashboard', layout='centered')


# Titulo de la app
st.title('Información sobre el País')


# Se selecciona el país
paisSeleccionado = st.selectbox('Nombre del País: ', paises)
st.write(f'Descripción del PBI y la Esperanza de vida en:  {paisSeleccionado}')

# Paises
cur = miConexion.cursor()
if paisSeleccionado == 'Argentina':
    pais = 0
elif paisSeleccionado == 'Chile':
    pais = 1
elif paisSeleccionado == 'Brazil':
    pais = 2
elif paisSeleccionado == 'Peru':
    pais = 3
elif paisSeleccionado == 'Bolivia':
    pais = 4
elif paisSeleccionado == 'Colombia':
    pais = 5
elif paisSeleccionado == 'Uruguay':
    pais = 6
elif paisSeleccionado == 'United States':
    pais = 7
elif paisSeleccionado == 'Mexico':
    pais = 8
elif paisSeleccionado == 'Canada':
    pais = 9
elif paisSeleccionado == 'China':
    pais = 10
elif paisSeleccionado == 'Russian Federation':
    pais = 11
elif paisSeleccionado == 'Japan':
    pais = 12
elif paisSeleccionado == 'India':
    pais = 13
elif paisSeleccionado == 'Syrian Arab Republic':
    pais = 14
elif paisSeleccionado == 'Nigeria':
    pais = 15
elif paisSeleccionado == 'Morocco':
    pais = 16
elif paisSeleccionado == 'South Africa':
    pais = 17
elif paisSeleccionado == 'Senegal':
    pais = 18
elif paisSeleccionado == 'Zimbabwe':
    pais = 19
elif paisSeleccionado == 'Angola':
    pais = 20
elif paisSeleccionado == 'Spain':
    pais = 21
elif paisSeleccionado == 'Italy':
    pais = 22
elif paisSeleccionado == 'Austria':
    pais = 23
elif paisSeleccionado == 'Finland':
    pais = 24
elif paisSeleccionado == 'Sweden':
    pais = 25
elif paisSeleccionado == 'Norway':
    pais = 26
elif paisSeleccionado == 'Germany':
    pais = 27
elif paisSeleccionado == 'Australia':
    pais = 28
elif paisSeleccionado == 'New Zealand':
    pais = 29

	

# Se consulta el PBI en la base de datos
cur.execute(f"SELECT PBI_per_capita FROM sys.tb_esperanza WHERE country = {pais} limit 2;")
pbi  = cur.fetchall()

# Se consulta la esperanza de vida en la base de datos
cur.execute(f"SELECT esperanza_vida_nacer_total FROM sys.tb_esperanza WHERE country = {pais} limit 2;")
year  = cur.fetchall()


# Como lo devuelve en forma de topla, se selecciona el numero
mesActualPbi = pbi[0][0]
mesAnteriorPbi = pbi[1][0]
mesActualYear = year[0][0]
mesAnteriorYear = year[1][0]


# Se crean las columnas
col1, col2 = st.columns(2)

with col1:
    st.metric(
        label='PBI del País',
        value= round(mesActualPbi,2),
        delta= round(-((mesAnteriorPbi-mesActualPbi)/mesAnteriorPbi)*100,2)
    )
with col2:
    st.metric(
        label='Esperanza de Vida (Años)',
        value= round(mesActualYear),
        delta= round(-((mesAnteriorYear-mesActualYear)/mesAnteriorYear)*100,2)
    )

# Se consulta la Población total en la base de datos
cur.execute(f"SELECT desempleo_total FROM sys.tb_esperanza WHERE country = {pais} limit 2;")
poblacion  = cur.fetchall()

# Se consulta el incremento de la inflación en la base de datos
cur.execute(f"SELECT crecimiento_masa_monetaria_inflacion FROM sys.tb_esperanza WHERE country = {pais} limit 2;")
inflacion  = cur.fetchall()


# Como lo devuelve en forma de topla, se selecciona el numero
mesActualPoblacion = poblacion[0][0]
mesAnteriorPoblacion = poblacion[1][0]
mesActualinflacion = inflacion[0][0]
mesAnteriorinflacion = inflacion[1][0]


# Se crean las columnas
col11, col22 = st.columns(2)

with col11:
    st.metric(
        label='Desempleo total de la Población (%)',
        value= round(mesActualPoblacion, 2),
        delta= round(-((mesAnteriorPoblacion-mesActualPoblacion)/mesAnteriorPoblacion)*100,2)
    )
with col22:
    st.metric(
        label='Incremento de la Inflación (%)',
        value= round(mesActualinflacion, 2),
        delta= round(-((mesAnteriorinflacion-mesActualinflacion)/mesAnteriorinflacion)*100,2)
    )

    