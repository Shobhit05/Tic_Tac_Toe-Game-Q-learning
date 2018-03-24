import copy
import pickle
import random
from game_board_functions import *

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

        
