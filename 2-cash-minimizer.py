from collections import deque, defaultdict

def cash_minimizer(coins, amount):

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


coins = input("Input the coins denominations in $, separated by spaces:\n")
coins = list(map(float, coins.strip().split()))
coins = [int(coin * 100) for coin in coins]
neg_coins = [-1 * coin for coin in coins]
coins = neg_coins + coins

money = float(input("Input the payment value in $:\n"))
money = int(money * 100)

n_coins, combination = cash_minimizer(coins, money)

payment = [c/100 for c in combination if c > 0]
change = [-c/100 for c in combination if c < 0]

payment_counts = defaultdict(int)
for coin in payment:
    payment_counts[coin] += 1

change_counts = defaultdict(int)
for coin in change:
    change_counts[coin] += 1

# Format payment breakdown (e.g., "10×2 + 5")
payment_str = " + ".join([f"{k}×{v}" if v > 1 else f"{k}" 
                            for k, v in sorted(payment_counts.items(), reverse=True)])

# Format change breakdown (e.g., "1×3 + 0.25")
change_str = " + ".join([f"{k}×{v}" if v > 1 else f"{k}" 
                        for k, v in sorted(change_counts.items(), reverse=True)])

print("Number of coins required:", n_coins)
print(f"Payment: ${sum(payment)} = {payment_str}")
print(f"Change: ${sum(change)} = {change_str}")