# Набір монет
coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy_alogorithm(amount):
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= count * coin
    return result


def find_min_coins(amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result



test_cases = [113, 99, 58, 32, 7, 1]
results = {"Amount": [], "Greedy Result": [], "DP Result": []}
for amount in test_cases:
    greedy_result = find_coins_greedy_alogorithm(amount)
    dp_result = find_min_coins(amount)
    results["Amount"].append(amount)
    results["Greedy Result"].append(greedy_result)
    results["DP Result"].append(dp_result)

print(results)