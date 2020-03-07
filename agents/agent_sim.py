from agents.strategy_pool import random_test, simple_rsi, noise
import random


class Agent(object):

    def __init__(self):
        self.balance = 100
        self.order_size = random.randint(1, 5)
        self.strategy = []
        self.name = ''

    def create_order(self, side, qty, **kwargs):
        return {'side': side, 'qty': qty}

    def process_state(self, state):

        if 'rsi' in self.strategy:
            action = simple_rsi(state, 14)
        if 'noise' in self.strategy:
            action = noise(state)
        else:
            action = random_test(state)

        if action == 'buy':
            return self.agent_buy()
        if action == 'sell':
            return self.agent_sell()
        if action == 'pass':
            return self.agent_pass()

    def risk_model(self):
        if self.balance > 0:
            return True

    def set_strategy(self):
        pass

    def agent_buy(self):
        if self.risk_model() is True:
            print('Agent {} wants to buy'.format(self.name))
            return self.create_order(side='buy', qty=self.order_size)

    def agent_sell(self):
        if self.risk_model() is True:
            print('Agent {} wants to sell'.format(self.name))
            return self.create_order(side='sell', qty=self.order_size)

    def agent_pass(self):
        return {}


def create_agents(n_agents):
    # Create agent list
    agent_list = []
    for i in range(n_agents):
        # Create a new_agent var, set it to Agent() Class.
        new_agent = Agent()
        # Set new_agent's name to i.
        new_agent.name = i
        # Add new agent to the list of agent classes.
        agent_list.append(new_agent)

    # Return the agent list
    return agent_list
