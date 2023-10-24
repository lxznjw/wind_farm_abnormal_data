import  pandas as pd
from data_read import read_xls

from utils import calculate_and_save_correlation_matrix,calculate_and_save_rmse,calculate_rmse


# 使用示例
file_name = '/8-10nwp.xls'
file_path = r'/Users/njw/Desktop/dr/wind_farm_abnormal_data/data/shaofolin' + file_name
data_frame = read_xls(file_path)
file_path_gl=r'/Users/njw/Desktop/dr/wind_farm_abnormal_data/data/shaofolin/9月份功率预测.xls'
data_frame_gonglv = read_xls(file_path_gl)




print(data_frame)
print(data_frame_gonglv)

#计算mse
# calculate_and_save_rmse(calculate_rmse,data_frame_gonglv,r'D:\Desktop\wind_farm_abnormal_data\data\shaofolin\RMSE_data.xlsx')

# 使用concat函数合并列
result = pd.concat([data_frame.iloc[2977:5857, :].reset_index(drop=True), data_frame_gonglv.reset_index(drop=True)], axis=1)  # 将df2的列与df1的列合并在一起
result.to_excel(r'/Users/njw/Desktop/dr/wind_farm_abnormal_data/data/shaofolin/sum_09_data.xlsx', index=False, engine='openpyxl')

print(result)

result = result.iloc[:,3:]
print(result)

# calculate_and_save_correlation_matrix(result, r'D:\Desktop\wind_farm_abnormal_data\data\shaofolin\correlation_matrix_Truepower.xls')

#计算
