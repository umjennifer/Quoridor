# Name: Jennifer Um
# Date: 2021-
# Description

class QuoridorGame:
    """
    TODO: description
    """

    def __init__(self):

        # initialize the board
        self._game_status = "In-Progress"  # TODO: to determine winner
        self._player1 = Player(1)
        self._player2 = Player(2)
        self._players = [self._player1, self._player2]  # TODO: maybe not needed

        # TODO: winning coordinates for player1
        # TOD: winning coordinates for player2

        self._current_turn = self._player1
        # self._player1_pawn = Pawn(self._player1.get_player_num())
        # self._player2_pawn = Pawn(self._player2.get_player_num())
        self._board = self._generate_board()

        # self._valid_inputted_fence_coordinate =

    def get_player_from_num(self, number):
        for player in self._players:
            if player.get_player_num() == number:
                return player
        return None

    def _generate_board(self):
        board = {}
        for row in range(0, 10):
            for col in range(0, 10):
                board[(col, row)] = {
                    "pawn": None,  # check if pawn is present
                    # "fence": None
                    "fence": []  # TODO list of fence objects? or initialize metadata
                }

        # place player1 and player2 pawn in their starting positions
        for player in self._players:
            board[player.get_pawn_coordinate()]["pawn"] = player.get_player_num()

        # edges are fences
        for i in range(0, 10):
            board[(0, i)]["fence"].append(Fence("v"))
            board[(9, i)]["fence"].append(Fence("v"))
        for i in range(0, 10):  # TODO: to prevent adding multiple fences to the edge
            board[(i, 0)]["fence"].append(Fence("h"))
            board[(i, 9)]["fence"].append(Fence("h"))

        # # TODO: erase me. Create test fence
        board[(6, 5)]["fence"].append(Fence("h"))

        return board

    def _print_board(self):

        # for key, value in self._board.items():
        #     print(key, end=" ")
        #     print()

        for i in range(0, 10):
            for j in range(0, 10):

                this_coord = (j, i)

                # create pawn string
                if self._board[this_coord]["pawn"] is None:
                    pawn_string = "None"
                else:
                    pawn_string = str(self._board[this_coord]["pawn"])

                # create fence string
                if len(self._board[this_coord]["fence"]) == 0:
                    fence_string = str(len(self._board[this_coord]["fence"]))
                else:
                    fence_string = ""
                    for fence in self._board[this_coord]["fence"]:
                        fence_string += str(fence.get_fence_direction())
                    # if len(self._board[this_coord]["fence"]) > 0:
                    #     fence_string = str(self._board[this_coord]["fence"][0].get_fence_direction())

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

    def _valid_current_turn(self, inputted_player):
        if inputted_player == self._current_turn:
            return True
        else:
            return False

    # def _check_if_fences_at_coordinate(self, coordinate):
    #     if len(self._board[coordinate]["fence"]) > 0:
    #         return True
    #     return False

    def _get_list_fences_at_coordinate(self, coordinate):
        return self._board[coordinate]["fence"]

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

        # get player from player_num
        this_player = self.get_player_from_num(player_num)
        print("moving_pawn_attempt\ncurrent_turn=", self._current_turn.get_player_num(), "this player=",
              this_player.get_player_num())  # debug

        # check if player entered is the correct current player
        if not self._valid_current_turn(this_player):  # TODO: put in function decorator
            print("False: not valid current player")  # debug
            return False  # return False if invalid move

        # check if coordinate is forbidden by the rules (diagonal, move in orthogonal directions)
        # check if desired coordinate  is within boundaries of the board
        if not self._pawn_coordinate_within_boundary(desired_coord):  # TODO: maybe rename this function or combine with fence coordiante
            print("False: not valid inputted coordinate")  # debug
            return False
        # check if move is blocked by fence
        valid_pawn_moves = self._get_valid_pawn_moves(this_player)

        # if desired coord in valid_pawn_moves,
        # get player object's current coordinate on board
        # on board, change that coordinate's pawn to none
        # update player object's current coordinate to desired coordinate
        # update board to that player's new pawn coordiante


        # check if game has already been won; if so, change game status

        # update current turn to the other player for the next round
        print("updating turn")
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
        # TODO: if game has already won

        # get player from player_num
        this_player = self.get_player_from_num(player_num)
        print("placing_fence_attempt\ncurrent_turn=", self._current_turn.get_player_num(), "this player=", this_player.get_player_num())  # debug

        # check if player entered is the correct current player
        if not self._valid_current_turn(this_player):  # TODO: put in function decorator
            print("False: not valid current player")  # debug
            return False  # return False if invalid move

        # check if player has fences left
        if not this_player.has_fences_remaining():
            print("False: does not have fences remaining")  # debug
            return False

        # check if desired coordinate is within boundaries of the board
        if not self._fence_coordinate_within_boundary(desired_coord):
            print("False: not valid inputted coordinate")  # debug
            return False

        # check if another fence is already there and new fence will overlap or intersect with the fence
        fences_at_desired_coord = self._get_list_fences_at_coordinate(desired_coord)
        if len(fences_at_desired_coord) > 0:
            print("There's fence(s) here")  # debug
            # check if there's already a fence with that direction
            for fence in fences_at_desired_coord:
                if fence.get_fence_direction() == direction:
                    print("False: Fence with direction", direction, "already at", desired_coord)
                    return False

        # place fence
        self._board[desired_coord]["fence"].append(Fence(direction))
        print("placing fence at ", desired_coord)
        this_player.decrement_num_fences_available()
        print("player ", this_player.get_player_num(), "remaining_fences=", this_player.get_num_fences_available())

        # update current turn to the other player for the next round
        print("updating turn")
        self._change_current_turn()  # TODO: put in function decorator


    def _fence_coordinate_within_boundary(self, coordinate):
        # TODO: currently used for fence, can prob use for pawn too
        x = coordinate[0]
        y = coordinate[1]

        if x < 0 or x > 8:
            return False
        if y < 0 or y > 8:
            return False
        return True

    def _pawn_coordinate_within_boundary(self, coordinate):
        # TODO: currently used for fence, can prob use for pawn too
        col_num = coordinate[0]
        row_num = coordinate[1]

        if col_num < -1 or col_num > 9:
            return False
        if row_num < -1 or row_num > 9:
            return False
        return True

    def _get_valid_pawn_moves(self, player):
        valid_moves = []
        current_pawn_coordinate = player.get_pawn_coordinate()
        print("current_pawn_coordinate=", current_pawn_coordinate)

        # check north
        valid_moves.extend(self._get_valid_north_pawn_moves(current_pawn_coordinate))

        # check east

        # check south

        # check west

    def _get_valid_north_pawn_moves(self, current_pawn_coordinate):
        curr_col = current_pawn_coordinate[0]
        curr_row = current_pawn_coordinate[1]
        valid_north_moves = []
        fences_in_curr_coordinate = self._get_list_fences_at_coordinate(current_pawn_coordinate)

        # check if there's a horizontal fence at current coordinate blocking northern moves
        if len(fences_in_curr_coordinate) > 0:
            # print("There's fence(s) north of current coordinate (", str(current_pawn_coordinate), ") with directions: ", end="")

            # get fence(s) direction
            for fence in fences_in_curr_coordinate:
                if fence.get_fence_direction() == "h" or fence.get_fence_direction() == "edge":
                    print("NORTH: Fence", fence.get_fence_direction(), current_pawn_coordinate, "is blocking pawn from going north.")


        # north_row = curr_row - 1
        # north_coordinate = (curr_col, north_row)
        #
        # if north_row < 0: # if row north of current row is within bounds
        #     # check if a fence is there
        #     if len(self._get_list_fences_at_coordinate())

        return valid_north_moves

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

