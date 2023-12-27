import pandas as pd
import datetime
import numpy as np

data = pd.read_csv('ADMISSIONS.csv', encoding='cp949', delimiter=',')
data.set_index('row_id', inplace=True)
data.head()

print(data.shape) #행열

dataformat = "%Y-%m-%d %H:%M:%S"
admit_dur = []

#2) 평균 입원 시간
for i in range(len(data)):
    start_date = data['admittime'][data.index[i]]
    end_date = data['dischtime'][data.index[i]]
    
    start_convert = datetime.datetime.strptime(start_date,dataformat)
    end_convert = datetime.datetime.strptime(end_date,dataformat)
    
    admit_day = (end_convert-start_convert).days
    admit_dur.append(admit_day) #각 환자 별 입원 날짜 추출, append
    
print("2) 평균 입원 일 : ",np.mean(admit_dur)) #np.mean 평균 구하기

print(data['admission_type'].unique()) #pandas data.unique : 그 행 중복제거
print(data['admission_type'].nunique()) #data.nunique : 중복제거했을 때 종류(몇가지?)
print(data['admission_type'].value_counts()) # data.value_counts : 값 마다 몇개씩 있는지

print(data['diagnosis'].unique()) 
print(data['diagnosis'].nunique()) 
print(data['diagnosis'].value_counts())



    
    