

import pandas as pd


# # Province add in unique id

id_unique = pd.read_excel(r'C:\Users\Shahadat Shuchon\Documents\M.Saif\Data Model\Data_model_100222.xlsx', sheet_name= 'ID_unique')
id_unique.head(2)


crop_history = pd.read_excel(r'C:\Users\Shahadat Shuchon\Documents\M.Saif\Data Model\Data_model_100222.xlsx', sheet_name= 'Crop_history')
crop_history.head(2)


crop_history = crop_history[['Unique_ID','Province']]
crop_history.head(2)


id_unique_rev = id_unique.set_index('Unique_ID').join(crop_history.set_index('Unique_ID'))
id_unique_rev=id_unique_rev.reset_index()
id_unique_rev=id_unique_rev.drop_duplicates(subset='Unique_ID',keep='first')
id_unique_rev.head(2)


# # stem count raw and id unique_rev join


stem_raw = pd.read_excel(r'C:\Users\Shahadat Shuchon\Documents\M.Saif\Data Model\Data_model_100222.xlsx', sheet_name ='Stem_count_raw')
stem_raw.head(2)


stem_id_unique = pd.merge(stem_raw, id_unique_rev, on="Unique_ID", how='left')
stem_id_unique.head(2)


# # Month Extraction

stem_id_unique['Month'] = stem_id_unique['Date'].dt.month
stem_id_unique['Month'] = stem_id_unique['Date'].dt.strftime('%B')
stem_id_unique.head(2)


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


stem_id_unique['Season'] = stem_id_unique.apply (lambda row: label_race(row), axis=1)
stem_id_unique.head(2)


# # Dataframe  refurbish


stem_id_unique=stem_id_unique.drop(['Column1', 'Field_name_y','Farm_name_y','Producer_y','JIRA_ID_y','Longitude_y','Latitude_y','Province_y' ], axis=1)
stem_id_unique.head(2)


stem_id_unique.columns


stem_id_unique= stem_id_unique.rename({'JIRA_ID_x':'JIRA_ID', 'Farm_name_x':'Farm_Name', 'Producer_x':'Producer', 'Province_x':'Province', 'Field_name_x':'Field_name', 'Longitude_x':'Longitude', 'Latitude_x':'Latitude'}, axis='columns')
stem_id_unique.head(2)


# # Filtering nan rows


stem_id_unique = stem_id_unique[stem_id_unique[['Point_no', 'Stem_count', 'Height_1cm','Height_2cm','Height_3cm','Height_4cm','Height_5cm','Longitude','Latitude']].notnull().all(1)]
stem_id_unique.head(2)


stem_id_unique.to_excel("stem_id_unique.xlsx")





