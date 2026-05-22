from collections import deque

def wave(matrix, n, m, start, wall):
    di = [-1, 0, 1, 0]
    dj = [0, -1, 0, 1]

    dist = [[-1] * m for _ in range(n)]

    queue = deque()
    queue.append((start[0], start[1]))

    dist[start[0]][start[1]] = 0

    while queue:
        i, j = queue.popleft()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < n and 0 <= nj < m:
                if dist[ni][nj] == -1 and matrix[ni][nj] != wall:
                    dist[ni][nj] = dist[i][j] + 1
                    queue.append((ni, nj))

    return dist


if __name__ == '__main__':
    file = open("input.txt")

    n, m = map(int, file.readline().split())

    matrix = [
        list(map(int, file.readline().split()))
        for _ in range(n)
    ]


    x1, y1 = map(int, file.readline().split())
    x2, y2 = map(int, file.readline().split())

    illya = [y1-1, x1-1]

    wave_ = wave(matrix, n, m, illya, 1)
    dist = wave_[y2-1][x2-1]
    print(dist)

    file.close()