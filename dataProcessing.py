import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('./adult.data')
# 去字符串中的空格，数据 类型转换
cols = [x for x in data.columns if x != 'age']
for col in cols:
     data[col] = data[col].map(lambda x: None if x.strip() in ('?','null') else x.strip())
     if col in ('education_num','capital_gain','capital_loss','hours_per_week'):
          data[col] = data[col].map(lambda x:None if x is None else int(x))


# question1: 一共多少条数据记录？
print('数据总数：%s条' %len(data))
# 统计各个列缺失值个数
for col in cols:
     null_num = data[col].isnull().sum()
     print(col+'缺失值个数是：%s个'%null_num)


drop_index = data[data['label'].isnull()].index
data.drop(drop_index, inplace=True)
data['label'] = data['label'].map(lambda x:1 if x == '>50K' else 0)
print('删除label为null的字段后样本数：%s条' %len(data))

# question2:每个字段中的异常值（含缺失值）分别有多少？


# 异常值统计 连续性变量和分类型变量分别进行统计
null_num = data['age'].isnull().sum()
L,U=data['age'].quantile([.25,.75])
IQR = U-L
upper = U+1.5*IQR
lower = L-1.5*IQR

# upper = 78所以大于78岁的为异常值，lower=-2
# 观察age的分布
age_good = data['label'].groupby(data['age']).sum()
age_count = data['label'].groupby(data['age']).count()
age_ratio = age_good/age_count


figure = plt.figure(1)
ax = figure.add_subplot(1,1,1)
ax.plot(age_ratio.index,age_ratio)

figure.show()
# print('年龄分布情况：',age_ratio)

# 从分布图中可以看出年龄和收入大于5K比例呈倒U型分布，异常在79岁开始表现异常
age_outlier = data.loc[data['age']>78,'age'].value_counts()
print('age 异常值：\n', age_outlier.sort_index())

# 对表现异常的样本进行删除
drop_index = data[data['age']>=79].index
data.drop(drop_index, inplace=True)




# 对workclass进行分析
workclass=data['workclass'].value_counts().sort_values()
workclass_good = data['label'].groupby(data['workclass']).sum()
workclass_count = data['label'].groupby(data['workclass']).count()
workclass_ratio = workclass_good/workclass_count

# Never-worked Without-pay 中人群没有超过50K 的，可以作为强规则，作为异常点处理，null值和Private最接近，使用private填充
workclass_outlier = data.loc[data['workclass'].isin(['Never-worked', 'Without-pay']),'workclass'].value_counts()
print('workclass的异常点统计：\n',workclass_outlier)

drop_index = data[data['workclass'].isin(['Never-worked', 'Without-pay'])].index
data.drop(drop_index,inplace=True)

# 对null值的处理
data['workclass'].fillna(value='Private',inplace=True)


# fnlwgt
fnlwgt = data['fnlwgt'].value_counts().sort_values()

# education
education = data['education'].value_counts().sort_values()
education_good = data['label'].groupby(data['education']).sum()
education_count = data['label'].groupby(data['education']).count()
education_ratio = education_good/education_count

# Preschool为0 为异常值 null值和Prof-school最为接近,但是null值只有3个，建议直接删除
education_outlier = data.loc[data['education']=='Preschool','education'].value_counts()
print('education的异常点统计：\n', education_outlier)
drop_index = data.loc[data['education']=='Preschool','education'].index
data.drop(drop_index,inplace=True)
data.dropna(inplace=True,subset=['education'])

# education_num
col = 'education_num'
col_stas = data[col].value_counts().sort_values()
col_good = data['label'].groupby(data[col]).sum()
col_count = data['label'].groupby(data[col]).count()
col_ratio = col_good/col_count
# education_num = 1 为异常值，null为2个，建议剔除
education_num_outlier = data.loc[data[col]==1,col].value_counts()
print('education_num的异常点统计：', education_num_outlier)
drop_index = data.loc[data[col]==1,col].index
data.drop(drop_index,inplace=True)
data.dropna(inplace=True,subset=[col])


col = 'martial_status'
col_stas = data[col].value_counts().sort_values()
col_good = data['label'].groupby(data[col]).sum()
col_count = data['label'].groupby(data[col]).count()
col_ratio = (col_good/col_count).sort_values()

# null值一个建议删除
data.dropna(inplace=True,subset=[col])


# occupation
col = 'occupation'
col_stas = data[col].value_counts().sort_values()
col_good = data['label'].groupby(data[col]).sum()
col_count = data['label'].groupby(data[col]).count()
col_ratio = (col_good/col_count).sort_values()

ratio = data.loc[data[col].isnull(),'label'].sum()/data.loc[data[col].isnull(),'label'].count()
# null值较多不建议删除与Armed-Forces最为接近，使用其填充
data[col].fillna(value='Armed-Forces',inplace=True)



# relationship
col = 'relationship'
col_stas = data[col].value_counts().sort_values()
col_good = data['label'].groupby(data[col]).sum()
col_count = data['label'].groupby(data[col]).count()
col_ratio = (col_good/col_count).sort_values()

# null值较少，建议直接删除。
data.dropna(inplace=True, subset=[col])

# race
col = 'race'
col_stas = data[col].value_counts().sort_values()
col_good = data['label'].groupby(data[col]).sum()
col_count = data['label'].groupby(data[col]).count()
col_ratio = (col_good/col_count).sort_values()

# null值较少建议直接删除
data.dropna(inplace=True, subset=[col])

# sex
col = 'sex'
col_stas = data[col].value_counts().sort_values()
col_good = data['label'].groupby(data[col]).sum()
col_count = data['label'].groupby(data[col]).count()
col_ratio = (col_good/col_count).sort_values()

# null值较少，建议直接删除
data.dropna(inplace=True, subset=[col])

# capital_gain
col = 'capital_gain'
null_num = data[col].isnull().sum()
# null值有4个建议删除
data.dropna(inplace=True, subset=[col])


col = 'capital_loss'
null_num = data[col].isnull().sum()
# null值2个建议直接删除
data.dropna(inplace=True, subset=[col])

# hours_per_week

col = 'hours_per_week'
null_num = data[col].isnull().sum()
# null为2个建议直接删除
data.dropna(inplace=True, subset=[col])
# 最大值为99，最小值是1



# native_country
col = 'native_country'
col_stas = data[col].value_counts().sort_values()
col_good = data['label'].groupby(data[col]).sum()
col_count = data['label'].groupby(data[col]).count()
col_ratio = (col_good/col_count).sort_values()
ratio_null = data.loc[data[col].isnull(),'label'].sum()/data.loc[data[col].isnull(),'label'].count()

# Outlying-US(Guam-USVI-etc) Holand-Netherlands
#  为异常值 null值较多不建议删除与Scotland 填充
native_country_outlier = data.loc[data[col].isin(['Outlying-US(Guam-USVI-etc)','Holand-Netherlands']),col].value_counts()
print('native_country outlier 样本数：\n', native_country_outlier)

drop_index = data[data[col].isin(['Outlying-US(Guam-USVI-etc)','Holand-Netherlands'])].index
data.drop(drop_index,inplace=True)
data[col].fillna(value='Scotland',inplace=True)


data.to_csv('./dataProcessed.csv',index=False)

