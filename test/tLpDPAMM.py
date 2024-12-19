import math
import sys
sys.path.insert(0,r'/DEFINE-YOUR-PATH-HERE/LP-Accounting-DPAMM-CPAMM/src') # add your path
from lpDPAMM import deposit,withdraw

# Pool Variable
balanceX = 0
balanceY = 0
priceX = 0
totalLpX = 0
totalLpY = 0

# LP's holding
LpX1 =0
LpY1 =0
holdX1 = 700
holdY1 = 10000

LpX2 =0
LpY2 =0
holdX2 = 0
holdY2= 0

LpX3 =0
LpY3 =0
holdX3 = 0
holdY3= 0

def getK():
    return balanceX*balanceY
def getRatio():
    return balanceY/balanceX

def testLpDPAMM():
    global totalLpX, totalLpY, balanceX, balanceY, LpX1, LpY1 , LpX2, LpY2, LpX3, LpY3 , holdX1, holdY1, holdX2, holdY2, holdX3, holdY3

    #Lp1 deposit + initiate the price to be as x=700 and y=1000 as in CPAMM
    priceX = 10000/700 # y/x in CPAMM
    LpX1, LpY1 = deposit(holdX1,holdY1, priceX, totalLpX, totalLpY, balanceX, balanceY)
    totalLpX += LpX1
    totalLpY += LpY1
    balanceX+=holdX1
    balanceY+=holdY1
    holdX1 = 0
    holdY1 = 0
    print()
    print("+++++ Lp1 initialize pool's liquidity")
    print("LP1/pool has LPX tokens: ", LpX1)
    print("LP1/pool has LPY tokens: ", LpY1)
    print("--------------------------")

    #1st swap
    currentRatio = getRatio()
    newX = balanceX - (balanceX/5) #20% of balance X if traded out
    newY = getK()/newX
    yIn = newY - balanceY
    newRatio = newY/newX
    priceX = (newRatio/currentRatio)*priceX
    balanceX = newX
    balanceY = newY
    print()
    print("+++++ 1st Swap")
    print("--------------------------")

    #Lp2 deposit
    LpX2, LpY2 = deposit(balanceX, balanceY, priceX, totalLpX, totalLpY, balanceX, balanceY)
    totalLpX += LpX2
    totalLpY += LpY2
    balanceX*=2
    balanceY*=2
    print()
    print("+++++ Lp2 provide liquidty with the same x and y as current LP1's")
    print("COMPARE: LP1 and LP2 have the same amount of LPX tokens = ", LpX1 ,', ', LpX2)
    print("COMPARE: LP1 and LP2 have the same amount of LPY tokens = ", LpY1 ,', ', LpY2)
    print("--------------------------")

    #2nd swap
    currentRatio = getRatio()
    newY = balanceY - (yIn*2)
    newX = getK()/newY
    newRatio = newY/newX
    priceX = (newRatio/currentRatio)*priceX
    balanceX = newX
    balanceY = newY
    print()
    print("+++++ 2nd Swap")
    print("--------------------------")

    #Lp2 withdraw
    holdX2, holdY2 = withdraw(LpX2, LpY2, totalLpX, totalLpY, balanceX, balanceY)
    totalLpX -= LpX2
    totalLpY -= LpY2
    LpX2=0
    LpY2=0
    balanceX -= holdX2
    balanceY -= holdY2
    print()
    print("+++++ LP2 withdraw all liquidity")
    print("COMPARE: balanceX equal to holdX2 = ", balanceX,', ', holdX2) 
    print("COMPARE: balanceY equal to holdY2 = ",balanceY,', ', holdY2)
    print("--------------------------")

    #Lp1 add liquidity to the pool (25% more than he currently has)
    newLpX1, newLpY1 = deposit(balanceX/4, balanceY/4, priceX, totalLpX, totalLpY, balanceX, balanceY)
    totalLpX += newLpX1
    totalLpY += newLpY1
    LpX1 += newLpX1
    LpY1 += newLpY1
    balanceX += balanceX/4
    balanceY += balanceY/4
    print()
    print("+++++ Lp1 deposit more 1/4 of his current liquidity")
    print("LP1/pool has LPX tokens: ", LpX1)
    print("LP1/pool has LPY tokens: ", LpY1)
    print("--------------------------")

    #Lp3 deposit liquidity, 50% of LP1's value
    LpX3, LpY3 = deposit(balanceX/2, balanceY/2, priceX, totalLpX, totalLpY, balanceX, balanceY)
    totalLpX += LpX3
    totalLpY += LpY3
    balanceX += balanceX/2
    balanceY += balanceY/2
    print()
    print("+++++ Lp3 provide liquidty with 1/2 x and 1/2 y of current LP1's")
    print("LP3 has LPX tokens: ", LpX3)
    print("LP3 has LPY tokens: ", LpY3)
    print("COMPARE: LP1 has 2x LP token compared to LP3's = ", LpX1 ,', ',LpX3)
    print("COMPARE: LP1 has 2x LP token compared to LP3's = ", LpY1 ,', ',LpY3)
    print("--------------------------")
    
    #3rd swap
    currentRatio = getRatio()
    newY = balanceY - (balanceY/3)
    newX = getK()/newY
    newRatio = newY/newX
    priceX = (newRatio/currentRatio)*priceX
    balanceX = newX
    balanceY = newY
    print()
    print("+++++ 3rd Swap")
    print("--------------------------")

    #LP3 withdraw all liquidity
    holdX3, holdY3 = withdraw(LpX3, LpY3, totalLpX, totalLpY, balanceX, balanceY)
    totalLpX -= LpX3
    totalLpY -= LpY3
    LpX3=0
    LpY3=0
    balanceX -= holdX3
    balanceY -= holdY3
    print()
    print("+++++ LP3 withdraw all liquidity")
    print("COMPARE: balanceX equal to 2x of holdX3 = ", balanceX,', ', holdX3)
    print("COMPARE: balanceY equal to 2x of holdY3 = ",balanceY,', ', holdY3)
    print("--------------------------")    

    
testLpDPAMM()
    
