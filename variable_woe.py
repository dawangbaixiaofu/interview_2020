import pandas as pd
import numpy as np

def woe_number_value(df,variable,flag,bins):
    """
    对分类型变量分箱后计算woe值和IV值
    :param df: 数据框
    :param variable: 进行分组依据的变量标签
    :param flag: 进行统计的个数标签
    :return: woe和IV值
    """
    variable_box = variable+"_box"
    variable_woe = variable+"_woe"

    df[variable_box] = pd.cut(df[variable],bins=bins)
    bad = df[flag].sum()
    good = df[flag].count()-bad
    group = df[flag].groupby(df[variable_box])
    group_bad = group.sum()
    group_good = group.count()-group_bad

    group_good_ratio = group_good/good
    group_bad_ratio = group_bad/bad

    woe = np.log(group_good_ratio/group_bad_ratio)
    woe_dataframe = pd.DataFrame({'woe': woe})
    iv = (group_good_ratio-group_bad_ratio)*woe
    IV = iv.sum()

    df[variable_woe] = pd.merge(df,woe_dataframe,left_on=variable_box,right_index=True,how='inner')['woe']
    return df,woe,IV
