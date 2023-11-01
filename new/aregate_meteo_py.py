import pandas as pd

filter_df = pd.read_excel(
    'C:/All/AlfaAlfa_project/Code_hub/Code_MM/data_luzerne_analyse_gps/luzerne_filtered_SoilAnalysis_updated/data_luzerne_analyse_gps_100522.xlsx',
    sheet_name='Filter_used')
luzerne_df = pd.read_excel(
    'C:/All/AlfaAlfa_project/Code_hub/Code_MM/data_luzerne_analyse_gps/luzerne_filtered_SoilAnalysis_updated/data_luzerne_analyse_gps_100522.xlsx',
    sheet_name='Data_luzerne_analyse_gps_070322')
unique_id_data_df = pd.read_excel(
    'C:/All/AlfaAlfa_project/Code_hub/Code_MM/data_luzerne_analyse_gps/luzerne_filtered_SoilAnalysis_updated/data_luzerne_analyse_gps_100522.xlsx',
    sheet_name='ID_updated')
soil_analysis_transpose_df = pd.read_excel(
    'C:/All/AlfaAlfa_project/Code_hub/Code_MM/data_luzerne_analyse_gps/luzerne_filtered_SoilAnalysis_updated/data_luzerne_analyse_gps_100522.xlsx',
    sheet_name='Soilanalysis')

df=pd.read_excel(r"C:\Users\Shahadat Shuchon\Documents\New folder\data_Luzrene-gps\13.5.22\data_luzerne_analyse_gps_100522.xlsx",sheet_name='Data_luzerne_analyse_gps_070322')
me=pd.read_excel(r'C:\Users\Shahadat Shuchon\Documents\New folder\data_Luzrene-gps\13.5.22\data_luzerne_analyse_gps_100522.xlsx',sheet_name='Meteo_station')
ag=pd.read_excel(r'C:\Users\Shahadat Shuchon\Documents\New folder\data_Luzrene-gps\13.5.22\data_luzerne_analyse_gps_100522.xlsx',sheet_name='agregat')


luzerne_filtered_df = luzerne_df.copy()
for col in filter_df.columns:
    if col not in {'Code QR', 'Longitude', 'Latitude'}:
        luzerne_filtered_df = luzerne_filtered_df[
            ~luzerne_filtered_df[col].str.lower().isin(list(filter_df[col].dropna().str.lower()))]
for col in filter_df.columns:
    if col in {'Code QR'}:
        # pass
        luzerne_filtered_df = luzerne_filtered_df[
            ~luzerne_filtered_df[col].isna() & ~(luzerne_filtered_df[col].duplicated())]
        # luzerne_filtered_df = luzerne_filtered_df[~(luzerne_filtered_df[col].isna())]
        # luzerne_filtered_df = luzerne_filtered_df[(~luzerne_filtered_df[col].duplicated())]
        # luzerne_filtered_df = luzerne_filtered_df[~(luzerne_filtered_df[col].isna())]
    elif col in {'Longitude', 'Latitude'}:
        luzerne_filtered_df = luzerne_filtered_df[~(luzerne_filtered_df[col].isna())]
        if col == 'Latitude':
            luzerne_filtered_df = luzerne_filtered_df[
                ~luzerne_filtered_df.loc[:, ['Longitude', 'Latitude']].duplicated()]
    else:
        pass

luzerne_unfiltered_df = luzerne_df[luzerne_df.Column1.isin(luzerne_filtered_df.Column1) == False]

