import pandas as pd


data = pd.read_csv('D:/HCI개론-캡스톤/230907_실습1(admissions)/ADMISSIONS.csv', encoding='cp949')
data.groupby(['religion']).count()['row_id'].plot(kind='pie') #pie차트
data.groupby(['religion']).count()['row_id'].plot(kind='bar') #bar차트

#데이터 결합하여 결과 내기
pdata = pd.read_csv('D:/HCI개론-캡스톤/230907_실습1(admissions)/PATIENTS.csv', encoding='cp949')
mergedata = pd.merge(data,pdata,on = 'subject_id',how='inner')
#ADMISSION.csv 파일의 subject_id와 PATIENTS.csv 파일의 subject_id를 통해 이너조인
mergedata.groupby(['religion','gender']).size().unstack().plot(kind="bar",stacked=True)
#솔직히 이 부분 이해 X 이게 왜 결과가 이런지 공부하기