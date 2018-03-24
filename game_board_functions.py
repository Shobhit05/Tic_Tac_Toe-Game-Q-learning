import copy

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
            
