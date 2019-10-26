#Load dataset and turn into pandas dataframe

Smashfly = pd.read_csv("SF_Datathon_Data.csv", encoding='utf-8')
sf_df = pd.DataFrame(Smashfly)
print(sf_df.head())
jobs_unique = sf_df['Job_Type'].unique()

cat_columns = ["Qualification_type", "Job_Type", "Race"]
print(sf_df.columns)
sf_df = pd.get_dummies(sf_df, prefix_sep="_", columns=cat_columns)

print(sf_df.columns)
