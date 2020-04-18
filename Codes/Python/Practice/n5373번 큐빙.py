colors = ['w','g','b','o','r','y']
TCs = int(input())

def turn(idx, p_or_m):
    if p_or_m == '-':
        cube[idx][0][0], cube[idx][0][1], cube[idx][0][2], cube[idx][1][2], cube[idx][2][2], cube[idx][2][1],\
        cube[idx][2][0], cube[idx][1][0] = cube[idx][0][2], cube[idx][1][2], cube[idx][2][2], cube[idx][2][1],\
                                           cube[idx][2][0], cube[idx][1][0], cube[idx][0][0], cube[idx][0][1]
    else:
        cube[idx][0][0], cube[idx][0][1], cube[idx][0][2], cube[idx][1][2], cube[idx][2][2], cube[idx][2][1], \
        cube[idx][2][0], cube[idx][1][0] = cube[idx][2][0], cube[idx][1][0], cube[idx][0][0], cube[idx][0][1], \
                                           cube[idx][0][2], cube[idx][1][2], cube[idx][2][2], cube[idx][2][1]

def move_2_plus():
    for i in range(3):
        cube[4][i][0], cube[1][i][0], cube[5][i][0], cube[6][i][0] = cube[6][i][0], cube[4][i][0], cube[1][i][0],\
                                                                     cube[5][i][0]

def move_2_minus():
    for i in range(3):
        cube[4][i][0], cube[1][i][0], cube[5][i][0], cube[6][i][0] = cube[1][i][0], cube[5][i][0], cube[6][i][0], \
                                                                     cube[4][i][0]

def move_3_minus():
    for i in range(3):
        cube[4][i][2], cube[1][i][2], cube[5][i][2], cube[6][i][2] = cube[6][i][2], cube[4][i][2], cube[1][i][2], \
                                                                     cube[5][i][2]

def move_3_plus():
    for i in range(3):
        cube[4][i][2], cube[1][i][2], cube[5][i][2], cube[6][i][2] = cube[1][i][2], cube[5][i][2], cube[6][i][2], \
                                                                     cube[4][i][2]

def move_4_plus():
    for i in range(3):
        cube[2][0][i], cube[1][0][i], cube[3][0][i], cube[6][2][2-i] = cube[1][0][i], cube[3][0][i], cube[6][2][2-i], \
                                                                     cube[2][0][i]

def move_4_minus():
    for i in range(3):
        cube[2][0][i], cube[1][0][i], cube[3][0][i], cube[6][2][2-i] = cube[6][2][2-i], cube[2][0][i], cube[1][0][i], \
                                                                     cube[3][0][i]

def move_5_plus():
    for i in range(3):
        cube[2][2][i], cube[1][2][i], cube[3][2][i], cube[6][0][2-i] = cube[6][0][2-i], cube[2][2][i], cube[1][2][i], \
                                                                     cube[3][2][i]

def move_5_minus():
    for i in range(3):
        cube[2][2][i], cube[1][2][i], cube[3][2][i], cube[6][0][2-i] = cube[1][2][i], cube[3][2][i], cube[6][0][2-i], \
                                                                     cube[2][2][i]

def move_1_plus():
    for i in range(3):
        cube[2][i][2], cube[4][2][2-i], cube[3][2-i][0], cube[5][0][i] = cube[5][0][i], cube[2][i][2], cube[4][2][2-i],\
                                                                         cube[3][2-i][0]

def move_1_minus():
    for i in range(3):
        cube[2][i][2], cube[4][2][2-i], cube[3][2-i][0], cube[5][0][i] = cube[4][2][2-i], cube[3][2-i][0], cube[5][0][i],  \
                                                                         cube[2][i][2]

def move_6_plus():
    for i in range(3):
        cube[2][i][0], cube[4][0][2-i], cube[3][2-i][2], cube[5][2][i] = cube[4][0][2-i], cube[3][2-i][2], cube[5][2][i],\
                                                                         cube[2][i][0]

def move_6_minus():
    for i in range(3):
        cube[2][i][0], cube[4][0][2-i], cube[3][2-i][2], cube[5][2][i] = cube[5][2][i], cube[2][i][0], cube[4][0][2-i],\
                                                                         cube[3][2-i][2]

for tc in range(TCs):
    cube = [[]]

    for i in range(6):
        tmp = [[colors[i] for k in range(3)] for j in range(3)]
        cube.append(tmp)

    moves = int(input())

    moves_list = input().split()

    for move in moves_list:
        side = move[0]
        direction = move[1]

        if side == 'U':
            if direction == '+':
                turn(1,direction)
                move_1_plus()
            else:
                turn(1,direction)
                move_1_minus()
        elif side == 'L':
            if direction == '+':
                turn(2,direction)
                move_2_plus()
            else:
                turn(2,direction)
                move_2_minus()
        elif side == 'R':
            if direction == '+':
                turn(3,direction)
                move_3_plus()
            else:
                turn(3,direction)
                move_3_minus()
        elif side == 'B':
            if direction == '+':
                turn(4 ,direction)
                move_4_plus()
            else:
                turn(4,direction)
                move_4_minus()
        elif side == 'F':
            if direction == '+':
                turn(5,direction)
                move_5_plus()
            else:
                turn(5,direction)
                move_5_minus()
        elif side == 'D':
            if direction == '+':
                turn(6,direction)
                move_6_plus()
            else:
                turn(6,direction)
                move_6_minus()

    for row in cube[1]:
        s = ''.join(row)
        print(s)