class Fence:  # TODO: maybe not needed
    def __init__(self, direction):
        self._v = False
        self._h = False
        self._edge = False

        if direction == "edge":
            self._edge = True
        if direction == "h":
            self._h = True
        if direction == "v":
            self._v = True
        # self._direction = direction  # horizontal, vertical, or edge

    def get_fence_direction(self):
        # return self._direction
        if self._edge:
            return "edge"
        if self._h:
            return "h"
        if self._v:
            return "v"

# class Pawn:
#     def __init__(self, player_num):
#         self._player = player_num
#
#
#     def get_pawn_number(self):
#         return self._player


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

        if player_num == 1:
            self._pawn_coordinate = (4, 0)
        else:
            self._pawn_coordinate = (4, 8)

        # self._pawn = Pawn(1, (4, 8))
        # # move_pawn(1, (4, 8))

    def set_pawn_coordinate(self, coordinate):
        self._pawn_coordinate = coordinate

    def get_pawn_coordinate(self):
        return self._pawn_coordinate

    def get_player_num(self):
        return self._player_num

    def get_num_fences_available(self):  # TODO: maybe not needed
        return self._num_fences_available

    def has_fences_remaining(self):
        if self._num_fences_available == 0:
            return False
        return True

    def decrement_num_fences_available(self):
        self._num_fences_available -= 1


q = QuoridorGame()
q._print_board()
# print(q.move_pawn(2, (4, 7)))  #moves the Player2 pawn -- invalid move because only Player1 can start, returns False
# print(q.move_pawn(1, (4, 1)))  #moves the Player1 pawn -- valid move, returns True


# this_player = q.get_player_from_num(1)  # get player from num
# for i in range(10): # test no fences
#     this_player.decrement_num_fences_available()
# print(this_player.get_num_fences_available())
# print(q.place_fence(1, 'h', (6, 5)))

print()
print(q.place_fence(2, 'v', (6, 5)))
q._print_board()

print()
print(q.place_fence(1, 'h', (4, 8)))
q._print_board()

print()
print(q.move_pawn(2, (4, 6)))
q._print_board()

print()
print(q.move_pawn(1, (4, -1)))
q._print_board()