import chess
import random
import os
import numpy

class FFighter(FighterBase) :
    def __init__(self) :
        pass

    def TotalMateriel(self, board, color) :
        value_n = {"p":1, "r":5, "n":3, "b":3, "q":10}
        value_b = {"P":1, "R":5, "N":3, "B":3, "Q":10}
        diff = 0
        total_n = 0
        total_b = 0
        chess_str = board.__str__().replace("\n", " ").split()
        for i in chess_str :
            if i in value_n :
                total_n += value_n[i]
            if i in value_b :
                total_b += value_b[i]
        if color is chess.WHITE :
            diff = total_b - total_n
        if color is chess.BLACK :
            diff = total_n - total_b
        return diff

    def EvaluationPositionnelle(self, board, color) :
        pieces_white = []
        pieces_black = []    
        pieces_white = list(board.pieces(chess.PAWN, chess.WHITE))
        pieces_white.extend(board.pieces(chess.KNIGHT, chess.WHITE))
        pieces_white.extend(board.pieces(chess.BISHOP, chess.WHITE))
        pieces_white.extend(board.pieces(chess.ROOK, chess.WHITE))
        pieces_white.extend(board.pieces(chess.QUEEN, chess.WHITE))
        pieces_white.extend(board.pieces(chess.KING, chess.WHITE))
        pieces_black = list(board.pieces(chess.PAWN, chess.BLACK))
        pieces_black.extend(board.pieces(chess.KNIGHT, chess.BLACK))
        pieces_black.extend(board.pieces(chess.BISHOP, chess.BLACK))
        pieces_black.extend(board.pieces(chess.ROOK, chess.BLACK))
        pieces_black.extend(board.pieces(chess.QUEEN, chess.BLACK))
        pieces_black.extend(board.pieces(chess.KING, chess.BLACK))
        cmpt_white = 0
        for piece in pieces_white :
            cmpt_white += len(board.attacks(piece))
        cmpt_black = 0
        for piece in pieces_black :
            cmpt_black += len(board.attacks(piece))
        if color is chess.WHITE :
            diff = cmpt_white - cmpt_black
        if color is chess.BLACK :
            diff = cmpt_black - cmpt_white
        return diff


    def Explorer(self, board, color) :
        diff_materiel = TotalMateriel(board, color)
        diff_positionnelle = EvaluationPositionnelle(board, color)
        actual_diff = (diff_materiel + diff_positionnelle) / 2
        moves = list(board.legal_moves)
        next_move = random.choice(moves)
        potential_moves = []
        for move in moves :
            board.push(move)
            diff_materiel = TotalMateriel(board, color)
            diff_positionnelle = EvaluationPositionnelle(board, color)
            diff = (diff_materiel + diff_positionnelle) / 2
            if diff > actual_diff :
                potential_moves.clear()
                potential_moves.append(move)
                actual_diff = diff
            elif diff == actual_diff :
                potential_moves.append(move)
            board.pop()
        next_move = random.choice(potential_moves)
        return next_move

    def trait(self, board, color) :
        return Explorer(board, color)

