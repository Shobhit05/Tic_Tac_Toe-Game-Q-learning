import copy
import pickle
import random

def convert_number_to_corresponding_state(number):
	arr = [0]*9
	three_pows = [1,3,9,27,81,243,729,2187,6561]
	t = number
	for j in xrange(8, -1, -1):
		arr[j] = t/three_pows[j]
		t = t%three_pows[j]
	p = [arr[8:5:-1], arr[5:2:-1],arr[2::-1]]
	return p

def convert_state_to_corresponding_decimal(state):
	decimal_value = 0
	three_pow = 6561
	for k in range(0, 9):
		i = k/3
		j = k%3
		decimal_value += three_pow * state[i][j]
		three_pow /= 3
	return decimal_value


def valid_state_from_a_given_state(state):
    upcoming_states=[]
    for i in range(0,3):
        for j in range(0,3):
            if state[i][j]==1:
                new_state=copy.deepcopy(state)
                new_state[i][j]=2
                upcoming_states.append(new_state)
                new_state=[]
    return upcoming_states






def initialise_all_states(state_values,winning_states,lossing_states,tie_states):
    for i in xrange(0, 19683):
        state = convert_number_to_corresponding_state(i)
        resp = check_win(state)
        if resp == 2:
            winning_states.append(state)
            state_values[i] = 1
        elif resp == 0:
            lossing_states.append(state)
            state_values[i] = -1
        elif resp == 1:
            tie_states.append(state)
            state_values[i] = 0.5
    
    

def display(board):
        values={0:"O",1:" ",2:"X"}
        print "--------"
        for i in range(0,3):
                for j in range(0,3):
                        print values[board[i][j]]+"|",
                print ""
                print "--------"
        print "\n"
    

def check_win(board):
    #check FOR MACHINE if there is any win
    for i in range(0,3):
        if board[i][0]==2 and board[i][1]==2 and board[i][2]==2:
            return 2
        if board[0][i]==2 and board[1][i]==2 and board[2][i]==2:
            return 2
    if board[0][0]==2 and board[1][1]==2 and board[2][2]==2:
        return 2
    if board[2][0]==2 and board[1][1]==2 and board[0][2]==2:
        return 2
            
    
    #check FOR USER if there is any win 
    for i in range(0,3):
        if board[i][0]==0 and board[i][1]==0 and board[i][2]==0:
            return 0
        if board[0][i]==0 and board[1][i]==0 and board[2][i]==0:
            return 0
        
    if board[0][0]==0 and board[1][1]==0 and board[2][2]==0:
        return 0
    if board[2][0]==0 and board[1][1]==0 and board[0][2]==0:
        return 0

    tie=True
    
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]==1:
                tie=False
                break
    if tie:
        return 1
    else:
        return 3 
            

def main_game():
        learning_rate=0.5
        
        winning_states,lossing_states,tie_states=[],[],[]
        
        state_values=[0]*19683
        try:
                state_num_temp = pickle.load(open('save_game_states.p', 'rb'))		
                state_values = state_num_temp
        except:
                pass
        initialise_all_states(state_values,winning_states,lossing_states,tie_states)
        
        board_initial_state=[[1,1,1],[1,1,1],[1,1,1]]
        current_state=copy.deepcopy(board_initial_state)
        initial=True
        while True:
                print sum(state_values)
                pickle.dump(state_values, open('save_game_states.p', 'wb'))
                if current_state in winning_states or current_state in lossing_states:
                        next_states=[board_initial_state]
                else:
                        next_states=valid_state_from_a_given_state(current_state)
                worst_case=-1
                if initial:
                        initial=False
                        upcoming_state=copy.deepcopy(random.choice(next_states))
                else:
                        for states in next_states:
                                curr_state_value=state_values[convert_state_to_corresponding_decimal(states)]
                                if curr_state_value>worst_case:
                                        worst_case=curr_state_value
                                        try:
                                                upcoming_state[:]=[]
                                        except:
                                                pass
                                        upcoming_state=copy.deepcopy(states)
                        
        

                if upcoming_state==board_initial_state:
                        current_state=copy.deepcopy(board_initial_state)
                        print "returning to Initial State"
                        continue
                score_of_curr_state=state_values[convert_state_to_corresponding_decimal(upcoming_state)]
                state_values[convert_state_to_corresponding_decimal(current_state)]=(1-learning_rate)*(state_values[convert_state_to_corresponding_decimal(current_state)])+learning_rate*score_of_curr_state
                current_state[:]=[]
                current_state=copy.deepcopy(upcoming_state)
                display(current_state)
                if current_state in winning_states:
                        print "The Machine has Won the Game"
                        initial=True
                        current_state[:]=[]
                        upcoming_state[:]=[]
                        current_state=copy.deepcopy(board_initial_state)
                        end_value=raw_input("Press X to shutdown the Game")
                        
                        if end_value=="X":
                                exit(0)
                        else:
                                continue
                        
                if current_state in lossing_states:
                        initial=True
                        print "The Machine has lost the Game"
                        current_state[:]=[]
                        upcoming_state[:]=[]
                        current_state=copy.deepcopy(board_initial_state)
                        end_value=raw_input("Press X to shutdown the Game")
                        if end_value=="X":
                                exit(0)
                        else:
                                continue
                if current_state in tie_states:
                        initial=True
                        print "The Game is Tied"
                        current_state[:]=[]
                        upcoming_state[:]=[]
                        current_state=copy.deepcopy(board_initial_state)
                        end_value=raw_input("Press X to shutdown the Game")
                        if end_value=="X":
                                exit(0)
                        else:
                                continue
                while True:
                        try:
                                s=int(input("Enter the square number starting from 0 to 9\t"))
                                if current_state[s/3][s%3]!=1:
                                        print "The value you entered is already been occupied"
                                        
                                else:
                                        prev_state=copy.deepcopy(current_state)
                                        current_state[s/3][s%3]=0
                                        break
                        except:
                                print("Please enter Right format input")

                display(current_state)
                score_of_curr_state=state_values[convert_state_to_corresponding_decimal(current_state)]
                state_values[convert_state_to_corresponding_decimal(prev_state)]=(1-learning_rate)*(state_values[convert_state_to_corresponding_decimal(prev_state)])+learning_rate*score_of_curr_state
                if current_state in lossing_states:
                        initial=True
                        print "The Machine has lost the Game"
                        current_state[:]=[]
                        upcoming_state[:]=[]
                        current_state=copy.deepcopy(board_initial_state)
                        end_value=raw_input("Press X to shutdown the Game")
                        if end_value=="X":
                                exit(0)
                        else:
                                continue
                if current_state in tie_states:
                        initial=True
                        print "The Game is Tied"
                        current_state[:]=[]
                        upcoming_state[:]=[]
                        current_state=copy.deepcopy(board_initial_state)
                        end_value=raw_input("Press X to shutdown the Game")
                        if end_value=="X":
                                exit(0)
                        else:
                                continue
        
        
        

if __name__=="__main__":
        main_game()

        
