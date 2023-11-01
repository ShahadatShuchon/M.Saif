
# # ###############
#Data Formation
########################

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\Users\Shahadat Shuchon\Documents\M.Saif\Data Model\stem_id_unique.xlsx')
df.head()


# # #################
#Data Processing
########################

# # Farm Name/ JIRA Id Table ##################

df1=df[['JIRA_ID','Farm_Name','Producer','Adviser']]
df1.head()


df2 = df1.drop_duplicates(subset=['JIRA_ID'], keep='last')

df2=pd.DataFrame(df2)
df2.head()
#un = df1.nunique()
#un


data1=df[["JIRA_ID", "Stem_count"]].groupby("JIRA_ID").describe()
data1=pd.DataFrame(data1)
data1#.head()


data1.to_excel("stem_analysis_JIRA_ID_stem_count_descriptive_statistics.xlsx")


#data2=df[['JIRA_ID','Farm_name','Adviser']].unique("JIRA_ID")
#data2.head()
df3 = pd.merge(df2, data1, how="right", on="JIRA_ID")
df3.head()


#df3 = pd.merge(df1,data1,how="right", on="JIRA_ID")
#df3.head()

df3.to_excel("stem_analysis_JIRA_ID_descriptive_analysis_farm_name_adviser.xlsx")


# # No champ/ Field name Table ##############

data2= df[["Field_name", "Stem_count"]].groupby("Field_name").describe()
data2=pd.DataFrame(data2)
data2


data2.to_excel("stem_analysis_No_champ_stem_count_descriptive_statistics.xlsx")


df4=df[['Field_name','Farm_Name','Producer','Adviser']]
df4.head()

df5 = df4.drop_duplicates(subset=['Field_name'], keep='last')

df5=pd.DataFrame(df5)
df5.head()


df6 = pd.merge(df5, data2, how="right", on="Field_name")
df6.head()

df6.to_excel("stem_analysis_Field_name_descriptive_statistics_farm_name_adviser.xlsx")


# # JIRA ID / Farm Name Seasons Table #######

# # Fall ##

dff = df[df['Season']=='Fall']
dff=dff[['JIRA_ID','Farm_Name','Producer','Adviser']]
dff.head()


dff = dff.drop_duplicates(subset=['JIRA_ID'], keep='last')

dff=pd.DataFrame(dff)
dff.head()


dff1=df[["JIRA_ID", "Stem_count"]].groupby("JIRA_ID").describe()
dff1=pd.DataFrame(dff1)
dff1.head()


dff2 = pd.merge(dff, dff1, how="left", on="JIRA_ID")
dff2.head()


dff2.to_excel("stem_analysis_JIRA_ID_Fall_season_descriptive_analysis.xlsx")


# # Spring ##

dfs = df[df['Season']=='Spring']
dfs=dfs[['JIRA_ID','Farm_Name','Producer','Adviser']]
dfs.head()


dfsc = dfs.drop_duplicates(subset=['JIRA_ID'], keep='last')

dfsc=pd.DataFrame(dfsc)
dfsc.head()


dfs1=df[["JIRA_ID", "Stem_count"]].groupby("JIRA_ID").describe()
dfs1=pd.DataFrame(dfs1)
dfs1.head()

dfs2 = pd.merge(dfsc, dfs1, how="left", on="JIRA_ID")
dfs2.head()

dfs2.to_excel("stem_analysis_JIRA_ID_Spring_season_descriptive_analysis.xlsx")


# # No champ / Field Name Season Table ###########

# # Fall ##

df_f = df[df['Season']=='Fall']
df_f=df_f[['Field_name','Farm_Name','Producer','Adviser']]
df_f.head()


df_f = df_f.drop_duplicates(subset=['Field_name'], keep='last')

df_f=pd.DataFrame(df_f)
df_f.head()

df_1=df[["Field_name", "Stem_count"]].groupby("Field_name").describe()
df_1=pd.DataFrame(df_1)
df_1.head()

df_2 = pd.merge(df_f, df_1, how="left", on="Field_name")
df_2#.head()

df_2.to_excel("stem_analysis_Field_name_Fall_season_descriptive_analysis.xlsx")


# # Spring ##


df_s = df[df['Season']=='Spring']
df_s=df_s[['Field_name','Farm_Name','Producer','Adviser']]
df_s.head()


df_s = df_s.drop_duplicates(subset=['Field_name'], keep='last')
df_s=pd.DataFrame(df_s)
df_s.head()


df_3 = pd.merge(df_s, df_1, how="left", on="Field_name")
df_3.head()


