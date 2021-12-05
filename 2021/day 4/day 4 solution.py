##import io
##
##import numpy as np
##import numpy.ma as ma
##
##with open('input.txt') as f:
##    data = f.read()
##
##class BingoSubsystem:
##
##    def __init__(self, bingo_data):
##        self._bingo_data = bingo_data
##        self.numbers = None
##        self.boards = None
##
##    @classmethod
##    def read_file(cls):
##        with open('input.txt') as f:
##            return cls(f.read())
##
##    def _process_data(self, bingo_data):
##        raw_numbers, *raw_boards = bingo_data.split('\n\n')
##        numbers = [int(number) for number in raw_numbers.split(',')]
##        boards = []
##        for raw_board in raw_boards:
##            f = io.StringIO(raw_board)
##            board = np.loadtxt(f, dtype=int)
##            boards.append(board)
##        boards = np.stack(boards, axis=0)
##        return numbers, boards
##
##    def win(self):
##        self.numbers, self.boards = self._process_data(self._bingo_data)
##        for number in self.numbers:
##            self.boards = ma.masked_equal(self.boards, number)
##            mask = ma.getmask(self.boards)
##            wins_by_vector = np.concatenate((mask.all(1), mask.all(2)), axis=1)
##            wins_by_grid = np.any(wins_by_vector, axis=1)
##            if wins_by_grid.any():
##                won_grid_no = np.where(wins_by_grid == True)[0][0]
##                won_grid = self.boards[won_grid_no]
##                return won_grid.sum() * number
##
##b1 = BingoSubsystem(data)
##print(b1.win())

import numpy as np
n, *b = open('input.txt')
n = np.loadtxt(n.split(','), int)
b = np.loadtxt(b, int).reshape(-1,5,5)

n = np.tile(n, len(n)).reshape(len(n), len(n))             # elements of the cartesian product
n[np.triu_indices_from(n,1)] = -1                          # use -1 as "None"

a = (b == n[:,:,None,None,None]).any(1)                    # broadcast all bingo numbers
m = (a.all(-1) | a.all(-2)).any(-1)                        # check win condition
m = np.where(np.add.accumulate(m, 0) == 1, True, False)    # take first win for each board
i,j = np.argwhere(m).T                                     # get indices
ans = b[j].sum(where=~a[m], axis=(-1,-2)) * n[-1][i]       # score of each board in order of winning 
print(ans[[0,-1]])                                         # print first and last score
