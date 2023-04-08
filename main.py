from data_processing import cholesterol_mean

data = cholesterol_mean()

data_v01 = data.to_csv('heartFile_processed.csv', sep=',',encoding='utf-8',index=False)