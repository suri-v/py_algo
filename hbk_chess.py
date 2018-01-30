import copy


class Board(object):

    def __init__(self, str_board):
        self.layout, self.invalid = Board.parse(str_board)
        self.row_size = len(self.layout)
        self.column_size = len(self.layout[0])

    @staticmethod
    def parse(str_board):
        print str_board
        return ((1, 2, 3), (4, 5, 6), (7, 8, 9), ('*', 0, '#')), {'*', '#'}

    def move(self, position):
        pass

    def get_index(self, value):
        pass

    def value(self, x, y):
        return self.layout[x][y]

    # def filter(self, x, y):
    #     for move in moves:
    #         if moves.


class KnightBoard(Board):

    def move(self, position):
        c = self.column_size
        r = self.row_size
        invalid = self.invalid
        l = self.layout
        x, y = position
        possible = (
            (x + 2, y + 1),
            (x + 2, y - 1),
            (x - 2, y + 1),
            (x - 2, y - 1),
            (x + 1, y + 2),
            (x - 1, y + 2),
            (x + 1, y - 2),
            (x - 1, y - 2),
        )
        allowed = []
        for p in possible:
            if -1 < p[0] < c and -1 < p[1] < r and l[p[1]][p[0]] not in invalid:
                allowed.append(p)
        return allowed


# def generate_paths(board, start_x, start_y, length):
#
#     def move(x, y, remaining, path):
#         if remaining > 1:
#             new_positions = board.move(x, y)
#             for new_position in new_positions:
#                 new_path = copy.deepcopy(path)
#                 new_path.append(new_position)
#                 move(x, y, remaining - 1, new_path)
#         else:
#             print path
#
#     move(start_x, start_y, length, [(start_x, start_y)])


def count_paths(board, start, length):

    def move(position, remaining, path):
        count = 0
        if remaining > 1:
            if position not in path_store:
                path_store[position] = board.move(position)
            new_positions = path_store[position]
            for new_position in new_positions:
                new_path = copy.deepcopy(path)
                new_path.append(new_position)
                count += move(new_position, remaining - 1, new_path)
            return count
        else:
            # print path
            return 1

    path_store = {}
    return move(start, length, [start])

    # combinations = [[board.get_number(start_x, start_y)]]
    # for i in xrange(length):
    #     new_combinations = []
    #     possible_number = b.move(x, y)
    #     while combinations:
    #         partial_number = combinations.pop()
    #         for new_digit in possible_number:
    #             new_combinations.append(partial_number.append(new_digit))
    #     combinations = new_combinations



b = KnightBoard('')
# print b.move(1, 1)
# generate_paths(b, 0, 0, 4)
print raw_input()
print b.layout[0][1]
print count_paths(b, (0, 1), 4)

