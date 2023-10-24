import pandas as pd
from data_read import read_xls

# 读取CSV文件
data = read_xls('/Users/njw/Desktop/dr/wind_farm_abnormal_data/data/shaofolin/sum_09_data.xlsx')  # 使用'\t'作为列分隔符

# 按日期分组数据
grouped = data.groupby('日期')

# 指定要保留的列
selected_columns = ['日期', '时间','风速(m/s)', '短期预测功率(MW)','实际功率(MW)']

# 遍历每个日期分组
for date, group in grouped:
    # 创建一个新的DataFrame只包含指定列
    new_df = group[selected_columns]

    # 将日期格式化为YYYY-MM-DD形式，以便用作文件名
    formatted_date = pd.to_datetime(date).strftime('%Y-%m-%d')

    # 保存为Excel文件
    file_name = f'/Users/njw/Desktop/dr/wind_farm_abnormal_data/data/shaofolin/wendang/{formatted_date}_data.xlsx'
    new_df.to_excel(file_name, index=False)
    print(f"Saved {file_name}")

print("Splitting and saving completed.")
