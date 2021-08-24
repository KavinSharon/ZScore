import pandas as pd
import csv
import plotly.figure_factory as ff
import random
import statistics
import plotly.graph_objects as go

df = pd.read_csv("pro/sampleDistribution/medium_data.csv")
data = df["reading_time"].tolist()

mean = statistics.mean(data)
stdDev = statistics.stdev(data)

print("Population Mean Is",mean)
print("Population Standard Deviation Is",stdDev)

def randomSetOfMean(counter):
    dataSet = []
    for i in range(1,counter):
        data_index = random.randint(0,len(data)-1)
        value = data[data_index]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean
meanList = []
for i in range(0,1000):
    setOfMean = randomSetOfMean(100)
    meanList.append(setOfMean)
sampleMean = statistics.mean(meanList)
stdError = statistics.stdev(meanList)
print("The Sample Mean Is ", sampleMean)
print("The Standard Error Is ", stdError)

firstStddevStart,firstStddevEnd = sampleMean-stdError,sampleMean+stdError
secondStddevStart,secondStddevEnd = sampleMean-(2*stdError),sampleMean+(2*stdError)
thirdStddevStart,thirdStddevEnd = sampleMean-(3*stdError),sampleMean+(3*stdError)

zScore = (mean-sampleMean)/stdError
print("Z Score Is ",zScore)


