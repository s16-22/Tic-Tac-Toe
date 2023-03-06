# write your code here
player_1 = "X"
player_2 = "O"
current_player = player_1


def printer(enter):
    print("---------")
    print(f'| {" ".join(enter[0:3])} |')
    print(f'| {" ".join(enter[3:6])} |')
    print(f'| {" ".join(enter[6:9])} |')
    print("---------")


def coordinates(enter):
    global current_player
    try:
        row, column = input().split()
        if int(row) > 3 or int(column) > 3:
            print("Coordinates should be from 1 to 3!")
            return coordinates(enter)
        column = int(column) + 2
        row = int(row) - 1
        index = (row * 3 + column) - 3
    except ValueError:
        print("You should enter numbers!")
        return coordinates(enter)
    if enter[index] == " ":
        enter[index] = current_player
    else:
        print("This cell is occupied! Choose another one!")
        return coordinates(enter)
    current_player = "O" if current_player == "X" else "X"


def winner(enter):
    winners = list()
    winners.append(enter[0:3])  # 0 по строкам
    winners.append(enter[3:6])  # 1 по строкам
    winners.append(enter[6:9])  # 2 по строкам

    winners.append(enter[0::3])  # 3 по столбцам
    winners.append(enter[1::3])  # 4 по столбцам
    winners.append(enter[2::3])  # 5 по столбцам

    winners.append(enter[2:7:2])  # 6 по диагонали
    winners.append(enter[0:9:4])  # 7 по диагонали

    if winners.count(['X', 'X', 'X']) and winners.count(['O', 'O', 'O']) or abs(
            enter.count("X") - enter.count("O")) >= 2:
        print("Impossible")
        return 1
    # else:
    #     if winners.count(['X', 'X', 'X']) == 0 and winners.count(['O', 'O', 'O']) == 0 and enter.count('_') > 0:
    #         print("Game not finished")
    #         return 1
    else:
        if winners.count(['X', 'X', 'X']) == 0 and winners.count(['O', 'O', 'O']) == 0 and enter.count(' ') == 0:
            print("Draw")
            return 1
        else:
            if winners.count(['X', 'X', 'X']) or winners.count(['O', 'O', 'O']):
                if (winners[0][0] != 'current_player') and (winners[0][0] == winners[0][1]) and (winners[0][1] == winners[0][2]):
                    print(f"{winners[0][0]} wins")
                    return 1
                elif (winners[1][0] != 'current_player') and (winners[1][0] == winners[1][1]) and (winners[1][1] == winners[1][2]):
                    print(f"{winners[1][0]} wins")
                    return 1
                elif (winners[2][0] != 'current_player') and (winners[2][0] == winners[2][1]) and (winners[2][1] == winners[2][2]):
                    print(f"{winners[2][0]} wins")
                    return 1
                elif (winners[3][0] != 'current_player') and (winners[3][0] == winners[3][1]) and (winners[3][1] == winners[3][2]):
                    print(f"{winners[3][0]} wins")
                    return 1
                elif (winners[4][0] != 'current_player') and (winners[4][0] == winners[4][1]) and (winners[4][1] == winners[4][2]):
                    print(f"{winners[4][0]} wins")
                    return 1
                elif (winners[5][0] != 'current_player') and (winners[5][0] == winners[5][1]) and (winners[5][1] == winners[5][2]):
                    print(f"{winners[5][0]} wins")
                    return 1
                elif (winners[6][0] != 'current_player') and (winners[6][0] == winners[6][1]) and (winners[6][1] == winners[6][2]):
                    print(f"{winners[6][0]} wins")
                    return 1
                elif (winners[7][0] != 'current_player') and (winners[7][0] == winners[7][1]) and (winners[7][1] == winners[7][2]):
                    print(f"{winners[7][0]} wins")
                    return 1


def main():
    enter = [" " for _ in range(9)]
    while True:
        winner(enter)
        printer(enter)
        if winner(enter) == 1:
            break
        coordinates(enter)




if __name__ == '__main__':
    main()
