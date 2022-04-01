import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

pmean = statistics.mean(data)
print(pmean)

pstd = statistics.stdev(data)
print(pstd)

def get_sample_mean():
    dataset = []
    for i in range(0,100):
       random_index = random.randint(0, len(data)-1)
       value = data[random_index]
       dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

meanlist = []
for i in range(0,1000):
    sampleMean = get_sample_mean()
    meanlist.append(sampleMean)

smean = statistics.mean(meanlist)
print(smean)

stdev_sample = statistics.stdev(meanlist)
print(stdev_sample)

zone1_start,zone1_end = smean - stdev_sample,smean+stdev_sample
zone2_start,zone2_end = smean - 2*stdev_sample,smean+2*stdev_sample
zone3_start,zone3_end = smean - 3*stdev_sample,smean+3*stdev_sample

df1 = pd.read_csv("data1.csv")
data1 = df1["Math_score"].tolist()
mean1 = statistics.mean(data1)

df2 = pd.read_csv("data2.csv")
data2 = df2["Math_score"].tolist()
mean2 = statistics.mean(data2)

df3 = pd.read_csv("data3.csv")
data3 = df3["Math_score"].tolist()
mean3 = statistics.mean(data3)


fig = ff.create_distplot([meanlist],["Sampling Mean Distrubution"],show_hist = False)
fig.add_trace(go.Scatter(x = [smean,smean],y = [0,0.18],mode = "lines",name = "mean"))
fig.add_trace(go.Scatter(x = [zone1_end,zone1_end],y = [0,0.18],mode = "lines",name = "zone1"))
fig.add_trace(go.Scatter(x = [zone2_end,zone2_end],y = [0,0.18],mode = "lines",name = "zone2"))
fig.add_trace(go.Scatter(x = [zone3_end,zone3_end],y = [0,0.18],mode = "lines",name = "zone3"))
fig.add_trace(go.Scatter(x = [mean1,mean1],y = [0,0.18],mode = "lines",name = "tabs"))
fig.add_trace(go.Scatter(x = [mean2,mean2],y = [0,0.18],mode = "lines",name = "extra_clases"))
fig.add_trace(go.Scatter(x = [mean3,mean3],y = [0,0.18],mode = "lines",name = "fun_sheets"))

fig.show()

zscore1 = (mean1-smean)/stdev_sample
print("zscore of first sample 'tabs' ",zscore1)

zscore2 = (mean2-smean)/stdev_sample
print("zscore of second sample 'tabs' ",zscore2)

zscore3 = (mean3-smean)/stdev_sample
print("zscore of third sample 'tabs' ",zscore3)