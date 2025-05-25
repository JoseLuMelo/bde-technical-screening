def cash_minimizer(coins, money):
    dp = [money + 1] * (money + 1)
    dp[0] = 0

    combination = [[] for _ in range(money + 1)]

    for i in range(1, money + 1):
        for c in coins:
            if i - c >= 0 and dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1
                combination[i] = combination[i - c] + [c]

    if dp[money] != money + 1:
        return dp[money], combination[money]
    else:
        return -1, []

coins = input()
coins = list(map(float, coins.strip().split()))
coins = [int(coin * 100) for coin in coins]

money = float(input())
money = int(money * 100)

n_coins, combination = cash_minimizer(coins, money)

print("Number of coins required: ", n_coins)
print("Coins combination: ", combination)