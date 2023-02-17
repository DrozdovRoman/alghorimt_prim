def FindMinimumSpanningForest(matrix):
    INF = float('inf')
    lenght = len(matrix)
    relation = [0 for i in range(len(matrix))]
    no_edge = 0
    relation[0] = True
    while (no_edge < lenght - 1):
        min = INF
        x, y = 0, 0
        for i in range(lenght):
            if relation[i]:
                for j in range(lenght):
                    if ((not relation[j]) and matrix[i][j]):
                        if min > matrix[i][j]:
                            min = matrix[i][j]
                            x, y = i, j
        print(f"{x + 1} - {y + 1} : {matrix[x][y]}")
        relation[y] = True
        no_edge += 1
