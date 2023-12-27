import pandas as pd
#load dataset
data=pd.read_csv("C:/test/",delimiter=',')
data.head()

data['Angle'].plot()


import numpy as np

Fs = 60
varCount=0
varHold = np.zeros(len(data['Angle']))
varDur = []
flag = np.zeros(len(data['Angle']))

Thres = 150 

for i in range(len(data['Angle'])):
	if data['Angle'][i]<Thres:
		flag[i]=1
	else:
		flag[i]=0
        
	varHold[i] = varHold[i-1] + flag[i]
    
    if varHold[i]==varHold[i-1] and varHold[i]>40:
        varCount+=1
        varDur.append(varHold[i])
        varHold[i]=0

print("Given Data performed {0:d} times of Squat with correct posture".format(varCount))
avgDur = sum(varDur)/len(varDur)

print("Average posture duration is {0:.2f} sec".format(avgDur/Fs))