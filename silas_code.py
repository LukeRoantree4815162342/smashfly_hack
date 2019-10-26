from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier


train, test = train_test_split(sf_df, test_size=0.15)

features = ['id', 'Age', 'Qualification_type_1',
       'Qualification_type_2', 'Qualification_type_3', 'Qualification_type_4',
       'Qualification_type_5', 'Job_Type_Accounting',
       'Job_Type_Business Development', 'Job_Type_Engineering',
       'Job_Type_Human Resources', 'Job_Type_Legal', 'Job_Type_Marketing',
       'Job_Type_Product Management', 'Job_Type_Research and Development',
       'Job_Type_Sales', 'Job_Type_Services', 'Job_Type_Support',
       'Job_Type_Training', 'Race_Asian', 'Race_Black', 'Race_Latino',
       'Race_Other', 'Race_White', 'Gender_M', 'Gender_F',
       'Gender_Unspecified']

X = train[features]
Y = train['Interviewed']

model1 = DecisionTreeClassifier(max_depth=4, min_samples_leaf=3)
model2 = AdaBoostClassifier(learning_rate=1, n_estimators=200, base_estimator=model1)

#model1.fit(X,Y)
for epoch in range(20):
    model2.fit(X,Y)

model2.score(X,Y)
