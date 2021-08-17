import random
import sys

# 黒:〇:Human
# 白:●:Com

def hyoji(y, x):
    if board[y][x] == 'n':
        return '　'

    if board[y][x] == 'w':
        return '●'

    if board[y][x] == 'b':
        return '〇'

    if board[y][x] == 'a':
        return '・' 

    if board[y][x] == 'd':
        return '　'

def ban():
    print ("  　０　１　２　３　４　５　６　７Ｘ")
    print ("  ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
    print ("０＊" + hyoji(0, 0) + "＊" + hyoji(0, 1) + "＊" + hyoji(0, 2) + "＊" + hyoji(0, 3) + "＊" + hyoji(0, 4) + "＊" + hyoji(0, 5) + "＊" + hyoji(0, 6) + "＊" + hyoji(0, 7)+ "＊")
    print ("  ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
    print ("１＊" + hyoji(1, 0) + "＊" + hyoji(1, 1) + "＊" + hyoji(1, 2) + "＊" + hyoji(1, 3) + "＊" + hyoji(1, 4) + "＊" + hyoji(1, 5) + "＊" + hyoji(1, 6) + "＊" + hyoji(1, 7) + "＊")
    print ("  ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
    print ("２＊" + hyoji(2, 0) + "＊" + hyoji(2, 1) + "＊" + hyoji(2, 2) + "＊" + hyoji(2, 3) + "＊" + hyoji(2, 4) + "＊" + hyoji(2, 5) + "＊" + hyoji(2, 6) + "＊" + hyoji(2, 7) + "＊")
    print ("　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
    print ("３＊" + hyoji(3, 0) + "＊" + hyoji(3, 1) + "＊" + hyoji(3, 2) + "＊" + hyoji(3, 3) + "＊" + hyoji(3, 4) + "＊" + hyoji(3, 5) + "＊" + hyoji(3, 6) + "＊" + hyoji(3, 7) + "＊")
    print ("　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
    print ("４＊" + hyoji(4, 0) + "＊" + hyoji(4, 1) + "＊" + hyoji(4, 2) + "＊" + hyoji(4, 3) + "＊" + hyoji(4, 4) + "＊" + hyoji(4, 5) + "＊" + hyoji(4, 6) + "＊" + hyoji(4, 7) + "＊")
    print ("　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
    print ("５＊" + hyoji(5, 0) + "＊" + hyoji(5, 1) + "＊" + hyoji(5, 2) + "＊" + hyoji(5, 3) + "＊" + hyoji(5, 4) + "＊" + hyoji(5, 5) + "＊" + hyoji(5, 6) + "＊" + hyoji(5, 7) + "＊")
    print ("　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
    print ("６＊" + hyoji(6, 0) + "＊" + hyoji(6, 1) + "＊" + hyoji(6, 2) + "＊" + hyoji(6, 3) + "＊" + hyoji(6, 4) + "＊" + hyoji(6, 5) + "＊" + hyoji(6, 6) + "＊" + hyoji(6, 7) + "＊")
    print ("　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
    print ("７＊" + hyoji(7, 0) + "＊" + hyoji(7, 1) + "＊" + hyoji(7, 2) + "＊" + hyoji(7, 3) + "＊" + hyoji(7, 4) + "＊" + hyoji(7, 5) + "＊" + hyoji(7, 6) + "＊" + hyoji(7, 7) + "＊")
    print ("Ｙ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")


def serch_mannaka(y, x, jibun, aite):

    if board[serch[0]][serch[1]] == jibun or board[serch[0]][serch[1]] == aite:
        return False

    return True

def serch_p(y, x, jibun, aite, p):
    y1 = y + muki[p][0]
    x1 = x + muki[p][1]

    if y1<0 or y1>7 or x1<0 or x1>7:
        return False

    if board[y1][x1] != aite:
        return False

    while True:
        y1 = y1 + muki[p][0]
        x1 = x1 + muki[p][1]

        if y1<0 or y1>7 or x1<0 or x1>7:
            return False

        if board[y1][x1] == jibun:
            return True

        if board[y1][x1] == 'n' or board[y1][x1] == 'a' or board[y1][x1] == 'd':
            return False

    return True

def kakunin(okeru):

    while True:
        print("置く場所をyxで入力：例）23")
        a = input()

        if len(a) != 2:
            continue

        bf=0

        try:
            b = okeru.index((int(a[0]), int(a[1])))

        except ValueError as error:
            bf=1
            print("置けません")

        if bf == 0:
            break
    return b

def hikkuri_p(p):
    y1 = okeru[kimeru][0] + muki[p][0]
    x1 = okeru[kimeru][1] + muki[p][1]

    hikkuri = []

    if y1>=0 and y1<=7 and x1>=0 and x1<=7:
        while board[y1][x1] == aite:
            hikkuri.append((y1, x1))

            y1 = y1 + muki[p][0]
            x1 = x1 + muki[p][1]

            if y1<0 or y1>7 or x1<0 or x1>7:
                break

            if board[y1][x1] == jibun:
                for item in hikkuri:
                    board[item[0]][item[1]] = jibun

                break

            if board[y1][x1] == 'a' or board[y1][x1] == 'd':
                break
    return 0

# main
ps = 0

muki = [(-1,-1), (-1,0), (-1, +1), (0, -1), (0, +1), (+1, -1), (+1, 0), (+1, +1)]

oitakazu = 4

board = [
          ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
          ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
          ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
          ['n', 'n', 'n', 'b', 'w', 'n', 'n', 'n'],
          ['n', 'n', 'n', 'w', 'b', 'n', 'n', 'n'],
          ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
          ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
          ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
]

ban()

print("黒番")

jibun = 'b'
aite = 'w'

while oitakazu < 64:
    okeru = []

    for y2 in range(8):
        for x2 in range(8):

            serch = (y2, x2)
            kekka = []

            # 真ん中
            kekka_mannaka = serch_mannaka(*serch, jibun, aite)  #True:置ける False:置けない

            if kekka_mannaka == True:
                for num in range(8):
                    kekka.append(serch_p(*serch, jibun, aite, num))

            if kekka_mannaka == False:
                continue

            if kekka[0] == True or kekka[1] == True or kekka[2] == True or kekka[3] == True or kekka[4] == True or kekka[5] == True or kekka[6] == True or kekka[7] == True:
                board[y2][x2] = 'a'  #able
                okeru.append((y2,x2))
            else:
                board[y2][x2] = 'd'  #disable

    ban()

    if len(okeru) > 0:
        if jibun == 'b':
            b = kakunin(okeru)
            kimeru = b

        if jibun == 'w':
            kimeru = random.randrange(len(okeru))

        board[okeru[kimeru][0]][okeru[kimeru][1]] = jibun
        oitakazu = oitakazu + 1

        # ひっくり返す場所を探す
        for num in range(8):
            hikkuri_p(num)

        ban()
        ps = 0

    else:
        if ps == 1:
            print("双方パスにて終了") 
            exit()

        if ps == 0:
            ps = 1
            print("パス")

    if jibun == 'b':
        jibun = 'w'
        aite = 'b'
        print("白番")
    else:
        jibun = 'b'
        aite = 'w'
        print("黒番")

    for y2 in range(8):
        for x2 in range(8):
            if board[y2][x2] == 'a' or board[y2][x2] == 'd':
                board[y2][x2]='n'


# 数える
kuro = 0
shiro = 0
for y in range(8):
    for x in range(8):
        if board[y][x] == 'b':
            kuro += 1
        
        if board[y][x] == 'w':
            shiro += 1

print ("黒の数 = " + str(kuro))
print ("白の数 = " + str(shiro))

if shiro>kuro:
    print("白の勝ち")

if kuro>shiro:
    print("黒の勝ち")

if kuro == shiro:
    print("引き分け")

print("終了")
