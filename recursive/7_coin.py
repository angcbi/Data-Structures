# -*- coding:utf-8 -*-
def recMC(coinValueList, change):
    minCoins = change

    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change-i)
            if numCoins < minCoins:
                minCoins = numCoins

    return minCoins

def recDC(conValueList, change, knownResults):
    """
    传递一个列表，缓存函数的结果，每次先从函数中查找，
    找不到在计算
    """

    minCoins = change

    if change in conValueList:
        knownResults[change] = 1
        return 1

    elif knownResults[change] > 0:
        return knownResults[change]

    else:
        for i in [c for c in conValueList if c <= change]:
            numCoins = 1 + recDC(conValueList, change-i, knownResults)

            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins

    for index, item in enumerate(knownResults):
        if item != 0:
            print index, item
    return minCoins

def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    """
    非递归算法， 存储每一步的最优解
    """
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c<= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin

    return minCoins[change]

def printCoins(coinUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinUsed[coin]
        print thisCoin
        coin = coin - thisCoin

def main():
    amnt = 63
    clist = [1, 5, 10, 21, 25]
    coinsUsed = [0]*(amnt + 1)
    coinCount = [0]*(amnt + 1)
    print 'Making change for', amnt, 'requires'
    print dpMakeChange(clist, amnt, coinCount, coinsUsed), 'coins'
    print 'They are:'
    printCoins(coinsUsed, amnt)
    print 'The used list is as follows:'
    print coinsUsed



def dpLearn(change, coinList, knownlist):
    minCoins = change

    # 如果面值相等，直接返回1
    if change in coinList:
        knownlist[change] = 1
        return 1

    # 如果缓存中有记录，返回记录
    elif knownlist[change] > 0:
        return knownlist[change]
    else:
        for i in [c for c in coinList if c <=change]:
            numCoins = 1 + dpLearn(change-i, coinList, knownlist)
            if numCoins < minCoins:
                minCoins = numCoins
                knownlist[change] = minCoins

    # print knownlist
    return minCoins

# print dpLearn(13, [1, 2, 3, 10], [0]*14)


def artThief(p_dict, limit_weight, knownList):
    maxValue = 0

    if limit_weight == 2:
        knownList[limit_weight] = 3
        return 3

    if knownList[limit_weight] > 0:
        return knownList[limit_weight]

    else:
        avaible_list = [w for w in p_dict.keys() if int(w) <= limit_weight]
        for value in avaible_list:
            currentValue = p_dict[value] + artThief(p_dict, limit_weight-int(value), knownList)
            if currentValue > maxValue:
                maxValue = currentValue
                knownList[limit_weight] = maxValue

    return maxValue

p_dict = {
    '2': 3,
    '3': 4,
    '4': 8,
    '5': 8,
    '9': 10
}
for weight in range(2, 10):
    print weight, artThief(p_dict, weight, [0]*(weight + 1))

