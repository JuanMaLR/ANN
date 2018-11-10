from random import randrange,uniform
from copy import deepcopy

class neuron:
    def __init__ ( self , numWeight , learnRate):
        self.weights = []
        for x in range(0, (numWeight+1)):
            self.weights.append(float(uniform(1,10))/10.0)
        self.LR = learnRate

    def obtainOutput(self,input):
        treshhold = self.weights[0]
        sum = 0.0;
        for x in range(0,len(input)):
            sum += (input[x]*self.weights[x+1])
        if sum > treshhold:
            return 1
        else:
            return 0

    def updateWeights(self,inputsAndOutput):
        dataLenght = len(inputsAndOutput)
        auxArr = deepcopy(inputsAndOutput)
        wantedOutput = int(auxArr[dataLenght-1])
        inputNum = []
        for x in range(0,dataLenght-1):
            inputNum.append(float(inputsAndOutput[x]))
        realOutput = self.obtainOutput(inputNum)
        #print(str(wantedOutput) + " " + str(realOutput))
        #print(self.weights)
        #self.weights[0] = self.weights[0] + self.LR*(wantedOutput-realOutput)
        for x in range(0,len(inputNum)):
            deltaW = self.LR*(wantedOutput-realOutput)*inputNum[x]
            self.weights[x+1] = self.weights[x+1] + deltaW


d = int(input())
m = int(input())
n = int(input())

dataSet = []
for x in range(0, m):
    dataSet.append(input().split(','))

testSet = []
for x in range(0, n):
    testSet.append(input().split(','))
perceptron = neuron(d,0.1)
count = 0
iniW = []
iniW = perceptron.weights
finW = []
flag = True

while (count<1000) and flag:

    flag = False
    iniW = deepcopy(perceptron.weights)

    for Line in dataSet:
        perceptron.updateWeights(Line)
        finW = deepcopy(perceptron.weights)
        if flag==False:
            for w in range(0,len(iniW)):
                if iniW[w]!=finW[w]:
                    flag = True
    count+=1
#print(count)
if count == 1000:
    print("no solution found")
    exit()

for Line in testSet:
    inp = []
    for x in range(0,len(Line)):
        inp.append(float(Line[x]))
    print(perceptron.obtainOutput(inp))


#print(dataSet)
#print(testSet)
#print(perceptron.weights)
