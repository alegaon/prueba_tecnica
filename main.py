import pandas as pd

# leer archivo
datos = pd.read_excel("Victims_Age_by_Offense_Category_2022.xlsx")

# elegir categoria Crimes Against Property 
# elimimar footer
crimes_against_property = datos.iloc[11:12,:]

# generar dataframe sin totales
columna_a_omitir = 'Unnamed: 1'

# Mostrar todas las columnas excepto la columna_a_omitir
df_resultante = crimes_against_property.drop(columns=[columna_a_omitir])

# generar csv

# Escribir el DataFrame a un archivo CSV, sin index , sin header
nombre_archivo_csv = 'datos.csv'

df_resultante.to_csv(nombre_archivo_csv, index=False, header=False)

print(f'Se ha generado el archivo CSV: {nombre_archivo_csv}')

