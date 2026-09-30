# Adapted from CLRS 2nd edition

def fastest_way(a: list[list[int]], 
                t: list[list[int]], 
                e: list[int], 
                x: list[int], 
                n: int) -> None:
    global f_star, l_star, f, l
    f[0][0] = e[0] + a[0][0]
    f[1][0] = e[1] + a[1][0]
    for j in range(1, n):
        if f[0][j - 1] + a[0][j] <= f[1][j - 1] + t[1][j - 1] + a[0][j]:
            f[0][j] = f[0][j - 1] + a[0][j]
            l[0][j] = 0
        else:
            f[0][j] = f[1][j - 1] + t[1][j - 1] + a[0][j]
            l[0][j] = 1
        if f[1][j - 1] + a[1][j] <= f[0][j - 1] + t[0][j - 1] + a[1][j]:
            f[1][j] = f[1][j - 1] + a[1][j]
            l[1][j] = 1
        else:
            f[1][j] = f[0][j - 1] + t[0][j - 1] + a[1][j]
            l[1][j] = 0
    if f[0][n - 1] + x[0] <= f[1][n - 1] + x[1]:
        f_star = f[0][n - 1] + x[0];
        l_star = 0;
    else:
        f_star = f[1][n - 1] + x[1];
        l_star = 1;


def print_stations(n: int) -> None:
    i = l_star;
    print(f'line {i}, station {n - 1}')
    for j in range(n - 1, 0, -1):
        i = l[i][j]
        print(f'line {i}, station {j - 1}')


if __name__ == '__main__':
    a = [[7, 9, 3, 4, 8, 4],
         [8, 5, 6, 4, 5, 7]]
    t = [[2, 3, 1, 3, 4],
         [2, 1, 2, 2, 1]]
    e = [2, 4]
    x = [3, 2]
    n = 6
    f_star = 0
    l_star = 0
    f = [[0 for _ in range(n)] for _ in range(2)]
    l = [[0 for _ in range(n)] for _ in range(2)]
    fastest_way(a, t, e, x, n)
    print_stations(n)



