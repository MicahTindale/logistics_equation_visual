import sys
import matplotlib.pyplot as plt

#program will crash without setting recursion limit
sys.setrecursionlimit(1500)

#recursion is required to find the value that the logistical equation settles on
def logisticalEquation(r, x, depth, i=0, arr = []):
    arr.append(x)
    if i < depth:
        logisticalEquation(r, r * x * (1 - x), depth, i+1, arr)
    return arr


#returns one or more values, depending on the numbers that the logistics algorithm settles on
def valsCreator(oArr, threshold):
    arr = [oArr[len(oArr) - 1]]

    #if the logistics algorithm settles on more than one number, add the other numbers to 'arr'
    for i in range(15):
        x = oArr[len(oArr) - 2 - i]
        add = True
        for y in arr:
            if (x > y - threshold) and (x < y + threshold):
                add = False
        if add:
            arr.append(x)
    return arr


def dataCreator(x):
    #r is the x coordinate
    r = 1
    #bifurcation array - used to find the points where the plot splits
    bifArr = []

    xData = []
    yData = []
    while r < 4:
        myArr = valsCreator(logisticalEquation(r, x, 1000), 0.006 / r)
        num = len(myArr)
        if not bifArr.__contains__(num):
            bifArr.append(num)
            print("Bifurcation of " + str(num) + " at r = " + str(r))
        for i in myArr:
            xData.append(r)
            yData.append(i)
        r += 0.005 #increment r slightly

    #returns a two dimensional array
    return [xData, yData]

myData = dataCreator(0.4)
plt.scatter(myData[0], myData[1], s=0.5)
plt.title("Logistics Algorithm Initial X = 0.4")
plt.show()