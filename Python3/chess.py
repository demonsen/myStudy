
import readline

''' 要堵的位置
deny_xy = [
    [ ['X',' ','X','X','X'],[1] ],
    [ ['X','X','X',' ','X'],[3] ],
    [ ['X','X','X','X',' '],[4] ],
    [ [' ','X','X','X','X'],[0] ],
    [ ['X',' ','X',' ','X',' ','X'],[3] ],
    
    [ [' ','X','X','X',' '],[0,4] ],
    [ ['X',' ','X','X',' '],[1,4] ],
    [ [' ','X','X',' ','X'],[0,3] ],
    [ ['X',' ','X',' ','X'],[1,3] ],
    [ [' ','X',' ','X',' '],[2,0,4] ],
    [ [' ','X','X',' '],[0,3] ],
]



deny_xy_high = [
    [ '10111', [1] ],
    [ '11101', [3] ],
    [ '11110', [4] ],
    [ '01111', [0] ],
    [ '1010101', [3] ],
    ]

deny_xy_low = [
    [ '01110', [0,4] ],
    [ '10110', [1,4] ],
    [ '01101', [0,3] ],
    [ '10101', [1,3] ],
    [ '01010', [2,0,4] ],
    [ '0110', [0,3] ],
]
'''

class chess():
    def __init__(self):
        self.map_max = 19
        self.chk = 5
        self.map = [[ ' ' for x in range(self.map_max)] for y in range(self.map_max)]
    # 打印棋盘
    def show_map(self):
        for y in range(self.map_max):
            for x in range(self.map_max):
                print(self.map[y][x],end='|')
            print()
    # 检查棋子是否在棋盘中
    def chk_pos(self, x, y, map_max = 19):
        if x < 0 or y < 0 or x >= map_max or y >= map_max:
            return False
        else:
            return True
    # 检查是否可以落子
    def chk_chess(self, x, y, chess):
        if self.map[y][x] == chess:
            return True
        else:
            return False
    # 检查棋子连续
    def chk_sum(self, x, y, chess, chk = 5, sum = 5):
        n = [ i for i in range(1 - chk, chk)]
        # 竖
        #[(pos_x - 5 , pos_x + 5), pos_y]
        count = 0
        for i in range(len(n)):
            if self.chk_pos(x + n[i] ,y):
                if self.chk_chess(x + n[i] ,y, chess):
                    count += 1
                    if count == sum:
                        return True
                        break
                else:
                    count = 0
        # 横
        #[pos_x , (pos_y - 5 , pos_y + 5)]
        count = 0
        for i in range(len(n)):
            if self.chk_pos(x, y + n[i]):
                if self.chk_chess(x, y + n[i], chess):
                    count += 1
                    if count == sum:
                        return True
                        break
                else:
                    count = 0
        # 斜 \  
        #  0,0    1,1    2,2   3,3  4,4  5,5  6,6
        # -3,-3  -2,-2  -1,-1  0,0  1,1  2,2  3,3
        #[(pos_x - 5 , pos_x + 5) ,(pos_y - 5 , pos_y + 5)]
        count = 0
        for i in range(len(n)):
            if self.chk_pos(x + n[i], y + n[i]):
                if self.chk_chess(x + n[i], y + n[i], chess):
                    count += 1
                    if count == sum:
                        return True
                        break
                else:
                    count = 0
        # 斜 /  
        #  0,6   1,5   2,4  3,3  4,2   5,1   6,0 
        # -3,3  -2,2  -1,1  0,0  1,-1  2,-2  3,-3
        #[(pos_x - 5 , pos_x + 5) ,(pos_y + 5, pos_y - 5) ]      
        count = 0
        for i in range(len(n)):
            if self.chk_pos(x + n[i], y - n[i]):
                if self.chk_chess(x + n[i], y - n[i], chess):
                    count += 1
                    if count == sum:
                        return True
                        break
                else:
                    count = 0
        return False
    # 获取落子点棋子连续列表
    def get_chess_list(self, x, y, chk = 5):
        # n = [ i for i in range(1 - chk, chk)]  chk=5 [-4, -3, -2, -1, 0, 1, 2, 3, 4]
        # 获取落子点范围内的棋子情况
        chess_list = ['','','','']
        chess_list_xy = [[],[],[],[]]
        for i in range(1 - chk, chk):
            # 坐标：
            #  0,0   1,0   2,0  3,0
            #  0,1   1,1   2,1  3,1
            #  0,2   1,2   2,2  3,2
            #  0,3   1,3   2,3  3,3
            # 横
            #[(pos_x - 5 , pos_x + 5), pos_y]
            if self.chk_pos(x + i ,y):
                chess_list[0] += self.map[y][x + i]
                chess_list_xy[0].append((x + i,y))
            # 竖
            #[pos_x , (pos_y - 5 , pos_y + 5)]
            if self.chk_pos(x, y + i):
                chess_list[1] += self.map[y + i][x]
                chess_list_xy[1].append((x, y + i))
            # 斜 \
            #  0,0    1,1    2,2   3,3  4,4  5,5  6,6
            # -3,-3  -2,-2  -1,-1  0,0  1,1  2,2  3,3
            #[(pos_x - 5 , pos_x + 5) ,(pos_y - 5 , pos_y + 5)]
            if self.chk_pos(x + i, y + i):
                chess_list[2] += self.map[y + i][x + i]
                chess_list_xy[2].append((x + i, y + i))
            # 斜 /
            #  0,6   1,5   2,4  3,3  4,2   5,1   6,0 
            # -3,3  -2,2  -1,1  0,0  1,-1  2,-2  3,-3
            #[(pos_x - 5 , pos_x + 5) ,(pos_y + 5, pos_y - 5) ]
            if self.chk_pos(x + i, y - i):
                chess_list[3] += self.map[y - i][x + i]
                chess_list_xy[3].append((x + i, y - i))
        print(chess_list)
        print(chess_list_xy)
        return chess_list,chess_list_xy
        
    # 检查棋子连续情况
    def chk_chess_sum(self, x, y, chess, chk = 5, sum = 5):
        chess_list, chess_list_xy = self.get_chess_list(x,y,chk)
        
        deny_xy = [
            [ 'X XXX', [1] ],
            [ 'XXX X', [3] ],
            [ 'XXXX ', [4] ],
            [ ' XXXX', [0] ],
            [ 'X X X X', [3] ],
            
            [ ' XXX ', [0,4] ],
            [ ' X XX ', [0,2,5] ],
            [ ' XX X ', [0,3,5] ],
            
            [ 'X XX ', [1,4] ],
            [ ' XX X', [0,3] ],
            [ 'X X X', [1,3] ],
            [ ' X X ', [2,0,4] ],
            [ ' XX ', [0,3] ],
        ]
    
        # 检查棋子连续情况，是否要堵
        for ls_num in range(len(chess_list)):
            ls_len = len(chess_list[ls_num])
            if ls_len > 4:
                ls = chess_list[ls_num]
                #print(ls)
                for deny in deny_xy:
                    deny_len = len(deny[0])
                    if ls_len >= deny_len:
                        D = deny[0].replace('X',chess)
                        for i in range(ls_len - deny_len + 1):
                            #print(ls[i:i+deny_len])
                            if ls[i:i+deny_len] == D:
                                res = i + deny[1][0]
                                print(res)
                                print(chess_list_xy[ls_num][res])

    # 落子
    def set_chess(self, x, y, chess):
        if self.chk_pos(x, y):
            if self.chk_chess(x, y, ' '):
                self.map[y][x] = chess
                return True
            else:
                print('位置(%d,%d)处有棋子，请选择空位！' % (x, y) )
                return False
        else:
            print('超出棋盘范围！')
            return False
#    def get_pos(self):
#        
    # MAIN
    def main(self):
        chess = 'X'
        while True:
            try:
                pos_input = input('请输入棋子(%s)坐标(x,y)：' % chess).strip().lower()
                #print(pos_input)
                if pos_input == 'quit' or pos_input == 'exit' or pos_input == 'q':
                    print('退出')
                    break
                x,y = pos_input.split(',')
                x,y = int(x),int(y)
            except KeyboardInterrupt:
                print('退出')
                exit()
            except:
                print('请输入棋子坐标(x,y)错误！')
            else:
                Done = self.set_chess(x,y,chess)
                if Done:
                    self.show_map()
                    win = self.chk_sum(x,y,chess)
                    self.chk_chess_sum(x,y,chess)
                    if win:
                        print('-- %s win!' % chess)
                    else:
                        if chess == 'X':
                            chess = 'O'
                        else:
                            chess = 'X'
a = chess()
a.main()





