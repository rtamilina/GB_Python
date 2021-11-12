class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        my_matrix = [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                my_matrix[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in my_matrix]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in my_matrix]))


my_matrix = Matrix([[31, 32, 22],
                    [5, 16, 54],
                    [1, 8, 9]],
                   [[45, 10, 25],
                    [1, 2, 3],
                    [5, 5, 10]])

print(my_matrix.__add__())
