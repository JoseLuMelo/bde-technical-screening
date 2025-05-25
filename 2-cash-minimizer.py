def cash_minimizer(coins, amount):
    from collections import deque

    queue = deque()
    queue.append((0, 0, []))  # (current_sum, num_coins, coin_combination)
    visited = set()
    visited.add(0)

    while queue:
        current_sum, num_coins, coin_combination = queue.popleft()

        if current_sum == amount:
            return num_coins, coin_combination

        for coin in coins:
            next_sum = current_sum + coin
            if next_sum not in visited:
                visited.add(next_sum)
                new_combination = coin_combination + [coin]
                queue.append((next_sum, num_coins + 1, new_combination))

    return -1, []


coins = input()
coins = list(map(float, coins.strip().split()))
coins = [int(coin * 100) for coin in coins]
neg_coins = [-1 * coin for coin in coins]
coins = neg_coins + coins

money = float(input())
money = int(money * 100)

n_coins, combination = cash_minimizer(coins, money)

print("Number of coins required: ", n_coins)
print("combination: ", combination)