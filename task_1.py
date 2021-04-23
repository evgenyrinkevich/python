class Matrix:
    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        # __str__ должен возвращать объект str поэтому создаем строку
        output_str = ''
        for i in range(len(self.matr)):
            for j in range(len(self.matr[i])):
                output_str += f'{self.matr[i][j]:02} '
            #     тут допустил 2значные числа чтобы красиво выводилось
            output_str += '\n'
        return output_str

    def __add__(self, other):
        if len(self.matr) == len(other.matr) and len(self.matr[0]) == len(other.matr[0]):
            sum_matrix = [
                [cell_1 + cell_2 for cell_1, cell_2 in zip(row_1, row_2)]
                for row_1, row_2 in zip(self.matr, other.matr)]
            return Matrix(sum_matrix)
        # решил возвратить объект класса Matrix, так как складываем 2 таких объекта
        else:
            return 'матрицы разного размера'


if __name__ == '__main__':
    m1 = [[1, 3, 5, 7],
          [4, 6, 8, 10],
          [12, 15, 18, 21]
          ]

    m2 = [[4, 1, 1, 2],
          [1, 2, 3, 4],
          [1, 5, 1, 2]
          ]

    mat = Matrix(m1)
    mat2 = Matrix(m2)
    print(mat)
    print(mat + mat2)
