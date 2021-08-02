# Name: Jennifer Um
# Date: 2021-
# Description

class QuoridorGame:
    """
    TODO: description
    """
    def __init__(self):
        self._pawn_board = self._generate_board("pawn")
        self._fence_board = self._generate_board("fence")

    def _generate_board(self, board_type):
        board = []
        if board_type == "pawn":
            board_size = 10
            board = [["[ ]" for i in range(board_size)] for j in range(board_size)]
            for i in range(board_size):  # invalid row
                board[i][board_size - 1] = " x "
        else:  # for fences
            board_size = 10
            for i in range(board_size):
                new_row = []
                for j in range(board_size):
                    new_row.append({"direction": "na", "coordinate": (j, i)})
                board.append(new_row)

            for j in range(board_size):
                # first row is a fence
                board[0][j]["direction"] = "h"
                # last row is a fence
                board[board_size-1][j]["direction"] = "h"

            for i in range(board_size):
                # first row is a fence
                board[i][0]["direction"] = "v"
                board[i][board_size-1]["direction"] = "v"

            # we don't really care what the corners of this board are initalized with

        return board

    def move_pawn(self, player, desired_coord):
        """
        TODO:
        :param player:
        :param desired_coord:
        :return:
            False if
            - desired coordinate is forbidden by the rules
            - or desired coordinate is blocked by the fence
            - or game has already been won
            True if desired move makes the player win
        """
        pass

    def place_fence(self, player, direction, desired_coord):
        """
        TODO
        :param player:
        :param direction:
        :param desired_coord:
        :return:
            False if
            - player has no fence left
            - fence is out of the boundaries of the board
            - if there is already a fence there and desired coordinate will overlap/ intersect with existing fence
            - if the game has already been won
            True if
            - fence can be placed there
        """

    def is_winner(self, player):
        """
        TODO
        :return:
            True if that player has won
            False if that player has not won
        """

    def print_board(self):
        for i in range(10):
            for j in range(10):
                # print(self._fence_board[i][j]["direction"], end=" ")
                direction = self._fence_board[i][j]["direction"]
                coord = self._fence_board[i][j]["coordinate"]

                special_coord = {(0, 0), (0, 9), (9, 0), (9, 9)}

                if coord in special_coord:
                    print(" ╋ ", end="")
                else:
                    if direction == "h":
                        print(" _ ", end="")
                    elif direction == "v":
                        print(" | ", end="")
                    else:
                        print(" . ", end="")
                print(self._pawn_board[i][j], end="")
            print()

        # for i in range(10):
        #     for j in range(10):
        #         coord = self._pawn_board[i][j]
        #         print(coord, end="")
        #     print()



q = QuoridorGame()
q.print_board()
