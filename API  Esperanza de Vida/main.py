from typing import Union
import json
from fastapi import FastAPI
import mysql.connector
app = FastAPI()

database_username = 'admin'
database_password = '123456789'
database_ip       = 'database-2.cmmt68xsoykx.us-east-1.rds.amazonaws.com'
database_name     = 'sys'
pais = []
conti = []
años = []
esperanza = []
api =[]


@app.get("/")
def read_root():
    list1 = ["bienvenidos al  api de esperanza de vida , aqui encontrara todos los datos relcionados al tema --->/esperanza,/year,/paises,/continentes"]
    list2 = ["esperanza de vida -- https://esperanzadevida.herokuapp.com/esperanza"]
    list3 = ["años -- https://esperanzadevida.herokuapp.com/year"]
    list4 = ["paises  -- https://esperanzadevida.herokuapp.com/paises"]
    list5 = ["continentes -- https://esperanzadevida.herokuapp.com/continentes"]
    list5 = ["datos totales  -- https://esperanzadevida.herokuapp.com/api"]

            
    return (list1,list2,list3,list4,list5)
    

@app.get("/paises")
def  uno():

    miConexion = mysql.connector.connect( host=database_ip, user= database_username, passwd=database_password, db=database_name )
    cur = miConexion.cursor()
    cur.execute("select * from tb_paises")

    datos  = cur.fetchall()
    for  fila  in datos :
        paises = {'id_paises':fila[0],'country':fila[1],'id_continente':fila[2]}
        pais.append(paises) 
    miConexion.close()

    return {"paises": pais}

@app.get("/continentes")
def  uno():

    miConexion = mysql.connector.connect( host=database_ip, user= database_username, passwd=database_password, db=database_name )
    cur = miConexion.cursor()
    cur.execute("select * from tb_continente")

    datos_cont  = cur.fetchall()
    for  fila  in datos_cont :
        continnente = {'id_continente':fila[0],'continente':fila[1]}
        conti.append(continnente) 
    miConexion.close()

    return {"continentes": conti}

@app.get("/year")
def  uno():

    miConexion = mysql.connector.connect( host=database_ip, user= database_username, passwd=database_password, db=database_name )
    cur = miConexion.cursor()
    cur.execute("select * from tb_year")
    global años
    datos_años  = cur.fetchall()
    for  fila  in datos_años :
        años_ = {'year':fila[0]}
        años.append(años_) 
    miConexion.close()

    return {"year": años}


@app.get("/esperanza")
def  year():
    miConexion = mysql.connector.connect( host=database_ip, user= database_username, passwd=database_password, db=database_name )
    cur = miConexion.cursor()
    cur.execute("select * from tb_esperanza")
    datos_esperanza  = cur.fetchall()
    for  fila  in datos_esperanza :
        esperanza_ = {
        'index':fila[0],
        'country':fila[1],
        'year':fila[2],
        'Desempleo_mujeres':fila[3],
        'Desempleo_mujeres_jóvenes_14_24_años':fila[4],
        'Desempleo_varones_jovenes_15_24_años':fila[5],
        'Desempleo_Población_activa_total':fila[6],
        'esperanza_vida_nacer_Mujeres':fila[7],
        'esperanza_vida_nacer_Varones':fila[8],
        'esperanza_vida_nacer_total':fila[9],
        'poblacion_total_salud':fila[10],
        'fertilidad_mujeres':fila[11],
        'tasa_mortalidad_bebes':fila[12],
        'crecimiento_masa_monetaria_inflacion':fila[13],
        'tasa_mort_5anios_cada_mil':fila[14],
        'crecimiento_poblacion':fila[15],
        'Tasa_fertilidad_mujeres':fila[16],
        'PBI_per_capita':fila[17],
        'desempleo_total':fila[18],
        'mortalidad_accidentes_transito':fila[19],
        'acceso_a_la_electricidad':fila[20],
        'id_continente':fila[21]}
        esperanza.append(esperanza_) 
    miConexion.close()

    return {"esperanza": esperanza}