df_3.to_excel("stem_analysis_Field_name_Spring_season_descriptive_analysis.xlsx")





# # JIRA_ID Histogram ###########


df['JIRA_ID'].plot(kind='hist',bins=20,color = "steelblue", rwidth=0.95)
#plt.title('Spring')
plt.xlabel('JIRA ID')
plt.ylabel('No. of obsevation')

fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('JIRA_ID_Histogram.jpg', dpi= 500)


df.Season.unique()


fd = df[["Province","Season", "Stem_count"]]
fd = fd[fd['Stem_count']<=150]
fd.head()


a=fd.loc[(fd['Season']== 'Spring')]
a.head()


a['Stem_count'].plot(kind='hist',color = "skyblue", rwidth=0.95)
plt.title('Spring')
plt.xlabel('Stem count')
plt.ylabel('No. of obsevation')
x = 10
y = 90
plt.axvline(x, color='k', linestyle='dashed', linewidth=1)
plt.axvline(y, color='k', linestyle='dashed', linewidth=1)
#plt.axvspan(x, y, color='w', alpha=0.5, lw=0)
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('season_spring_stem_count.jpg', dpi= 500)


b=fd.loc[(fd['Season']== 'Fall')]
b.head()


b['Stem_count'].plot(kind='hist',color = "cornflowerblue", rwidth=0.95)
plt.title('Fall')
plt.xlabel('Stem count')
plt.ylabel('No. of obsevation')
x = 10
y = 90
plt.axvline(x, color='k', linestyle='dashed', linewidth=1)
plt.axvline(y, color='k', linestyle='dashed', linewidth=1)
#plt.axvspan(x, y, color='w', alpha=0.5, lw=0)
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('season_fall_stem_count.jpg', dpi= 500)


k=df[df['Stem_count']<=150]
k['Stem_count'].plot(kind='hist',bins=100, color = "steelblue", rwidth=0.95)
#plt.title('Stem_count Histogram')
plt.xlabel('Stem count')
plt.ylabel('No. of obsevation')
x = 10
y = 90
plt.axvline(x, color='k', linestyle='dashed', linewidth=1)
plt.axvline(y, color='k', linestyle='dashed', linewidth=1)
#plt.axvspan(x, y, color='orange', alpha=0.5, lw=0)
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('stem_count_histogram.jpg', dpi= 500)


data1 = k['Stem_count']

fd.Province.unique()


c=fd.loc[(fd['Province']== 'Manitoba')]
c.head()


c['Stem_count'].plot(kind='hist', bins= 50, color = "bisque", rwidth=0.95)
plt.title('Manitoba')
plt.xlabel('Stem count')
plt.ylabel('No. of obsevation')
x = 10
y = 90
plt.axvline(x, color='k', linestyle='dashed', linewidth=1)
plt.axvline(y, color='k', linestyle='dashed', linewidth=1)
#plt.axvspan(x, y, color='orange', alpha=0.5, lw=0)
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('province_Manitoba_stem_count.jpg', dpi= 500)


data5 = c['Stem_count']


plt.figure(figsize=(8,6))
plt.hist(data1, bins=100, color = "steelblue", alpha=1.0, label="Total")
plt.hist(data5, bins=50, color = "bisque", alpha=1, label="Manitoba")
#plt.hist(data3, bins=100, alpha=0.5, label="Potassium (K)")
x = 10
y = 90
plt.axvline(x, color='k', linestyle='dashed', linewidth=1)
plt.axvline(y, color='k', linestyle='dashed', linewidth=1)
plt.xlabel("Stem count", size=14)
plt.ylabel("No. of obsevation", size=14)
#plt.title("Multiple Histograms with Matplotlib")
plt.legend(loc='best')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig("Total_Manitoba_Overlapping_histogram.jpg", dpi= 500)



d=fd.loc[(fd['Province']== 'Ontario')]
d.head()


d['Stem_count'].plot(kind='hist', bins=30, color = "burlywood", rwidth=0.95)
plt.title('Ontario')
plt.xlabel('Stem count')
plt.ylabel('No. of obsevation')
x = 10
y = 90
plt.axvline(x, color='k', linestyle='dashed', linewidth=1)
plt.axvline(y, color='k', linestyle='dashed', linewidth=1)
#plt.axvspan(x, y, color='orange', alpha=0.5, lw=0)
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('province_Ontario_stem_count.jpg', dpi= 500)


data4 = d['Stem_count']


