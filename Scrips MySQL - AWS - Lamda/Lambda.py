# Importamos librerias
from pandas_datareader import wb
import pandas as pd 
import mysql.connector
import sqlalchemy


#credenciale smysql 
database_username = 'admin'
database_password = '123456789'
database_ip       = 'database-1.cmmt68xsoykx.us-east-1.rds.amazonaws.com'
database_name     = 'Tabla_prueba'



#creacion de paices 
americaSur = ['Argentina','Chile','Brazil','Peru','Bolivia','Colombia', 'Uruguay'] # 7
americaNorte = ['United States','Mexico','Canada'] # 3
asia = ['China','Russian Federation','Japan','India','Syrian Arab Republic'] # 5
africa = ['Nigeria','Morocco','South Africa','Senegal','Zimbabwe','Angola'] # 6
europa = ['Spain', 'Italy','Austria','Finland','Sweden','Norway','Germany'] # 7
oceania = ['Australia','New Zealand'] # 2

paises = americaSur+americaNorte+asia+africa+europa+oceania

#creacion de continenetes 
continentes_ = ["America del Sur",'America del Norte','Asia','Africa','Europa','Oceania']

#creamos nuestra tabla continetes 
id_continente=[0,1,2,3,4,5]
df_continentes = pd.DataFrame({"id_continente":id_continente,"continentes":continentes_}) 
df_continentes=df_continentes.set_index("id_continente")

#creamos nuestra tabla paices  
catidad_paices = len(paises)
id_continent = [0,0,0,0,0,0,0,1,1,1,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,4,5,5]
id_paises =list(range(0, catidad_paices))
df_paises = pd.DataFrame({"id_paises":id_paises,"country":paises,"id_continente":id_continent}) 
df_paises=df_paises.set_index("id_paises")


# creamos nuestra tabla años 
años = list(range(1990, 2020+1))
df_años = pd.DataFrame({"year":años}) 
df_años=df_años.set_index("year")

data1 =  wb.download(indicator="SL.UEM.TOTL.FE.ZS", country="all", start=1990 ,  end=2020)
data1 = data1.reset_index()
data1.columns=['country','year','Desempleo_mujeres']
data1 = data1.loc[data1['country'].isin(paises)]  
data1 = data1.fillna(method='ffill')



data2 =  wb.download(indicator="SL.UEM.1524.FE.ZS", country="all", start=1990 ,  end=2020)
data2 = data2.reset_index()
data2.columns=['country','year','Desempleo_mujeres_jóvenes_14_24_años']
data2 = data2.loc[data2['country'].isin(paises)] 
data2 = data2.fillna(method='ffill')

#SL.UEM.1524.MA.ZS
data3=  wb.download(indicator="SL.UEM.1524.MA.ZS", country="all", start=1990 ,  end=2020)
data3 = data3.reset_index()
data3.columns=['country','year','Desempleo_varones_jovenes_15_24_años']
data3 = data3.loc[data3['country'].isin(paises)]  
data3 = data3.fillna(method='ffill')


data4=  wb.download(indicator="SL.TLF.TOTL.IN", country="all", start=1990 ,  end=2020)
data4 = data4.reset_index()
data4.columns=['country','year','Desempleo_Población_activa_total']
data4 = data4.loc[data4['country'].isin(paises)]  

#SP.DYN.LE00.FE.IN
data5 =  wb.download(indicator="SP.DYN.LE00.FE.IN", country="all", start=1990 ,  end=2020)
data5 = data5.reset_index()
data5.columns=['country','year','esperanza_vida_nacer_Mujeres']
data5 = data5.loc[data5['country'].isin(paises)] 


#SP.DYN.LE00.MA.IN
data6 =  wb.download(indicator="SP.DYN.LE00.MA.IN", country="all", start=1990 ,  end=2020)
data6 = data6.reset_index()
data6.columns=['country','year','esperanza_vida_nacer_Varones']
data6 = data6.loc[data6['country'].isin(paises)] 


