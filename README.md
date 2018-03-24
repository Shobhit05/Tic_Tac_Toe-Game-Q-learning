# Tic Tac Toe Game Using Q-learning/Reinforcement learning

### Requirements:</br>
    1-> Python 2.7

# BackGround

## Q Learning ->
Q-learning is a model-free reinforcement learning technique. It is able to compare the expected utility of the available actions (for a given state) without requiring a model of the environment.
It works by learning an action-value function  Q(s,a), which ultimately gives the expected utility of a given action "a" while in a given state "s" and following an optimal policy thereafter.

### Algorithm Used </br>
The problem space consists of an agent, a set of states "S", and a set of actions per state "A". By performing an action  "A", the agent can move from state to state. Executing an action in a specific state provides the agent with a reward. The goal of the agent is to maximize its total (future) reward. It does this by learning which action is optimal for each state. The action that is optimal for each state is the action that has the highest long-term reward.
So to make machine learn in every state,the learning algorithm in each state is defined as 

#### P(s)-> P(s)**(1-learning_rate) + learning_rate**P(s+1) </br>
#### P(s) is the probability of state S
#### Initially P(s) for winning state is 1,for tie state is 0.5,for loosing_state is -1

  
### Learning Rate </br>
The learning rate or step size determines to what extent newly acquired information overrides old information. A factor of 0 makes the agent learn nothing, while a factor of 1 makes the agent consider only the most recent information.In this game I have kept the learning rate as 0.5