@app.get("/api")
def  year():
    miConexion = mysql.connector.connect( host=database_ip, user= database_username, passwd=database_password, db=database_name )
    cur = miConexion.cursor()
    #cur.execute("SELECT p.country as pais ,c.continentes as continente ,e.year,e.Desempleo_mujeres,e.Desempleo_mujeres_jóvenes_14_24_años,e.Desempleo_varones_jovenes_15_24_años,e.Desempleo_Población_activa_total,e.esperanza_vida_nacer_Mujeres,e.esperanza_vida_nacer_Varones,e.esperanza_vida_nacer_total,e.poblacion_total_salud,e.fertilidad_mujeres,e.tasa_mortalidad_bebes,e.crecimiento_masa_monetaria_inflacion,e.tasa_mort_5anios_cada_mil,e.crecimiento_poblacion,e.Tasa_fertilidad_mujeres,e.PBI_per_capita,e.desempleo_total,e.mortalidad_accidentes_transito,e.acceso_a_la_electricidad FROM tb_paises AS  p INNER JOIN tb_continente AS c ON p.id_continente = c.id_continente INNER JOIN tb_esperanza AS e ON e.country = p.id_paises;")
    cur.execute("SELECT p.country as pais ,c.continentes as continente ,e.* FROM tb_paises AS  p INNER JOIN tb_continente AS c ON p.id_continente = c.id_continente INNER JOIN tb_esperanza AS e ON e.country = p.id_paises;")
    datos_total  = cur.fetchall()
    for  fila  in datos_total :
        total = {
        'pais':fila[0],
        'continentes':fila[1],
        'year':fila[2],
        'Desempleo_mujeres':fila[3],
        'Desempleo_mujeres_jóvenes_14_24_años':fila[4],
        'Desempleo_varones_jovenes_15_24_años':fila[5],
        'Desempleo_Población_activa_total':fila[6],
        'esperanza_vida_nacer_Mujeres':fila[7],
        'esperanza_vida_nacer_Varones':fila[8],
        'esperanza_vida_nacer_total':fila[9],
        'poblacion_total_salud':fila[10],
        'fertilidad_mujeres':fila[11],
        'tasa_mortalidad_bebes':fila[12],
        'crecimiento_masa_monetaria_inflacion':fila[13],
        'tasa_mort_5anios_cada_mil':fila[14],
        'crecimiento_poblacion':fila[15],
        'Tasa_fertilidad_mujeres':fila[16],
        'PBI_per_capita':fila[17],
        'desempleo_total':fila[18],
        'mortalidad_accidentes_transito':fila[19],
        'acceso_a_la_electricidad':fila[20],
        'id_continente':fila[21]}
        api.append(total) 
    miConexion.close()

    return {"api": api}
@app.get("/api2")
def  year():
    miConexion = mysql.connector.connect( host=database_ip, user= database_username, passwd=database_password, db=database_name )
    cur = miConexion.cursor()
    cur.execute("SELECT p.country as pais ,c.continentes as continente ,e.* FROM tb_paises AS  p INNER JOIN tb_continente AS c ON p.id_continente = c.id_continente INNER JOIN tb_esperanza AS e ON e.country = p.id_paises;")
    api2=[]
    datos_total  = cur.fetchall()
    for  a  in datos_total :
        total = {
        'pais':a[0],
        'continentes':a[1],
        'index':a[2],
        'country':a[3],
        'year':a[4],
        'Desempleo_mujeres':a[5],
        'Desempleo_mujeres_jóvenes_14_24_años':a[6],
        'Desempleo_varones_jovenes_15_24_años':a[7],
        'Desempleo_Población_activa_total':a[8],
        'esperanza_vida_nacer_Mujeres':a[9],
        'esperanza_vida_nacer_Varones':a[10],
        'esperanza_vida_nacer_total':a[11],
        'poblacion_total_salud':a[12],
        'fertilidad_mujeres':a[13],
        'tasa_mortalidad_bebes':a[14],
        'crecimiento_masa_monetaria_inflacion':a[15],
        'tasa_mort_5anios_cada_mil':a[16],
        'crecimiento_poblacion':a[17],
        'Tasa_fertilidad_mujeres':a[18],
        'PBI_per_capita':a[19],
        'desempleo_total':a[20],
        'mortalidad_accidentes_transito': a[21],
        'acceso_a_la_electricidad':a[22],
        'Inscripción_escolar_nivel_primario':a[23],
        'Inscripción_escolar_nivel_secundaria':a[24],
        'inscripciones_nivel_terciario':a[25]}

        api2.append(total) 
    miConexion.close()

    return {"api2": api2}