plt.figure(figsize=(8,6))
plt.hist(data1, bins=100, color = "steelblue", alpha=1.0, label="Total")
plt.hist(data4, bins=30, color = "burlywood", alpha=1.0, label="Ontario")
#plt.hist(data3, bins=100, alpha=0.5, label="Potassium (K)")
x = 10
y = 90
plt.axvline(x, color='k', linestyle='dashed', linewidth=1)
plt.axvline(y, color='k', linestyle='dashed', linewidth=1)
plt.xlabel("Stem count", size=14)
plt.ylabel("No. of obsevation", size=14)
#plt.title("Multiple Histograms with Matplotlib")
plt.legend(loc='best')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig("Total_Ontario_Overlapping_histogram.jpg", dpi= 500)


e=fd.loc[(fd['Province']== 'Nova Scotia')]
e.head()

e['Stem_count'].plot(kind='hist', bins=10, color = "aquamarine", rwidth=0.95)
plt.title('Nova Scotia')
plt.xlabel('Stem count')
plt.ylabel('No. of obsevation')
x = 10
y = 90
plt.axvline(x, color='k', linestyle='dashed', linewidth=1)
plt.axvline(y, color='k', linestyle='dashed', linewidth=1)
#plt.axvspan(x, y, color='orange', alpha=0.5, lw=0)
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('province_Nova Scotia_stem_count.jpg', dpi= 500)


data3 = e['Stem_count']


plt.figure(figsize=(8,6))
plt.hist(data1, bins=100, color = "steelblue", alpha=1.0, label="Total")
plt.hist(data3, bins=10, color = "aquamarine", alpha=1.0, label="Nova Scotia")
#plt.hist(data3, bins=100, alpha=0.5, label="Potassium (K)")
x = 10
y = 90
plt.axvline(x, color='k', linestyle='dashed', linewidth=1)
plt.axvline(y, color='k', linestyle='dashed', linewidth=1)
plt.xlabel("Stem count", size=14)
plt.ylabel("No. of obsevation", size=14)
#plt.title("Multiple Histograms with Matplotlib")
plt.legend(loc='best')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig("Total_Nova Scotia_Overlapping_histogram.jpg", dpi= 500)


f=(fd.loc[(fd['Province']== 'Quebec') | (fd['Province']== 'Québec')])
f.head()


f['Stem_count'].plot(kind='hist', bins= 100, color = "mediumaquamarine", rwidth=0.95)
plt.title('Quebec')
plt.xlabel('Stem count')
plt.ylabel('No. of obsevation')
x = 10
y = 90
plt.axvline(x, color='k', linestyle='dashed', linewidth=1)
plt.axvline(y, color='k', linestyle='dashed', linewidth=1)
#plt.axvspan(x, y, color='orange', alpha=0.5, lw=0)
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('province_Quebec_stem_count.jpg', dpi= 500)

data2 = f['Stem_count']


plt.figure(figsize=(8,6))
plt.hist(data1, bins=100, color = "steelblue", alpha=1.0, label="Total")
plt.hist(data2, bins=100,color = "mediumaquamarine", alpha=1.0, label="Quebec")
#plt.hist(data3, bins=100, alpha=0.5, label="Potassium (K)")
x = 10
y = 90
plt.axvline(x, color='k', linestyle='dashed', linewidth=1)
plt.axvline(y, color='k', linestyle='dashed', linewidth=1)
plt.xlabel("Stem count", size=14)
plt.ylabel("No. of obsevation", size=14)
#plt.title("Multiple Histograms with Matplotlib")
plt.legend(loc='best')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig("Total_Quebec_Overlapping_histogram.jpg", dpi= 500)


plt.figure(figsize=(8,6))

plt.hist(data2, bins=100,color = "mediumaquamarine", alpha=1, label="Quebec")
plt.hist(data5, bins=50, color = "bisque", alpha=1, label="Manitoba")
plt.hist(data4, bins=30, color = "burlywood", alpha=1, label="Ontario")
plt.hist(data3, bins=10, color = "aquamarine", alpha=1, label="Nova Scotia")


#plt.hist(data3, bins=100, alpha=0.5, label="Potassium (K)")
x = 10
y = 90
plt.axvline(x, color='k', linestyle='dashed', linewidth=1)
plt.axvline(y, color='k', linestyle='dashed', linewidth=1)
plt.xlabel("Stem count", size=14)
plt.ylabel("No. of obsevation", size=14)
#plt.title("Multiple Histograms with Matplotlib")
plt.legend(loc='best')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig("Combined_province_Overlapping_histogram.jpg", dpi= 500)





