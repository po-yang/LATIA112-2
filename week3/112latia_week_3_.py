# -*- coding: utf-8 -*-
"""112LATIA_week_3 .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12kk8Kvc1EXTcYWqJCk3_wu7EveD_8kEw
"""

from google.colab import drive
drive.mount('/content/gdrive/')

import os
os.chdir("/content/gdrive/My Drive/")

import pandas as pd

csv_file = '/content/gdrive/My Drive/112-2LATIA/week2/112_student.csv'

df = pd.read_csv(csv_file, encoding='utf-8')

#columns = [
#    "學年度","學校代碼","學校名稱","日間∕進修別","等級別","總計","男生計",
#    "女生計","一年級男","一年級女","二年級男","二年級女","三年級男","三年級女",
#    "四年級男","四年級女","五年級男","五年級女","六年級男","六年級女",
#    "七年級男","七年級女","延修生男","延修生女","縣市名稱","體系別"
#]
df = pd.read_csv(csv_file, encoding='utf-8')
#print(df.head())

#查看資料欄位資訊
print(df.info(verbose=True, show_counts=True))

#查看資料的統計學資訊描述
#print(df.describe())

"""# 1. 哪間大專院校有最多的學士生

"""

df1 = df[['總計']] # 取出想要觀看的欄位
print("本資料集共有", len(df1), "筆紀錄")

df1_1 = df1[df['等級別'] == 'B 學士']
print("有招生學士學制的學校數量為", df1_1, "\n")
df1_1_sorted = df1_1.sort_values(by = "總計", ascending = False)
max_school_index = df1_1_sorted.index[0]
max_school_name = df.loc[max_school_index, '學校名稱']
print("112學年度在籍的學士生最多人數之學校",max_school_name )

"""# 2. 國立？所；私立？所"""

type_list = [] # 建立空字串

for i in df['學校名稱']:
    if ('國立' in i) or ('市立' in i):
        type_list.append('國立')
    else:
        type_list.append('私立')

df['公私立'] = type_list # 將 Dataframe 新增「公私立」column

df2 = df.drop_duplicates('學校名稱')
count = df2['公私立'].value_counts()

print(df2)
print(f"本資料集共收集了 {len(df2)} 所學校，其中公立：{count['國立']} 所；私立：{count['私立']} 所。")

"""# 3. 各等級別學制共有？所"""

df3 = df.drop_duplicates(subset=['學校名稱', '等級別'])
count = df3['等級別'].value_counts()
degree_list = list(df['等級別'].unique())

print(f"本資料集總共收集了 {len(set(df3['學校名稱']))} 所學校，各等級學制當中：")
for degree in degree_list:
    print(f"一共有{count[degree]} 所學校， 有招收{degree}。")

"""# 4.博士生有幾人"""

doctoral_students = df[df['等級別'] == 'D 博士']['總計'].sum()
print("博士生共有", doctoral_students, "人")

doctoral_students = df[df['等級別'] == 'D 博士']
school_doctoral_counts = doctoral_students.groupby('學校名稱')['總計'].sum()
print(school_doctoral_counts)