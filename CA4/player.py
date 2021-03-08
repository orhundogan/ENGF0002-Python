from board import Direction, Rotation
from random import Random


class Player:

    def __init__(self, seed=None):
        self.random = Random(seed)

    def aggregiate_height(self,board):
        agg_height = 0
        for col in range(board.width):
            height = 0
            for row in range(board.height):
                position = (col,row)
                if position in board.cells:
                    height = board.height - row
                    break


            agg_height+=height
        
        return agg_height

    def complete_lines(self,board):
        lines_completed = 0
        for row in range(board.height):
            blocks_present=0
            for col in range(board.width):
                position = (col,row)
                if position in board.cells:
                    blocks_present +=1
            
            if blocks_present == board.width:
                lines_completed += 1

        return lines_completed

    def holes(self,board):
        total_holes = 0
        for col in range(board.width):
            check = False
            for row in range(board.height):
                position = (col,row)
                if position in board.cells:
                    if check == False:
                        check=True
                elif check==True:
                   total_holes+=1 

       
        return total_holes   
        
    def bumpiness(self,board):
        height_list=[]
        for col in range(board.width):
            height = 0
            for row in range(board.height):
                position = (col,row)
                if position in board.cells:
                    height = board.height - row
                    height_list.append(height)
                    break
            if height==0:
                height_list.append(0)
        bump=0
        for i in range(len(height_list)-1):
            diff = abs(height_list[i]-height_list[i+1])
            bump+=diff
        
        return bump
    
    def skorc(self,board):
        a=-0.51
        b=0.76
        c=-0.35
        d=-0.18
        skor = a*self.aggregiate_height(board) + b*self.complete_lines(board) + c*self.holes(board) + d*self.bumpiness(board)
        return skor

    def try_actions(self , board,chosen_action):
        
        skor_list=[]

        if len(chosen_action) ==5:
            for action in self.get_available_actions(board):
                sandbox = board . clone ()
                cacopy = list(chosen_action)
                if action in [Rotation . Anticlockwise, Rotation .Clockwise]:
                    sandbox.rotate(action)
                    sandbox.move(Direction.Drop)
                    cacopy.append(action)
                    cacopy.append(Direction.Drop)
                else: 
                    sandbox.move(action)
                    sandbox.move(Direction.Drop)
                    cacopy.append(action)
                    cacopy.append(Direction.Drop)
                
                skor_list.append([self.skorc(sandbox),cacopy])

            best_skor=skor_list[0][0]
            best_action=[]
            for element in skor_list:
                if element[0] >best_skor:
                    best_skor = element[0]
                    best_action = element[1]
            
            return [best_skor,best_action]

        
        for action in self.get_available_actions(board):
            sandbox = board . clone ()
            sandbox2 = board . clone ()
            cacopy = list(chosen_action)
            cacopy2 = list(chosen_action)
            if action in [Rotation . Anticlockwise, Rotation .Clockwise]:
                sandbox.rotate(action)
                sandbox.move(Direction.Drop)
                cacopy.append(action)
                cacopy.append(Direction.Drop)

                sandbox2.rotate(action)
                cacopy2.append(action)


            else: 
                sandbox.move(action)
                sandbox.move(Direction.Drop)
                cacopy.append(action)
                cacopy.append(Direction.Drop)

                sandbox2.move(action)
                cacopy2.append(action)
            
            skor_list.append([self.skorc(sandbox),cacopy])
            skor_list.append(self.try_actions(sandbox2,cacopy2))

        best_skor=skor_list[0][0]
        best_action=[]
        for element in skor_list:
            if element[0] >best_skor:
                best_skor = element[0]
                best_action = element[1]
        
        return [best_skor,best_action]

    def find_edges(self,cells):
        
        coords=[]
        for position in cells:
            x,y = position
            coords.append(x)
        
        return min(coords), max(coords)


    def choose_action(self, board):
        skor_list=[]
        for rotates in range(0,4):
            init_board=board . clone ()
            int_actions=[]
            for ri in range(0,rotates):
                int_actions.append(Rotation.Clockwise)
                init_board.rotate(Rotation.Clockwise)

            actions=list(int_actions)

            left,right = self.find_edges(init_board.falling.cells)

            sandbox = init_board. clone ()

            actions.append(Direction.Drop)
            sandbox.move(Direction.Drop)

            skor_list.append([self.skorc(sandbox),list(actions)])

            for i in range(1,left+1):
                sandbox = init_board. clone ()
                actions=list(int_actions)
                for ii in range(0,i):
                    actions.append(Direction.Left)
                    sandbox.move(Direction.Left)
                actions.append(Direction.Drop)
                sandbox.move(Direction.Drop)

                skor_list.append([self.skorc(sandbox),list(actions)])

            for i in range(1,board.width-right+1):
                sandbox = init_board. clone ()
                actions=list(int_actions)
                for ii in range(0,i):
                    actions.append(Direction.Right)
                    sandbox.move(Direction.Right)
                actions.append(Direction.Drop)
                sandbox.move(Direction.Drop)

                skor_list.append([self.skorc(sandbox),list(actions)])

        best_skor=skor_list[0][0]
        best_action=skor_list[0][1]
        for element in skor_list:
            if element[0] >best_skor:
                best_skor = element[0]
                best_action = element[1]
        
        return best_action
            



        # sandbox = board . clone ()

        # result = self.try_actions(sandbox,[])

        # actions = list(result[1])
        # actions.append(Direction.Drop)

        # return actions


        #yield Direction.Drop


        #raise NotImplementedError


class RandomPlayer(Player):

    def __init__(self, seed=None):
        self.random = Random(seed)

    def choose_action(self, board):
        return self.random.choice([
            Direction.Left,
            Direction.Right,
            Direction.Down,
            Rotation.Anticlockwise,
            Rotation.Clockwise,
        ])
    

SelectedPlayer = Player

