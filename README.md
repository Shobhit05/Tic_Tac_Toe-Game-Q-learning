# Tic Tac Toe Game Using Q-learning/Reinforcement learning

Requirements:
  1-> Python 2.7

# BackGround

### Q Learning ->
Q-learning is a model-free reinforcement learning technique. It is able to compare the expected utility of the available actions (for a given state) without requiring a model of the environment.

It works by learning an action-value function {\displaystyle Q(s,a)} {\displaystyle Q(s,a)}, which ultimately gives the expected utility of a given action {\displaystyle a} a while in a given state {\displaystyle s} s and following an optimal policy thereafter. A policy {\displaystyle \pi } \pi , is a rule that the agent follows in selecting actions, given the state it is in. When such an action-value function is learned, the optimal policy can be constructed by selecting the action with the highest value in each state.

  
The algorithm, therefore, has a function that calculates the quality of a state-action combination:

{\displaystyle Q:S\times A\to \mathbb {R} } Q:S\times A\to {\mathbb  {R}} .
Before learning begins, {\displaystyle Q} Q is initialized to a possibly arbitrary fixed value (chosen by the programmer). Then, at each time {\displaystyle t} t the agent selects an action {\displaystyle a_{t}} a_{t}, observes a reward {\displaystyle r_{t}} r_{t}, enters a new state {\displaystyle s_{t+1}} s_{t+1} (that may depend on both the previous state {\displaystyle s_{t}} s_{t} and the selected action), and {\displaystyle Q} Q is updated. The core of the algorithm is a simple value iteration update, using the weighted average of the old value and the new information:

{\displaystyle Q(s_{t},a_{t})\leftarrow (1-\alpha )\cdot \underbrace {Q(s_{t},a_{t})} _{\rm {old~value}}+\underbrace {\alpha } _{\rm {learning~rate}}\cdot \overbrace {{\bigg (}\underbrace {r_{t}} _{\rm {reward}}+\underbrace {\gamma } _{\rm {discount~factor}}\cdot \underbrace {\max _{a}Q(s_{t+1},a)} _{\rm {estimate~of~optimal~future~value}}{\bigg )}} ^{\rm {learned~value}}} {\displaystyle Q(s_{t},a_{t})\leftarrow (1-\alpha )\cdot \underbrace {Q(s_{t},a_{t})} _{\rm {old~value}}+\underbrace {\alpha } _{\rm {learning~rate}}\cdot \overbrace {{\bigg (}\underbrace {r_{t}} _{\rm {reward}}+\underbrace {\gamma } _{\rm {discount~factor}}\cdot \underbrace {\max _{a}Q(s_{t+1},a)} _{\rm {estimate~of~optimal~future~value}}{\bigg )}} ^{\rm {learned~value}}}
where {\displaystyle r_{t}} {\displaystyle r_{t}} is the reward observed for the current state {\displaystyle s_{t}} s_{t}, and {\displaystyle \alpha } \alpha  is the learning rate ( {\displaystyle 0<\alpha \leq 1} 0<\alpha \leq 1).

An episode of the algorithm ends when state {\displaystyle s_{t+1}} s_{t+1} is a final or terminal state. However, Q-learning can also learn in non-episodic tasks.[citation needed] If the discount factor is lower than 1, the action values are finite even if the problem can contain infinite loops.

For all final states {\displaystyle s_{f}} s_{f}, {\displaystyle Q(s_{f},a)} Q(s_{f},a) is never updated, but is set to the reward value {\displaystyle r} r observed for state {\displaystyle s_{f}} s_{f}. In most cases, {\displaystyle Q(s_{f},a)} Q(s_{f},a) can be taken to be equal to zero.
  
  
 
