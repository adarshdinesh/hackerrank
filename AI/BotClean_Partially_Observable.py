#!/usr/bin/python3
def getpos(r,c, posr, posc):
    dx = abs(r - posr)
    dy = abs(c - posc)
    return dx+dy

def read():
    try:
        f = open('dat','r')
        dat = f.read().strip()
        color = eval(dat)
        f.close()
    except:
        color = []
    return color

def write(color):
    f = open('dat', 'w')
    f.write(str(color))
    f.close()


def next_move(posr, posc, board):
    r,c = (posr, posc)
    lst = {}
    color = read()
    for i, row  in enumerate(board):
        for j, val in enumerate(list(row)):
            if val !='o' and (i,j) in color:
                color.remove((i,j))
            if val == 'o' and (i,j) not in color:
                color.append((i,j))
    write(color)
    minm = 1000
    for i, row  in enumerate(board):
        for j, val in enumerate(list(row)):
            if val == 'd':
                if (i,j) == (r,c):
                    print('CLEAN')
                    return
                if getpos(r, c, i, j) not in lst:
                    lst[getpos(r, c, i, j)] = [(i,j)]
                else:
                    lst[getpos(r, c, i, j)].append((i,j))
    if not lst:
        p,q = color[0]
        shc, shr = p-r, q-c
        if shr>0:
            print('RIGHT')
        elif shr<0:
            print('LEFT')
        elif shc>0:
            print('DOWN')
        elif shc<0:
            print('UP')
        else:
            print('CLEAN')
        return
    
    p,q = lst[min(lst)][0]
    shc, shr = p-r, q-c
    if shr>0:
        print('RIGHT')
    elif shr<0:
        print('LEFT')
    elif shc>0:
        print('DOWN')
    elif shc<0:
        print('UP')
    else:
        print('CLEAN')
    return

if __name__ == "__main__": 
    pos = [int(i) for i in input().strip().split()] 
    board = [[j for j in input().strip()] for i in range(5)]  
    next_move(pos[0], pos[1], board)

