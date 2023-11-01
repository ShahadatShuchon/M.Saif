

import pandas as pd


# # Columns Name in English


data_luzerne = pd.read_excel(r"C:\Users\Shahadat Shuchon\Documents\data luzerne\data_luzerne_evaluation.xls")
data_luzerne.head(2)

data_luzerne.columns


data_luzerne = data_luzerne.rename({'No ferme':'JIRA_ID', 'Nom ferme':'Farm_Name', 'Responsable':'Producer','Rue':'Road', 'Municipalité':'Municipality', 'Code postal':'Postal_code','Année':'Year', 'ID unique champ':'Unique_ID', 'No champ':'Field_no','Nom champ':'Field_name', 'No point':'Point_no','Nom point':'Point_name', 'État':'Status', 'Nombre de tiges':'Stem_count','Hauteur de tige 1 (cm)':'Height_1cm', 'Hauteur de tige 2 (cm)':'Height_2cm','Hauteur de tige 3 (cm)':'Height_3cm', 'Hauteur de tige 4 (cm)':'Height_4cm', 'Hauteur de tige 5 (cm)':'Height_5cm','Borne':'Land_mark'}, axis='columns')
data_luzerne.head(2)


# # adding Adviser

id_unique = pd.read_excel(r"C:\Users\Shahadat Shuchon\Documents\data luzerne\ID_unique.xlsx")
id_unique.head(2)


id_unique =id_unique[['Unique_ID','Adviser']]


data_luzerne_rev = pd.merge(data_luzerne, id_unique, on="Unique_ID", how='left')
data_luzerne_rev.head(2)


# # Month Extraction

data_luzerne_rev['Month'] = data_luzerne_rev['Date'].dt.month
data_luzerne_rev['Month'] = data_luzerne_rev['Date'].dt.strftime('%B')
data_luzerne_rev.head(2)


# # season inclution


def label_race (row):
   if row['Month'] == 'May' :
      return 'Spring'
   if row['Month'] == 'June' :
      return 'Spring'
   if row['Month'] == 'July' :
      return 'Spring'
   if row['Month'] == 'August':
      return 'Fall'
   if row['Month']  == 'September':
      return 'Fall'
   if row['Month'] == 'October':
      return 'Fall'
   if row['Month'] == 'November':
      return 'Fall'
   if row['Month'] == 'December':
      return 'Fall'


data_luzerne_rev['Season'] = data_luzerne_rev.apply (lambda row: label_race(row), axis=1)
data_luzerne_rev.head(2)


# # Filtering nan rows

data_luzerne_rev = data_luzerne_rev[data_luzerne_rev[['Point_no', 'Stem_count', 'Height_1cm','Height_2cm','Height_3cm','Height_4cm','Height_5cm','Longitude','Latitude']].notnull().all(1)]
data_luzerne_rev.head(2)



data_luzerne_rev.to_excel("data_luzerne_rev.xlsx")



