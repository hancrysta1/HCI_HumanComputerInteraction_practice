
import pandas as pd
from datetime import datetime, timedelta


df = pd.read_csv('ADMISSIONS.csv', encoding='cp949')


#2) 평균 입원 일 구하기
sum_time = 0
for i in range(len(df)):
    admittime = datetime.strptime(df['admittime'][i], '%Y-%m-%d %H:%M:%S')
    distime = datetime.strptime(df['dischtime'][i], '%Y-%m-%d %H:%M:%S')
    time = timedelta.total_seconds(distime-admittime)
    sum_time += time

#3) 입원 유형과 카운트
admit_type = list(set(df['admission_type']))
admit_type_count = []
for v in admit_type:
    count =0;
    for i in range(len(df)):
        if(df['admission_type'][i]==v):
            count+=1
    admit_type_result = v+": "+str(count)+"명"
    admit_type_count.append(admit_type_result)

#4) 진단명(diagnosis)의 종류와 진단별 환자 수
diag_type = list(set(df['diagnosis']))
diag_type_count = []
for v in diag_type:
    count =0;
    for i in range(len(df)):
        if(df['diagnosis'][i]==v):
            count+=1
    diag_type_result = v+": "+str(count)+"명"
    diag_type_count.append(diag_type_result)



#결과 출력        
print("1) 총 환자 수 : ",len(df),"명")
print("2) 평균 입원시간 : ",datetime.fromtimestamp(sum_time / len(df)).strftime('%d'),"일")
print("3) 입원 유형(admission_type)의 종류와 유형별 환자 수 : ")
for i in admit_type_count:
    print(i)
print("")
print("4) 진단명(diagnosis)의 종류와 진단별 환자 수 : ")
for i in diag_type_count:
    print(i)