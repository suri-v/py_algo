import copy


class Board(object):

    def __init__(self, moving_piece, row_size, column_size, starting_digits_str, str_board):
        self.row_size = row_size
        self.column_size = column_size
        self.starting_digits = set(starting_digits_str.split())
        self.layout, self.invalid, self.start_index = Board.parse(self.starting_digits, str_board)
        self.move = self.knight_move if 'knight' == moving_piece.lower() else self.bishop_move

    @staticmethod
    def parse(starting_digits, str_board):
        layout = []
        start_index = {}
        invalid_chars = set()
        for r, str_row in enumerate(str_board):
            row = []
            for c, entry in enumerate(str_row.split()):
                row.append(entry)
                if entry in starting_digits:
                    start_index[entry] = r , c
                try:
                    int(entry)
                except ValueError:
                    invalid_chars.add(entry)
            layout.append(row)
        return layout, invalid_chars, start_index

    def value(self, x, y):
        return self.layout[x][y]

    def bishop_move(self, position):
        c = self.column_size
        r = self.row_size
        invalid = self.invalid
        l = self.layout
        x, y = position

        possible = []
        higher = min(r - x, c - y)
        lower = min(x, y)
        for i in xrange(higher):
            possible.append((x + i, y + i))

        for i in xrange(lower):
            possible.append((x - i, y - i))

        allowed = []
        for p in possible:
            if -1 < p[0] < c and -1 < p[1] < r and l[p[1]][p[0]] not in invalid:
                allowed.append(p)
        return allowed

    def knight_move(self, position):
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


def count_paths(start_value):

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
            print path
            return 1

    path_store = {}
    try:
        start = board.start_index[start_value]
        return move(start, phone_number_length, [start])
        # print 'Return val: ', x
        # return x
    except KeyError:
        print 'Invalid starting value: ' + str(start_value)
        return 0


piece = 'Knight'  # raw_input()
phone_number_length = 2 # int(raw_input())
starting_digits_str = '2 3 4 5 6 7 8 9'  # raw_input().split()
board_rows = 4  # int(raw_input())
board_columns = 3  # int(raw_input())
# rows = []
# for i in xrange(board_rows):
#     rows.append(raw_input())
rows = [
    '1 2 3', '4 5 6', '7 8 9', '* 0 #'
]

total = 0
board = Board(piece, board_rows, board_columns, starting_digits_str, rows)
for c in board.starting_digits:
    x = count_paths(c.strip())
    total += x
print total

