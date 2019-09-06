from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    # TODO - you fill in here.
    # First attempt, takes way too much time....
    '''maxSell = 0.0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > maxSell:
                maxSell = profit
    return maxSell'''
    # End first attempt.

    # Second attempt.
    min = float("inf")
    maxSell = 0.0
    for i in range(len(prices)):
        if prices[i] < min:
            min = prices[i]
        if (prices[i] - min) > maxSell:
            maxSell = prices[i] - min
    return maxSell


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
