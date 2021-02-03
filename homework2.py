import random


def gameRSP(first_item):
    """ a function that emulates the game "rock, scissors, paper """

    available_items = ['rock', 'scissors', 'paper']

    if first_item not in available_items:
        raise ValueError(f"item must be in {available_items}")
    second_item = random.choice(available_items)
    print(f"{first_item} vs {second_item}")
    if first_item == second_item:
        print("draw")
    elif first_item == 'rock' and second_item == 'scissors' or \
        first_item == 'scissors' and second_item == 'paper' or \
        first_item == 'paper' and second_item == 'rock':
        print("You are a winner!")
    else:
        print("You are lose!")


def is_enough_toilet_paper(data):
    """ Return a statement telling the user if 
    they need to buy more TP """

    if not ("people" in data and "tp" in data):
        raise KeyError("there are not correct keys in dict")
    if data["people"] * 57 * 14 <= data["tp"] * 500:
        return True
    return False


def encrypt(data):
    """a function that encrypts a given input"""

    key_dict = {'a': 0, 'e': 1, 'i': 2, 'o': 2, 'u': 3}
    reverse_data = data[::-1]
    lower_case_data = reverse_data.lower()
    for key in key_dict:
        lower_case_data = lower_case_data.replace(key, str(key_dict[key]))
    return lower_case_data


def tic_tac_toe(game_field):
    """
    a function that returns whether the game is a win 
    for "X", "O", or a "Draw", where "X" and "O" 
    represent themselves on the matrix
    """

    for row in game_field:
        if row[0] == row[1] == row[2]:
            return row[0]
    for col in range(3):
        if game_field[0][col] == game_field[1][col] == game_field[2][col]:
            return game_field[0][col]
    if game_field[0][0] == game_field[1][1] == game_field[2][2]:
        return game_field[0][0]
    if game_field[0][2] == game_field[1][1] == game_field[2][0]:
        return game_field[0][2]
    return "Draw"


if __name__ == '__main__':
    #-------------------------------------------------------------#
    # 1
    #-------------------------------------------------------------#
    item = input("enter your item:")
    gameRSP(item)
    
    #-------------------------------------------------------------#
    # 2
    #-------------------------------------------------------------#
    result = is_enough_toilet_paper({
        "people": 12,
        "tp": 24
    })
    print(f'2:\t{result}')

    #-------------------------------------------------------------#
    # 3
    #-------------------------------------------------------------#
    word = "banana"
    print(f'4:\t{word} --> {encrypt(word)}')

    #-------------------------------------------------------------#
    # 4
    #-------------------------------------------------------------#
    winner = tic_tac_toe([
        ["X", "X", "X"],
        ["X", "O", "O"],
        ["O", "O", "E"]
    ])
    print(f'4:\t{winner}')