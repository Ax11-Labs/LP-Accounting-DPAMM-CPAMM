import math

def deposit(amountX, amountY, priceX, totalLpX, totalLpY ,balanceX, balanceY):
    mintedLpX = 0
    mintedLpY = 0
    
    # Check if this is the first liquidity provision (pool initialization)
    if totalLpX == 0 or totalLpY == 0:
        # Mint LP tokens based on the initial geometric mean
        mintedLpX = amountX * math.sqrt(priceX)
        mintedLpY = amountY * math.sqrt(1 / priceX)
    else:
        # Proportional minting based on existing liquidity
        if amountX > 0:
            mintedLpX = (amountX / balanceX) * totalLpX
        if amountY > 0:
            mintedLpY = (amountY / balanceY) * totalLpY

    # Return the minted LP tokens for both X and Y
    return mintedLpX, mintedLpY

def withdraw(LpXAmount, LpYAmount, totalLpX, totalLpY, balanceX, balanceY):
    amountX = 0
    amountY = 0

    if LpXAmount > 0:
        # Proportional withdrawal for X
        amountX = (LpXAmount / totalLpX) * balanceX
    if LpYAmount > 0:
        # Proportional withdrawal for Y
        amountY = (LpYAmount / totalLpY) * balanceY

    return amountX, amountY

