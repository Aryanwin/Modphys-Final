import csv
import math

signals = []
backgrounds = []
eqval = []

with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        backgrounds.append(row[0])
        signals.append(row[1])
        
signals.pop(0)
backgrounds.pop(0)
for i in range(len(signals)):
    signals[i] = float(signals[i])
backgrounds = backgrounds[:-22]
for i in range(len(backgrounds)):
    backgrounds[i] = float(backgrounds[i])

signalcount = len(signals)

for i in range(int(max(signals))):
    valCount = len([x for x in signals if x>i])
    valCount2 = len([x for x in backgrounds if x>i])
    eqval.append((18880000*valCount/len(signals))/(2.5+math.sqrt(284894400*valCount2/len(backgrounds))))

print("Invariant mass max Punzi criterion: " + str(max(eqval)));
print("Cut at: >" + str(eqval.index(max(eqval))))


signals2 = []
backgrounds2 = []
eqval2 = []

with open('data2.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        backgrounds2.append(row[0])
        signals2.append(row[1])
        
signals2.pop(0)
backgrounds2.pop(0)
for i in range(len(signals2)):
    signals2[i] = float(signals2[i])
backgrounds2 = backgrounds2[:-30]
for i in range(len(backgrounds2)):
    backgrounds2[i] = float(backgrounds2[i])

signalcount = len(signals2)

for i in range(int(max(signals2))):
    valCount = len([x for x in signals2 if x < i])
    valCount2 = len([x for x in backgrounds2 if x<i])
    eqval2.append((18880000*valCount/len(signals2))/(2.5+math.sqrt(284894400*valCount2/len(backgrounds2))))

print("pT max Punzi criterion: " + str(max(eqval2)));
print("Cut at: >" + str(eqval2.index(max(eqval2))))

signals3 = []
backgrounds3 = []
eqval3 = []

with open('data3.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        signals3.append(row[0])
        backgrounds3.append(row[1])
#print(len(signals3))
#print(len(backgrounds3))
signals3.pop(0)
backgrounds3.pop(0)
for i in range(len(signals3)):
    signals3[i] = float(signals3[i])
    #print(signals3[i])
#backgrounds2 = backgrounds2[:-30]
for i in range(len(backgrounds3)):
    backgrounds3[i] = float(backgrounds3[i])

for i in range(int(max(signals3))*20):
    valCount = len([x for x in signals3 if x < i/20])
    valCount2 = len([y for y in backgrounds3 if y < i/20])
    eqval3.append((18880000*valCount/len(signals3))/(2.5+math.sqrt(284894400*valCount2/len(backgrounds3))))
    #print(valCount)
    #print(valCount2)
    #print((18880000*valCount/len(signals3))/(2.5+math.sqrt(284894400*valCount2/len(backgrounds3))))
    #print(" ")
    
#print(eqval3)
#print(len(signals3))
#print(len(backgrounds3))
print("Delta R Punzi criterion: " + str(max(eqval3)));
print("Cut at: <" + str(eqval3.index(max(eqval3))/20))
