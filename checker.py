class CheckSudoku():
    """Класс для проверки корректности Судоку"""
    __slots__ = ['grid']

    def __init__(self, grid: list()):
        self.grid = grid

    def is_valid_rows(self, row: list()) -> bool:
        """Проверяет ряд на корректность"""
        required_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        sum_row = sum(row)
        for num in row:
            condition = not isinstance(num, int) or \
                        isinstance(num, bool) or num < 1
            if condition:
                return False
        for number in required_numbers:
            """not (0 <= sum_row <= 45) сравнение с нуле,
               потомучто неизвестно будут ли пустые поля в
               массиве или все будут заполнены
            """
            condition = not (0 <= sum_row <= 45) or\
                        row.count(number) > 1
            if condition:
                return False
        return True

    def check_rows(self, grid) -> bool:
        """Выводит ряд для проверки в is_valid_rows"""
        for row in self.grid:
            if self.is_valid_rows(row) == False:
                return False
        return True

    def check_cols(self, grid):
        """Выводит колонку для проверки в is_valid_rows"""
        columns = []
        for index in range(9):
            new_column = []
            for row in self.grid:
                new_column.append(row[index])
            columns.append(new_column)
        return self.check_rows(columns)

    def check_boxes(self, grid):
        """Выводит квадрат 3х3 для проверки в is_valid_rows"""
        allBox = []
        for i in range(0, 3):
            for j in range(0, 3):
                box = []
                for ii in range(0, 3):
                    for jj in range(0, 3):
                        row = (3 * i) + ii
                        col = (3 * j) + jj
                        val = self.grid[row][col]
                        val2 = val
                        box.append(val2)
                allBox.append(box)
        return self.check_rows(allBox)

    @property
    def check_sudoku(self):
        condition = self.check_rows(self.grid) and \
                    self.check_cols(self.grid) and \
                    self.check_boxes(self.grid)
        if condition:
            return "Корректно"
        return "Некорректно"


valid_grid = [
    [5, 1, 7, 6, 9, 8, 2, 3, 4],
    [2, 8, 9, 1, 3, 4, 7, 5, 6],
    [3, 4, 6, 2, 7, 5, 8, 9, 1],
    [6, 7, 2, 8, 4, 9, 3, 1, 5],
    [1, 3, 8, 5, 2, 6, 9, 4, 7],
    [9, 5, 4, 7, 1, 3, 6, 8, 2],
    [4, 9, 5, 3, 6, 2, 1, 7, 8],
    [7, 2, 3, 4, 8, 1, 5, 6, 9],
    [8, 6, 1, 9, 5, 7, 4, 2, 3]
]


sudoku = CheckSudoku(valid_grid)
print(sudoku.check_sudoku)