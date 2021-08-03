# Name: Jennifer Um
# Date: 2021-
# Description

class QuoridorGame:
    """
    TODO: description
    """

    def __init__(self):

        # initialize the board
        self._game_status  # TODO: to determine winner
        self._player1 = Player(1)
        self._player2 = Player(2)
        self._players = [self._player1, self._player2]  # TODO: maybe not needed

        self._current_turn = self._player1
        # self._player1_pawn = Pawn(self._player1.get_player_num())

        # self._player2_pawn = Pawn(self._player2.get_player_num())
        self._board = self._generate_board()




    def get_player_from_num(self, number):
        for player in self._players:
            if player.get_player_num() == number:
                return player
        return None

    def _generate_board(self):
        board = {}
        for row in range(-1, 10):
            for col in range(-1, 10):
                board[(col, row)] = {"pawn": None, "fence": None}

        # place player1 and player2 pawn in their starting positions
        board[(4, 0)]["pawn"] = self._player1.get_player_num()
        board[(4, 8)]["pawn"] = self._player2.get_player_num()

        # edges are fences
        for i in range(-1, 10):
            board[(-1, i)]["fence"] = Fence("edge")
            board[(9, i)]["fence"] = Fence("edge")
            board[(i, -1)]["fence"] = Fence("edge")
            board[(i, 9)]["fence"] = Fence("edge")

        return board

    def _print_board(self):

        # for key, value in self._board.items():
        #     print(key, end=" ")
        #     print()

        for i in range(-1,10):
            for j in range(-1,10):

                this_coord = (j, i)

                # create pawn string
                if self._board[this_coord]["pawn"] is None:
                    pawn_string = "None"
                else:
                    pawn_string = str(self._board[this_coord]["pawn"])

                # create fence string
                if self._board[this_coord]["fence"] is None:
                    fence_string = "None"
                else:
                    fence_string = str(self._board[this_coord]["fence"].get_fence_direction())

                location_string = str(this_coord) + ",pawn=" + pawn_string + ",fence=" + fence_string
                print(location_string.ljust(35), end="")
                # print(this_coord, self._board[this_coord], end=" | ")
                # print(this_coord, end="")
            print()
        # for row in self._board:
        #     for square in row:
        #         for coord in square.keys():
        #             print(coord.get_coordinate(), end="")
        #         # for value in square.values():
        #         #     print(value, end="")
        #         # print(square.keys(), end="")
        #     print()

    def _get_current_turn(self):
        return self._current_turn

    def _change_current_turn(self):
        if self._current_turn == self._player1:
            self._current_turn = self._player2
        else:
            self._current_turn = self._player1
        # if self._current_turn == 1:
        #     self._current_turn = 2
        # else:
        #     self._current_turn = 1

    def _validate_current_turn(self, inputted_player):
        if inputted_player == self._current_turn:
            return True
        else:
            return False

    def move_pawn(self, player_num, desired_coord):
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
        # check if player entered is the correct current player
        if not self._validate_current_turn(player_num):  # TODO: put in function decorator
            return False  # return False if invalid move



        # check if player has fences left

        # check if fence is within boundaries of the board

        # check if another fence is already there and new fence will overlap or intersect with the fence

        # if game has already won

        # update current turn to the other player for the next round
        self._change_current_turn()  # TODO: put in function decorator




    def place_fence(self, player_num, direction, desired_coord):
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
        # check if player entered is the correct current player
        if not self._validate_current_turn(player_num):  # TODO: put in function decorator
            return False  # return False if invalid move

        # check if player has fences left
        # if self.plaer

        # update current turn to the other player for the next round
        self._change_current_turn()  # TODO: put in function decorator

    def is_winner(self, player_num):
        """
        TODO
        :return:
            True if that player has won
            False if that player has not won
        """


# class Board:
#     def __init__(self):
#         self._board = Boar

class Fence:
    def __init__(self, direction):
        # self._coord
        self._direction = direction  # horizontal, vertical, or edge

    def get_fence_direction(self):
        return self._direction


class Pawn:
    def __init__(self, player_num):
        self._player = player_num

    def get_pawn_number(self):
        return self._player


# class Coordinate:
#     def __init__(self, col, row):
#         self._col = col
#         self._row = row
#
#     def get_coordinate(self):
#         return (self._col, self._row)


class Player:
    def __init__(self, player_num):
        self._player_num = player_num
        self._num_fences_available = 10
        # self._pawn = Pawn(1, (4, 8))
        # # move_pawn(1, (4, 8))
        # TODO: initialize first pawn on board

    def get_player_num(self):
        return self._player_num

    def get_num_fences_available(self):
        return self._num_fences_available

    def decrement_num_fences_available(self):
        self._num_fences_available -= 1


q = QuoridorGame()
q._print_board()
# print(q.move_pawn(2, (4, 7)))  #moves the Player2 pawn -- invalid move because only Player1 can start, returns False
# print(q.move_pawn(1, (4, 1)))  #moves the Player1 pawn -- valid move, returns True
print(q.place_fence(1, 'h',(6,5)))
# q.move_pawn(2, (4,7)) #moves the Player2 pawn -- valid move, returns True
# q.place_fence(1, 'h',(6,5)) #places Player1's fence -- returns True
# q.place_fence(2, 'v',(3,3)) #places Player2's fence -- returns True
# q.is_winner(1) #returns False because Player 1 has not won
# q.is_winner(2) #returns False because Player 2 has not won

print(q.get_player_from_num(1))