#SP.DYN.LE00.IN
data7 =  wb.download(indicator="SP.DYN.LE00.IN", country="all", start=1990 ,  end=2020)
data7 = data7.reset_index()
data7.columns=['country','year','esperanza_vida_nacer_total']
data7 = data7.loc[data7['country'].isin(paises)] 

#SP.POP.TOTL
data8 =  wb.download(indicator="SP.POP.TOTL", country="all", start=1990 ,  end=2020)
data8 = data8.reset_index()
data8.columns=['country','year','poblacion_total_salud']
data8 = data8.loc[data8['country'].isin(paises)]  


#SP.DYN.TFRT.IN
data10 =  wb.download(indicator="SP.DYN.TFRT.IN", country="all", start=1990 ,  end=2020)
data10 = data10.reset_index()
data10.columns=['country','year','fertilidad_mujeres']
data10 = data10.loc[data10['country'].isin(paises)] 



data12 =  wb.download(indicator="SP.DYN.IMRT.IN", country="all", start=1990 ,  end=2020)
data12 = data12.reset_index()
data12.columns=['country','year','tasa_mortalidad_bebes']
data12 = data12.loc[data12['country'].isin(paises)] 


#FM.LBL.BMNY.ZG
data13 =  wb.download(indicator="FM.LBL.BMNY.ZG", country="all", start=1990 ,  end=2020)
data13 = data13.reset_index()
data13.columns=['country','year','crecimiento_masa_monetaria_inflacion']
data13 = data13.loc[data13['country'].isin(paises)]  
data13.loc[(data13.year == '2018') & (data13.country == 'Argentina'), "crecimiento_masa_monetaria_inflacion"]  = 47.65
data13.loc[(data13.year == '2019') & (data13.country == 'Argentina'), "crecimiento_masa_monetaria_inflacion"]  = 53.83
data13.loc[(data13.year == '2020') & (data13.country == 'Argentina'), "crecimiento_masa_monetaria_inflacion"]  = 36.15
data13 = data13.fillna(method='ffill')

data14 = wb.download(indicator='SH.DYN.MORT', country="all", start=1990 ,  end=2020)  # tasa de mortalidad menores de 5 anios (cada mil)
data14 = data14.reset_index()
data14.columns=['country','year','tasa_mort_5anios_cada_mil']
data14 = data14.loc[data14['country'].isin(paises)]  


data15= wb.download(indicator='SP.POP.GROW', country="all", start=1990 ,  end=2020)  # Tasa de crecimiento
data15 = data15.reset_index()
data15.columns=['country','year','crecimiento_poblacion']
data15 = data15.loc[data15['country'].isin(paises)]  
data15 = data15.fillna(method='ffill')



data18 = wb.download(indicator='SP.ADO.TFRT', country="all", start=1990 ,  end=2020)  # Tasa de fertilidad, nacimientos por cada 1000 mujeres entre 15 y 19 anios
data18 = data18.reset_index()
data18.columns=['country','year','Tasa_fertilidad_mujeres']
data18 = data18.loc[data18['country'].isin(paises)] 


data20 = wb.download(indicator='NY.GDP.PCAP.CD', country="all", start=1990, end=2020)
data20 = data20.reset_index()
data20.columns=['country','year','PBI_per_capita']
data20 = data20.loc[data20['country'].isin(paises)]
data20 = data20.fillna(method='bfill')


data21 = wb.download(indicator='SL.UEM.TOTL.ZS', country="all", start=1990 ,  end=2020)
data21 = data21.reset_index()
data21.columns=['country','year','desempleo_total']
data21 = data21.loc[data21['country'].isin(paises)]
data21 = data21.fillna(method='ffill')


data22 = wb.download(indicator='SH.STA.TRAF.P5', country="all", start=1990, end=2020)
data22 = data22.reset_index()
data22.columns=['country','year','mortalidad_accidentes_transito']
data22 = data22.loc[data22['country'].isin(paises)]
data22 = data22.fillna(method='bfill')


