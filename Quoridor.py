# Name: Jennifer Um
# Date: 2021-08-06
# Description: Create a Quoridor class

# TODO:
#  - verify function names (_ in front for private)
#  - create unit tests
#  - recursion extra credit
#  - erase debug statements

class QuoridorGame:
    """
    Class for a Quoridor game.
    - Interacts with Fence class: Fences will be placed on the Quoridor game board.
    - Interacts with Player class: Players will have a number of fences, and each will have a pawn on the game board.
    """

    def __init__(self):
        # initialize the board
        self._status = "IN_PROGRESS"  # set to GAME_WON when game is won by a player
        self._winner = None  # will be set to either Player object
        self._player1 = Player(1)
        self._player2 = Player(2)
        self._players = [self._player1, self._player2]
        self._current_turn = self._player1
        self._board = self._generate_board()

    def has_game_been_won(self):
        """
        Checks if game has been won.
        :return: True if game has been won. False if game has not been won.
        """
        if self._status == "GAME_WON":
            return True
        return False

    def get_status(self):
        """
        Get the status of the game.
        :return: status of the game; either "IN_PROGRESS" or "GAME_WON"
        """
        return self._status

    def get_winner(self):
        """
        Get the winner of the game.
        :return: None if no player has won. Otherwise, return the winning Player object.
        """
        return self._winner

    def set_status_to_game_won_update_winner(self, player):
        """
        Set status to "GAME_WON" and update the winner to the winning Player object
        :param player: winning player object
        :return: none
        """
        self._status = "GAME_WON"
        self._winner = player

    def get_player_from_num(self, number):
        """
        Get Player object from a number
        :param number: player's number
        :return: Player object with that number
        """
        for player in self._players:
            if player.get_player_num() == number:
                return player
        return None

    def _generate_board(self):
        """
        Generate the Quoridor board and starting positions of each player's pawn
        - the board has 10 rows and 10 columns
            - 100 coordinates with 81 playable coordinates
            - coordinates in row 9 and column 9 are not playable coordinates, but were created to act as edge fences
            - each playable coordinate can have
                - a pawn
                - a vertical (v) fence and/or a horizontal (h) fence
                - column 0 and row 0 are playable coordinates that have v and/or h fences acting as edge fences
            - each non-playable coordinate has
                - a v fence and/or an h fence acting as edge fences
        :return:
            - a dictionary called "board" with
                key: coordinate
                value: a dictionary of
                    - key="pawn", value=None or Pawn object
                    - key="fences", value=empty list or list of Fence objects
            - sample board:
                {(column, row): {
                    "pawn": Pawn object (or None if no pawn at that coordinate),
                    "fence" = [Fence object(s) (if there are fences at that coordinate)]
                    }
                }
        """
        board = {}
        for row in range(0, 10):
            for col in range(0, 10):
                board[(col, row)] = {
                    "pawn": None,
                    "fence": []
                }

        # place player1 and player2 pawn in their starting positions
        for player in self._players:
            board[player.get_pawn_coordinate()]["pawn"] = player.get_player_num()
            # pawns are denoted by the player number

        # edges are fences
        for i in range(0, 10):
            board[(0, i)]["fence"].append(Fence("v"))
            board[(9, i)]["fence"].append(Fence("v"))
            board[(i, 0)]["fence"].append(Fence("h"))
            board[(i, 9)]["fence"].append(Fence("h"))

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
        return board

    def print_board(self):
        """
        Print the Quoridor board
        :return: none
        """
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
                    fence_string = "0"  # denoting no fences at that coordinate
                else:
                    fence_string = ""
                    for fence in self._board[this_coord]["fence"]:
                        fence_string += str(fence.get_fence_direction())  # append "v" and/or "h"

                location_string = str(this_coord) + ",pawn=" + pawn_string + ",fence=" + fence_string
                print(location_string.ljust(35), end="")
            print()

    def _get_current_turn(self):
        """
        Get the player whose turn it currently is
        :return: player whose turn it currently is
        """
        return self._current_turn

    def _change_current_turn(self):
        """
        Change the player whose turn it currently is
        :return: none
        """
        if self._current_turn == self._player1:
            self._current_turn = self._player2
        else:
            self._current_turn = self._player1

    def is_valid_current_turn(self, inputted_player):
        """
        Validate whose turn it currently is
        :param inputted_player: player that was entered in main
        :return: True if the current_turn is the inputted_player, False otherwise
        """
        if inputted_player == self._current_turn:
            return True
        return False

    def _get_list_fences_at_coordinate(self, coordinate):
        """
        Get fences at a coordinate as a list
        :param coordinate: inputted coordinate
        :return: list of Fences object at that coordinate
        """
        return self._board[coordinate]["fence"]

    def _get_pawn_at_coordinate(self, coordinate):
        """
        Get pawn at a coordinate
        :param coordinate: inputted coordinate
        :return: Pawn at that coordinate
        """
        return self._board[coordinate]["pawn"]

    def move_pawn(self, player_num, desired_coord):
        """
        Validate if a pawn can be moved to the desired coordinate; if so, move it there
        :param player_num: player's number
        :param desired_coord: coordinate player would like to move pawn to
        :return:
            False if
            - desired coordinate is forbidden by the rules
            - or desired coordinate is blocked by the fence
            - or game has already been won
            True if desired move makes the player win
        """
        # TODO: put in function decorator along with place_fence?

        # check if the game has already been won
        if self.has_game_been_won() is True:
            print("game has already been won")
            return False

        # get player from player_num
        this_player = self.get_player_from_num(player_num)
        print("moving_pawn_attempt\ncurrent_turn=", self._current_turn.get_player_num(), "this player=",
              this_player.get_player_num(), "desired_coord=", desired_coord)  # debug

        # check if player entered is the correct current player
        if not self.is_valid_current_turn(this_player):
            print("False: not valid current player")  # debug
            return False  # return False if invalid move

        # check if coordinate is forbidden by the rules (diagonal, move in orthogonal directions)
        # check if desired_coord is within valid pawn coordinate boundaries
        if not self._pawn_coordinate_within_boundary(desired_coord):
            print("False: not valid inputted coordinate")  # debug
            return False

        # get a list of valid moves/coordinates the pawn can move to with its current location
        valid_pawn_moves = self._get_valid_pawn_moves(this_player)
        print("valid_pawn_moves=", valid_pawn_moves)  # debug

        if desired_coord in valid_pawn_moves:
            print("Desired_coord is in valid_pawn_moves")  # debug

            # this_player.get_pawn_coordinate() will get player's current pawn coordinate on board
            # on board, update that current coordinate's Pawn key to None
            self._board[this_player.get_pawn_coordinate()]["pawn"] = None

            # update player object's current coordinate to desired coordinate
            this_player.set_pawn_coordinate(desired_coord)

            # update board to that player's new pawn coordinate
            self._board[this_player.get_pawn_coordinate()]["pawn"] = this_player.get_player_num()

            # determine if player has won with that new pawn coordinate
            if this_player.is_pawn_in_winning_coordinate() is True:
                self.set_status_to_game_won_update_winner(this_player)  # if so, change game status
                print("status=", self.get_status())  # debug
                print("winner=", self.get_winner().get_player_num())  # debug
                return True

            # update current turn to the other player for the next round
            print("updating turn")
            self._change_current_turn()
            return True

        else:  # if desired_coord is not in valid_pawn_moves
            print("invalid desired_coord; not updating current turn")
            return False

    def place_fence(self, player_num, direction, desired_coord):
        """
        Validate and place fence at desired coordinate.
        :param player_num: number of the player
        :param direction: direction of the fence (horizontal, vertical)
        :param desired_coord: coordinate player would like to move pawn to
        :return:
            False if
            - player has no fence left
            - fence is out of the boundaries of the board
            - if there is already a fence there and desired coordinate will overlap/ intersect with existing fence
            - if the game has already been won
            True if
            - fence can be placed there
        """
        # check if the game has already been won
        if self.has_game_been_won() is True:
            print("game has already been won")
            return False

        # get player from player_num
        this_player = self.get_player_from_num(player_num)
        print("placing_fence_attempt\ncurrent_turn=", self._current_turn.get_player_num(),
              "this player=", this_player.get_player_num(), "desired_coord", direction, desired_coord)  # debug

        # check if player entered is the correct current player
        if not self.is_valid_current_turn(this_player):  # TODO: put in function decorator
            print("False: not valid current player")  # debug
            return False  # return False if invalid move

        # check if player has fences left
        if not this_player.has_fences_remaining():
            print("False: does not have fences remaining")  # debug
            return False

        # check if desired_coord is within valid fence coordinate boundaries
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
        print("placing", direction, "fence at ", desired_coord)  # debug
        this_player.decrement_num_fences_available()
        print("player ", this_player.get_player_num(),
              "remaining_fences=", this_player.get_num_fences_available())  # debug

        # update current turn to the other player for the next round
        print("updating turn")  # debug
        self._change_current_turn()  # TODO: put in function decorator
        return True

    def _fence_coordinate_within_boundary(self, coordinate):
        """
        Check if coordinate of a fence is within the valid boundary
        :param coordinate: coordinate of the fence
        :return: False if it is within the valid boundary, True if it is not within the valid boundary
        """
        col_num = coordinate[0]
        row_num = coordinate[1]

        if col_num < 1 or col_num > 8:
            return False
        if row_num < 1 or row_num > 8:
            return False
        return True

    def _pawn_coordinate_within_boundary(self, coordinate):
        """
        Check if coordinate of a pawn is within the valid boundary
        :param coordinate: coordinate of the pawn
        :return: False if it is within the valid boundary, True if it is not within the valid boundary
        """
        col_num = coordinate[0]
        row_num = coordinate[1]

        if col_num < 0 or col_num > 8:
            return False
        if row_num < 0 or row_num > 8:
            return False
        return True

    def _get_valid_pawn_moves(self, player):
        """
        Get a list of valid moves a player's pawn can move to with its current coordinate
        :param player: player that is moving their pawn
        :return: list of valid moves a player's pawn can move to with its current coordinate
        """
        current_pawn_coordinate = player.get_pawn_coordinate()
        print("current_pawn_coordinate=", current_pawn_coordinate)  # debug

        # check valid moves in each direction
        valid_north = self._get_valid_north_pawn_moves(current_pawn_coordinate)
        valid_south = self._get_valid_south_pawn_moves(current_pawn_coordinate)
        valid_west = self._get_valid_west_pawn_moves(current_pawn_coordinate)
        valid_east = self._get_valid_east_pawn_moves(current_pawn_coordinate)
        valid_moves = valid_north + valid_south + valid_west + valid_east

        print("valid_north=", valid_north, "valid_south=", valid_south,
              "valid_west=", valid_west, "valid_east=", valid_east)

        return valid_moves

    def _get_valid_south_pawn_moves(self, current_pawn_coordinate):
        """
        Get list of southern, southeastern (se), and southwestern (sw) moves a pawn can move to.
        :param current_pawn_coordinate: current pawn coordinate
        :return: list of southern, southeastern (se), and southwestern (sw) moves a pawn can move to
        """
        # TODO: shorten
        curr_col = current_pawn_coordinate[0]
        curr_row = current_pawn_coordinate[1]
        valid_south_moves = []
        south_row = curr_row + 1

        s_coord = (curr_col, south_row)
        s_coord_is_valid = self._pawn_coordinate_within_boundary(s_coord)
        s_coord_has_h_fence = self._coordinate_has_h_fence(s_coord)

        se_coord = (curr_col + 1, curr_row + 1)
        se_coord_is_valid = self._pawn_coordinate_within_boundary(se_coord)

        sw_coord = (curr_col - 1, curr_row + 1)
        sw_coord_is_valid = self._pawn_coordinate_within_boundary(se_coord)

        s_of_s_coord = (curr_col, south_row+1)
        s_of_s_coord_is_valid = self._pawn_coordinate_within_boundary(s_of_s_coord)

        if s_coord_is_valid is False:
            # print("SOUTH: s_coord does not exist")  # debug
            return valid_south_moves  # empty list

        # check h fence directions in south coordinate
        if s_coord_has_h_fence:
            # print("SOUTH: Horizontal fence in", current_pawn_coordinate,"is blocking pawn from going south.")  # debug
            return valid_south_moves  # empty list because pawn can't go south

        # at this point, s_coord does exist and there's no immediate south fence blocking
        south_pawn = self._get_pawn_at_coordinate(s_coord)
        if south_pawn is not None:  # check if there's a pawn in the south coordinate
            # print("There is a south pawn", south_pawn, "in ", s_coord)   # debug

            # if no fence behind adjacent pawn
            if s_of_s_coord_is_valid is True and self._coordinate_has_h_fence(s_of_s_coord) is False:
                valid_south_moves.append(s_of_s_coord)
                return valid_south_moves

            # fence behind adjacent pawn
            if s_of_s_coord_is_valid is True and self._coordinate_has_h_fence(s_of_s_coord) is True:
                if se_coord_is_valid is True:  # check if we can move se
                    if self._coordinate_has_v_fence(se_coord) is False:
                        valid_south_moves.append(se_coord)

                if sw_coord_is_valid is True:  # check if we can move sw
                    if self._coordinate_has_v_fence(sw_coord) is False:
                        valid_south_moves.append(sw_coord)

        else:  # if there's no pawn in south coordinate blocking
            valid_south_moves.append(s_coord)

        return valid_south_moves

    def _coordinate_has_v_fence(self, coordinate):
        """
        Check if coordinate has a vertical fence
        :param coordinate: inputted coordinate
        :return: True if the coordinate has a vertical fence. False otherwise.
        """
        for fence in self._get_list_fences_at_coordinate(coordinate):
            if fence.get_fence_direction() == "v":
                return True
        return False

    def _coordinate_has_h_fence(self, coordinate):
        """
        Check if coordinate has a horizontal fence
        :param coordinate: inputted coordinate
        :return: True if the coordinate has a horizontal fence. False otherwise.
        """
        for fence in self._get_list_fences_at_coordinate(coordinate):
            if fence.get_fence_direction() == "h":
                return True
        return False

    def _get_valid_north_pawn_moves(self, current_pawn_coordinate):
        """
        Get list of northern, northeastern (ne), and northwestern (nw) moves a pawn can move to.
        :param current_pawn_coordinate: current pawn coordinate
        :return: list of northern, northeastern (ne), and northwestern (nw) moves a pawn can move to
        """
        # TODO: shorten
        curr_col = current_pawn_coordinate[0]
        curr_row = current_pawn_coordinate[1]
        valid_north_moves = []
        north_row = curr_row - 1

        n_coord = (curr_col, north_row)
        n_coord_is_valid = self._pawn_coordinate_within_boundary(n_coord)

        ne_coord = (curr_col + 1, north_row)
        ne_coord_is_valid = self._pawn_coordinate_within_boundary(ne_coord)

        nw_coord = (curr_col - 1, north_row)
        nw_coord_is_valid = self._pawn_coordinate_within_boundary(nw_coord)

        n_of_n_coord = (curr_col, north_row+1)
        n_of_n_coord_is_valid = self._pawn_coordinate_within_boundary(n_of_n_coord)

        if n_coord_is_valid is False:
            # print("North: n_coord does not exist")  # debug
            return valid_north_moves  # empty list

        current_coord_has_h_fence = self._coordinate_has_h_fence(current_pawn_coordinate)
        if current_coord_has_h_fence:
            # print("NORTH: Fence h in", current_pawn_coordinate, "is blocking pawn from going north.")  # debug
            return valid_north_moves  # empty list

        # at this point, n_coord does exist and there's no immediate north fence blocking
        north_pawn = self._get_pawn_at_coordinate(n_coord)
        if north_pawn is not None:  # check if there's a pawn in the north coordinate
            # print("There is a north pawn", north_pawn, "in ", n_coord)  # debug

            if n_of_n_coord_is_valid and self._coordinate_has_h_fence(n_coord) is False:
                valid_north_moves.append(n_of_n_coord)
                return valid_north_moves

            if n_of_n_coord_is_valid is True and self._coordinate_has_h_fence(n_coord) is True:
                if nw_coord_is_valid is True:
                    if self._coordinate_has_v_fence(n_coord) is False:  # check if we can move nw
                        valid_north_moves.append(nw_coord)
                if ne_coord_is_valid is True:
                    if self._coordinate_has_v_fence(ne_coord) is False:
                        valid_north_moves.append(ne_coord)
        else:  # if there's no pawn in n_coord blocking
            valid_north_moves.append(n_coord)
        return valid_north_moves

    def _get_valid_west_pawn_moves(self, current_pawn_coordinate):
        """
        Get list of western, northwestern (nw), and southwestern (se) moves a pawn can move to.
        :param current_pawn_coordinate: current pawn coordinate
        :return: list of western, northwestern (nw), and southwestern (se) moves a pawn can move to.
        """
        # TODO: shorten
        curr_col = current_pawn_coordinate[0]
        curr_row = current_pawn_coordinate[1]
        valid_west_moves = []
        west_col = curr_col - 1

        w_coord = (west_col, curr_row)
        w_coord_is_valid = self._pawn_coordinate_within_boundary(w_coord)

        w_of_w_coord = (west_col - 1, curr_row)
        w_of_w_coord_is_valid = self._pawn_coordinate_within_boundary(w_of_w_coord)

        nw_coord = (west_col, curr_row-1)
        nw_coord_is_valid = self._pawn_coordinate_within_boundary(nw_coord)

        sw_coord = (west_col, curr_row+1)
        sw_coord_is_valid = self._pawn_coordinate_within_boundary(sw_coord)

        # print("w_coord", w_coord)  # debug
        # print("nw_coord", nw_coord)  # debug
        # print("sw_coord", sw_coord)  # debug
        # print("w_of_w_coord", w_of_w_coord)  # debug

        if w_coord_is_valid is False:
            # print("w_coord does not exist")  # debug
            return valid_west_moves  # empty list

        # check if immediate western fence is blocking
        if self._coordinate_has_v_fence(current_pawn_coordinate):
            # print("immediate western fence blocking pawn from going west")  # debug
            return valid_west_moves  # empty list

        # at this point, w_coord does exist and there's no immediate western fence blocking
        west_pawn = self._get_pawn_at_coordinate(w_coord)
        if west_pawn is not None:
            # print("There's a west pawn at", w_coord)  # debug

            # no fence behind adjacent pawn
            if w_of_w_coord_is_valid is True and self._coordinate_has_v_fence(w_coord) is False:
                valid_west_moves.append(w_of_w_coord)
                return valid_west_moves

            # fence behind adjacent pawn
            if w_of_w_coord_is_valid is True and self._coordinate_has_v_fence(w_coord) is True:
                if nw_coord_is_valid is True:
                    if self._coordinate_has_h_fence(w_coord) is False:
                        valid_west_moves.append(nw_coord)
                        # print("no h fence at current coordinate; valid_west_moves=", valid_west_moves)  # debug

                if sw_coord_is_valid is True:
                    if self._coordinate_has_h_fence(sw_coord) is False:
                        valid_west_moves.append(sw_coord)
                        # print("no h fence at sw_coord. valid_west_moves=", valid_west_moves)  # debug
                # print("valid_west_moves", valid_west_moves)  # debug

        else:  # if there's no pawn in west coordinate blocking
            valid_west_moves.append(w_coord)

        return valid_west_moves

    def _get_valid_east_pawn_moves(self, current_pawn_coordinate):
        """
        Get list of eastern, northeastern (ne), and southeastern (se) moves a pawn can move to.
        :param current_pawn_coordinate: current pawn coordinate
        :return: list of eastern, northeastern (ne), and southeastern (se) moves a pawn can move to.
        """
        # TODO: shorten
        curr_col = current_pawn_coordinate[0]
        curr_row = current_pawn_coordinate[1]
        valid_east_moves = []
        east_col = curr_col + 1

        e_coord = (east_col, curr_row)
        e_coord_is_valid = self._pawn_coordinate_within_boundary(e_coord)

        e_of_e_coord = (east_col+1, curr_row)
        e_of_e_coord_is_valid = self._pawn_coordinate_within_boundary(e_of_e_coord)

        ne_coord = (east_col, curr_row-1)
        ne_coord_is_valid = self._pawn_coordinate_within_boundary(ne_coord)

        se_coord = (east_col, curr_row+1)
        se_coord_is_valid = self._pawn_coordinate_within_boundary(se_coord)

        # print("e_coord", e_coord)  # debug
        # print("ne_coord", ne_coord)  # debug
        # print("se_coord", se_coord)  # debug
        # print("e_of_e_coord", e_of_e_coord)  # debug

        if e_coord_is_valid is False:
            # print("e_coord does not exist")  # debug
            return valid_east_moves  # empty list

        # check if immediate eastern fence is blocking
        if self._coordinate_has_v_fence(e_coord) is True:
            # print("immediate eastern fence blocking pawn from going east")  # debug
            return valid_east_moves  # empty list

        # at this point, e_coord does exist and there's no immediate western fence blocking
        east_pawn = self._get_pawn_at_coordinate(e_coord)
        if east_pawn is not None:
            # print("There's an east pawn at", e_coord)  # debug

            # no fence behind adjacent pawn
            if e_of_e_coord_is_valid is True and self._coordinate_has_v_fence(e_of_e_coord) is False:
                valid_east_moves.append(e_of_e_coord)
                return valid_east_moves

            # fence behind adjacent pawn
            if e_of_e_coord_is_valid is True and self._coordinate_has_v_fence(e_of_e_coord) is True:
                if ne_coord_is_valid is True:
                    if self._coordinate_has_h_fence(e_coord) is False:
                        valid_east_moves.append(ne_coord)
                if se_coord_is_valid is True:
                    if self._coordinate_has_h_fence(se_coord) is False:
                        valid_east_moves.append(se_coord)

        else:  # if there's no pawn in east coordinate blocking
            valid_east_moves.append(e_coord)

        return valid_east_moves

    def is_winner(self, player_num):
        """
        Get if player has won
        :param player_num: player's number
        :return: True if that player has won, False if that player has not won
        """
        this_player = self.get_player_from_num(player_num)
        if self.get_winner() == this_player:
            return True
        return False


