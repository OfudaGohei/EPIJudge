from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    # TODO - you fill in here.
    maxSell = 0.0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > maxSell:
                maxSell = profit
    return maxSell


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