# EG.ELC.ACCS.ZS = Acceso a la electricidad (% de población)
data23 =  wb.download(indicator="EG.USE.ELEC.KH.PC",country="all",start=1990 ,end=2020)
data23 = data23.reset_index()
data23.columns=["country","year","acceso_a_la_electricidad"]
data23 = data23.loc[data23["country"].isin(paises)]
data23 = data23.fillna(method='bfill')

# Inscripción escolar, nivel primario (% bruto)
data26 =  wb.download(indicator="SE.PRM.ENRR", country="all", start=1990 ,  end=2020)
data26 = data26.reset_index()
data26.columns=['country','year','Inscripción_escolar_nivel_primario']
data26 = data26.loc[data26['country'].isin(paises)] 
data26 = data26.fillna(data26['Inscripción_escolar_nivel_primario'].mean())


# Inscripción escolar, nivel secundaria (% bruto)
data27 =  wb.download(indicator="SE.SEC.ENRR", country="all", start=1990 ,  end=2020)
data27 = data27.reset_index()
data27.columns=['country','year','Inscripción_escolar_nivel_secundaria']
data27 = data27.loc[data27['country'].isin(paises)] 
data27 = data27.fillna(data27['Inscripción_escolar_nivel_secundaria'].mean())


# Inscripción escolar, nivel terciario (% bruto)



# Inscripción escolar, nivel terciario (% bruto)
data28 =  wb.download(indicator="SE.TER.ENRR", country="all", start=1990 ,  end=2020)
data28 = data28.reset_index()
data28.columns=['country','year','inscripciones_nivel_terciario']
data28 = data28.loc[data28['country'].isin(paises)]



