import os
import time

def main():
    content = '北京欢迎你为你开天辟地…………'
    for _ in range(100):
        # 清理屏幕的输出
        os.system('cls') # os.system('clear')
        print(content)

        # 休眠200ms
        time.sleep(0.2)
        content = content[1:] + content[0]

def get_suffix(filename, has_dot=False):
    """
    get the suffix of filename
    :filename
    :has_dot: Whether the suffix name returned needs to be dotted
    :reutrn : the suffix of filename
    """

    pos = filename.rfind('.')
    if 0 < pos < len(filename)-1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''

def max2(x):
    """
    : 返回传入的列表中最大  和  第二大的元素的值。
    """
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if m2 < x[index]:
            m2 = x[index]
        
        if m1 < m2:
            m1, m2 = m2, m1
    return m1, m2

def yanghuiTriangle():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()

from random import randrange, randint, sample
def display(balls):
    '''
    输出列表中的双色球号码
    '''
    # 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('| ', end='')
        print('%-2d ' % ball, end='')
    print()

def random_select():
    n = int(input('机选几注: '))
    for _ in range(n):
        """
        随机选择一组号码
        """
        red_balls = [x for x in range(1, 34)]
        selected_balls = []
        selected_balls = sample(red_balls, 6)
        selected_balls.sort()
        selected_balls.append(randint(1, 16))

        display(selected_balls)


def Joseph_ring():
    """
    : 约瑟夫环问题。
    《幸运的基督徒》
    有15个基督徒和15个非基督徒在海上遇险，
    为了能让一部分人活下来不得不将其中15个人扔到海里面去，
    有个人想了个办法就是大家围成一个圈，
    由某个人开始从1报数，报到9的人就扔到海里面，
    他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。
    由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，
    哪些位置是基督徒哪些位置是非基督徒。
    """
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index] == True:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    
    for person in persons:
        print('基 ' if person else '非 ', end='')
    
def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

def Keener_Tic_Tac_Toe():
    '''
    井字棋游戏。
    '''
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }

    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False

        turn = 'x'
        counter = 0
        os.system('cls')
        print_board(curr_board)

        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('cls')
            print_board(curr_board)
        choise = input('再玩一局?(yes|no)')
        begin = choise == 'yes'




if __name__ == '__main__':
    # main()
    # print(get_suffix('helo.py'))
    
    # x = [2, 4, 9, 7, 5, 10]
    # print(max2(x))
    # yanghuiTriangle()

    # random_select()

    # Joseph_ring()

    Keener_Tic_Tac_Toe()
