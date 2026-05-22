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


if __name__ == "__main__":
    file = open("input.txt")

    n = int(file.readline())

    matrix = [
        list(file.readline().strip())
        for _ in range(n)
    ]

    file.close()

    start = end = None
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == '@':
                start = (i, j)
            elif matrix[i][j] == 'X':
                end = (i, j)

    dist = wave(matrix, n, n, start, 'O')

    if dist[end[0]][end[1]] == -1:
        print('N')
    else:
        print('Y')

        di = [-1, 0, 1, 0]
        dj = [0, -1, 0, 1]

        path = set()
        cur = end

        while cur != start:
            path.add(cur)
            i, j = cur
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < n and 0 <= nj < n:
                    if dist[ni][nj] == dist[i][j] - 1:
                        cur = (ni, nj)
                        break

        for i in range(n):
            row = ''
            for j in range(n):
                if (i, j) in path:
                    row += '+'
                else:
                    row += matrix[i][j]
            print(row)