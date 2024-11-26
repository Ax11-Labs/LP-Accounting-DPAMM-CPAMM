import math
import sys
sys.path.insert(0,'/DEFINE-YOUR-PATH-HERE/LP-Accounting-DPAMM-CPAMM/src') # add your path
from lpCPAMM import deposit,withdraw

# Pool Variable
balanceX = 0
balanceY = 0
totalLP = math.sqrt(balanceX*balanceY)

# LP's holding
Lp1 = 0
holdX1 = 700
holdY1 = 10000

Lp2 = 0
holdX2 = 0
holdY2= 0

Lp3 = 0
holdX3 = 0
holdY3= 0

def getK():
    return balanceX*balanceY

def getTotalLP():
    return math.sqrt(getK())

# def updateHolding(operation, amountX, amountY):
    

def testLpCPAMM():
    global totalLP
    global balanceX
    global balanceY
    global Lp1
    global Lp2
    global Lp3
    global holdX1
    global holdY1
    global holdX2
    global holdY2
    global holdX3
    global holdY3

    #Lp1 deposit
    totalLP = deposit(holdX1,holdY1, 0,0,0,0)
    Lp1= totalLP
    balanceX += holdX1
    balanceY += holdY1
    holdX1 = 0
    holdY1 = 0
    print()
    print("+++++ Lp1 initialize pool's liquidity")
    print("LP1/pool has LP tokens: ", totalLP)
    print("--------------------------")


    #1st swap
    k = getK()
    balanceX -= (balanceX/5) #20% of balance X if traded out
    yIn = k/balanceX - balanceY
    balanceY += yIn
    print()
    print("+++++ 1st Swap")
    print("--------------------------")

    #Lp2 deposit
    Lp2 = deposit(balanceX,balanceY, k, totalLP, balanceX, balanceY)
    totalLP += Lp2
    balanceX*=2
    balanceY*=2
    print()
    print("+++++ Lp2 provide liquidty with the same x and y as current LP1's")
    print("COMPARE: LP1 and LP2 have the same amount of LP tokens = ", Lp2 ,', ', Lp1)
    print("--------------------------")
    # print(totalLP)
    
    #2nd swap
    k = getK()
    balanceY -= yIn * 2
    balanceX = k/balanceY
    print()
    print("+++++ 2nd Swap")
    print("--------------------------")


    #Lp2 withdraw
    holdX2, holdY2 = withdraw(Lp2, k, totalLP, balanceX, balanceY)
    totalLP -=Lp2
    Lp2 = 0
    balanceX -= holdX2
    balanceY -= holdY2
    print()
    print("+++++ LP2 withdraw all liquidity")
    print("COMPARE: balanceX equal to holdX2 = ", balanceX,', ', holdX2)
    print("COMPARE: balanceY equal to holdY2 = ",balanceY,', ', holdY2)
    print("--------------------------")

    #Lp1 add liquidity to the pool (25% more than he currently has)
    k = getK()
    newLp1 = deposit(balanceX/4, balanceY/4, k, totalLP,balanceX, balanceY)
    totalLP+=newLp1
    Lp1 += newLp1
    balanceX += balanceX/4
    balanceY += balanceY/4
    print()
    print("+++++ Lp1 deposit more 1/4 of his current liquidity")
    print("LP1/pool has LP tokens: ", Lp1)
    print("--------------------------")

    #Lp3 deposit liquidity, 50% of LP1's value
    k= getK()
    Lp3 = deposit(balanceX/2,balanceY/2, k, totalLP,balanceX,balanceY)
    totalLP += Lp3
    balanceX+= balanceX/2
    balanceY+= balanceY/2
    print()
    print("+++++ Lp3 provide liquidty with 1/2 x and 1/2 y of current LP1's")
    print("LP3 has LP tokens: ", Lp3)
    print("COMPARE: LP1 has 2x LP token compared to LP3's = ", Lp1 ,', ',Lp3)
    print("--------------------------")

    #3rd swap
    k = getK()
    balanceY -= balanceY/3
    balanceX = k/balanceY
    print()
    print("+++++ 3rd Swap")
    print("--------------------------")

    #LP3 withdraw all liquidity
    holdX3, holdY3 = withdraw(Lp3, k, totalLP, balanceX, balanceY)
    totalLP -=Lp3
    Lp3 = 0
    balanceX -= holdX3
    balanceY -= holdY3
    print()
    print("+++++ LP3 withdraw all liquidity")
    print("balanceX equal to 2x of holdX2 = ", balanceX,', ', holdX3)
    print("COMPARE: balanceY equal to 2x of holdY2 = ",balanceY,', ', holdY3)
    print("--------------------------")
    
testLpCPAMM()