with pd.ExcelWriter('SoilAnalysis_filtered.xlsx') as writer:
    luzerne_filtered_df.to_excel(writer, sheet_name='GPS')

    unique_id_data_df.rename({'id_field_c': 'ID unique champ'}, axis=1, inplace=True)
    luzerne_filtered_df['ID unique champ'] = luzerne_filtered_df['ID unique champ'].str.strip()
    unique_id_data_df['ID unique champ'] = unique_id_data_df['ID unique champ'].str.strip()

    luzerne_filtered_df = luzerne_filtered_df.join(
        unique_id_data_df.loc[:, ['ID unique champ', 'advisor']].set_index('ID unique champ'), on='ID unique champ')
    luzerne_filtered_df.reset_index(drop=True, inplace=True)
    luzerne_filtered_df.to_excel(writer, sheet_name='GPS_with_advisor')

    # luzerne_filtered_df['Code QR'] = luzerne_filtered_df['Code QR'].str.lower()
    # luzerne_filtered_df['Code QR'] = luzerne_filtered_df['Code QR'].str.strip()
    soil_analysis_transpose_df.rename({'QR_code': 'Code QR'}, axis=1, inplace=True)
    # soil_analysis_transpose_df['Code QR'] = soil_analysis_transpose_df['Code QR'].str.lower()
    # soil_analysis_transpose_df['Code QR'] = soil_analysis_transpose_df['Code QR'].str.strip()

    luzerne_with_soil_analysis_all = luzerne_filtered_df.merge(soil_analysis_transpose_df, on='Code QR', how='outer')
    luzerne_with_soil_analysis_all.to_excel(writer, sheet_name='GPS_soil_analysis_all')

    luzerne_filtered_df_luzerne_only = luzerne_filtered_df.merge(
        soil_analysis_transpose_df,
        on='Code QR', how='left',
        indicator=True).query('_merge == "left_only"').drop('_merge', 1)
    luzerne_filtered_df_luzerne_only.to_excel(writer, sheet_name='GPS_only')

    luzerne_filtered_df_soil_analysis_only = luzerne_filtered_df.merge(
        soil_analysis_transpose_df,
        on='Code QR', how='right',
        indicator=True).query('_merge == "right_only"').drop('_merge', 1)
    luzerne_filtered_df_soil_analysis_only.to_excel(writer, sheet_name='SoilAnalysis_only')

    luzerne_filtered_df_common = luzerne_filtered_df.merge(soil_analysis_transpose_df, on='Code QR', how='inner')
    luzerne_filtered_df_common.to_excel(writer, sheet_name='GPS_SoilAnalysis_common')

## meteo analysis
comment=list(me[' Commentaire'])
comment=[x for x in comment if str(x) != 'nan']
enchat=list(me["Nom de l''échantillon"])
enchat=[x for x in enchat if str(x) != 'nan']
point=list(me["Nom du point GPS"])
point=[x for x in point if str(x) != 'nan']

c=df.apply(lambda row: row[df[' Commentaire'].isin(comment)])
e=df.apply(lambda row: row[df["Nom de l''échantillon"].isin(enchat)])
g=df.apply(lambda row: row[df["Nom du point GPS"].isin(point)])

dfs=[c,e,g]
res = pd.concat(dfs, axis=0)
res=res.drop_duplicates(subset=['Code QR', 'Latitude','Longitude'], keep='first')
res=res.dropna(subset = ['Code QR', 'Longitude', 'Latitude'])

# Agregate analysis
com=list(ag[' Commentaire'])
com=[x for x in com if str(x) != 'nan']
enc=list(ag["Nom de l''échantillon"])
enc=[x for x in enc if str(x) != 'nan']
poi=list(ag["Nom du point GPS"])
poi=[x for x in poi if str(x) != 'nan']

ca=df.apply(lambda row: row[df[' Commentaire'].isin(com)])
ea=df.apply(lambda row: row[df["Nom de l''échantillon"].isin(enc)])
ga=df.apply(lambda row: row[df["Nom du point GPS"].isin(poi)])

dfs=[ca,ea,ga]
res_a = pd.concat(dfs, axis=0)
res_a=res_a.drop_duplicates(subset=['Code QR', 'Latitude','Longitude'], keep='first')
res_a=res_a.dropna(subset = ['Code QR', 'Longitude', 'Latitude'])

with pd.ExcelWriter('SoilAnalysis_unfiltered.xlsx') as writer:
    luzerne_unfiltered_df.to_excel(writer, sheet_name='GPS')
    unique_id_data_df.rename({'id_field_c': 'ID unique champ'}, axis=1, inplace=True)
    luzerne_unfiltered_df['ID unique champ'] = luzerne_unfiltered_df['ID unique champ'].str.strip()
    luzerne_unfiltered_df = luzerne_unfiltered_df.join(
        unique_id_data_df.loc[:, ['ID unique champ', 'advisor']].set_index('ID unique champ'), on='ID unique champ')
    luzerne_unfiltered_df.reset_index(drop=True, inplace=True)
    luzerne_unfiltered_df.to_excel(writer, sheet_name='GPS_with_advisor')
    res.to_excel(writer, sheet_name='gps_meteo')
    res_a.to_excel(writer, sheet_name='gps_agegate')


luzerne_filtered_df







