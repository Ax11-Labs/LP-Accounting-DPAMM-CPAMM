import math

def deposit(amountX, amountY, totalLiquidity, totalLP, balanceX, balanceY):
    liquidity = amountX * amountY
    if(totalLiquidity <= 1):
        mintedLP = math.sqrt(amountX*amountY)
    else:
        mintedLP = min(amountX * totalLP / balanceX, amountY * totalLP / balanceY)
    return ( mintedLP)


def withdraw(lpAmount, totalLiquidity,totalLP, balanceX, balanceY):
    liquidity = ((lpAmount) * totalLiquidity)/ totalLP
    amountX  = (liquidity/totalLiquidity) * balanceX
    amountY = (liquidity/totalLiquidity) * balanceY
    return (amountX, amountY)

    
