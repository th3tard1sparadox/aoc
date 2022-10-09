with open("input4.txt") as file:
    inputs = file.readlines()

numbers = [int(i) for i in inputs[0].split(',')]
boards = []
board = []
for row in inputs[2:]:
    if row == '\n':
        boards.append(board)
        board = []
    else:
        board.append([int(item) for item in row.split()])
boards.append(board)


def check_rows(board, nums):
    for row in board:
        if all(item in nums for item in row):
            return True
    return False


def check_cols(board, nums):
    for i in range(len(board[0])):
        col = []
        for row in board:
            col.append(row[i])
        if all (item in nums for item in col):
            return True
    return False


def when_win(board, numbers):
    checked_nums = []
    for i, num in enumerate(numbers):
        checked_nums.append(num)
        if check_rows(board, checked_nums) or check_cols(board, checked_nums):
            return i
    return len(numbers) + 1


def not_called(board, called):
    not_called = []
    for row in board:
        for num in row:
            if num not in called:
                not_called.append(num)
    return(sum(not_called))


def first_win(boards, numbers):
    smallest = len(numbers) + 1
    number_called = 0
    first_board = []
    for board in boards:
        win = when_win(board, numbers)
        if win < smallest:
            smallest = win
            number_called = numbers[win]
            first_board = board.copy()
    return(not_called(first_board, numbers[:smallest + 1]) * number_called)


print("problem 1:" + str(first_win(boards, numbers)))


def last_win(boards, numbers):
    largest = 0
    number_called = 0
    first_board = []
    for board in boards:
        win = when_win(board, numbers)
        if win > largest:
            largest = win
            number_called = numbers[win]
            first_board = board.copy()
    return(not_called(first_board, numbers[:largest + 1]) * number_called)


print("problem 2:" + str(last_win(boards, numbers)))
