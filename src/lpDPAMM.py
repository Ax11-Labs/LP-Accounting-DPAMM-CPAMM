import math

def deposit(amountX, amountY, priceX):
    mintedLpX=0
    mintedLpY=0
    if (amountX > 0):       
        mintedLpX = (amountX*priceX)/math.sqrt(priceX)
    if (amountX > 0):       
        mintedLpY = (amountY/priceX)/math.sqrt(1/priceX)
    
    return mintedLpX,mintedLpY

def withdraw(LpXAmount, LpYAmount, priceX):
    amountX=0
    amountY=0
    if (LpXAmount > 0):
        amountX = (LpXAmount*(math.sqrt(priceX)))/priceX
    if (LpYAmount > 0):
        amountY = (LpYAmount*(math.sqrt(1/priceX)))*priceX
    return amountX, amountY