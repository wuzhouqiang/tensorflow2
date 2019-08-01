import sys


# [2, 5, 7] 27 递归
# def exchange(N,M):
#     a = []
#     for i in range(1, M+1):
#         x = f(i, N)
#         a.append(-1 if x == sys.maxsize else x)
#
#     print(a)
#
#
# def f(x, N):
#     if x == 0:
#         return 0
#     if x < 0:
#         return sys.maxsize
#
#     min_value = sys.maxsize
#     for n in N:
#         min_value = min(f(x - n, N) + 1, min_value)
#
#     return min_value


# def exchange(coins, amount):
#     if amount == 0:  # 总数为0，消耗钱为0
#         return 0
#     if amount < min(coins):  # 总数比所有的硬币面值都小，无解
#         return -1
#     dp = [0 for i in range(amount + 1)]
#
#     for coin in coins:  # 初始化dp数组
#         if coin <= amount:
#             dp[coin] = 1
#
#     for i in range(1, amount + 1):
#         if dp[i] == 1:
#             continue
#         min_ = 100000
#
#         for j in coins:
#             if i - j > 0:
#                 min_ = min(min_, dp[i - j] + 1)
#
#         dp[i] = min_
#
#     if dp[-1] < 100000:
#         return dp[-1]
#     else:
#         return -1


def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    res = [0 for _ in range(amount + 1)]

    for i in range(1, amount + 1):
        cost = float('inf')

        for c in coins:
            if i - c >= 0:
                cost = min(cost, res[i - c] + 1)

        res[i] = cost

    if res[amount] == float('inf'):
        return -1
    else:
        return res[amount]

dp = coinChange([2, 5, 7],27)

print(dp)
