import math

def deposit(amountX, amountY, priceX):
    mintedLpX=0
    mintedLpY=0
    if (amountX > 0):       
        # mintedLpX = (amountX*priceX)/math.sqrt(priceX)
        mintedLpX = amountX*math.sqrt(priceX)
        # print(mintedLpX)
    if (amountY > 0):       
        # mintedLpY = (amountY/priceX)/math.sqrt(1/priceX)
        mintedLpY = amountY*math.sqrt(1/priceX)
        # print(mintedLpY)
    
    return mintedLpX,mintedLpY

def withdraw(LpXAmount, LpYAmount, priceX):
    amountX=0
    amountY=0
    if (LpXAmount > 0):
        amountX = (LpXAmount*(math.sqrt(priceX)))/priceX
    if (LpYAmount > 0):
        amountY = (LpYAmount*(math.sqrt(1/priceX)))*priceX
    return amountX, amountY

# deposit(700,10000, 10000/700)
