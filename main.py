class SimpleBacktrackingQueensSolver:
    def __init__(self, grid_size: int, color_areas: list[list[int]]):
        """
        Args:
            grid_size (int): グリッドのサイズ
            color_areas (list[list[int]]): 各セルのカラーエリアを示すNxNグリッド
        """
        self.grid_size = grid_size
        self.color_areas = color_areas
        self.queens = []

    def can_place_queen(self, row: int, col: int) -> bool:
        """
        Args:
            row (int): 行
            col (int): 列
        Returns:
            bool: クイーンを配置できるかどうか
        """
        for r, c in self.queens:
            if r == row or c == col or self.color_areas[r][c] == self.color_areas[row][col]:
                return False
            if abs(r - row) <= 1 and abs(c - col) <= 1:
                return False
        return True

    def solve(self, row=0):
        """
        Args:
            row (int): 行
        Returns:
            bool: クイーンを配置できるかどうか
        """
        if row == self.grid_size:
            return True

        for col in range(self.grid_size):
            if self.can_place_queen(row, col):
                self.queens.append((row, col))
                if self.solve(row + 1):
                    return True
                self.queens.pop()

        return False

    def display_solution(self):
        """
        クイーンを配置したグリッドを表示
        """
        grid = [['.' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        for r, c in self.queens:
            grid[r][c] = 'Q'
        for row in grid:
            print(" ".join(row))


def run_test(grid_size, color_areas):
    """
    与えられた grid_size と color_areas に対してテストを実行し、結果を表示
    """
    solver = SimpleBacktrackingQueensSolver(grid_size, color_areas)
    if solver.solve():
        print("解が見つかりました:")
        solver.display_solution()
    else:
        print("解は存在しません。")


def main():
    # テストケース 1
    grid_size_1 = 7
    color_areas_1 = [
        [0, 0, 1, 1, 1, 4, 4],
        [0, 1, 1, 3, 1, 1, 4],
        [0, 1, 3, 3, 3, 1, 5],
        [0, 1, 1, 3, 1, 1, 5],
        [0, 6, 1, 1, 1, 6, 6],
        [6, 6, 6, 7, 6, 6, 6],
        [6, 6, 6, 6, 6, 6, 6]
    ]
    print("テストケース 1:")
    run_test(grid_size_1, color_areas_1)
    
    # テストケース 2
    grid_size_2 = 5
    color_areas_2 = [
        [0, 1, 2, 3, 4],
        [1, 0, 1, 2, 3],
        [2, 1, 0, 1, 2],
        [3, 2, 1, 0, 1],
        [4, 3, 2, 1, 0]
    ]
    print("\nテストケース 2:")
    run_test(grid_size_2, color_areas_2)
    

if __name__ == "__main__":
    main()
