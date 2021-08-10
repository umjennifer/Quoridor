import unittest

from Quoridor import QuoridorGame
from Quoridor import Fence
from Quoridor import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.q = QuoridorGame()
        self.coordinates = [(0, 0), (4, 0), (8, 0), (8, 4), (8, 8), (4, 8), (0, 8), (0, 4), (4, 4)]

    def test_fence_coordinate_within_boundary(self):
        self.assertFalse(self.q._fence_coordinate_within_boundary((10, 9)))

    def test_get_valid_north_pawn_moves(self):
        print("test_get_valid_north_pawn_moves")
        for coord in self.coordinates:
            print("coord", coord, ":", self.q._get_valid_north_pawn_moves(coord))

    def test_get_valid_south_pawn_moves(self):
        print("test_get_valid_south_pawn_moves")
        for coord in self.coordinates:
            print("coord", coord, ":", self.q._get_valid_south_pawn_moves(coord))

    def test_get_valid_east_pawn_moves(self):
        print("test_get_valid_east_pawn_moves")
        for coord in self.coordinates:
            print("coord", coord, ":", self.q._get_valid_east_pawn_moves(coord))

    def test_get_valid_west_pawn_moves(self):
        print("test_get_valid_west_pawn_moves")
        for coord in self.coordinates:
            print("coord", coord, ":", self.q._get_valid_west_pawn_moves(coord))

    # def test_game(self):
    #
    # print(q.move_pawn(2, (4,7))) #moves the Player2 pawn -- invalid move because only Player1 can start, returns False
    # print(q.move_pawn(1, (4,1))) #moves the Player1 pawn -- valid move, returns True
    # # q.print_board()
    # print(q.place_fence(1, 'h',(6,5))) #places Player1's fence -- out of turn move, returns False
    # # q.print_board()
    # print(q.move_pawn(2, (4,7))) #moves the Player2 pawn -- valid move, returns True
    # # q.print_board()
    # print(q.place_fence(1, 'h',(6,5))) #places Player1's fence -- returns True
    # # q.print_board()
    # print(q.place_fence(2, 'v',(3,3))) #places Player2's fence -- returns True
    # # q.print_board()
    # print(q.is_winner(1)) #returns False because Player 1 has not won
    # # q.print_board()
    # print(q.is_winner(2)) #returns False because Player 2 has not won

        # DEBUGGING - north moves
        # board[(6, 5)]["fence"].append(Fence("h"))
        # board[(4, 7)]["fence"].append(Fence("h"))
        # board[(4, 7)]["fence"].append(Fence("v"))
        # board[(5, 7)]["fence"].append(Fence("v"))
        # board[(4, 7)]["pawn"] = 3

        # # DEBUGGING - south moves
        # board[(4, 1)]["fence"].append(Fence("h"))
        # board[(4, 1)]["fence"].append(Fence("v"))
        # board[(4, 2)]["fence"].append(Fence("h"))
        # board[(5, 1)]["fence"].append(Fence("v"))
        # board[(3, 1)]["fence"].append(Fence("v"))
        # board[(4, 1)]["pawn"] = 4

        # Debugging - west moves
        # board[(7,4)]["pawn"] = 5
        # board[(7, 4)]["fence"].append(Fence("v"))
        # board[(7, 4)]["fence"].append(Fence("h"))
        # board[(7, 5)]["fence"].append(Fence("h"))
        # board[(8, 4)]["fence"].append(Fence("v"))

        # Debugging - east moves
        # board[(1, 4)]["pawn"] = 6
        # # board[(1, 4)]["fence"].append(Fence("v"))
        # board[(2, 4)]["fence"].append(Fence("v"))
        # board[(1, 4)]["fence"].append(Fence("h"))
        # board[(1, 5)]["fence"].append(Fence("h"))


if __name__ == '__main__':
    unittest.main()

