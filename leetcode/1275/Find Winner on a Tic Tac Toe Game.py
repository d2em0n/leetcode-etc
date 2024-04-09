class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        movesA = []
        movesB = []
        for i in range(0, len(moves), 2):
            movesA.append(moves[i])
        for i in range(1, len(moves), 2):
            movesB.append(moves[i])

        def isWinner(moves):
            movesSet = tuple(i for i in moves)
            a1 = [0, 0] in movesSet and [0, 1] in movesSet and [0, 2] in movesSet
            a2 = [1, 0] in movesSet and [1, 1] in movesSet and [1, 2] in movesSet
            a3 = [2, 0] in movesSet and [2, 1] in movesSet and [2, 2] in movesSet
            a4 = [0, 0] in movesSet and [1, 0] in movesSet and [2, 0] in movesSet
            a5 = [0, 1] in movesSet and [1, 1] in movesSet and [2, 1] in movesSet
            a6 = [0, 2] in movesSet and [1, 2] in movesSet and [2, 2] in movesSet
            a7 = [0, 0] in movesSet and [1, 1] in movesSet and [2, 2] in movesSet
            a8 = [2, 0] in movesSet and [1, 1] in movesSet and [0, 2] in movesSet
            return a1 or a2 or a3 or a4 or a5 or a6 or a7 or a8

        if isWinner(movesA): return "A"
        elif isWinner(movesB): return "B"
        elif len(moves) < 9: return "Pending"
        else: return "Draw"