pro_ang = data28[data28.country == 'Angola']['inscripciones_nivel_terciario'].mean()
angola = data28[data28['country']== 'Angola'].fillna(pro_ang)
# --------
pro_arg = data28[data28.country == 'Argentina']['inscripciones_nivel_terciario'].mean()
argentina = data28[data28['country']== 'Argentina'].fillna(pro_arg)
# --------
pro_australia = data28[data28.country == 'Australia']['inscripciones_nivel_terciario'].mean()
australia = data28[data28['country']== 'Australia'].fillna(pro_australia)
# --------
pro_austria = data28[data28.country == 'Austria']['inscripciones_nivel_terciario'].mean()
austria = data28[data28['country']== 'Austria'].fillna(pro_austria)
# --------
pro_bolivia = data28[data28.country == 'Bolivia']['inscripciones_nivel_terciario'].mean()
bolivia = data28[data28['country']== 'Bolivia'].fillna(pro_bolivia)
# --------
pro_brazil = data28[data28.country == 'Brazil']['inscripciones_nivel_terciario'].mean()
brazil = data28[data28['country']== 'Brazil'].fillna(pro_brazil)
# --------
pro_canada= data28[data28.country == 'Canada']['inscripciones_nivel_terciario'].mean()
canada = data28[data28['country']== 'Canada'].fillna(pro_canada)
# --------
pro_chile = data28[data28.country == 'Chile']['inscripciones_nivel_terciario'].mean()
chile = data28[data28['country']== 'Chile'].fillna(pro_chile)
# --------
pro_china = data28[data28.country == 'China']['inscripciones_nivel_terciario'].mean()
china = data28[data28['country']== 'China'].fillna(pro_china)
# --------
pro_colombia = data28[data28.country == 'Colombia']['inscripciones_nivel_terciario'].mean()
colombia = data28[data28['country']== 'Colombia'].fillna(pro_colombia)
# --------
pro_finland = data28[data28.country == 'Finland']['inscripciones_nivel_terciario'].mean()
finland = data28[data28['country']== 'Finland'].fillna(pro_finland)
# --------
pro_alemania = data28[data28.country == 'Germany']['inscripciones_nivel_terciario'].mean()
alemania = data28[data28['country']== 'Germany'].fillna(pro_alemania)
# --------
pro_india = data28[data28.country == 'India']['inscripciones_nivel_terciario'].mean()
india = data28[data28['country']== 'India'].fillna(pro_india)
# --------
pro_italia = data28[data28.country == 'Italy']['inscripciones_nivel_terciario'].mean()
italia = data28[data28['country']== 'Italy'].fillna(pro_italia)
# --------
pro_japon = data28[data28.country == 'Japan']['inscripciones_nivel_terciario'].mean()
japon = data28[data28['country']== 'Japan'].fillna(pro_japon)
# --------
pro_mexico = data28[data28.country == 'Mexico']['inscripciones_nivel_terciario'].mean()
mexico = data28[data28['country']== 'Mexico'].fillna(pro_mexico)
# --------
pro_morocco = data28[data28.country == 'Morocco']['inscripciones_nivel_terciario'].mean()
morocco = data28[data28['country']== 'Morocco'].fillna(pro_morocco)
# --------
pro_nuevaZelanda = data28[data28.country == 'New Zealand']['inscripciones_nivel_terciario'].mean()
nuevaZelanda = data28[data28['country']== 'New Zealand'].fillna(pro_nuevaZelanda)
# --------
pro_niger = data28[data28.country == 'Nigeria']['inscripciones_nivel_terciario'].mean()
nigeria = data28[data28['country']== 'Nigeria'].fillna(pro_niger)
# --------
pro_norway = data28[data28.country == 'Norway']['inscripciones_nivel_terciario'].mean()
norway = data28[data28['country']== 'Norway'].fillna(pro_norway)
# --------
pro_peru = data28[data28.country == 'Peru']['inscripciones_nivel_terciario'].mean()
peru = data28[data28['country']== 'Peru'].fillna(pro_peru)
# --------
pro_rusia = data28[data28.country == 'Russian Federation']['inscripciones_nivel_terciario'].mean()
rusia = data28[data28['country']== 'Russian Federation'].fillna(pro_rusia)
# --------
pro_seneg = data28[data28.country == 'Senegal']['inscripciones_nivel_terciario'].mean()
senegal = data28[data28['country']== 'Senegal'].fillna(pro_seneg)
# --------
pro_safri = data28[data28.country == 'South Africa']['inscripciones_nivel_terciario'].mean()
safri= data28[data28['country']== 'South Africa'].fillna(pro_safri)
# --------
pro_espana = data28[data28.country == 'Spain']['inscripciones_nivel_terciario'].mean()
espana = data28[data28['country']== 'Spain'].fillna(pro_espana)
# --------
pro_sw = data28[data28.country == 'Sweden']['inscripciones_nivel_terciario'].mean()
sweden = data28[data28['country']== 'Sweden'].fillna(pro_sw)
# --------
pro_syria = data28[data28.country == 'Syrian Arab Republic']['inscripciones_nivel_terciario'].mean()
syria = data28[data28['country']== 'Syrian Arab Republic'].fillna(pro_syria)
# --------
pro_eeuu = data28[data28.country == 'United States']['inscripciones_nivel_terciario'].mean()
eeuu = data28[data28['country']== 'United States'].fillna(pro_eeuu)
# --------
pro_uru = data28[data28.country == 'Uruguay']['inscripciones_nivel_terciario'].mean()
uruguay = data28[data28['country']== 'Uruguay'].fillna(pro_uru)
# --------
pro_zimba = data28[data28.country == 'Zimbabwe']['inscripciones_nivel_terciario'].mean()
zimba = data28[data28['country']== 'Zimbabwe'].fillna(pro_zimba)
# --------

# Concatenamos para crear la ultima tabla (inscripciones_nivel_terciario)
inscripciones_nivel_terciario = pd.concat([angola, argentina, australia, austria,  bolivia,  brazil, canada, chile, china, colombia, finland, alemania, india, italia, japon, mexico, morocco, nuevaZelanda, nigeria, norway, peru, rusia, senegal, safri, espana, sweden, syria, eeuu, uruguay, zimba])


