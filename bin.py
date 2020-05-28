# 对字符分类型性变量采用负样本占比差异最大化进行分箱
# 对数值型连续性变量采用卡方分箱

import pandas as pd
# from chi2_bins import Chi2Box
from variable_woe import woe_number_value
import matplotlib.pyplot as plt

data = pd.read_csv('./dataProcessed.csv')
data.drop(columns=['fnlwgt'],inplace=True)
# 字符型变量处理
col = 'sex'
dic = {'Male':1,'Female':0}
data[col]  = data[col].map(dic)

col = 'workclass'
dic = {'Private':1,'State-gov':2,'Self-emp-not-inc':3,'Local-gov':4, 'Federal-gov':5,'Self-emp-inc':6}
data[col]  = data[col].map(dic)

col = 'education'
dic = {'1st-4th':1,'5th-6th':2,'11th':3,'9th':3,'7th-8th':3,'10th':3,'12th':4, 'HS-grad':5,'Some-college':6,'Assoc-acdm':7
       ,'Assoc-voc':7,'Bachelors':8,'Masters':9,'Prof-school':10,'Doctorate':10}
data[col] = data[col]  = data[col].map(dic)

col = 'martial_status'
dic = {'Never-married':1,'Separated':2,'Married-spouse-absent':3,'Widowed':3,'Divorced':4,'Married-AF-spouse':5,'Married-civ-spouse':6}
data[col]  = data[col].map(dic)


col='occupation'
dic={'Priv-house-serv':1,'Other-service':2,'Handlers-cleaners':2,'Armed-Forces':3,'Farming-fishing':3,'Machine-op-inspct':4,'Adm-clerical':4
     ,'Transport-moving':5,'Craft-repair':5,'Sales':6,'Tech-support':7,'Protective-serv':7,'Prof-specialty':8,'Exec-managerial':9}
data[col]  = data[col].map(dic)

col = 'relationship'
dic = {'Own-child':1,'Other-relative':2,'Unmarried':3,'Not-in-family':4
,'Husband':5,'Wife':5}
data[col]  = data[col].map(dic)

col = 'race'
dic={'Other':1,'Amer-Indian-Eskimo':2,'Black':3,'White':4,'Asian-Pac-Islander':5
}
data[col]  = data[col].map(dic)

col = 'native_country'
dic={'Dominican-Republic':1,
'Columbia':1,
'Guatemala':1,
'Mexico':2,
'Nicaragua':2,
'Peru':2,
'Vietnam':2,
'Honduras':2,
'El-Salvador':2,
'Haiti':2,
'Trinadad&Tobago':3,
'Portugal':3,
'Puerto-Rico':3,
'Ecuador':3,
'Laos':3,
'Jamaica':3,
'Thailand':3,
'Poland':4,
'South':4,
'Ireland':4,
'United-States':5,
'Scotland':5,
'Hungary':5,
'Cuba':6,
'China':6,
'Greece':6,
'Philippines':6,
'Hong':6,
'Germany':7,
'Canada':7,
'England':7,
'Italy':7,
'Yugoslavia':7,
'Japan':7,
'Cambodia':7,
'Taiwan':7,
'India':7,
'France':7,
'Iran':7
}
data[col]  = data[col].map(dic)



# result_box, chi2 = Chi2Box(df=data,variable='age',flag='label',bins=10)
# result_box.to_csv('./age_bin.csv')
# result_box, chi2 = Chi2Box(df=data,variable='education_num',flag='label',bins=10)
# result_box.to_csv('./education_num_bin.csv')
# result_box, chi2 = Chi2Box(df=data,variable='capital_gain',flag='label',bins=10)
# result_box.to_csv('./capital_gain_bin.csv')
# result_box, chi2 = Chi2Box(df=data,variable='capital_loss',flag='label',bins=10)
# result_box.to_csv('./capital_loss_bin.csv')
# result_box, chi2 = Chi2Box(df=data,variable='hours_per_week',flag='label',bins=10)
# result_box.to_csv('./hours_per_week_bin.csv')


bin_age = [0,21,23,27,29,33,36,43,61,68,78]
bin_workclass = [0,1,2,3,4,5,6]
bin_education = [0,1,2,3,4,5,6,7,8,9,10]
bin_education_num = [-1,8,9,10,12,13,14,16]
bin_martial_status = [0,1,2,3,4,5,6]
bin_occupation = [0,1,2,3,4,5,6,7,8,9]
bin_relationship = [0,1,2,3,4,5]
bin_race = [0,1,2,3,4,5]
bin_sex = [-1,0,1]
bin_capital_gain = [-1,2993,4101,7443,10566,99999]
bin_capital_loss = [-1,1539,1902,4365]
bin_hours_per_week = [-1,34,39,43,49,54,99]
bin_native_country = [0,1,2,3,4,5,6,7]

IV_temp = []
cols = data.columns
label = 'label'
features = [x for x in cols if x!=label]


for feature in features:
    bin = 'bin_'+feature
    df , woe, IV = woe_number_value(df=data, variable=feature, flag='label',bins=eval(bin))
    IV_temp.append(IV)

IV_dataFrame = pd.DataFrame({'iv':IV_temp},index=features)
IV_dataFrame.to_csv('./total_IV.csv')
df.to_csv('./total_woe.csv')

features_num = range(len(features))
fig = plt.figure(1)
ax = fig.add_subplot(1,1,1)
ax.bar(features_num,IV_temp,tick_label=features)
plt.xticks(rotation=90)
plt.show()

