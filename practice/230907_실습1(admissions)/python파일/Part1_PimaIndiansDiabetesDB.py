import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt

data = 'D:/HCI개론-캡스톤/230907_실습1(admissions)/diabetes.csv'
df = pd.read_csv(data)
print(df.shape)
df.head() #데이터셋 검토

df.describe().transpose() #데이터 요약 (꿀 기능)

cor = df.corr() #데이터 상관계수 구하기
sns.heatmap(cor)
plt.show()


#타깃 변수인 Outcome을 ‘hue’로 지정하여, Outcome 값에 따른 예측 변수의 분포 시각화
sns.pairplot(df,hue='Outcome')