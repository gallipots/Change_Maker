from pandas import *

def _get_change_making_matrix(set_of_coins, r: int):
    m = [[0 for _ in range(r + 1)] for _ in range(len(set_of_coins) + 1)]
    for i in range(1, r + 1):
        m[0][i] = float('inf')  # By default there is no way of making change
    return m

def change_making(coins, n: int):
    """This function assumes that all coins are available infinitely.
    n is the number to obtain with the fewest coins.
    coins is a list or tuple with the available denominations.
    """
    m = _get_change_making_matrix(coins, n)
    p = _get_change_making_matrix(coins, n)

    for c, coin in enumerate(coins, 1):
        for r in range(1, n + 1):
            # Just use the coin
            if coin == r:
                m[c][r] = 1
                p[c][r] = 1
                # zero out the entries for smaller denominations
                for i in range(1,c):
                    p[i][r] = 0
            # coin cannot be included.
            # Use the previous solution for making r,
            # excluding coin
            elif coin > r:
                m[c][r] = m[c - 1][r]
            # coin can be used.
            # Decide which one of the following solutions is the best:
            # 1. Using the previous solution for making r (without using coin).
            # 2. Using the previous solution for making r - coin (without
            #      using coin) plus this 1 extra coin.
            else:
            #    m[c][r] = min(m[c - 1][r], 1 + m[c][r - coin])
                prev = m[c-1][r]
                new = 1 + m[c][r-coin]
                if (prev < new):
                    m[c][r] = prev
                else:
                    m[c][r] = new
                    p[c][r] = 1 + p[c][r-coin]
                    for i in range(1,c):
                        p[i][r] = p[i][r-coin]

    return m,p

def main():
    coins = [1,4,9,11,26,38,44]
    n = 99
    m,p = change_making(coins, n)
    print(DataFrame(m))
    print(DataFrame(p))

if __name__ == "__main__":
    main()

