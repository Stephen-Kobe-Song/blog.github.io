import pandas as pd
import os
'''
    将文件目录下所有的Excel文件名放入到filename里面
'''
filename = []
path = r'D:\标注过的培训数据'
for file in os.listdir(path):
    filename.append(file)
# print(len(filename))
os.chdir('D:\标注过的培训数据')  # 设置默认读取路径！
date = []
writer = pd.ExcelWriter('2.xlsx',engine='openpyxl')
for file in filename:
    df = pd.read_excel(file)
    # print(df)
    lable = df.values[:,8]
    date.append(lable)
# print(date[0])
df = pd.DataFrame(date, )
df.to_excel(writer)  # 将数据写入excel
writer.save()  # 保存
print("写入完成！")

