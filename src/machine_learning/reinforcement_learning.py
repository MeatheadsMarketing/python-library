import numpy as np

class QLearningAgent:
    """A simple Q-learning agent for reinforcement learning."""
    def __init__(self, state_size, action_size, learning_rate=0.1, discount_factor=0.9):
        self.q_table = np.zeros((state_size, action_size))
        self.lr = learning_rate
        self.gamma = discount_factor

    def update_q_table(self, state, action, reward, next_state):
        """Updates the Q-table based on reward feedback."""
        best_next_action = np.argmax(self.q_table[next_state])
        self.q_table[state, action] += self.lr * (reward + self.gamma * self.q_table[next_state, best_next_action] - self.q_table[state, action])