@app.get("/api3")
def  year():
    miConexion = mysql.connector.connect( host=database_ip, user= database_username, passwd=database_password, db=database_name )
    cur = miConexion.cursor()
    cur.execute("SELECT p.country as pais ,c.continentes as continente ,e.* FROM tb_paises AS  p INNER JOIN tb_continente AS c ON p.id_continente = c.id_continente INNER JOIN tb_esperanza AS e ON e.country = p.id_paises;")
    api2=[]
    datos_total  = cur.fetchall()
    for  a  in datos_total :
        total = {
        'pais':a[0],
        'continentes':a[1],
        'index':a[2],
        'country':a[3],
        'year':a[4],
        'Desempleo_mujeres':a[5],
        'Desempleo_mujeres_jóvenes_14_24_años':a[6],
        'Desempleo_varones_jovenes_15_24_años':a[7],
        'Desempleo_Población_activa_total':a[8],
        'esperanza_vida_nacer_Mujeres':a[9],
        'esperanza_vida_nacer_Varones':a[10],
        'esperanza_vida_nacer_total':a[11],
        'poblacion_total_salud':a[12],
        'fertilidad_mujeres':a[13],
        'tasa_mortalidad_bebes':a[14],
        'crecimiento_masa_monetaria_inflacion':a[15],
        'tasa_mort_5anios_cada_mil':a[16],
        'crecimiento_poblacion':a[17],
        'Tasa_fertilidad_mujeres':a[18],
        'PBI_per_capita':a[19],
        'desempleo_total':a[20],
        'mortalidad_accidentes_transito': a[21],
        'acceso_a_la_electricidad':a[22],
        'Inscripción_escolar_nivel_primario':a[23],
        'Inscripción_escolar_nivel_secundaria':a[24],
        'inscripciones_nivel_terciario':a[25]}

        api2.append(total) 
    miConexion.close()

    return {"api3": api2}


@app.get("/api4")
def  year():
    miConexion = mysql.connector.connect( host=database_ip, user= database_username, passwd=database_password, db=database_name )
    cur = miConexion.cursor()
    cur.execute("SELECT p.country as pais ,c.continentes as continente ,e.* FROM tb_paises AS  p INNER JOIN tb_continente AS c ON p.id_continente = c.id_continente INNER JOIN tb_esperanza AS e ON e.country = p.id_paises;")
    api2=[]
    datos_total  = cur.fetchall()
    for  a  in datos_total :
        total = {
        'pais':a[0],
        'continentes':a[1],
        'index':a[2],
        'country':a[3],
        'year':a[4],
        'Desempleo_mujeres':a[5],
        'Desempleo_mujeres_jóvenes_14_24_años':a[6],
        'Desempleo_varones_jovenes_15_24_años':a[7],
        'Desempleo_Población_activa_total':a[8],
        'esperanza_vida_nacer_Mujeres':a[9],
        'esperanza_vida_nacer_Varones':a[10],
        'esperanza_vida_nacer_total':a[11],
        'poblacion_total_salud':a[12],
        'fertilidad_mujeres':a[13],
        'tasa_mortalidad_bebes':a[14],
        'crecimiento_masa_monetaria_inflacion':a[15],
        'tasa_mort_5anios_cada_mil':a[16],
        'crecimiento_poblacion':a[17],
        'Tasa_fertilidad_mujeres':a[18],
        'PBI_per_capita':a[19],
        'desempleo_total':a[20],
        'mortalidad_accidentes_transito': a[21],
        'acceso_a_la_electricidad':a[22],
        'Inscripción_escolar_nivel_primario':a[23],
        'Inscripción_escolar_nivel_secundaria':a[24],
        'inscripciones_nivel_terciario':a[25]}

        api2.append(total) 
    miConexion.close()

    return {"api4": api2}