
Smashfly = pd.read_csv("SF_Datathon_Data.csv", encoding='utf-8')
sf_df = pd.DataFrame(Smashfly)
#print(sf_df.head())
jobs_unique = sf_df['Job_Type'].unique()

cat_columns = ["Qualification_type", "Job_Type", "Race"]
#print(sf_df.columns)
sf_df = pd.get_dummies(sf_df, prefix_sep="_", columns=cat_columns)
sf_df["Gender_M"] = sf_df["Gender"] == "M"
sf_df["Gender_F"] = sf_df["Gender"] == "F"
sf_df["Gender_Unspecified"] = 1 - sf_df["Gender_F"] - sf_df["Gender_M"]
sf_df["Gender_Unspecified"] = sf_df["Gender_Unspecified"].astype('bool')
del sf_df['Gender']
del sf_df['Name']
sf_df.loc[sf_df['Qualification_type_1']+sf_df['Qualification_type_2']+sf_df['Qualification_type_3'] == 0, ['GPA']] = np.NaN

print(sf_df.columns)
