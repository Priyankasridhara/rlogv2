from pandas import ExcelFile, read_excel
xlsx= ExcelFile("Candidate Pipeline Data - Dnyanada")
df= read_excel(xlsx, 'Datasheet')
df['is_duplicated']=df.duplicated(['Job_ID','Company_ID'])
print(df['is_duplicated'])
print(df['is_duplicated'].sum())

df_nodup=df.loc[df['is_duplicated']== True]
print(df_nodup)
df.drop_duplicates(subset=['Job_ID','Company_ID'],keep='first',inplace=True)
df['is_duplicates']=df.duplicated(['Job_ID','Company_ID'])
print(df['is_duplicates'])
print(df['is_duplicates'].sum())