# Creamos un dataset final con todas las tablas
datosFinales1= pd.concat([data1, data2.iloc[:, 2],data3.iloc[:, 2],data4.iloc[:, 2],data5.iloc[:, 2],data6.iloc[:, 2],data7.iloc[:, 2],data8.iloc[:, 2]], axis=1)
datosFinales2 = pd.concat([data10.iloc[:, 2],data12.iloc[:, 2],data13.iloc[:, 2],data14.iloc[:, 2],data15.iloc[:, 2],data18.iloc[:, 2]], axis=1)
datosFinales3 = pd.concat ([data20.iloc[:, 2],data21.iloc[:, 2],data22.iloc[:, 2],data23.iloc[:, 2],data26.iloc[:, 2],data27.iloc[:, 2],inscripciones_nivel_terciario.iloc[:,2]],axis=1)
datosFinal = pd.concat ([datosFinales1, datosFinales2,datosFinales3] ,axis=1)
datosFinal = datosFinal.reset_index()
datosFinal=datosFinal.drop(['index'], axis=1)
datosFinal =datosFinal.reset_index()
datosFinal=datosFinal.set_index("index")
datosFinal['year'] = datosFinal['year'].astype('int64')

datosFinal["country"] = datosFinal["country"].replace(
       { 'Argentina':0 ,'Chile': 1,'Brazil':2,'Peru':3,'Bolivia':4,'Colombia':5, 'Uruguay':6 ,'United States':7,'Mexico':8,'Canada':9,
         'China':10,'Russian Federation':11,'Japan':12,'India':13,'Syrian Arab Republic':14,
         'Nigeria':15,'Morocco':16,'South Africa':16,'Senegal':17,'Zimbabwe':18,'Angola':19,
         'Spain':20, 'Italy':21,'Austria':22,'Finland':23,'Sweden':24,'Norway':25,'Germany':26,
         'Australia':27 ,'New Zealand':28
       })


# Eliminamos tablas
miConexion = mysql.connector.connect( host=database_ip, user= database_username, passwd=database_password, db=database_name )
cur = miConexion.cursor()
cur.execute( "drop table if exists tb_esperanza,tb_continente,tb_paises,tb_year ")
miConexion.close()


# Ingestamos las tablas nuevas
database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password, 
                                                      database_ip, database_name), pool_recycle=1, pool_timeout=57600).connect()

datosFinal.to_sql(con=database_connection, name='tb_esperanza', if_exists='append',chunksize=100)
df_continentes.to_sql(con=database_connection, name='tb_continente', if_exists='append',chunksize=100)
df_paises.to_sql(con=database_connection, name='tb_paises', if_exists='append',chunksize=100)
df_años.to_sql(con=database_connection, name='tb_year', if_exists='append',chunksize=100)
database_connection.close()



#creamos las consultas para modificar primary key y foren key 
import mysql.connector
primary_key_tb_paises ="ALTER TABLE tb_paises  add   PRIMARY KEY (id_paises);"
primary_key_tb_continente ="ALTER TABLE tb_continente  add   PRIMARY KEY (id_continente);"
foren_key_ta_paises ="ALTER TABLE tb_paises  ADD FOREIGN KEY (id_continente) REFERENCES tb_continente(id_continente);"
foren_key_ta_esperanza ="ALTER TABLE tb_esperanza  ADD FOREIGN KEY (country) REFERENCES tb_paises(id_paises);"


miConexion = mysql.connector.connect( host=database_ip, user= database_username, passwd=database_password, db=database_name )
cur = miConexion.cursor()
cur.execute(primary_key_tb_paises)

cur = miConexion.cursor()
cur.execute(primary_key_tb_continente)

cur = miConexion.cursor()
cur.execute(foren_key_ta_paises)

cur = miConexion.cursor()
cur.execute(foren_key_ta_esperanza)
miConexion.close()