class Fence:
    """
    Class for a fence piece.
    Interacts with QuoridorGame class: fence objects with directions are placed on the board.
    """
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
        """
        Get a fence object's direction
        :return: fence object's direction as a string
        """
        if self._edge:
            return "edge"
        if self._h:
            return "h"
        if self._v:
            return "v"


class Player:
    """
    Class for a Player.
    Interacts with QuoridorGame class: Players will have a number of fences, and each will have a pawn on the game board
    """
    def __init__(self, player_num):
        self._player_num = player_num
        self._num_fences_available = 10

        if player_num == 1:
            self._pawn_coordinate = (4, 0)
            self._winning_coordinates = [(0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8)]
        else:  # if player 2
            self._pawn_coordinate = (4, 8)
            self._winning_coordinates = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)]

    def is_pawn_in_winning_coordinate(self):
        """
        Check if player's pawn is in a winning coordinate.
        :return: True if player's pawn is in a winning coordinate, False otherwise
        """
        if self._pawn_coordinate in self._winning_coordinates:
            return True
        return False

    def set_pawn_coordinate(self, coordinate):
        """
        Set the coordinate of a player's pawn
        :param coordinate: coordinate of a player's pawn
        :return: none
        """
        self._pawn_coordinate = coordinate

    def get_pawn_coordinate(self):
        """
        Get a player's pawn coordinate
        :return: player's pawn coordinate
        """
        return self._pawn_coordinate

    def get_player_num(self):
        """
        Get the player's number
        :return: player's number as an integer
        """
        return self._player_num

    def get_num_fences_available(self):
        """
        Get the number of fences a player has left
        :return: number of fences a player has left
        """
        return self._num_fences_available

    def has_fences_remaining(self):
        """
        Checks if a player has fences remaining
        :return: True if a player has fences remaining, False otherwise
        """
        if self._num_fences_available == 0:
            return False
        return True

    def decrement_num_fences_available(self):
        """
        Subtract one from the number of fences a player has left
        :return: none
        """
        self._num_fences_available -= 1


q = QuoridorGame()
q.print_board()
# print(q.move_pawn(2, (4, 7)))  #moves the Player2 pawn -- invalid move because only Player1 can start, returns False
# print(q.move_pawn(1, (4, 1)))  #moves the Player1 pawn -- valid move, returns True


# this_player = q.get_player_from_num(1)  # get player from num
# for i in range(10): # test no fences
#     this_player.decrement_num_fences_available()
# print(this_player.get_num_fences_available())
# print(q.place_fence(1, 'h', (6, 5)))

print()
print(q.place_fence(2, 'v', (6, 5)))
q.print_board()

# print()
# print(q.place_fence(1, 'v', (4, 8)))
# q._print_board()

# print()
# print(q.move_pawn(2, (4, 7)))
# q._print_board()
#
print()
print(q.move_pawn(1, (4, 1)))
q.print_board()

print()
print(q.move_pawn(2, (0, 0)))
q.print_board()

print(q.is_winner(2))
